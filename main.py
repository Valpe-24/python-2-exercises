
# Update with the exercise you are trying to test
from src import test
from src import solutions


def main():
    test.hello()

    solutions.sort_people(solutions.people_list, 'age', 'asc')
    print(solutions.people_list)

    print(solutions.filter_males(solutions.people_list))


if __name__ == '__main__':
    main()
