from pprint import pprint

def create_cook_book(filename,encoding):
    cook_book = {}
    with open(filename,encoding=encoding) as file:
        for line in file:
            dish = line.strip()
            num_ingredients = int(file.readline())

            temp_list=[]
            for item in range(num_ingredients):
                ingr_name,quantity,measure = file.readline().strip().split("|")
                temp_list.append(
                    {'ingredient_name': ingr_name, 'quantity': quantity, 'measure': measure}
                )

            file.readline()
            cook_book[dish] = temp_list
    return cook_book

pprint(create_cook_book('recipies.txt','UTF-8'))




