[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/545oUMxH)

### Please use the following template to add a ReadMe for your repo.

## 1. Project Title and Description
    - Title: MyJournal
    - Description: MyJournal allows user to create, view, edit, and delete their journal entries. Each entry is composed of a date, title, and main body.
## 2. Installation
    - Dependencies: 
        + asgiref==3.7.2
        + certifi==2024.2.2
        + charset-normalizer==3.3.2
        + Django==3.2.1
        + idna==3.6
        + psycopg2==2.9.9
        + pytz==2024.1
        + requests==2.31.0
        + sqlparse==0.4.4
        + urllib3==2.2.1
        
    - Installation Instructions: 
        1. Pull code from the git repository.
        2. In diary\settings.py, find the 'USER' and 'PASSWORD' key in DATABASES dictionary and change their value to your postgress account's username and password.
        3. Create a database by running this command: python manage.py migrate.
        4. Download the required dependencies.
        5. Make yourself a superuser of the project by running this command: python manage.py createsuperuser.
        6. Enter user information according to prompts.
        7. Run the web server by running this command: python manage.py runserver.
## 3. Usage
    - Examples: 
        1. You must start the Django development server by running the command python manage.py runserver.
        2. Access the project in the browser by the url: http://127.0.0.1:8000/
        3. You can access different pages to use different functionalities by the following urls:
            + Homepage - view all journal entries: http://127.0.0.1:8000/
            + Details of a specific journal entry with id==<int:pk>: http://127.0.0.1:8000/entry/<int:pk>
            + Update a specific journal entry with id==<int:pk>: http://127.0.0.1:8000/entry/<int:pk>/update
            + Delete a specific journal entry with id==<int:pk>: http://127.0.0.1:8000/entry/<int:pk>/delete
            + *Note: <int:pk> is the id (primary key) of the journal entry and you can find it: 
                * In the pgAdmin app. 
                * Clicks the entry title, then the browser will navigate you to the details page at http://127.0.0.1:8000/entry/<int:pk>, where you can inspect the id by viewing the <int:pk> parameter.
        4. You can click the "Logout" Link to log you out of the Django admin site so that other people can not access your journal entries through your laptop.
        5. You can click the "log in again" link to log in so you can access and modify your journal entries again!
      
    - Configuration: 
        1. In diary\settings.py, find the 'USER' and 'PASSWORD' key in DATABASES dictionary and change their value to your postgress account's username and password.
        2. Create a database by running this command: python manage.py migrate.
        3. Make yourself a superuser of the project by running this command: python manage.py createsuperuser.

## 4. Features
    - List of Features: 
        + Create journal entries
        + Read journal entries
        + Update journal entries
        + Delete journal entries
        + Provide authentication to protect user's journal entries (login, logout)
## 5. Contributing
    - Guidelines: 
        + Bug Reports: If you encounter any bugs or issues while using MyJournal, please submit a detailed bug report through our GitHub Issues page. Please ensure that you include propoer titile (Bug Report), the steps to reproduce the issue, expected vs. actual behavior, and any relevant screenshots. 
        + Feature Requests: If you have any feauture request or suggestion for improving My Journal, please submit a feature request through our GitHub Issue page. Please ensure that you include the proper title (Feature request), a clear description of the proposed feature, and any potential use cases.
        + Code Contribution: We appreciate contributions from the community to help us improve MyJournal. If you're interested in contributing code, please follow these steps:
            1. Fork the repository.
            2. Create a new branch for your feature or bug fix.
            3. Implement changes and make sure you are following our coding style.
            4. Submit a pull request to the main branch of the original repository, explaining the purpose of your changes and any relevant details.
            5. Your pull request will be reviewed by the our developer, and any necessary feedback or adjustments will be provided before merging.

    - Code Style: We follow the PEP 8 style guide (https://peps.python.org/pep-0008/) for Python code in MyJournal.
## 6. Credits
    - Authors: Kristina Zaporozhets, Zoey Lin.
    - Acknowledgments: 
        + tutorial 1: https://www.w3schools.com/django/ 
        + tutotial 2: https://www.linkedin.com/learning/django-essential-training/what-is-django?u=2169170
        + idea: https://startcodingnow.com/django-projects-ideas-for-beginners 
## 7. License
    - License Information: Specify the license under which your project is distributed.
## 8. Additional Sections (Optional)
    - FAQ: Include frequently asked questions and their answers.
    - Troubleshooting: Provide solutions to common issues or troubleshooting tips.
    - Roadmap: Outline the future development plans for your project.
    - Changelog: Document changes and updates to your project over time.

## Markdown Formatting Tips
  - Use headings (#, ##, ###, etc.) to structure your document.
  - Utilize lists (- or 1.) for easy-to-read information.
  - Include links to relevant resources or documentation.
  - Add code blocks using triple backticks (```) for code snippets.
  - Use images or diagrams to enhance understanding where applicable.
