from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        name = f'{stars_count} stars Hotel'
        return cls(name)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = self._find_room(room_number)
        result = room.take_room(people)
        if result is None:
            self.guests += people
        else:
            return result

    def free_room(self, room_number):
        room = self._find_room(room_number)
        result = room.free_room()
        if result is None:
            self.guests -= room.guests
            room.guests = 0
        else:
            return result

    def _find_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room

    def print_status(self):
        free_rooms = [room.number for room in self.rooms if not room.is_taken]
        taken_rooms = [room.number for room in self.rooms if room.is_taken]
        print(f'Hotel {self.name} has {self.guests} total guests')
        print(f'Free rooms: {", ".join(map(str, free_rooms))}')
        print(f'Taken rooms: {", ".join(map(str, taken_rooms))}')
