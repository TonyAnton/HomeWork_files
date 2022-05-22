from pprint import pprint
import os


def name_file():
    name = input('Введите имя файла: ') + '.txt'
    return name


def open_file():
    name_open_file = name_file()
    file_directory = os.path.join(os.getcwd(), name_open_file)
    keys_list = ['ingredient_name', 'quantity', 'measure']
    cookbook = {}

    with open(file_directory, encoding='UTF-8') as file:
        for all_data in file:
            ingr_list = []
            dish_name = all_data
            amount_ingredients = int(file.readline())
            for ingredients in range(amount_ingredients):
                parse_str = str(file.readline().strip()).split('|')
                ingr_dict = {keys_list[i]: parse_str[i] for i in range(len(keys_list))}
                ingr_list.append(ingr_dict)
            file.readline()
            cookbook[dish_name.strip()] = ingr_list
    return cookbook


def get_shop_list_by_dishes(dishes, person_count):
    cookbook = open_file()
    ingr_dict = {}
    for dish_name in dishes:
        if dish_name in cookbook.keys():
            for ingredients in cookbook[dish_name]:
                ingredient = ingredients['ingredient_name']
                sum_quantity = int(ingredients['quantity']) * person_count
                measure = ingredients['measure']
                if ingredient not in ingr_dict.keys():
                    ingr_dict[ingredient] = {'quantity': sum_quantity, 'measure': measure}
                else:
                    ingr_dict[ingredient]['quantity'] += sum_quantity
        else:
            print(f'Блюдо {dish_name} не найдено')
    return ingr_dict


pprint(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Фахитос', 'Чизбургер'], 3))
