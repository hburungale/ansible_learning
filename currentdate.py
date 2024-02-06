# from datetime import date

# today = date.today()
# print(today)

# # Output:
# # 2022-10-11
from datetime import datetime

# current dateTime
now = datetime.now()

# convert to string
date_time_str = now.strftime("%d-%m-%Y")


# Output 2021-07-20 16:26:24