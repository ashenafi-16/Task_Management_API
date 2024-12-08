# TaskManager Django Project

## Overview
This project is a Django-based application for managing tasks. It includes:
- A virtual environment for isolating dependencies.
- A Django project named **TaskManager**.
- An app named **tasks**.

---

## Prerequisites
Before setting up the project, ensure you have the following installed:
- Python 3.x
- pip (Python package manager)
- Git

---

## Setup Instructions


### 1. Set Up the Virtual Environment
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

---

### 2. Install Dependencies
Install Django and other necessary packages:
```bash
pip install django
```

---

### 3. Create and Configure the Project
1. Create the Django project:
   ```bash
   django-admin startproject TaskManager .
   ```

2. Create the app named **tasks**:
   ```bash
   python manage.py startapp tasks
   ```

---

## File Structure
Here’s the structure of the project:
```
TaskManager/
├── TaskManager/           # The project directory
├── venv/                  # Virtual environment
├── .gitignore             # Git ignore file
└── README.md              # Project setup instructions
```

---
