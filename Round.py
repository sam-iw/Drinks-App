class Round:
    # constructor with brewer as an argument
    def __init__(self, brewer):
        # assign a brewer
        self.brewer = brewer
        # set active to true
        self.active = True
        # create an empty dictionary
        self.orders = {brewer: prefs[brewer]}
    # add person method
    def add_person(self, name):
        # only add if round is active
        if self.active:
            self.orders[name] = prefs[name]
        else:
            print("Sorry this round is closed")
    # set round to inactive method
    def stop_orders(self):
        self.active = False

