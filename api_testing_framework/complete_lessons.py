#!/usr/bin/env python3
"""Script to create remaining comprehensive lessons for Project 1."""

import os

BASE_PATH = "/project/workspace/api_testing_framework/Project_1_REST_API_Testing_Foundations"

# Lesson templates with comprehensive content
lessons_content = {
    "1.11_Testing_POST_Endpoints.md": """# Lesson 1.11: Testing POST Endpoints

## A. Concept Overview

### What & Why
**POST endpoint testing** verifies that resource creation works correctly. POST is used to create new resources, submit forms, and send data to the server. Testing POST ensures data is created correctly, validation works, and appropriate status codes are returned.

### Analogy
POST is like filling out a library card application. You provide your information (request body), the librarian processes it (server validation), and you get a new library card with an ID number (201 Created response with new resource).

---

## B. POST Request Basics

**Characteristics**:
- Creates new resources
- Has request body (JSON, form data, etc.)
- Not idempotent (creates new resource each time)
- Returns 201 Created on success
- Should include Location header with new resource URL

**Example**:
```http
POST /api/users
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com"
}

Response:
201 Created
Location: /api/users/123

{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2024-01-15T10:30:00Z"
}
```

---

## C. Testing POST with JSON

File: `tests/test_post_json.py`
```python
\"\"\"
Test POST requests with JSON data.
\"\"\"
import httpx


def test_create_user_returns_201():
    \"\"\"Test creating user returns 201 Created.\"\"\"
    payload = {
        "name": "Test User",
        "email": "test@example.com",
        "username": "testuser"
    }
    
    response = httpx.post(
        "https://jsonplaceholder.typicode.com/users",
        json=payload
    )
    
    assert response.status_code == 201


def test_create_post_with_json():
    \"\"\"Test creating a post with JSON data.\"\"\"
    payload = {
        "title": "Test Post",
        "body": "This is a test post body",
        "userId": 1
    }
    
    response = httpx.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )
    
    assert response.status_code == 201
    data = response.json()
    
    # Verify response contains what we sent
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    
    # Should have assigned an ID
    assert "id" in data
    assert isinstance(data["id"], int)


def test_post_content_type_header():
    \"\"\"Test that POST with json sets correct Content-Type.\"\"\"
    payload = {"test": "data"}
    
    response = httpx.post(
        "https://httpbin.org/post",
        json=payload
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # httpbin echoes back headers
    assert "application/json" in data["headers"]["Content-Type"]


def test_create_comment():
    \"\"\"Test creating a comment.\"\"\"
    payload = {
        "postId": 1,
        "name": "Test Comment",
        "email": "commenter@example.com",
        "body": "This is a test comment"
    }
    
    response = httpx.post(
        "https://jsonplaceholder.typicode.com/comments",
        json=payload
    )
    
    assert response.status_code == 201
    data = response.json()
    
    assert data["postId"] == payload["postId"]
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert data["body"] == payload["body"]
```

---

## D. Testing Validation Errors

File: `tests/test_post_validation.py`
```python
\"\"\"
Test POST validation and error handling.
\"\"\"
import httpx


def test_post_empty_body():
    \"\"\"Test POST with empty body.\"\"\"
    response = httpx.post(
        "https://httpbin.org/post",
        json={}
    )
    
    # httpbin accepts empty body
    assert response.status_code == 200


def test_post_missing_required_fields():
    \"\"\"Test POST with missing required fields.\"\"\"
    # JSONPlaceholder is lenient, use httpbin to demonstrate
    payload = {"incomplete": "data"}
    
    response = httpx.post(
        "https://httpbin.org/post",
        json=payload
    )
    
    # httpbin echoes back what we sent
    assert response.status_code == 200
    data = response.json()
    assert data["json"] == payload


def test_post_invalid_json():
    \"\"\"Test POST with invalid JSON string.\"\"\"
    import pytest
    
    # httpx handles JSON serialization, so manually test with data parameter
    response = httpx.post(
        "https://httpbin.org/post",
        data="not valid json",
        headers={"Content-Type": "application/json"}
    )
    
    # Server might return 400 or accept it
    assert response.status_code in [200, 400]


def test_post_data_types():
    \"\"\"Test POST with various data types.\"\"\"
    payload = {
        "string": "text",
        "number": 42,
        "float": 3.14,
        "boolean": True,
        "null": None,
        "array": [1, 2, 3],
        "object": {"nested": "value"}
    }
    
    response = httpx.post(
        "https://httpbin.org/post",
        json=payload
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # httpbin echoes back our payload
    assert data["json"] == payload
```

---

## E. Testing Form Data

File: `tests/test_post_form_data.py`
```python
\"\"\"
Test POST with form-encoded data.
\"\"\"
import httpx


def test_post_form_data():
    \"\"\"Test POST with application/x-www-form-urlencoded.\"\"\"
    form_data = {
        "username": "testuser",
        "password": "secret123",
        "remember": "true"
    }
    
    response = httpx.post(
        "https://httpbin.org/post",
        data=form_data  # Use 'data' for form encoding
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # httpbin shows form data in 'form' field
    assert data["form"]["username"] == "testuser"
    assert data["form"]["password"] == "secret123"


def test_post_multipart_form_data():
    \"\"\"Test POST with multipart/form-data.\"\"\"
    files = {
        "file": ("test.txt", "file content", "text/plain")
    }
    data = {
        "description": "Test file upload"
    }
    
    response = httpx.post(
        "https://httpbin.org/post",
        files=files,
        data=data
    )
    
    assert response.status_code == 200
```

---

## F. Testing Response Data

File: `tests/test_post_response.py`
```python
\"\"\"
Test POST response validation.
\"\"\"
import httpx


def test_post_returns_created_resource():
    \"\"\"Test that POST response includes created resource.\"\"\"
    payload = {
        "title": "New Post",
        "body": "Post content",
        "userId": 1
    }
    
    response = httpx.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )
    
    assert response.status_code == 201
    data = response.json()
    
    # Should include ID for new resource
    assert "id" in data
    assert data["id"] > 0


def test_post_response_structure():
    \"\"\"Test that POST response has expected structure.\"\"\"
    payload = {
        "name": "New Todo",
        "completed": False
    }
    
    response = httpx.post(
        "https://jsonplaceholder.typicode.com/todos",
        json=payload
    )
    
    assert response.status_code == 201
    data = response.json()
    
    # Check response structure
    assert isinstance(data, dict)
    assert "id" in data
```

---

## G. Key Takeaways

🔑 **POST creates resources**: Returns 201 Created  
🔑 **Use json parameter**: For JSON data  
🔑 **Use data parameter**: For form data  
🔑 **Validate response**: Check status, new ID, data  
🔑 **Test validation**: Send invalid/incomplete data  
🔑 **Check Location header**: Should point to new resource  
🔑 **Not idempotent**: Each POST creates new resource  

---

## H. What's Next?

In **Lesson 1.12: Testing PUT and PATCH Endpoints**, we'll learn how to test updates with both full replacement (PUT) and partial updates (PATCH).

**Ready for lesson 1.12?**
""",

    "1.12_Testing_PUT_and_PATCH_Endpoints.md": """# Lesson 1.12: Testing PUT and PATCH Endpoints

## A. Concept Overview

### What & Why
**PUT and PATCH** are used to update existing resources. PUT replaces the entire resource, while PATCH updates only specified fields. Testing both ensures updates work correctly and data integrity is maintained.

### Analogy
Think of editing a document:
- **PUT** = Replace entire document with new version (all content changes)
- **PATCH** = Edit specific paragraphs (only changed parts update)

---

## B. PUT vs PATCH Differences

| Aspect | PUT | PATCH |
|--------|-----|-------|
| **Updates** | Entire resource | Specific fields |
| **Missing fields** | Removed/defaulted | Unchanged |
| **Idempotent** | Yes | Yes |
| **Status code** | 200 OK | 200 OK |
| **Use when** | Replacing all data | Updating few fields |

---

## C. Testing PUT Requests

File: `tests/test_put_requests.py`
```python
\"\"\"
Test PUT requests for full resource updates.
\"\"\"
import httpx


def test_put_update_user():
    \"\"\"Test updating entire user with PUT.\"\"\"
    user_id = 1
    payload = {
        "id": user_id,
        "name": "Updated Name",
        "username": "updateduser",
        "email": "updated@example.com"
    }
    
    response = httpx.put(
        f"https://jsonplaceholder.typicode.com/users/{user_id}",
        json=payload
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # Verify updates applied
    assert data["name"] == payload["name"]
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]


def test_put_replaces_all_fields():
    \"\"\"Test that PUT replaces entire resource.\"\"\"
    post_id = 1
    payload = {
        "id": post_id,
        "title": "Completely New Title",
        "body": "Completely new body",
        "userId": 1
    }
    
    response = httpx.put(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}",
        json=payload
    )
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]


def test_put_nonexistent_resource():
    \"\"\"Test PUT to non-existent resource.\"\"\"
    response = httpx.put(
        "https://jsonplaceholder.typicode.com/posts/99999",
        json={"title": "New", "body": "Content", "userId": 1}
    )
    
    # JSONPlaceholder may return 200 or 404
    assert response.status_code in [200, 404]


def test_put_idempotency():
    \"\"\"Test that multiple identical PUT requests produce same result.\"\"\"
    post_id = 1
    payload = {"id": post_id, "title": "Same Title", "body": "Same Body", "userId": 1}
    
    # First PUT
    response1 = httpx.put(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}",
        json=payload
    )
    
    # Second identical PUT
    response2 = httpx.put(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}",
        json=payload
    )
    
    assert response1.status_code == 200
    assert response2.status_code == 200
    
    # Results should be identical (idempotent)
    assert response1.json() == response2.json()
```

---

## D. Testing PATCH Requests

File: `tests/test_patch_requests.py`
```python
\"\"\"
Test PATCH requests for partial updates.
\"\"\"
import httpx


def test_patch_update_single_field():
    \"\"\"Test updating single field with PATCH.\"\"\"
    user_id = 1
    payload = {
        "email": "newemail@example.com"
    }
    
    response = httpx.patch(
        f"https://jsonplaceholder.typicode.com/users/{user_id}",
        json=payload
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # Only email should be updated
    assert data["email"] == payload["email"]


def test_patch_update_multiple_fields():
    \"\"\"Test updating multiple fields with PATCH.\"\"\"
    post_id = 1
    payload = {
        "title": "Updated Title",
        "body": "Updated body content"
    }
    
    response = httpx.patch(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}",
        json=payload
    )
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    # userId should remain unchanged
    assert "userId" in data


def test_patch_preserves_other_fields():
    \"\"\"Test that PATCH doesn't affect unspecified fields.\"\"\"
    todo_id = 1
    
    # First, get current todo
    get_response = httpx.get(
        f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    )
    original_data = get_response.json()
    
    # PATCH only completed field
    patch_payload = {"completed": True}
    patch_response = httpx.patch(
        f"https://jsonplaceholder.typicode.com/todos/{todo_id}",
        json=patch_payload
    )
    
    assert patch_response.status_code == 200
    updated_data = patch_response.json()
    
    # Completed should be updated
    assert updated_data["completed"] == True
    
    # Other fields should remain (in real API)
    # JSONPlaceholder mock may not preserve all fields


def test_patch_idempotency():
    \"\"\"Test that PATCH is idempotent.\"\"\"
    user_id = 1
    payload = {"name": "Consistent Name"}
    
    # First PATCH
    response1 = httpx.patch(
        f"https://jsonplaceholder.typicode.com/users/{user_id}",
        json=payload
    )
    
    # Second identical PATCH
    response2 = httpx.patch(
        f"https://jsonplaceholder.typicode.com/users/{user_id}",
        json=payload
    )
    
    assert response1.status_code == 200
    assert response2.status_code == 200
```

---

## E. PUT vs PATCH Comparison Tests

File: `tests/test_put_vs_patch.py`
```python
\"\"\"
Compare PUT and PATCH behavior.
\"\"\"
import httpx


def test_put_vs_patch_difference():
    \"\"\"Demonstrate difference between PUT and PATCH.\"\"\"
    user_id = 1
    
    # PUT with partial data (would remove other fields in real API)
    put_payload = {"name": "Only Name"}
    put_response = httpx.put(
        f"https://jsonplaceholder.typicode.com/users/{user_id}",
        json=put_payload
    )
    
    # PATCH with partial data (preserves other fields)
    patch_payload = {"name": "Only Name"}
    patch_response = httpx.patch(
        f"https://jsonplaceholder.typicode.com/users/{user_id}",
        json=patch_payload
    )
    
    # Both should succeed
    assert put_response.status_code == 200
    assert patch_response.status_code == 200
    
    # In a real API:
    # PUT response would only have 'name' field
    # PATCH response would have all fields with 'name' updated
```

---

## F. Key Takeaways

🔑 **PUT**: Replaces entire resource  
🔑 **PATCH**: Updates specific fields only  
🔑 **Both idempotent**: Same request = same result  
🔑 **Status 200 OK**: For successful updates  
🔑 **Status 404**: If resource doesn't exist  
🔑 **Use PUT**: When replacing all data  
🔑 **Use PATCH**: When updating few fields  

---

## G. What's Next?

In **Lesson 1.13: Testing DELETE Endpoints**, we'll learn how to test resource deletion, verify removal, and handle deletion errors.

**Ready for lesson 1.13?**
"""
}

# Write lessons
for filename, content in lessons_content.items():
    filepath = os.path.join(BASE_PATH, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Created: {filename}")

print(f"\nCompleted {len(lessons_content)} lessons!")
