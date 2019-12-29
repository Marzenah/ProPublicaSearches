
import json
import requests


class ProPublicaAPI():
    ''' A class for interracting with ProPublica API. '''

    def get(self, url):
        ''' This method performs HTTP GET requests through ProPublica's API. '''

        key = open('key.txt').read().strip()
        headers = {"X-API-KEY": key}
        url = "https://api.propublica.org/congress/v1" + url
        data = requests.get(url, headers=headers).json()
        return data['results']

class Congress():
    ''' A class that provides a blueprint for a Congressional session. '''

    def __init__(self, session_num):
        session_num = session_num

    def getSessionStartYear(self, session_num):
        ''' This method takes as argument the ID number of the Congressional
            2-year session and returns the year that session started. '''

        session = int(session_num)
        sessions = {102: 1991, 103: 1993, 104: 1995, 105: 1997, 106: 1999,
         107: 2001, 108: 2003, 109: 2005, 110: 2007, 111: 2009, 112: 2011,
         113: 2013, 114: 2015, 115: 2017, 116: 2019}
        return sessions[session]

    def get_reps_ages(self, session_num, chamber, api):
        ''' This method processes an API request for information on the
            congressional members in a given session and chamber; it returns
            a list with members' ages at the beginning of the session. '''

        chamber_reps_ages = []
        response = api.get(f"/{session_num}/{chamber}/members.json")
        for r in response:
            for rep in r['members']:
                dob = rep['date_of_birth'].split("-")
                session_start_year = self.getSessionStartYear(session_num)
                age= int(session_start_year) - int(dob[0]) - 1
                chamber_reps_ages.append(age)
        return chamber_reps_ages

    def average_age(self, session_num, reps_ages):
        ''' This method calculates and returns the average age of members
            whose ages are contained in the list provided as an argument. '''
        average = int(sum(reps_ages)/len(reps_ages))
        return average

    def search_member(self, session_num, firstName, lastName, api):
        member_data = {}
        for chamber in ['house', 'senate']:
            response = api.get(f"/{session_num}/{chamber}/members.json")
            for r in response:
                for rep in r['members']:
                    if rep['first_name'].lower() == firstName.lower() and rep['last_name'].lower() == lastName.lower():
                        gender = rep['gender']
                        state = rep['state']
                        party = rep['party']
                        title = rep['title']
                        dob = rep['date_of_birth']
                        twitter = rep['twitter_account']
                        facebook = rep['facebook_account']
                        youtube = rep['youtube_account']
                        url = rep['url']
                        total_votes = rep['total_votes']
                        missed_votes = rep['missed_votes']
                        office = rep['office']
                        phone = rep['phone']

                        name = (f'{firstName.capitalize()} {lastName.capitalize()}')
                        member_data = {"Name: ": name, "Gender: ": gender,
                            "State: ": state, "Party affiliation: ": party, "Title: ": title, "DOB: ": dob, "Twitter account: ": twitter, "Facebook account: ": facebook, "Youtube account: ": youtube, "Website: ": url, "Total votes: ": total_votes,
                            "Missed votes: ": missed_votes, "Office address: ": office, "Phone: ": phone}
                        return member_data

        return member_data
