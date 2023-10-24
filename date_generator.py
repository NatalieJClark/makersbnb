from datetime import date, timedelta

# Define the start and end dates for your calendar
start_date = date(2023, 1, 1)
end_date = date(2023, 12, 31)

# Define the step (usually one day)
day_step = timedelta(days=1)

# Initialize an empty list to store the dates
all_dates = []

# Use a loop to generate dates
current_date = start_date
while current_date <= end_date:
    all_dates.append(current_date)
    current_date += day_step