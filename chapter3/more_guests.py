guest_list = ['dad', 'grandpa', 'grandma']
print(f"{guest_list[0].title()}, you are invited to dinner!")
print(f"So are you {guest_list[1].title()}")
print(f"I wouldn't forget {guest_list[2].title()}, so much fun!")
print(f"Wait ... unfortunately {guest_list[1].title()} can't make it :(")
guest_list[1] = "hatred"
print(f"{guest_list[0].title()}, you are invited to dinner!")
print(f"So are you {guest_list[1].title()}")
print(f"I wouldn't forget {guest_list[2].title()}, so much fun!")
print("We found a bigger table! We'll be inviting more people!")
guest_list.insert(0, "bob")
guest_list.insert(2, "susan")
guest_list.append("Andrew")
print(guest_list)