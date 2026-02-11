#  FocusForge – Smart Study Time Analyzer

FocusForge is a Python + MySQL based CLI application that helps students track, analyze, and visualize their study sessions.

##  Features

- Add study sessions
- Calculate focus score automatically
- View all stored sessions
- Analytics:
  - Total study hours
  - Average focus score
  - Most productive subject
- Data visualization using matplotlib

##  Tech Stack

- Python
- MySQL
- matplotlib
- mysql-connector-python

##  Installation

1. Install required libraries:
   pip install -r requirements.txt

2. Make sure MySQL is installed and running.

3. Create the database:
   CREATE DATABASE focusforge;

4. Run the project:
   python main.py

##  Focus Score Formula

Focus Score = (Actual Study Time / Total Session Time) × 100

---

Built as a first-year backend data project.
