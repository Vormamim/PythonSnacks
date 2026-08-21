# Working with Lists

This folder is for beginners who are learning how to use Python lists. Lists are one of the most important data types in Python, and they are used to store multiple items in one place.

A list can hold things like:

- names
- numbers
- record titles
- favourite foods
- items in a game inventory

## What you will learn

- how to create a list
- how to access items in a list
- how to add items to a list
- how to check whether something is in a list
- how to use a list in a simple decision

## Key idea

```python
items = ["apple", "banana", "grape"]

if "banana" in items:
    print("Banana is in the list.")
```

This is a very common beginner pattern in Python.

---

## Sample scripts

1. `01_create_list.py` - create a simple list
2. `02_access_items.py` - access items by index
3. `03_check_item.py` - check if an item is in a list
4. `04_length.py` - find the number of items in a list
5. `05_append.py` - add an item to a list
6. `06_list_in_decision.py` - use a list in an if statement
7. `07_vampire_inventory.py` - a vampire-themed inventory example
8. `08_record_shop_stock.py` - a record-shop inventory example

## Exercises

9. `exercise_01_favourite_games.py` - make a list of favourite games
10. `exercise_02_book_list.py` - check whether a book is in a list
11. `exercise_03_inventory_check.py` - check if a player has an item
12. `exercise_04_record_search.py` - search a list of record titles
13. `exercise_05_vampire_gear.py` - decide what a vampire carries
14. `exercise_06_remove_duplicate.py` - search for duplicates in a list

## Theory notes

### Creating a list

```python
friends = ["Sam", "Mia", "Lee"]
```

This stores several names in one variable.

### Accessing a list item

```python
print(friends[0])
```

The number in brackets is the index. Python starts counting from 0.

### Checking if something is in a list

```python
if "Mia" in friends:
    print("Mia is in the list")
```

This is a very useful part of decision making.

### Adding to a list

```python
friends.append("Alex")
```

This adds a new item to the end of the list.

### Finding the length of a list

```python
print(len(friends))
```

This tells you how many items are in the list.

---

## Why lists are useful

Lists help us store lots of similar things in one place. This saves time and makes programs easier to read.

For example:

- a list of record titles
- a list of vampire names
- a list of game inventory items
- a list of prices

---

## How to use this folder

Read the sample scripts first. Then try the exercises and change the values. The best way to learn is to test out a few different examples.
