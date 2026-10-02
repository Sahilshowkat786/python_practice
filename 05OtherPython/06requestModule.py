# ============================================================
# requests MODULE IN PYTHON
# ============================================================

# Install first:
# pip install requests

import requests


# ============================================================
# 1. GET REQUEST
# ============================================================

response = requests.get("https://example.com")

print(response)


# ============================================================
# 2. STATUS CODE
# ============================================================

print("Status Code:", response.status_code)


# ============================================================
# 3. RESPONSE TEXT
# ============================================================

print(response.text)


# ============================================================
# 4. RESPONSE CONTENT
# ============================================================

print(response.content)


# ============================================================
# 5. RESPONSE HEADERS
# ============================================================

print(response.headers)


# ============================================================
# 6. RESPONSE URL
# ============================================================

print(response.url)


# ============================================================
# 7. GET JSON DATA FROM API
# ============================================================

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

print(data)


# ============================================================
# 8. PRINT DATA FROM JSON
# ============================================================

for user in data:
    print(user["name"])
    print(user["email"])
    print()


# ============================================================
# 9. GET REQUEST WITH PARAMETERS
# ============================================================

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

response = requests.get(url, params=params)

print(response.url)
print(response.json())


# ============================================================
# 10. HEADERS
# ============================================================

headers = {
    "User-Agent": "Python Requests"
}

response = requests.get(
    "https://example.com",
    headers=headers
)

print(response.status_code)


# ============================================================
# 11. POST REQUEST
# ============================================================

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Python",
    "body": "Learning requests module",
    "userId": 1
}

response = requests.post(
    url,
    json=data
)

print(response.status_code)
print(response.json())


# ============================================================
# 12. PUT REQUEST
# ============================================================

url = "https://jsonplaceholder.typicode.com/posts/1"

data = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated body",
    "userId": 1
}

response = requests.put(
    url,
    json=data
)

print(response.status_code)
print(response.json())


# ============================================================
# 13. PATCH REQUEST
# ============================================================

url = "https://jsonplaceholder.typicode.com/posts/1"

data = {
    "title": "New Title"
}

response = requests.patch(
    url,
    json=data
)

print(response.status_code)
print(response.json())


# ============================================================
# 14. DELETE REQUEST
# ============================================================

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)

print("Status Code:", response.status_code)


# ============================================================
# 15. TIMEOUT
# ============================================================

try:

    response = requests.get(
        "https://example.com",
        timeout=5
    )

    print(response.status_code)

except requests.exceptions.Timeout:

    print("Request timed out!")


# ============================================================
# 16. ERROR HANDLING
# ============================================================

try:

    response = requests.get(
        "https://example.com",
        timeout=5
    )

    response.raise_for_status()

    print("Request successful!")

except requests.exceptions.RequestException as e:

    print("Error:", e)


# ============================================================
# 17. CHECK STATUS CODE
# ============================================================

response = requests.get("https://example.com")

if response.status_code == 200:
    print("Success!")

elif response.status_code == 404:
    print("Page not found!")

else:
    print("Something went wrong!")


# ============================================================
# 18. CHECK WHETHER REQUEST WAS SUCCESSFUL
# ============================================================

response = requests.get("https://example.com")

if response.ok:
    print("Request successful")

else:
    print("Request failed")


# ============================================================
# 19. SEND FORM DATA
# ============================================================

url = "https://httpbin.org/post"

data = {
    "name": "Sahil",
    "course": "B.Tech CSE"
}

response = requests.post(
    url,
    data=data
)

print(response.json())


# ============================================================
# 20. SEND JSON DATA
# ============================================================

url = "https://httpbin.org/post"

data = {
    "name": "Sahil",
    "language": "Python"
}

response = requests.post(
    url,
    json=data
)

print(response.json())


# ============================================================
# 21. DOWNLOAD A FILE
# ============================================================

url = "https://example.com"

response = requests.get(url)

with open("website.html", "wb") as file:
    file.write(response.content)

print("File downloaded!")


# ============================================================
# 22. BASIC AUTHENTICATION
# ============================================================

url = "https://httpbin.org/basic-auth/user/pass"

response = requests.get(
    url,
    auth=("user", "pass")
)

print(response.status_code)
print(response.json())


# ============================================================
# 23. COOKIES
# ============================================================

response = requests.get("https://example.com")

print(response.cookies)


# ============================================================
# 24. CUSTOM COOKIES
# ============================================================

cookies = {
    "username": "Sahil"
}

response = requests.get(
    "https://httpbin.org/cookies",
    cookies=cookies
)

print(response.json())


# ============================================================
# IMPORTANT REQUESTS FUNCTIONS
# ============================================================

"""
requests.get()       -> GET request
requests.post()      -> POST request
requests.put()       -> PUT request
requests.patch()     -> PATCH request
requests.delete()    -> DELETE request

response.status_code -> HTTP status code
response.text        -> Response as text
response.content     -> Response as bytes
response.json()      -> JSON -> Python object
response.headers     -> Response headers
response.cookies      -> Cookies
response.url         -> URL
response.ok           -> True/False

response.raise_for_status()
                       -> Raises error for bad status

requests.exceptions.RequestException
                       -> General request error
"""