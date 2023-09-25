import habits
import unittest
from predefined_habits import initialize_predefined_habits


class TestHabitStreaks(unittest.TestCase):
    def setUp(self):
        # Initialize predefined habits and tracking data
        initialize_predefined_habits()

    def test_daily_habit_streak(self):
        # Test streak calculation for daily habit (Exercise Daily)
        habit1 = habits.get_habit_by_name()
        self.assertEqual(habit1.current_streak, 28)  # Assuming 28 days of tracking

    def test_weekly_habit_streak(self):
        # Test streak calculation for weekly habit (Read Weekly)
        habit2 = habits.get_habit_by_name()
        self.assertEqual(habit2.current_streak, 4)  # Assuming 4 weeks of tracking

    def test_daily_habit_reset(self):
        # Test streak reset for daily habit (Meditate Daily)
        habit3 = habits.get_habit_by_name()
        self.assertEqual(habit3.current_streak, 0)  # Streak should be reset

    def test_weekly_habit_reset(self):
        # Test streak reset for weekly habit (Write Weekly)
        habit4 = habits.get_habit_by_name()
        self.assertEqual(habit4.current_streak, 0)  # Streak should be reset


if __name__ == "__main__":
    unittest.main()
