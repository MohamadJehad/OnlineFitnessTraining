# Online Fit Trainer App

A fitness management application designed for trainers to keep track of members' information, vital details, subscriptions, workout plans, and nutrition plans.

## Prerequisites

- Python with Flask
- MySQL workbench (as you will need to import my files(stored in database folder) in your workbench)
- Modern web browser with localStorage support
- Jinja (only used in one html page)


## Project Checklist

- [x] Available on GitHub.
- [x] Uses the Flask web framework.
- [x] Uses modules from the Python Standard Library.
  - Module name: `datetime`, `os`,`mysql`
- [x] Contains at least one class with properties and methods.
  - File name for the class definition: `server.py`
  - Line number(s) for the class definition: `28-117` ,`122-147` , `149-172`
  - Name of properties for `Member` class: `name`, `birthdate`,`gender`,`name`,
        `height`,`weight`, `phone`,`email`,`id`
   - Name of properties for `Package` class: `name`, `value`,`duration`,`id`
   - Name of properties for `vital-details` class: `member_id`, `fitnessGoals`,`medications`
        ,`allergy`,`disease`,`bodyFatPercentage`
  - Name of two methods for `Member` class: `add_to_DB`, `get_subscription`,
        `calculate_age`,`calculate_bmr`
  - Name of two methods for `package` class: `add_to_DB`
  - Name of two methods for `Vital-details` class: `add_to_DB`
  - File name and line numbers where the methods used: `server.py` -> `47`,`158`,`302`,`467`,`624`
                                                        `member_profile.html`-> `33`,``48``
- [x] Uses JavaScript in the front end and localStorage. 
- [x] Uses modern JavaScript.
- [x] Makes use of reading and writing to the same file feature.
- [x] Contains conditional statements.
  - File name: `server.py`
  - Line number(s): `34`,`45`,`108`, `128`,`245`,......
- [x] Contains loops.
  - File name: `server.py`
  - Line number(s): `202`, `226`, `299`,`330`,`670`,....
- [x] Lets the user enter a value in a text box.
- [x] Styled using CSS.
- [x] Follows code and style conventions.
- [x] All exercises completed and pushed to the respective GitHub repository.

## Features

- Member management(`add`,`search`,`delete`,`view`, `view profile`)
- Vital details tracking(`add`,`delete`,`view`)
- Subscription handling(`subscripe` if not subscriped or expired,
                        `resubscripe` if already has valid subscription)
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
- Three tables created to hold the main information of the (members, packages, vital details) 

## Contact
- Gmail: m.jehad.kh@gmail.com
- linkedIn: https://eg.linkedin.com/in/jehadkh
- GitHub: https://github.com/jehadkh