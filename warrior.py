import random
#  импорт модуля рэндом
class Warrior:
    # создание класса воин и инициализация имени для того чтобы можно было вставлять его как значение, дальше идут статичные значение
    # не понимаю зачем нужна везде ссылка селф, и почему она обьявляется в аргументах у всех функций одинаково, если это ссылка, примерно понял что этот
    # момент для обьявления всех переменых которые будут использваться в следующих функциях и навигация по нему идет через точку и уточнения что именно берем

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.armor = 100
        self.endurance = 100
# создаем функцию по атаке , они месят друг друга по заданным параметрам
# я так понимаю взаимно дерутся они уже в баттл , а тут только обьявляются условия того как они наносят урон, но странно что для него прописывается принт
# в атак , а для второго в defend, это путает, я бы наверное пропиывал бы все рядом через elif, либо я неправильно что то понял
    def attack(self, other):
        if self.endurance > 0:
            self.endurance -= 10
            damage = random.randint(0, 10) if self.endurance == 0 else random.randint(10, 30)
            other.health -= damage
            print(f"{self.name} attacks {other.name} causing {damage} damage. {other.name} has {other.health} health left.")
        else:
            print(f"{self.name} is too tired to attack.")
# тут селф прописал броню как то им обоим?
# если я это правильно понял, скажи пожалуйста, концепция ооп вроде в этом и заключается просто пока трудно понять как имено это происходит, мне кажется в баттл уже

    def defend(self, other):
        if other.endurance > 0:
            if self.armor > 0:
                health_loss = random.randint(0, 20)
                armor_loss = random.randint(0, 10)
                self.health -= health_loss
                self.armor -= armor_loss
                print(f"{self.name} defends. Loses {health_loss} health and {armor_loss} armor. {self.name} has {self.health} health and {self.armor} armor left.")
            else:
                # тут если броня и энергия кончилась то не отнимается броня, отнимается здоровье
                # сначала я считал name это воин 1, а  other, воин 2, но сейчас становится понятно, что name это имена двух воинов, а other это их значение
                
                health_loss = random.randint(10, 30)
                self.health -= health_loss
                print(f"{self.name} defends but has no armor. Loses {health_loss} health. {self.name} has {self.health} health left.")

def battle(warrior1, warrior2):
    # здесь продолжается схватка если у обоих больше 10 хп и выбирается одно из действий для воинов, но что значит строка action1(warrior2)?
    while warrior1.health > 10 and warrior2.health > 10:
        action1 = random.choice([warrior1.attack, warrior1.defend])
        action2 = random.choice([warrior2.attack, warrior2.defend])
        action1(warrior2)
        if warrior2.health <= 10:
            # если хп 10 или меньше брейк
            break 
        action2(warrior1)
        if warrior1.health <= 10:
            break
    if warrior1.health > 10:
        # если у одного из хп больше он победитель и выбирает че делать со вторым
        winner = warrior1
    else:
        winner = warrior2

    decision = input(f"{winner.name} has won! Do you want to spare the loser? (yes/no): ")
    if decision.lower() == "yes":
        print("The loser has been spared.")
    else:
        print("The loser has been defeated.")
# тут задаются имена воинов, куда именно они записываются и как потом используется пока загадка
warrior1 = Warrior("Warrior 1")
warrior2 = Warrior("Warrior 2")
# тут применяется метод батл, к двум воинам, а погоди кажись понял, но если понял не доконца правильно скажи пожалуйста
# типа сейчас и назначаются эти именна для аргументов функции батл, а из батл уже просто применяются стандартные настройки для обоих?
battle(warrior1, warrior2)
