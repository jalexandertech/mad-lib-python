"""
This program is to present my skill in Python. I will build a mad lib based on what I have learned from w3schools and codecademy. 

Mad Lib - Story will be about someone's vacation. 

I will include nouns, adjective, name, a place, verbs, animals, food, number, and a type of transportation
"""
# Variables

place1 = input("Enter name of place: ")
verb1 = input("Enter the verb: ")
transportation = input("Enter the type of transportation: ")
number = input("Enter number of hours: ")
noun1 = input("Enter a noun:")
noun2 = input("Enter a noun:")
verb2 = input("Enter the verb: ")
noun3 = input("Enter a noun: ")
food = input("Enter food here: ")
place2 = input("Enter name of place: ")

#Story: What I did on my vacation - Mad Lib
def vacationStory():
    print("Last summer, my family and I went to " + place1 + " on vacation. We " + verb1 + " in a " + transportation + \
    " and it took " + number + " hours to get there. I took lots of photos of " + noun1 + " there, and saw " + noun2 + " " + verb2 + " in the " \
    + noun3 + ". I loved eating " + food + " at " + place2 + ". I had so much fun when I went to " + place1 + ". I can't wait to go back again!") 

vacationStory()
