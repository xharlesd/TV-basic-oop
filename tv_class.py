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

    # get TV channel
    def get_channel(self):
        return self.channel
    
    # Set TV channel
    def set_channel(self, channel):
        if self.status and 1 <= channel >= 120:
            self.channel = channel

    # get TV volume
    def get_volume(self):
        return self.volume_level

    # Set TV volume
    def set_volume(self, volume_level):
        if self.status and 1 <= volume_level >= 7:
            self.volume_level = volume_level

    # switch channel up 
    def channel_up(self, channel):
        if self.status and 1 <= channel >= 120:
            self.channel += 1

    # switch channel down
    def channel_down(self, channel):
        if self.status and 1 <= channel >= 120:
            self.channel -= 1

    # volume up
    def volume_up(self, volume_level):
        if self.status and 1 <= volume_level >= 7:
            self.volume_level += 1

    

