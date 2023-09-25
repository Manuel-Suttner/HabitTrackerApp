# Example usage:

def filter_habits_by_periodicity(habits, periodicity):
    return [habit for habit in habits if habit.frequency.lower() == periodicity]
# Import necessary modules and functions


if __name__ == "__main__":
    from database import (
        create_database_connection,
        create_habits_table,
        insert_habit,
        create_new_habit,
        load_habits_from_database,
        update_habit_in_database,
        delete_habit_from_database,
        display_habits,
        update_run_streak,
    )

    # Create a database connection and initialize the habits table
    connection = create_database_connection("habit_tracker.db")
    create_habits_table(connection)

    # Load existing habits from the database
    habits = load_habits_from_database(connection)

    while True:
        print("Menu:")
        print("1. Create a new habit")
        print("2. Modify a habit")
        print("3. View all habits")
        print("4. Check off a habit")
        print("5. Delete a habit")
        print("6. Longest habit streak")
        print("7. Overall longest streak")
        print("8. Filter by periodicity")
        print("9. Quit")
        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")

        if choice == '1':
            # Create a new habit and add it to the list of habits
            habit = create_new_habit(habits)
            habits.append(habit)
            insert_habit(connection, habit)
            print(f"{habit.name} has been created on {habit.creation_date_time}")
        elif choice == '2':
            # Modify an existing habit's frequency and target streak
            display_habits(habits)
            selection = int(input("Enter the number of the habit to modify: ")) - 1
            if 0 <= selection < len(habits):
                habit_to_modify = habits[selection]
                new_frequency = input("Enter the new frequency (e.g., Daily, Weekly): ")
                new_target_streak = int(input("Enter the new target streak in periods (days/weeks): "))
                print("Your habit has been modified successfully.")
                habit_to_modify.update_habit(new_frequency, new_target_streak)
                update_habit_in_database(connection, habit_to_modify)
            else:
                print("Invalid selection. Please try again.")
        elif choice == '3':
            # View all habits
            display_habits(habits)
        elif choice == '4':
            # Check off a habit and update the streak
            display_habits(habits)
            selection = int(input("Enter the number of the habit to check off: ")) - 1
            if 0 <= selection < len(habits):
                habit_to_check_off = habits[selection]

                # Check and reset streak if necessary
                habit_to_check_off.check_reset_streak()

                habit_to_check_off.record_completion()
                update_habit_in_database(connection, habit_to_check_off)
                update_run_streak(connection, habit_to_check_off.name, habit_to_check_off.current_streak)
            else:
                print("Invalid selection. Please try again.")
        elif choice == '5':
            # Delete a habit
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
            # Calculate and display the longest streak for a certain habit
            if not habits:
                print("There are no current habits.")
            else:
                display_habits(habits)
                selection = int(input("Enter the number of the habit to check longest streak: ")) - 1
                if 0 <= selection < len(habits):
                    habit_to_check_streak = habits[selection]
                    longest_streak = habit_to_check_streak.longest_streak()
                    print(f"Longest streak for {habit_to_check_streak.name}: {longest_streak} days")
                else:
                    print("Invalid selection. Please try again.")
        elif choice == '7':
            # Calculate and display the overall longest current run streak across all habits
            max_streak_habit = None
            max_current_run_streak = 0
            for habit in habits:
                current_run_streak = habit.current_longest_run_streak()
                if current_run_streak > max_current_run_streak:
                    max_current_run_streak = current_run_streak
                    max_streak_habit = habit.name

            if max_streak_habit:
                print(f"Longest current run streak is for habit '{max_streak_habit}': {max_current_run_streak} days")
            else:
                print("There are no habits to calculate the longest current run streak.")
        elif choice == '8':
            # Filter habits by periodicity (Daily or Weekly)
            periodicity = input("Enter the periodicity (e.g., 'Daily' or 'Weekly'): ").strip().lower()
            matching_habits = filter_habits_by_periodicity(habits, periodicity)
            if matching_habits:
                print(f"Habits with {periodicity} periodicity:")
                display_habits(matching_habits)
            else:
                print(f"No habits with {periodicity} periodicity found.")
        elif choice == '9':
            # Quit the application
            break
        else:
            print("Invalid choice. Please try again.")

    connection.close()
