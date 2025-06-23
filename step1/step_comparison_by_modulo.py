import random
import json


# a = int(input())
# b = int(input())

# print(a**637 % 17)
# print(b % 17)


print("куда мчим ?")

my_dict = json.load(open("data.json", "r"))
my_choice = random.choice(list(my_dict))

my_dict[my_choice] += 1

json.dump(my_dict,  open("data.json", "w"), indent=4)  # Запись в файл


print(f"Идем в: {my_choice} увеличен на: {my_dict}")




