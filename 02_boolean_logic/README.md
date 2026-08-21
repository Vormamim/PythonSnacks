# Boolean Logic with IF, ELIF, ELSE

This folder is a beginner-friendly set for working with boolean logic in Python.

A boolean is a value that is either:

- `True`
- `False`

We use booleans to make decisions in our code.

## What you will learn

- how `if` checks a condition
- how `elif` checks another option
- how `else` handles everything else
- how to use booleans with variables and lists

## Core idea

```python
age = 16

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
```

Python checks the conditions in order. The first true condition runs.

---

## Sample scripts

1. `01_boolean_value.py` - simple True and False values
2. `02_age_check.py` - use `if` with a variable
3. `03_list_membership.py` - check if a value is inside a list
4. `04_access_granted.py` - combine booleans with `and`
5. `05_vampire_status.py` - decide by conditions
6. `06_record_shop_stock.py` - use a list to make a decision
7. `07_age_group.py` - use `if`, `elif`, and `else`
8. `08_ticket_choice.py` - use a list and a variable in a decision

## Exercises

9. `exercise_01_weather.py` - decide what to wear
10. `exercise_02_genre_choice.py` - choose a recommendation from a list
11. `exercise_03_member_status.py` - check access with booleans
12. `exercise_04_budget_check.py` - compare numbers and decide
13. `exercise_05_vampire_gate.py` - decide who can enter
14. `exercise_06_record_search.py` - search a list and decide

## Theory notes

### Boolean values

```python
is_member = True
is_open = False
```

Boolean values are used in decisions.

### `if` statements

```python
if age >= 18:
    print("You can enter")
```

This only runs when the condition is true.

### `elif` and `else`

```python
if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Pass")
else:
    print("Try again")
```

### Checking a list

```python
items = ["book", "record", "poster"]

if "record" in items:
    print("The record is in stock")
else:
    print("It is not in stock")
```

The `in` operator is useful for lists.

---

## Beginner tip

Boolean logic asks questions like:

- Is this true?
- Is this value in the list?
- Is the person old enough?
- Are both conditions true?

When you learn these questions, you are learning how Python makes decisions.

## How to use this folder

Read each sample script and try changing the variable values. Then complete the exercises. This helps you understand how each condition changes the result.
