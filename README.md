# Task Management API

## Overview

The Task Management API allows users to manage tasks, categories, notifications, and activity logs. It provides a set of endpoints for creating, retrieving, updating, and deleting tasks and categories, as well as managing user authentication and notifications.

## Features

- User  Authentication: Login, logout, and registration functionalities.
- Task Management: Create, list, retrieve, update, and delete tasks.
- Category Management: Create, list, retrieve, update, and delete categories.
- Notification Management: Create, list, retrieve, and delete notifications related to tasks.
- Activity Logging: Track user actions related to task management.

## API Endpoints

### Authentication

#### Login
- Method: POST
- Endpoint: /api/login/
- Description: Allows a user to log in and retrieve an authentication token.
- Input:
        {
        "username": "new_user",
        "password": "your_password"
    }
    
- Response:
        {
        "token": "1c334b044bcc09b992b0c1e81086aff26dcb7f39",
        "login-message": "Login successful!"
    }
    

#### Logout
- Method: POST
- Endpoint: /api/logout/
- Description: Logs out the user by invalidating their token.
- Input: {} (No input required)
- Response:
        {
        "logout-message": "Logout successful!"
    }
    

#### Register
- Method: POST
- Endpoint: /api/register/
- Description: Registers a new user.
- Input:
        {
        "username": "new_user",
        "email": "new_user@example.com",
        "password": "your_password"
    }
    
- Response:
        {
        "message": "User  registered successfully!",
        "username": "new_user",
        "email": "new_user@example.com"
    }
    

### Task Management

#### Create Task
- Method: POST
- Endpoint: /api/tasks/
- Description: Creates a new task.
- Input:
        {
        "title": "Complete project",
        "description": "Work on the API development.",
        "completed": false
    }
    
- Response:
        {
        "id": 1,
        "title": "Complete project",
        "description": "Work on the API development.",
        "completed": false,
        "message": "Task created successfully!"
    }
    

#### List Tasks
- Method: GET
- Endpoint: /api/tasks/
- Description: Retrieves a list of all tasks.
- Response:
        [
        {
            "id": 1,
            "title": "Complete project",
            "description": "Work on the API development.",
            "completed": false
        },
        {
            "id": 2,
            "title": "Review code",
            "description": "Check for bugs and optimize.",
            "completed": true
        }
    ]
    

#### Retrieve Task
- Method: GET
- Endpoint: /api/tasks/{id}/
- Description: Retrieves details of a specific task by ID.
- Response:
        {
        "id": 1,
        "title": "Complete project",
        "description": "Work on the API development.",
        "completed": false
    }
    

#### Update Task
- Method: PUT
- Endpoint: /api/tasks/{id}/
- Description: Updates a task with new details.
- Input:
        {
        "title": "Complete project v2",
        "description": "Work on API and documentation.",
        "completed": true
    }
    
- Response:
        {
        "id": 1,
        "title": "Complete project v2",
        "description": "Work on API and documentation.",
        "completed": true,
        "message": "Task updated successfully!"
    }
    

#### Delete Task
- Method: DELETE
- Endpoint: /api/tasks/{id}/
- Description: Deletes a specific task by ID.
- Response:
        {
        "message": "Task deleted successfully!"
    }
    

### Category Management

#### Create Category
- Method: POST
- Endpoint: /api/categories/
- Description: Creates a new category.
- Input:
        {
        "name": "New Category"
    }
    
- Response:
        {
        "id": 1,
        "name": "New Category",
        "message": "Category created successfully!"
    }

አኑኤል, [1/17/2025 9:56 PM]
#### List Categories
- Method: GET
- Endpoint: /api/categories/
- Description: Retrieves a list of all categories.
- Response:
        [
        {
            "id": 1,
            "name": "New Category"
        },
        {
            "id": 2,
            "name": "Existing Category"
        }
    ]
    

#### Retrieve Category
- Method: GET
- Endpoint: /api/categories/{id}/
- Description: Retrieves details of a specific category by ID.
- Response:
        {
        "id": 1,
        "name": "New Category"
    }
    

#### Update Category
- Method: PUT
- Endpoint: /api/categories/{id}/
- Description: Updates a category with new details.
- Input:
        {
        "name": "Updated Category Name"
    }
    
- Response:
        {
        "id": 1,
        "name": "Updated Category Name",
        "message": "Category updated successfully!"
    }
    

#### Delete Category
- Method: DELETE
- Endpoint: /api/categories/{id}/
- Description: Deletes a specific category by ID.
- Response:
        {
        "message": "Category deleted successfully!"
    }
    

### Notification Management

#### Create Notification
- Method: POST
- Endpoint: /api/notifications/
- Description: Creates a new notification for a task or event.
- Input:
        {
        "task_id": 1,
        "message": "Reminder: Task is due soon!"
    }
    
- Response:
        {
        "id": 1,
        "task_id": 1,
        "message": "Reminder: Task is due soon!",
        "date_created": "2025-01-17T15:00:00Z",
        "message": "Notification created successfully!"
    }
    

#### List Notifications
- Method: GET
- Endpoint: /api/notifications/
- Description: Retrieves a list of all notifications.
- Response:
        [
        {
            "id": 1,
            "task_id": 1,
            "message": "Reminder: Task is due soon!",
            "date_created": "2025-01-17T15:00:00Z"
        },
        {
            "id": 2,
            "task_id": 2,
            "message": "Task completed, good job!",
            "date_created": "2025-01-16T14:30:00Z"
        }
    ]
    

#### Retrieve Notification
- Method: GET
- Endpoint: /api/notifications/{id}/
- Description: Retrieves details of a specific notification by ID.
- Response:
        {
        "id": 1,
        "task_id": 1,
        "message": "Reminder: Task is due soon!",
        "date_created": "2025-01-17T15:00:00Z"
    }
    

#### Delete Notification
- Method: DELETE
- Endpoint: /api/notifications/{id}/
- Description: Deletes a specific notification by ID.
- Response:
        {
        "message": "Notification deleted successfully!"
    }
    

### Activity Log Management

#### Create Activity Log
- Method: POST
- Endpoint: /api/create-task/
- Description: Creates a new task and logs the activity.
- Input: {} (No input required)
- Response:
        {
        "message": "Task created successfully!",
        "task_id": 123
    }
    

#### Get Activity Logs
- Method: GET
- Endpoint: /api/logs/
- Description: Retrieves a list of activity logs.
- Response:
        [
        {
            "action": "Created Task",
            "user": "john_doe",
            "timestamp": "2025-01-17T12:34:56Z",
            "details": "Task ID: 123"
        },
        {
            "action": "Updated Task",
            "user": "jane_doe",
            "timestamp": "2025-01-17T14:00:00Z",
            "details": "Task ID: 124"
        }
    ]
    
