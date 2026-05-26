# 🧪 Pract# 1️⃣ Practice Dictionaries

```python
accounts = {
    "gmail": "12345",
    "github": "abcde"
}

print(accounts)
```

Run:

```bash
python3 practice.py
```

---

# 2️⃣ Access Dictionary Values

```python
print(accounts["gmail"])
```

---

# 3️⃣ Add New Entry

```python
accounts["instagram"] = "instapass"

print(accounts)
```

---

# 4️⃣ Delete Entry

```python
del accounts["github"]

print(accounts)
```

---

# 5️⃣ Check Key Exists

```python
if "gmail" in accounts:
    print("Found")
```

---

# 6️⃣ Practice Loops

```python
for account in accounts:
    print(account)
```

---

# 7️⃣ Practice User Input

```python
site = input("Enter website: ")

print(site)
```

---

# 8️⃣ Build Mini Version Yourself

Try creating:
- Dictionary storage
- Add account feature
- Search feature

WITHOUT copying full project code.

---

# 🎯 Challenge Upgrade

Modify app to:
- Prevent duplicate accounts
- Show total saved accounts
- Confirm before deleting
- Hide passwords while typing

Hint:
Research:
```python
getpass
```

---

# 🧠 Self Check

Can you:
- Use dictionaries?
- Store key-value data?
- Search information?
- Build menu-based apps?
- Handle user input?
