'''Checks if the day already exists in the dictionary'''
def add_daily_temp( temp_dict, temp,day ):
    if day not in temp_dict: #Only add if the day is not already recorded
        temp_dict[day]=temp
    return temp_dict #Return the dictionary

#Example usage
weekly_temps ={}
print(add_daily_temp(weekly_temps,30,'Monday'))
print(add_daily_temp(weekly_temps,25,'Tuesday'))
print(add_daily_temp(weekly_temps,28,'Monday'))