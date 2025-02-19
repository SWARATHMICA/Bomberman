class Player:
    def __init__(self, position):
        self.player_pos = position


class Key:
    def __init__(self, position):
        self.key_pos = position


class Brick:
    def __init__(self, position):
        self.brick_pos = position


class Villain:
    def __init__(self, position):
        self.villain_pos = position


class Board:
    def __init__(self):
        self.size = int(input("Enter the size of the board: "))
        self.grid = {}  # Dictionary to store occupied positions

    def set_element(self, x, y, symbol):
        if 0 <= x < self.size and 0 <= y < self.size:
            self.grid[(x, y)] = symbol

    def display(self):
        # Print column labels
        print("  ", end="")
        for i in range(self.size):
            print(chr(ord('A') + i), end=" ")
        print()
        
        for i in range(self.size):
            # Print row labels
            print(chr(ord('A') + i), end=" ")
            for j in range(self.size):
                print(self.grid.get((i, j), '.'), end=' ')
            print()
        print()

    def convert_position(self, pos):
        return ord(pos[0]) - ord('A'), ord(pos[1]) - ord('A') # Conversion of labels to coordinates


class Bomberman:
    def __init__(self):
        self.board = Board()
        pos = input("Enter player position: ")
        x, y = self.board.convert_position(pos)
        self.player = Player((x, y))
        self.board.set_element(x, y, 'P')

        pos = input("Enter key position: ")
        x, y = self.board.convert_position(pos)
        self.key = Key((x, y))
        self.board.set_element(x, y, 'K')

        self.bricks = []
        self.villains = []

    def create_map(self):
        # boundaries
        for i in range(self.board.size):
            self.board.set_element(0, i, '*')
            self.board.set_element(self.board.size - 1, i, '*')
            self.board.set_element(i, 0, '*')
            self.board.set_element(i, self.board.size - 1, '*')

        # internal walls
        for i in range(2, self.board.size - 2, 2):
            for j in range(2, self.board.size - 2, 2):
                self.board.set_element(i, j, '*')

        # bricks
        brick_count = int(input("Enter number of bricks: "))
        for _ in range(brick_count):
            pos = input("Enter brick position: ")
            x, y = self.board.convert_position(pos)
            self.bricks.append(Brick((x, y)))
            self.board.set_element(x, y, 'B')

        # villains
        villain_count = int(input("Enter number of villains: "))
        for _ in range(villain_count):
            pos = input("Enter villain position: ")
            x, y = self.board.convert_position(pos)
            self.villains.append(Villain((x, y)))
            self.board.set_element(x, y, 'V')

    def display(self):
        self.board.display()


game = Bomberman()
game.create_map()
game.display()
