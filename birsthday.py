from collections import defaultdict
from datetime import datetime, timedelta
# Данный код сделан из расчета  того, что сегодня в понедельник (04) я могу посмотреть дни рождения с субботы 02 по пятницу 08. 
# в файле birthday_old.py мой предыдущий код. Он более простой и расчитан на то, что выдаются день рождения на семь дней вперед,
# не считая сегодняшнего  
def get_birthdays_per_week(users):
    birthdays_by_day = defaultdict(list)
    today = datetime.today().date()
    today_day = datetime.today().strftime("%A")

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)


        if birthday_this_year < today: 
            if ((birthday_this_year - today).days)>-3 and today_day not in ["Monday", "Sanday", "Saturday" ]:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        delta_days = (birthday_this_year - today).days
     
        if delta_days<7 and delta_days>=-2:
            birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A")
            if delta_days<7 and delta_days>=0 and today_day not in ["Monday", 'Sunday','Saturday'] :
                if birthday_weekday in ['Sunday','Saturday']:
                    birthday_weekday='Monday'
            elif delta_days<7 and delta_days>5 and today_day=="Monday": 
                continue       
            elif delta_days>=-2 and delta_days<=0 and today_day=="Monday":
                birthday_weekday='Monday'
            elif delta_days>=-1 and delta_days==0 and today_day=="Sunday":
                birthday_weekday='Monday'
            elif delta_days==0 and today_day=="Sunday":
                birthday_weekday='Monday'   
        else:
            continue

        birthdays_by_day[birthday_weekday].append(name)

    for day, names in birthdays_by_day.items():
        print(f"{day}: {', '.join(names)}")


