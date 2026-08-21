# Random Module

This folder introduces the Python `random` module.

The `random` module lets us generate random numbers and choose random values. This is useful for games, simulations, and simple experiments.

## What you will learn

- how to import the random module
- how to generate random integers
- how to choose random items from a list
- how to use random values in beginner-friendly examples

## Core idea

```python
import random

print(random.randint(1, 10))
```

This prints a random number between 1 and 10.

```python
items = ["record", "book", "coin"]
print(random.choice(items))
```

This chooses one random item from the list.

---

## Sample scripts

1. `01_random_int.py` - generate a random integer
2. `02_random_float.py` - generate a random float
3. `03_random_choice.py` - choose a random item in a list
4. `04_random_shuffle.py` - shuffle a list
5. `05_dice_roll.py` - simulate a die roll
6. `06_card_draw.py` - draw a random card
7. `07_vampire_pick.py` - choose a random vampire clue
8. `08_record_shop_pick.py` - choose a random record from stock
9. `09_magic_8_ball.py` - starter activity for a Magic 8 Ball
10. `10_magic_8_ball_loop.py` - starter loop version of the Magic 8 Ball

## Exercises

11. `exercise_01_random_number.py` - generate a random number
12. `exercise_02_pick_item.py` - choose a random item
13. `exercise_03_pick_winner.py` - choose a random name from a list
14. `exercise_04_dice_total.py` - roll dice and total the score
15. `exercise_05_vampire_choice.py` - choose from several vampire options
16. `exercise_06_stock_pick.py` - choose a record at random
17. `exercise_07_magic_8_ball.py` - build a basic Magic 8 Ball
18. `exercise_08_magic_8_ball_custom.py` - build a more advanced custom Magic 8 Ball

## Theory notes

### Importing the module

```python
import random
```

This gives access to random tools.

### `randint()`

```python
number = random.randint(1, 6)
print(number)
```

This creates a random whole number between the two values.

### `choice()`

```python
options = ["red", "blue", "green"]
print(random.choice(options))
```

This picks one item at random.

### `shuffle()`

```python
cards = ["A", "B", "C"]
random.shuffle(cards)
print(cards)
```

This changes the order of items randomly.

---

## Beginner tip

Randomness means the computer chooses something without a pattern.

This is useful for:

- dice games
- lucky picks
- random rewards
- simple simulations

## How to use this folder

Read each script and run it a few times. You will see the output change each time because the values are random.
