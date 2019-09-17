from simlib import *

def print_time(time, msg):
    print(time, msg, sep=': ')

# TODO: add new functions below this line
def start_event(time, sim, ingredient):
    if(sim.get_available_chef_count()>0):
        print_time(time, "Starting to prep "+ingredient)
        sim.assign_chef()
        sim.schedule_event(time +sim.get_prep_time(ingredient), end_event, ingredient)
    else:
        sim.schedule_event(time+1 , start_event, ingredient)


def end_event(time, sim, ingredient):
    sim.dismiss_chef()
    print_time(time, "Done prepping "+ingredient)    

# TODO: add new functions above this line

def handle_new_order(time, sim, recipe):
    enough_ingredients= True

    for ingredient in recipe:
        if(sim.get_count(ingredient)<=0 ):
            enough_ingredients = False
    # TODO: check if there are enough ingredients
    if enough_ingredients:
        sim.increment_accepted_order_count()
        print_time(time, 'Accepting order')

        for ingredient in recipe:
            sim.schedule_event(time , start_event, ingredient)
            sim.use_ingredient(ingredient)
            #sim.schedule_event(time +sim.get_prep_time(ingredient), end_event, ingredient)
            #time=time+

        # TODO: schedule events for each ingredient
        #sim.schedule_event(time + 5, start_event, recipe[0])

    else:
        # TODO: handle case where there are not enough ingredients (and delete following line)
        sim.increment_rejected_order_count()

        pass

def setup_simulation(sim):
    sim.set_available_chef_count(2)
    sim.add_ingredient('burger', 10, 8)
    sim.add_ingredient('lettuce', 8, 2)
    sim.add_ingredient('tomato', 15, 2)
    sim.add_ingredient('bun', 20, 5)
