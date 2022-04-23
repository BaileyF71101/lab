class Television:
    """
    This class is for all functions for a television remote, and where the television will follow commands
    """

    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:

        """
        Constructor to create initial state of the television object, and to store private variables and their
        parameters throughout file

        :param self.__channel: the number associated with a particular television station
        :param self.__volume: the number associated with the level of noise coming from the television
        :param self.__status: the boolean value of 'on' or 'off', which describes if the television is powered
        """

        self.__channel: int = 0
        self.__volume: int = 0
        self.__status: str = 'Off'

    def power(self) -> None:

        """
        Method to activate/deactivate the television's power when called
        """

        if self.__status == 'On':
            self.__status = 'Off'
        else:
            self.__status = "On"

    def channel_up(self) -> None:

        """
        Method to increase the self.__channel variable by 1, or reset to minimum value if self.__channel is at
        maximum value when called
        """

        if self.__status == "On":
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:

        """
        Method to decrease the self.__channel variable by 1, or reset to maximum value if self.__channel is at
        minimum value when called
        """

        if self.__status == "On":
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:

        """
        Method to increase the self.__volume variable by 1, or remain at same level if self.__volume is
        already at maximum value when called
        """

        if self.__status == "On":
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:

        """
        Method to decrease the self.__volume variable by 1, or remain at same level if self.__volume is
        already at minimum value when called
        """

        if self.__status == "On":
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:

        """
        Method to give the values of the variables self.__status, self.__channel, and self.__volume, in that
        order

        :return: returns a string stating the current states of the variables self.__status,
        self.__channel, and self.__volume, in that order (regardless if input variables were type(str) or not
        prior to return)
        """

        stat = False
        if self.__status == "On":
            stat = True

        return f'TV Status: Is on = {stat}, Channel = {self.__channel}, Volume = {self.__volume}'
