"""
Given a large integer representing a duration in total seconds, convert it into standard digital format tracking
Days, Hours, Minutes, and Seconds (DD:HH:MM:SS).
Sample Input: Seconds = 90061
Expected Output: Formatted Time: 01 days, 01 hours, 01 minutes, 01 seconds
"""

seconds = int(input("Enter seconds = "))
if seconds <= 60:
    print(f"Formatted Time: {seconds} seconds")
elif seconds > 60:
    minutes = seconds // 60
    seconds = seconds % 60
    if minutes <= 60:
        print(f"Formatted Time: {minutes} minutes, {seconds} seconds")
    elif minutes > 60:
        hours = minutes // 60
        minutes = minutes % 60
        if hours <= 24:
            print(f"Formatted Time: {hours} hours, {minutes} minutes, {seconds} seconds")
        elif hours > 24:
            days = hours // 24
            hours = hours % 24
            print(f"Formatted Time: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
        else:
            print("invalid input")


