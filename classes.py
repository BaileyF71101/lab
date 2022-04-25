class Television:
    """
    This class is for all functions for a television remote, and where the television will follow commands
    """

    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self, channel: int, volume: int, status: bool) -> None:

        """
        Constructor to create initial state of the television object, and to store variables and their
        parameters throughout file

        :param self.channel: the number associated with a particular television station
        :param self.volume: the number associated with the level of noise coming from the television
        :param self.status: the boolean value of 'True' or 'False', which describes if the television is powered
        """

        self.channel: int = channel
        self.volume: int = volume
        self.status: bool = status

    def power(self) -> bool:

        """
        Method to activate/deactivate the television's power when called
        """

        if self.status is True:
            self.status = False
        elif self.status is False:
            self.status = True

        return self.status

    def channel_up(self) -> int:

        """
        Method to increase the self.channel variable by 1, or reset to minimum value if self.channel is at
        maximum value when called (assuming power status is True)
        """

        if self.status is True:
            if self.channel < Television.MAX_CHANNEL:
                self.channel += 1
            else:
                self.channel = Television.MIN_CHANNEL

        return self.channel

    def channel_down(self) -> int:

        """
        Method to decrease the self.channel variable by 1, or reset to maximum value if self.channel is at
        minimum value when called (assuming power status is True)
        """

        if self.status is True:
            if self.channel > Television.MIN_CHANNEL:
                self.channel -= 1
            else:
                self.channel = Television.MAX_CHANNEL

        return self.channel

    def volume_up(self) -> int:

        """
        Method to increase the self.volume variable by 1, or remain at same level if self.volume is
        already at maximum value when called (assuming power status is True)
        """

        if self.status is True:
            if self.volume < Television.MAX_VOLUME:
                self.volume += 1

        return self.volume

    def volume_down(self) -> int:

        """
        Method to decrease the self.volume variable by 1, or remain at same level if self.volume is
        already at minimum value when called (assuming power status is True)
        """

        if self.status is True:
            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1

        return self.volume

    def __str__(self) -> str:

        """
        Method to give the values of the variables self.status, self.channel, and self.volume, in that
        order

        :return: returns a string stating the current states of the variables self.status,
        self.channel, and self.volume, in that order (regardless if input variables were type(str) or not
        prior to return)
        """

        stat = False
        if self.status is True:
            stat = True

        return f'TV Status: Is on = {stat}, Channel = {self.channel}, Volume = {self.volume}'
