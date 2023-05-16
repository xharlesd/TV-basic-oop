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
    
    # Set TV channel
    def set_channel(self, channel):
        if 1 <= channel >= 120:
            self.channel = channel

    # TV volume
    def get_volume(self):
        return self.volume_level

    # Set TV volume
    def set_volume(self, volume_level):
        if 1 <= volume_level >= 7:
            self.volume_level = volume_level

    # channel up or down

    # volume up or down