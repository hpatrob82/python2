meal = {
    "drink": "beer",
    "appetizer": "nachos",
    "entree": "tacos",
    "dessert": "churros"
}

meal["water"] = "fizzy"
meal["quesadilla"] = False
print(meal)
if "quesadilla" in meal and "quesadilla" == True:
    print("Hilda had a quesadilla")
else:
    print("Hilda did NOT have a quesadilla")