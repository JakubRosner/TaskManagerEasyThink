# Task Manager

There are 2 ways to run Task Manager.

## Non docker ver

TaskManager\settings.py:
    In section DATABASES you have to set your DB credencials.
        
Before you run app you have to run this commands:
    *python manage.py migrate*
    *python manage.py makemigrations*
    *python manage.py migrate*
    *python manage.py runserver*

## Docker ver

TaskManager\settings.py:
    In section DATABASES you have to set
         'HOST': 'db',
Before you run app you have to run this commands in container:
    *python manage.py makemigrations*
    *python manage.py migrate*
    *python manage.py runserver*


