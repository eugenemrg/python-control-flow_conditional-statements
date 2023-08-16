# Solutions before Python 3.10
dog = "cuddly"

# # Solution 1 
# if dog == "hungry":
#     owner = "Refilling food bowl."
# elif dog == "thirsty":
#     owner = "Refilling water bowl."
# elif dog == "playful":
#     owner = "Playing tug-of-war."
# elif dog == "cuddly":
#     owner = "Snuggling."
# else:
#     owner = "Reading newspaper."

dict_map = {
    "hungry": "Refilling food bowl.",
    "thirsty": "Refilling water bowl.",
    "playful": "Playing tug-of-war.",
    "cuddly": "Snuggling.",
}

# Remember that a dictionary's .get() method lets us set a default value!
owner = dict_map.get(dog, "Reading newspaper.")
print(owner)