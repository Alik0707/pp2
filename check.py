class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Я животное по имени {self.name}"

class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name  # Вызываем конструктор родителя
        self.breed = breed      # Дополнительный атрибут

    def info(self):  # Переопределяем метод
        return f"{super().info()} и я породы {self.breed}"

dog = Dog("Шарик", "Овчарка")
print(dog.info())  # Я животное по имени Шарик и я породы Овчарка
