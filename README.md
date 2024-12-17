# API Testing Framework Using Python and Builder Pattern

## Overview

This repository provides an API Testing Framework built using Python and the Builder Pattern. The framework enables efficient, scalable, and modular testing of CRUD (Create, Read, Update, Delete) operations for APIs.

By leveraging the Builder Pattern, the framework allows dynamic request building and clean separation of configuration, test data, and test modules.

## Directory Structure

```
api_testing_framework/
├── api_framework/              # Core framework components
│   ├── __init__.py
│   ├── request_builder.py      # Request builder using Builder Pattern
│   ├── utils.py                # Utility functions for loading files and environment variables
│
├── tests/                      # Separate test modules for each CRUD operation
│   ├── __init__.py
│   ├── test_create_resource.py # Test case for creating a resource
│   ├── test_read_resource.py   # Test case for reading a resource
│   ├── test_update_resource.py # Test case for updating a resource
│   ├── test_delete_resource.py # Test case for deleting a resource
│
├── config/                     # JSON files for endpoints and test data
│   ├── create_endpoint.json    # Endpoint for CREATE operation
│   ├── read_endpoint.json      # Endpoint for READ operation
│   ├── update_endpoint.json    # Endpoint for UPDATE operation
│   ├── delete_endpoint.json    # Endpoint for DELETE operation
│   ├── create_data.json        # Test data for CREATE operation
│   ├── update_data.json        # Test data for UPDATE operation
│
├── .env                        # Environment variables (e.g., base URL)
```

## Key Features

- **Builder Pattern**: Simplifies and dynamically constructs HTTP requests.
- **Separation of Concerns**:
  - Endpoints and test data are stored in JSON files for easy maintenance.
  - Test cases are modularized for each CRUD operation.
- **Environment Configurations**: Uses an .env file for storing base URLs, supporting multiple environments like staging and production.
- **Scalable Design**: New endpoints and test cases can be added seamlessly.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/api-testing-framework.git
cd api-testing-framework
```

### 2. Create a Virtual Environment

```bash
# On Linux/Mac
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Ensure requests and python-dotenv are installed:

```bash
pip install -r requirements.txt
```

### 4. Add .env File

Create a `.env` file in the root directory with the following content:

```
BASE_URL=https://example.com/api
```

### 5. Configure JSON Files

Define endpoints and test data in the `config` folder:

#### create_endpoint.json
```json
{ "create": "/posts" }
```

#### read_endpoint.json
```json
{ "read": "/posts/{id}" }
```

#### update_endpoint.json
```json
{ "update": "/posts/{id}" }
```

#### delete_endpoint.json
```json
{ "delete": "/posts/{id}" }
```

#### create_data.json
```json
{ "title": "foo", "body": "bar", "userId": 1 }
```

#### update_data.json
```json
{ "title": "updated title", "body": "updated body", "userId": 1 }
```

## How to Run Tests

Run the test suite using pytest. Each CRUD operation is implemented as a separate test module.

### Create Resource
```bash
pytest tests/test_create_resource.py
```

### Read Resource
```bash
pytest tests/test_read_resource.py
```

### Update Resource
```bash
pytest tests/test_update_resource.py
```

### Delete Resource
```bash
pytest tests/test_delete_resource.py
```

### Run All Tests
```bash
pytest tests/
```

## Code Example: Request Builder

Here's an example of the `RequestBuilder` class for constructing API requests:

```python
# api_framework/request_builder.py
import requests

class RequestBuilder:
    def __init__(self):
        self.url = None
        self.headers = {}
        self.data = None
        self.method = "GET"

    def set_url(self, url):
        self.url = url
        return self

    def add_header(self, key, value):
        self.headers[key] = value
        return self

    def set_data(self, data):
        self.data = data
        return self

    def set_method(self, method):
        self.method = method
        return self

    def build(self):
        if self.method == "POST":
            return requests.post(self.url, headers=self.headers, json=self.data)
        elif self.method == "GET":
            return requests.get(self.url, headers=self.headers)
        elif self.method == "PUT":
            return requests.put(self.url, headers=self.headers, json=self.data)
        elif self.method == "DELETE":
            return requests.delete(self.url, headers=self.headers)
```

## Future Enhancements

- Integrate a reporting tool like Allure or HTML reporting for better visualization of test results.
- Add authentication handling for APIs requiring tokens or credentials.
- Implement parallel execution of test cases using pytest-xdist.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.

---

