"""Filter a shop's records by genre.

This script uses a list of dictionaries. Each dictionary represents one record.
We look at the 'genre' value and decide which ones match the customer's taste.
"""

records = [
    {"title": "Blue Train", "genre": "Jazz", "price": 22.00},
    {"title": "Rumours", "genre": "Rock", "price": 18.50},
    {"title": "Thriller", "genre": "Pop", "price": 16.00},
    {"title": "The Miseducation", "genre": "Soul", "price": 19.00},
    {"title": "A Love Supreme", "genre": "Jazz", "price": 24.00}
]

chosen_genre = "Jazz"

print(f"Records in the {chosen_genre} section:")

for record in records:
    if record["genre"] == chosen_genre:
        print(f"- {record['title']} costs ${record['price']:.2f}")
