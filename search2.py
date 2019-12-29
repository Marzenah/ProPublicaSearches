import json
import sys
import requests
from search_modules.proPublicaAPI import *

def member_data(first, last):
    api = ProPublicaAPI() # new instance of ProPublicaAPI class
    mamber_stats = {}
    for num in range(116, 111, -1):
        cong = Congress(num)

        member_stats = cong.search_member(num, first, last, api)
        if member_stats != {}:
            break
    return member_stats



def results_string(first, last):
    results_dict = member_data(first, last)
    if results_dict == {}:
        return "No such member in US Congress"
    else:
        string_out = ''
        for key, value in results_dict.items():
            string_out += (f"{key}{value} \n")

        return string_out
