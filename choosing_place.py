def get_destination_list(loc, loc_type):
        east_city = [ "New York City", "Boston", "Miami", "Orlando", "Washington DC", "Chicago"]
        east_nature = [ "Niagara Falls", "Shenandoah National Park", "Acadia National Park"]
        west_city =  [ "LA", "Las Vegas", "San Francisco", "Seattle", "Hawaiian Islands"]
        west_nature = ["Yosemite", "Yellowstone", "Grand Canyon", "Anchorage"]
      
        if (loc == "east"):
             if (loc_type == "city"):
               return east_city
             if (loc_type == "nature"):
               return east_nature


        if (loc == "west"):
             if (loc_type == "city"):
               return west_city
             if (loc_type == "nature"):
               return west_nature

def select_destination(destination_list):
   print("\n!---Available Destinations---!")
   i=0
   while i < len(destination_selection_list):
        print(f"{i+1}. {destination_selection_list[i]}")
        i += 1
   destination=""
   size = len(destination_list)
   while True:
        choice = input("Enter the number of your favorite destination: ")
        if choice.isdigit() and int(choice) > 0 and int(choice) <= size:
             destination = destination_list[int(choice) - 1]
             break
        else: print("Please enter a valid input")
   return destination

vacation=""
while vacation != "yes" and vacation != "no":
   vacation = input("Are you looking to go on a vaction this summer in the US? (Yes/No): ").lower()


if vacation == "yes":
   location = ""
   while location != "east" and location != "west":
       location = input("Would you like to go East or West? (East/West): ").lower()
      
   place_type = ""
   while place_type != "city" and place_type != "nature":
       place_type = input("Would you like to be in a city or nature (City/Nature): ").lower()


   destination_selection_list = get_destination_list(location, place_type)
   selected_destination = select_destination(destination_selection_list)        
   print(f"\nYou've chosen: {selected_destination}!")
