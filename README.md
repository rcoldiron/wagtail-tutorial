Wagtail Tutorial
================

This tutorial assumes some knowledge of Python, Django, and Git/GitHub (optional). If you have experience with none of these, consider following these tutorials beforehand and coming back to this one once you are ready:

* [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)

* [Python virtual environments](https://docs.python.org/3/tutorial/venv.html)

* [Django Girls Tutorial](https://tutorial.djangogirls.org/en/)

* [Django 3.2 Tutorial](https://docs.djangoproject.com/en/3.2/intro/)

* [Git Handbook](https://guides.github.com/introduction/git-handbook/)


Key Technologies
----------------

These are the key technologies that we are using for this tutorial:

* Python 3.9

* Git and GitHub (if you want to track your code and its versions and/or publish your code)

* Wagtail 2.14 (Django 3.2 is included in the package)

* Visual Studio Code (or your favorite code editor)


Initial Setup
-------------

1. If you want to work with this repo, you can either download the files from GitHub, or fork the repo and clone it to your local machine. Otherwise, make a folder on your local machine to work in and open your command line tool to `cd` into the folder: `cd my-folder`

2. Install Python 3.9 if you do not have it on your computer; however, Wagtail 2.13 is compatible with Python 3.6 and up. Check your Python version with `python --version`. 

> NOTE: If it throws an error or doesn't recognize it, you may need to download it. Go to [Python - Downloads](https://www.python.org/downloads/) and follow download instructions for your Operating System.

3. Now create a virtual environment: `python3 -m venv .venv` on Windows 10. The command you have to use may be different, depending on your operating system and version.

4. Activate the virtual environment: `.venv\Scripts\activate.ps1` (on Windows 10) If it worked, you should see the name of the virtual environment in the command line before the file path on the next line, similar to the following: `(.venv) C:Users/YourName/Your/File/Location:`

5. Install Wagtail. This will also install all of its dependencies. I use `pip` to install, but you may use a different Python package manager. This command is for `pip`: `pip install wagtail`

> NOTE: The current version at the time of the creation of this repo is Wagtail 2.14. You can select a version to download, like this `pip install wagtail==2.14`

6. Create the first project: `wagtail start myproject .` where `myproject` is the name of the website or project (this can be whatever you want) and the `.` tells it to create it in your current folder. This command generates the new project files from Wagtail. Please take a moment to look them over.

> NOTE: Docker files are automatically generated with the project. While we will not be using them, we are keeping them in the repo in case you want to look them over and learn more about what they do. Docker can be used for deployment. [READ MORE](https://docs.wagtail.io/en/v2.14/reference/project_template.html#dockerfile)

7. Navigate into the project: `cd myproject` and do the first migration with: `python manage.py migrate`. Next, create a login account for your project with the command `python manage.py createsuperuser` and follow the prompts. Check if it all worked by running `python manage.py runserver` and opening your browser to `http://127.0.0.1:8000/`.

**Before moving onto the code section, get familiar with the CMS interface. Log into your site at `http://127.0.0.1:8000/admin` and read the [Wagtail documentation for Editors[(https://docs.wagtail.io/en/stable/editor_manual/index.html)].**


Customizing Your Site - Part I
------------------------------



