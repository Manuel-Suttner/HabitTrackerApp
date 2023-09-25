import datetime


class HabitTrackerApp:
    """
    Represents a habit tracking application.

    Attributes:
        name (str): The name of the habit.
        frequency (str): The frequency of the habit (e.g., 'Daily', 'Weekly').
        target_streak (int): The target streak in periods (days or weeks).
        current_streak (int): The current streak of the habit.
        last_checked_off_date (datetime.date): The date when the habit was last checked off.
        completion_history (list of datetime.date): A list of completion dates.
        creation_date_time (datetime.datetime): The date and time when the habit was created.
    """

    def __init__(self, name, frequency, target_streak):
        """
        Initializes a new habit.

        Args:
            name (str): The name of the habit.
            frequency (str): The frequency of the habit (e.g., 'Daily', 'Weekly').
            target_streak (int): The target streak in periods (days or weeks).
        """
        self.name = name
        self.frequency = frequency
        self.target_streak = target_streak
        self.current_streak = 0
        self.last_checked_off_date = None
        self.completion_history = []
        self.creation_date_time = datetime.datetime.now()

    def record_completion(self):
        """
        Records a completion for the habit and updates the streak.
        """
        today = datetime.date.today()
        if self.last_checked_off_date != today:
            self.current_streak += 1
            self.last_checked_off_date = today
            print(f"{self.name} has been marked as complete for today!")
        else:
            print(f"{self.name} has already been checked off today.")

    def update_habit(self, frequency, target_streak):
        """
        Updates the habit's frequency and target streak.

        Args:
            frequency (str): The new frequency of the habit (e.g., 'Daily', 'Weekly').
            target_streak (int): The new target streak in periods (days or weeks).
        """
        self.frequency = frequency
        self.target_streak = target_streak

    def delete_habit(self):
        """
        Deletes the habit and resets streak information.
        """
        print(f"Deleting habit: {self.name}")
        self.current_streak = 0
        self.last_checked_off_date = None

    @staticmethod
    def display_habits(habits):
        """
        Displays a list of habits.

        Args:
            habits (list of HabitTrackerApp): List of HabitTrackerApp objects.
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
                print("")  # Add a blank line to separate habits

    def check_reset_streak(self):
        """
        Checks and resets the streak if necessary based on the habit's frequency.
        """
        desired_frequency = self.frequency.lower()
        last_checked_off_date = self.last_checked_off_date

        if last_checked_off_date is None:
            last_checked_off_date = datetime.date.today()

        current_date = datetime.date.today()

        threshold = current_date

        if desired_frequency == 'daily':
            threshold = last_checked_off_date + datetime.timedelta(days=1)
        elif desired_frequency == 'weekly':
            threshold = last_checked_off_date + datetime.timedelta(weeks=1)

        if current_date > threshold:
            self.current_streak = 0
            self.last_checked_off_date = None
            print(f"{self.name}'s streak has been reset to 0 days.")

    def check_streak_milestone(self):
        """
        Checks and prints a message when a streak milestone is achieved.
        """
        desired_frequency = self.frequency.lower()

        daily_milestone = 14  # 14 consecutive days
        weekly_milestone = 4  # 4 consecutive weeks

        if desired_frequency == 'daily' and self.current_streak == daily_milestone:
            print(f"Congratulations! You've achieved a {daily_milestone}-day streak for {self.name}!")
        elif desired_frequency == 'weekly' and self.current_streak == weekly_milestone:
            print(f"Congratulations! You've achieved a {weekly_milestone}-week streak for {self.name}!")

    def longest_streak(self):
        """
        Calculates and returns the longest streak for the habit.

        Returns:
            int: The longest streak in days.
        """
        if not self.completion_history:
            return 0

        current_date = datetime.date.today()
        max_streak = 0
        streak = 0

        for date in self.completion_history:
            if (current_date - date).days <= 1:
                streak += 1
            else:
                max_streak = max(max_streak, streak)
                streak = 0

        return max(max_streak, streak)

    def current_longest_run_streak(self):
        """
        Calculates and returns the current longest run streak for the habit.

        Returns:
            int: The current longest run streak.
        """

        if not self.completion_history:
            return 0

        current_date = datetime.date.today()
        streak = 0

        for date in reversed(self.completion_history):
            if (current_date - date).days <= 1:
                streak += 1
                current_date = date  # Update current_date to the checked-off date
            else:
                break

        return streak

    def __str__(self):
        """
        Returns a string representation of the habit.

        Returns:
            str: A string containing habit information.
        """
        return (f"Habit: {self.name}\nFrequency: {self.frequency}\nTarget Streak: {self.target_streak}"
                f"\nCurrent Streak: {self.current_streak}")
