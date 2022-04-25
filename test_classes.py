from classes import *


class Test:
    def setup_method(self):
        self.tvOffMin = Television(0, 0, False)
        self.tvOnMid = Television(1, 1, True)
        self.tvOnMax = Television(3, 2, True)
        self.tvOnMin = Television(0, 0, True)
        self.tvOffMid = Television(1, 1, False)

    def teardown_method(self):
        del self.tvOffMin
        del self.tvOnMid
        del self.tvOnMax
        del self.tvOnMin
        del self.tvOffMid

    def test_power(self):
        assert self.tvOffMin.power() is True
        assert self.tvOnMid.power() is False
        assert self.tvOnMax.power() is False
        assert self.tvOnMin.power() is False
        assert self.tvOffMid.power() is True

    def test_channel_up(self):
        assert self.tvOffMin.channel_up() == 0
        assert self.tvOnMid.channel_up() == 2
        assert self.tvOnMax.channel_up() == 0
        assert self.tvOnMin.channel_up() == 1
        assert self.tvOffMid.channel_up() == 1

    def test_channel_down(self):
        assert self.tvOffMin.channel_down() == 0
        assert self.tvOnMid.channel_down() == 0
        assert self.tvOnMax.channel_down() == 2
        assert self.tvOnMin.channel_down() == 3
        assert self.tvOffMid.channel_down() == 1

    def test_volume_up(self):
        assert self.tvOffMin.volume_up() == 0
        assert self.tvOnMid.volume_up() == 2
        assert self.tvOnMax.volume_up() == 2
        assert self.tvOnMin.volume_up() == 1
        assert self.tvOffMid.volume_up() == 1

    def test_volume_down(self):
        assert self.tvOffMin.volume_down() == 0
        assert self.tvOnMid.volume_down() == 0
        assert self.tvOnMax.volume_down() == 1
        assert self.tvOnMin.volume_down() == 0
        assert self.tvOffMid.volume_down() == 1

    def test_str(self):
        assert self.tvOffMin.__str__() == "TV Status: Is on = False, Channel = 0, Volume = 0"
        assert self.tvOnMid.__str__() == "TV Status: Is on = True, Channel = 1, Volume = 1"
        assert self.tvOnMax.__str__() == "TV Status: Is on = True, Channel = 3, Volume = 2"
        assert self.tvOnMin.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 0"
        assert self.tvOffMid.__str__() == "TV Status: Is on = False, Channel = 1, Volume = 1"

