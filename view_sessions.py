import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yamini@07",
        database="focusforge"
    )

def classify_focus(score):
    if score >= 80:
        return "🔥 Deep Focus"
    elif score >= 50:
        return " Average"
    else:
        return "⚠️ Distracted"

def view_sessions():
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM study_sessions"
    cursor.execute(query)

    sessions = cursor.fetchall()

    if not sessions:
        print("No study sessions found.")
        return

    print("\n📚 Study Sessions:\n")

    for session in sessions:
        id, subject, start, end, break_min, score = session
        status = classify_focus(score)

        print(f"ID: {id}")
        print(f"Subject: {subject}")
        print(f"Start: {start}")
        print(f"End: {end}")
        print(f"Break: {break_min} mins")
        print(f"Focus Score: {score}%")
        print(f"Status: {status}")
        print("-" * 40)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    view_sessions()
