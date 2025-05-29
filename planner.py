num_days = ""
   while not num_days.isdigit() or int(num_days) <=0:
        num_days = input ("How many days are you planning to travel: ")
        if not num_days.isdigit() or int(num_days) <=0:
             print("Please enter a valid number")
   num_days = int(num_days)

num_travellers = ""
   while not num_travellers.isdigit() or int(num_travellers) <=0:
        num_travellers = input ("How many people are travelling: ")
        if not num_travellers.isdigit() or int(num_travellers) <=0:
             print("Please enter a valid number")
   num_travellers = int(num_travellers)

daily_plan = []
   print("\nLets plan what you want to do each day!!!")
   for day in range(1, num_days + 1):
        activity = input(f"What do you want to do on Day {day}? (e.g Amusment Park, Eating, Fishing, Hiking, Sight-Seeing): ")
        daily_plan.append(f"Day {day}: {activity}")
