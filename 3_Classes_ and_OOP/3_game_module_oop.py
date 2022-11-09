# Поместите сюда код объявленных классов.
class Character:
    ...


class Warrior(Character):
    ...


class Mage(Character):
    ...
#--------------------------------------------------------
class Character:
    # Объявляем конструктор класса.
    def __init__(self, name):
        self.name = name
    
   # Объявляем метод атаки
    def attack(self):
        ...
    
    # Объявляем метод защиты.
    def defence(self):
        ...
    
    # Объявляем метод специального умения.
    def special(self):
        ...

class Warrior(Character):
    ...

class Mage(Character):
    ...

class Healer(Character):
    ... 
#--------------------------------------------------------
#Оптимизация
...
def attack(char_name: str, char_class: str) -> str:
    # Для Воина.
    if char_class == 'warrior':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(3, 5)}')
    # Для Мага.
    if char_class == 'mage':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(5, 10)}')
    # Для Лекаря.
    if char_class == 'healer':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(-3, -1)}')
    return (f'{char_name} нанёс противнику урон, равный 5')
... 
#----------------------V-----------------------------
class Character:

    def __init__(self, name):
        self.name = name
    
    def attack(self):
        # Описываем метод атаки.
        return (f'{self.name} нанёс противнику урон, равный '
                f'{5 + randint(5, 10)}')
    
    def defence(self):
        ...

    def special(self):
        ...

class Warrior(Character):
    ...

class Mage(Character):
    ...

class Healer(Character):
    ... 
#--------------------------------------------------------
#Глобальная константа
# Вот она — новая глобальная константа.
from random import randint

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10 

class Character:
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    # Вот они — две новые константы.
    SPECIAL_BUFF = 15
    SPECIAL_SKILL = 'Удача'

    def __init__(self, name):
        self.name = name

    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}.')

    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    def special(self):
        # Здесь описано тело метода special().
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

class Warrior(Character):
    ...

class Mage(Character):
    ...

class Healer(Character):
    ... 
#--------------------------------------------------------
#ИТОГ
from random import randint

DEFAULT_ATTACK = 5
# Новая константа — стандартное значение защиты.
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80 


class Character:
    # Новая константа.
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    # Константа для диапазона очков урона.
    RANGE_VALUE_ATTACK = (1, 3)
    # Новая переменная класса — диапазон значения защиты.
    RANGE_VALUE_DEFENCE = (1, 5)
    # Вот они — две новые константы.
    SPECIAL_BUFF = 15
    SPECIAL_SKILL = 'Удача'


    # Объявляем конструктор класса.
    def __init__(self, name):
        self.name = name
    

    def attack(self):
        # Описываем метод атаки.
        # Вместо диапазона записана переменная класса.
        # Оператор * распаковывает передаваемый кортеж.
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')
    

    def defence(self):
        # Вычисляем значение защиты в переменной value_defence.
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')
        
    
    def special(self):
        # Здесь описано тело метода special().
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    # Новый метод базового класса.
    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.' 

# Далее описываем классы-наследники.

class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита' 

#warrior = Warrior('Кодослав')
#print(warrior)
#print(warrior.attack())

def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """
    # Добавили словарь, в котором соотносится ввод пользователя и класс персонажа.
    game_classes = {
        'warrior': Warrior,
        'mage': Mage,
        'healer': Healer,
    } 

    approve_choice: str  = None
    
    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        # Вывели в терминал описание персонажа.
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class

    
def start_training(character):
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    # Замените конструкцию условных операторов на словарь.
    commands = {'attack': character.attack,
                'defence': character.defence,
                'special': character.special}
    
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        # Вместо блока условных операторов добавьте условие
        # принадлежности введённой команды словарю.
        # В функции print() будет вызываться метод класса,
        # который соответствует введённой команде.
        if cmd in commands:
            print(commands[cmd]())

    return 'Тренировка окончена.'

#--------------------------------------------------------
