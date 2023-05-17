class TV:

    # constructor
    def __init__(television, channel = 1, volume_level = 1, status = False):
        # instance variables
        television.channel = channel
        television.volume_level = volume_level
        television.status = status

    # turn on the TV
    def turn_on_TV(television):
        television.status = True

    # turn off the TV
    def turn_off_TV(television):
        television.status = False

    # get TV channel
    def get_channel(television):
        return television.channel  # return channel
    
    # set a new TV channel
    def set_channel(television, channel):
        if television.status and 1 <= channel <= 120:
            television.channel = channel

    # get TV volume
    def get_volume_level(television):
        return television.volume_level

    # set a new TV volume
    def set_volume_level(television, volume_level):
        if television.status and 1 <= volume_level <= 7:
            television.volume_level = volume_level

    # increases channel number by 1
    def channel_up(television, channel):
        if television.status and 1 <= channel <= 120:
            television.channel += 1

    # decreases channel number by 1
    def channel_down(television, channel):
        if television.status and 1 <= channel <= 120:
            television.channel -= 1

    # increases volume level by 1
    def volume_up(television, volume_level):
        if television.status and 1 <= volume_level <= 7:
            television.volume_level += 1

    # decreases volume level by 1
    def volume_down(television, volume_level):
        if television.status and 1 <= volume_level <= 7:
            television.volume_level -= 1

# FINAL