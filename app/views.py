from flask import render_template, request
from app import app
import ds
import json

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/moderator')
def moderator():
    return render_template("moderator.html")

@app.route('/moderator', methods=['POST'])
def moderator_session_data():
    session_id = ds.get_session_id()
    
    session_dict = {}
    player_dict_list = []
    print(session_id)

    total_num_players = int(request.form['num_players'])

    num_special_characters = 0
    num_werewolves = 0
    if 6 <= total_num_players <= 8:
        num_werewolves = 1
    elif 9 <= total_num_players <= 11:
        num_werewolves = 2
    elif 12 <= total_num_players <= 15:
        num_werewolves = 3
    elif total_num_players >= 16:
        num_werewolves = 4
    
    should_include_bodyguard = request.form.getlist('bodyguard')
    if (should_include_bodyguard):
        player_dict = {
            "role": "bodyguard",
            "is_alive": True
        }
        num_special_characters += 1
        player_dict_list.append(player_dict)
    
    should_include_hunter = request.form.getlist('hunter')
    if (should_include_hunter):
        player_dict = {
            "role": "hunter",
            "is_alive": True
        }
        num_special_characters += 1
        player_dict_list.append(player_dict)
    
    should_include_spellcaster = request.form.getlist('spellcaster')
    if (should_include_spellcaster):
        player_dict = {
            "role": "spellcaster",
            "is_alive": True
        }
        num_special_characters += 1
        player_dict_list.append(player_dict)
    
    should_include_doppelganger = request.form.getlist('doppelganger')
    if (should_include_doppelganger):
        player_dict = {
            "role": "doppelganger",
            "is_alive": True
        }
        num_special_characters += 1
        player_dict_list.append(player_dict)
    
    # add the werewolves
    for i in range(0, num_werewolves):
        player_dict = {
            "role": "werewolf",
            "is_alive": True
        }
        player_dict_list.append(player_dict)

    #  -1 is for the seer
    num_villagers = total_num_players - num_special_characters - num_werewolves - 1
    # TODO: check is number of villagers is not 0 or negative
    # add the villagers
    for i in range(0, num_villagers):
        player_dict = {
            "role": "villager",
            "is_alive": True
        }
        player_dict_list.append(player_dict)
    
    # but num_villagers also includes a seer
    num_villagers += 1

    # add the seer
    player_dict = {
            "role": "seer",
            "is_alive": True
        }
    player_dict_list.append(player_dict)
   
    session_dict['session_id'] = session_id
    session_dict['num_players'] = total_num_players
    session_dict["player_info"] = player_dict_list
    session_dict["num_special_chars"] = num_special_characters
    session_dict["num_werewolves"] = num_werewolves
    session_dict["num_villagers"] = num_villagers

    # return json.dumps(session_dict)
    return render_template("session.html", session_dict = session_dict)
    

@app.route('/player')
def player():
    return "Welcome, Player!"
