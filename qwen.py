from transformers import AutoModelForCausalLM, AutoTokenizer
import time
import psutil


def runqwen(prompt_request):
    start_time = time.time()

    device = "cpu"

    model = AutoModelForCausalLM.from_pretrained(
        "Qwen/Qwen2-0.5B-Instruct",
        torch_dtype="auto",
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-0.5B-Instruct")
    
    prompt = prompt_request
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    
    response = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    model_inputs = tokenizer([response], return_tensors="pt")
    
    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=512
    )
 
 
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    
    generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    end_time = time.time()

    total_time = end_time - start_time
    print(f"the Time taken to generate the response was", {total_time})


    print(f"Generated Response: {generated_text}")
    cpu_usage= psutil.cpu_percent(interval=1)
    print(cpu_usage)
    memory_usage=psutil.virtual_memory()
    print(memory_usage)

    return(generated_text, total_time, cpu_usage, memory_usage)