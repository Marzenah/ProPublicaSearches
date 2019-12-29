import json
import requests
from search_modules.proPublicaAPI import *

def search_state_reps(state_code):
    api = ProPublicaAPI() # new instance of ProPublicaAPI class
    state = state_code.upper()
    house_members = []
    senate_members = []

    for chamber in ['house', 'senate']:
        try:
            search_file = api.get(f'/members/{chamber}/{state}/current.json')
        except:
            return None

        for member in search_file:

            if member['middle_name'] == None:
                middleName = ''
            else:
                middleName = member['middle_name']
            rep =  { "first name: ": member['first_name'],
                    "  middle name: ": middleName,
                    "  last name: ": member['last_name'],
                    "  party: ": (f"party: {member['party']}")}

            if chamber == "house":
                house_members.append(rep)
            else:
                senate_members.append(rep)

    results_dict = {'State': state, 'House': house_members, 'Senate': senate_members}

    return results_dict

def results_string(state_code):
    results_dict = search_state_reps(state_code)
    if results_dict == None:
        return "No such state. Try again"
    string_out = ''
    string_out += f"State: {results_dict['State']} \n"
    string_out += '\nHouse of Representatives members: \n'
    num = 1
    for member in results_dict['House']:
        string_out += (f'\n{num}.')
        for key,val in member.items():
            string_out += (f' {val}')
        num+=1

    string_out += '\n\nSenate members: \n'
    num = 1
    for member in results_dict['Senate']:
        string_out += (f'\n{num}.')
        for key, val in member.items():
            string_out += (f' {val}')
        num+=1

    return string_out
