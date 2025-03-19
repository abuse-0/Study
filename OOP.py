# Наследование, полиморфизм, абстракция, инкапсуляция

# Отличие метода объекста от метода класса

'''
Вот тут я передал name "Бобик" в def __init__, а затем создал
именно self.name - атрибут объекта, чтобы мог использовать
переданное значение в будущем
'''
class Dog:
    def __init__(self, name, age):
        self.name = name

my_dog = Dog("Бобик")


'''Классы и объекты
1. В питоне объекты создаются на основе классов. Класс - это шаблон или форма, определеяющая
атрибуты и методы, которые будут присутствовать в объексте

Переменные класса и объекта = атрибуты класса и объекта
'''

class Dog:
    def __init__(self, name, age): # Магический метод
        self.name = name # Атрибут
        self.age = age # Атрибут

    def bark(self): # Метод
        return "Гав-гав!"
    
# Создание объекста
my_dog = Dog("Бобик", 3)

# Использование метода
print(my_dog.bark()) # Гав-гав!

'''Наследование
2. Одной из основных принципов ООП является наследование,
которое опзоволяет создавать новые классы на основе уже 
суещствующих. Наследование позволяет повторно использовать
код и добавлять новые функциональные возможности.
'''

# Наследуются все методы и атрибуты
# Не наследуется привиатный атрибут и метод __hidden_var, __private_method()

class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        return "Животное говорит"
    

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name) # Вызывает метод __init__ из класса Animal

# Переопределение метода(без этого было бы: Животное говорит)
    def talk(self):
        return "Мяу!"
    
# Создание объекта
my_cat = Cat("Мурзик")

# Использование метода
print(my_cat.talk()) # Мяу!

## Прикол

class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def greetings(self):
        return self.name + ": yo"

# Создание объекта
my_cat = Cat("Мурзик")

# Использование метода
print(my_cat.greetings()) # Мурзик: yo

# Расширение __init__ с помощью super()

class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Вызываем __init__ родителя, передаем только name
        self.color = color  # Добавляем новое поле

# Создание объекта
my_cat = Cat("Мурзик", "рыжий")

# Вывод атрибутов объект
print(my_cat.name, my_cat.color) # Мурзик рыжий

    
''' Полиморфизм
3. Полиморфизм позволяет объектам разных классов иметь одинаковые методы,
но с разными реализациями. Это позволяет нам работать с объектами разных
классов, используя общий интерфейс.
'''

# 2 Класса наследуют метод area y Shape, который не делает ничего и переопределяют
class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
# Создание объектов
my_rectangle = Rectangle(5, 3)
my_circle = Circle(4)

# Удобно вот так вот потом юзать
print(my_rectangle.area())
print(my_circle.area())

# Вот так еще можно делать потом

shapes = [Rectangle(5, 3), Circle(4)]

for shape in shapes:
    print(shape.area())  

'''Абстракция
4. Абстракция позволяет скрывать сложные детали реализации и предоставлять 
только необходимые методы для взаимодействия с объектом. Это упрощает 
использование классов, предоставляя пользователю только важные методы 
и свойства.
'''

from abc import ABC, abstractmethod

# Запрещает создавать объекты от этого класса, переопределять метод(без этого не создастся объект)
class Transport(ABC):
    def __init__(self, speed):
        self.speed = speed  # Общий атрибут скорости

    @abstractmethod
    def move(self):
        pass  # Метод без реализации (заставляет подклассы его реализовать)


class Car(Transport):
    def move(self):
        return f"Машина едет со скоростью {self.speed} км/ч"


class Airplane(Transport):
    def move(self):
        return f"Самолет летит со скоростью {self.speed} км/ч"


# Создаем объекты
my_car = Car(100)
my_airplane = Airplane(900)

# Вызываем методы
print(my_car.move())       # Машина едет со скоростью 100 км/ч
print(my_airplane.move())  # Самолет летит со скоростью 900 км/ч


# Пример
class Airplane(Transport):
    pass

print(my_airplane.move())  # Самолет летит со скоростью 900 км/ч
# TypeError: Can't instantiate abstract class Airplane with abstract method move
# Если без него, то вывело бы просто None без ошибки

'''Инкапсуляция
5. Инкапсуляция обеспечивает скрытие данных и методов внутри класса. Это
позволяет изолировать данные и методы от внешнего доступа, что улучшает
безопасность и упрощает использование классов. В Python инкапсуляцию можно
достичь путем использования префиксов "__" или "_" перед именами атрибутов
и методов
'''
# __account_number и __balance скрыты от внешнего доступа
# вместо них реализованы методы depist, withdraw, get_balance

class BankAccount:
    def __init__(self, account_number, balance, negr):
        self.__account_number = account_number
        self.__balance = balance
        self.negr = negr

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            return "Недостаточно средств"
        
    def get_balance(self):
        return self.__balance
    
# Создание объекта
my_account = BankAccount('12345678', 1000, 456)

# Внесение деползита и вывод баланса
my_account.deposit(500)
print(my_account.get_balance()) # 1500

# Снятие денег и вывод баланса
print(my_account.withdraw(200)) # 200
print(my_account.get_balance()) # 1300


# Пример
print(my_account.__balance) # AttributeError: 'BankAccount' object has no attribute '__balance'.
print(my_account.__account_number) # AttributeError: 'BankAccount' object has no attribute '__account_number'