# Peak fitness - gym booking system

## CodeClan - week 5 - Solo Project

## Introduction
This was my first project while studying software development at CodeClan. The timeframe for the project was one week (6th Oct -> 13th Oct 2022). The project marked the end of the first module where I learne the fundamental principles of software development. This included learning the following technologies and design patterns:
- Python3 with the Flask micro-framework
- Jinga2 templating engine
- SQL (with PostgreSQL object-relational database management system)
- Object-oriented programming
- Test-driven development(TDD)
- Representational state transfer architecture (RESTful development)
- Model-View-Controller architecture (MVC)

## Brief

The purpose of the project was to design an activity booking system for a gym. The task was to create software that manages the members, classes and bookings of a gym. The minimum viable product included enabling the user to create and edit members, create and delete classes, view a list of classes, assign a member to a class and view members attending each class.

## Planning

I began by mapping out the fundamental features of the application by producing a series of wireframes allowing me to visualise the components and how the app would be structured. I also mapped out the relationships between the tables in my database using class diagrams.

#### Wireframes

<img src="https://github.com/ST3V3NP3RRY/Peak_fitness_gym_app/blob/main/Wireframes.png">

#### Class and Object Diagrams

<img src="https://github.com/ST3V3NP3RRY/Peak_fitness_gym_app/blob/main/Class%20Diagram.png" >

## Design 

The wanted the completed applications to be easy to use with clear headings and signposts guiding the user through completing the tasks while using the app. I designed the app  to be mobile responsive so the it would work as intended on various viewports and device dimensions. This gave me the opportunity to research and utilise flexbox and CSS Media quieries to provide the functionality I needed within the application.

#### Screenshots of the completed application (desktop view)

<img src="https://github.com/ST3V3NP3RRY/Peak_fitness_gym_app/blob/main/Group%20Screenshots.png">

## How to run the application

Python_project

To run Peak Fitness Booking app do the following:

- DROP any existing conflicting db managers in terminal: 'dropdb peak_fitness'
- CREATE your db manager in terminal: 'createdb peak_fitness'
- JOIN the two with the following terminal command and create your tables: 'psql -d peak_fitness -f peak_fitness.sql'
- LOAD existing data in terminal by: 'python3 console.py'
- RUN the app so you can access local host in terminal by: 'flask run'
- OPEN host by clicking on '* Running on http://127.0.0.1:5000' use either option/cmd click to open this in a new browser







