import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Yamini@07",
            database="focusforge"
        )
        print("✅ Connected to FocusForge database!")
        return connection

    except mysql.connector.Error as e:
        print("❌ Error:", e)
        return None


if __name__ == "__main__":
    conn = create_connection()
    if conn:
        conn.close()
        print("🔌 Connection closed.")
