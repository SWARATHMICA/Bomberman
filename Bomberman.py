class Bomberman:
    def __init__(self):
        self.n = int(input("Map size: "))
        self.mapp = [['' for _ in range(self.n)] for _ in range(self.n)]

        # Initialize boundary letters
        self.boundary = {0: ' '}
        for i in range(self.n - 1):
            self.boundary[i + 1] = chr(ord('A') + i)

        # Create boundary with letters at top and left
        for i in range(self.n):
            self.mapp[0][i] = self.boundary[i]  # Top boundary
            self.mapp[i][0] = self.boundary[i]  # Left boundary
        self.mapp[0][0] = ' '

    def create_map(self):
        # Walls inside the map
        for i in range(1, self.n):
            for j in range(1, self.n):
                if i == 1 or i == self.n - 1 or j == 1 or j == self.n - 1:
                    self.mapp[i][j] = '*'  # Border walls
                elif i % 2 != 0 and j % 2 != 0:
                    self.mapp[i][j] = '*'  # Internal walls

        # Player position
        self.player_pos = input("Enter Player position: ")
        for k in self.boundary.keys():
            if self.boundary[k] == self.player_pos[0]:
                i = k
            if self.boundary[k] == self.player_pos[1]:
                j = k
        self.mapp[i][j] = 'P'

        # Key position
        self.key_pos = input("Enter key position: ")
        for k in self.boundary.keys():
            if self.boundary[k] == self.key_pos[0]:
                i1 = k
            if self.boundary[k] == self.key_pos[1]:
                j1 = k
        self.mapp[i1][j1] = 'K'

        # Brick positions
        self.no_bricks = int(input("Number of bricks: "))
        self.brick_pos = []
        for _ in range(self.no_bricks):
            pos = input("Enter brick position: ")
            self.brick_pos.append(pos)
        for pos in self.brick_pos:
            for k in self.boundary.keys():
                if self.boundary[k] == pos[0]:
                    i2 = k
                if self.boundary[k] == pos[1]:
                    j2 = k
            self.mapp[i2][j2] = 'B'

        # Villain positions
        self.no_villians = int(input("Number of villains: "))
        self.villian_pos = []
        for _ in range(self.no_villians):
            pos = input("Enter villain position: ")
            self.villian_pos.append(pos)
        for pos in self.villian_pos:
            i3 = j3 = None
            for k in self.boundary.keys():
                if self.boundary[k] == pos[0]:
                    i3 = k
                if self.boundary[k] == pos[1]:
                    j3 = k
            if i3 is None or j3 is None:
                raise ValueError(f"Invalid position input: {pos}. Check your boundary values.")
            self.mapp[i3][j3] = 'V'

    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.mapp[i][j] if self.mapp[i][j] else '.', end=' ')
            print()


# Create a Bomberman game object and initialize the map
b = Bomberman()
b.create_map()
b.display()
