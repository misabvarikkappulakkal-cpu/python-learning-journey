# 🎯 Goal

Build a command-line password manager using Python.

The application stores:
- Account names
- Passwords

Users can:
- Add accounts
- View saved accounts
- Search passwords
- Delete accounts

---

# 🧠 Concepts Used

| Concept | Purpose |
|---|---|
| Dictionary | Store account-password pairs |
| while loop | Keep app running |
| if/elif/else | Menu handling |
| input() | User interaction |
| del | Delete dictionary entry |
| in keyword | Search dictionary |

---

# 📦 Important Python Concepts

## Dictionary

```python
passwords = {}
```

Stores data like:

```python
{
    "gmail": "mypassword123",
    "github": "secret456"
}
```

---

## Add Data

```python
passwords[account] = password
```

Adds new account and password.

---

## Search Data

```python
if account in passwords:
```

Checks whether account exists.

---

## Delete Data

```python
del passwords[account]
```

Removes account from dictionary.

---

# ⚠️ Important Security Note

This beginner project stores passwords in plain text.

Real password managers use:
- Encryption
- Hashing
- Databases
- Authentication systems

This project is for learning programming concepts only.

Never store real sensitive passwords inside beginner scripts.

---

# 🧠 Why This Project Matters

This project teaches:
- Data structures
- Interactive CLI apps
- Information storage
- Search operations
