import datefinder
string_value = "my date of birth is January |22 and May|23"
matches = datefinder.find_dates(string_value) 
print(list(matches))          
for match in matches:
    print("match found ",match)


#----------------------------------------------------
import datetime
def get_date(s_date):
    date_patterns = ["%d-%m-%Y", "%Y-%m-%d"]

    for pattern in date_patterns:
        try:
            return datetime.datetime.strptime(s_date, pattern).date()
        except:
            pass

    print("Date is not in expected format: %s" %(s_date))

print(get_date("rahul 12-May-22"))


import datetime
regex = datetime.datetime.strptime
assert regex('2020-08-03', '%Y-%m-%d')
print("happymood")
assert regex('2020-08', '%Y-%m-%d')