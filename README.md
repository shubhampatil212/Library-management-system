# Library Management System

## Introduction

This is a Library Management System built using Django and MySQL. It allows an admin to perform CRUD operations on books. The system has an admin login and signup feature to ensure only authorized users can manage books. Students or other users can view the list of available books.

## Technologies Used

- **Backend**: Python, Django (5.1.7)
- **Database**: MySQL
- **Frontend**: HTML, CSS, Bootstrap

## Features

### Admin Features

1. **Admin Signup**: The admin can create an account by entering their details. The email must be unique.
2. **Admin Login**: Admins can log in using their email and password.
3. **Add Book**: Admins can add new books by entering details such as title, author, published date, and ISBN.
4. **Update Book**: Admins can edit book details.
5. **Delete Book**: Admins can delete books from the database.
6. **View Books**: Admins can see all books in the system.

### Student View

1. **View All Books**: Students can view the list of books but cannot edit them.

## Database Models

### Admin Model

The admin model stores admin details like name, email, and password. The email field is unique to prevent duplicate accounts.

### Book Model

The book model stores details like title, author, published date, and ISBN. The ISBN field is unique.

## Setup Instructions

### Step 1: Clone the Repository
```sh
git clone <repository_url>
cd <repository_folder>
```

### Step 2: Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 4: Configure the Database
Edit the `settings.py` file and update the `DATABASES` section with your MySQL credentials.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Step 5: Apply Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser
```sh
python manage.py createsuperuser
```
Follow the instructions to set up an admin account.

### Step 7: Run the Development Server
```sh
python manage.py runserver
```

### Step 8: Access the Application
Open a web browser and go to `http://127.0.0.1:8000/` to access the system.
