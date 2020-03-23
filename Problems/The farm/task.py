money = int(input())

animal_dict = {"chicken": 23, "goat": 678, "pig": 1296, "cow": 3848, "sheep": 6769}

most_expensive = animal_dict['chicken']
animal = ""

for key in animal_dict:
    if money >= animal_dict[key]:
        most_expensive = animal_dict[key]
        animal = key

number_of_animal = money // most_expensive
if number_of_animal > 0:
    if animal != "sheep":
        print(str(number_of_animal) + " " + animal + "s" if number_of_animal > 1 else
              str(number_of_animal) + " " + animal)
    else:
        print(str(number_of_animal) + " " + animal)
else:
    print("None")
