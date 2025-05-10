# Online Fit Trainer App

A fitness management application designed for trainers to manage and keep track of members' information, vital details, subscriptions, workout plans, and nutrition plans.

## Prerequisites

- Python with Flask
- MySQL workbench 
   1- You will need to import my files(stored in database folder) in your workbench
   2- You will need to change the mysql_config(file `app/database.py`) with yours
   3- mysql.connector: Ensure that you have the mysql.connector module installed to interact with MySQL databases in the Python environment.
- Modern web browser with localStorage support
- Jinja (only used in two html pages(edit_member, member_profile))

- to run the website use `flask --app .\server.py run --debug  `


## Project Checklist

- [x] Uses the Flask web framework.
- [x] Contains at least one class with properties and methods.
  - File name for the class definition: `app/classes.py`
  - Line number(s) for the class definition: `7` ,`94` , `121`
  - Name of properties for `Member` class: `name`, `birthdate`,`gender`,`name`,
        `height`,`weight`, `phone`,`email`,`id`
   - Name of properties for `Package` class: `name`, `value`,`duration`,`id`
   - Name of properties for `vital-details` class: `member_id`, `fitnessGoals`,`medications`
        ,`allergy`,`disease`,`bodyFatPercentage`
  - Name of all methods for `Member` class: `add_to_DB`, `get_subscription`,
        `calculate_age`,`calculate_bmr`
  - Name of method for `package` class: `add_to_DB`
  - Name of method for `Vital-details` class: `add_to_DB`
  - File name and line numbers where the methods used:
   `app/html_handling` ->`22`,`29` 
   `member_profile.html`-> `33`,`48`
   `app/classes.py`-> `26` 
   `app/functions.py` -> `192`,

- [x] Styled using CSS and responsive to smaller screens.
- [x] Follows code and style conventions.

## Features

- Member management(`add`,`edit`,`search by name or ID`,`delete`,`view`, `view profile`)
- Vital details tracking(`add`,`delete`,`view`)
- Subscription handling(`subscripe` if not subscriped or expired,
                        `resubscripe` if the user already has valid subscription)
- Workout plans(`add`, `view`, `print`)
- Nutrition plans(`add`, `view`, `print`)


## Using of local storage
- The main usage is to keep track of the selected package in member profile after
  leaving and returning to the page.
- LocalStorage is used to store the trainer name.


## Usage of file (read and write)
- Files used to store member's workout program and nutration plan as each memebr has
  directorie to store two text files for him. 

## Usage of database 
- MYSQL database is used whith Three tables created to hold the main information of the (members, packages, vital details) 

## Contact
- Gmail: m.jehad.kh@gmail.com
- linkedIn: https://eg.linkedin.com/in/jehadkh
- GitHub: https://github.com/MohamadJehad
