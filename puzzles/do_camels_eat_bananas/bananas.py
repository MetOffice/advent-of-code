

class World:

    def __init__(self, length, initial_bananas, step):
        self.length = length
        self.bananastores = {0: BananaStore(initial_bananas, initial_bananas)}
        self.step = step
        self.initial_bananas = initial_bananas
        self.camel = None
        
    def spawn_camel(self, camel_carrying_capacity):
        """
        Create a camel in the world.
        """
        if self.camel is None:
            self.camel = Camel(camel_carrying_capacity)
        else:
            raise AttributeError("There is only one camel.")
    
    def kill_camel(self):
        """
        >:)
        """
        self.camel = None
    
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
    
    def round_trip(self, end_point):
        """
        Perform a round trip - update all banana stores and camel's banana store.
        """
        # Camel picks up bananas
        bananas_at_start = self.bananastores[self.camel.location]
        bananas_to_pick_up = max(self.camel.banana_store.remaining_capacity(), bananas_at_start.bananas)
        self.camel.banana_store.add(bananas_to_pick_up)

        # Camel walks to destination and drops bananas
        distance = end_point - self.camel.location
        self.camel.move(distance)
        number_of_bananas_to_drop = self.camel.banana_store.bananas - self.camel.bananas_required(distance)





class Camel:

    def __init__(self, camel_carrying_capacity):
        self.camel_carrying_capacity = camel_carrying_capacity
        self.banana_consumption_rate = 1
        self.banana_store = BananaStore(0, self.camel_carrying_capacity)
        self.location = 0

    def move(self, distance):
        """Positive distance moves towards destination
        negative distance moves towards the beginning"""
        self.location += distance
        self.banana_store.remove(self.bananas_required(distance))
    
    def bananas_required(self, distance):
        return self.banana_consumption_rate * abs(distance)
    
    def possible_round_trip(self):
        """
        Return the maximum possible round trip distance, assuming the camel drops all its bananas.
        """
        return self.banana_store.bananas // 2
    
    def drop_bananas(self, box):
        """

        """
    


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
        world.spawn_camel(camel_carrying_capacity)
        results = world.get_final_bananas(camel_carrying_capacity)
        print(results)