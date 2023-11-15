# Django OTP Login

A Django project for implementing OTP (One-Time Password) generation for secure user login with SQLite database backend.

## Table of Contents

- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Requirements](#requirements)

## Installation

Ensure you have Python and pip installed on your system. Create and activate a virtual environment to keep your project dependencies isolated.

```bash
# Create a virtual environment (Linux/macOS)
python3 -m venv venv

# Activate the virtual environment (Linux/macOS)
source venv/bin/activate

# Create a virtual environment (Windows)
python -m venv venv

# Activate the virtual environment (Windows)
.\venv\Scripts\activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

Before running the project, apply migrations to set up the SQLite database:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser to view the project.

## Requirements

Ensure your system meets the following prerequisites:

### For All Operating Systems:

- Python (version 3.6 or higher)
- Django (version 3.0 or higher)
- django-otp (for OTP generation)
- Pillow (for image handling, if applicable)


<hr><hr>

## Happy Codding 💻💻🖥🖥⌨⌨⌨
