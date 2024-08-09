#  classes are BLUEPRINTS for objects

class Vehicle:
    # methods
    def __init__(self, make, model):
        self.make = make               # properties
        self.model = model             # properties

    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Telsa', 'Model 3')

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Range Rover', 'Defender')
your_car.get_make_model()
my_car.moves()


class Airplane(Vehicle):
    # methods
    def __init__(self, make, model, faa_id):
        # <--- this means we will inherit these from the parent, we dont need to set those individually.
        super().__init__(make, model)
        # <--- it come in handy when you have to the property had more information than its parent. That is why you have to redefine the initallizer like above.
        self.faa_id = faa_id

    def moves(self):
        print('Flies along...')


class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')


class GolfCart(Vehicle):
    # <--- This will inherit the message from the orginal print statement: print('Moves along..')
    pass


# objects
cessna = Airplane('cessna', 'Skyhawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

print('\n\n')

####################################
# PLOY-morphism
# the ability to behave differently in response to the same input message

# in the loop below we can expect to get different responses when we call .get_make_model, eventhough we are giving these object the same input message.
for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()
