import uuid

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