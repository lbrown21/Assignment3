# task 1


attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees >= 100 else "conference room"
print(venue)


# task 2

attendees = 100
attendees = int(input("Enter number of attendees:"))

venue = "large hall" if attendees > 100 else "conference room"
facilities = ""

if attendees > 50:
    facilities += "audio system"
if attendees > 80:
    facilities += ", projector"

print("Venue:", venue)
print("Additional Facilities:", facilities)

# task 3

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

food_choice = input("Do you want vegetarian food? (yes/no): ")
caterer = "Veggie Delight Caterers" if food_choice.lower() == "yes" else "Gourmet Meals Caterers"
print(f"We recommend {caterer} for catering services.")






