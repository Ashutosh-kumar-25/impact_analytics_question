total_attendances = 0
missed_last_day_count = 0


def attendance_probability(previous, current, missed_count, days_count, target_attendance, miss_flag):
    global total_attendances
    global missed_last_day_count

    if missed_count >= 4:
        miss_flag = True
        return

    if days_count == target_attendance:
        attendance_str = previous + current
        if miss_flag:
            return
        if current == 'A':
            missed_last_day_count += 1
        total_attendances += 1
        return

    attendance_probability(previous=previous + current, current="P",
                        missed_count=0, days_count=days_count + 1, target_attendance=target_attendance, miss_flag=miss_flag)
    attendance_probability(previous=previous + current, current="A",
                        missed_count=missed_count + 1, days_count=days_count + 1, target_attendance=target_attendance, miss_flag=miss_flag)
    return

N=int(input("give the number of days: "))
attendance_probability("", "", 0, 0, N, False)
print(str(missed_last_day_count)+'/'+str(total_attendances))
