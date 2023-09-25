import sqlite3
from habits import HabitTrackerApp


def create_database_connection(database_name):
    """
    Create a connection to the SQLite database.

    Args:
        database_name (str): The name of the database file.

    Returns:
        sqlite3.Connection: The database connection.
    """
    return sqlite3.connect(database_name)


def create_habits_table(connection):
    """
    Create the 'habits' table in the database if it doesn't exist.

    Args:
        connection (sqlite3.Connection): The database connection.
    """
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            frequency TEXT,
            target_streak INTEGER,
            current_streak INTEGER
        )
    ''')
    connection.commit()


def insert_habit(connection, habit):
    """
    Insert a new habit into the 'habits' table.

    Args:
        connection (sqlite3.Connection): The database connection.
        habit (HabitTrackerApp): The habit object to insert.
    """
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO habits (name, frequency, target_streak, current_streak)
        VALUES (?, ?, ?, ?)
    ''', (habit.name, habit.frequency, habit.target_streak, habit.current_streak))
    connection.commit()


def create_new_habit(habits):
    """
    Create a new habit and check if a habit with the same name already exists.

    Args:
        habits (list): List of existing habits.

    Returns:
        HabitTrackerApp or None: The created habit object or None if a habit with the same name exists.
    """
    name = input("Enter the habit name: ")

    for habit in habits:
        if habit.name == name:
            print("A habit with the same name already exists. Please choose a different name.")
            return None

    frequency = input("Enter the habit frequency (e.g., Daily, Weekly): ")
    target_streak = int(input("Enter the target streak in periods (days/weeks): "))

    print("Your new habit has been created.")
    return HabitTrackerApp(name, frequency, target_streak)


def display_habits(habits):
    """
    Display a list of habits with their details.

    Args:
        habits (list): List of habit objects.
    """
    if not habits:
        print("There are no current habits.")
    else:
        for i, habit in enumerate(habits):
            print(f"{i + 1}. Habit: {habit.name}")
            print(f"   Frequency: {habit.frequency}")
            print(f"   Target Streak: {habit.target_streak}")
            print(f"   Current Streak: {habit.current_streak} days")
            print(f"   Created On: {habit.creation_date_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print()  # Add a blank line to separate habits


def load_habits_from_database(connection):
    """
    Load habits from the 'habits' table in the database.

    Args:
        connection (sqlite3.Connection): The database connection.

    Returns:
        list: List of habit objects.
    """
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM habits')
    habits = []
    for row in cursor.fetchall():
        habit = HabitTrackerApp(row[1], row[2], row[3])
        habit.current_streak = row[4]
        habits.append(habit)
    return habits


def update_habit_in_database(connection, habit):
    """
    Update a habit's information in the 'habits' table.

    Args:
        connection (sqlite3.Connection): The database connection.
        habit (HabitTrackerApp): The habit object to update.
    """
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE habits
        SET frequency = ?, target_streak = ?
        WHERE name = ?
    ''', (habit.frequency, habit.target_streak, habit.name))
    connection.commit()


def delete_habit_from_database(connection, habit_name):
    """
    Delete a habit from the 'habits' table.

    Args:
        connection (sqlite3.Connection): The database connection.
        habit_name (str): The name of the habit to delete.
    """
    cursor = connection.cursor()
    cursor.execute('DELETE FROM habits WHERE name=?', (habit_name,))
    connection.commit()


def update_run_streak(connection, habit_name, run_streak):
    """
    Update the run streak of a habit in the 'habits' table.

    Args:
        connection (sqlite3.Connection): The database connection.
        habit_name (str): The name of the habit to update.
        run_streak (int): The new run streak value.
    """
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE habits
        SET current_streak = ?
        WHERE name = ?
    ''', (run_streak, habit_name))
    connection.commit()
