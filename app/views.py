from flask import render_template, request
from app import app
from app import ds
import json
import random

# global session context
# TODO: find another way to do it
g_session_dict = {}
g_random_set = set()

g_special_char_list = ['bodyguard', 'hunter', 'spellcaster', 'doppelganger']

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
    global g_special_char_list

    g_session_dict.clear()
    g_random_set.clear()

    session_id = ds.get_session_id()
    
    session_dict = {}
    player_dict_list = []

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
    
    player_id = 0
    # add the special characters
    for special_char in g_special_char_list:
        should_include = request.form.getlist(special_char)
        player_dict = {}
        if should_include:
            player_dict["player_id"] = player_id
            player_dict["role"] = special_char
            player_dict["is_alive"] = True
            player_dict["name"] = "TBD"
            player_id += 1
            num_special_characters += 1
            player_dict_list.append(player_dict)

    # add the werewolves
    for i in range(0, num_werewolves):
        player_dict = {}
        player_dict["player_id"] = player_id
        player_dict["role"] = "werewolf"
        player_dict["is_alive"] = True
        player_dict["name"] = "TBD"
        player_id += 1
        player_dict_list.append(player_dict)

    #  -1 is for the seer
    num_villagers = total_num_players - num_special_characters - num_werewolves - 1
    # TODO: check is number of villagers is not 0 or negative
    # add the villagers
    for i in range(0, num_villagers):
        player_dict = {}
        player_dict["player_id"] = player_id
        player_dict["role"] = "villager"
        player_dict["is_alive"] = True
        player_dict["name"] = "TBD"
        player_id += 1
        player_dict_list.append(player_dict)
    
    # but num_villagers also includes a seer
    num_villagers += 1

    # add the seer
    player_dict = {}
    player_dict["player_id"] = player_id
    player_dict["role"] = "seer"
    player_dict["is_alive"] = True
    player_dict["name"] = "TBD"
    player_id += 1
    player_dict_list.append(player_dict)
   
    # fill in the session details
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
    return render_template("session.html", session_dict = g_session_dict)

@app.route('/player')
def player():
    return render_template("player.html")

@app.route('/player', methods=['POST'])
def player_join():
    player_name = request.form['player_name']
    entered_session_id = request.form['session_id']

    # handle errors
    if not g_session_dict:
        return render_template('selected_player.html', error = True, err_msg = "Session not created yet. Please contact the moderator", role = None)
    if g_session_dict['session_id'] not in entered_session_id:
        return render_template('selected_player.html', error = True, err_msg = "Invalid session ID", role = None)
    if (len(g_random_set) >= g_session_dict['num_players']):
        return render_template('selected_player.html', error = True, err_msg = "Session Full! Please contact the moderator", role = None)

    # get random index from the range
    random_idx = random.randint(0, g_session_dict['num_players']-1)
    if random_idx in g_random_set:
        # make sure we don't get a duplicate
        while True:
            random_idx = random.randint(0, g_session_dict['num_players']-1)
            if random_idx not in g_random_set:
                break
    g_random_set.add(random_idx)

    alias = ""
    profession = ""

    should_include_alias = request.form.getlist('alias')
    if (should_include_alias):
        alias = ds.get_alias()
    
    should_include_profession = request.form.getlist('profession')
    if (should_include_profession):
        profession = ds.get_profession()

    # update the player name in the global session dict
    g_session_dict["player_info"][random_idx]['name'] = player_name
    return render_template("selected_player.html", error = False, err_msg = None, role = g_session_dict["player_info"][random_idx]['role'], alias = alias, profession = profession)
