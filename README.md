# Magic the Gathering Card Viewer Website

This website only contains the source files for the website and migrations needed to setup the database. It does *not* contain any card data.

## Prerequisites
- Python
- Django

## Setup
1. Install the prerequisites
2. Run the migrations: `python3 manage.py migrate`
3. To download cards, go to [MTGJSON](https://mtgjson.com/downloads/all-sets/) and download a json file for a set.
4. In `savecards.py`, change the name of the json file you are opening.
5. Run `savecards.py` to store the cards in the database.
