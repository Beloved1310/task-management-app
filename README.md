# Task Management Dashboard with Django, HTML, TailwindCSS, and jQuery

## Overview

This project implements a task management dashboard using Django for the backend and HTML, TailwindCSS, and jQuery for the frontend. It allows users to manage tasks with features such as CRUD operations, task filtering, sorting, and drag-and-drop functionality for task status updates.

## Features

- **Backend:**
  - Built with Django, utilizing Django models for Task and User management.
  - CRUD operations for tasks implemented through Django views.
  - RESTful API endpoints to fetch tasks based on their status (In Progress, Completed, Overdue).

- **Frontend:**
  - Designed the frontend using HTML to mirror the provided design.
  - Styled the dashboard using TailwindCSS for a responsive and visually appealing UI.
  - Implemented dynamic task loading using jQuery AJAX requests to interact with Django's backend API.
  - Included search functionality, task filtering (by priority, due date, category), and sorting capabilities.
  - Integrated modal dialogs for adding, editing, and deleting tasks, enhancing user interaction.
  - Implemented drag-and-drop functionality for seamless task status updates (e.g., moving tasks between "In Progress" and "Completed").

- **Additional Features:**
  - User authentication and authorization handled securely using Django's built-in capabilities.
  - Implemented form validation on both the client (jQuery) and server sides (Django forms).
  - Unit tests written for Django views and models to ensure functionality and reliability.
  - Comprehensive documentation provided within the codebase and a detailed README for setup and usage instructions.

## Setup Instructions

To run this project locally:

1. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/Beloved1310/task-management-app
   cd task-management-app

2.  Create a virtual environment and activate it:
   ```bash
   python -m venv venv

3.  Install dependencies:
   ```bash
   pip install -r requirements.txt

4.  Apply database migrations:
   ```bash
   python manage.py migrate

5. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser

6. Run the development server:
   ```bash
   python manage.py runserver


## Usage Instructions

### Login:

- Navigate to the login page.
- Use the superuser credentials created earlier to log in.

### Dashboard:

- After logging in, you will be directed to the task management dashboard.
- Here, you can view, add, edit, and delete tasks.

### Adding a Task:

- Click the "Add Task" button to open the task creation modal.
- Fill in the task details and click "Save" to add the task.

### Editing a Task:

- Click the edit icon next to a task to open the task editing modal.
- Modify the task details as needed and click "Save" to update the task.

### Deleting a Task:

- Click the delete icon next to a task to remove it from the dashboard.

### Filtering and Sorting:

- Use the search bar and filters to find tasks based on title, priority, due date, and category.
- Sort tasks by clicking on the column headers.

### Drag-and-Drop:

- Change the status of tasks by dragging and dropping them between "In Progress" and "Completed" columns.



