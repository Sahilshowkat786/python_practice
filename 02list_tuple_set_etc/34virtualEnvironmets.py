# # ================================
# # PYTHON + VIRTUAL ENVIRONMENT
# # ================================

# # Check Python version
# python --version

# # Check pip version
# pip --version

# # Check which Python is being used
# where python

# # Check which pip is being used
# where pip


# # ================================
# # CREATE VIRTUAL ENVIRONMENT
# # ================================

# # Create virtual environment named "venv"
# python -m venv venv

# # Or create one named ".venv"
# python -m venv .venv


# # ================================
# # ACTIVATE VIRTUAL ENVIRONMENT
# # ================================

# # Windows CMD
# venv\Scripts\activate

# # Windows PowerShell
# venv\Scripts\Activate.ps1

# # macOS / Linux
# source venv/bin/activate


# # ================================
# # DEACTIVATE
# # ================================

# deactivate


# # ================================
# # PIP / PACKAGE COMMANDS
# # ================================

# # Install a package
# pip install flask

# # Install multiple packages
# pip install flask requests pandas

# # Install a specific version
# pip install flask==3.1.2

# # Upgrade a package
# pip install --upgrade flask

# # Uninstall a package
# pip uninstall flask

# # Show all installed packages
# pip list

# # Show information about a package
# pip show flask

# # Check outdated packages
# pip list --outdated


# # ================================
# # REQUIREMENTS.TXT
# # ================================

# # Create requirements.txt
# pip freeze > requirements.txt

# # View requirements.txt
# type requirements.txt

# # Install packages from requirements.txt
# pip install -r requirements.txt

# # Upgrade packages using requirements.txt
# pip install -r requirements.txt --upgrade


# # ================================
# # GITIGNORE
# # ================================

# # Add these to .gitignore
# venv/
# .venv/


# # ================================
# # COMPLETE PROJECT WORKFLOW
# # ================================

# # Create project folder
# mkdir myproject

# # Enter project
# cd myproject

# # Create virtual environment
# python -m venv venv

# # Activate it
# venv\Scripts\activate

# # Install packages
# pip install flask requests pandas

# # Create requirements.txt
# pip freeze > requirements.txt

# # Run your Python program
# python app.py

# # Deactivate when finished
# deactivate