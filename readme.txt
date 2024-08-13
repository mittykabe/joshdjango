Setting Up Django Project:
Step 1 - Create Database
Step 2 - Open Project in VS Code
Step 3 - Change Database password in /storefront/Settings.py
Step 4 - Set location for virtual environment
 - Create an empty folder in the project and name it .venv
Step 5 - Set project to use current python version
 - In Terminal Window run python --version
 - Edit Pipfile and change the version of python
Step 6 - Install Project Dependencies
 - In Terminal Window run pipenv install
Step 7 - Activate virtual environment
 - In Terminal Window type pipenv shell
Step 8 - Set Python Interpreter Path
 - Click on View > Command Palette
 - Enter Python: Select Interpreter and click on menu option
 - Enter path of python virtual environment ( should be path of project as set in Step 4 )
Step 9 - Run migrations with python manage.py migrate
Step 10 - Populate Database
 - Run python manage.py seed_db
 - If no script file in project, open seed.sql file in Workbench and run it
Step 11 - Create superuser
 - In Terminal Window run python manage.py createsuperuser
Step 12 - Run server
 - In Terminal Window run python manage.py runserver
 