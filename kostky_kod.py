import random

def main_fce():
    def roll_dice():
        return [random.randint(1, 6) for _ in range(6)]

    def calculate_score(dice):
        score = 0

        # Hledá všechny speciální kombinace
        if dice == [1, 2, 3, 4, 5, 6]:
            return score == 1500

        elif all(x == 1 for x in dice):
            score += 2 ** (len(dice) - 1) * 1000

        elif all(x == dice[0] for x in dice):
            if dice[0] == 1:
                score += 2 ** (len(dice) - 1) * 1000
            else:
                score += dice[0] * (2 ** (len(dice) - 1) * 100)

        elif len(set(dice)) == 3 and all(dice.count(x) == 2 for x in set(dice)):
            score += 1000


        else:
            # Hledá samotné 1 a 5
            for value in set(dice):
                count = dice.count(value)

                if value == 1:
                    score += count * 100 if count < 3 else (count - 2) * 1000
                elif value == 5:
                    score += count * 50 if count < 3 else (count - 2) * 500
                elif count in [3, 4, 5, 6]:
                    score += value * (2 ** (count - 3) * 100)

        return score

    total_score = 0

    while True:
        input("zmáčkněte Enter pro hod kostkou...")

        # hod 6 kostkami
        dice = roll_dice()

        print("Kosty: {}".format(dice))

        # vypočítávání skóre pro současný hod
        round_score = calculate_score(dice)
        print("Skóre: {}".format(round_score))

        # přidá skóre do celkového skóre
        total_score += round_score
        print("Celkové skóre: {}\n".format(total_score))

        # zeptá se uživatele jestli chce zpustit další
        play_again = input("Chcete hrát další kolo? (ano/ne): ").lower()
        if play_again != 'ano':
            print("Konec hry! Celkové skóre: {}".format(total_score))
            break

# Vyvolávání celého kódu
main_fce()
