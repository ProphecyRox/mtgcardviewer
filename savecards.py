# Script to save json data from https://mtgjson.com/
# to the website's database

import json
from viewer.models import Card

fp = open("ARN.json")
data = json.load(fp)

for card in data["data"]["cards"]:
    print(f'Importing {card["name"]}...')
    card_obj = Card(
        name=card["name"],
        mana_cost=card["convertedManaCost"],
        card_type=card["type"],
        ability_text=card["text"]
    )

    try:
        card_obj.flavor_text = card["flavorText"]
    except:
        # Just don't set flavor text if card doesn't have one
        pass

    card_obj.save()

fp.close()
print("Done")

