from random import sample

from colorama import init, Fore, Back, Style

from objects import characters


init()


def auto_game():
    while True:
        defender, attacker = sample(characters, 2)
        defender.get_damage(attacker.attack)

        # Цвета для игроков и атаки
        attacker_name_colored = Fore.RED + str(attacker) + Style.RESET_ALL
        defender_name_colored = Fore.BLUE + str(defender) + Style.RESET_ALL
        attack_colored = Fore.YELLOW + str(attacker.attack) + Style.RESET_ALL

        print(f'{attacker_name_colored} наносит {defender_name_colored} {attack_colored} урона!')

        if defender.hp <= 0:
            print(f'{attacker_name_colored} одерживает победу над {defender_name_colored}!')
            characters.remove(defender)
            if len(characters) == 1:
                break
        else:
            print(f'У {defender_name_colored} остаётся {defender.hp} здоровья!')

    winner = characters[0]
    winner_name_colored = Fore.GREEN + str(winner) + Style.RESET_ALL
    print(f'\nИ на арене остаётся только один, и это наш чемпион {winner_name_colored}!')


if __name__ == '__main__':
    auto_game()
