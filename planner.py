num_days = ""
   while not num_days.isdigit() or int(num_days) <=0:
        num_days = input ("How many days are you planning to travel: ")
        if not num_days.isdigit() or int(num_days) <=0:
             print("Please enter a valid number")
   num_days = int(num_days)
