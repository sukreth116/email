# Django Email System

A web-based email application built using **Django, JavaScript, HTML, and CSS** that provides an email experience similar to Gmail. Users can create accounts, send and receive messages, manage their inbox, archive emails, and reply to messages through a dynamic interface.

The application uses Django for backend logic, data management, and authentication, while JavaScript handles client-side interactions to provide a smoother experience without requiring full-page reloads for every email operation.

## Features

### Authentication & User Management
- User registration
- Login and logout functionality
- User-specific email management

### Email Management
- Compose and send emails to one or multiple recipients
- View received emails in the inbox
- View sent emails
- Read email details
- Reply to emails with pre-filled recipient and content
- Archive emails
- Unarchive emails
- Unread email highlighting

### Interactive User Interface
- Single-page application-like experience
- Asynchronous requests using JavaScript Fetch API
- Dynamic email loading and updates without full-page refreshes
- Responsive UI with Bootstrap

## Tech Stack

| Technology | Usage |
|---|---|
| Python | Backend programming |
| Django | Web framework, authentication, routing, and backend logic |
| JavaScript | Client-side interactions and asynchronous requests |
| Fetch API | Communicating with Django endpoints |
| HTML5 | Page structure and templates |
| CSS3 | Styling and UI customization |
| Bootstrap | Responsive layouts and UI components |
| SQLite | Database |
| Git & GitHub | Version control |

## Application Modules

- **Inbox** – View received emails and identify unread messages.
- **Compose** – Create and send emails to one or multiple recipients.
- **Sent** – View previously sent emails.
- **Archive** – Move emails out of the inbox and manage archived messages.
- **Reply** – Respond to received emails with the recipient and subject automatically populated.

## How It Works

The application follows a client-server architecture:

1. Django handles authentication, requests, email data, and backend processing.
2. Email information is stored and managed through Django's database models.
3. JavaScript sends asynchronous requests to Django using the Fetch API.
4. The server returns responses that JavaScript uses to update the interface dynamically.
5. Users can manage emails without repeatedly reloading the entire page.

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/sukreth116/email.git
```

```bash
cd email
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```powershell
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Project Structure

```text
email/
├── manage.py
├── requirements.txt
├── project configuration/
├── application modules/
├── templates/
│   ├── register.html
│   ├── user-template.html
│   └── user-template-1.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── README.md
```

*Note: The directory structure above is a simplified overview.*

## Learning Objectives

This project helped explore and practice:

- Django application development
- User authentication and session management
- Database models and ORM operations
- URL routing and views
- Backend and frontend communication
- JavaScript Fetch API
- Asynchronous programming
- Dynamic DOM manipulation
- Email workflows and CRUD operations
- Responsive UI development with Bootstrap

## Future Improvements

- Improve email search and filtering
- Add attachment support
- Improve notification handling
- Enhance UI responsiveness and accessibility
- Add more advanced email organization features

---

**Developed by Sukreth O M**

GitHub: [@sukreth116](https://github.com/sukreth116)
