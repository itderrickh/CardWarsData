import sqlite3
import json
import glob
import os

DB_OUTPUT_NAME = 'card_database.db'
CARD_INSERT_SQL = open('procedures/cardInsert.sql', 'r').read()
CARD_IMAGE_INSERT_SQL = open('procedures/cardImageInsert.sql', 'r').read()
CARD_REVISION_INSERT_SQL = open('procedures/cardRevisionInsert.sql', 'r').read()

def insert_cards_from_json(db_name, json_file, revisionNumber):
    # Connect to SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Read JSON file
    with open(json_file, "r") as file:
        cards = json.load(file)

    # Insert data into the Card table
    for card in cards:
        if (revisionNumber == 1):
            cursor.execute(CARD_INSERT_SQL, (
                card.get("id"),
            ))
        cursor.execute(CARD_REVISION_INSERT_SQL, (
            card.get("id"),
            revisionNumber, #revisionNumber - Revision 1
            card.get("name"),
            card.get("type"),
            card.get("ability"),
            card.get("set"),
            card.get("landscape"),
            card.get("cost"),
            card.get("attack"),
            card.get("defense"),
        ))
        revisionId = cursor.lastrowid
        cursor.execute(CARD_IMAGE_INSERT_SQL, (
            revisionId,
            2, #cardImageType - Regular,
            card.get("imageurl")
        ))

    # Commit changes and close connection
    conn.commit()
    conn.close()
    print(f"Inserted {len(cards)} cards into the database.")

def create_database_from_sql(db_name, sql_file):
    # Connect to SQLite (creates the DB if it doesn't exist)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Read the SQL file
    with open(sql_file, "r") as file:
        sql_script = file.read()

    # Execute the SQL script
    cursor.executescript(sql_script)

    # Commit and close
    conn.commit()
    conn.close()
    print(f"Database '{db_name}' created successfully from '{sql_file}'.")


create_database_from_sql(DB_OUTPUT_NAME, "tables.sql")

json_files = glob.glob(os.path.join("../../cards", "*.json"))
for json_file in json_files:
    insert_cards_from_json(DB_OUTPUT_NAME, json_file, 1)
for json_file in json_files:
    insert_cards_from_json(DB_OUTPUT_NAME, json_file, 2)