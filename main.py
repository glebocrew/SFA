from random import choice as random_action
from colorama import Fore as foreground
from colorama import Back as background
from colorama import Style as reset

# победные комбинации:       
#   |  ПРЕДМЕТ  |    ЧТО БЬЁТ     |
#   |-----------|-----------------|
#   |   камень  |     бумага      |
#   |-----------|-----------------|
#   |   бумага  |    ножницы      |
#   |-----------|-----------------|
#   |   ножницы |     камень      |
#   |-----------|-----------------|

# Создаем словарь победных комбинаций
winners_list = \
{
    "камень": "ножницы",
    "ножницы": "бумага",
    "бумага": "камень"
}

items = ["камень", "ножницы", "бумага"]

print(f"Здравствуйте! \nВас приветсвует {foreground.CYAN}консольный чат-бот{reset.RESET_ALL} для игры в камень-ножницы-бумага.\nДля старта напишите {foreground.BLUE}/start{reset.RESET_ALL} \nДля окончания игры напишите {foreground.BLUE}/end{reset.RESET_ALL}")

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

command = input(">>>"  + foreground.GREEN)
print(reset.RESET_ALL)
if command not in ["/start", "/end"]:
    while (command not in ["/start", "/end"]):
        print("Некорректный ввод!")
        command = input(">>>" + foreground.GREEN)
        print(reset.RESET_ALL)



print("Введите сложность игры. \n1 - Случайная(приближенная к реальности)\n2 - Легкая(бот крайне глупый) \n3 - Алгоритмический(бот пытается рассчитывать свои ходы)")

hardness = input(">>>" + foreground.GREEN)
print(reset.RESET_ALL)
if hardness not in ["1", "2", "3"]:
    while (hardness not in ["1", "2", "3"]):
        print("Некорректный ввод!")
        hardness = input(">>>"+ foreground.GREEN)
        print(reset.RESET_ALL)



game_over = False
computer_points, user_points = 0, 0
computer_action = random_action(items)
previous_user = []
user_prediction = ""



while not game_over:
    print("Введите ваш ход (ТОЛЬКО 'камень', 'ножницы' или 'бумага')")
    user_input = input(">>>" + foreground.GREEN)
    print(reset.RESET_ALL)
    user_input = user_input.lower()
    if user_input == "/end":
        game_over = True
    else:
        if user_input.lower() in winners_list:
            if hardness == "1":
                computer_action = random_action(items)
            elif hardness == "2":
                pass
            elif hardness == "3": 
                if len(previous_user) < 2:
                    computer_action = random_action(items)
                else:
                    if previous_user[len(previous_user)-1] == \
                        previous_user[len(previous_user)-2]:

                        user_prediction = previous_user[len(previous_user)-1]
                        computer_action = get_key(winners_list,user_prediction)
                    else: 
                        current_count = \
                        {
                            "камень": 0,
                            "ножницы": 0,
                            "бумага": 0
                        }
                        for x in previous_user:
                            if x == items[0]:
                                current_count["камень"] += 1
                            elif x == items[1]:
                                current_count["ножницы"] += 1
                            elif x == items[2]:
                                current_count["бумага"] += 1

                        computer_action = get_key(current_count, min(current_count.values()))
                previous_user.append(user_input)
            print(f"{foreground.CYAN}Бот{reset.RESET_ALL} сделал свой ход: {foreground.CYAN}{computer_action}{reset.RESET_ALL}")
            if winners_list[computer_action] == user_input:
                print(f"В данном случае {foreground.CYAN}{computer_action}{reset.RESET_ALL} бьёт {foreground.GREEN}{user_input}{reset.RESET_ALL}.\nК сожалению, {foreground.RED}вы проиграли{reset.RESET_ALL} этот ход( \nПопробуйте выиграть следующий ход!")
                user_points += 1
            elif winners_list[user_input] == computer_action:
                print(f"Ну кто же не знает, что {foreground.GREEN}{user_input}{reset.RESET_ALL} бьёт {foreground.CYAN}{computer_action}{reset.RESET_ALL}! \nПоздравляю! {foreground.GREEN}Вы выиграли{reset.RESET_ALL} этот ход! \nСможете победить в следующем?)")
                computer_points += 1
            else:
                print("Каша малаша! Вы выдали одинаковые фигуры!")
        else:
            print("Вы ввели неправильное действие!")

print(f"Игра окончена! \nРезультаты: \n{foreground.GREEN}Вы{reset.RESET_ALL}:{user_points}\n{foreground.CYAN}Компьютер{reset.RESET_ALL}:{computer_points}")