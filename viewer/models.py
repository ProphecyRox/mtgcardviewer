from django.db import models

# Create your models here.

CHAR_FIELD_MAX_LEN = 1000

class Card(models.Model):
    name = models.CharField("Card name", max_length=CHAR_FIELD_MAX_LEN)
    mana_cost = models.IntegerField("Mana cost")
    card_type = models.CharField("Type", max_length=CHAR_FIELD_MAX_LEN)
    ability_text = models.CharField("Ability", max_length=CHAR_FIELD_MAX_LEN)
    flavor_text = models.CharField("Flavor Text", max_length=CHAR_FIELD_MAX_LEN, blank=True)
