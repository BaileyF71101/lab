import pytest
from classes import *

def setup_method(self):
    self.tv1 = Television()

# import unittest
# from classes import *
#
#
# class MyTestCase(unittest.TestCase):
#
#     def setUp(self):
#         self.pow = Television(self.__init__)
#         self.ch = Television(self.__init__)
#         self.vol = Television(self.__init__)
#
#     def tearDown(self):
#         del self.pow
#         del self.ch
#         del self.vol
#
#     def test_init(self):
#         self.assertEqual(self.__str__(), 'TV Status: Is on = False, Channel = 0, Volume = 0')
#
#      def test_power(self):
#          self.assertEqual(self.pow.power(), 'On', msg='Not True')
#
#      def test_channel_up(self):
#          self.assertEqual(self.ch.channel_up(), 1, msg='Did not increase channel correctly')
#
#     def test_channel_down(self):
#          self.assertEqual(self.vol.channel_down(), 2, msg='Did not decrease channel correctly')
#
#      def test_volume_up(self):
#          self.assertEqual(self.vol.volume_up(), 1, msg='Did not increase volume correctly')
#
#      def test_volume_down(self):
#          self.assertEqual(self.vol.volume_down(), 0, msg='Did not decrease volume correctly')
#
# if __name__ == '__main__':
#      unittest.main()
