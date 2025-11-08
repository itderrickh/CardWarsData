import sqlite3
import os

query = """
SELECT ci.* FROM cardImage ci
JOIN 
(SELECT COUNT(*) AS ItemCount, MIN(CardImageTypeId), MAX(CardImageTypeId) as MaxSize, RevisionId FROM cardImage
GROUP BY RevisionId
HAVING ItemCount > 1
ORDER BY MaxSize) as dupeRecords ON dupeRecords.RevisionId = ci.RevisionId
WHERE CardImageTypeId != 2
"""

def get_card_images(db_path="carddatabase.db"):
    """
    Connects to the SQLite database and retrieves all cardImage records.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Execute the query to fetch all rows from the cardImage table
        cursor.execute(query)

        # Fetch all results
        card_images = cursor.fetchall()

        # Optional: get column names for better readability
        column_names = [description[0] for description in cursor.description]

        # Convert rows into list of dictionaries (optional, but cleaner)
        card_image_objects = [
            dict(zip(column_names, row)) for row in card_images
        ]

        return card_image_objects

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    cards = get_card_images()
    card_ids = [card['Id'] for card in get_card_images()]
    delete_card_images(card_ids)
    #for card in card_ids:
    #    print(card)