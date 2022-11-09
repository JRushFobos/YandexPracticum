#Принципы ООП
# Абстракция - Родительский класс.
class MeleeWeapon:

    # Конструктор родительского класса.
    def __init__(self, name):
        # Свойства родительского класса: название оружия и прочность.
        self.name = name
        self.strength = 100
    
    # Метод родительского класса — рубящий удар.
    def slashing_blow(self):
        # При рубящем ударе уменьшаем прочность меча на 10.
        self.strength -= 10
        return f'Нанесён рубящий удар оружием {self.name}.'
    
    # Метод родительского класса — заточка оружия.
    def sharpen(self):
        # При заточке восстанавливаем стартовую прочность оружия.
        self.strength = 100
        return (f'Оружие "{self.name}" заточено.')

# Дочерний класс Sword.        
class Sword(MeleeWeapon):
    ...

# Дочерний класс Axe.
class Axe(MeleeWeapon):
    pass

# Создаём объекты дочерних классов.
# Скандинавский боевой топор.
brodex = Axe('Верный')
# Древнегреческий одноручный меч.
xiphos = Sword('Разящий')

# Каждый из дочерних классов имеет такие же методы и свойства, что и родительский.
brodex.slashing_blow()
xiphos.sharpen()

#--------------------------------------------------------
#Наследование - Дочерний класс
...

class Axe(MeleeWeapon):

    # В классе-наследнике определяется конструктор
    # с собственным параметром material.
    def __init__(self, name, material):
        # Вызываем конструктор класса-родителя.
        super().__init__(name)
        # Передаём значение параметра в новое свойство.
        self.material = material

    # Объявляем собственный для класса Axe метод.
    def slashing_blow(self):
        # Описываем логику работы метода дочернего класса.
        print('СОКРУШИТЕЛЬНЫЙ УДАР!')
        # Возвращаем результат выполнения метода slashing_blow() в родительском классе.
        return super().slashing_blow()  

# Теперь при создании объекта класса Axe
# нужно обязательно указывать два параметра:
# название и материал.
brodex = Axe('Верный', "железо")

print(brodex.slashing_blow())
... 
#--------------------------------------------------------

class MeleeWeapon:

    def __init__(self, name):
        self.name = name
        self.strength = 100
    
    # Метод родительского класса.
    def slashing_blow(self):
        # При рубящем ударе уменьшаем прочность меча на 10.
        self.strength -= 10
        return f'Нанесён рубящий удар оружием {self.name}.'
    
    def sharpen(self):
        self.strength = 100
        return (f'Оружие "{self.name}" заточено.')


class Sword(MeleeWeapon):

    # Переопределяем метод родительского класса...
    def slashing_blow(self):
        # ...меняем значение снижения прочности...
        self.strength -= 5
        # ...и меняем сообщение.
        return f'Мечом {self.name} был нанесен рубящий удар.'

# Этот класс-наследник полностью наследует все методы и свойства
# родительского класса.
class Axe(MeleeWeapon):
    ...

brodex = Axe('Верный')
xiphos = Sword('Разящий')

# Для класса Sword будет вызыван переопределённый метод.
print(xiphos.slashing_blow())
# Для класса Axe будет вызван метод родительского класса.
print(brodex.slashing_blow())
# Исходное значение прочности для класса Sword будет уменьшено
# на переопределённое значение.
print(xiphos.strength)
# Исходное значение просности для класса Axe будет уменьшено
# на значение, указанное в родительском классе.
print(brodex.strength)

#--------------------------------------------------------
#3 - Инкапсуляция — объединение и скрытие методов и свойств,
#и предоставление доступа к ним через простой внешний интерфейс.

#--------------------------------------------------------
#Полиморфизм — возможность взаимодействовать с объектами разных классов через
#одинаковые интерфейсы, обращаться к свойствам и методам, общим для всех объектов.
#--------------------------------------------------------
#ООП: практика 3/6
class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color

    def describe(self, full=False):
        if full:
            return (f'Попугай {self.name} — заметная птица, '
                    f'окрас её перьев — {self.color}, '
                    f'а размер — {self.size}. '
                    'Интересный факт: попугаи чувствуют ритм, '
                    'а вовсе не бездумно двигаются под музыку. '
                    'Если сменить композицию, '
                    'то и темп движений птицы изменится.')
        return super().describe()

    # Добавьте метод repeat().
    def repeat(self, phrase):
        self.phrase = phrase
        return f'Попугай {self.name} говорит: {self.phrase}.'


