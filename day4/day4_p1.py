class Game:
    def __init__(self, line: str):
        self.game_id: int = int(line[4 : line.index(":")])
        self.winners: list[int] = [
            int(x) for x in line[line.index(":") + 1 : line.index("|")].split(" ") if x
        ]
        self.numbers: list[int] = [
            int(x) for x in line[line.index("|") + 1 : len(line)].split(" ") if x
        ]
        self.matches: int = len(set(self.winners).intersection(set(self.numbers)))
        self.points: int = 2 ** (self.matches - 1) if self.matches else 0


with open("day4/input.txt", mode="r") as f:
    lines = f.read().splitlines()
    games = (Game(line) for line in lines)
    print(sum([game.points for game in games]))
