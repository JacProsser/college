import datetime
date_string = input("date: ")
date_string = str(date_string)
date_format = '%m/%y'
try:
  date_obj = str(datetime.datetime.now().strptime(date_string, date_format))
except ValueError:
  print("Incorrect date format, should be MM/YY")


datee = date_obj


  
if date_string > datee:
    print("Valid")
elif date_string < datee:
    print("Invalid")