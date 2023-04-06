class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def index_of_body(self):
        return self.ro * self.volume

    def __eq__(self, other):
        other = other.index_of_body() if isinstance(other, Body) else other
        return self.index_of_body() == other

    def __lt__(self, other):
        other = other.index_of_body() if isinstance(other, Body) else other
        return self.index_of_body() < other

    def __gt__(self, other):
        other = other.index_of_body() if isinstance(other, Body) else other
        return self.index_of_body() > other

