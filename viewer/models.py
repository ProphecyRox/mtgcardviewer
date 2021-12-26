from django.db import models

# Create your models here.

CHAR_FIELD_MAX_LEN = 1000

class Card(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    image = models.ImageField()
    mana_cost = models.IntegerField()
    type_line = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    expansion = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    ability_text = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    flavor_text = models.CharField(max_length=CHAR_FIELD_MAX_LEN)