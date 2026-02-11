import mysql.connector
import matplotlib.pyplot as plt

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yamini@07",
        database="focusforge"
    )

def visualize_focus():
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT subject, focus_score FROM study_sessions"
    cursor.execute(query)
    data = cursor.fetchall()

    if not data:
        print("No data to visualize.")
        return

    subjects = [row[0] for row in data]
    scores = [row[1] for row in data]

    plt.figure()
    plt.bar(subjects, scores)
    plt.xlabel("Subjects")
    plt.ylabel("Focus Score (%)")
    plt.title("Focus Score Per Study Session")
    plt.show()

    cursor.close()
    connection.close()

if __name__ == "__main__":
    visualize_focus()
