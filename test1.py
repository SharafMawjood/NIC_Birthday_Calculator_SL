# months = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# month_names = (
#     'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
#     'December')

months = {'January': 31, 'February': 29, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31,
          'September': 30, 'October': 31, 'November': 30, 'December': 31}

month_names = list(months.keys())
month_days = list(months.values())


# nic = input('please enter your id: ')
# id_count = len(nic)


def nid(nic_days, months):
    bmonth = 0
    if nic_days > 366:
        nic_days = nic_days - 500

    month_count = 0
    day_sum = 0
    while day_sum < nic_days:
        day_sum += month_days[month_count]
        month_count += 1
        # print(month_count)
        # print(day_sum)
    month_count = -1
    day_sum -= month_days[month_count]



    if remaining_days == 0:
        month_count = month_count - 1

    remaining_days = nic_days - day_sum

    # for x in range(month_count):
    #     bmonth += months[x]
    #
    # remain_date = nic_days - bmonth
    return remaining_days, month_count -1


for i in range(1,367):
    birthday = nid(i,months)
    day, month = birthday
    result = f'Your birthday: {i}  {month_names[month]} {day}'
    print(result)


# if id_count == 10:
#     year = '19' + nic[:2]
#     id_days = int(nic[2:5])
#     birthday = nid(id_days, months)
#
#
# elif id_count == 12:
#     year = nic[:4]
#     id_days = int(nic[4:7])
#     birthday = nid(id_days, months)
#
# day, month = birthday
#
# result = f'Your birthday:{year} {month_names[month]} {day}'
# print(result)
