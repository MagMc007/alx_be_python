from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

days = int(input("Enter the number of days to add to the current date:"))

def calculate_future_date(days):
    future_date = datetime.now() + timedelta(days=days)
    print(future_date.strftime("%Y-%m-%d"))
display_current_datetime()
calculate_future_date(days)