# Initialize variables to count total attendances and missed last day count
total_attendances = 0
missed_last_day_count = 0

# Function to calculate attendance probability recursively
def attendance_probability(previous, current, missed_count, days_count, target_attendance, miss_flag):
    global total_attendances
    global missed_last_day_count

    # Base case: if missed attendance exceeds 4, set miss flag and return
    if missed_count >= 4:
        miss_flag = True
        return

    # Base case: if current day is the target attendance day
    if days_count == target_attendance:
        # Concatenate previous and current attendance
        attendance_str = previous + current
        # If miss flag is set, return without further processing
        if miss_flag:
            return
        # If current attendance is 'A', increment missed last day count
        if current == 'A':
            missed_last_day_count += 1
        # Increment total attendances
        total_attendances += 1
        return

    # Recursive calls for both present and absent scenarios
    attendance_probability(previous=previous + current, current="P",
                        missed_count=0, days_count=days_count + 1, target_attendance=target_attendance, miss_flag=miss_flag)
    attendance_probability(previous=previous + current, current="A",
                        missed_count=missed_count + 1, days_count=days_count + 1, target_attendance=target_attendance, miss_flag=miss_flag)
    return

# Input number of days
N=int(input("Enter the number of days: "))
# Calculate attendance probability
attendance_probability("", "", 0, 0, N, False)
# Print missed last day count and total attendances
print("the number of ways to attend the class: "+ str(total_attendances))
print(str(missed_last_day_count)+'/'+str(total_attendances))
