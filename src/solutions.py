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
print()