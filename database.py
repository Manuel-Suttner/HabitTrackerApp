import sqlite3

from habits import HabitTrackerApp


def create_database_connection(database_name):
    return sqlite3.connect(database_name)


def create_habits_table(connection):
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
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO habits (name, frequency, target_streak, current_streak)
        VALUES (?, ?, ?, ?)
    ''', (habit.name, habit.frequency, habit.target_streak, habit.current_streak))
    connection.commit()


def create_new_habit(habits):
    name = input("Enter the habit name: ")

    for habit in habits:
        if habit.name == name:
            print("A habit with the same name already exists. Please choose a different name.")
            return None

    frequency = input("Enter the habit frequency (e.g., Daily, Weekly): ")
    target_streak = int(input("Enter the target streak (in days): "))

    print("Your new habit has been created.")
    return HabitTrackerApp(name, frequency, target_streak)


def display_habits(habits):
    if not habits:
        print("There are no current habits.")
    else:
        for i, habit in enumerate(habits):
            print(f"{i+1}. {habit}")


def load_habits_from_database(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM habits')
    habits = []
    for row in cursor.fetchall():
        habit = HabitTrackerApp(row[1], row[2], row[3])
        habit.current_streak = row[4]
        habits.append(habit)
    return habits


def update_habit_in_database(connection, habit):
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE habits
        SET frequency = ?, target_streak = ?
        WHERE name = ?
    ''', (habit.frequency, habit.target_streak, habit.name))
    connection.commit()


def delete_habit_from_database(connection, habit_name):
    cursor = connection.cursor()
    cursor.execute('DELETE FROM habits WHERE name=?', (habit_name,))
    connection.commit()
