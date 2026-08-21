# Record Shop Code Snacks

Welcome to the Record Shop Code Snacks! These short Python scripts are designed for absolute beginners. They use simple lists and dictionaries to model a vintage record store and show how Python makes decisions using `if`, `elif`, and `else`.

The goal is simple: read each script, understand the idea, then change a few values and try it yourself.

## What you will learn

- how to store data in a list
- how to store data in a dictionary
- how to check conditions using `if`
- how to choose between different outcomes using `elif` and `else`
- how to make simple recommendations based on customer choices

## How to run a script

Open your terminal, go to the folder that contains the scripts, and run:

```bash
python script_name.py
```

For example:

```bash
python 01_stock_check.py
```

## The record shop theme

Imagine a small vintage shop that sells old and new vinyl records. The shop keeps track of:

- record titles
- genres
- prices
- conditions
- whether a customer is a member
- the customer's budget

These scripts make simple decisions like:

- Is this record in stock?
- Can the customer afford it?
- Is the record vintage?
- Should we recommend a jazz album or a rock album?

---

## Script list and theory

### 1. `01_stock_check.py` - Checking stock
Theory:
This script uses a list of record titles. We ask, "Is this item in the list?" Python checks the list using `in`.

If the title is in the list, the program prints a positive message. Otherwise, it prints a sorry message.

### 2. `02_genre_filter.py` - Filtering by genre
Theory:
This script uses a list of dictionaries. Each dictionary represents one record. We check the value stored under `"genre"` and compare it to the chosen genre.

This teaches you how to read data from a dictionary and make a decision based on one value.

### 3. `03_price_check.py` - Budget check
Theory:
This script stores the record price in a dictionary and compares it to a budget value. The condition uses `<=` to decide whether the record is affordable.

This is a very common beginner pattern: compare a number with a limit.

### 4. `04_condition_check.py` - Checking record condition
Theory:
This script uses `if`, `elif`, and `else` to make several possible decisions. The condition depends on the value stored in `"condition"`.

This helps you understand that one variable can lead to different outcomes.

### 5. `05_member_discount.py` - Member discount
Theory:
The script checks whether a customer is a member by looking at the value `True` or `False`. If the customer is a member, they receive a discount. If not, they pay full price.

This introduces boolean logic: `True` and `False`.

### 6. `06_recommendation.py` - Making a recommendation
Theory:
This script uses an `if` / `elif` / `else` chain. Python checks the customer's favourite genre and then chooses a matching record.

This is a simple way to build a recommendation system without functions or classes.

### 7. `07_budget_finder.py` - Finding records in budget
Theory:
This script loops through a list of records and checks each price. If the price is within budget, it prints the record. Otherwise, it says it is too expensive.

This shows how a loop and a decision can work together.

### 8. `08_vintage_choice.py` - Vintage decision
Theory:
This script compares the year of a record to a value. If the year is before a certain point, it is treated as vintage. Otherwise, it is seen as a more recent record.

This shows that decisions can be based on numbers as well as words.

### 9. `09_bundle_offer.py` - Bundle discount
Theory:
This script uses the length of a list, `len(basket)`, to decide whether the customer has enough items for a special offer.

This teaches you how list length can be used in decision making.

### 10. `10_cart_total.py` - Final basket decision
Theory:
This script adds up the prices in a basket and then makes a recommendation based on the total cost. It uses several conditions to decide whether the basket is within budget, close to budget, or over budget.

This is a nice final example because it combines loops, totals, and decisions.

---

## Helpful beginner tips

- Read the script from top to bottom.
- Look for the variable names and ask, "What is this storing?"
- Spot the `if` statements and ask, "What question is Python asking?"
- Try changing one value and running the script again.
- Make small changes before making bigger ones.

## Challenge ideas

Try these yourself:

1. Add a new record to the list.
2. Change the budget.
3. Add a new genre like "Funk" or "Metal".
4. Change the member discount from 10 to 15.
5. Write your own mini record shop recommendation using the same pattern.

These are starter scripts for learning, so the best way to learn is to edit them and test your ideas.
