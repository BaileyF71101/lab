class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):

        self.channel = 0
        self.volume = 0
        self.status = 'Off'

        """
        - Create a private variable to store the TV channel. It should be set to the minimum TV channel by default.
        - Create a private variable to store the TV volume. It should be set to the minimum TV volume by default.
        - Create a private variable to store the TV status. The TV should start when it is off.
        """

    def power(self):

        if self.status == 'On':
            self.status = 'Off'
        else:
            self.status = "On"

        """
        - This method should be used to turn the TV on/off.
        - If called on a TV object that is off, the TV object should be turned on.
        - If called on a TV object that is on, the TV object should be turned off.
        """

    def channel_up(self):

        if self.status == "On":
            if self.channel < Television.MAX_CHANNEL:
                self.channel += 1
            else:
                self.channel = Television.MIN_CHANNEL

        """
        - This method should be used to adjust the TV channel by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
        """

    def channel_down(self):

        if self.status == "On":
            if self.channel > Television.MIN_CHANNEL:
                self.channel -= 1
            else:
                self.channel = Television.MAX_CHANNEL

        """
        - This method should be used to adjust the TV channel by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        """

    def volume_up(self):

        if self.status == "On":
            if self.volume < Television.MAX_VOLUME:
                self.volume += 1

        """
        - This method should be used to adjust the TV volume by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
        """

    def volume_down(self):

        if self.status == "On":
            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1

        """
        - This method should be used to adjust the TV volume by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.
        """

    def __str__(self):

        stat = False
        if self.status == "On":
            stat = True

        return f'TV Status: Is on = {stat}, Channel = {self.channel}, Volume = {self.volume}'

        # """
        # - This method should be used to return the TV status using the format shown in the comments of main.py
        # """
