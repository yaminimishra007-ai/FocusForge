from add_session import add_session
from view_sessions import view_sessions

def main_menu():
    while True:
        print("\n===== 📘 FocusForge Menu =====")
        print("1. Add Study Session")
        print("2. View All Sessions")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_session()
        elif choice == "2":
            view_sessions()
        elif choice == "3":
            print("👋 Exiting FocusForge. Stay focused!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
