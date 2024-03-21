
# fast-scaff
A Rapid FastAPI Project Scaffolding Tool

Fast-Scaff simplifies the FastAPI project setup, focusing on efficient and quick generation of a robust project structure. While transitioning from a CLI tool, Fast-Scaff continues to support developers by preparing the necessary groundwork for FastAPI applications, ensuring a smooth start to building your application.

## Features

- Provides a template for a comprehensive directory structure tailored for FastAPI projects, including a README.md in each directory with a brief description of its purpose.
- Recommends a setup for creating a Python virtual environment and managing dependencies.
- Suggests a Git repository structure for an initial commit and future project expansion.
- Designed for ease of use, supporting developers in adhering to best practices in FastAPI development.

## Getting Started

### Prerequisites

- Python 3.7+ 
- Git

### Setup Guide

1. **Clone the Fast-Scaff repository** to get the latest version of the project scaffold:

   `git clone https://github.com/ederwii/fast-scaff.git`

2. **Navigate to the project directory**:

   `cd fast-scaff`

3. **Run Fast-Scaff**: Follow the instructions in `main.py` to customize and use the scaffolding for your FastAPI project.

### Project Structure

Using Fast-Scaff, you'll find a well-organized starting point for your FastAPI project, including:

- An `/app` directory for your application code.
- A `/tests` directory set up for writing test cases.
- A `requirements.txt` file to manage project dependencies.
- An `.env` sample file for environment variable management.
- A structured approach that conforms to FastAPI development best practices.

### How to Use

1. **Ensure Python and Git Are Installed**: Before you begin, make sure Python 3.7 or higher and Git are installed on your system.

2. **Download Fast-Scaff**: Clone the Fast-Scaff repository or download the `main.py` script directly to your local machine.

   `git clone https://github.com/ederwii/fast-scaff.git`

   Or, if downloading directly:

   `wget https://raw.githubusercontent.com/ederwii/fast-scaff/main/main.py`

3. **Run Fast-Scaff**: Navigate to the directory containing `main.py` and run the script with Python. The script will prompt you for the name of your new FastAPI project.

   `cd path/to/fast-scaff`

   `python main.py`

   When prompted, enter the desired name of your FastAPI project:

   `Enter the name of your FastAPI project: your_project_name`

4. **Next Steps**: Fast-Scaff will automatically create a project directory and structure, including initial files. Remember to install `uvicorn` with `pip install uvicorn` if you plan to run the FastAPI app with Uvicorn.

5. **Activate the Virtual Environment** and start developing your FastAPI application. Run your application with:

   `python -m uvicorn main:app --reload`

Fast-Scaff is designed to give you a head start in FastAPI development by setting up a structured project environment, allowing you to dive straight into building your application.

## Contributing

We welcome contributions! If you have suggestions for improving Fast-Scaff, please feel free to open an issue or submit a pull request.

## License

This project is distributed under the MIT License - see the `LICENSE` file for details.

## Author

Alan Martinez - ederalan@me.com

## Acknowledgments

- Thanks to the FastAPI community for providing the inspiration for project structure and setup.
- Appreciation to OpenAI for their documentation and API guidelines, which have informed some of the best practices incorporated into Fast-Scaff.
