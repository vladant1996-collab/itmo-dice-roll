import random
def create_profile(taken_names):
    while True:
        user_name = input("Введите ваше имя:")
        if user_name in taken_names:
            print("Это имя уже занято, выберите другое!")
        else:
            taken_names.append(user_name)
            break
    profile = {"name": user_name, "balance": 0, "status": "Базовый"}
    return profile
def main_screen(profile, taken_names):
    history = []
    price_adult_regime = 500
    while True:
        regime_choice = input("Выберите режим игры: (1 - игра с ботом, 2 - игра с соперником, 3 - Режим 18+, 4 - История мгр), 5 - Выход")
        if regime_choice == "1":
            print("Запускаем игру с ботом")
            player_roll = random.randint(1, 6)
            bot_roll = random.randint(1, 6)
            print(f"Игрок бросает кости и получает: {player_roll}, бот бросает кости и получает: {bot_roll}")
            if player_roll > bot_roll:
                result = f"{profile['name']} победил бота {player_roll} : {bot_roll}"
            elif player_roll < bot_roll:
                result = f"Поражение от бота {player_roll} : {bot_roll}"
            else:
               result = f"Ничья {player_roll} : {bot_roll}"
            print(result)
            history.append(result)
        elif regime_choice == "2":
            print("ожидаем второго игрока")
            opponent = create_profile(taken_names)
            player1_roll = random.randint(1, 6)
            player2_roll = random.randint(1, 6)
            print(f"{profile['name']} выбрасывает: {player1_roll} | {opponent['name']} выбрасывает: {player2_roll}")
            if player1_roll > player2_roll:
                result = f"{profile['name']} победил игрока {opponent['name']} ({player1_roll}:{player2_roll})"
            elif player1_roll < player2_roll:
                result = f"{opponent['name']} победил игрока {profile['name']} ({player2_roll}:{player1_roll})"
            else:
                result = f"Ничья между {profile['name']} и {opponent['name']} ({player1_roll}:{player2_roll})"
            print(result)
            history.append(result)
        elif regime_choice == "3":
            if profile["balance"] < price_adult_regime:
                print(f"Недостаточно средств для доступа. Необходимо пополнить баланс на {price_adult_regime} рублей")
            elif profile["status"] == "VIP":
                print("Вы уже купили статус для режима 18+")
            else:
                profile['balance'] = profile['balance'] - price_adult_regime
                profile["status"] = "VIP"
                print(f"Оплата прошла успешно. Остаток на счете: {profile['balance']} рублей. Статус: {profile['status']}")
        elif regime_choice == "4":
            print("История игр")
            if not history:
                print("История пуста")
            else:
                for game in history:
                    print(game)
        elif regime_choice == "5":
            with open("history.txt", "w", encoding="utf-8") as file:
                for game in history:
                    file.write(game + "\n")
            print("История сохранена в файл. Выход")
            break
names_list = ["Ivan"]
player = create_profile(names_list)
main_screen(player, names_list)