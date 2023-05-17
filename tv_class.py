class TV:

    # constructor
    def __init__(television, channel = 1, volume_level = 1, status = False):
        # instance variables
        television.channel = channel
        television.volume_level = volume_level
        television.status = status

    # turn on/off TV
    def turn_on_TV(television):
        television.status = True
    def turn_off_TV(television):
        television.status = False

    # get TV channel
    def get_channel(television):
        return television.channel
    
    # Set TV channel
    def set_channel(television, channel):
        if television.status and 1 <= channel <= 120:
            television.channel = channel

    # get TV volume
    def get_volume_level(television):
        return television.volume_level

    # Set TV volume
    def set_volume_level(television, volume_level):
        if television.status and 1 <= volume_level <= 7:
            television.volume_level = volume_level

    # switch channel up 
    def channel_up(television, channel):
        if television.status and 1 <= channel <= 120:
            television.channel += 1

    # switch channel down
    def channel_down(television, channel):
        if television.status and 1 <= channel <= 120:
            television.channel -= 1

    # volume up
    def volume_up(television, volume_level):
        if television.status and 1 <= volume_level <= 7:
            television.volume_level += 1

    # volume down
    def volume_down(television, volume_level):
        if television.status and 1 <= volume_level <= 7:
            television.volume_level -= 1

tv_1 = TV()
tv_1.turn_on_TV()
tv_1.set_channel(5)
tv_1.set_volume_level(6)

print("TV 1's channel is", tv_1.get_channel(), "and volume level is", tv_1.get_volume_level())

tv_2 = TV()
tv_2.turn_on_TV()
tv_2.set_channel(7)
tv_2.set_volume_level(7)

print("TV 2's channel is", tv_2.get_channel(), "and volume level is", tv_2.get_volume_level())