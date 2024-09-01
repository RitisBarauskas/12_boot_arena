from random import randint, uniform, choice, sample
from classes import *


names_persons = [
    'Рудеус Грейрат',
    'Сильфи Грейрат',
    'Эрис Грейрат',
    'Пауло Грейрат',
    'Зенит Грейрат',
    'Рокси Мигурдия',
    'Орстед',
    'Гислен Дедольдия',
    'Риния Дедольдия',
    'Пурсена Дедольдия',
    'Хитогами',
    'Элинализ Драгонард',
    'Атофератофе Райбэк',
    'Обер Корвет',
    'Бадигади',
    'Нина Фарион',
    'Клифф Гремуар',
    'Рейда Реина',
    'Руйджерд Супердия',
    'Золдат Хэклер',
    'Каруман Второй'
]

names_things = (
    'Плащ',
    'Красное кольцо',
    'Синее кольцо',
    'Ложка',
    'Шлем',
    'Щит',
    'Меч',
    'Кружка пива',
    'Сапоги',
    'Очки',
    'Вилка'
)

# Создаём предметы
things = sorted(
    [Thing(
        choice(names_things),
        randint(1, 5),
        randint(1, 5),
        round(uniform(0.01, 0.1), 2))
        for _ in range(10)], key=lambda x: x.protection
)

# Создаём персонажей
characters = [choice((Person, Warrior, Paladin))(
    names_persons.pop(names_persons.index(choice(names_persons))),
    randint(1, 10),
    randint(1, 10),
    round(uniform(0.01, 0.1), 2)) for _ in range(4)
]

# Даём персонажам предметы
for character in characters:
    character.set_things(sample(things, randint(1, 4)))
