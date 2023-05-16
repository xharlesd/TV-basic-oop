class TV:

    # constructor
    def __init__(self, channel = 1, volume_level = 1, status = False):
        # instance variables
        self.channel = channel
        self.volume_level = volume_level
        self.status = status

    # turn on/off TV
    def turn_on_TV(self):
        self.status = True
    def turn_off_TV(self):
        self.status = False

    # TV channel
    def get_channel(self):
        return self.channel
    

    # TV volume

    # channel up or down

    # volume up or down