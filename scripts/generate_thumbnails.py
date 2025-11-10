import os
from PIL import Image
import sqlite3
import urllib.parse

def generate_thumbnails(file_list, output_dir="../images/generated/small", size=(118, 167)):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    for file_path in file_list:
        try:
            with Image.open(file_path) as img:
                # Resize image while maintaining aspect ratio
                img.thumbnail(size)

                # Construct output file path
                filename = os.path.basename(file_path)
                output_path = os.path.join(output_dir, filename)

                # Save the thumbnail
                img.save(output_path)
                #print(f"Thumbnail created: {output_path}")

        except Exception as e:
            print(f"Error processing {file_path}: {e}")


base_dir = f"F:\\CornDome\\data\\images"
db_path ="../carddatabase.db"

def get_card_images(db):
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


insert_query = """
INSERT INTO cardImage
    (revisionId, cardImageTypeId, imageUrl)
VALUES
    (?, ?, ?);
"""

def add_thumbnail_images(db, cards):
    try:
        # Connect to the database
        conn = sqlite3.connect(db)
        cursor = conn.cursor()

        # Set card size to small
        card_images = [(card["RevisionId"], 1, card["ImageUrl"].replace("regular/", "generated/small/").replace("old/", "generated/small/").replace("upload/", "generated/small/")) for card in cards]

        # Insert multiple rows into the table
        cursor.executemany(insert_query, card_images)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    files = get_card_images(db_path)
    add_thumbnail_images(db_path, files)
    file_paths = [os.path.join(base_dir, urllib.parse.unquote(f["ImageUrl"])) for f in files]

    generate_thumbnails(file_paths)