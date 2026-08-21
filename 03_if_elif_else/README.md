# IF, ELIF, ELSE Practice Pack

This folder is a simple learning set for beginners who are practising `if`, `elif`, and `else` in Python.

The aim is to help students understand how Python makes decisions and chooses one path from several possible options.

## What you are learning

- `if` checks one condition
- `elif` checks another condition if the first one is false
- `else` runs when none of the earlier conditions are true

## Key idea

```python
if condition_1:
    print("First choice")
elif condition_2:
    print("Second choice")
else:
    print("Default choice")
```

Python moves through the conditions in order and stops as soon as it finds one that is true.

---

## Sample scripts

1. `01_basic_if.py` - a simple if statement
2. `02_if_else.py` - one condition with two outcomes
3. `03_if_elif_else.py` - multiple choices
4. `04_comparison.py` - comparing numbers
5. `05_membership.py` - checking if a value is in a list
6. `06_bool_example.py` - using True and False
7. `07_vampire_choice.py` - a vampire-themed example
8. `08_record_shop_choice.py` - a record-shop-themed example

## Exercises

9. `exercise_01_age_check.py` - decide if a person is old enough
10. `exercise_02_ticket_price.py` - decide a ticket price
11. `exercise_03_genre_recommendation.py` - recommend a record by genre
12. `exercise_04_weather_decision.py` - choose clothing for the weather
13. `exercise_05_vampire_gate.py` - decide what gate to open
14. `exercise_06_stock_check.py` - decide if an item is in stock

## Theory notes

### The structure of an if statement

```python
if score >= 50:
    print("Pass")
else:
    print("Fail")
```

- The condition is checked first.
- If the condition is true, the `if` block runs.
- If it is false, the `else` block runs.

### The structure of an if/elif/else chain

```python
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
```

This works like a decision tree:

- check the first option
- if that is not true, check the next option
- if none match, use `else`

### Important beginner tip

Always test the condition carefully. For example:

- `==` means equal to
- `!=` means not equal to
- `<` means less than
- `>` means greater than
- `<=` means less than or equal to
- `>=` means greater than or equal to

---

## How to use this folder

Read each sample first, then try the exercises. Change the values and run the script again to see how the decision changes.

These are designed to be easy to adapt and easy to understand.
