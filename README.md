# Employee Table Management System

A comprehensive employee management system built with Django framework, providing complete employee information management, department management, task assignment, order management, and more.

## 🚀 Features

### Core Features

- **Employee Management** - Full CRUD operations for employee information including name, age, gender, salary, hire date, etc.
- **Department Management** - Department information management with employee-department associations
- **User Authentication** - Session-based login/logout system with CAPTCHA support
- **Access Control** - Custom middleware for access permission control
- **Pagination** - Custom pagination component for better data browsing experience

### Extended Features

- **Phone Number Management** - Phone number database with level and status classification
- **Task Management** - Task assignment and tracking system
- **Order Management** - Order information management and status tracking
- **Data Visualization** - Chart-based data presentation
- **Password Encryption** - MD5 encryption for secure password storage

## 🛠️ Tech Stack

- **Backend Framework**: Django 3.2.21
- **Database**: MySQL 
- **Frontend**: HTML + CSS + Bootstrap + JavaScript
- **Python Version**: Python 3.x
- **Database Driver**: PyMySQL

## 📋 System Requirements

- Python 3.6+
- Django 3.2.21
- MySQL 5.7+
- PyMySQL
- Pillow (for CAPTCHA generation)

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/which-W/employee_table.git
cd employee_table
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install -f requirements.txt
```

### 4. Database Configuration

Configure database connection in `employee_table/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'employee-table',  # Database name
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}
```

### 5. Create Database

```sql
CREATE DATABASE `employee-table` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Start Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the system.

## 📁 Project Structure

```
employee_table/
├── app01/                          # Main application
│   ├── middleware/                 # Middleware
│   │   └── auth.py                # Authentication middleware
│   ├── migrations/                 # Database migration files
│   ├── uels/                      # Utility classes
│   │   ├── bootstrap.py           # Bootstrap form base class
│   │   ├── font_virity.py         # CAPTCHA generation
│   │   ├── model_form.py          # Model forms
│   │   ├── pageform.py            # Pagination component
│   │   └── pwd_md5.py             # Password encryption
│   ├── view/                      # View modules
│   ├── models.py                  # Data models
│   └── ...
├── employee_table/                 # Project configuration
│   ├── settings.py                # Project settings
│   ├── urls.py                    # URL routing
│   └── ...
├── static/                        # Static files
├── templates/                     # Template files
├── manage.py                      # Django management script
├── requirements.txt               # Dependencies list
└── README.md                      # Project documentation
```

## 🗄️ Data Models

### Main Models

1. **Admin** - Administrator users
   - username: Username
   - password: Password (MD5 encrypted)

2. **Department** - Departments
   - title: Department name

3. **Employee_Table** - Employee information
   - name: Full name
   - age: Age
   - gender: Gender
   - salary: Salary
   - date: Hire date
   - depart: Department (Foreign Key)

4. **Telephone_User** - Phone number management
   - mobile: Phone number
   - price: Price
   - level: Level (1-4 grades)
   - status: Status (Sold/Available)

5. **Task** - Task management
   - level: Task priority level
   - name: Task name
   - description: Task description
   - user: Assignee (Foreign Key to Admin)

6. **Order** - Order management
   - user: Handler (Foreign Key to Admin)
   - name: Product name
   - price: Price
   - sale_situation: Sales status

## 🔗 URL Routes

| Module     | URL Path            | Description     |
| ---------- | ------------------- | --------------- |
| Department | `/depart/show`      | Department list |
|            | `/depart/add`       | Add department  |
|            | `/depart/<id>/edit` | Edit department |
| Employee   | `/user/show`        | Employee list   |
|            | `/user/add/info`    | Add employee    |
|            | `/user/<id>/edit`   | Edit employee   |
| Phone      | `/telephone/list`   | Phone list      |
|            | `/telephone/add`    | Add phone       |
| Admin      | `/admin/list`       | Admin list      |
|            | `/admin/add`        | Add admin       |
| Auth       | `/account/login`    | User login      |
|            | `/account/logout`   | User logout     |
| Task       | `/task/list`        | Task list       |
|            | `/task/add`         | Add task        |
| Order      | `/order/list`       | Order list      |
|            | `/order/add`        | Add order       |
| Charts     | `/chart/list`       | Chart display   |

## 🔐 Security Features

- **Password Encryption**: MD5 encryption for user passwords
- **Session Authentication**: Django Session-based user authentication
- **Access Control**: Custom middleware for page access control
- **CAPTCHA**: Graphical CAPTCHA for login pages
- **CSRF Protection**: Built-in Django CSRF protection

## 🎨 Custom Components

### 1. Pagination Component (`pageform.py`)

```python
# Usage example
page_object = Pagination(request, user_list, page_size=10)
context = {
    'user_list': page_object.queryset,
    'page_str': page_object.html()
}
```

### 2. Bootstrap Form Base Class (`bootstrap.py`)

Automatically adds Bootstrap CSS classes and placeholders to form fields.

### 3. CAPTCHA Generation (`font_virity.py`)

Generates graphical CAPTCHAs with interference lines and dots.

## 🚀 Deployment

### Production Environment Setup

1. Set `DEBUG = False` in `settings.py`

2. Configure `ALLOWED_HOSTS`

3. Collect static files:

   ```bash
   python manage.py collectstatic
   ```

4. Deploy with Gunicorn or other WSGI servers

### Docker Deployment (Optional)

```dockerfile
FROM python:3.8
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Changelog

- **v1.0.0** - Initial release
  - Basic employee management functionality
  - Department management
  - User authentication system

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

If you have any questions or suggestions, please contact us through:

- Create an [Issue](../../issues)
- Send email to: [wengzu728.love@gmail.com]

## 🙏 Acknowledgments

Thanks to all developers who have contributed to this project!

---

⭐ If this project helps you, please give it a star!
