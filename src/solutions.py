from pprint import pprint


def sort_people(list_people, sort_by, asc_desc):
    if asc_desc == 'asc':
        list_people.sort(key=lambda p: p[sort_by])
    else:
        list_people.sort(key=lambda p: p[sort_by], reverse=True)


people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
sort_people(people_list, 'age', 'asc')
print(people_list)


def filter_males(list_people):
    only_males = list(filter(lambda p: p['sex'] == 'male', people_list))
    return only_males


filtered_list = filter_males(people_list)
print(filtered_list)


def bmi(person):
    bmi_calc = round(person['weight_kg'] / person['height_meters'] ** 2, 1)
    new_list = {**person, 'bmi': bmi_calc}
    return new_list


def calc_bmi(list_people):
    new_list = list(map(bmi, list_people))
    return new_list


people_list_2 = [
    {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
    {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
]
new_people_list = calc_bmi(people_list_2)
print(new_people_list)


def get_people(list_people):
    new_list = [p['name'] for p in list_people if p['age'] >= 15]
    return new_list


print(get_people(people_list))
