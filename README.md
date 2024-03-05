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
    - Examples: Include examples or code snippets to demonstrate how to use your project.
    - Configuration: Explain any configuration options or settings users might need to know about.
## 4. Features
    - List of Features: 
        + Create journal entries
        + Read journal entries
        + Update journal entries
        + Delete journal entries
        + Provide authentication to protect user's journal entries (login, logout)
## 5. Contributing
    - Guidelines: Explain how others can contribute to your project, including information on submitting bug reports, feature requests, or code contributions.
    - Code Style: If applicable, provide guidelines or references to your code style.
## 6. Credits
    - Authors: Kristina Zaporozhets, Zoey Lin.
    - Acknowledgments: Mention any individuals or resources that helped inspire or support your project.
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
