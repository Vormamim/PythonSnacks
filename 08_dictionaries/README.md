# Dictionaries

This folder is for beginners learning how to use Python dictionaries.

A dictionary stores data as pairs of keys and values. Each key has a value attached to it.

Example:

```python
student = {
    "name": "Ava",
    "age": 15,
    "grade": "A"
}
```

This is useful when we want to store information about one thing in a structured way.

## What you will learn

- how to create a dictionary
- how to access values by key
- how to update a value
- how to check a value in a dictionary
- how to use dictionaries in simple decisions

## Key idea

```python
record = {
    "title": "Rumours",
    "genre": "Rock",
    "price": 18.50
}

print(record["title"])
```

This prints the value stored for the key `"title"`.

---

## Sample scripts

1. `01_create_dict.py` - create a dictionary
2. `02_access_value.py` - access a value by key
3. `03_update_value.py` - change a value
4. `04_check_key.py` - check whether a key exists
5. `05_nested_dict.py` - store a dictionary inside another dictionary
6. `06_dict_in_decision.py` - use a dictionary in an if statement
7. `07_vampire_character.py` - vampire-themed dictionary example
8. `08_record_shop_record.py` - record-shop dictionary example

## Exercises

9. `exercise_01_student_profile.py` - create a student dictionary
10. `exercise_02_ticket_info.py` - store ticket information in a dictionary
11. `exercise_03_vampire_status.py` - store a vampire's details
12. `exercise_04_record_status.py` - check a record dictionary
13. `exercise_05_inventory_item.py` - use a dictionary to store an item
14. `exercise_06_favourite_record.py` - make a simple recommendation using a dictionary

## Theory notes

### Creating a dictionary

```python
student = {
    "name": "Mia",
    "age": 14
}
```

### Accessing values

```python
print(student["name"])
```

### Updating values

```python
student["age"] = 15
```

### Checking keys

```python
if "name" in student:
    print("The key exists")
```

### Using dictionaries in decisions

```python
if student["age"] >= 18:
    print("Adult")
else:
    print("Not an adult")
```

---

## Beginner tip

Dictionaries are useful when you want to store information about one object, such as:

- a record
- a vampire character
- a player
- a product

A dictionary keeps all the information together.

---

## How to use this folder

Read the sample scripts first. Then try the exercises by changing values and testing different conditions.
