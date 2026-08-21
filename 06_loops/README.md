# For and While Loops

This folder is for beginners who are learning how to use loops in Python.

Loops help us repeat actions without writing the same code again and again.

## What you will learn

- how a `for` loop works
- how a `while` loop works
- how to count with loops
- how to loop through a list
- how to stop a loop when a condition is met

## Key idea

```python
for item in ["apple", "banana", "grape"]:
    print(item)
```

This repeats the code once for each item in the list.

```python
count = 0
while count < 3:
    print(count)
    count = count + 1
```

This repeats while the condition is still true.

---

## Sample scripts

1. `01_for_list.py` - loop through a list
2. `02_for_range.py` - use `range()` in a for loop
3. `03_while_count.py` - count with a while loop
4. `04_while_stop.py` - stop when a condition is reached
5. `05_for_string.py` - loop through characters in a string
6. `06_nested_loop.py` - a simple loop inside another loop
7. `07_vampire_paths.py` - vampire-themed loop example
8. `08_record_shop_stock.py` - a record-shop loop example

## Exercises

9. `exercise_01_print_names.py` - print names from a list
10. `exercise_02_count_to_ten.py` - count from 1 to 10
11. `exercise_03_inventory_check.py` - loop through inventory items
12. `exercise_04_record_list.py` - print record titles
13. `exercise_05_vampire_escape.py` - repeat an action until a condition changes
14. `exercise_06_while_budget.py` - spend money until a budget is reached

## Theory notes

### For loop
A `for` loop repeats a block of code once for each item in a collection.

```python
for number in [1, 2, 3]:
    print(number)
```

### While loop
A `while` loop keeps repeating as long as a condition is true.

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
```

### Range
The `range()` function creates a sequence of numbers.

```python
for i in range(5):
    print(i)
```

This prints 0, 1, 2, 3, 4.

### Important safety note
A `while` loop can become endless if the condition never becomes false. Always change the value inside the loop.

---

## Beginner tips

- Use a `for` loop when you know the items you want to work with.
- Use a `while` loop when you need to keep going until a condition changes.
- Make sure the value inside a while loop changes or the loop may run forever.

---

## How to use this folder

Read the sample scripts first, then try the exercises. Change the values and test the effect of the loop.
