from person import Person

my_friends = [
    Person('Ivan Ivanov', 18, 'M'),
    Person('Petr Petrov', 19, 'M'),
    Person('Georg Georg', 20, 'M')
]


def get_oldest_person():
    older = my_friends[0]

    for j in my_friends[1:]:
        if j.age > older.age:
            older = j

    older.print_person_info()