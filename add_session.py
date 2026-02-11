import mysql.connector
from datetime import datetime

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yamini@07",
        database="focusforge"
    )

def calculate_focus_score(start, end, break_minutes):
    total_minutes = (end - start).total_seconds() / 60
    actual_study = total_minutes - break_minutes
    
    if total_minutes == 0:
        return 0
    
    focus_score = (actual_study / total_minutes) * 100
    return round(focus_score, 2)

def add_session():
    subject = input("Enter subject: ")
    start_input = input("Enter start time (YYYY-MM-DD HH:MM:SS): ")
    end_input = input("Enter end time (YYYY-MM-DD HH:MM:SS): ")
    break_minutes = int(input("Enter break minutes: "))

    start_time = datetime.strptime(start_input, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(end_input, "%Y-%m-%d %H:%M:%S")

    focus_score = calculate_focus_score(start_time, end_time, break_minutes)

    connection = create_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO study_sessions 
    (subject, start_time, end_time, break_minutes, focus_score)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (subject, start_time, end_time, break_minutes, focus_score)

    cursor.execute(query, values)
    connection.commit()

    print("✅ Study session added successfully!")
    print("📊 Focus Score:", focus_score, "%")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    add_session()
