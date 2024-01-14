import random

def main_fce():
    def roll_dice():
        return [random.randint(1, 6) for _ in range(6)]

    def calculate_score(dice):
        score = 0
        
        # hledá všechny speciální kombinace
        if all(x == 1 for x in dice):
            score += 1000 if len(dice) == 3 else 2000 if len(dice) == 4 else 4000 if len(dice) == 5 else 8000
        if all(x == dice[0] for x in dice):
            if dice[0] == 1:
                score += 1000 if len(dice) == 3 else 2000 if len(dice) == 4 else 4000 if len(dice) == 5 else 8000
            else:
                score += dice[0] * (100 if len(dice) == 3 else 200 if len(dice) == 4 else 400 if len(dice) == 5 else 800)
        elif len(set(dice)) == 3 and all(dice.count(x) == 2 for x in set(dice)):
            score += 1000
        elif dice == [1, 2, 3, 4, 5, 6]:
            score += 1500
        else:
            # hledá samotné 1, a 5
            for value in set(dice):
                count = dice.count(value)
                if value == 1:
                    score += count * 100 if count < 3 else 1000 + (count - 3) * 100
                elif value == 5:
                    score += count * 50 if count < 3 else 500 + (count - 3) * 50
                elif count == 3:
                    score += value * 100
                elif count == 4:
                    score += value * 200  # Changed from 400 to 200
                elif count == 5:
                    score += value * 400
                elif count == 6:
                    score += value * 800

            # hledá speciální případy
            if all(x == 2 for x in dice) or all(x == 3 for x in dice) or all(x == 4 for x in dice) or all(x == 5 for x in dice) or all(x == 6 for x in dice):
                score += 1500

            if dice.count(1) == 3:
                score += 1000
            elif dice.count(1) == 4:
                score += 2000
            elif dice.count(1) == 5:
                score += 4000
            elif dice.count(1) == 6:
                score += 8000

        return score

    total_score = 0

    while True:
        input("Press Enter to roll the dice...")

        # hod 6 kostkami
        dice = roll_dice()

        print("Dice: {}".format(dice))

        # vypočítávání skóre pro současný hod
        round_score = calculate_score(dice)
        print("Score for this round: {}".format(round_score))

        # přidá skóre do celkového skóre
        total_score += round_score
        print("Total score: {}\n".format(total_score))

        # zeptá se uživatele jestli chce zpustit další
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Game over! Final score: {}".format(total_score))
            break

# Volání hlavní funkce
main_fce()
