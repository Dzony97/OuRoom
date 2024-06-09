# OuRoom

## Table of contents
* [Description](#description)
* [Technologies](#technologies)
* [Setup](#setup)
* [Screen](#screen)

## Description
OuRoom is a social media web application where users can create posts, form groups and enjoy playing the classic Snake game. The platform integrates dynamic content updates using modern web technologies, providing a seamless and interactive user experience.

## Technologies
List of main technologies used in the project:

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django
- **API Fetching**: JavaScript Fetch API


## Setup
To set up the OuRoom project, you will need to install Python, Django, and perform database migrations. Below are the detailed steps to get you started:

### Prerequisites
Python: Ensure you have Python installed. You can download it from the official Python website.

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Dzony97/OuRoom.git
   cd OuRoom

2. **Install Python**:
    - Verify if Python is installed by running:
      ```sh
      python --version
      ```
    - If Python is not installed, download and install it from the [official Python website](https://www.python.org/downloads/).

3. **Create a Virtual Environment**:
    - It is a good practice to create a virtual environment for your project to manage dependencies.
      ```sh
      python -m venv ouroom_env
      ```
    - Activate the virtual environment:
      - On Windows:
        ```sh
        ouroom_env\Scripts\activate
        ```
      - On macOS and Linux:
        ```sh
        source ouroom_env/bin/activate
        ```

4. **Install Django**:
    - With the virtual environment activated, install Django using pip:
      ```sh
      pip install django
      ```

5. **Navigate to the Project Directory**:
    - Change your directory to the project's root directory:
      ```sh
      cd ouroom
      ```

6. **Apply Migrations**:
    - Django uses migrations to propagate changes you make to your models into your database schema.
      ```sh
      python manage.py migrate
      ```

7. **Run the Development Server**:
    - Start the development server to verify everything is set up correctly:
      ```sh
      python manage.py runserver
      ```

8. **Access the Application**:
    - Open your web browser and go to `http://127.0.0.1:8000/` to see your Django project running.
