# Exam-Portal

## Overview
A complete Exam Portal System built using Django. Currently, the portal has login system(with authentication) for admin(the top level supervisor), professors and students with their respective homepage; MCQ questions, question papers, student groups and exams can be created/edited by professors; students can appear for exams allotted to them within the time constraints set by the professor and then view their marks and solutions after completing the exam.

## Running
For running the project, navigate to the project directory and type the following in the command line:
* python manage.py makemigrations (or cli/makemigrations.sh)
* python manage.py migrate (or cli/migrate.sh)
* python manage.py runserver (or cli/runserver.sh)

The project will start in localhost **127.0.0.1:8000/**. Open the same on any browser and the login page of the project will load.