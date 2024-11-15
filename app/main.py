class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name.lower()] = self


def create_person_list(people: list) -> list:
    person_list_people = []
    for person in people:
        name = Person(person["name"], person["age"])
        if person.get("wife"):
            name.wife = person["wife"]
        elif person.get("husband"):
            name.husband = person["husband"]
        person_list_people.append(name)
    return person_list_people
