# Example usage:
if __name__ == "__main__":
    from database import create_database_connection, create_habits_table, insert_habit, create_new_habit, \
        display_habits, load_habits_from_database, update_habit_in_database, delete_habit_from_database

    connection = create_database_connection("habit_tracker.db")
    create_habits_table(connection)

    habits = load_habits_from_database(connection)

    while True:
        print("Menu:")
        print("1. Create a new habit")
        print("2. Modify a habit")
        print("3. View all habits")
        print("4. Check off a habit")
        print("5. Delete a habit")
        print("6. Quit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            new_habit = create_new_habit(habits)
            if new_habit is not None:
                habits.append(new_habit)
                insert_habit(connection, new_habit)
        elif choice == '2':
            display_habits(habits)
            selection = int(input("Enter the number of the habit to modify: ")) - 1
            if 0 <= selection < len(habits):
                habit_to_modify = habits[selection]
                new_frequency = input("Enter the new frequency (e.g., Daily, Weekly): ")
                new_target_streak = int(input("Enter the new target streak (in days): "))
                print("Your habit has been modified successfully.")
                habit_to_modify.update_habit(new_frequency, new_target_streak)
                update_habit_in_database(connection, habit_to_modify)
            else:
                print("Invalid selection. Please try again.")
        elif choice == '3':
            display_habits(habits)
        elif choice == '4':
            display_habits(habits)
            selection = int(input("Enter the number of the habit to check off: ")) - 1
            if 0 <= selection < len(habits):
                habit_to_check_off = habits[selection]
                habit_to_check_off.record_completion()
                update_habit_in_database(connection, habit_to_check_off)
            else:
                print("Invalid selection. Please try again.")
        elif choice == '5':
            display_habits(habits)
            selection = int(input("Enter the number of the habit to delete: ")) - 1
            if 0 <= selection < len(habits):
                habit_to_delete = habits[selection]
                habits.remove(habit_to_delete)
                habit_to_delete.delete_habit()
                delete_habit_from_database(connection, habit_to_delete.name)
                print(f"{habit_to_delete.name} has been deleted.")
            else:
                print("Invalid selection. Please try again.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

    connection.close()
