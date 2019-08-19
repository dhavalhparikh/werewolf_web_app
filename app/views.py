from flask import render_template, request
from app import app
import ds
import json
import random

# global session context
# TODO: find another way to do it
g_session_dict = {}
g_random_set = set()

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
    global g_session_dict
    global g_random_set

    g_session_dict.clear()
    g_random_set.clear()

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
            "is_alive": True,
            "name": "TBD"
        }
        num_special_characters += 1
        player_dict_list.append(player_dict)
    
    should_include_hunter = request.form.getlist('hunter')
    if (should_include_hunter):
        player_dict = {
            "role": "hunter",
            "is_alive": True,
            "name": "TBD"
        }
        num_special_characters += 1
        player_dict_list.append(player_dict)
    
    should_include_spellcaster = request.form.getlist('spellcaster')
    if (should_include_spellcaster):
        player_dict = {
            "role": "spellcaster",
            "is_alive": True,
            "name": "TBD"
        }
        num_special_characters += 1
        player_dict_list.append(player_dict)
    
    should_include_doppelganger = request.form.getlist('doppelganger')
    if (should_include_doppelganger):
        player_dict = {
            "role": "doppelganger",
            "is_alive": True,
            "name": "TBD"
        }
        num_special_characters += 1
        player_dict_list.append(player_dict)
    
    # add the werewolves
    for i in range(0, num_werewolves):
        player_dict = {
            "role": "werewolf",
            "is_alive": True,
            "name": "TBD"
        }
        player_dict_list.append(player_dict)

    #  -1 is for the seer
    num_villagers = total_num_players - num_special_characters - num_werewolves - 1
    # TODO: check is number of villagers is not 0 or negative
    # add the villagers
    for i in range(0, num_villagers):
        player_dict = {
            "role": "villager",
            "is_alive": True,
            "name": "TBD"
        }
        player_dict_list.append(player_dict)
    
    # but num_villagers also includes a seer
    num_villagers += 1

    # add the seer
    player_dict = {
            "role": "seer",
            "is_alive": True,
            "name": "TBD"
        }
    player_dict_list.append(player_dict)
   
    session_dict['session_id'] = session_id
    session_dict['num_players'] = total_num_players
    session_dict['player_info'] = player_dict_list
    session_dict['num_special_chars'] = num_special_characters
    session_dict['num_werewolves'] = num_werewolves
    session_dict['num_villagers'] = num_villagers

    # store in global session dict
    g_session_dict = session_dict

    # return json.dumps(session_dict)
    return render_template("session.html", session_dict = g_session_dict)
    
@app.route('/reload')
def reload_session_data():
    # here the reload is only mocking dead werewolves on reload
    if g_session_dict:
        for dict_item in g_session_dict["player_info"]:
            if "werewolf" in dict_item["role"]:
                dict_item['name'] = "Makinda"
                dict_item['is_alive'] = False
    
    return render_template("session.html", session_dict = g_session_dict)

@app.route('/player')
def player():
    return render_template("player.html")

@app.route('/player', methods=['POST'])
def player_join():
    player_name = request.form['player_name']
    entered_session_id = request.form['session_id']
    if not g_session_dict:
        return "Session not created yet!"

    random_idx = random.randint(0, g_session_dict['num_players'])
    if random_idx in g_random_set:
        while True:
            random_idx = random.randint(0, g_session_dict['num_players']-1)
            if random_idx not in g_random_set:
                break
    g_random_set.add(random_idx)
        
    print(random_idx)
    g_session_dict["player_info"][random_idx]['name'] = player_name

    if g_session_dict['session_id'] in entered_session_id:
        return render_template("selected_player.html", role = g_session_dict["player_info"][random_idx]['role'])
    return "Session ID invalid"
