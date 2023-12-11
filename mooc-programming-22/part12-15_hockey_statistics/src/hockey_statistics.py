import json

"""
    {
      "name": "Travis Zajac",
      "nationality": "CAN",  
      "assists": 16,
      "goals": 9,
      "penalties": 28,       
      "team": "NJD",
      "games": 69
    },
"""


class Application():
    def __init__(self) -> None:
        self.hockey_league = None # should store the json file after read_data() is called. 
    
    def ask_file(self):
        file_name = input("file name: ")
        #file_name = r"C:\Users\Wilson\AppData\Local\tmc\vscode\mooc-programming-22\part12-15_hockey_statistics\src\partial.json"
        return file_name

    # returns a list of dictionaries (json)
    def read_data(self, file_name: str):
        with open(file_name, 'r') as file:
            my_string = file.read()  # reads file contents and stores into a string
            #print(my_string) 
        self.hockey_league = json.loads(my_string) #  parses a JSON-formatted string (in this case, my_data) and converts it into a Python object, like a dictionary or a list
        print(f"read the data of {len(self.hockey_league)} players")
    
    
    def search_for_player(self, name: str):
        for player in self.hockey_league:
            if player["name"] == name:
                print(f"{player['name']:21}{player['team']}{player['goals']:>4} + {player['assists']:>2} = {(player['goals'] + player['assists']):>3}")

        #print("123456789012345678901234567890123456789")
    # list all the abbreviations for team names in alphabetical order

    def teams(self):
        all_teams = sorted(set([player['team'] for player in self.hockey_league]))

        for team in all_teams:
            print(team)
    
    # list all the abbreviations for countries in alphabetical order
    def countries(self):
        all_countries = sorted(set([player['nationality'] for player in self.hockey_league]))

        for country in all_countries:
            print(country)

    # list players in a specific team in the order of points scored, from highest to lowest. Points equals goals + assists
    def players_in_team(self, team_name):
        team_players = [player for player in self.hockey_league if player['team'] == team_name]
        team_players = sorted(team_players, key= lambda player : player['assists'] + player['goals'], reverse=True)

        for player in team_players:
            self.search_for_player(player['name']) # print function should be a seperate thing, but it is what it is 

    # list players from a specific country in the order of points scored, from highest to lowest
    def players_in_country(self, country: str):
        team_players = [player for player in self.hockey_league if player['nationality'] == country]
        team_players = sorted(team_players, key= lambda player : player['assists'] + player['goals'], reverse=True)

        for player in team_players:
            self.search_for_player(player['name']) # print function should be a seperate thing, but it is what it is 

    def most_points(self, n: int):
                                                                 
        team_players = [player for player in self.hockey_league]

        # tupule here sorts by total points, then if same, sorts by highest goal count 
        team_players = sorted(team_players, key= lambda player : (player['goals'] + player['assists'], player['goals']), reverse=True)

        # get top players
        top_players = team_players[:n]

        for player in top_players:
            self.search_for_player(player['name'])

    def most_goals(self, n: int):
                                                                         
        team_players = [player for player in self.hockey_league]

        # sorts by most goals, then if same, sorts by lowest games, #okay the bug is that it's sorting by games, but by highest number of games--FIXME: should sort by lowest num games 
        #FIXED: just negate the player['games'] by adding a negative sign :) ! 
        team_players = sorted(team_players, key= lambda player : (player['goals'], -player['games']), reverse=True)

        # get top players
        top_players = team_players[:n]

        for player in top_players:
            self.search_for_player(player['name'])



    def help(self): 
        print("commands: ")
        print("0 quit")  
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")    


    def execute(self):
        self.read_data(self.ask_file())
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                name = input("name: ")
                self.search_for_player(name) # I should seperate the application interface from the hockey_team object. 
            elif command == "2":
                self.teams()
            elif command == "3": 
                self.countries()
            elif command == "4":
                team_name = input("team: ")
                self.players_in_team(team_name)
            elif command == "5":
                country = input("country: ")
                self.players_in_country(country)
            elif command == "6":
                num = int(input("how many: "))
                self.most_points(num)
            elif command == "7":
                num = int(input("how many: "))
                self.most_goals(num)
            else:
                self.help()




hey = Application()
hey.execute()

