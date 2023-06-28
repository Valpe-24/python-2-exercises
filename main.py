
# Update with the exercise you are trying to test
from src import test
from src import solutions


def main():
    test.hello()

    #  Ex1
    solutions.sort_people(solutions.people_list, 'age', 'asc')
    print(solutions.people_list)

    #  Ex2
    print(solutions.filter_males(solutions.people_list))

    #  Ex3
    new_people_list = solutions.calc_bmi(solutions.people_list_2)
    print(solutions.new_people_list)

    #  Ex4
    print(solutions.get_people(solutions.people_list))


if __name__ == '__main__':
    main()
