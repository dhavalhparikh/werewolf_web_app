import uuid
import random

# list of player_dict dictionaries
player_dict_list = []

# the player dictionary
player_dict = {
    # "name": "name",
    # "role": "role",
    # "is_alive": True
}

# the session dicationary
session_dict = {
    # "session_id": "xxxx",
    # "num_players": 7,
    # "player_info": player_dict_list
}

# returns the last 4 characters of the
# generated uuid
def get_session_id():
    return str(uuid.uuid4())[-4:]

def get_alias():
    return random.choice(["John","Smith","Suzie","ShoeDog","Bob","Nicolas",
    "Barbra","Henry","Thomas","Ronald","Margaret","Claudia","Berta","Agnes",
    "Mary","Paula","Paul","Ivan","Alexey","Gretta","Alexandra","Svetlana",
    "Natasha","Laura","Aarav","Vivaan","Aditya","Arjun","Shaurya","Adhira",
    "Charu","Eka","Hiya","Keya", "Pedro Pedro","Dwight Schrute"])

def get_profession():
    quality = random.choice(["Apprentice","Wannabe","Mature","Elder","Underqualified",
    "Overqualified","Accomplished","Reknown","Wealthy","Famous","Avoided","Strange",
    "Unwelcoming","Friendly","Surprising","Optimistinc","Pessimistic","Angry","Happy",
    "Boring","Annoying","Smelly","Bright","Fun","Trendy","Upcoming"])
    position = random.choice(["Barber","Shopkeep","Librarian","Smith","Guard",
    "City Council","Firefighter","Pirate","Batender","Inn Keep","Drunkard",
    "Hermit","Dentist","Lumberjack","Monk","Herbalist","Doctor","Teacher",
    "Banker","Scientist","Alchemist","Shoe Maker","Baker","Confectioner","Lawyer"])
    return quality + " " + position