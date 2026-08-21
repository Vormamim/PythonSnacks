# Nested Loops

This folder introduces nested loops in Python.

A nested loop is a loop inside another loop. It is useful when you want to work through a list of items and, inside that, work through another list or another set of values.

## What you will learn

- what a nested loop is
- how an outer loop and an inner loop work together
- how to print combinations
- how nested loops can be used with lists and simple game logic

## Core idea

```python
for item in ["a", "b"]:
    for number in [1, 2]:
        print(item, number)
```

The inner loop runs completely for each loop of the outer loop.

---

## Sample scripts

1. `01_basic_nested_loop.py` - a simple nested loop
2. `02_list_pairs.py` - print pairs from two lists
3. `03_table.py` - multiplication table pattern
4. `04_vampire_room_grid.py` - simple vampire-themed grid example
5. `05_record_shop_rows.py` - rows of records and prices
6. `06_while_nested_loop.py` - nested while loop example
7. `07_inventory_grid.py` - nested loop with inventory items
8. `08_game_board.py` - simple board layout

## Exercises

9. `exercise_01_print_grid.py` - build a grid pattern
10. `exercise_02_grade_table.py` - loop through rows and columns
11. `exercise_03_treasure_map.py` - read a small map
12. `exercise_04_record_pairs.py` - match records to prices
13. `exercise_05_vampire_paths.py` - check possible paths
14. `exercise_06_nested_budget.py` - work with prices in rows

## Theory notes

### Why nested loops are useful

Nested loops help when you need to compare or combine items.

For example:

```python
for genre in ["rock", "jazz"]:
    for price in [10, 15]:
        print(genre, price)
```

This prints every genre with every price.

### The outer loop controls the main pattern

The outer loop repeats the whole inner loop again.

### The inner loop does the detailed work

The inner loop runs each time the outer loop repeats.

### Important beginner tip

Nested loops can run a lot more times than a single loop, so start with small examples.

---

## Beginner tip

When you see a nested loop, think:

- outer loop = big group
- inner loop = smaller group inside each big group

This is useful for tables, grids, matching items, and checking many combinations.

## How to use this folder

Read the examples first. Then change the values and run the scripts again. Try small examples before larger ones.
