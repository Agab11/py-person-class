class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        result_list.append(Person(name, age))

    for person in people:
        name = person["name"]
        obj = Person.people[name]
        if "wife" in person and person["wife"] is not None:
            wife_name = person["wife"]
            obj.wife = Person.people[wife_name]
        elif "husband" in person and person["husband"] is not None:
            husband_name = person["husband"]
            obj.husband = Person.people[husband_name]

    return result_list
