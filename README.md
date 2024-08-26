# Qwen LLM

A sample API that allows interaction with a small LLM.

# Table of Contents
- [Qwen LLM](#qwen-llm)
- [Table of Contents](#table-of-contents)
- [Getting Started](#getting-started)
- [Development](#development)
- [Setup](#setup)
- [Usage](#usage)
- [Known Issues](#known-issues)

# Getting Started

- Please base all your contributions to the `development` branch.
- For any doubts or concerns, please reach out to sreekar.achanta@ispace.com or abhyuday.vatsavai@ispace.com
- Please follow the guidlines in the Developement section.
- Please refer to the Setup section to set up the application.

# Development
For a quick refresher on Git and GitLab watch [this video](https://www.youtube.com/watch?v=4lxvVj7wlZw)

The practices below are expected to be followed:
- Make sure not to commit your virtual environment (`venv`) to the main branch include it in your `.gitignore`.
- The package manager being used is the standard pip.
- when running your code make sure you are using the python interpreter that pertains to your virtual environment, because that is where your installed packages will be.
- Make sure to create a branch and make changes to that branch instead of commiting directly to main to avoid breaking the code for everyone who pulls the code from the repository.
- Commit Conventions: Refer to the [following resource](https://www.conventionalcommits.org/en/v1.0.0-beta.2/) on how to author commit messages to enable certain CI/CD features. Please keep the commit messages clean and informative.
- Do not commit build artifacts or __pycache__ folders: Make sure to add them to the .gitignore file.
- Use make: For all repetitive tasks, use the Makefile to create shortcuts for the same. This will help in maintaining a clean and consistent development environment.
- DO NOT commit sensitive information, this includes API Keys, passwords and any documents with PHI.
- As of now this program works assuming you are using a Windows system, therefore using VSCode is recommended so you have access to command prompt. 

# Setup

Virtual Environment and Dependencies:
1. Using command prompt create your virtual environment using the command `python -m venv /path/to/new/virtual/environment`
2. Using command prompt, activate your virtual environment using the command: `<venv>\Scripts\activate.bat`
3. Now that we are in the virtual environment make sure you install all the packages that are listed in `requirements.txt` using `pip`

Postman:
1. To install Postman go to [here](https://www.postman.com/downloads/) and install the program based on the OS you are using.
2. After installation you will want to create a Postman account as well for that go [here](https://identity.getpostman.com/signup/)

PostgreSQL and PGAdmin:
1. First install PostgreSQL by going [here](https://www.postgresql.org/download/)
2. Then in order to visualize your data and set up a local postgres server download pgadmin by going [here](https://www.pgadmin.org/download/)
3. To connect to the database with your code go to `database.py` and set `SQLALCHEMY_DATABASE_URL` to be equal to `'postgresql://username:password@localhost/fastapi'`


# Usage
1. In the VSCode command prompt go ahead and run the command `<venv>\Scripts\activate.bat` to enter your virtual environment.
2. Then start the FastAPI server using the command `fastapi run` or you can use `fastapi dev main.py`
3. With that the fastapi server should be up and running.
4. Then go into pgadmin and start up your local postgres server.
5. With that your local database and fastapi server should be running.
6. To interact with the LLM using HTTP requests use the endpoint `http://127.0.0.1:8000/qwen` and type in your type in your request in [json format.](https://www.w3schools.com/js/js_json_intro.asp)
7. After a few minutes the LLMs response should be shown as the HTTP response in Postman.

# Known Issues
1. If you use a request that is already in the database but not in the cache, you will get an error telling you the same request is already in the database.