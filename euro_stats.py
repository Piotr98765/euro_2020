from turtle import home
from requests import get
from pprint import PrettyPrinter, pprint

printer = PrettyPrinter()

BASE_URL = "https://raw.githubusercontent.com/lsv/uefa-euro-2020/master/data.json"
general_data = get(BASE_URL).json()

def get_groups():
    teams = get(BASE_URL).json()["teams"]
    teams_dict = {}

    for team in teams:
        nickname = team["id"]
        name = team["name"]
        teams_dict[nickname] = name
    groups = get(BASE_URL).json()["groups"]
    for i, group in enumerate(groups):
        group_name = group["name"]
        winner = group["winner"]
        matches = group["matches"]
        for match in matches:
            home_team = match["home_team"]
            home_team = teams_dict[home_team]
            away_team = match["away_team"]
            away_team = teams_dict[away_team]
            home_result = match["home_result"]
            away_result = match["away_result"]
            print(home_team, "VS", away_team, "Result:", 
            home_result,"-", away_result)
            print("---------------------------------------------------")
        #print(i+1,"Name:", group_name,"Winner:", winner)
        #printer.pprint(matches)
         
#get_teams()
get_groups()

#printer.pprint(general_data["groups"])