# Lists

This folder is for beginners learning how to work with Python lists.

A list is a collection of items stored in one variable. Lists are very useful because they let us keep lots of related values together.

## What you will learn

- how to create a list
- how to access items in a list
- how to check whether an item is in a list
- how to add items to a list
- how to use a list in a decision-making program

## Key idea

```python
items = ["apple", "banana", "grape"]
print(items[0])
```

This prints the first item in the list.

## Sample scripts

1. `01_create_list.py` - create a list
2. `02_access_items.py` - access list items by index
3. `03_check_item.py` - check if something is in the list
4. `04_length.py` - find how many items are in the list
5. `05_append.py` - add an item to a list
6. `06_list_in_decision.py` - use a list in an if statement
7. `07_vampire_inventory.py` - a vampire inventory example
8. `08_record_shop_stock.py` - a record shop stock list example

## Exercises

9. `exercise_01_travel_list.py` - make a travel list
10. `exercise_02_search_book.py` - check if a book is in a list
11. `exercise_03_inventory_check.py` - check the contents of an inventory
12. `exercise_04_record_search.py` - search for a record title
13. `exercise_05_vampire_gear.py` - check whether a vampire has the right gear
14. `exercise_06_duplicates.py` - find duplicates in a list

## Theory notes

### Creating a list

```python
students = ["Ava", "Ben", "Chloe"]
```

### Accessing items by index

```python
print(students[1])
```

Python starts counting at 0, so `students[1]` is `Ben`.

### Checking if an item is in a list

```python
if "Ben" in students:
    print("Ben is here")
```

### Find the length of a list

```python
print(len(students))
```

### Add item to the end of a list

```python
students.append("Dylan")
```

---

## Beginner tip

Lists are useful when you need to keep lots of similar data together, such as:

- a list of names
- a list of weapons
- a list of record titles
- a list of food items

## How to use this folder

Read each sample and then try the exercises. Change the values and run them again to see how the output changes.
