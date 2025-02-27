import sqlite3
import time

DB_OUTPUT_NAME = '../../card_database.db'
CARD_INSERT_SQL = open('insert_card.sql', 'r').read()
REVISION_INSERT_SQL = open('insert_revision.sql', 'r').read()
IMAGE_INSERT_SQL = open('insert_image.sql', 'r').read()

def insert_card(name,typeId,ability,setId,landscapeId,cost,attack,defense,cardImageType,imageUrl):
    # Connect to SQLite database
    conn = sqlite3.connect(DB_OUTPUT_NAME)
    cursor = conn.cursor()

    cursor.execute(CARD_INSERT_SQL)

    cardId = cursor.lastrowid
    cursor.execute(REVISION_INSERT_SQL, (
        cardId,
        name,
        typeId,
        ability,
        setId,
        landscapeId,
        cost,
        attack,
        defense
    ))

    revId = cursor.lastrowid
    cursor.execute(IMAGE_INSERT_SQL, (
        revId,
        cardImageType,
        imageUrl
    ))

    conn.commit()
    conn.close()

def collect_card_data():
    while True:
        print("\nEnter card details (or type 'exit' to quit):")
            
        name = input("Name: ")
        if name.lower() == "exit":
            break

        typeId = input("Type ID: ")
        ability = input("Ability: ")
        setId = input("Set ID: ")
        landscapeId = input("Landscape ID: ")
        cost = input("Cost: ")
        attack = input("Attack: ")
        defense = input("Defense: ")
        cardImageType = input("Card Image Type: ")
        imageUrl = input("Image URL: ")

        try:
            typeId = int(typeId)

            if len(landscapeId.strip()) == 0:
                landscapeId = None
            else:
                landscapeId = int(landscapeId)

            if len(setId.strip()) == 0:
                setId = None
            else:
                setId = int(setId)

            if len(ability.strip()) == 0:
                ability = None

            if len(cost.strip()) == 0:
                cost = None
            else:
                cost = int(cost)
            
            if len(attack.strip()) == 0:
                attack = None
            else:
                attack = int(attack)

            if len(defense.strip()) == 0:
                defense = None
            else:
                defense = int(defense)

            if len(cardImageType.strip()) == 0:
                cardImageType = None
            else:
                cardImageType = int(cardImageType)

            if (cardImageType == 1):
                imageUrl = 'small/' + imageUrl
            elif (cardImageType == 2):
                imageUrl = 'regular/' + imageUrl
            elif (cardImageType == 3):
                imageUrl = 'large/' + imageUrl

        except ValueError:
            print("Invalid number entered. Please try again.")
            continue
        
        # Insert the collected data
        insert_card(name, typeId, ability, setId, landscapeId, cost, attack, defense, cardImageType, imageUrl)

        time.sleep(1)  # Small delay to prevent rapid looping
    

if __name__ == "__main__":
    collect_card_data()

# Type
# "0"	"Creature"
# "1"	"Spell"
# "2"	"Building"
# "3"	"Landscape"
# "4"	"Hero"
# "5"	"Teamwork"
# 
# SetId
# "11"	"FlamePrincessVSFern"
# "12"	"PrismoVSTheLich"
# "13"	"PeppermintButlerVSMagicMan"
# "14"	"Kickstarter2"
# "15"	"DarklandsExpansion"
# 
# Landscape
# "0"	"BluePlains"	"Blue Plains"
# "1"	"Cornfield"	"Cornfield"
# "2"	"UselessSwamp"	"Useless Swamp"
# "3"	"SandyLands"	"SandyLands"
# "4"	"NiceLands"	"NiceLands"
# "5"	"IcyLands"	"IcyLands"
# "6"	"Rainbow"	"Rainbow"
# "7"	"LavaFlats"	"LavaFlats"

#Card Image Type
#"1"	"sm"
#"2"	"rg"
#"3"	"lg"