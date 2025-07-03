import datetime


class Person:
    def __init__(self, name, age, date):
        self.name = name
        self.age = age
        self.date = date

    def __str__(self):
        return f'Person(Name = {self.name}, Age = {self.age}, Date = {self.date})'

def collect_user_input():
    people = []
    print("Welcome to the Personal Data Collector!")
    print("Press Ctrl+C at any time to stop input.")

    try:
        while True:
            try:
                name = input("Please enter your name: ")
                if not name  or not name.isalpha():
                    raise ValueError("Name cannot be empty and must be alphanumerical. Please try again.")

                age = int(input("Please enter your age: "))
                if age < 0:
                    raise ValueError("Age can not be negative. Please try again.")

                date = datetime.datetime.now().strftime('%m/%d/%Y')
                person = Person(name, age, date)
                people.append(person)
                print(f"'{person}' has been successfully added to the list.")

            except ValueError as e:
                 print(e)
            finally:
                print("Waiting for the next entry...")

    except KeyboardInterrupt:
        print("Data collection terminated.")

    print("Collected Data:")
    for person in people:
        print(person)

if __name__ == '__main__':
    collect_user_input()