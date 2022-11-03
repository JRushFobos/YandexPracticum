class Sword:

    def __init__(self, name, blade_length, grip, material='сталь'):
        self.name = name
        self.blade_length = blade_length
        self.material = material
        self.grip = grip
        self.strength = 10
        print(f'Новый меч {name} выкован!')
    
    def slashing_blow(self):
        self.strength -= 10
        return (f'Нанесён рубящий удар мечом {self.name}. '
                f'Радиус поражения: {self.blade_length}.')

    def piercing_strike(self):
        self.strength -= 5
        return (f'Нанесён пронзающий удар мечом {self.name}. '
                f'Рукоять {self.grip} мягко легла в руку.')

    def sharpen(self):
        self.strength = 100
        return (f'Меч "{self.name}" заточен,'
                f' {self.material} отлично поддалась обработке.')
    
    # Вот он — новый метод! Именно в нём описывается то, что должно выводиться
    # при печати объекта.
    def __str__(self):
        # Можно задать любую строку, например
        # «Не печатай меня, ведь я — объект!».
        # Но лучше пусть при печати выводится что-то осмысленное,
        # например имя объекта и его основные параметры.
        return (
            f'Меч — «{self.name}». ' 
            f'Выкован из материала {self.material}, '
            f'длина клинка — {self.blade_length}, '
            f'прочность — {self.strength}.'
        )


katana = Sword('Верный', 1.5,
               'хват двумя руками')
classic_sword = Sword('Дежурный', 1.2,
                      'хват одной рукой')

# Печатаем созданные объекты.
print(katana)
print(classic_sword)



# Импортируйте datetime. 
import datetime as dt
# Импортируйте time.
import time

#--------------------------------------------------------

import datetime as dt
import time

class Quest:
    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = None
        self.end_time = None

    def accept_quest(self):
        if self.end_time:
            return 'С этим испытанием вы уже справились.'
        self.start_time = dt.datetime.now()
        return f'Начало "{self.name}" положено.'

    def pass_quest(self):
        if not self.start_time:
            return 'Нельзя завершить то, что не имеет начала!'
        self.end_time = dt.datetime.now()
        completion_time = self.end_time - self.start_time
        return (f'Квест "{self.name}" окончен.'
                f' Время выполнения квеста {completion_time}')
    
    # Напишите код метода __str__.
    def __str__(self):
        if self.end_time:
            return (
                f'Цель квеста {self.name} - ' 
                f'{self.goal}. Квест завершён.'
                )
        elif self.start_time:
            return (
                f'Цель квеста {self.name} - ' 
                f'{self.goal}. Квест выполняется.'
                )
        else:
            return (
                f'Цель квеста {self.name} - ' 
                f'{self.goal}.'
                )
            

quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники'
quest_description = '''
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники'''

new_quest = Quest(quest_name, quest_description, quest_goal) 

print(new_quest.pass_quest())
print(new_quest.accept_quest())
time.sleep(3)
print(new_quest.pass_quest())
print(new_quest.accept_quest())

# Проверка печати объекта класса.
print(new_quest)

#--------------------------------------------------------

# Родительский класс.
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
#Наследование
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
#--------------------------------------------------------
#--------------------------------------------------------
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