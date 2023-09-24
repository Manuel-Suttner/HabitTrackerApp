import datetime
import habits
from database import create_new_habit


# Example predefined habits
def initialize_predefined_habits():
    habit1 = create_new_habit(habits)
    habit1.name = "Exercise Daily"
    habit1.frequency = "Daily"
    habit1.target_streak = 30

    habit2 = create_new_habit(habits)
    habit2.name = "Read Weekly"
    habit2.frequency = "Weekly"
    habit2.target_streak = 4

    habit3 = create_new_habit(habits)
    habit3.name = "Meditate Daily"
    habit3.frequency = "Daily"
    habit3.target_streak = 30

    habit4 = create_new_habit(habits)
    habit4.name = "Write Weekly"
    habit4.frequency = "Weekly"
    habit4.target_streak = 4

    # Example tracking data for "Exercise Daily" habit
    today = datetime.date.today()
    for _ in range(28):  # Assuming 4 weeks (28 days)
        habit1.record_completion()
        today -= datetime.timedelta(days=1)  # Move to the previous day

    # Example tracking data for "Read Weekly" habit
    today = datetime.date.today()
    for _ in range(4):  # 4 weeks
        habit2.record_completion()
        today -= datetime.timedelta(weeks=1)  # Move to the previous week

    # Example tracking data for "Meditate Daily" habit
    today = datetime.date.today()
    for _ in range(28):  # Assuming 4 weeks (28 days)
        habit3.record_completion()
        today -= datetime.timedelta(days=1)  # Move to the previous day

    # Example tracking data for "Write Weekly" habit
    today = datetime.date.today()
    for _ in range(4):  # 4 weeks
        habit4.record_completion()
        today -= datetime.timedelta(weeks=1)  # Move to the previous week
