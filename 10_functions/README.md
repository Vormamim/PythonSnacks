# Functions in Python

This folder explains the basics of functions in Python.

A function is a block of code that does a job. It helps us organise our program and reuse code instead of writing the same thing many times.

## What you will learn

- what a function is
- how to create a function
- how to call a function
- how to pass values into a function
- how to return a value from a function

## Important idea

A function is like a named task.

```python
def greet():
    print("Hello!")

greet()
```

This defines the function and then calls it.

---

## Part 1: Simple functions without parameters

These are functions that do not need extra information.

### Example

```python
def say_hello():
    print("Hello from the castle")
```

This is useful for small repeated messages.

---

## Part 2: Functions with parameters

These functions receive values when they are called.

### Example

```python
def welcome(name):
    print(f"Welcome, {name}!")
```

This function uses the value passed in as `name`.

---

## Part 3: Functions with return values

These functions calculate something and send the answer back.

### Example

```python
def add_two_numbers(a, b):
    return a + b
```

The function gives back the result using `return`.

---

## Sample scripts

### Simple functions

1. `01_simple_function.py` - a basic function with no parameters
2. `02_greet_player.py` - a function that prints a message
3. `03_vampire_message.py` - a vampire-themed function

### Functions with parameters

4. `04_welcome_user.py` - function with one parameter
5. `05_record_recommendation.py` - function with a choice parameter
6. `06_vampire_gate.py` - function with a gate choice parameter

### Functions with return values

7. `07_add_numbers.py` - function returns a total
8. `08_calculate_ticket.py` - function returns a ticket price
9. `09_total_inventory.py` - function returns total items in an inventory

## Exercises

10. `exercise_01_say_goodbye.py` - create a simple function
11. `exercise_02_welcome_name.py` - create a parameter-based function
12. `exercise_03_double_value.py` - return a doubled number
13. `exercise_04_price_with_discount.py` - return a discounted price
14. `exercise_05_vampire_recommendation.py` - function returns a recommendation
15. `exercise_06_record_total.py` - function returns a total from a list

## Theory notes

### Defining a function

```python
def greet():
    print("Hello")
```

### Calling a function

```python
greet()
```

### Function with a parameter

```python
def greet_name(name):
    print(f"Hello {name}")
```

### Function with a return value

```python
def add_one(number):
    return number + 1
```

## Beginner tips

- A function should do one clear job.
- Use a name that tells you what the function does.
- `print()` shows output.
- `return` sends a result back to the caller.

## How to use this folder

Read the simple examples first. Then look at the parameter examples. Finally, study the return-value examples. This is the easiest way to understand functions.
