

class World:

    def __init__(self, length, initial_bananas, step):
        self.length = length
        self.bananastores = {0: BananaStore(initial_bananas, initial_bananas)}
        self.step = step
        self.initial_bananas = initial_bananas

    def get_final_bananas(self, camel_carrying_capacity):
        my_camel = Camel(camel_carrying_capacity)
        if my_camel.location in self.bananastores:
            free_space = my_camel.banana_store.remaining_capacity
            pick_up = max(free_space,)
        # Camel needs to pick up bananas
        # Camel needs to move a specific distance
        # Camel needs to drop bananas, but keep enough to get back
        # Camel goes back to get move bananas
        return "Hello!"


class Camel:

    def __init__(self, max_bananas):
        self.max_bananas = max_bananas
        self.banana_store = BananaStore(0, self.max_bananas)
        self.location = 0

    def move(self, distance):
        """Positive distance moves towards destination
        negative distance moves towards the beginning"""
        self.location += distance
        self.banana_store.remove(abs(distance))


class BananaStore:

    def __init__(self, bananas, max_bananas):
        self.bananas = bananas
        self.max_bananas = max_bananas

    def add(self, number):
        if number >= 0:
            self.bananas += number
        else:
            raise ValueError("You cannot add negative bananas")
        if self.max_bananas < self.bananas:
            raise ValueError("Too many bananas")

    def remove(self, number):
        if self.bananas >= number >= 0:
            self.bananas -= number
        else:
            if number < 0:
                raise ValueError("You cannot remove negative bananas")
            else:
                raise ValueError(f"You only have {self.bananas} bananas, tried "
                                 f"to remove {number} bananas")

    @property
    def remaining_capacity(self):
        return self.max_bananas - self.bananas


if __name__ == "__main__":

    length = 1000
    initial_bananas = 3000
    camel_carrying_capacity = 1000

    for x in range(1000):
        step = x
        world = World(length, initial_bananas, step)
        results = world.get_final_bananas(camel_carrying_capacity)
        print(results)