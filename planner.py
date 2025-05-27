destinations = ["Hawaii", "New York", "Yellowstone", "San Diego", "Los Angeles", "San Fransisco", "Lake Tahoe", "Florida", "Yosemite", "Alaska", "Las Vegas", "Boston", "Chicago"]
print("Here are some top destinations for your summer vacation:")
for place in destinations:
    print("- " + place)

activities = []
for day in range(1,4):
    activity = input("What would you like to do on Day {}?")
    activities.append(activity)

print("\nYoir Vacation Schedule:")
for i in range(len(activities)):
    print("Day {i + 1}: {activities[i]}")
