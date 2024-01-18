# Hra Kostek

Jednoduchý program v Pythonu, který simuluje hru s kostkami a vypočítává skóre na základě hodů.

## Jak používat

### Požadavky

Program vyžaduje nainstalovaný Python.

### Spuštění

Stačí spustit funkci v Pythonu. Příkaz k spuštění:
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



```python
#Výpočet skóre pro současný hod
round_score = calculate_score(dice)
print("Score for this round: {}".format(round_score))

# Přidání skóre do celkového skóre
total_score += round_score
print("Total score: {}\n".format(total_score))

# zeptá se uživatele jestli chce zpustit další
play_again = input("Chcete hrát další kolo? (ano/ne): ").lower()
if play_again != 'ano':
 print("Konec hry! Celkové skóre: {}".format(total_score))
 break
```


## Ukázka použití
```
zmáčkněte Enter pro hod kostkou...
Kosty: [4, 5, 4, 1, 2, 6]
Skóre: 150
Celkové skóre: 150

Chcete hrát další kolo? (ano/ne): ano
zmáčkněte Enter pro hod kostkou...
Kosty: [5, 3, 1, 4, 5, 4]
Skóre: 200
Celkové skóre: 350

Chcete hrát další kolo? (ano/ne): ne
Konec hry! Celkové skóre: 350
```
