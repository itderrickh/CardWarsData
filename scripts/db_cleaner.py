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

def delete_card_images(card_ids, db_path="carddatabase.db"):
    """
    Deletes records from the cardImage table and removes the corresponding image files.

    Args:
        card_ids (list): List of card IDs (or other unique identifiers) to delete.
        db_path (str): Path to the SQLite database file.
    """
    if not card_ids:
        print("No records to delete.")
        return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # First, fetch the ImageUrl paths for the given IDs
        placeholders = ','.join('?' * len(card_ids))
        cursor.execute(f"SELECT Id, ImageUrl FROM cardImage WHERE id IN ({placeholders})", card_ids)
        images_to_delete = cursor.fetchall()

        delete_files(images_to_delete)

        # Delete the records from the database
        cursor.execute(f"DELETE FROM cardImage WHERE id IN ({placeholders})", card_ids)
        conn.commit()
        print(f"Deleted {cursor.rowcount} records from the database.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

def delete_files(cardImages):
    # Delete the files
        for record_id, image_path in cardImages:
            final_path = f"F:/CornDome/data/images/{image_path}"
            if final_path and os.path.exists(final_path):
                try:
                    #os.remove(final_path)
                    print(f"Deleted file: {final_path}")
                except Exception as e:
                    print(f"Error deleting file {final_path}: {e}")
            else:
                print(f"File not found or invalid path for record {record_id}: {final_path}")

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