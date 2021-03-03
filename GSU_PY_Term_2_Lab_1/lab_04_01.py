import time


class Ticket:
    def __init__(self, date, name, deadline):
        self.createDate = date
        self.owner = name
        self.deadline = deadline

    def __del__(self):
        print("Delete ticket:", time.asctime(self.createDate))

    def display(self):
        print("Ticket:")
        print(" createDate: ", time.asctime(self.createDate))
        print(" owner: ", self.owner)
        print(" deadline:", time.asctime(self.deadline))


# создание объекта класса
ticket1 = Ticket(time.localtime(), "Ivan Ivanov", time.strptime("25.02.2021", "%d.%m.%Y"))
# вызов метода
ticket1.display()
# получение значения атрибута
print("Owner: ", ticket1.owner)
print("Owner(getattr): ", getattr(ticket1, "owner"))
# проверка наличия атрибута
print("hasattr: ", hasattr(ticket1, "owner"))
# установка значения атрибута
setattr(ticket1, "owner", "Alexei Petrov")
print("Owner(setattr): ", ticket1.owner)
# удаление значения атрибута
print("delattr: ", ticket1.owner)
delattr(ticket1, "owner")
# удаление объекта
print(ticket1)
del ticket1

print(time.asctime())

time.strptime("17.07.2017 10:53:00", "%d.%m.%Y %h:%M:%s")
