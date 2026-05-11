# Virtual Environment in Python

A virtual environment is an isolated Python environment used for project-specific packages.

It helps to:
- Avoid package conflicts
- Keep project dependencies organized
- Install packages separately for each project

---

# Project Location

```powershell
C:\Users\hp\python-learning-journey\basics\day14_VirtualEnvironment
```

---

# Project Structure

```text
day14_VirtualEnvironment/
├── venv/
├── .gitignore
├── requirements.txt
└── day14_VirtualEnvironment.py
```

---

# Create Virtual Environment

```powershell
python -m venv venv
```

This creates an isolated Python environment inside the `venv/` folder.

---

# Activate Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

After activation:

```powershell
(venv) PS C:\Users\hp\python-learning-journey\basics\day14_VirtualEnvironment>
```

The `(venv)` indicates the virtual environment is active.

---

# Install requests Package

```powershell
pip install requests
```

The package is installed only inside the virtual environment.

---

# Python Script

## day14_VirtualEnvironment.py

```python
import requests

response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)
print(response.json())
```

The script sends a GET request to the GitHub API and prints the response data.

---

# Run Python Script

```powershell
python day14_VirtualEnvironment.py
```

Output:

```text
Status Code: 200
```

This confirms the API request was successful.

---

# Save Installed Packages

```powershell
pip freeze > requirements.txt
```

This stores installed package versions inside `requirements.txt`.

---

# .gitignore

```gitignore
venv/
__pycache__/
```

Used to prevent unnecessary files from being uploaded to GitHub.

---

# Deactivate Virtual Environment

```powershell
deactivate
```

This exits the virtual environment. 