import os
import sys
import time
from pathlib import Path
import subprocess

def type_print(text, delay=0.01):
    """Prints text to the console, simulating typing."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

def create_directories(project_name):
    type_print("Creating project directories...")
    directories = {
        f"{project_name}/app/api/v1/endpoints": "Contains endpoint definitions for version 1 of the API.",
        f"{project_name}/app/core": "Core settings and configuration files.",
        f"{project_name}/app/crud": "CRUD operations interfacing the database.",
        f"{project_name}/app/db": "Database models and session management.",
        f"{project_name}/app/models": "ORM models defining the database schema.",
        f"{project_name}/app/schemas": "Pydantic models for request and response validation.",
        f"{project_name}/app/services": "Business logic and service layer.",
        f"{project_name}/app/utils": "Utility functions and helper classes.",
        f"{project_name}/migrations": "Database migration scripts.",
        f"{project_name}/tests/api": "Tests for the API endpoints.",
        f"{project_name}/tests/db": "Tests for database operations.",
    }

    for directory, description in directories.items():
        Path(directory).mkdir(parents=True, exist_ok=True)
        readme_path = Path(directory) / "README.md"
        with readme_path.open('w') as f:
            f.write(f"# {directory.split('/')[-1]}\n\n{description}\n")
    type_print("Directories and README.md files created successfully.")

def create_files(project_name):
    type_print("Creating initial project files...")
    files = {
        f"{project_name}/app/__init__.py": "#__init__ file for app module.",
        f"{project_name}/app/main.py": "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/')\ndef read_root():\n    return {'Hello': 'World'}",
        f"{project_name}/requirements.txt": "fastapi\nuvicorn",
        f"{project_name}/.env": "SECRET_KEY=your_secret_key_here",
        f"{project_name}/README.md": f"# {project_name}\nThis is a FastAPI project.",
    }

    for file_path, file_content in files.items():
        with open(file_path, 'w') as f:
            f.write(file_content)
    type_print("Files created successfully.")

def setup_virtual_env(project_path):
    type_print("Setting up the virtual environment...")
    os.system(f'python -m venv "{project_path}/venv"')
    
    pip_path = "bin/pip" if sys.platform != "win32" else "Scripts\\pip"
    requirements_path = f"{project_path}/requirements.txt"
    
    type_print("Installing dependencies...")
    subprocess.run([f"{project_path}/venv/{pip_path}", "install", "-r", requirements_path], check=True)
    
    type_print("Virtual environment created and dependencies installed.")

def init_git(project_path):
    type_print("Initializing Git repository...")
    os.system(f'cd {project_path} && git init && git add . && git commit -m "Initial commit"')
    type_print("Git repository initialized successfully.")

def main():
    project_name = input("Enter the name of your FastAPI project: ")
    type_print(f"Starting the setup for {project_name}...", delay=0.05)
    create_directories(project_name)
    create_files(project_name)
    setup_virtual_env(project_name)
    init_git(project_name)
    type_print(f"FastAPI project '{project_name}' has been created with a basic structure and is ready for development!")

if __name__ == "__main__":
    main()
