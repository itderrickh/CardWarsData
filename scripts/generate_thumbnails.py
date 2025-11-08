import os
from PIL import Image
import sqlite3

def generate_thumbnails(file_list, output_dir="generated/small", size=(118, 167)):
    """
    Creates thumbnails for a list of image files.

    Args:
        file_list (list): List of file paths to images.
        output_dir (str): Directory where thumbnails will be saved.
        size (tuple): Thumbnail size (width, height).
    """
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
                print(f"Thumbnail created: {output_path}")

        except Exception as e:
            print(f"Error processing {file_path}: {e}")


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

if __name__ == "__main__":
    files = get_card_images(db_path)
    file_paths = [os.path.join(base_dir, f["ImageUrl"]) for f in files]

    generate_thumbnails(file_paths)