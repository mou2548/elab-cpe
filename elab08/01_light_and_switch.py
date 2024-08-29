class Switch():
    def __init__(self, name="", status=False):
        self.name = name
        self.status = status
    
    def clone(self):
        return Switch(self.name+".copy", self.status)
    
    def turn(self):
        if self.status == True:
            self.status = False
        else:
            self.status = True

    def __str__(self):
        if self.status == True:
            status = 'on'
        else:
            status = 'off'
        return f"switch({self.name}) is {status}"

class Light():
    def __init__(self, name="", switch=None):
        self.name = name
        self.switch = switch
    
    def turn(self):
        self.switch.turn()
    
    def get_status(self):
        return self.switch
    
    def set_switch(self, new_switch):
        self.switch = new_switch

    def clone(self):
        return Light(self.name+'.copy', self.switch.clone())
    
    def __str__(self):
        return f"light({self.name}) with {self.switch}"