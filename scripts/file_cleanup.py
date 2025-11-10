import os
import sqlite3
from urllib.parse import unquote

base_dir = f"F:\\CornDome\\data\\images"
db_path ="../carddatabase.db"

def get_card_images(db):
    """
    Connects to the SQLite database and retrieves all cardImage records.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(db)
        cursor = conn.cursor()

        # Execute the query to fetch all rows from the cardImage table
        cursor.execute("SELECT * FROM cardImage")

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

def get_all_files(directory):
    """
    Recursively get all files from the given directory.
    
    Args:
        directory (str): Root directory to search in.
    
    Returns:
        list: List of full file paths.
    """
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            all_files.append(full_path)
    return all_files


if __name__ == "__main__":
    for i in range(1, 5):
        print()
    files = get_all_files(base_dir)
    
    fps = [os.path.relpath(f, base_dir).replace("\\", "/") for f in files]

    card_images = get_card_images(db_path)
    ci_paths = [unquote(card['ImageUrl'].replace("\\", "/")) for card in card_images]

    non_intersecting = sorted(list(set(fps) - set(ci_paths)))
    for n in non_intersecting:
        print(n)

    #for i in range(1, 5):
    #    print()

    #non_intersecting_b = list(set(ci_paths) - set(fps))
    #for n in non_intersecting_b:
    #    print(n)