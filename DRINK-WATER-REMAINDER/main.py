import time
from plyer import notification

while True:
    try:
        time_interval = int(input("Enter the time interval in seconds: "))
        reminders = int(input("How many remainders do you want?: "))
        break
    except ValueError:
        print("Enter valid input!")

for _ in range(reminders):
    print("Please sip some water!")
    notification.notify(
        title="Please drink some water",
        message="You need to drink"
    )
    time.sleep(time_interval)

notification.notify(title = "Remainders:", message = "All remainders done!")
