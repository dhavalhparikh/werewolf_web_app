import uuid
import random
import json

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
    with open('app/data.json') as f:
        data = json.load(f)
        f.close
    return random.choice(data["names"])

def get_profession():
    with open('app/data.json') as f:
        data = json.load(f)
        f.close
    quality = random.choice(data["quality"])
    position = random.choice(data["profession"])
    return quality + " " + position