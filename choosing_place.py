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
