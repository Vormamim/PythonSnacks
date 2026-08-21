# Searching Lists and Dictionaries

This folder is a simple beginner pack for searching data in Python.

We will look at how to:

- search a list for an item
- check whether a value exists in a list
- find a value in a dictionary by key
- search for a matching record or item

## What you will learn

- `in` with lists
- `in` with dictionary keys
- how to get a value from a dictionary
- simple searching patterns for beginner code

## Core idea

```python
items = ["book", "record", "poster"]

if "record" in items:
    print("Found it!")
```

```python
record = {"title": "Midnight Echo", "price": 18}

print(record["title"])
```

---

## Sample scripts

1. `01_search_list.py` - search for a value in a list
2. `02_search_list_with_if.py` - use if to decide
3. `03_search_dict_key.py` - check if a key exists
4. `04_get_dict_value.py` - read the value for a key
5. `05_find_record.py` - look for a record name in a list of dictionaries
6. `06_find_vampire_item.py` - search through a list of item names
7. `07_find_price.py` - search a dictionary for a price
8. `08_search_with_loop.py` - use a loop to search items

## Exercises

9. `exercise_01_find_book.py` - search a list for a book
10. `exercise_02_find_student.py` - search a list of dictionaries
11. `exercise_03_find_genre.py` - check a dictionary key
12. `exercise_04_find_price.py` - read a value from a dictionary
13. `exercise_05_find_vampire_weapon.py` - search a list
14. `exercise_06_find_record_by_name.py` - search a list of records

## Theory notes

### Searching a list

```python
stock = ["vinyl", "cassette", "cd"]

if "vinyl" in stock:
    print("It is in stock")
```

The `in` operator checks whether the item is in the list.

### Searching a dictionary

```python
details = {"title": "Moonlight", "price": 20}

if "title" in details:
    print(details["title"])
```

This checks whether a key exists in the dictionary.

### Searching a list of dictionaries

```python
records = [
    {"title": "Night Song", "price": 12},
    {"title": "Castle Lights", "price": 15}
]

for record in records:
    if record["title"] == "Night Song":
        print(record["price"])
```

This is a simple way to search through a set of records.

---

## Beginner tip

A search is just a question:

- Is this value in the list?
- Does this key exist in the dictionary?
- Does this record match the title I want?

That is why searching is so important in Python.

## How to use this folder

Read the sample scripts first. Then change the values and run them again. Try each one with different names, keys, and items.
