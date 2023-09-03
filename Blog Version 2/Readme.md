# Django Blog Project

This is a Django web application for a simple blogging platform inspired by the book "Django for Beginners" by William Vincent. It allows users to create, view, update, and delete blog posts. Users can also sign up for an account, sign in, and log out.

## Features

- User Authentication: Users can sign up, log in, and log out.
- Blog Post Management: Users can create, view, update, and delete their own blog posts.
- Responsive Design: The project uses HTML templates with Bootstrap for a responsive and user-friendly interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x: Make sure you have Python installed on your system. You can download it from the [official website](https://www.python.org/downloads/).
- Django: This project is built with Django. You can install it using pip:

    ```
    pip install django
    ```

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/120lennox/Python-Django.git
    cd Python-Django
    ```

2. Create a virtual environment (optional but recommended):

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install project dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```
    python manage.py migrate
    ```

5. Create a superuser account (admin):

    ```
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```
    python manage.py runserver
    ```

7. Access the application in your web browser at `http://localhost:8000/`.

## Usage

1. Sign up for an account on the website.
2. Log in with your credentials.
3. Create, edit, and delete blog posts from your dashboard.
4. Log out when you're done.

## Folder Structure

- `BLOG VERSION 2/`: Contains the Django app for the blog functionality.
- `templates/`: Stores HTML templates used in the project.


## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.

## Credits

This project is based on the book "Django for Beginners" by William Vincent, and it was created for educational purposes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.