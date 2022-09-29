class Player:
    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]

    def __repr__(self):
        return f"Player: {self.name}, Year: {self.age}, Position: {self.position}, Team: {self.team}"
    

    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)

    @classmethod
    def get_team(cls, team_list):
        cls.populate_list(team_list)


kevin = {
    "name" : "Kevin Durant",
    "age" : 34,
    "position" : "small forward",
    "team" : "Brooklyn Nets"
}

jason = {
    "name" : "Jason Tatum",
    "age" : 24,
    "position" : "Point Guard",
    "team" : "Brooklyn Nets"
}

kyrie = {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

players = [kevin, jason, kyrie]

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

player_kevin.display_info()

new_team = []
for player in players:
    a_player = Player(player)
    new_team.append(a_player)

print(new_team)

