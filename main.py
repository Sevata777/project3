# Таюрский С.В. FPY-82. Д. З. Открытие и чтение файла, запись в файл
# Задание №1

cook_book = {}
with open('recipes.txt', encoding='utf-8') as file:
    # x: str
    for x in file:
        food_name = x.strip()
        ingredients = []
        y = file.readline()
        for i in range(int(y)):
            z = file.readline()
            ingredient_name, quantity, measure = z.strip().split(' | ')
            ingredients.append({'ingredient_name': ingredient_name,
                                'quantity': quantity,
                                'measure': measure})
            w = {food_name: ingredients}
        q = file.readline()
        cook_book.update(w)
# from pprint import pprint
# print('cook_book = ')
# pprint(cook_book, width=130, indent=2)

# Задание №2

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    p = 0
    for dish in dishes:
        if dish in cook_book:
            for exist in cook_book[dish]:
                p = int(exist['quantity'])*int(person_count)
                name = exist['ingredient_name']
                if name not in shop_list:
                    shop_list_temp = {name: {'measure': exist['measure'], 'quantity': p}}
                    shop_list.update(shop_list_temp)
                else:
                    j = shop_list[name].setdefault('quantity')
                    p = p+j
                    shop_list_temp = {name: {'measure': exist['measure'], 'quantity': p}}
                    shop_list.update(shop_list_temp)
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')
    # print(shop_list)
    # from pprint import pprint
    # pprint(shop_list, width=130, indent=2)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# Задание №3

with open('1.txt', encoding='utf-8') as file:
    text1 = []
    txt_1 = {}
    txt_11 = {}
    id1 = 0
    for f in file.readlines():
        id1 += 1
        text1.append(f)
    txt_1 = {id1: text1}
    text_11 = {id1: '1.txt'}

with open('2.txt', encoding='utf-8') as file:
    text2 = []
    txt_2 = {}
    txt_22 = {}
    id2 = 0
    for f in file.readlines():
        id2 += 1
        text2.append(f)
    txt_2 = {id2: text2}
    text_22 = {id2: '2.txt'}

with open('3.txt', encoding='utf-8') as file:
    text3 = []
    txt_3 = {}
    txt_33 = {}
    id3 = 0
    for f in file.readlines():
        id3 += 1
        text3.append(f)
    txt_3 = {id3: text3}
    text_33 = {id3: '3.txt'}

text_all = {}
text_all_sort = {}
text_all_sort_dict = {}
text_all = txt_1 | txt_2 | txt_3

text_all_sort = sorted(text_all.items())
text_all_sort_dic = dict(text_all_sort)

with open('result.txt','w',encoding='utf-8') as file:
    for k, v in text_all_sort_dic.items():
        if k == id1:
            file.write('\n')
            file.write(text_11[id1])
            file.write('\n')
            file.write(str(k))
            file.write('\n')
        if k == id2:
            file.write('\n')
            file.write(text_22[id2])
            file.write('\n')
            file.write(str(k))
            file.write('\n')
        if k == id3:
            file.write('\n')
            file.write(text_33[id3])
            file.write('\n')
            file.write(str(k))
            file.write('\n')
        res = ''.join(v)
        file.write(res)
        file.write('\n')


