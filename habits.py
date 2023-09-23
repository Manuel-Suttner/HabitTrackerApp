import datetime


class HabitTrackerApp:
    def __init__(self, name, frequency, target_streak):
        self.name = name
        self.frequency = frequency
        self.target_streak = target_streak
        self.current_streak = 0
        self.last_checked_off_date = None

    def record_completion(self):
        today = datetime.date.today()
        if self.last_checked_off_date != today:
            self.current_streak += 1
            self.last_checked_off_date = today
            print(f"{self.name} has been marked as complete for today!")
        else:
            print(f"{self.name} has already been checked off today.")

    def update_habit(self, frequency, target_streak):
        self.frequency = frequency
        self.target_streak = target_streak

    def delete_habit(self):
        print(f"Deleting habit: {self.name}")
        self.current_streak = 0
        self.last_checked_off_date = None

    def display_habits(habits):
        if not habits:
            print("There are no current habits.")
        else:
            for i, habit in enumerate(habits):
                print(f"{i + 1}. {habit}")

    def __str__(self):
        return (f"Habit: {self.name}\nFrequency: {self.frequency}\nTarget Streak: {self.target_streak}"
                f"\nCurrent Streak: {self.current_streak}")
