#!/usr/bin/python
import os
import random
import time
from Tkinter import *


class Presentation(object):
    def __init__(self):
        # initiate settings.screen
        self.root = Tk()
        self.root.title('RPGame')
        self.root.geometry(settings.SCREEN)
        self.root.configure(background='black')

        self.root.mainloop()


class settings(object):
    SCREEN = '800x650'
    FORMATED_OPTIONS = "[{}]  "
    MENU = ["move", "select item", "exit"]
    INFO = {"location": "forest", "health": 100, "energy": 100,
            "items": {}, "selected_item": None}
    SITES = {
        "city": {
            "options": {"house", "market", "smith"},
        },
        "forest": {
            "options": {
                "Pick wood": {"energy": -10, "wood": 1},
                "Plant a tree": {"energy": -20, "tree": -1},
                "Pick apples": {"energy": -5, "apples": 1},
                },
            "probabilities": {"tree": 0.1, "apples": 0.2},
            "wood": 2, "apples": 10,
        },
        "mine": {},
    }


class Logic(object):
    def __init__(self):
        super(Logic, self).__init__()
        print "try to create a main character"
        self.create_main_character()
        print "create main character with sucess\n"
        print "try to create all places"
        self.create_places()
        print "create all places with sucess"
        self.gon.do_something()

    def create_main_character(self):
        self.gon = Person(logic=self)

    def create_places(self):
        for site in settings.SITES:
            print site
            site_class = getattr(Places, site.title())(logic=self)
            setattr(self, site, site_class)

    def check_if_you_are_in_the_forest(self):
        print "check if you are in the forest"
        # check if you are in the forest
        if self.gon.location != "forest":
            print "you are not in the forest"
            raw_input()
            return False
        return True

    def check_if_the_forest_have_enough_resource(self, resource, quantity=1):
        # check if the forest have enough wood
        resource_in_forest = getattr(self.forest, resource)
        print resource_in_forest
        if resource_in_forest < quantity:
            print "there are no wood in the forest, please plant some tree"
            raw_input()
            return False
        setattr(self.forest, resource, resource_in_forest - quantity)
        return True

    def check_if_you_have_enough_energy(self, energy):
        # check if you have enough energy
        if self.gon.energy < energy:
            print "you need to eat, your have {}% the energy".format(
                  self.gon.energy)
            raw_input()
            return False
        self.gon.energy -= energy
        return True

    def add_item2items(self, item, quantity=1):  # item = "wood"
        if item in self.gon.items:
            self.gon.items[item] += quantity
        else:
            self.gon.items[item] = quantity
        print "{}  +{} => {}".format(item, quantity, self.gon.items[item])

    # Actions in forest
    def pick_wood(self):
        print "\npick some wood"
        if not self.check_if_you_are_in_the_forest():
            return
        print "you are in forest"
        wood = settings.SITES["forest"]["options"]["Pick wood"]["wood"]
        energy = abs(settings.SITES["forest"]["options"]["Pick wood"]["energy"])
        if not self.check_if_the_forest_have_enough_resource(resource="wood", quantity=wood):
            return
        if not self.check_if_you_have_enough_energy(energy):
            return
        self.add_item2items(item="wood", quantity=wood)
        raw_input()

    def plant_a_tree(self):
        if not self.check_if_you_are_in_the_forest():
            return
        if "tree" in self.gon.items:
            self.items["tree"] -= 1
            # check if you still have any trees
            if self.items["tree"] == 0:
                self.items.pop("tree")
            self.forest.wood += settings.PLANT_A_TREE["wood"]
        else:
            print "\nyou do not have any tree to plant"
            raw_input()

    def pick_apples(self):
        if not self.check_if_you_are_in_the_forest():
            return
        apples = settings.SITES["forest"]["options"]["Pick apples"]["apples"]
        energy = abs(settings.SITES["forest"]["options"]["Pick apples"]["energy"])
        if not self.check_if_the_forest_have_enough_resource(resource="apples", quantity=apples):
            return
        if not self.check_if_you_have_enough_energy(energy):
            return
        self.add_item2items(item="apples", quantity=apples)
        raw_input()


class Person(object):
    def __init__(self, logic=None, attributes=settings.INFO):
        self.logic = logic
        for attribute, attribute_value in attributes.iteritems():
            setattr(self, attribute, attribute_value)
        self.selected_item = None

    def print_menu(self):
        os.system('clear')
        self.get_information()
        self.print_options()

    def get_information(self):
        for feature in settings.INFO:
            print "{}: {}".format(feature, getattr(self, feature))
        print

    def print_options(self):
        current_place = self.location
        for option in settings.SITES[current_place]["options"]:
            print settings.FORMATED_OPTIONS.format(option),
        for option in settings.MENU:
            print settings.FORMATED_OPTIONS.format(option),

    def exit(self):
        print "have a nice day :)"
        sys.exit(0)

    def do_something(self):
        self.print_menu()
        do = raw_input("\nwhat you wanna do? ")
        do = do.replace(" ", "_").lower()
        print do
        try:
            # check if there are any method in Person class
            getattr(self, do)()
        except AttributeError:
            getattr(self.logic, do)()
            # try:
            #     # check if there are any method in Logic class
            #     getattr(self.logic, do)()
            # except AttributeError as e:
            #     print "please chose a valid action ({})".format(e)
        self.do_something()

    def move(self):  # decide_where_want2go
        print "\nI'm decided where I want to go"
        for option in settings.SITES:
            print settings.FORMATED_OPTIONS.format(option),
        where = raw_input("\nwhere you want to go? ")
        if where in settings.SITES:
            setattr(self, 'location', where)
        else:
            print "don't know that place/n"
            self.move()

    def select_item(self):
        for item, value in self.items.iteritems():
            print "{}: {}   ".format(item, value),
        item = raw_input("\nwhat item you want? ")
        if item in self.items:
            self.selected_item = item
        else:
            print "that item is not on item you own"
            time.sleep(3)


class Places(object):
    class City(object):
        def __init__(self, logic=None, market=None):
            self.logic = logic
            self.market = market

        def print_greetings(self):
            print "\nI entered the city"
            print "have a nice day"

    class Forest(object):
        def __init__(
            self, logic=None,
            wood=settings.SITES["forest"]["wood"],
            apples=settings.SITES["forest"]["apples"]):
            self.wood = wood
            self.apples = apples

    class Mine(object):
        def __init__(self, logic=None):
            pass


def run():
    Logic()
    # Presentation()


if __name__ == '__main__':
    os.system('clear')
    print 'is running\n'
    run()
