import settings


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
