from player import Player
import price
import army


def choose_race(name):
    race = input(
        "{}, пришло время выбрать сторону: Гондор или Изенгард? ".format(name)).lower()
    if not (race in ("1", '2', 'изенгард', 'гондор')):
        print("incorrect input")
        return choose_race(name)
    else:
        return race


def read_base_info():
    name = input("Доброго времени суток!\nВведи своё имя: ")
    choosen_race = choose_race(name)
    # choosen_race = choose_race(name)
    player = Player(name=name, race=choosen_race)
    player.create_army(input(
        "Введи название своей первой армии: "))
    # player.create_castle(name=input("Введи название своей первой крепости: "), owner=Player.name)
    print("Отлично, {}, хорошей игры и пусть удача всегда будет на твоей стороне!".format(name))
    return player


def choice_of_action(player):
    while True:
        action = input(
            'Выбери действие: \n1) Отправиться в поход\n2) Развивать войска\n3) Развивать замки\n4) Закрыть игру\n')
        if action == '1':
            crusade(player)
        elif action == '2':
            develop_troops(player)
        elif action == '3':
            print("in development")
            # develop_castles()
        elif action == '4':
            break


def try_to_int(x):
    try:
        return int(x)
    except:
        return x


def upgrade_number_of_steps(player, index_current_army):
    while True:
        cur_value = player.army[index_current_army].number_of_steps
        print(cur_value)
        if cur_value < army.max_number_of_steps:
            choice = input("Текущий запас хода {}. Улучшение будет стоить {} золота.\nВ данный момента у игрока {} золота. Произвести улучшение?\n".format(
                cur_value, price.number_of_steps[cur_value], player.gold))
            if choice.lower() in "да" or choice == '1':
                if player.gold >= price.number_of_steps[cur_value]:
                    player.set_number_of_steps(index_current_army)
                else:
                    print("У вас недостаточно золота")
                    break
            elif choice.lower() in 'нет' or choice == '2':
                break
            else:
                print("Некорректный ввод")
        else:
            print("Запас хода твоей армии максимален, так держать!")
            break


def upgrade_morale(player, index_current_army):
    while True:
        cur_value = player.army[index_current_army].morale
        if float(cur_value) < army.max_morale:
            choice = input("Текущий боевой дух {}. Улучшение будет стоить {} золота.\nВ данный момента у игрока {} золота. Произвести улучшение?\n".format(
                cur_value, price.morale[cur_value], player.gold))
            if choice.lower() in "да" or choice == '1':
                if player.gold >= price.morale[cur_value]:
                    player.set_morale(index_current_army)
                else:
                    print("У вас недостаточно золота")
                    break
            elif choice.lower() in 'нет' or choice == '2':
                break
            else:
                print("Некорректный ввод")
        else:
            print("Боевой дух твоей армии максимален, так держать!")
            break


def develop_economy_of_army(player, index_current_army):
    while True:
        print("Выбери, что ты хочешь улучшить:")
        print("1) Увеличить запас хода армии")
        print("2) Поднять боевой дух армии")
        print("3) Вернуться назад")
        action = input()
        if action == '1':
            upgrade_number_of_steps(player, index_current_army)
            break
        elif action == '2':
            upgrade_morale(player, index_current_army)
            break
        elif action == '3':
            break
        else:
            print("Некорректный ввод")


def hire_troops(player, index_current_army):
    try:
        index_squad = int(input(
            "Введи номер отряда до {}, в который ты хочешь нанимать войска. Если хочешь создать новый отряд - введи 0.\n".format(len(player.army[index_current_army].squads)))) - 1
        player.show_squad(index_current_army, index_squad)
        print("Введи тип юнита для найма и количество: ")
    except:
        print("Введите корректный аргумент")
        hire_troops(player, index_current_army)
    try:
        _type, _quantity = map(try_to_int, input().split())
        player.army[index_current_army].hire(
            index_squad, _type, _quantity)
    except ValueError:
        print("Введите два корректных аргумента")
        hire_troops(player, index_current_army)


def crusade(player):
    print("in development")


def develop_troops(player):
    while True:
        action = input(
            'Выбери действие: \n1) Развивать существующие армии\n2) Создавать новые\n3) Вернуться назад\n')
        if action == '1':
            print('Выбери номер армии: ')
            for i in range(len(player.army)):
                print('{}) {}'.format(i + 1, player.army[i].name_army))
            while True:
                try:
                    index_current_army = int(input()) - 1
                    break
                except:
                    print("Некорректный ввод")
            while True:
                sub_action = input(
                    "1) Развивать экономику\n2) Нанимать войска\n3) Вернуться назад\n")
                if sub_action == '1':
                    develop_economy_of_army(player, index_current_army)
                elif sub_action == '2':
                    hire_troops(player, index_current_army)
                elif sub_action == '3':
                    break  # нужно сделать переход к след части кода
        elif action == '2':
            name_army = input("Введи название армии: ")
            player.create_army(name_army)
        elif action == '3':
            break
