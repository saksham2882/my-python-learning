# Demonstrates commands for creating and managing virtual environments in Python

# Virtual environments isolate project-specific packages, avoiding conflicts with global installations

# Create a virtual environment named 'myenv':
# python -m venv myenv

# Activate the virtual environment:
# On Linux/Mac: source myenv/bin/activate
# On Windows (Command Prompt): myenv\Scripts\activate.bat
# On Windows (PowerShell): myenv\Scripts\Activate.ps1

# Deactivate the virtual environment:
# deactivate

# Save installed packages to a file:
# pip freeze > requirements.txt

# Install packages from requirements.txt:
# pip install -r requirements.txt