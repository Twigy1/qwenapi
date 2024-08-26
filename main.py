from fastapi import FastAPI, Response, status, HTTPException, Depends, Request 
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import psycopg2 
from psycopg2.extras import RealDictCursor 
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session
from .qwen import runqwen
import torch
import asyncio
import aioredis
import redis.asyncio as redis
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.backends.memcached import MemcachedBackend
from fastapi_cache.decorator import cache
from pymemcache.client.base import Client
import time
import psutil

models.Base.metadata.create_all(bind=engine)

cache_dict ={}
 
app = FastAPI()
 
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

def cache_hit(request):
 
 try:
    cache_found = cache_dict[Request]
 except:
     return False
 if cache_found:
  return True
 return False

class Query(BaseModel):
    query: str
 
@app.on_event("startup")
async def startup():
    Client = redis.Redis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache") # type: ignore

 
@app.get("/")
@cache(expire=60)
def root():
    return{"message", "Hello World"}
 
@app.get("/posts")
@cache(expire=60)
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}
 
@app.post("/posts")
def create_posts(post: Post, db: Session = Depends(get_db)):
    new_post = models.Post(title = post.title, content = post.content, published = post.published)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return{"data": new_post}

@app.post("/qwen")
def create_qwen(query: Query, db: Session = Depends(get_db)):
    start =time.time()
    print("Request", query)
    cache = cache_hit(query.query)
    if cache == True:
        cpu_usage = psutil.virtual_memory()
        end = time.time()
        total_time = end - start
        qwen_result = runqwen(query.query)
        return{"llm statement": qwen_result[0], "Time_taken": qwen_result[1], "cpu_usage": qwen_result[2], "memory_usage": qwen_result[3]}
    
    else:
         qwen_result = runqwen(query.query)
         new_result = models.LLM(query=query.query, llm_statement=qwen_result[0], time_taken=qwen_result[1], cpu_usage=qwen_result[2], memory_usage=qwen_result[3][2])
         cache_dict[query.query] = qwen_result[0]
         print(cache_dict)
         db.add(new_result)
    db.commit()
    db.refresh(new_result)
    return new_result


@app.get("/qwen$query={query}")
@cache(expire=60)
def create_qwen(query: str):
    print("Request", query)
    qwen_result = runqwen(query)
    return{"llm statement": qwen_result[0], "Time_taken": qwen_result[1], "cpu_usage": qwen_result[2], "memory_usage": qwen_result[3]}


