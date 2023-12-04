from collections import Counter


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
        self.child_cards: int = 2 ** (self.matches - 1) if self.matches else 0


class Games:
    def __init__(self):
        self.games: dict[int, Game] = {}
        self.copies = Counter()

    def add_game(self, line) -> None:
        game = Game(line)
        self.games.update({game.game_id: game})
        for _ in range(self.copies[game.game_id] + 1):
            for game_id in range(game.game_id + 1, game.game_id + game.matches + 1):
                self.copies.update([game_id])

    def get_total_cards(self) -> int:
        return sum(
            [value for key, value in self.copies.items() if key in self.games.keys()]
        ) + len(self.games.keys())

    def get_copies(self):
        return self.copies


with open("day4/input.txt", mode="r") as f:
    lines = f.read().splitlines()
    games = Games()
    [games.add_game(line) for line in lines]
    print(games.get_total_cards())
    print(games.get_copies())
