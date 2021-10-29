import random
from random import randint


hp = 0
attak = 0
monster_counter = 0

def validate_input(txt):
    while txt not in ['1', '2',]:
        print('Необходимо ввести 1 или 2')
        txt = input('Ввести 1 или 2')
    return txt

def apple():
    global hp
    print('Ты нашел Матур-Алма! Вдруг прибавит здоровья')
    apple_hp = random.randint(1, 5)
    hp += apple_hp
    print(f'Высъели яблоко с силой {apple_hp}')
    print(f'Теперь у тебя силы {hp}')

def meetMonster():
    global monster_counter
    global hp
    
    monsterLvl = random.randint(1, 3)
    monster_hp = monsterLvl
    monster_dmg = monsterLvl * 2 - 1
    monsters = ['Кошмар-Бабай', 'Кошмар-Апа', 'Колотун-Бабай', 'Исярь-Малай', 'Сантый-Кэз']
    
    monster = random.choice(monsters)
    
    print(f'Ой-ой на твоем пути дракон {monster} у него {monsterLvl}уровен, {monster_hp}жизней и {monster_dmg} сила удара  и его пытались победить{monster_counter}')
    
    while monster_hp>0:
        s = input('Нажми 1 - Алга в атаку, 2 - бежать пока жив :')
        
        castomer_choise = validate_input(s)
        
        if s == '1':
            monster_hp -= monster_dmg
            print('Ты атаковал дракона и у него осталось' ,monster_hp, ' жизней')
        elif s == '2':
            chance = random.randint(0, monsterLvl)
            if chance == 0:
                print("Тебе удалось сбежать с поля боя!")
                break
            else:
                print("Монстр оказался чересчур сильным и догнал тебя... Батыр - Киттэ")
        else:
            continue
        
        if monster_hp > 0:
            hp -= monster_dmg
            print("Дракон атаковал и у тебя осталось", hp, "жизней.")
        
        if hp <= 0:
            break
    else:
        loot = random.randint(0, 2) + monsterLvl
        monster_counter += loot
        print("Тебе удалось одолеть дракона, за что ты получил", loot, "побед.")
        monster_counter()
 
        

def meetSword():
    global sword_attak
    global sword
    sword_attak = random.randint(2, 4)
    swords = ['Зур-Топор', 'Бензопила-Дуслык', 'Палка-Ган - бывает, раз в год и она стреляет!']
    sword = random.choice(swords)
    print(f'Это легендарный {sword}! У него {sword_attak} сила удара')
    d = input('Нажми 1 - взять новый легендарный меч и выбросить свой старый, 2 - Айда дальше, мой старый меч тоже хорош!')
    castomer_choise = validate_input(d)
    if castomer_choise == '1':
        print('Новый меч хоть и легендарный, но давно не был в бою...Удачи тебе с ним!')
        if sword_attak == attak:
                print('В твоих руках он обретает новую сиду!')
    else:
            print('Тоже вариант! Азарт порой губителен...')
            

def initGame(inithp, initattk, initmonster_counter):
    global hp
    global attak
    global monster_counter

    print(''' Салям Ипташ! Ты оказался в стране Башкыртастания, где
                тебе предстоит сразиться с дрраконами.
                 Хайэрле юл Урал-Батыр!''')


        
def gameLoop():
    situation = random.randint(2, 10)

    if situation == 2:
        meetMonster()
    elif situation == 1:
        meetSword()
    else:
        input("Ходим, бродим...")

initGame(4, 8, 4)
while True:
    gameLoop()

    if hp <= 0:
        if input("Хочешь начать сначала (да/нет да - 1, нет - 2): ").lower() == "1":
            initGame(4, 8, 4)
        else:
            break

  

