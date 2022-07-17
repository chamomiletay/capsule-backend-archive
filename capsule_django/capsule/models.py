from statistics import quantiles
from django.db import models

##------ brain dump ------
    #-- wardrobe clothing article elements --
        # Name
        # Color
        # Image (via image upload)
        # Article type (top, bottom, dress, etc.)
        # Category (work, loungewear, casual, etc.)
        # Brand
        # Quantity

    #-- outfit randomizer elements --
        # Articles: Wardrobe item IDs,
        # Images
        # Weather conditions
        # Clothing category (work, loungewear, etc.)

    #-- user profile elements --
        # Username
        # Password
        # Name
        # Age
        # Description
        # Favorite Outfits (select favorites from generated outfits)
        # Favorite Colors
        # Favorite Brands 

##------ end brain dump . ------


# Create your models here.

# --- wardrobe clothing articles model ---

class Article(models.Model):
#---- define clothing choices for user to select ----
    class ArticleType(models.TextChoices):
        TOP = '1', 'Top'
        BOTTOMS = '2', 'Bottoms'
        DRESS = '3', 'Dress'
        JUMPSUIT = '4', 'Jumpsuit/Romper'
        SWEATER = '5', 'Sweater'
        CARDIGAN = '6', 'Cardigan'
        OUTERWEAR = '7', 'Outerwear'
        BODYSUIT = '8', 'Bodysuit'
        LINGERIE = '9', 'Lingerie'
        SHOES = '10', 'Shoes'
        ACCESSORY = '11', 'Accessory'
        SOCKS = '12', 'Socks/Tights'

#---- define clothing categories ----
    class CategoryType(models.TextChoices):
        LOUNGEWEAR = '1', 'Loungewear'
        CASUAL = '2', 'Casual'
        FORMAL = '3', 'Formal'
        PARTY = '4', 'Party'
        WORK = '5', 'Work'


#---- define clothing color options ----
    class Color(models.TextChoices):
        RED = '1', 'Red'
        ORANGE = '2', 'Orange'
        YELLOW = '3', 'Yellow'
        BLUE = '4', 'Blue'
        GREEN = '5', 'Green'
        WHITE = '6', 'White'
        BEIGE = '7', 'Beige'
        BLACK = '8', 'Black'
        PURPLE = '9', 'Purple'
        PINK = '10', 'Pink'
        GRAY = '11', 'Gray'
        BROWN = '12', 'Brown'
        TAN = '13', 'Tan'
        MULTI = '14', 'Multi'


    name = models.CharField(max_length=255)
    color = models.CharField(max_length=2, choices=Color.choices, default=Color.RED)
    image = models.ImageField(upload_to='images/')
    article_type = models.CharField(max_length=2, choices=ArticleType.choices, default=ArticleType.TOP)
    category = models.CharField(max_length=1, choices=CategoryType.choices, default=CategoryType.LOUNGEWEAR)
    brand = models.CharField(max_length=255)
    quantity = models.IntegerField()

    #display model instance
    def __str__(self):
        return self.name

# --- 