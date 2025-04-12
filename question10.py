'''This program write a function called add_daily_temp'''
def get_daily_temps():
    temp_dict = {}  # Empty dictionary
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for day in days:
        temp_dict[day] = float(input(f"Enter temperature for {day}: "))  # Get user input and store

    return temp_dict  # Return the dictionary

# Example usage
print(get_daily_temps())
