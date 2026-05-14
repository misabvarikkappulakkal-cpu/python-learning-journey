# Web Basics in Python
# Topics:
# 1. HTTP GET request
# 2. JSON handling
# 3. Status codes
# 4. Headers
# 5. Simple API usage

import requests
print("Web Basics in Python")

# Making a GET request

url = "https://jsonplaceholder.typicode.com/posts/1"

# 1. HTTP GET request

response = requests.get(url)

print("\nStatus Code:", response.status_code)
print("\nHeaders:", response.headers)
print("\nResponse Text:", response.text)

# 2. JSON handling

data = response.json()

print("\nJSON Data:", data)

print("Title from JSON:", data['title'])

# Checking Successful Response

if response.status_code == 200:
    print("\nRequest Successful!")
else:    print("\nRequest Failed")

# 3. Status codes

print("Status Code:", response.status_code)

# 4. Headers

print("Content-Type:", response.headers['Content-Type'])

# 5. Simple API usage

response = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = response.json()
print("Number of posts:", len(posts))
print("First post title:", posts[0]['title'])

