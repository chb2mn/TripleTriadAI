class Card:
    def __init__(self, name="\t\t\t", north=0, east=0, south=0, west=0, level=0):
        self.n = north
        self.w = west
        self.e = east
        self.s = south
        self.name = name
        self.level = level
        self.owner = 0
        self.color = 0

    def __str__(self):
        return "|-----------|\n" \
               "|{}|\n" \
               "|Color: {}\t|\n" \
               "|N: {}\t\t|\n" \
               "|E: {}\t\t|\n" \
               "|S: {}\t\t|\n" \
               "|W: {}\t\t|\n" \
               "|-----------|".format(self.name[:10], self.color, self.n, self.e, self.s, self.w)

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, other):
        if len(self.name) == 0 or len(other.name) == 0:
            return None
        else:
            return self.name == other.name