class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus

    def describe(self, full=False):
        if full:
            return (f'Размер пингвина {self.name} '
                    f'из рода {self.genus} — {self.size}. '
                    'Интересный факт: однажды группа геологов-разведчиков '
                    'похитила пингвинье яйцо, '
                    'и их принялась преследовать вся стая, '
                    'не пытаясь, впрочем, при этом нападать. '
                    'Посовещавшись, похитители вернули птицам яйцо, '
                    'и те отстали. ')
        return super().describe()

    # Добавьте метод swimming().
    def swimming(self, swimming):
        self.swimming = swimming
        return f'Пингвин {self.name} плавает со средней скоростью 11 км/ч.'


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')


print(kesha.repeat('Кеша хороший!'))
print(kowalski.swimming('Ковальски'))

#--------------------------------------------------------
#ООП: практика 5/6
# импортируем функции из библиотеки math для рассчёта расстояния
from math import radians, sin, cos, acos


class Point:
    def __init__(self, latitude, longitude):
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)

    # считаем расстояние между двумя точками в км
    def distance(self, other):
        cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(other.latitude) * cos(
        self.longitude - other.longitude)

        return 6371 * acos(cos_d)


class City(Point):
    def __init__(self, latitude, longitude, name, population):
        # допишите код: сохраните свойства родителя
        # и добавьте свойства name и population
        super().__init__(latitude, longitude)
        self.name = name
        self.population = population

    def show(self):
        print(f"Город {self.name}, население {self.population} чел.")


class Mountain(Point):
    # допишите код: напишите конструктор, в нём сохраните свойства родителя
    # и добавьте свойства name и height
    def __init__(self, latitude, longitude, name, height):
        # допишите код: сохраните свойства родителя
        # и добавьте свойства name и population
        super().__init__(latitude, longitude)
        self.name = name
        self.height = height
    # Создайте метод show(self):
    # информацию о горе нужно вывести в формате:
    # "Высота горы <название> - <высота> м."
    def show(self):
        print(f"Высота горы {self.name} - {self.height} м.")


# эта функция печатает расстояние
# между двумя любыми наследниками класса Point
def print_how_far(geo_object_1, geo_object_2):
    print(f'От точки «{geo_object_1.name}» до точки «{geo_object_2.name}» — {geo_object_1.distance(geo_object_2)} км.')


# основной код
moscow = City(55.7522200, 37.6155600, 'Москва', 12615882)
everest = Mountain(27.98791, 86.92529, 'Эверест', 8848)
chelyabinsk = City(55.154, 61.4291, 'Челябинск', 1200703)

moscow.show()
everest.show()
print_how_far(moscow, everest)
print_how_far(moscow, chelyabinsk)

#--------------------------------------------------------
#--------------------------------------------------------
#ООП: практика 6/6
class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю.')
    
    def __str__(self):
        print(f'{self.name}')

class Student(Human):
    def __init__(self, name):
        super().__init__(name)
    def ask_question(self, someone, question):
        self.someone = someone
        self.question = question
    
        print(f'{someone.name}, {question}')
        someone.answer_question(question)
        print()

class Mentor(Human):
    def __init__(self, name):
        super().__init__(name)

    def answer_question(self, question):
        if question == 'как устроиться работать питонистом?':
            print('Сейчас расскажу.')
        elif question == 'мне грустненько, что делать?':
            print('Отдохни и возвращайся с вопросами по теории.')
        else:
            super().answer_question(question)

class Curator(Human):
    def __init__(self, name):
        super().__init__(name)
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Держись, всё получится. Хочешь видео с котиками?')
        else:
            super().answer_question(question)

class CodeReviewer(Human):
    def __init__(self, name):
        super().__init__(name)
    def answer_question(self, question):
        if question == 'что не так с моим проектом?':
            print('О, вопрос про проект, это я люблю.')
        else:
            super().answer_question(question)

student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')