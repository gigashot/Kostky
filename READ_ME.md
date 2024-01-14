# Hra Kostek

Jednoduchý program v Pythonu, který simuluje hru s kostkami a vypočítává skóre na základě hodů.

## Jak používat

### Požadavky

Program vyžaduje nainstalovaný Python (verze 3.x).

### Spuštění

Stačí spustit skript v Pythonu. Příkaz k spuštění může být:
```bash
 main_fce()
```
python nazev_skriptu.py
## Pravidla hry
Po stisknutí klávesy Enter jsou hodeny šest kostek.
Program automaticky rozpoznává speciální kombinace a přiděluje jim odpovídající body.
Skóre za každé kolo je zobrazeno a přidáno k celkovému skóre.
Uživatel je vyzván k zadání, zda chce hrát další kolo.
## Rozpoznávané Kombinace / Body
Program rozpoznává následující kombinace a přiděluje jim odpovídající body:

|           | Hodnota           |   Počet bodů   |           |
|:---------:|:-----------------:|:--------------:|:---------:|
|           |             1     |    100 bodů    |           |
|           |             5     |    50 bodů     |           |
|           |3x stejné číslo (kromě 1)|číslo * 100 bodů|           |
|           |4x stejné číslo (kromě 1)|číslo * 200 bodů|           |
|           |5x stejné číslo (kromě 1)|číslo * 400 bodů|           |
|           |6x stejné číslo (kromě 1)|číslo * 800 bodů|           |
|           |       3x jednička   |   1000 bodů    |           |
|           |       4x jednička   |   2000 bodů    |           |
|           |       5x jednička   |   4000 bodů    |           |
|           |       6x jednička   |   8000 bodů    |           |
|           |       3x dvojice    |   1000 bodů    |           |
|           |Postupka (1, 2, 3, 4, 5, 6)|   1500 bodů    |           |
´´´bash
        # vypočítávání skóre pro současný hod
        round_score = calculate_score(dice)
        print("Score for this round: {}".format(round_score))

        # přidá skóre do celkového skóre
        total_score += round_score
        print("Total score: {}\n".format(total_score))
´´´ 

## Ukázka použití
```bash
Press Enter to roll the dice...
Dice: [3, 3, 1, 6, 2, 5]
Score for this round: 50
Total score: 50

Do you want to play another round? (yes/no): yes
Press Enter to roll the dice...
Dice: [4, 1, 1, 4, 4, 2]
Score for this round: 600
Total score: 650

Do you want to play another round? (yes/no): no
Game over! Final score: 650
```
