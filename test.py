import xbmc
import xbmcgui
import xbmcaddon
import os
import datetime
import time
import _strptime
import threading
import urllib2
import urllib
import StringIO
import sqlite3
import string
import platform
import re
import move_right
import liveprogramming
from sqlite3 import dbapi2 as database
from xml.etree import ElementTree
from itertools import izip_longest
import xml.etree.ElementTree as ET
from UserDict import DictMixin

# two separate flags to kill the AllChannelsThread and the TimerThread
__killthread__ = False
FULL_CHANNELS_PAGE = range(0, 1000)
CHANNELS_PER_PAGE = 7
mode_EPG = 'EPG'
mode_TV = 'TV'


#get actioncodes from keyboard.xml
ACTION_MOVE_LEFT = 1
ACTION_MOVE_RIGHT = 2
ACTION_MOVE_UP = 3
ACTION_MOVE_DOWN = 4
ACTION_ENTER = 7
ACTION_PREVIOUS_MENU = 10
ACTION_BACKSPACE = 92
ACTION_NUMBER1 = 59
ACTION_NUMBER2 = 60
ACTION_NUMBER3 = 61
ACTION_NUMBER4 = 62
ACTION_NUMBER5 = 63
ACTION_NUMBER6 = 64
ACTION_NUMBER7 = 65
ACTION_NUMBER8 = 66
ACTION_NUMBER9 = 67
ACTION_NUMBER0 = 58

def cSetVisible(WiNdOw,iD,V=True): WiNdOw.getControl(iD).setVisible(V)
ADDON = xbmcaddon.Addon(id = 'script.tvguide')


class OrderedDict(dict, DictMixin):

     def __init__(self, *args, **kwds):
         if len(args) > 1:
             raise TypeError('expected at most 1 arguments, got %d' % len(args))
         try:
             self.__end
         except AttributeError:
             self.clear()
         self.update(*args, **kwds)

     def clear(self):
         self.__end = end = []
         end += [None, end, end]         # sentinel node for doubly linked list
         self.__map = {}                 # key --> [key, prev, next]
         dict.clear(self)

     def __setitem__(self, key, value):
         if key not in self:
             end = self.__end
             curr = end[1]
             curr[2] = end[1] = self.__map[key] = [key, curr, end]
         dict.__setitem__(self, key, value)

     def __delitem__(self, key):
         dict.__delitem__(self, key)
         key, prev, next = self.__map.pop(key)
         prev[2] = next
         next[1] = prev

     def __iter__(self):
         end = self.__end
         curr = end[2]
         while curr is not end:
             yield curr[0]
             curr = curr[2]

     def __reversed__(self):
         end = self.__end
         curr = end[1]
         while curr is not end:
             yield curr[0]
             curr = curr[1]

     def popitem(self, last=True):
         if not self:
             raise KeyError('dictionary is empty')
         if last:
             key = reversed(self).next()
         else:
             key = iter(self).next()
         value = self.pop(key)
         return key, value

     def __reduce__(self):
         items = [[k, self[k]] for k in self]
         tmp = self.__map, self.__end
         del self.__map, self.__end
         inst_dict = vars(self).copy()
         self.__map, self.__end = tmp
         if inst_dict:
             return (self.__class__, (items,), inst_dict)
         return self.__class__, (items,)

     def keys(self):
         return list(self)

     setdefault = DictMixin.setdefault
     update = DictMixin.update
     pop = DictMixin.pop
     values = DictMixin.values
     items = DictMixin.items
     iterkeys = DictMixin.iterkeys
     itervalues = DictMixin.itervalues
     iteritems = DictMixin.iteritems

     def __repr__(self):
         if not self:
             return '%s()' % (self.__class__.__name__,)
         return '%s(%r)' % (self.__class__.__name__, self.items())

     def copy(self):
         return self.__class__(self)

     @classmethod
     def fromkeys(cls, iterable, value=None):
         d = cls()
         for key in iterable:
             d[key] = value
         return d

     def __eq__(self, other):
         if isinstance(other, OrderedDict):
             if len(self) != len(other):
                 return False
             for p, q in  zip(self.items(), other.items()):
                 if p != q:
                     return False
             return True
         return dict.__eq__(self, other)

     def __ne__(self, other):
         return not self == other




class ProgramControls(object):
     def __init__(self, control, program):
         self.control = control
         self.program = program



class MyClass(xbmcgui.WindowXML):

     def __new__(cls):
         return super(MyClass, cls).__new__(cls, 'script-tvguide-mainmenu.xml', ADDON.getAddonInfo('path'))
         print "it is running the xml added no 1"



     def __init__(self):
         self.thread = None
         self.program_buttons = list()
         #self.program_labels = list()
         self.channels_Index = 0
         self.programs_Index = 0
         self.button_focus = 'programs_yellow.png'
         self.button_nofocus = 'channels_bar1.png'
         self.path = 'special://home/addons/script.tvguide/resources/skins/Default/media/'
         self.initialized = False
         self.strmFile = None
         self.move_up_flag = False
         self.move_down_flag = False
         self.move_left_flag = False
         self.move_right_flag = False
         self.move_flag = False
         self.move_back_flag = False
         self.programs_Index_flag = False
         self.current_program_flag = False
         self.time_flag = False
         self.move_program_flag = False
         self.next_program = False
         self.previous_program = False
         self.lastchannels = False
         self.channelsOnLeft = False
         self.channelsOnMiddle = False
         self.channelsOnRight = False
         self.program_remaining = False
         self.select_db_flag = False
         self.single_program = False
         self.program_index_flags = True
         self.program_id = list()
         self.prog_id_list = list()
         self.channel = list()
         self.program_end_time = list()
         self.program_finished = list()
         self.nextprogram_id = list()
         self.nextprogram_clock = list()
         self.nextprogram_stop_clock = list()
         self.nextprogram1_id = list()
         self.nextprogram1_clock = list()
         self.remove_controls = list()
         self.program = list()
         self.epg_time_1 = list()
         self.epg_time_2 = list()
         self.epg_time_3 = list()
         self.program_stop_time = list()
         self.program_stop_minutes = 0
         self.channel_page = 0
         self.program_index = 0
         self.get_button_id = 0
         self.channelspress = 0
         self.program_day = 0
         self.today_date = time.strftime("%d")
         self.today_month = time.strftime("%m")
         self.today_year = time.strftime("%Y")
         self.streamList = list()
         #self.ChannelCheckList = list()
         self.mode = mode_EPG
         self.player = xbmc.Player()
         self.full_screen = False




     def onInit(self):
         if self.initialized:
             return
         self.initialized = True

         if self.full_screen == False:
             if not self.player.isPlaying():
                 self.getControl(3).setAnimations([('fade', 'effect=fade start=0 end=100 time=1500')])
                 self.getControl(5).setAnimations([('fade', 'effect=fade start=0 end=100 time=1500')])
                 self.getControl(7).setAnimations([('fade', 'effect=fade start=0 end=100 time=1500')])
                 self.getControl(9).setAnimations([('fade', 'effect=fade start=0 end=100 time=1500')])
                 self.getControl(4).setVisible(False)
                 self.getControl(6).setVisible(False)
                 self.getControl(8).setVisible(False)
                 self.getControl(10).setVisible(False)
                 cSetVisible(self,11,True)
                 allchannels_yellow_BOX = self.getControl(11)
                 allchannels_yellow_BOX.setImage(self.path + "channels_yellow.png")
                 cSetVisible(self,10,False)
                 allchannels_blue_BOX = self.getControl(10)
                 allchannels_blue_BOX.setImage(self.path + "channels_blue.png")
                 cSetVisible(self,12,False)
                 entertainment_yellow_BOX = self.getControl(12)
                 entertainment_yellow_BOX.setImage(self.path + "channels_yellow.png")
                 cSetVisible(self,13,True)
                 entertainment_blue_BOX = self.getControl(13)
                 entertainment_blue_BOX.setImage(self.path + "channels_blue.png")
                 cSetVisible(self,14,False)
                 movies_yellow_BOX = self.getControl(14)
                 movies_yellow_BOX.setImage(self.path + "channels_yellow.png")
                 cSetVisible(self,15,True)
                 movies_blue_BOX = self.getControl(15)
                 movies_blue_BOX.setImage(self.path + "channels_blue.png")
                 cSetVisible(self,16,False)
                 kids_yellow_BOX = self.getControl(16)
                 kids_yellow_BOX.setImage(self.path + "channels_yellow.png")
                 cSetVisible(self,17,True)
                 kids_blue_BOX = self.getControl(17)
                 kids_blue_BOX.setImage(self.path + "channels_blue.png")
                 cSetVisible(self,18,False)
                 sports_yellow_BOX = self.getControl(18)
                 sports_yellow_BOX.setImage(self.path + "channels_yellow.png")
                 cSetVisible(self,19,True)
                 sports_blue_BOX = self.getControl(19)
                 sports_blue_BOX.setImage(self.path + "channels_blue.png")
                 cSetVisible(self,20,False)
                 news_yellow_BOX = self.getControl(20)
                 news_yellow_BOX.setImage(self.path + "channels_yellow.png")
                 cSetVisible(self,21,True)
                 news_blue_BOX = self.getControl(21)
                 news_blue_BOX.setImage(self.path + "channels_blue.png")
                 cSetVisible(self,22,False)
                 documentaries_yellow_BOX = self.getControl(22)
                 documentaries_yellow_BOX.setImage(self.path + "channels_yellow.png")
                 cSetVisible(self,23,True)
                 documentaries_blue_BOX = self.getControl(23)
                 documentaries_blue_BOX.setImage(self.path + "channels_blue.png")
                 cSetVisible(self,24,False)
                 musicradio_yellow_BOX = self.getControl(24)
                 musicradio_yellow_BOX.setImage(self.path + "channels_yellow.png")
                 cSetVisible(self,25,True)
                 musicradio_blue_BOX = self.getControl(25)
                 musicradio_blue_BOX.setImage(self.path + "channels_blue.png")
                 cSetVisible(self,26,False)
                 adult_yellow_BOX = self.getControl(26)
                 adult_yellow_BOX.setImage(self.path + "channels_yellow.png")
                 cSetVisible(self,27,True)
                 adult_blue_BOX = self.getControl(27)
                 adult_blue_BOX.setImage(self.path + "channels_blue.png")
                 cSetVisible(self,28,False)
                 favourites_yellow_BOX = self.getControl(28)
                 favourites_yellow_BOX.setImage(self.path + "channels_yellow.png")
                 cSetVisible(self,29,True)
                 favourites_blue_BOX = self.getControl(29)
                 favourites_blue_BOX.setImage(self.path + "channels_blue.png")
                 cSetVisible(self,30,False)
                 picture_yellow_BOX = self.getControl(30)
                 picture_yellow_BOX.setImage(self.path + "allsettings_yellow.png")
                 cSetVisible(self,31,False)
                 picture_blue_BOX = self.getControl(31)
                 picture_blue_BOX.setImage(self.path + "allsettings_blue.png")
                 cSetVisible(self,32,False)
                 sound_yellow_BOX = self.getControl(32)
                 sound_yellow_BOX.setImage(self.path + "allsettings_yellow.png")
                 cSetVisible(self,33,False)
                 sound_blue_BOX = self.getControl(33)
                 sound_blue_BOX.setImage(self.path + "allsettings_blue.png")
                 cSetVisible(self,34,False)
                 changelanguage_yellow_BOX = self.getControl(34)
                 changelanguage_yellow_BOX.setImage(self.path + "allsettings_yellow.png")
                 cSetVisible(self,35,False)
                 changelanguage_blue_BOX = self.getControl(35)
                 changelanguage_blue_BOX.setImage(self.path + "allsettings_blue.png")
                 cSetVisible(self,36,False)
                 changepin_yellow_BOX = self.getControl(36)
                 changepin_yellow_BOX.setImage(self.path + "allsettings_yellow.png")
                 cSetVisible(self,37,False)
                 changepin_blue_BOX = self.getControl(37)
                 changepin_blue_BOX.setImage(self.path + "allsettings_blue.png")
                 cSetVisible(self,38,False)
                 viewrestrictions_yellow_BOX = self.getControl(38)
                 viewrestrictions_yellow_BOX.setImage(self.path + "allsettings_yellow.png")
                 cSetVisible(self,39,False)
                 viewrestrictions_blue_BOX = self.getControl(39)
                 viewrestrictions_blue_BOX.setImage(self.path + "allsettings_blue.png")
                 cSetVisible(self,40,False)
                 removechannels_yellow_BOX = self.getControl(40)
                 removechannels_yellow_BOX.setImage(self.path + "allsettings_yellow.png")
                 cSetVisible(self,41,False)
                 removechannels_blue_BOX = self.getControl(41)
                 removechannels_blue_BOX.setImage(self.path + "allsettings_blue.png")
                 cSetVisible(self,42,False)
                 systemdetails_yellow_BOX = self.getControl(42)
                 systemdetails_yellow_BOX.setImage(self.path + "allsettings_yellow.png")
                 cSetVisible(self,43,False)
                 systemdetails_blue_BOX = self.getControl(43)
                 systemdetails_blue_BOX.setImage(self.path + "allsettings_blue.png")
                 cSetVisible(self,44,False)
                 speedtest_yellow_BOX = self.getControl(44)
                 speedtest_yellow_BOX.setImage(self.path + "allsettings_yellow.png")
                 cSetVisible(self,45,False)
                 speedtest_blue_BOX = self.getControl(45)
                 speedtest_blue_BOX.setImage(self.path + "allsettings_blue.png")
                 cSetVisible(self,101,False)
                 picture_setting_yellow = self.getControl(101)
                 picture_setting_yellow.setImage(self.path + "yellow_settings_button.png")
                 cSetVisible(self,102,False)
                 picture_setting_blue = self.getControl(102)
                 picture_setting_blue.setImage(self.path + "blue_settings_button.png")
                 cSetVisible(self,105,False)
                 picture_setting_on_yellow = self.getControl(105)
                 picture_setting_on_yellow.setImage(self.path + "yellow_settings_button.png")
                 cSetVisible(self,106,False)
                 picture_setting_on_blue = self.getControl(106)
                 picture_setting_on_blue.setImage(self.path + "blue_settings_button.png")
                 self.getControl(107).setVisible(False)
                 changepicture_left_black = self.getControl(107)
                 changepicture_left_black.setImage(self.path + "left_button_black.png")
                 self.getControl(108).setVisible(False)
                 changepicture_left_white = self.getControl(108)
                 changepicture_left_white.setImage(self.path + "left_button_white.png")
                 self.getControl(109).setVisible(False)
                 changepicture_right_black = self.getControl(109)
                 changepicture_right_black.setImage(self.path + "right_button_black.png")
                 self.getControl(110).setVisible(False)
                 changepicture_right_white = self.getControl(110)
                 changepicture_right_white.setImage(self.path + "right_button_white.png")
                 self.getControl(121).setVisible(False)
                 display_picture_yellow = self.getControl(121)
                 display_picture_yellow.setImage(self.path + "yellow_settings_button.png")
                 self.getControl(122).setVisible(False)
                 display_picture_blue = self.getControl(122)
                 display_picture_blue.setImage(self.path + "blue_settings_button.png")
                 self.getControl(125).setVisible(False)
                 display_picture_on_yellow = self.getControl(125)
                 display_picture_on_yellow.setImage(self.path + "yellow_settings_button.png")
                 cSetVisible(self,126,False)
                 display_picture_on_blue = self.getControl(126)
                 display_picture_on_blue.setImage(self.path + "blue_settings_button.png")
                 self.getControl(131).setVisible(False)
                 displaypicture_left_black = self.getControl(131)
                 displaypicture_left_black.setImage(self.path + "left_button_black.png")
                 self.getControl(132).setVisible(False)
                 displaypicture_left_white = self.getControl(132)
                 displaypicture_left_white.setImage(self.path + "left_button_white.png")
                 self.getControl(133).setVisible(False)
                 displaypicture_right_black = self.getControl(133)
                 displaypicture_right_black.setImage(self.path + "right_button_black.png")
                 self.getControl(134).setVisible(False)
                 displaypicture_right_white = self.getControl(134)
                 displaypicture_right_white.setImage(self.path + "right_button_white.png")
                 self.getControl(135).setVisible(False)
                 video_output_yellow = self.getControl(135)
                 video_output_yellow.setImage(self.path + "yellow_settings_button.png")
                 self.getControl(136).setVisible(False)
                 video_output_blue = self.getControl(136)
                 video_output_blue.setImage(self.path + "blue_settings_button.png")
                 self.getControl(140).setVisible(False)
                 video_output_on = self.getControl(140)
                 video_output_on.setImage(self.path + "blue_settings_button.png")
                 self.getControl(145).setVisible(False)
                 video_output_on_left_black = self.getControl(145)
                 video_output_on_left_black.setImage(self.path + "left_button_black.png")
                 self.getControl(146).setVisible(False)
                 video_output_on_left_white = self.getControl(146)
                 video_output_on_left_white.setImage(self.path + "left_button_white.png")
                 self.getControl(147).setVisible(False)
                 video_output_on_right_black = self.getControl(147)
                 video_output_on_right_black.setImage(self.path + "right_button_black.png")
                 self.getControl(148).setVisible(False)
                 video_output_on_right_black = self.getControl(148)
                 video_output_on_right_black.setImage(self.path + "right_button_white.png")
                 self.getControl(149).setVisible(False)
                 On_Screen_channels_yellow = self.getControl(149)
                 On_Screen_channels_yellow.setImage(self.path + "yellow_settings_button.png")
                 self.getControl(150).setVisible(False)
                 On_Screen_channels_blue = self.getControl(150)
                 On_Screen_channels_blue.setImage(self.path + "blue_settings_button.png")
                 self.getControl(154).setVisible(False)
                 On_Screen_channels_on = self.getControl(154)
                 On_Screen_channels_on.setImage(self.path + "blue_settings_button.png")
                 self.getControl(159).setVisible(False)
                 On_Screen_channels_on_left_black = self.getControl(159)
                 On_Screen_channels_on_left_black.setImage(self.path + "left_button_black.png")
                 self.getControl(160).setVisible(False)
                 On_Screen_channels_on_left_white = self.getControl(160)
                 On_Screen_channels_on_left_white.setImage(self.path + "left_button_white.png")
                 self.getControl(161).setVisible(False)
                 On_Screen_channels_on_right_black = self.getControl(161)
                 On_Screen_channels_on_right_black.setImage(self.path + "right_button_black.png")
                 self.getControl(162).setVisible(False)
                 On_Screen_channels_on_right_black = self.getControl(162)
                 On_Screen_channels_on_right_black.setImage(self.path + "right_button_white.png")
                 self.getControl(163).setVisible(False)
                 On_Screen_alert_yellow = self.getControl(163)
                 On_Screen_alert_yellow.setImage(self.path + "yellow_settings_button.png")
                 self.getControl(164).setVisible(False)
                 On_Screen_alert_blue = self.getControl(164)
                 On_Screen_alert_blue.setImage(self.path + "blue_settings_button.png")
                 self.getControl(168).setVisible(False)
                 On_Screen_alert_on = self.getControl(168)
                 On_Screen_alert_on.setImage(self.path + "blue_settings_button.png")
                 self.getControl(173).setVisible(False)
                 On_Screen_alert_on_left_black = self.getControl(173)
                 On_Screen_alert_on_left_black.setImage(self.path + "left_button_black.png")
                 self.getControl(174).setVisible(False)
                 On_Screen_alert_on_left_white = self.getControl(174)
                 On_Screen_alert_on_left_white.setImage(self.path + "left_button_white.png")
                 self.getControl(175).setVisible(False)
                 On_Screen_alert_on_right_black = self.getControl(175)
                 On_Screen_alert_on_right_black.setImage(self.path + "right_button_black.png")
                 self.getControl(176).setVisible(False)
                 On_Screen_alert_on_right_black = self.getControl(176)
                 On_Screen_alert_on_right_black.setImage(self.path + "right_button_white.png")
                 self.getControl(177).setVisible(False)
                 Show_Subtitle_yellow = self.getControl(177)
                 Show_Subtitle_yellow.setImage(self.path + "yellow_settings_button.png")
                 self.getControl(178).setVisible(False)
                 Show_Subtitle_blue = self.getControl(178)
                 Show_Subtitle_blue.setImage(self.path + "blue_settings_button.png")
                 self.getControl(182).setVisible(False)
                 Show_Subtitle_on = self.getControl(182)
                 Show_Subtitle_on.setImage(self.path + "blue_settings_button.png")
                 self.getControl(187).setVisible(False)
                 Show_Subtitle_on_left_black = self.getControl(187)
                 Show_Subtitle_on_left_black.setImage(self.path + "left_button_black.png")
                 self.getControl(188).setVisible(False)
                 Show_Subtitle_on_left_white = self.getControl(188)
                 Show_Subtitle_on_left_white.setImage(self.path + "left_button_white.png")
                 self.getControl(189).setVisible(False)
                 Show_Subtitle_on_right_black = self.getControl(189)
                 Show_Subtitle_on_right_black.setImage(self.path + "right_button_black.png")
                 self.getControl(190).setVisible(False)
                 Show_Subtitle_on_right_black = self.getControl(190)
                 Show_Subtitle_on_right_black.setImage(self.path + "right_button_white.png")
                 self.getControl(192).setVisible(False)
                 Save_settings = self.getControl(192)
                 Save_settings.setImage(self.path + "blue_settings_button.png")
                 self.getControl(198).setVisible(False)
                 reset_button_red = self.getControl(198)
                 reset_button_red.setImage(self.path + "reset_button_red.png")
                 self.getControl(199).setVisible(False)
                 left_right_button_settings = self.getControl(199)
                 left_right_button_settings.setImage(self.path + "left_right_button_settings.png")
                 self.getControl(201).setVisible(False)
                 Sound_Audio_yellow = self.getControl(201)
                 Sound_Audio_yellow.setImage(self.path + "yellow_settings_button.png")
                 self.getControl(202).setVisible(False)
                 Sound_Audio_blue = self.getControl(202)
                 Sound_Audio_blue.setImage(self.path + "blue_settings_button.png")
                 self.getControl(205).setVisible(False)
                 Sound_Audio_on_yellow = self.getControl(205)
                 Sound_Audio_on_yellow.setImage(self.path + "yellow_settings_button.png")
                 self.getControl(207).setVisible(False)
                 Sound_Audio_on_left_black = self.getControl(207)
                 Sound_Audio_on_left_black.setImage(self.path + "left_button_black.png")
                 self.getControl(208).setVisible(False)
                 Sound_Audio_on_left_white = self.getControl(208)
                 Sound_Audio_on_left_white.setImage(self.path + "left_button_white.png")
                 self.getControl(209).setVisible(False)
                 Sound_Audio_on_left_black = self.getControl(209)
                 Sound_Audio_on_left_black.setImage(self.path + "right_button_black.png")
                 self.getControl(210).setVisible(False)
                 Sound_Audio_on_left_black = self.getControl(210)
                 Sound_Audio_on_left_black.setImage(self.path + "right_button_white.png")
                 self.getControl(218).setVisible(False)
                 Volume_Level_Blue = self.getControl(218)
                 Volume_Level_Blue.setImage(self.path + "blue_settings_button.png")
                 self.getControl(222).setVisible(False)
                 Volume_Level_On_Blue = self.getControl(222)
                 Volume_Level_On_Blue.setImage(self.path + "blue_settings_button.png")
                 self.getControl(227).setVisible(False)
                 Volume_Level_on_left_white = self.getControl(227)
                 Volume_Level_on_left_white.setImage(self.path + "left_button_black.png")
                 self.getControl(228).setVisible(False)
                 Volume_Level_on_left_black = self.getControl(228)
                 Volume_Level_on_left_black.setImage(self.path + "left_button_white.png")
                 self.getControl(229).setVisible(False)
                 Volume_Level_on_right_black = self.getControl(229)
                 Volume_Level_on_right_black.setImage(self.path + "right_button_black.png")
                 self.getControl(230).setVisible(False)
                 Volume_Level_on_right_white = self.getControl(230)
                 Volume_Level_on_right_white.setImage(self.path + "right_button_white.png")
                 self.getControl(356).setVisible(False)
                 Audio_output_blue = self.getControl(356)
                 Audio_output_blue.setImage(self.path + "blue_settings_button.png")
                 self.getControl(360).setVisible(False)
                 Audio_output_on_blue = self.getControl(360)
                 Audio_output_on_blue.setImage(self.path + "blue_settings_button.png")
                 self.getControl(241).setVisible(False)
                 Audio_output_on_left_black = self.getControl(241)
                 Audio_output_on_left_black.setImage(self.path + "left_button_black.png")
                 self.getControl(242).setVisible(False)
                 Audio_output_on_left_white = self.getControl(242)
                 Audio_output_on_left_white.setImage(self.path + "left_button_white.png")
                 self.getControl(243).setVisible(False)
                 Audio_output_on_right_black = self.getControl(243)
                 Audio_output_on_right_black.setImage(self.path + "right_button_black.png")
                 self.getControl(244).setVisible(False)
                 Audio_output_on_right_white = self.getControl(244)
                 Audio_output_on_right_white.setImage(self.path + "right_button_white.png")
                 self.getControl(246).setVisible(False)
                 background_music_blue = self.getControl(246)
                 background_music_blue.setImage(self.path + "blue_settings_button.png")
                 self.getControl(250).setVisible(False)
                 background_music_on_blue = self.getControl(250)
                 background_music_on_blue.setImage(self.path + "blue_settings_button.png")
                 self.getControl(255).setVisible(False)
                 background_music_on_left_black = self.getControl(255)
                 background_music_on_left_black.setImage(self.path + "left_button_black.png")
                 self.getControl(256).setVisible(False)
                 background_music_on_left_white = self.getControl(256)
                 background_music_on_left_white.setImage(self.path + "left_button_white.png")
                 self.getControl(257).setVisible(False)
                 background_music_on_right_black = self.getControl(257)
                 background_music_on_right_black.setImage(self.path + "right_button_black.png")
                 self.getControl(258).setVisible(False)
                 background_music_on_right_white = self.getControl(258)
                 background_music_on_right_white.setImage(self.path + "right_button_white.png")
                 self.getControl(260).setVisible(False)
                 beep_error_blue = self.getControl(260)
                 beep_error_blue.setImage(self.path + "blue_settings_button.png")
                 self.getControl(264).setVisible(False)
                 beep_error_on_blue = self.getControl(264)
                 beep_error_on_blue.setImage(self.path + "blue_settings_button.png")
                 self.getControl(269).setVisible(False)
                 beep_error_on_left_black = self.getControl(269)
                 beep_error_on_left_black.setImage(self.path + "left_button_black.png")
                 self.getControl(270).setVisible(False)
                 beep_error_on_left_white = self.getControl(270)
                 beep_error_on_left_white.setImage(self.path + "left_button_white.png")
                 self.getControl(271).setVisible(False)
                 beep_error_on_right_black = self.getControl(271)
                 beep_error_on_right_black.setImage(self.path + "right_button_black.png")
                 self.getControl(272).setVisible(False)
                 beep_error_on_right_black = self.getControl(272)
                 beep_error_on_right_black.setImage(self.path + "right_button_white.png")
                 self.getControl(273).setVisible(False)
                 sound_settings_yellow = self.getControl(273)
                 sound_settings_yellow.setImage(self.path + "yellow_settings_button.png")
                 self.getControl(274).setVisible(False)
                 sound_settings_blue = self.getControl(274)
                 sound_settings_blue.setImage(self.path + "blue_settings_button.png")
                 self.getControl(280).setVisible(False)
                 sound_reset_button_red = self.getControl(280)
                 sound_reset_button_red.setImage(self.path + "reset_button_red.png")
                 self.getControl(281).setVisible(False)
                 left_right_button_sound = self.getControl(281)
                 left_right_button_sound.setImage(self.path + "left_right_button_settings.png")
                 cSetVisible(self,283,False)
                 changelanguage_yellow_BOX = self.getControl(283)
                 changelanguage_yellow_BOX.setImage(self.path + "changelang_yellow.png")
                 cSetVisible(self,284,False)
                 changelanguage_blue_BOX = self.getControl(284)
                 changelanguage_blue_BOX.setImage(self.path + "changelang_blue.png")
                 self.getControl(287).setVisible(False)
                 chang_language_yellow = self.getControl(287)
                 chang_language_yellow.setImage(self.path + "changelang_yellow.png")
                 self.getControl(288).setVisible(False)
                 chang_language_yellow = self.getControl(288)
                 chang_language_yellow.setImage(self.path + "changelang_blue.png")
                 self.getControl(289).setVisible(False)
                 left_arrow_lang_black = self.getControl(289)
                 left_arrow_lang_black.setImage(self.path + "left_button_black.png")
                 self.getControl(290).setVisible(False)
                 left_arrow_lang_white = self.getControl(290)
                 left_arrow_lang_white.setImage(self.path + "left_button_white.png")
                 self.getControl(291).setVisible(False)
                 right_arrow_lang_black = self.getControl(291)
                 right_arrow_lang_black.setImage(self.path + "right_button_black.png")
                 self.getControl(292).setVisible(False)
                 right_arrow_lang_white = self.getControl(292)
                 right_arrow_lang_white.setImage(self.path + "right_button_white.png")
                 self.getControl(317).setVisible(False)
                 savesettings_yellow_BOX = self.getControl(317)
                 savesettings_yellow_BOX.setImage(self.path + "savesettings_yellow.png")
                 self.getControl(318).setVisible(False)
                 savesettings_blue_BOX = self.getControl(318)
                 savesettings_blue_BOX.setImage(self.path + "savesettings_blue.png")
                 cSetVisible(self,321,False)
                 self.getControl(321).setLabel('$INFO[System.Date(ddd dd mmm)]'  + ' ' + time.strftime("%I").lstrip('0') + time.strftime(":%M%p"))
                 cSetVisible(self,323,False)
                 enterpin_yellow = self.getControl(323)
                 enterpin_yellow.setImage(self.path + "enterpin_yellow.png")
                 cSetVisible(self,324,False)
                 enterpin_blue = self.getControl(324)
                 enterpin_blue.setImage(self.path + "enterpin_blue1.png")
                 cSetVisible(self,325,False)
                 enterpin_bottom_blue = self.getControl(325)
                 enterpin_bottom_blue.setImage(self.path + "enterpin_blue1.png")
                 cSetVisible(self,329,False)
                 pin_press_back = self.getControl(329)
                 pin_press_back.setImage(self.path + "pressback3.png")
                 cSetVisible(self,332,False)
                 enterpin_blank_1 = self.getControl(332)
                 enterpin_blank_1.setImage(self.path + "pin_numb1.png")
                 cSetVisible(self,333,False)
                 enterpin_blank_2 = self.getControl(333)
                 enterpin_blank_2.setImage(self.path + "pin_numb2.png")
                 cSetVisible(self,334,False)
                 enterpin_blank_3 = self.getControl(334)
                 enterpin_blank_3.setImage(self.path + "pin_numb3.png")
                 cSetVisible(self,335,False)
                 enterpin_blank_4 = self.getControl(335)
                 enterpin_blank_4.setImage(self.path + "pin_numb4.png")
                 cSetVisible(self,336,False)
                 enterpin_chars_1 = self.getControl(336)
                 enterpin_chars_1.setImage(self.path + "pin_1.png")
                 cSetVisible(self,337,False)
                 enterpin_chars_2 = self.getControl(337)
                 enterpin_chars_2.setImage(self.path + "pin_2.png")
                 cSetVisible(self,338,False)
                 enterpin_chars_3 = self.getControl(338)
                 enterpin_chars_3.setImage(self.path + "pin_3.png")
                 cSetVisible(self,339,False)
                 enterpin_chars_4 = self.getControl(339)
                 enterpin_chars_4.setImage(self.path + "pin_4.png")
                 cSetVisible(self,340,False)
                 loading_gif = self.getControl(340)
                 loading_gif.setImage(self.path + "tvguide-loading.gif")
                 cSetVisible(self,347,False)
                 channel_1_yellow = self.getControl(347)
                 channel_1_yellow.setImage(self.path + "changelang_yellow.png")
                 cSetVisible(self,354,False)
                 channel_1_blue = self.getControl(354)
                 channel_1_blue.setImage(self.path + "channels_bar1.png")
                 cSetVisible(self,348,False)
                 channel_2_blue = self.getControl(348)
                 channel_2_blue.setImage(self.path + "channels_bar1.png")
                 cSetVisible(self,355,False)
                 channel_2_yellow = self.getControl(355)
                 channel_2_yellow.setImage(self.path + "changelang_yellow.png")
                 cSetVisible(self,349,False)
                 channel_3_blue = self.getControl(349)
                 channel_3_blue.setImage(self.path + "channels_bar1.png")
                 cSetVisible(self,356,False)
                 channel_3_yellow = self.getControl(356)
                 channel_3_yellow.setImage(self.path + "changelang_yellow.png")
                 cSetVisible(self,350,False)
                 channel_4_blue = self.getControl(350)
                 channel_4_blue.setImage(self.path + "channels_bar1.png")
                 cSetVisible(self,357,False)
                 channel_4_yellow = self.getControl(357)
                 channel_4_yellow.setImage(self.path + "changelang_yellow.png")
                 cSetVisible(self,351,False)
                 channel_5_blue = self.getControl(351)
                 channel_5_blue.setImage(self.path + "channels_bar1.png")
                 cSetVisible(self,358,False)
                 channel_5_yellow = self.getControl(358)
                 channel_5_yellow.setImage(self.path + "changelang_yellow.png")
                 cSetVisible(self,352,False)
                 channel_6_blue = self.getControl(352)
                 channel_6_blue.setImage(self.path + "channels_bar1.png")
                 cSetVisible(self,359,False)
                 channel_6_yellow = self.getControl(359)
                 channel_6_yellow.setImage(self.path + "changelang_yellow.png")
                 cSetVisible(self,353,False)
                 channel_7_blue = self.getControl(353)
                 channel_7_blue.setImage(self.path + "channels_bar1.png")
                 cSetVisible(self,360,False)
                 channel_7_yellow = self.getControl(360)
                 channel_7_yellow.setImage(self.path + "changelang_yellow.png")
                 cSetVisible(self,341,False)
                 tvguide_time_bar = self.getControl(341)
                 tvguide_time_bar.setImage(self.path + "channels_bar1.png")
                 cSetVisible(self,375,False)
                 buttons_bar = self.getControl(375)
                 buttons_bar.setImage(self.path + "channels_bar1.png")
                 cSetVisible(self,376,False)
                 epg_red_button = self.getControl(376)
                 epg_red_button.setImage(self.path + "red_button.png")
                 cSetVisible(self,377,False)
                 epg_green_button = self.getControl(377)
                 epg_green_button.setImage(self.path + "green_button.png")
                 cSetVisible(self,378,False)
                 epg_yellow_button = self.getControl(378)
                 epg_yellow_button.setImage(self.path + "yellow_button.png")
                 cSetVisible(self,379,False)
                 epg_blue_button = self.getControl(379)
                 epg_blue_button.setImage(self.path + "blue_button.png")
                 cSetVisible(self,384,False)
                 epg_select_button = self.getControl(384)
                 epg_select_button.setImage(self.path + "select_button.png")
                 cSetVisible(self,385,False)
                 epg_record_button = self.getControl(385)
                 epg_record_button.setImage(self.path + "record_button.png")
                 cSetVisible(self,386,False)
                 epg_back_button = self.getControl(386)
                 epg_back_button.setImage(self.path + "back_button.png")
                 cSetVisible(self,388,False)
                 epg_back_button = self.getControl(388)
                 epg_back_button.setImage(self.path + "tv_blackscreen.png")
                 ADDON = xbmcaddon.Addon(id = 'script.tvguide')
                 english_enabled = ADDON.getSetting('english.enabled') == 'true'
                 french_enabled = ADDON.getSetting('french.enabled') == 'true'
                 self.getString = ADDON.getLocalizedString
                 self.getControl(46).setVisible(False)
                 self.getControl(46).setLabel(self.getString(30001))
                 self.getControl(47).setVisible(False)
                 self.getControl(47).setLabel(self.getString(30001))
                 self.getControl(48).setVisible(False)
                 self.getControl(48).setLabel(self.getString(30002))
                 self.getControl(49).setVisible(False)
                 self.getControl(49).setLabel(self.getString(30002))
                 self.getControl(50).setVisible(False)
                 self.getControl(50).setLabel(self.getString(30003))
                 self.getControl(51).setVisible(False)
                 self.getControl(51).setLabel(self.getString(30003))
                 self.getControl(52).setVisible(False)
                 self.getControl(52).setLabel(self.getString(30004))
                 self.getControl(53).setVisible(False)
                 self.getControl(53).setLabel(self.getString(30004))
                 self.getControl(54).setLabel(self.getString(30005))
                 self.getControl(55).setVisible(False)
                 self.getControl(55).setLabel(self.getString(30005))
                 self.getControl(56).setVisible(False)
                 self.getControl(56).setLabel(self.getString(30006))
                 self.getControl(57).setVisible(False)
                 self.getControl(57).setLabel(self.getString(30006))
                 self.getControl(58).setVisible(False)
                 self.getControl(58).setLabel(self.getString(30007))
                 self.getControl(59).setVisible(False)
                 self.getControl(59).setLabel(self.getString(30007))
                 self.getControl(60).setVisible(False)
                 self.getControl(60).setLabel(self.getString(30008))
                 self.getControl(61).setVisible(False)
                 self.getControl(61).setLabel(self.getString(30008))
                 self.getControl(62).setVisible(False)
                 self.getControl(62).setLabel(self.getString(30009))
                 self.getControl(63).setVisible(False)
                 self.getControl(63).setLabel(self.getString(30009))
                 self.getControl(64).setVisible(False)
                 self.getControl(64).setLabel(self.getString(30010))
                 self.getControl(65).setVisible(False)
                 self.getControl(65).setLabel(self.getString(30010))
                 self.getControl(66).setVisible(False)
                 self.getControl(66).setLabel(self.getString(30011))
                 self.getControl(67).setVisible(False)
                 self.getControl(67).setLabel(self.getString(30011))
                 self.getControl(68).setVisible(False)
                 self.getControl(68).setLabel(self.getString(30012))
                 self.getControl(69).setVisible(False)
                 self.getControl(69).setLabel(self.getString(30012))
                 self.getControl(70).setVisible(False)
                 self.getControl(70).setLabel(self.getString(30013))
                 self.getControl(71).setVisible(False)
                 self.getControl(71).setLabel(self.getString(30013))
                 self.getControl(72).setVisible(False)
                 self.getControl(72).setLabel(self.getString(30014))
                 self.getControl(73).setVisible(False)
                 self.getControl(73).setLabel(self.getString(30014))
                 self.getControl(74).setVisible(False)
                 self.getControl(74).setLabel(self.getString(30015))
                 self.getControl(75).setVisible(False)
                 self.getControl(75).setLabel(self.getString(30015))
                 self.getControl(76).setVisible(False)
                 self.getControl(76).setLabel(self.getString(30016))
                 self.getControl(77).setVisible(False)
                 self.getControl(77).setLabel(self.getString(30016))
                 self.getControl(78).setVisible(False)
                 self.getControl(78).setLabel(self.getString(30017))
                 self.getControl(79).setVisible(False)
                 self.getControl(79).setLabel(self.getString(30017))
                 self.getControl(80).setVisible(False)
                 self.getControl(80).setLabel(self.getString(30018))
                 self.getControl(81).setVisible(False)
                 self.getControl(81).setLabel(self.getString(30018))
                 self.getControl(82).setVisible(False)
                 self.getControl(82).setLabel(self.getString(30019))
                 self.getControl(83).setVisible(False)
                 self.getControl(83).setLabel(self.getString(30019))
                 self.getControl(84).setVisible(False)
                 self.getControl(84).setLabel(self.getString(30020))
                 self.getControl(85).setVisible(False)
                 self.getControl(85).setLabel(self.getString(30020))
                 self.getControl(86).setVisible(False)
                 self.getControl(86).setLabel(self.getString(30021))
                 self.getControl(87).setVisible(False)
                 self.getControl(87).setLabel(self.getString(30021))
                 self.getControl(88).setVisible(False)
                 self.getControl(88).setLabel(self.getString(30022))
                 self.getControl(89).setVisible(False)
                 self.getControl(89).setLabel(self.getString(30022))
                 self.getControl(90).setVisible(False)
                 self.getControl(90).setLabel(self.getString(30023))
                 self.getControl(91).setVisible(False)
                 self.getControl(91).setLabel(self.getString(30024))
                 self.getControl(92).setVisible(False)
                 self.getControl(92).setLabel(self.getString(30025))
                 self.getControl(93).setVisible(False)
                 self.getControl(93).setLabel(self.getString(30026))
                 self.getControl(94).setVisible(False)
                 self.getControl(94).setLabel(self.getString(30027))
                 self.getControl(95).setVisible(False)
                 self.getControl(95).setLabel(self.getString(30028))
                 self.getControl(96).setVisible(False)
                 self.getControl(96).setLabel(self.getString(30029))
                 self.getControl(97).setVisible(False)
                 self.getControl(97).setLabel(self.getString(30030))
                 self.getControl(98).setVisible(False)
                 self.getControl(98).setLabel(self.getString(30031))
                 self.getControl(99).setVisible(False)
                 self.getControl(99).setLabel(self.getString(30032))
                 self.getControl(100).setVisible(False)
                 self.getControl(100).setLabel(self.getString(30035))
                 self.getControl(103).setVisible(False)
                 self.getControl(103).setLabel(self.getString(30036))
                 self.getControl(104).setVisible(False)
                 self.getControl(104).setLabel(self.getString(30036))
                 self.getControl(111).setVisible(False)
                 self.getControl(111).setLabel(self.getString(30037))
                 self.getControl(112).setVisible(False)
                 self.getControl(112).setLabel(self.getString(30037))
                 self.getControl(113).setVisible(False)
                 self.getControl(113).setLabel(self.getString(30038))
                 self.getControl(114).setVisible(False)
                 self.getControl(114).setLabel(self.getString(30038))
                 self.getControl(115).setVisible(False)
                 self.getControl(115).setLabel(self.getString(30039))
                 self.getControl(116).setVisible(False)
                 self.getControl(116).setLabel(self.getString(30039))
                 self.getControl(117).setVisible(False)
                 self.getControl(117).setLabel(self.getString(30040))
                 self.getControl(118).setVisible(False)
                 self.getControl(118).setLabel(self.getString(30040))
                 self.getControl(119).setVisible(False)
                 self.getControl(119).setLabel(self.getString(30041))
                 self.getControl(120).setVisible(False)
                 self.getControl(120).setLabel(self.getString(30041))
                 self.getControl(123).setVisible(False)
                 self.getControl(123).setLabel(self.getString(30042))
                 self.getControl(124).setVisible(False)
                 self.getControl(124).setLabel(self.getString(30042))
                 self.getControl(127).setVisible(False)
                 self.getControl(127).setLabel(self.getString(30047))
                 self.getControl(128).setVisible(False)
                 self.getControl(128).setLabel(self.getString(30047))
                 self.getControl(129).setVisible(False)
                 self.getControl(129).setLabel(self.getString(30048))
                 self.getControl(130).setVisible(False)
                 self.getControl(130).setLabel(self.getString(30048))
                 self.getControl(137).setVisible(False)
                 self.getControl(137).setLabel(self.getString(30045))
                 self.getControl(138).setVisible(False)
                 self.getControl(138).setLabel(self.getString(30045))
                 self.getControl(141).setVisible(False)
                 self.getControl(141).setLabel(self.getString(30047))
                 self.getControl(142).setVisible(False)
                 self.getControl(142).setLabel(self.getString(30047))
                 self.getControl(143).setVisible(False)
                 self.getControl(143).setLabel(self.getString(30048))
                 self.getControl(144).setVisible(False)
                 self.getControl(144).setLabel(self.getString(30048))
                 self.getControl(151).setVisible(False)
                 self.getControl(151).setLabel(self.getString(30046))
                 self.getControl(152).setVisible(False)
                 self.getControl(152).setLabel(self.getString(30046))
                 self.getControl(155).setVisible(False)
                 self.getControl(155).setLabel(self.getString(30047))
                 self.getControl(156).setVisible(False)
                 self.getControl(156).setLabel(self.getString(30047))
                 self.getControl(157).setVisible(False)
                 self.getControl(157).setLabel(self.getString(30048))
                 self.getControl(158).setVisible(False)
                 self.getControl(158).setLabel(self.getString(30048))
                 self.getControl(165).setVisible(False)
                 self.getControl(165).setLabel(self.getString(30049))
                 self.getControl(166).setVisible(False)
                 self.getControl(166).setLabel(self.getString(30049))
                 self.getControl(169).setVisible(False)
                 self.getControl(169).setLabel(self.getString(30047))
                 self.getControl(170).setVisible(False)
                 self.getControl(170).setLabel(self.getString(30047))
                 self.getControl(171).setVisible(False)
                 self.getControl(171).setLabel(self.getString(30048))
                 self.getControl(172).setVisible(False)
                 self.getControl(172).setLabel(self.getString(30048))
                 self.getControl(179).setVisible(False)
                 self.getControl(179).setLabel(self.getString(30050))
                 self.getControl(180).setVisible(False)
                 self.getControl(180).setLabel(self.getString(30050))
                 self.getControl(183).setVisible(False)
                 self.getControl(183).setLabel(self.getString(30047))
                 self.getControl(184).setVisible(False)
                 self.getControl(184).setLabel(self.getString(30047))
                 self.getControl(185).setVisible(False)
                 self.getControl(185).setLabel(self.getString(30048))
                 self.getControl(186).setVisible(False)
                 self.getControl(186).setLabel(self.getString(30048))
                 self.getControl(193).setVisible(False)
                 self.getControl(193).setLabel(self.getString(30051))
                 self.getControl(194).setVisible(False)
                 self.getControl(194).setLabel(self.getString(30051))
                 self.getControl(196).setVisible(False)
                 self.getControl(196).setLabel(self.getString(30052))
                 self.getControl(197).setVisible(False)
                 self.getControl(197).setLabel(self.getString(30034))
                 self.getControl(200).setVisible(False)
                 self.getControl(200).setLabel(self.getString(30053))
                 self.getControl(203).setVisible(False)
                 self.getControl(203).setLabel(self.getString(30054))
                 self.getControl(204).setVisible(False)
                 self.getControl(204).setLabel(self.getString(30054))
                 self.getControl(211).setVisible(False)
                 self.getControl(211).setLabel(self.getString(30037))
                 self.getControl(212).setVisible(False)
                 self.getControl(212).setLabel(self.getString(30037))
                 self.getControl(213).setVisible(False)
                 self.getControl(213).setLabel(self.getString(30038))
                 self.getControl(214).setVisible(False)
                 self.getControl(214).setLabel(self.getString(30038))
                 self.getControl(215).setVisible(False)
                 self.getControl(215).setLabel(self.getString(30039))
                 self.getControl(216).setVisible(False)
                 self.getControl(216).setLabel(self.getString(30039))
                 self.getControl(219).setVisible(False)
                 self.getControl(219).setLabel(self.getString(30058))
                 self.getControl(220).setVisible(False)
                 self.getControl(220).setLabel(self.getString(30058))
                 self.getControl(223).setVisible(False)
                 self.getControl(223).setLabel(self.getString(30047))
                 self.getControl(224).setVisible(False)
                 self.getControl(224).setLabel(self.getString(30047))
                 self.getControl(225).setVisible(False)
                 self.getControl(225).setLabel(self.getString(30048))
                 self.getControl(226).setVisible(False)
                 self.getControl(226).setLabel(self.getString(30048))
                 self.getControl(233).setVisible(False)
                 self.getControl(233).setLabel(self.getString(30059))
                 self.getControl(234).setVisible(False)
                 self.getControl(234).setLabel(self.getString(30059))
                 self.getControl(237).setVisible(False)
                 self.getControl(237).setLabel(self.getString(30047))
                 self.getControl(238).setVisible(False)
                 self.getControl(238).setLabel(self.getString(30047))
                 self.getControl(239).setVisible(False)
                 self.getControl(239).setLabel(self.getString(30048))
                 self.getControl(240).setVisible(False)
                 self.getControl(240).setLabel(self.getString(30048))
                 self.getControl(247).setVisible(False)
                 self.getControl(247).setLabel(self.getString(30060))
                 self.getControl(248).setVisible(False)
                 self.getControl(248).setLabel(self.getString(30060))
                 self.getControl(251).setVisible(False)
                 self.getControl(251).setLabel(self.getString(30047))
                 self.getControl(252).setVisible(False)
                 self.getControl(252).setLabel(self.getString(30047))
                 self.getControl(253).setVisible(False)
                 self.getControl(253).setLabel(self.getString(30048))
                 self.getControl(254).setVisible(False)
                 self.getControl(254).setLabel(self.getString(30048))
                 self.getControl(261).setVisible(False)
                 self.getControl(261).setLabel(self.getString(30061))
                 self.getControl(262).setVisible(False)
                 self.getControl(262).setLabel(self.getString(30061))
                 self.getControl(265).setVisible(False)
                 self.getControl(265).setLabel(self.getString(30047))
                 self.getControl(266).setVisible(False)
                 self.getControl(266).setLabel(self.getString(30047))
                 self.getControl(267).setVisible(False)
                 self.getControl(267).setLabel(self.getString(30048))
                 self.getControl(268).setVisible(False)
                 self.getControl(268).setLabel(self.getString(30048))
                 self.getControl(275).setVisible(False)
                 self.getControl(275).setLabel(self.getString(30076))
                 self.getControl(276).setVisible(False)
                 self.getControl(276).setLabel(self.getString(30051))
                 self.getControl(278).setVisible(False)
                 self.getControl(278).setLabel(self.getString(30052))
                 self.getControl(279).setVisible(False)
                 self.getControl(279).setLabel(self.getString(30034))
                 self.getControl(282).setVisible(False)
                 self.getControl(282).setLabel(self.getString(30062))
                 self.getControl(285).setVisible(False)
                 self.getControl(285).setLabel(self.getString(30063))
                 self.getControl(286).setVisible(False)
                 self.getControl(286).setLabel(self.getString(30063))
                 self.getControl(293).setVisible(False)
                 self.getControl(293).setLabel(self.getString(30064))
                 self.getControl(294).setVisible(False)
                 self.getControl(294).setLabel(self.getString(30064))
                 self.getControl(295).setVisible(False)
                 self.getControl(295).setLabel(self.getString(30065))
                 self.getControl(296).setVisible(False)
                 self.getControl(296).setLabel(self.getString(30065))
                 self.getControl(297).setVisible(False)
                 self.getControl(297).setLabel(self.getString(30066))
                 self.getControl(298).setVisible(False)
                 self.getControl(298).setLabel(self.getString(30066))
                 self.getControl(299).setVisible(False)
                 self.getControl(299).setLabel(self.getString(30067))
                 self.getControl(300).setVisible(False)
                 self.getControl(300).setLabel(self.getString(30067))
                 self.getControl(301).setVisible(False)
                 self.getControl(301).setLabel(self.getString(30068))
                 self.getControl(302).setVisible(False)
                 self.getControl(302).setLabel(self.getString(30068))
                 self.getControl(303).setVisible(False)
                 self.getControl(303).setLabel(self.getString(30069))
                 self.getControl(304).setVisible(False)
                 self.getControl(304).setLabel(self.getString(30069))
                 self.getControl(305).setVisible(False)
                 self.getControl(305).setLabel(self.getString(30070))
                 self.getControl(306).setVisible(False)
                 self.getControl(306).setLabel(self.getString(30070))
                 self.getControl(307).setVisible(False)
                 self.getControl(307).setLabel(self.getString(30071))
                 self.getControl(308).setVisible(False)
                 self.getControl(308).setLabel(self.getString(30071))
                 self.getControl(309).setVisible(False)
                 self.getControl(309).setLabel(self.getString(30072))
                 self.getControl(310).setVisible(False)
                 self.getControl(310).setLabel(self.getString(30072))
                 self.getControl(311).setVisible(False)
                 self.getControl(311).setLabel(self.getString(30073))
                 self.getControl(312).setVisible(False)
                 self.getControl(312).setLabel(self.getString(30073))
                 self.getControl(313).setVisible(False)
                 self.getControl(313).setLabel(self.getString(30074))
                 self.getControl(314).setVisible(False)
                 self.getControl(314).setLabel(self.getString(30074))
                 self.getControl(315).setVisible(False)
                 self.getControl(315).setLabel(self.getString(30075))
                 self.getControl(316).setVisible(False)
                 self.getControl(316).setLabel(self.getString(30075))
                 self.getControl(319).setVisible(False)
                 self.getControl(319).setLabel(self.getString(30076))
                 self.getControl(320).setVisible(False)
                 self.getControl(320).setLabel(self.getString(30076))
                 self.getControl(322).setVisible(False)
                 self.getControl(322).setLabel(self.getString(30078))
                 self.getControl(326).setVisible(False)
                 self.getControl(326).setLabel(self.getString(30079))
                 self.getControl(327).setVisible(False)
                 self.getControl(327).setLabel(self.getString(30079))
                 self.getControl(328).setVisible(False)
                 self.getControl(328).setLabel(self.getString(30080))
                 self.getControl(330).setVisible(False)
                 self.getControl(330).setLabel(self.getString(30081))
                 self.getControl(331).setVisible(False)
                 self.getControl(331).setLabel(self.getString(30082))
                 self.getControl(342).setVisible(False)
                 self.getControl(342).setLabel(self.getString(30071))
                 self.getControl(343).setVisible(False)
                 self.getControl(343).setLabel(self.getString(30082))
                 cSetVisible(self,344,False)
                 cSetVisible(self,345,False)
                 cSetVisible(self,346,False)
                 self.getControl(361).setLabel(' ')
                 cSetVisible(self,361,False)
                 self.getControl(361).setLabel(' ')
                 cSetVisible(self,362,False)
                 self.getControl(362).setLabel(' ')
                 cSetVisible(self,363,False)
                 self.getControl(363).setLabel(' ')
                 cSetVisible(self,364,False)
                 self.getControl(364).setLabel(' ')
                 cSetVisible(self,365,False)
                 self.getControl(365).setLabel(' ')
                 cSetVisible(self,366,False)
                 self.getControl(366).setLabel(' ')
                 cSetVisible(self,367,False)
                 self.getControl(367).setLabel(' ')
                 cSetVisible(self,368,False)
                 self.getControl(368).setLabel(' ')
                 cSetVisible(self,369,False)
                 self.getControl(369).setLabel(' ')
                 cSetVisible(self,370,False)
                 self.getControl(370).setLabel(' ')
                 cSetVisible(self,371,False)
                 self.getControl(372).setLabel(' ')
                 cSetVisible(self,373,False)
                 self.getControl(373).setLabel(' ')
                 cSetVisible(self,374,False)
                 self.getControl(374).setLabel(' ')
                 #self.label = xbmcgui.ControlLabel(50, 50, 525, 75, 'My Label Text', textColor='0xFFFFFFFF')
                 #self.addControl(self.label)
                 #MyLabelText = "Hello!"
                 #self.label.setLabel('[COLOR FF00C936]' + MyLabelText + '[/COLOR]')



                 if english_enabled:
                     cSetVisible(self,380,False)
                     cSetVisible(self,381,False)
                     cSetVisible(self,382,False)
                     cSetVisible(self,383,False)
                     cSetVisible(self,384,False)
                     cSetVisible(self,387,False)
                     cSetVisible(self,46,True)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,True)
                     cSetVisible(self,53,True)
                     cSetVisible(self,54,True)
                     cSetVisible(self,57,True)
                     cSetVisible(self,59,True)
                     cSetVisible(self,61,True)
                     cSetVisible(self,63,True)
                     cSetVisible(self,65,True)
                     cSetVisible(self,67,True)
                     cSetVisible(self,69,True)
                     cSetVisible(self,71,True)
                     cSetVisible(self,73,True)



                 if french_enabled:
                     pass
                     #cSetVisible(self,264,True)




     def parseDateTimeToMinutesSinceEpoch(self, p_datetime):
         datetime = time.strptime(p_datetime, "%Y%m%d%H%M%S")
         seconds_epoch = time.mktime(datetime)
         minutes_epoch = int(seconds_epoch / 60)
         return minutes_epoch



     def format(time):
         return time.strftime("%I").lstrip('0') + time.strftime(":%M%p")



     def abortdownload(self):
         global __killthread__
         __killthread__ = True
         if self.thread is not None:
            self.thread.join(3000)
         del self.thread
         self.thread = None



     def setControlImage(self, controlId, image):
         control = self.getControl(controlId)
         if control:
             control.setImage(image)



     def clearEPG(self):
         if self.move_down_flag == False:
             program_buttons = [elem.control for elem in self.program_buttons]
             try:
                 self.removeControls(program_buttons)
             except RuntimeError:
                 for elem in self.program_buttons:
                     try:
                         self.removeControl(elem.control)
                     except RuntimeError:
                         pass # happens if we try to remove a control that doesn't exist
             del self.program_buttons[:]



         if self.move_up_flag == True:
             program_buttons = [elem.control for elem in self.program_buttons]
             self.move_up_flag = False
             try:
                 self.removeControls(program_buttons)
             except:
                 for elem in self.program_buttons:
                     try:
                         self.removeControl(elem.control)
                     except:
                         pass # happens if we try to remove a control that doesn't exist
             del self.program_buttons[:]



         if self.move_down_flag == True:
             program_buttons = [elem.control for elem in self.program_buttons]
             self.move_down_flag = False
             try:
                 self.removeControls(program_buttons)
             except:
                 for elem in self.program_buttons:
                     try:
                         self.removeControl(elem.control)
                     except:
                         pass # happens if we try to remove a control that doesn't exist
             del self.program_buttons[:]



         if self.move_back_flag == True:
             program_buttons = [elem.control for elem in self.program_buttons]
             self.move_back_flag = False
             try:
                 self.removeControls(program_buttons)
             except:
                 for elem in self.program_buttons:
                     try:
                         self.removeControl(elem.control)
                     except:
                         pass # happens if we try to remove a control that doesn't exist
             del self.program_buttons[:]




     def get_programming_info(self):
         print "hello chris, your self.get_button_id is " + str(self.get_button_id)
         self.getControl(int(self.get_button_id)).setVisible(False)
         #cur = con.cursor()
         #cur.execute('SELECT stop_date FROM programs where channel=?', [self.prog_id])
         #stop_date = cur.fetchone()


         #if stop_date is not None:
             #stop_date = str(stop_date[1])
             #half_hour = str(self.getControl(344).getLabel())
             #one_hour = str(self.getControl(345).getLabel())
             #one_hour_half = str(self.getControl(346).getLabel())
             #epg_time_1 = time.strptime(half_hour, '%I:%M%p')
             #epg_time_2 = time.strptime(one_hour, '%I:%M%p')
             #epg_time_3 = time.strptime(one_hour_half, '%I:%M%p')

             #if prog_stop_clock == '05':
                 #print "change itn news width size"
                 #print "program_length"
                 #print program_length




     def All_Channels_BACKUP(self):
         global __killthread__
         self.getControl(343).setLabel("0%")

         try:
             # DOWNLOAD THE XML SOURCE HERE
             profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide/'))
             url = ADDON.getSetting('database.url')
             urllib.urlretrieve(url, profilePath + 'source.db')

             #if (0 <= datetime.datetime.now().minute <= 5):
                 #url = ADDON.getSetting('database.url')
                 #urllib.urlretrieve(url, profilePath + 'source.db')
                 #print "you are in the database 1"
             #elif (6 <= datetime.datetime.now().minute <= 29):
                 #url = ADDON.getSetting('database.url')
                 #urllib.urlretrieve(url, profilePath + 'source.db')
                 #print "you are in the database 2"
             #elif (30 <= datetime.datetime.now().minute <= 35):
                 #url = ADDON.getSetting('database1.url')
                 #urllib.urlretrieve(url, profilePath + 'source.db')
                 #print "you are in the database 3"
             #elif (36 <= datetime.datetime.now().minute <= 58):
                 #url = ADDON.getSetting('database.url')
                 #urllib.urlretrieve(url, profilePath + 'source.db')
                 #print "you are in the database 4"


             data = ''
             response = urllib2.urlopen(url)
             meta = response.info()
             file_size = int(meta.getheaders("Content-Length")[0])
             file_size_dl = 0
             block_size = 2066

             while True and not __killthread__:
                 mbuffer = response.read(block_size)
                 if not mbuffer:
                     break
                 file_size_dl += len(mbuffer)
                 data += mbuffer
                 state = int(file_size_dl * 100.0 / file_size)
                 self.getControl(343).setLabel(str(state) + '%')
             else:
                 if __killthread__:
                     raise AbortDownload('downloading')
             del response

             #CONNECT TO THE DATABASE
             conn = database.connect(profilePath + 'source.db')
             cur = conn.cursor()

             #Get the loaded data
             channels = OrderedDict()
             channelsList = list()
             categoryList = list()
             title_list = list()
             start_time_list = list()
             stop_time_list = list()

             print 'Channels have been successfully stored into the database!'
             #xbmc.sleep(3000)

             #Set the date and time row
             current_time = time.time() # now (in seconds)
             half_hour = current_time + 60*30  # now + 30 minutes
             one_hour = current_time + 60*60  # now + 60 minutes

             for t in [current_time,half_hour,one_hour]:
                 if (0 <= datetime.datetime.now().minute <= 29):
                     self.getControl(344).setLabel(time.strftime("%I").lstrip('0') + ':00' + time.strftime("%p"))
                     self.getControl(345).setLabel(time.strftime("%I").lstrip('0') + ':30' + time.strftime("%p"))
                     self.getControl(346).setLabel(time.strftime("%I" + ":00%p",time.localtime(t)).lstrip("0"))
                 else:
                     self.getControl(344).setLabel(time.strftime("%I").lstrip('0') + ':30' + time.strftime("%p"))
                     self.getControl(345).setLabel(time.strftime("%I" + ":00%p",time.localtime(t)).lstrip("0"))
                     self.getControl(346).setLabel(time.strftime("%I" + ":30%p",time.localtime(t)).lstrip("0"))


             #Pull the data from the database
             prog_title = list()
             prog_stop_date = list()
             channelList = list()

             if os.path.exists(profilePath):
                 #get the channels list
                 cur = conn.cursor()
                 cur.execute('SELECT channel, title, start_date, stop_date, category FROM programs WHERE channel GROUP BY channel')

                 for row in cur:
                     channels = row[0].encode('ascii')
                     channelList.append(channels)


                 #find channels from the channels list
                 for channels in channelList:
                     cur.execute('SELECT channel, title, start_date, stop_date FROM programs where channel=? LIMIT 1', [channels])
                     program = cur.fetchall()

                     for ind, row in enumerate(program):
                         test_channels = row[0]
                         program_title_1 = row[1]
                         start_date = row[2]
                         program_start_date_1 = str(row[2])
                         program_end_date_1 = str(row[3])
                         minutes = int(time.strftime("%M"))
                         epg_minutes = '00'

                         if minutes >= 00 and minutes <= 29:
                             epg_minutes = '00'
                         elif minutes >= 30 and minutes <= 59:
                             epg_minutes = '30'


                         epg_time = str(time.strftime("%Y") + time.strftime("%m") + time.strftime("%d") + time.strftime("%H") + epg_minutes + '00')
                         epg_time_1 = time.strptime(epg_time, '%Y%m%d%H%M%S')
                         epg_time_1 = datetime.datetime.fromtimestamp(time.mktime(epg_time_1))
                         program_stop_time_1 = time.strptime(program_end_date_1, '%Y%m%d%H%M%S')
                         program_stop_time_1 = datetime.datetime.fromtimestamp(time.mktime(program_stop_time_1))
                         program_start_time_1 = time.strptime(program_start_date_1, '%Y%m%d%H%M%S')
                         program_start_time_1 = datetime.datetime.fromtimestamp(time.mktime(program_start_time_1))

                         if start_date == '':
                             print "you are deleted the empty data for the start_time and stop_time row"
                             cur.execute("DELETE FROM programs WHERE title=?", (program_title_1,))
                             conn.commit()


                         #check if the program stop times is less than the epg_time_1
                         if program_start_time_1 == epg_time_1 or program_start_time_1 > epg_time_1:
                             #print "keep the program running " + str (program_title_1) + " from channel " + str(channels)
                             pass

                         #elif program_stop_time_1 < epg_time_1 or program_stop_time_1 == epg_time_1:
                         elif program_stop_time_1 <= epg_time_1:
                             #print "delete " + (program_title_1) + " from " + (channels)
                             cur.execute("DELETE FROM programs WHERE title=?", (program_title_1,))
                             conn.commit()
                             print "delete database in epg_time_1"
                             print program_title_1


                             cur.execute('SELECT channel, title, start_date, stop_date FROM programs where channel=? LIMIT 1', [channels])
                             program = cur.fetchall()

                             for ind, row in enumerate(program):
                                 program_title_2 = row[1]
                                 program_end_date_2 = str(row[3])
                                 minutes = int(time.strftime("%M"))
                                 epg_minutes = '00'

                                 if minutes >= 00 and minutes <= 29:
                                     epg_minutes = '00'
                                 elif minutes >= 30 and minutes <= 59:
                                     epg_minutes = '30'


                                 epg_time = str(time.strftime("%Y") + time.strftime("%m") + time.strftime("%d") + time.strftime("%H") + epg_minutes + '00')
                                 epg_time_1 = time.strptime(epg_time, '%Y%m%d%H%M%S')
                                 epg_time_1 = datetime.datetime.fromtimestamp(time.mktime(epg_time_1))
                                 program_stop_time_2 = time.strptime(program_end_date_2, '%Y%m%d%H%M%S')
                                 program_stop_time_2 = datetime.datetime.fromtimestamp(time.mktime(program_stop_time_2))
                                 print "program_title_2"
                                 #print str(program_title_2)

                                 if program_stop_time_2 <= epg_time_1:
                                     print "you are deleted the data for the epg_time_1 equal 2"
                                     cur.execute("DELETE FROM programs WHERE title=?", (program_title_2,))
                                     conn.commit()
                                     cur.execute('SELECT channel, title, start_date, stop_date FROM programs where channel=? LIMIT 1', [channels])
                                     program = cur.fetchall()

                                     for ind, row in enumerate(program):
                                         program_title_3 = row[1]
                                         program_end_date_3 = str(row[3])
                                         minutes = int(time.strftime("%M"))
                                         epg_minutes = '00'

                                         if minutes >= 00 and minutes <= 29:
                                             epg_minutes = '00'
                                         elif minutes >= 30 and minutes <= 59:
                                             epg_minutes = '30'


                                         epg_time = str(time.strftime("%Y") + time.strftime("%m") + time.strftime("%d") + time.strftime("%H") + epg_minutes + '00')
                                         epg_time_1 = time.strptime(epg_time, '%Y%m%d%H%M%S')
                                         epg_time_1 = datetime.datetime.fromtimestamp(time.mktime(epg_time_1))
                                         program_stop_time_3 = time.strptime(program_end_date_3, '%Y%m%d%H%M%S')
                                         program_stop_time_3 = datetime.datetime.fromtimestamp(time.mktime(program_stop_time_3))
                                         print "program_title_3"
                                         print program_title_3

                                         if program_stop_time_3 <= epg_time_1:
                                             print "you are deleted the data for the epg_time_1 equal 3"
                                             cur.execute("DELETE FROM programs WHERE title=?", (program_title_3,))
                                             conn.commit()


                 cur.execute('SELECT channel, title, start_date, stop_date, category FROM programs')

                 for row in cur:
                     channels = row[0].encode('ascii')
                     channelsList.append(channels)
                     title = row[1]
                     title_list.append(title)
                     start_time = row[2]
                     start_time_list.append(start_time)
                     stop_time = row[3]
                     stop_time_list.append(stop_time)
                     category = row[4].encode('ascii')
                     categoryList.append(category)

                 #self.button.setLabel('Status', 'font14', '0xFFFFFFFF', '0xFFFF3300', '0xFF000000')
                 #or self.getControl(361).setLabel('Status', 'font14', '0xFFFFFFFF', '0xFFFF3300', '0xFF000000')

                 #set the channels text
                 channels_list = list()


                 for index in range(0, CHANNELS_PER_PAGE):
                     channel = channelList[index]
                     channel_index = index

                     if channel is not None:
                         self.getControl(361 + index).setLabel(channel)
                         self.getControl(368 + index).setLabel(channel)


                     #get the programs list
                     cur.execute('SELECT channel, title, start_date, stop_date FROM programs where channel=? LIMIT 10', [channel])
                     programList = list()
                     programs = cur.fetchall()
                     start_pos = 375    # indent for first program

                     for ind, row in enumerate(programs):
                         program = row[0], row[1], row[2], row[3]
                         channels = str(row[0])
                         title = row[1]
                         title = title.encode('utf-8', 'ignore')
                         program_start_date = str(row[2])
                         program_end_date = str(row[3])
                         prog_title.append(title)
                         prog_stop_date.append(program_end_date)

                         #convert the date formats into minutes
                         minutes_start = self.parseDateTimeToMinutesSinceEpoch(program_start_date)
                         minutes_end = self.parseDateTimeToMinutesSinceEpoch(program_end_date)
                         minutes_length = minutes_end - minutes_start
                         program_minutes = minutes_length
                         programs_top = 315
                         program_height = 33
                         program_gap = 3
                         position_start = start_pos
                         position_top = programs_top + channel_index * (program_height + program_gap + 1.5)

                         if position_top == 315:
                             position_top = 314
                         elif position_top == 352.5:
                             position_top = 352
                         elif position_top == 390.0:
                             position_top = 390
                         elif position_top == 427.5:
                             position_top = 427
                         elif position_top == 465.0:
                             position_top = 465
                         elif position_top == 502.5:
                             position_top = 502
                         elif position_top == 540.0:
                             position_top = 539
                         path = "special://home/addons/script.tvguide/resources/skins/Default/media/"

                         #work out on program per minute to multiply by 11.4 to get the width size
                         program_width = program_minutes * 11.4
                         program_width = eval(str(program_width).replace('.0', ''))

                         #create width size for program buttons
                         if program_width == 57:
                             program_width = 59
                         elif program_width == 79:
                             program_width = 59
                         elif program_width == 114:
                             program_width = 117
                         elif program_width == 148:
                             program_width = 168
                         elif program_width == 171:
                             program_width = 167
                         elif program_width == 228:
                             program_width = 227
                         elif program_width == 278:
                             program_width = 276
                         elif program_width == 285:
                             program_width = 286
                         elif program_width == 342:
                             program_width = 342
                         elif program_width == 399:
                             program_width = 396
                         elif program_width == 460:
                             program_width = 456
                         elif program_width == 453:
                             program_width = 452
                         elif program_width == 513:
                             program_width = 515
                         elif program_width == 570:
                             program_width = 567
                         elif program_width == 627:
                             program_width = 626
                         elif program_width == 677:
                             program_width = 676
                         elif program_width == 684:
                             program_width = 691
                         elif program_width == 3876:
                             program_width = 3787


                         #print program_width
                         start_pos += program_width + 2 * program_gap + 1

                         if program_width > 1:
                             if program_width < 1:
                                 program_title = ''
                             else:
                                 program_title = '[B]' + title + '[/B]'

                             program_controls = xbmcgui.ControlButton(
                                 int(position_start), 
                                 int(position_top), 
                                 int(program_width), 
                                 int(program_height), 
                                 program_title, 
                                 focusTexture = path + self.button_focus, 
                                 noFocusTexture = path + self.button_nofocus,
                                 alignment=0,
                                 textColor = '0xFFFFFFFF',
                                 focusedColor = '0xFF000000'
                             )
                             #Enabled the channels and programs control
                             self.getControl(347).setVisible(True)
                             self.getControl(348).setVisible(True)
                             self.getControl(349).setVisible(True)
                             self.getControl(350).setVisible(True)
                             self.getControl(351).setVisible(True)
                             self.getControl(352).setVisible(True)
                             self.getControl(353).setVisible(True)
                         self.program_buttons.append(ProgramControls(program_controls, program))
                         self.program.append(program)
                     channels_list.append(channel)
                 #create the table in a database
                 programs_button = [elem.control for elem in self.program_buttons]
                 program_id = list()
                 program_width = list()
                 posX = list()
                 program_start_clock = list()
                 cur.execute('CREATE TABLE IF NOT EXISTS buttons(button_ids TEXT, button_width TEXT)')
                 cur.execute('CREATE TABLE IF NOT EXISTS streams(channels TEXT, stream_url TEXT)')
                 print "buttons stored in a database"


                 #add the programs buttons
                 if len(programs_button) > 1:
                     self.addControls(programs_button)
                     #ADDON.setSetting('FullScreen.enabled', 'false')

                     for elem in programs_button:
                         program_id.append(elem.getId())
                         posX.append(elem.getX())
                     program_id = map(str, program_id)
                     posX = map(str, posX)

                     #Store the list of strings in the lists
                     for i in range(len(posX)):
                         pos_X = posX[i]

                         if pos_X == '375':
                             self.prog_id_list.append(program_id[i])



                     for channels in channels_list:
                         #get the stop_date from the programs list
                         cur.execute('SELECT start_date, stop_date FROM programs where channel=?', [channels])
                         stop_date = cur.fetchone()

                         if stop_date is not None:
                             start_date = str(stop_date[0])
                             stop_date = str(stop_date[1])
                             date = str(time.strftime("%Y") + time.strftime("%m") + time.strftime("%d") + time.strftime("%H") + time.strftime("%M") + '00')
                             current_time = time.strptime(date, '%Y%m%d%H%M%S')
                             current_time = datetime.datetime.fromtimestamp(time.mktime(current_time))
                             start_time = time.strptime(start_date, '%Y%m%d%H%M%S')
                             start_time = datetime.datetime.fromtimestamp(time.mktime(start_time))
                             stop_time = time.strptime(stop_date, '%Y%m%d%H%M%S')
                             stop_time = datetime.datetime.fromtimestamp(time.mktime(stop_time))
                             currenttime = self.parseDateTimeToMinutesSinceEpoch(start_date)
                             program_stop = self.parseDateTimeToMinutesSinceEpoch(stop_date)
                             program_stop - currenttime
                             datetime.timedelta(0, 8100)
                             total_program_length = program_stop - currenttime
                             get_program_stop_hours = stop_time.strftime('%H')
                             get_program_stop_minutes = stop_time.strftime('%M')
                             #get_program_start_hours = start_time.strftime('%H')
                             #get_program_start_minutes = start_time.strftime('%M')
                             #program_start_hours = str(get_program_start_hours)
                             #program_start_minutes = str(get_program_start_minutes)
                             program_stop_hours = str(get_program_stop_hours)
                             program_stop_minutes = str(get_program_stop_minutes)
                             program_AM_PM = ''

                             if program_stop_hours == "00":
                                 program_stop_hours = "12"
                                 program_AM_PM = 'AM'
                             elif program_stop_hours == "01":
                                 program_stop_hours = "1"
                                 program_AM_PM = 'AM'
                             elif program_stop_hours == "02":
                                 program_stop_hours = "2"
                                 program_AM_PM = 'AM'
                             elif program_stop_hours == "03":
                                 program_stop_hours = "3"
                                 program_AM_PM = 'AM'
                             elif program_stop_hours == "04":
                                 program_stop_hours = "4"
                                 program_AM_PM = 'AM'
                             elif program_stop_hours == "05":
                                 program_stop_hours = "5"
                                 program_AM_PM = 'AM'
                             elif program_stop_hours == "06":
                                 program_stop_hours = "6"
                                 program_AM_PM = 'AM'
                             elif program_stop_hours == "07":
                                 program_stop_hours = "7"
                                 program_AM_PM = 'AM'
                             elif program_stop_hours == "08":
                                 program_stop_hours = "8"
                                 program_AM_PM = 'AM'
                             elif program_stop_hours == "09":
                                 program_stop_hours = "9"
                                 program_AM_PM = 'AM'
                             elif program_stop_hours == "10":
                                 program_stop_hours = "10"
                                 program_AM_PM = 'AM'
                             elif program_stop_hours == "11":
                                 program_stop_hours = "11"
                                 program_AM_PM = 'AM'
                             elif program_stop_hours == "12":
                                 program_stop_hours = "12"
                                 program_AM_PM = 'PM'
                             elif program_stop_hours == "13":
                                 program_stop_hours = "1"
                                 program_AM_PM = 'PM'
                             elif program_stop_hours == "14":
                                 program_stop_hours = "2"
                                 program_AM_PM = 'PM'
                             elif program_stop_hours == "15":
                                 program_stop_hours = "3"
                                 program_AM_PM = 'PM'
                             elif program_stop_hours == "16":
                                 program_stop_hours = "4"
                                 program_AM_PM = 'PM'
                             elif program_stop_hours == "17":
                                 program_stop_hours = "5"
                                 program_AM_PM = 'PM'
                             elif program_stop_hours == "18":
                                 program_stop_hours = "6"
                                 program_AM_PM = 'PM'
                             elif program_stop_hours == "19":
                                 program_stop_hours = "7"
                                 program_AM_PM = 'PM'
                             elif program_stop_hours == "20":
                                 program_stop_hours = "8"
                                 program_AM_PM = 'PM'
                             elif program_stop_hours == "21":
                                 program_stop_hours = "9"
                                 program_AM_PM = 'PM'
                             elif program_stop_hours == "22":
                                 program_stop_hours = "10"
                                 program_AM_PM = 'PM'
                             elif program_stop_hours == "23":
                                 program_stop_hours = "11"
                                 program_AM_PM = 'PM'


                             program_stop_time = program_stop_hours + ":" + program_stop_minutes + program_AM_PM
                             #get_24_hours = int(time.strftime("%I"))
                             #get_24_minutes = int(time.strftime("%M"))
                             #current_time_ = datetime.timedelta(hours = get_24_hours, minutes = get_24_minutes)
                             #end_program = datetime.timedelta(hours = int(program_stop_hours), minutes = int(program_stop_minutes))
                             #current_program = end_program - current_time_
                             #program_mins = int(current_program.seconds / 60)
                             #program_remaining.append(program_mins)
                             program_end_time = stop_time
                             self.program_end_time.append(program_end_time)

                             if total_program_length >= 5:
                                 program_index = self.program_index
                                 self.program_index_ = list()
                                 self.program_index_.append(program_index)

                             program_finished_minutes = program_stop_time.split(':')[1].replace('PM', '').replace('AM', '')
                             self.program_finished.append(program_finished_minutes)
                             #self.program_stop_clock = list()
                             #self.program_stop_clock.append(program_stop_time)


                             #KEEP THIS DONT DELETE THIS!
                             #if current_time == start_time:
                                 #print "the program has started"

                                 #if total_program_length >= 5:
                                     #program_index = self.program_index
                                     #self.program_index_ = list()
                                     #self.program_index_.append(program_index)


                                 #############for pos_X in posX:
                                     #############if int(pos_X) == 375:
                                         #############prog_index = [self.program_index_]

                                         #############if len(self.program_index_) >= 1:
                                             #############for index in prog_index[0]:
                                                 #############prog_id = self.prog_id_list[index]
                                                 ##self.program_id = list()
                                                 ##self.program_id.append(prog_id)


                                 #program_finished_minutes = program_stop_time.split(':')[1].replace('PM', '').replace('AM', '')
                                 #self.program_finished = list()
                                 #self.program_finished.append(program_finished_minutes)
                                 #self.program_stop_clock = list()
                                 #self.program_stop_clock.append(program_stop_time)
                                 #self.program_remaining = True
                                 #liveprogramming.programs_remaining(self)


                             ############elif current_time > start_time and current_time < stop_time or start_time < current_time and current_time < stop_time:
                             #elif current_time > start_time and current_time < stop_time or current_time < stop_time:
                                 #print "program is half way"

                                 #if total_program_length >= 5:
                                     #program_index = self.program_index
                                     #self.program_index_ = list()
                                     #self.program_index_.append(program_index)


                                 #############for pos_X in posX:
                                     #############if int(pos_X) == 375:
                                         #############prog_index = [self.program_index_]

                                         #############if len(self.program_index_) >= 1:
                                             #############for index in prog_index[0]:
                                                     #prog_id = self.prog_id_list[index]
                                                     ##self.program_id = list()
                                                     ##self.program_id.append(prog_id)


                                 #program_finished_minutes = program_stop_time.split(':')[1].replace('PM', '').replace('AM', '')
                                 #self.program_finished = list()
                                 #self.program_finished_clock.append(program_finished_minutes)
                                 #self.program_stop_clock = list()
                                 #self.program_stop_clock.append(program_stop_time)
                                 #self.program_remaining = True
                                 #liveprogramming.programs_remaining(self)


                             #else:
                                 #print "program has finished"

                                 #if total_program_length >= 5:
                                     #program_index = self.program_index
                                     #self.program_index_ = list()
                                     #self.program_index_.append(program_index)


                                 #program_finished_minutes = program_stop_time.split(':')[1].replace('PM', '').replace('AM', '')
                                 #self.program_finished_clock = list()
                                 #self.program_finished_clock.append(program_finished_minutes)
                                 #self.program_stop_clock = list()
                                 #self.program_stop_clock.append(program_stop_time)
                                 #self.program_remaining = True
                                 #liveprogramming.programs_remaining(self)
                             self.program_index += 1
                         #conn.close()
                     self.program_remaining = True
                     liveprogramming.programs_remaining(self)

                     cur.execute("DELETE FROM programs")
                     ##############xbmc.sleep(1000)
                     channel_namelast = ""
                     countbc = 0 #for first button


                     #store the id and width of buttons in a database
                     for title, channel_name, start_time, stop_time, category, prog_width in izip_longest(title_list, channelsList, start_time_list, stop_time_list, categoryList, program_width, fillvalue=''):
                         if channel_name != channel_namelast:  # next channel
                             countbut = 0  # we will allow for 10 buttons per channel (0 to 9 from button_id list)
                         if countbut < 10 and countbc < 70:
                             #ie we are adding a button_id here
                             buttonadd = program_id[countbc] # get the buttonid from the list
                             countbc = countbc + 1
                             countbut = countbut + 1
                         else:
                             buttonadd = "" #put in a blank
                         #Store the data into the database
                         cur.execute("INSERT INTO programs(channel, title, start_date, stop_date, category, program_id)" + " VALUES(?, ?, ?, ?, ?, ?)", [channel_name, title, start_time, stop_time, category, buttonadd])
                         channel_namelast = channel_name

                     #Empty the list after stored the programming data in a list
                     channelsList = list()
                     categoryList = list()
                     title_list = list()
                     start_time_list = list()
                     stop_time_list = list()


                     for button_id, prog_width in zip(program_id, program_width)[:70]:
                         cur.execute("INSERT INTO buttons(button_ids, button_width)" + " VALUES(?, ?)", [button_id, prog_width])


                     #for full_channels, streams_url in zip(channelList, streamList):
                         #cur.execute("INSERT INTO streams(channels, stream_url)" + " VALUES(?, ?)", [full_channels, streams_url])
                     conn.commit()
                     conn.close()


                     #Enabled EPG and other controls
                     self.getControl(340).setVisible(False)
                     self.getControl(343).setVisible(False)
                     self.getControl(341).setVisible(False)
                     self.getControl(342).setVisible(True)
                     self.getControl(344).setVisible(True)
                     self.getControl(345).setVisible(True)
                     self.getControl(346).setVisible(True)
                     self.getControl(375).setVisible(True)
                     self.getControl(376).setVisible(True)
                     self.getControl(380).setVisible(True)
                     self.getControl(377).setVisible(True)
                     self.getControl(381).setVisible(True)
                     self.getControl(378).setVisible(True)
                     self.getControl(382).setVisible(True)
                     self.getControl(379).setVisible(True)
                     self.getControl(383).setVisible(True)
                     self.getControl(384).setVisible(True)
                     self.getControl(385).setVisible(True)
                     self.getControl(386).setVisible(True)
                     self.getControl(387).setVisible(True)
                     self.getControl(388).setVisible(True)
                     self.getControl(321).setVisible(True)

                     #set focus for the button
                     program_X = programs_button[0].getX()
                     program_width = programs_button[0].getWidth()
                     nextprogram_X = programs_button[1].getX()
                     nextprogram_width = programs_button[1].getWidth()
                     nextprogram1_X = programs_button[2].getX()

                     if program_X < 375:
                         if program_width == 227:
                             if nextprogram_width == 117:
                                 self.setFocus(programs_button[2])
                             else:
                                 self.setFocus(programs_button[1])

                         else:
                             if nextprogram_width >= 227:
                                 print "you are here 1"
                                 self.setFocus(programs_button[1])


                     else:
                         if nextprogram_X == 375:
                             self.setFocus(programs_button[1])
                         elif nextprogram1_X == 375:
                             self.setFocus(programs_button[2])
                         elif program_X == 375:
                             self.setFocus(programs_button[0])




         except AbortDownload, e:
             __killthread__ = False
             if e.value == 'downloading':
                 try:
                    if response is not None:
                         self.thread = AllChannelsThread(self.All_Channels_BACKUP)
                         self.thread.start()
                    return
                 except:
                    return
             elif e.value == 'filling':
                 try:
                    if cur is not None:
                        del cur
                    if con is not None:
                        con.close()
                        del con
                    if os.path.exists(profilePath):
                        os.remove(profilePath)
                    return
                 except:
                    return



     def My_Favourites(self):
         pass




     def Picture(self):
         pass




     def Sound(self):
         pass




     def Change_Language(self):
         pass




     def Parental_Control(self):
         for i in range(1):
             time.sleep(0.3)
             self.getControl(2).setVisible(False)
             self.getControl(5).setVisible(False)
             self.getControl(7).setVisible(False)
             self.getControl(8).setVisible(False)
             self.getControl(31).setVisible(False)
             self.getControl(33).setVisible(False)
             self.getControl(35).setVisible(False)
             self.getControl(36).setVisible(False)
             self.getControl(39).setVisible(False)
             self.getControl(41).setVisible(False)
             self.getControl(43).setVisible(False)
             self.getControl(45).setVisible(False)
             self.getControl(200).setVisible(True)
             self.getControl(201).setVisible(True)
             self.getControl(4002).setVisible(True)
             self.getControl(4006).setVisible(True)
             self.getControl(4009).setVisible(True)
             self.getControl(4010).setVisible(True)
             self.getControl(4011).setVisible(True)
             self.getControl(4012).setVisible(True)
             ADDON.setSetting('changepin.enabled', 'true')
             english_enabled = ADDON.getSetting('english.enabled') == 'true'


             if english_enabled:
                 self.getControl(47).setVisible(False)
                 self.getControl(49).setVisible(False)
                 self.getControl(51).setVisible(False)
                 self.getControl(52).setVisible(False)
                 self.getControl(75).setVisible(False)
                 self.getControl(77).setVisible(False)
                 self.getControl(79).setVisible(False)
                 self.getControl(80).setVisible(False)
                 self.getControl(83).setVisible(False)
                 self.getControl(85).setVisible(False)
                 self.getControl(87).setVisible(False)
                 self.getControl(89).setVisible(False)
                 self.getControl(4003).setVisible(True)
                 self.getControl(204).setVisible(True)
                 self.getControl(205).setVisible(True)
                 self.getControl(4007).setVisible(True)
                 self.getControl(4008).setVisible(True)



     def View_Restrictions(self):
         pass



     def Remove_Buttons(self):
         #print "you are in Remove_Buttons"

         for program_buttons in self.remove_controls:
             self.removeControl(program_buttons)

         #remove the program buttons in the list
         #print "self.program"
         #print self.program


         #for program_controls in self.program_buttons:
         #for program_controls, program in zip(self.program_buttons, self.program):
             #self.program_buttons.append(ProgramControls(program_controls, program))
             #print self.program_buttons



     def System_Details(self):
         pass



     def Speed_Test(self):
         pass



     def GoBack(self):
         channels_1_yellow = xbmc.getCondVisibility('Control.IsVisible(347)')
         channels_2_yellow = xbmc.getCondVisibility('Control.IsVisible(355)')
         channels_3_yellow = xbmc.getCondVisibility('Control.IsVisible(356)')
         channels_4_yellow = xbmc.getCondVisibility('Control.IsVisible(357)')
         channels_5_yellow = xbmc.getCondVisibility('Control.IsVisible(358)')
         channels_6_yellow = xbmc.getCondVisibility('Control.IsVisible(359)')
         channels_7_yellow = xbmc.getCondVisibility('Control.IsVisible(360)')

         if channels_1_yellow == True:
             #disable the images from channel 1
             self.getControl(347).setVisible(False)
             self.getControl(361).setLabel('')
             self.getControl(368).setLabel('')


             #disable the images from channel 2
             self.getControl(348).setVisible(False)
             self.getControl(362).setLabel('')
             self.getControl(369).setLabel('')


             #disable the images from channel 3
             self.getControl(349).setVisible(False)
             self.getControl(363).setLabel('')
             self.getControl(370).setLabel('')


             #disable the images from channel 4
             self.getControl(350).setVisible(False)
             self.getControl(364).setLabel('')
             self.getControl(371).setLabel('')


             #disable the images from channel 5
             self.getControl(351).setVisible(False)
             self.getControl(365).setLabel('')
             self.getControl(372).setLabel('')


             #disable the images from channel 6
             self.getControl(352).setVisible(False)
             self.getControl(366).setLabel('')
             self.getControl(373).setLabel('')


             #disable the images from channel 7
             self.getControl(353).setVisible(False)
             self.getControl(367).setLabel('')
             self.getControl(374).setLabel('')



         elif channels_2_yellow == True:
             #disable the images from channel 1
             self.getControl(354).setVisible(False)
             self.getControl(368).setVisible(False)
             self.getControl(361).setVisible(True)
             self.getControl(368).setLabel('')
             self.getControl(361).setLabel('')


             #disable the images from channel 2
             self.getControl(355).setVisible(False)
             self.getControl(369).setVisible(False)
             self.getControl(369).setLabel('')
             self.getControl(362).setLabel('')
             self.getControl(362).setVisible(True)


             #disable the images from channel 3
             self.getControl(349).setVisible(False)
             self.getControl(363).setLabel('')
             self.getControl(370).setLabel('')


             #disable the images from channel 4
             self.getControl(350).setVisible(False)
             self.getControl(364).setLabel('')
             self.getControl(371).setLabel('')


             #disable the images from channel 5
             self.getControl(351).setVisible(False)
             self.getControl(365).setLabel('')
             self.getControl(372).setLabel('')


             #disable the images from channel 6
             self.getControl(352).setVisible(False)
             self.getControl(366).setLabel('')
             self.getControl(373).setLabel('')


             #disable the images from channel 7
             self.getControl(353).setVisible(False)
             self.getControl(367).setLabel('')
             self.getControl(374).setLabel('')



         elif channels_3_yellow == True:
             #disable the images from channel 1
             self.getControl(354).setVisible(False)
             self.getControl(368).setVisible(False)
             self.getControl(361).setVisible(True)
             self.getControl(368).setLabel('')
             self.getControl(361).setLabel('')


             #disable the images from channel 2
             self.getControl(348).setVisible(False)
             self.getControl(362).setLabel('')
             self.getControl(369).setLabel('')


             #disable the images from channel 3
             self.getControl(356).setVisible(False)
             self.getControl(370).setVisible(False)
             self.getControl(370).setLabel('')
             self.getControl(363).setLabel('')
             self.getControl(363).setVisible(True)


             #disable the images from channel 4
             self.getControl(350).setVisible(False)
             self.getControl(364).setLabel('')
             self.getControl(371).setLabel('')


             #disable the images from channel 5
             self.getControl(351).setVisible(False)
             self.getControl(365).setLabel('')
             self.getControl(372).setLabel('')


             #disable the images from channel 6
             self.getControl(352).setVisible(False)
             self.getControl(366).setLabel('')
             self.getControl(373).setLabel('')


             #disable the images from channel 7
             self.getControl(353).setVisible(False)
             self.getControl(367).setLabel('')
             self.getControl(374).setLabel('')



         elif channels_4_yellow == True:
             #disable the images from channel 1
             self.getControl(354).setVisible(False)
             self.getControl(368).setVisible(False)
             self.getControl(361).setVisible(True)
             self.getControl(368).setLabel('')
             self.getControl(361).setLabel('')


             #disable the images from channel 2
             self.getControl(348).setVisible(False)
             self.getControl(362).setLabel('')
             self.getControl(369).setLabel('')


             #disable the images from channel 3
             self.getControl(349).setVisible(False)
             self.getControl(363).setLabel('')
             self.getControl(370).setLabel('')


             #disable the images from channel 4
             self.getControl(357).setVisible(False)
             self.getControl(371).setVisible(False)
             self.getControl(371).setLabel('')
             self.getControl(364).setLabel('')
             self.getControl(364).setVisible(True)


             #disable the images from channel 5
             self.getControl(351).setVisible(False)
             self.getControl(365).setLabel('')
             self.getControl(372).setLabel('')


             #disable the images from channel 6
             self.getControl(352).setVisible(False)
             self.getControl(366).setLabel('')
             self.getControl(373).setLabel('')


             #disable the images from channel 7
             self.getControl(353).setVisible(False)
             self.getControl(367).setLabel('')
             self.getControl(374).setLabel('')



         elif channels_5_yellow == True:
             #disable the images from channel 1
             self.getControl(354).setVisible(False)
             self.getControl(368).setVisible(False)
             self.getControl(361).setVisible(True)
             self.getControl(368).setLabel('')
             self.getControl(361).setLabel('')


             #disable the images from channel 2
             self.getControl(348).setVisible(False)
             self.getControl(362).setLabel('')
             self.getControl(369).setLabel('')


             #disable the images from channel 3
             self.getControl(349).setVisible(False)
             self.getControl(363).setLabel('')
             self.getControl(370).setLabel('')


             #disable the images from channel 4
             self.getControl(350).setVisible(False)
             self.getControl(364).setLabel('')
             self.getControl(371).setLabel('')


             #disable the images from channel 5
             self.getControl(358).setVisible(False)
             self.getControl(372).setVisible(False)
             self.getControl(372).setLabel('')
             self.getControl(365).setLabel('')
             self.getControl(365).setVisible(True)


             #disable the images from channel 6
             self.getControl(352).setVisible(False)
             self.getControl(366).setLabel('')
             self.getControl(373).setLabel('')


             #disable the images from channel 7
             self.getControl(353).setVisible(False)
             self.getControl(367).setLabel('')
             self.getControl(374).setLabel('')



         elif channels_6_yellow == True:
             #disable the images from channel 1
             self.getControl(354).setVisible(False)
             self.getControl(368).setVisible(False)
             self.getControl(361).setVisible(True)
             self.getControl(368).setLabel('')
             self.getControl(361).setLabel('')


             #disable the images from channel 2
             self.getControl(348).setVisible(False)
             self.getControl(362).setLabel('')
             self.getControl(369).setLabel('')


             #disable the images from channel 3
             self.getControl(349).setVisible(False)
             self.getControl(363).setLabel('')
             self.getControl(370).setLabel('')


             #disable the images from channel 4
             self.getControl(350).setVisible(False)
             self.getControl(364).setLabel('')
             self.getControl(371).setLabel('')
             


             #disable the images from channel 5
             self.getControl(351).setVisible(False)
             self.getControl(365).setLabel('')
             self.getControl(372).setLabel('')


             #disable the images from channel 6
             self.getControl(359).setVisible(False)
             self.getControl(373).setVisible(False)
             self.getControl(373).setLabel('')
             self.getControl(366).setLabel('')
             self.getControl(366).setVisible(True)


             #disable the images from channel 7
             self.getControl(353).setVisible(False)
             self.getControl(367).setLabel('')
             self.getControl(374).setLabel('')



         elif channels_7_yellow == True:
             #disable the images from channel 1
             self.getControl(354).setVisible(False)
             self.getControl(368).setVisible(False)
             self.getControl(361).setVisible(True)
             self.getControl(368).setLabel('')
             self.getControl(361).setLabel('')


             #disable the images from channel 2
             self.getControl(348).setVisible(False)
             self.getControl(362).setLabel('')
             self.getControl(369).setLabel('')


             #disable the images from channel 3
             self.getControl(349).setVisible(False)
             self.getControl(363).setLabel('')
             self.getControl(370).setLabel('')


             #disable the images from channel 4
             self.getControl(350).setVisible(False)
             self.getControl(364).setLabel('')
             self.getControl(371).setLabel('')


             #disable the images from channel 5
             self.getControl(351).setVisible(False)
             self.getControl(365).setLabel('')
             self.getControl(372).setLabel('')


             #disable the images from channel 6
             self.getControl(352).setVisible(False)
             self.getControl(366).setLabel('')
             self.getControl(373).setLabel('')


             #disable the images from channel 7
             self.getControl(360).setVisible(False)
             self.getControl(374).setVisible(False)
             self.getControl(374).setLabel('')
             self.getControl(367).setLabel('')
             self.getControl(367).setVisible(True)



         #find all buttons in pixels area to disabled it
         for elem in self.program_buttons:
             pos_top = elem.control.getY()
             prog_id = elem.control.getId()

             #if int(pos_top) >= 315 and int(pos_top) <= 540:
                 #self.getControl(prog_id).setVisible(False)
         self.channels_Index = 0
         self.programs_Index = 0


         self.getControl(3).setVisible(True)
         self.getControl(5).setVisible(True)
         self.getControl(7).setVisible(True)
         self.getControl(9).setVisible(True)
         self.getControl(321).setVisible(False)
         self.getControl(344).setVisible(False)
         self.getControl(345).setVisible(False)
         self.getControl(346).setVisible(False)
         self.getControl(388).setVisible(False)
         self.getControl(375).setVisible(False)
         self.getControl(376).setVisible(False)
         self.getControl(377).setVisible(False)
         self.getControl(378).setVisible(False)
         self.getControl(379).setVisible(False)
         self.getControl(380).setVisible(False)
         self.getControl(381).setVisible(False)
         self.getControl(384).setVisible(False)
         self.getControl(385).setVisible(False)
         self.getControl(386).setVisible(False)


         #check if enable
         #cSetVisible(self,340,False)
         #cSetVisible(self,343,False)
         #self.getControl(343).setLabel('')

         #check if enable
         self.abortdownload()


         if self.move_up_flag == True:
             self.clearEPG()


         if self.move_down_flag == True:
             self.clearEPG()


         if self.channels_Index == 0:
             self.move_back_flag = True
             if self.move_back_flag == True:
                 self.clearEPG()




     def GoUp(self):
         channels_1_yellow = xbmc.getCondVisibility('Control.IsVisible(347)')
         channels_2_yellow = xbmc.getCondVisibility('Control.IsVisible(355)')
         channels_3_yellow = xbmc.getCondVisibility('Control.IsVisible(356)')
         channels_4_yellow = xbmc.getCondVisibility('Control.IsVisible(357)')
         channels_5_yellow = xbmc.getCondVisibility('Control.IsVisible(358)')
         channels_6_yellow = xbmc.getCondVisibility('Control.IsVisible(359)')
         channels_7_yellow = xbmc.getCondVisibility('Control.IsVisible(360)')
         path = 'special://home/addons/script.tvguide/resources/skins/Default/media/'
         print self.channelsOnLeft
         print self.channelsOnMiddle
         print self.channelsOnRight


         if channels_7_yellow == True:
             #set the image to blue
             self.getControl(360).setVisible(False)
             self.getControl(353).setVisible(True)

             #set the label to white
             self.getControl(374).setVisible(False)
             self.getControl(367).setVisible(True)

             #set the image to yellow
             self.getControl(352).setVisible(False)
             self.getControl(359).setVisible(True)

             #set the label to black
             self.getControl(366).setVisible(False)
             self.getControl(373).setVisible(True)


             self.channels_Index -= 1
             #self.programs_Index -= 69
             CurrentRowId = self.getFocusId()
             CurrentRowX = self.getControl(CurrentRowId).getX()
             CurrentRowY = self.getControl(CurrentRowId).getY()
             CurrentWidth = self.getControl(CurrentRowId).getWidth()

             program_button = [elem.control for elem in self.program_buttons]
             program_id = list()
             program_width = list()
             position_X = list()
             position_Y = list()
             for elem in program_button:
                 program_id.append(elem.getId())
                 program_width.append(elem.getWidth())
                 position_X.append(elem.getX())
                 position_Y.append(elem.getY())
             program_id = map(str, program_id)
             program_width = map(str, program_width)
             posX = map(str, position_X)
             posY = map(str, position_Y)


             #get each posX, posY and prog_id then move them up for each program button
             for pos_X, pos_Y, prog_width, prog_id in zip(position_X, position_Y, program_width, program_id):
                 if CurrentRowX == 375 and CurrentRowY == 541:
                     if CurrentWidth <= 691:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 503:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 503:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 375 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                             if pos_X == 724 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 503:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 503:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                 else:
                                     if pos_X == 375 and pos_Y == 503:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 724 and CurrentRowY == 541:
                     if CurrentWidth <= 691:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 503:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 503:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 503:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnMiddle == True:
                             if pos_X == 375 and pos_Y == 503:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 503:
                                 if prog_width >= 342:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 503:
                                     if prog_width >= 342:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 1072 and CurrentRowY == 541:
                     if CurrentWidth <= 691:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 503:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 503:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 503:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 503:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))



         elif channels_6_yellow == True:
             #set the image to blue
             self.getControl(359).setVisible(False)
             self.getControl(352).setVisible(True)

             #set the label to white
             self.getControl(373).setVisible(False)
             self.getControl(366).setVisible(True)

             #set the image to yellow
             self.getControl(351).setVisible(False)
             self.getControl(358).setVisible(True)

             #set the label to black
             self.getControl(365).setVisible(False)
             self.getControl(372).setVisible(True)


             self.channels_Index -= 1
             #self.programs_Index -= 69
             CurrentRowId = self.getFocusId()
             CurrentRowX = self.getControl(CurrentRowId).getX()
             CurrentRowY = self.getControl(CurrentRowId).getY()
             CurrentWidth = self.getControl(CurrentRowId).getWidth()

             program_button = [elem.control for elem in self.program_buttons]
             program_id = list()
             program_width = list()
             position_X = list()
             position_Y = list()
             for elem in program_button:
                 program_id.append(elem.getId())
                 program_width.append(elem.getWidth())
                 position_X.append(elem.getX())
                 position_Y.append(elem.getY())
             program_id = map(str, program_id)
             program_width = map(str, program_width)
             posX = map(str, position_X)
             posY = map(str, position_Y)


             #get each posX, posY and prog_id then move them up for each program button
             for pos_X, pos_Y, prog_width, prog_id in zip(position_X, position_Y, program_width, program_id):
                 if CurrentRowX == 375 and CurrentRowY == 503:
                     if CurrentWidth <= 691:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 466:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 466:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                     
                                 if pos_X == 375 and pos_Y == 466:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 466:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 466:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 466:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 724 and CurrentRowY == 503:
                     if CurrentWidth <= 691:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 466:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 466:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 466:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnMiddle == True:
                             if pos_X == 375 and pos_Y == 466:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 466:
                                 if prog_width >= 342:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 466:
                                     if prog_width >= 342:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 1072 and CurrentRowY == 503:
                     if CurrentWidth <= 691:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 466:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 466:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 466:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 466:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))



         elif channels_5_yellow == True:
             #set the image to blue
             self.getControl(358).setVisible(False)
             self.getControl(351).setVisible(True)

             #set the label to white
             self.getControl(372).setVisible(False)
             self.getControl(365).setVisible(True)

             #set the image to yellow
             self.getControl(350).setVisible(False)
             self.getControl(357).setVisible(True)

             #set the label to black
             self.getControl(364).setVisible(False)
             self.getControl(371).setVisible(True)


             self.channels_Index -= 1
             #self.programs_Index -= 69
             CurrentRowId = self.getFocusId()
             CurrentRowX = self.getControl(CurrentRowId).getX()
             CurrentRowY = self.getControl(CurrentRowId).getY()
             CurrentWidth = self.getControl(CurrentRowId).getWidth()

             program_button = [elem.control for elem in self.program_buttons]
             program_id = list()
             program_width = list()
             position_X = list()
             position_Y = list()
             for elem in program_button:
                 program_id.append(elem.getId())
                 program_width.append(elem.getWidth())
                 position_X.append(elem.getX())
                 position_Y.append(elem.getY())
             program_id = map(str, program_id)
             program_width = map(str, program_width)
             posX = map(str, position_X)
             posY = map(str, position_Y)


             #get each posX, posY and prog_id then move them up for each program button
             for pos_X, pos_Y, prog_width, prog_id in zip(position_X, position_Y, program_width, program_id):
                 if CurrentRowX == 375 and CurrentRowY == 466:
                     if CurrentWidth <= 691:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 428:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 428:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 428:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 428:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 428:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 428:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 724 and CurrentRowY == 466:
                     if CurrentWidth <= 691:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 428:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 428:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 428:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnMiddle == True:
                             if pos_X == 375 and pos_Y == 428:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 428:
                                 if prog_width >= 342:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 428:
                                     if prog_width >= 342:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 1072 and CurrentRowY == 466:
                     if CurrentWidth <= 691:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 428:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 428:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 428:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 428:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))



         elif channels_4_yellow == True:
             #set the image to blue
             self.getControl(357).setVisible(False)
             self.getControl(350).setVisible(True)

             #set the label to white
             self.getControl(371).setVisible(False)
             self.getControl(364).setVisible(True)

             #set the image to yellow
             self.getControl(349).setVisible(False)
             self.getControl(356).setVisible(True)

             #set the label to black
             self.getControl(363).setVisible(False)
             self.getControl(370).setVisible(True)


             self.channels_Index -= 1
             #self.programs_Index -= 69
             CurrentRowId = self.getFocusId()
             CurrentRowX = self.getControl(CurrentRowId).getX()
             CurrentRowY = self.getControl(CurrentRowId).getY()
             CurrentWidth = self.getControl(CurrentRowId).getWidth()

             program_button = [elem.control for elem in self.program_buttons]
             program_id = list()
             program_width = list()
             position_X = list()
             position_Y = list()
             for elem in program_button:
                 program_id.append(elem.getId())
                 program_width.append(elem.getWidth())
                 position_X.append(elem.getX())
                 position_Y.append(elem.getY())
             program_id = map(str, program_id)
             program_width = map(str, program_width)
             posX = map(str, position_X)
             posY = map(str, position_Y)


             #get each posX, posY and prog_id then move them up for each program button
             for pos_X, pos_Y, prog_width, prog_id in zip(position_X, position_Y, program_width, program_id):
                 if CurrentRowX == 375 and CurrentRowY == 428:
                     if CurrentWidth <= 691:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 391:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 391:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                             else:
                                 if pos_X == 375 and pos_Y == 391:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 391:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 391:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 391:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 724 and CurrentRowY == 428:
                     if CurrentWidth <= 691:
                         if self.channelsOnMiddle == True:
                             if pos_X == 375 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                             if pos_X == 724 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 391:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 391:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnMiddle == True:
                             if pos_X == 375 and pos_Y == 391:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 391:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 391:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 391:
                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 1072 and CurrentRowY == 428:
                     if CurrentWidth <= 691:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 391:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 391:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 391:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 391:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 391:
                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))



         elif channels_3_yellow == True:
             #set the image to blue
             self.getControl(356).setVisible(False)
             self.getControl(349).setVisible(True)

             #set the label to white
             self.getControl(370).setVisible(False)
             self.getControl(363).setVisible(True)

             #set the image to yellow
             self.getControl(348).setVisible(False)
             self.getControl(355).setVisible(True)

             #set the label to black
             self.getControl(362).setVisible(False)
             self.getControl(369).setVisible(True)


             self.channels_Index -= 1
             #self.programs_Index -= 69
             print "hello chris 3"
             CurrentRowId = self.getFocusId()
             CurrentRowX = self.getControl(CurrentRowId).getX()
             CurrentRowY = self.getControl(CurrentRowId).getY()
             CurrentWidth = self.getControl(CurrentRowId).getWidth()

             program_button = [elem.control for elem in self.program_buttons]
             program_id = list()
             program_width = list()
             position_X = list()
             position_Y = list()
             for elem in program_button:
                 program_id.append(elem.getId())
                 program_width.append(elem.getWidth())
                 position_X.append(elem.getX())
                 position_Y.append(elem.getY())
             program_id = map(str, program_id)
             program_width = map(str, program_width)
             posX = map(str, position_X)
             posY = map(str, position_Y)


             #get each posX, posY and prog_id then move them up for each program button
             for pos_X, pos_Y, prog_width, prog_id in zip(position_X, position_Y, program_width, program_id):
                 if CurrentRowX == 375 and CurrentRowY == 391:
                     if CurrentWidth <= 691:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 353:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 353:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 353:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 353:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 353:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 353:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 353:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 353:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 353:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 353:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 353:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 353:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 724 and CurrentRowY == 391:
                     if CurrentWidth <= 691:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 353:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 353:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 353:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 353:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 353:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnMiddle == True:
                             if pos_X == 375 and pos_Y == 353:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 353:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 353:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 353:
                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 1072 and CurrentRowY == 391:
                     if CurrentWidth <= 691:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 353:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 353:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 353:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 353:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 353:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 353:
                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))



         elif channels_2_yellow == True:
             #set the image to blue
             self.getControl(355).setVisible(False)
             self.getControl(348).setVisible(True)

             #set the label to white
             self.getControl(369).setVisible(False)
             self.getControl(362).setVisible(True)

             #set the image to yellow
             self.getControl(354).setVisible(False)
             self.getControl(347).setVisible(True)

             #set the label to black
             self.getControl(368).setVisible(False)
             self.getControl(361).setVisible(True)


             self.channels_Index -= 1
             #self.programs_Index -= 69
             CurrentRowId = self.getFocusId()
             CurrentRowX = self.getControl(CurrentRowId).getX()
             CurrentRowY = self.getControl(CurrentRowId).getY()
             CurrentWidth = self.getControl(CurrentRowId).getWidth()

             program_button = [elem.control for elem in self.program_buttons]
             program_id = list()
             program_width = list()
             position_X = list()
             position_Y = list()
             for elem in program_button:
                 program_id.append(elem.getId())
                 program_width.append(elem.getWidth())
                 position_X.append(elem.getX())
                 position_Y.append(elem.getY())
             program_id = map(str, program_id)
             program_width = map(str, program_width)
             posX = map(str, position_X)
             posY = map(str, position_Y)

             #get each posX, posY and prog_id then move them up for each program button
             for pos_X, pos_Y, prog_width, prog_id in zip(position_X, position_Y, program_width, program_id):
                 if CurrentRowX == 375 and CurrentRowY == 353:
                     if CurrentWidth <= 691:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 315:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 315:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 315:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 315:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 315:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 315:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 315:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 315:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 315:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 315:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 315:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 315:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 724 and CurrentRowY == 353:
                     if CurrentWidth <= 691:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 315:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 315:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 315:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 315:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 315:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 315:
                                 if prog_width >= 342:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 315:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 315:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 315:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 315:
                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 1072 and CurrentRowY == 353:
                     if CurrentWidth <= 691:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 315:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 315:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 315:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 315:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 315:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 315:
                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))



         elif channels_1_yellow == True:
             self.channels_Index -= 1
             #self.programs_Index -= 69

             try:
                 #get the programs list
                 profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
                 con = database.connect(profilePath)
                 cur = con.cursor()
                 cur.execute('SELECT DISTINCT channel FROM programs;')
                 channel = sorted(row[0] for row in cur.fetchall())
                 cur.execute('SELECT channel, title, start_date, stop_date FROM programs WHERE channel=?;', (channel[self.channels_Index],))
                 programs = cur.fetchall()
                 start_pos = 375    # indent for first program
                 channel = list()
                 positions_start = list()
                 positions_top = list()
                 programs_width = list()
                 programs_height = list()
                 programs_title = list()

                 for ind, row in enumerate(programs):
                     program = row[0].encode('ascii'), str(row[1]), str(row[2]), str(row[3])
                     channels = row[0].encode('ascii')
                     program_title = row[1].encode('ascii')
                     program_start_date = str(row[2])
                     program_end_date = str(row[3])

                     #convert the date formats into minutes
                     minutes_start = self.parseDateTimeToMinutesSinceEpoch(program_start_date)
                     minutes_end = self.parseDateTimeToMinutesSinceEpoch(program_end_date)
                     minutes_length = minutes_end - minutes_start
                     channel_index = self.channels_Index

                     program_length = minutes_length
                     program_notification = program
                     programs_top = 315
                     program_height = 33
                     program_gap = 3
                     position_start = start_pos
                     position_top = programs_top + channel_index * (program_height + program_gap + 1.5)


                     #create width size for program buttons
                     if program_length >= 0 and program_length <= 10:   #10 mins
                         program_width = 84
                     elif program_length > 10 and program_length <= 20:   #15 mins
                         program_width = 167
                     elif program_length > 20 and program_length <= 35:   #30 mins
                         program_width = 342
                     elif program_length > 40 and program_length <= 48:   #45 mins
                         program_width = 515
                     elif program_length >= 50 and program_length <= 70:   #1 hour
                         program_width = 691
                     elif program_length >= 75 and program_length <= 85:   #1 hour and 15 mins
                         program_width = 879
                     elif program_length >= 90 and program_length <= 105:   #1 hour and 30 mins
                         program_width =  1038
                     elif program_length > 100 and program_length <= 115:   #1 hour and 45 mins
                         program_width =  1209
                     elif program_length > 115 and program_length <= 125:   #2 hours
                         program_width =  1392
                     elif program_length > 120 and program_length <= 135:   #2 hours and 15 mins
                         program_width =  1563
                     elif program_length > 135 and program_length <= 155:   #2 hour and 30 mins
                         program_width = 1735
                     elif program_length > 150 and program_length <= 165:   #2 hour and 45 mins
                         program_width = 1906
                     elif program_length > 165 and program_length <= 185:   #3 hours
                         program_width = 2082
                     elif program_length > 180 and program_length <= 195:   #3 hours and 15 mins
                         program_width = 2253
                     elif program_length > 195 and program_length <= 210:   #3 hour and 30 mins
                         program_width = 2437
                     elif program_length > 210 and program_length <= 225:   #3 hour and 45 mins
                         program_width = 2608
                     elif program_length > 225 and program_length <= 240:   #4 hours
                         program_width = 2779
                     elif program_length > 240 and program_length <= 255:   #4 hours and 15 mins
                         program_width = 2779
                     elif program_length > 255 and program_length <= 270:   #4 hour and 30 mins
                         program_width = 3121
                     elif program_length > 270 and program_length <= 286:   #4 hour and 45 mins
                         program_width = 3292
                     elif program_length > 286 and program_length <= 300:   #5 hours
                         program_width = 3463
                     elif program_length > 300 and program_length <= 315:   #5 hours and 15 mins
                         program_width = 3634
                     elif program_length > 315 and program_length <= 330:   #5 hour and 30 mins
                         program_width = 3805
                     elif program_length > 330 and program_length <= 345:   #5 hour and 45 mins
                         program_width = 3976
                     elif program_length > 345 and program_length <= 360:   #6 hours
                         program_width = 4146
                     elif program_length > 360 and program_length <= 375:   #6 hours and 15 mins
                         program_width = 4317
                     elif program_length > 375 and program_length <= 390:   #6 hour and 30 mins
                         program_width = 4489
                     elif program_length > 390 and program_length <= 405:   #6 hour and 45 mins
                         program_width = 4660
                     elif program_length > 405 and program_length <= 420:   #7 hours
                         program_width = 4831
                     elif program_length > 420 and program_length <= 435:   #7 hours and 15 mins
                         program_width = 5002
                     elif program_length > 435 and program_length <= 450:   #7 hours and 30 mins
                         program_width = 5173
                     elif program_length > 435 and program_length <= 450:   #7 hour and 45 mins
                         program_width = 5344
                     elif program_length > 450 and program_length <= 480:   #8 hours
                         program_width = 5515

                     start_pos += program_width + 2 * program_gap + 1
                     position_top += 37.5

                     #extract the list of elements from the arrays
                     positions_start.append(position_start)
                     positions_top.append(position_top)
                     programs_width.append(program_width)
                     programs_height.append(program_height)
                     programs_title.append(program_title)
                 program_button = [elem.control for elem in self.program_buttons]
                 programs_id = list()
                 positions_X = list()
                 positions_Y = list()
                 for elem in program_button:
                     programs_id.append(elem.getId())
                     positions_X.append(elem.getX())
                     positions_Y.append(elem.getY())
                 programs_id = map(str, programs_id)
                 posX = map(str, positions_X)
                 posY = map(str, positions_Y)


                 #get each posX, posY and prog_id then move them up for each program button
                 for pos_X, pos_Y, prog_id in zip(positions_X, positions_Y, programs_id):

                     if int(pos_Y) == 541:
                         pos_Y = 577
                         pos_X = int(pos_X)
                         prog_id = int(prog_id)
                         self.getControl(int(prog_id)).setVisible(False)
                         self.getControl(prog_id).setPosition(int(pos_X), int(pos_Y))


                     if int(pos_Y) == 503:
                         pos_Y = 540
                         pos_X = int(pos_X)
                         prog_id = int(prog_id)
                         self.getControl(prog_id).setPosition(int(pos_X), int(pos_Y))


                     if int(pos_Y) == 466:
                         pos_Y = 502
                         pos_X = int(pos_X)
                         prog_id = int(prog_id)
                         self.getControl(prog_id).setPosition(int(pos_X), int(pos_Y))


                     if int(pos_Y) == 428:
                         pos_Y = 465
                         pos_X = int(pos_X)
                         prog_id = int(prog_id)
                         self.getControl(prog_id).setPosition(int(pos_X), int(pos_Y))


                     if int(pos_Y) == 391:
                         pos_Y = 427
                         pos_X = int(pos_X)
                         prog_id = int(prog_id)
                         self.getControl(prog_id).setPosition(int(pos_X), int(pos_Y))


                     if int(pos_Y) == 353:
                         pos_Y = 390
                         pos_X = int(pos_X)
                         prog_id = int(prog_id)
                         self.getControl(prog_id).setPosition(int(pos_X), int(pos_Y))


                     if int(pos_Y) == 315:
                         pos_Y = 352
                         pos_X = int(pos_X)
                         prog_id = int(prog_id)
                         self.getControl(prog_id).setPosition(int(pos_X), int(pos_Y))


                 channels_2 = self.getControl(361).getLabel()
                 channels_3 = self.getControl(362).getLabel()
                 channels_4 = self.getControl(363).getLabel()
                 channels_5 = self.getControl(364).getLabel()
                 channels_6 = self.getControl(365).getLabel()
                 channels_7 = self.getControl(366).getLabel()

                 #set the channels text
                 self.getControl(361).setLabel(channels)
                 self.getControl(368).setLabel(channels)
                 self.getControl(362).setLabel(channels_2)
                 self.getControl(369).setLabel(channels_2)
                 self.getControl(363).setLabel(channels_3)
                 self.getControl(370).setLabel(channels_3)
                 self.getControl(364).setLabel(channels_4)
                 self.getControl(371).setLabel(channels_3)
                 self.getControl(365).setLabel(channels_4)
                 self.getControl(372).setLabel(channels_5)
                 self.getControl(366).setLabel(channels_6)
                 self.getControl(373).setLabel(channels_6)
                 self.getControl(367).setLabel(channels_7)
                 self.getControl(374).setLabel(channels_7)

                 #set the image to blue
                 self.getControl(347).setVisible(False)
                 self.getControl(354).setVisible(True)

                 #set the label to white
                 self.getControl(361).setVisible(False)
                 self.getControl(368).setVisible(True)

                 #set the image to yellow
                 self.getControl(348).setVisible(False)
                 self.getControl(355).setVisible(True)

                 #set the label to black
                 self.getControl(362).setVisible(False)
                 self.getControl(369).setVisible(True)


                 #if the program width is greater than 1 then do something.
                 if program_width > 1:
                     for position_start, position_top, program_width, program_height, program_title in zip(positions_start, positions_top, programs_width, programs_height, programs_title):
                         program_title = '[B]' + program_title + '[/B]'
                         position_top = 315

                         program_controls = xbmcgui.ControlButton(
                             int(position_start),
                             int(position_top),
                             int(program_width),
                             int(program_height),
                             program_title,
                             focusTexture = self.path + self.button_focus, 
                             noFocusTexture = path + self.button_nofocus,
                             alignment=4,
                             textColor ='0xFFFFFFFF',
                             focusedColor ='0xFF000000'
                         )
                         self.program_buttons.append(ProgramControls(program_controls, program))


                         #create the program buttons
                         if self.program_buttons > 1:
                             self.addControl(program_controls)


                 if self.channels_Index >= 1:

                     #set the image to blue
                     self.getControl(355).setVisible(False)
                     self.getControl(348).setVisible(True)

                     #set the label to white
                     self.getControl(369).setVisible(False)
                     self.getControl(362).setVisible(True)

                     #set the image to yellow
                     self.getControl(354).setVisible(False)
                     self.getControl(347).setVisible(True)

                     #set the label to black
                     self.getControl(368).setVisible(False)
                     self.getControl(361).setVisible(True)


                 else:
                     #set the image to blue
                     self.getControl(355).setVisible(False)
                     self.getControl(348).setVisible(True)

                     #set the label to white
                     self.getControl(369).setVisible(False)
                     self.getControl(362).setVisible(True)

                     #set the image to yellow
                     self.getControl(354).setVisible(False)
                     self.getControl(347).setVisible(True)

                     #set the label to black
                     self.getControl(368).setVisible(False)
                     self.getControl(361).setVisible(True)


                 if self.channels_Index >= 0:
                     if self.channels_Index != 0:
                         self.setFocus(self.program_buttons[self.programs_Index].control)
                         print "fix this trouble"
                     else:
                         program_buttons = [elem.control for elem in self.program_buttons]
                         programs_id = list()
                         positions_X = list()
                         positions_Y = list()
                         for elem in program_buttons:
                             programs_id.append(elem.getId())
                             positions_X.append(elem.getX())
                             positions_Y.append(elem.getY())
                         programs_id = map(str, programs_id)
                         posX = map(str, positions_X)
                         posY = map(str, positions_Y)
                         #get each posX, posY and prog_id then move them up for each program button
                         for pos_X, pos_Y, prog_id in zip(positions_X, positions_Y, programs_id):
                             if int(pos_X) == 375 and int(pos_Y) == 315:
                                 self.setFocus(self.getControl(int(prog_id)))


                 if self.move_up_flag == False:
                     self.move_up_flag = True


             except:
                 pass




     def GoDown(self):
         channels_1_yellow = xbmc.getCondVisibility('Control.IsVisible(347)')
         channels_2_yellow = xbmc.getCondVisibility('Control.IsVisible(355)')
         channels_3_yellow = xbmc.getCondVisibility('Control.IsVisible(356)')
         channels_4_yellow = xbmc.getCondVisibility('Control.IsVisible(357)')
         channels_5_yellow = xbmc.getCondVisibility('Control.IsVisible(358)')
         channels_6_yellow = xbmc.getCondVisibility('Control.IsVisible(359)')
         channels_7_yellow = xbmc.getCondVisibility('Control.IsVisible(360)')
         path = 'special://home/addons/script.tvguide/resources/skins/Default/media/'

         CurrentRowId = self.getFocusId()
         CurrentRowX = self.getControl(CurrentRowId).getX()
         CurrentRowY = self.getControl(CurrentRowId).getY()
         CurrentWidth = self.getControl(CurrentRowId).getWidth()



         if channels_1_yellow == True:
             #set the image to blue
             self.getControl(347).setVisible(False)
             self.getControl(354).setVisible(True)

             #set the label to white
             self.getControl(361).setVisible(False)
             self.getControl(368).setVisible(True)

             #set the image to yellow
             self.getControl(348).setVisible(False)
             self.getControl(355).setVisible(True)

             #set the label to black
             self.getControl(362).setVisible(False)
             self.getControl(369).setVisible(True)

             self.channels_Index += 1
             #self.programs_Index += 69
             CurrentRowId = self.getFocusId()
             CurrentRowX = self.getControl(CurrentRowId).getX()
             CurrentRowY = self.getControl(CurrentRowId).getY()
             CurrentWidth = self.getControl(CurrentRowId).getWidth()

             program_button = [elem.control for elem in self.program_buttons]
             program_id = list()
             program_width = list()
             position_X = list()
             position_Y = list()
             for elem in program_button:
                 program_id.append(elem.getId())
                 program_width.append(elem.getWidth())
                 position_X.append(elem.getX())
                 position_Y.append(elem.getY())
             program_id = map(str, program_id)
             program_width = map(str, program_width)
             posX = map(str, position_X)
             posY = map(str, position_Y)


             #get each posX, posY and prog_id then move them up for each program button
             for pos_X, pos_Y, prog_width, prog_id in zip(position_X, position_Y, program_width, program_id):
                 if CurrentRowX == 375 and CurrentRowY == 315:
                     if CurrentWidth <= 691:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 353:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 353:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 353:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 353:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 353:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 353:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 353:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 724 and CurrentRowY == 315:
                     if CurrentWidth <= 691:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 353:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 353:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 353:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 353:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 353:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 353:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 353:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 353:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 353:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 1072 and CurrentRowY == 315:
                     if CurrentWidth <= 691:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 353:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                             else:
                                 if pos_X == 724 and pos_Y == 353:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 353:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 353:
                                 if prog_width >= 342:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 353:
                                     if prog_width >= 342:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 353:
                                         if prog_width >= 342:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

             self.channels_Index + 1
             #self.setFocus(self.program_buttons[self.programs_Index].control)


         elif channels_2_yellow == True:

             #set the image to blue
             self.getControl(355).setVisible(False)
             self.getControl(348).setVisible(True)

             #set the label to white
             self.getControl(369).setVisible(False)
             self.getControl(362).setVisible(True)

             #set the image to yellow
             self.getControl(349).setVisible(False)
             self.getControl(356).setVisible(True)

             #set the label to black
             self.getControl(363).setVisible(False)
             self.getControl(370).setVisible(True)


             self.channels_Index += 1
             #self.programs_Index += 69
             CurrentRowId = self.getFocusId()
             CurrentRowX = self.getControl(CurrentRowId).getX()
             CurrentRowY = self.getControl(CurrentRowId).getY()
             CurrentWidth = self.getControl(CurrentRowId).getWidth()

             program_button = [elem.control for elem in self.program_buttons]
             program_id = list()
             program_width = list()
             position_X = list()
             position_Y = list()
             for elem in program_button:
                 program_id.append(elem.getId())
                 program_width.append(elem.getWidth())
                 position_X.append(elem.getX())
                 position_Y.append(elem.getY())
             program_id = map(str, program_id)
             program_width = map(str, program_width)
             posX = map(str, position_X)
             posY = map(str, position_Y)


             #get each posX, posY and prog_id then move them up for each program button
             for pos_X, pos_Y, prog_width, prog_id in zip(position_X, position_Y, program_width, program_id):
                 if CurrentRowX == 375 and CurrentRowY == 353:
                     if CurrentWidth <= 691:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 724 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 391:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 391:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 391:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 391:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 391:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 724 and CurrentRowY == 353:
                     if CurrentWidth <= 691:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 391:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 391:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 391:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 391:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 391:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 391:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 391:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 391:
                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 1072 and CurrentRowY == 353:
                     if CurrentWidth <= 691:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                             else:
                                 if pos_X == 724 and pos_Y == 391:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 391:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 391:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 391:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 391:
                                         if prog_width >= 342:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

             #self.setFocus(self.program_buttons[self.programs_Index].control)



         elif channels_3_yellow == True:

             #set the image to blue
             self.getControl(356).setVisible(False)
             self.getControl(349).setVisible(True)

             #set the label to white
             self.getControl(370).setVisible(False)
             self.getControl(363).setVisible(True)

             #set the image to yellow
             self.getControl(350).setVisible(False)
             self.getControl(357).setVisible(True)

             #set the label to black
             self.getControl(364).setVisible(False)
             self.getControl(371).setVisible(True)


             self.channels_Index += 1
             #self.programs_Index += 69
             CurrentRowId = self.getFocusId()
             CurrentRowX = self.getControl(CurrentRowId).getX()
             CurrentRowY = self.getControl(CurrentRowId).getY()
             CurrentWidth = self.getControl(CurrentRowId).getWidth()

             program_button = [elem.control for elem in self.program_buttons]
             program_id = list()
             program_width = list()
             position_X = list()
             position_Y = list()
             for elem in program_button:
                 program_id.append(elem.getId())
                 program_width.append(elem.getWidth())
                 position_X.append(elem.getX())
                 position_Y.append(elem.getY())
             program_id = map(str, program_id)
             program_width = map(str, program_width)
             posX = map(str, position_X)
             posY = map(str, position_Y)


             #get each posX, posY and prog_id then move them up for each program button
             for pos_X, pos_Y, prog_width, prog_id in zip(position_X, position_Y, program_width, program_id):
                 if CurrentRowX == 375 and CurrentRowY == 391:
                     if CurrentWidth <= 691:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 342:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                                     
                             else:
                                 if pos_X == 724 and pos_Y == 428:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 428:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 428:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 428:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 428:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 428:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 724 and CurrentRowY == 391:
                     if CurrentWidth <= 691:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 428:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                             else:
                                 if pos_X == 724 and pos_Y == 428:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 428:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 428:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 428:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 428:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 428:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 428:
                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 1072 and CurrentRowY == 391:
                     if CurrentWidth <= 691:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 428:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 428:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 428:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 428:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 428:
                                         if prog_width >= 342:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

             #self.setFocus(self.program_buttons[self.programs_Index].control)



         elif channels_4_yellow == True:

             #set the image to blue
             self.getControl(357).setVisible(False)
             self.getControl(350).setVisible(True)

             #set the label to white
             self.getControl(371).setVisible(False)
             self.getControl(364).setVisible(True)

             #set the image to yellow
             self.getControl(351).setVisible(False)
             self.getControl(358).setVisible(True)

             #set the label to black
             self.getControl(365).setVisible(False)
             self.getControl(372).setVisible(True)


             self.channels_Index += 1
             #self.programs_Index += 69
             CurrentRowId = self.getFocusId()
             CurrentRowX = self.getControl(CurrentRowId).getX()
             CurrentRowY = self.getControl(CurrentRowId).getY()
             CurrentWidth = self.getControl(CurrentRowId).getWidth()

             program_button = [elem.control for elem in self.program_buttons]
             program_id = list()
             program_width = list()
             position_X = list()
             position_Y = list()
             for elem in program_button:
                 program_id.append(elem.getId())
                 program_width.append(elem.getWidth())
                 position_X.append(elem.getX())
                 position_Y.append(elem.getY())
             program_id = map(str, program_id)
             program_width = map(str, program_width)
             posX = map(str, position_X)
             posY = map(str, position_Y)


             #get each posX, posY and prog_id then move them up for each program button
             for pos_X, pos_Y, prog_width, prog_id in zip(position_X, position_Y, program_width, program_id):
                 if CurrentRowX == 375 and CurrentRowY == 428:
                     if CurrentWidth <= 691:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 466:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 466:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 466:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 466:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 466:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 466:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 724 and CurrentRowY == 428:
                     if CurrentWidth <= 691:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 466:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 466:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 466:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 466:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 466:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 466:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 466:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 466:
                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 1072 and CurrentRowY == 428:
                     if CurrentWidth <= 691:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 466:
                                 if prog_width >= 342:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 466:
                                     if prog_width >= 342:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 466:
                                         if prog_width >= 342:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                     if CurrentWidth >= 1038:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 466:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 466:
                                     if prog_width >= 342:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 466:
                                         if prog_width >= 342:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

             #self.setFocus(self.program_buttons[self.programs_Index].control)



         elif channels_5_yellow == True:

             #set the image to blue
             self.getControl(358).setVisible(False)
             self.getControl(351).setVisible(True)

             #set the label to white
             self.getControl(372).setVisible(False)
             self.getControl(365).setVisible(True)

             #set the image to yellow
             self.getControl(352).setVisible(False)
             self.getControl(359).setVisible(True)

             #set the label to black
             self.getControl(366).setVisible(False)
             self.getControl(373).setVisible(True)


             self.channels_Index += 1
             #self.programs_Index += 69
             CurrentRowId = self.getFocusId()
             CurrentRowX = self.getControl(CurrentRowId).getX()
             CurrentRowY = self.getControl(CurrentRowId).getY()
             CurrentWidth = self.getControl(CurrentRowId).getWidth()

             program_button = [elem.control for elem in self.program_buttons]
             program_id = list()
             program_width = list()
             position_X = list()
             position_Y = list()
             for elem in program_button:
                 program_id.append(elem.getId())
                 program_width.append(elem.getWidth())
                 position_X.append(elem.getX())
                 position_Y.append(elem.getY())
             program_id = map(str, program_id)
             program_width = map(str, program_width)
             posX = map(str, position_X)
             posY = map(str, position_Y)


             #get each posX, posY and prog_id then move them up for each program button
             for pos_X, pos_Y, prog_width, prog_id in zip(position_X, position_Y, program_width, program_id):
                 if CurrentRowX == 375 and CurrentRowY == 466:
                     if CurrentWidth <= 691:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 503:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 503:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 503:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 503:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 503:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 503:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 724 and CurrentRowY == 466:
                     if CurrentWidth <= 691:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 503:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 503:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 503:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 503:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 503:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 503:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 503:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 503:
                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 1072 and CurrentRowY == 466:
                     if CurrentWidth <= 691:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 503:
                                 if prog_width >= 342:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 503:
                                     if prog_width >= 342:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 503:
                                         if prog_width >= 342:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 503:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 503:
                                     if prog_width >= 342:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 503:
                                         if prog_width >= 342:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

             #self.setFocus(self.program_buttons[self.programs_Index].control)



         elif channels_6_yellow == True:

             #set the image to blue
             self.getControl(359).setVisible(False)
             self.getControl(352).setVisible(True)

             #set the label to white
             self.getControl(373).setVisible(False)
             self.getControl(366).setVisible(True)

             #set the image to yellow
             self.getControl(353).setVisible(False)
             self.getControl(360).setVisible(True)

             #set the label to black
             self.getControl(367).setVisible(False)
             self.getControl(374).setVisible(True)

             #self.programs_Index += 69
             CurrentRowId = self.getFocusId()
             CurrentRowX = self.getControl(CurrentRowId).getX()
             CurrentRowY = self.getControl(CurrentRowId).getY()
             CurrentWidth = self.getControl(CurrentRowId).getWidth()

             program_button = [elem.control for elem in self.program_buttons]
             program_id = list()
             program_width = list()
             position_X = list()
             position_Y = list()
             for elem in program_button:
                 program_id.append(elem.getId())
                 program_width.append(elem.getWidth())
                 position_X.append(elem.getX())
                 position_Y.append(elem.getY())
             program_id = map(str, program_id)
             program_width = map(str, program_width)
             posX = map(str, position_X)
             posY = map(str, position_Y)


             #get each posX, posY and prog_id then move them up for each program button
             for pos_X, pos_Y, prog_width, prog_id in zip(position_X, position_Y, program_width, program_id):
                 if CurrentRowX == 375 and CurrentRowY == 503:
                     if CurrentWidth <= 691:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 541:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 541:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 541:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 541:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 541:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 541:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnLeft == True:
                             if pos_X == 375 and pos_Y == 541:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 541:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 541:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 541:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                         elif self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 541:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 541:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 724 and CurrentRowY == 503:
                     if CurrentWidth <= 691:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 541:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 541:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 541:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 541:
                                     if prog_width <= 691:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))

                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 541:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                     if CurrentWidth >= 1038:
                         if self.channelsOnMiddle == True:
                             if pos_X == 724 and pos_Y == 541:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 375 and pos_Y == 541:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))


                         elif self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 541:
                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 541:
                                     if prog_width >= 1038:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 541:
                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                 if CurrentRowX == 1072 and CurrentRowY == 503:
                     if CurrentWidth <= 691:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 541:
                                 if prog_width >= 342:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 541:
                                     if prog_width >= 342:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 541:
                                         if prog_width >= 342:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                     if CurrentWidth >= 1038:
                         if self.channelsOnRight == True:
                             if pos_X == 1072 and pos_Y == 541:
                                 if prog_width <= 691:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))

                                 if prog_width >= 1038:
                                     program_id = int(prog_id)
                                     self.setFocus(self.getControl(program_id))
                             else:
                                 if pos_X == 724 and pos_Y == 541:
                                     if prog_width >= 342:
                                         program_id = int(prog_id)
                                         self.setFocus(self.getControl(program_id))
                                 else:
                                     if pos_X == 375 and pos_Y == 541:
                                         if prog_width >= 342:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

             #self.setFocus(self.program_buttons[self.programs_Index].control)



         elif self.channels_Index >= 6:

             self.channels_Index += 1
             #self.programs_Index += 69

             try:
                 #get the programs list
                 profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
                 con = database.connect(profilePath)
                 cur = con.cursor()
                 cur.execute('SELECT DISTINCT channel FROM programs;')
                 channel = sorted(row[0] for row in cur.fetchall())
                 cur.execute('SELECT channel, title, start_date, stop_date FROM programs WHERE channel=?;', (channel[self.channels_Index],))
                 programs = cur.fetchall()
                 start_pos = 375    # indent for first program
                 channel = list()
                 positions_start = list()
                 positions_top = list()
                 programs_width = list()
                 programs_height = list()
                 programs_title = list()

                 for ind, row in enumerate(programs):
                     program = row[0].encode('ascii'), str(row[1]), str(row[2]), str(row[3])
                     channels = row[0].encode('ascii')
                     program_title = row[1].encode('ascii')
                     program_start_date = str(row[2])
                     program_end_date = str(row[3])

                     #convert the date formats into minutes
                     minutes_start = self.parseDateTimeToMinutesSinceEpoch(program_start_date)
                     minutes_end = self.parseDateTimeToMinutesSinceEpoch(program_end_date)
                     minutes_length = minutes_end - minutes_start
                     channel_index = self.channels_Index

                     program_length = minutes_length
                     program_notification = program
                     programs_top = 315
                     program_height = 33
                     program_gap = 3
                     position_start = start_pos
                     position_top = programs_top + channel_index * (program_height + program_gap + 1.5)


                     #create width size for program buttons
                     if program_length >= 0 and program_length <= 10:   #10 mins
                         program_width = 84
                     elif program_length > 10 and program_length <= 20:   #15 mins
                         program_width = 167
                     elif program_length > 20 and program_length <= 35:   #30 mins
                         program_width = 342
                     elif program_length > 40 and program_length <= 48:   #45 mins
                         program_width = 515
                     elif program_length >= 50 and program_length <= 70:   #1 hour
                         program_width = 691
                     elif program_length >= 75 and program_length <= 85:   #1 hour and 15 mins
                         program_width = 879
                     elif program_length >= 90 and program_length <= 105:   #1 hour and 30 mins
                         program_width =  1038
                     elif program_length > 100 and program_length <= 115:   #1 hour and 45 mins
                         program_width =  1209
                     elif program_length > 115 and program_length <= 125:   #2 hours
                         program_width =  1392
                     elif program_length > 120 and program_length <= 135:   #2 hours and 15 mins
                         program_width =  1563
                     elif program_length > 135 and program_length <= 155:   #2 hour and 30 mins
                         program_width = 1735
                     elif program_length > 150 and program_length <= 165:   #2 hour and 45 mins
                         program_width = 1906
                     elif program_length > 165 and program_length <= 185:   #3 hours
                         program_width = 2082
                     elif program_length > 180 and program_length <= 195:   #3 hours and 15 mins
                         program_width = 2253
                     elif program_length > 195 and program_length <= 210:   #3 hour and 30 mins
                         program_width = 2437
                     elif program_length > 210 and program_length <= 225:   #3 hour and 45 mins
                         program_width = 2608
                     elif program_length > 225 and program_length <= 240:   #4 hours
                         program_width = 2779
                     elif program_length > 240 and program_length <= 255:   #4 hours and 15 mins
                         program_width = 2779
                     elif program_length > 255 and program_length <= 270:   #4 hour and 30 mins
                         program_width = 3121
                     elif program_length > 270 and program_length <= 286:   #4 hour and 45 mins
                         program_width = 3292
                     elif program_length > 286 and program_length <= 300:   #5 hours
                         program_width = 3463
                     elif program_length > 300 and program_length <= 315:   #5 hours and 15 mins
                         program_width = 3634
                     elif program_length > 315 and program_length <= 330:   #5 hour and 30 mins
                         program_width = 3805
                     elif program_length > 330 and program_length <= 345:   #5 hour and 45 mins
                         program_width = 3976
                     elif program_length > 345 and program_length <= 360:   #6 hours
                         program_width = 4146
                     elif program_length > 360 and program_length <= 375:   #6 hours and 15 mins
                         program_width = 4317
                     elif program_length > 375 and program_length <= 390:   #6 hour and 30 mins
                         program_width = 4489
                     elif program_length > 390 and program_length <= 405:   #6 hour and 45 mins
                         program_width = 4660
                     elif program_length > 405 and program_length <= 420:   #7 hours
                         program_width = 4831
                     elif program_length > 420 and program_length <= 435:   #7 hours and 15 mins
                         program_width = 5002
                     elif program_length > 435 and program_length <= 450:   #7 hours and 30 mins
                         program_width = 5173
                     elif program_length > 435 and program_length <= 450:   #7 hour and 45 mins
                         program_width = 5344
                     elif program_length > 450 and program_length <= 480:   #8 hours
                         program_width = 5515

                     start_pos += program_width + 2 * program_gap + 1
                     position_top -= 37.5

                     #extract the list of elements from the arrays
                     positions_start.append(position_start)
                     positions_top.append(position_top)
                     programs_width.append(program_width)
                     programs_height.append(program_height)
                     programs_title.append(program_title)
                 program_button = [elem.control for elem in self.program_buttons]
                 programs_id = list()
                 positions_X = list()
                 positions_Y = list()
                 for elem in program_button:
                     programs_id.append(elem.getId())
                     positions_X.append(elem.getX())
                     positions_Y.append(elem.getY())
                 programs_id = map(str, programs_id)
                 posX = map(str, positions_X)
                 posY = map(str, positions_Y)


                 #get each posX, posY and prog_id then move them up for each program button
                 for pos_X, pos_Y, prog_id in zip(positions_X, positions_Y, programs_id):

                     if int(pos_Y) == 315:
                         pos_Y = 278
                         pos_X = int(pos_X)
                         prog_id = int(prog_id)
                         self.getControl(int(prog_id)).setVisible(False)
                         self.getControl(prog_id).setPosition(int(pos_X), int(pos_Y))


                     if int(pos_Y) == 353:
                         pos_Y = 315
                         pos_X = int(pos_X)
                         prog_id = int(prog_id)
                         self.getControl(prog_id).setPosition(int(pos_X), int(pos_Y))


                     if int(pos_Y) == 391:
                         pos_Y = 352
                         pos_X = int(pos_X)
                         prog_id = int(prog_id)
                         self.getControl(prog_id).setPosition(int(pos_X), int(pos_Y))


                     if int(pos_Y) == 428:
                         pos_Y = 390
                         pos_X = int(pos_X)
                         prog_id = int(prog_id)
                         self.getControl(prog_id).setPosition(int(pos_X), int(pos_Y))


                     if int(pos_Y) == 466:
                         pos_Y = 427
                         pos_X = int(pos_X)
                         prog_id = int(prog_id)
                         self.getControl(prog_id).setPosition(int(pos_X), int(pos_Y))


                     if int(pos_Y) == 503:
                         pos_Y = 465
                         pos_X = int(pos_X)
                         prog_id = int(prog_id)
                         self.getControl(prog_id).setPosition(int(pos_X), int(pos_Y))


                     if int(pos_Y) == 541:
                         pos_Y = 502
                         pos_X = int(pos_X)
                         prog_id = int(prog_id)
                         self.getControl(prog_id).setPosition(int(pos_X), int(pos_Y))


                 #if self.move_down_flag == True:
                     #self.move_down_flag = False
                     #remove existing controls
                     #self.clearEPG()


                 channels_2 = self.getControl(362).getLabel()
                 channels_3 = self.getControl(363).getLabel()
                 channels_4 = self.getControl(364).getLabel()
                 channels_5 = self.getControl(365).getLabel()
                 channels_6 = self.getControl(366).getLabel()
                 channels_7 = self.getControl(367).getLabel()

                 #set the channels text
                 self.getControl(361).setLabel(channels_2)
                 self.getControl(368).setLabel(channels_2)
                 self.getControl(362).setLabel(channels_3)
                 self.getControl(369).setLabel(channels_3)
                 self.getControl(363).setLabel(channels_4)
                 self.getControl(370).setLabel(channels_4)
                 self.getControl(364).setLabel(channels_5)
                 self.getControl(371).setLabel(channels_5)
                 self.getControl(365).setLabel(channels_6)
                 self.getControl(372).setLabel(channels_6)
                 self.getControl(366).setLabel(channels_7)
                 self.getControl(373).setLabel(channels_7)
                 self.getControl(367).setLabel(channels)
                 self.getControl(374).setLabel(channels)

                 #set the image to blue
                 self.getControl(360).setVisible(False)
                 self.getControl(353).setVisible(True)

                 #set the label to white
                 self.getControl(374).setVisible(False)
                 self.getControl(367).setVisible(True)

                 #set the image to yellow
                 self.getControl(352).setVisible(False)
                 self.getControl(359).setVisible(True)

                 #set the label to black
                 self.getControl(366).setVisible(False)
                 self.getControl(373).setVisible(True)


                 #if the program width is greater than 1 then do something.
                 if program_width > 1:
                     for position_start, position_top, program_width, program_height, program_title in zip(positions_start, positions_top, programs_width, programs_height, programs_title):
                         program_title = '[B]' + program_title + '[/B]'
                         position_top = 540

                         program_controls = xbmcgui.ControlButton(
                             int(position_start),
                             int(position_top),
                             int(program_width),
                             int(program_height),
                             program_title,
                             focusTexture = self.path + self.button_focus, 
                             noFocusTexture = path + self.button_nofocus,
                             alignment=4,
                             textColor ='0xFFFFFFFF',
                             focusedColor ='0xFF000000'
                         )
                         self.program_buttons.append(ProgramControls(program_controls, program))


                         #create the program buttons
                         if self.program_buttons > 1:
                             self.addControl(program_controls)


                 #get the program buttons after when the buttons have been added
                 programs_button = [elem.control for elem in self.program_buttons]
                 program_id = list()
                 position_X = list()
                 position_Y = list()
                 for elem in programs_button:
                     program_id.append(elem.getId())
                     position_X.append(elem.getX())
                     position_Y.append(elem.getY())
                 program_id = map(str, program_id)
                 pos_X = map(str, position_X)
                 pos_Y = map(str, position_Y)


                 if self.channels_Index >= 7:

                     #set the image to blue
                     self.getControl(359).setVisible(False)
                     self.getControl(352).setVisible(True)

                     #set the label to white
                     self.getControl(373).setVisible(False)
                     self.getControl(366).setVisible(True)

                     #set the image to yellow
                     self.getControl(353).setVisible(False)
                     self.getControl(360).setVisible(True)

                     #set the label to black
                     self.getControl(367).setVisible(False)
                     self.getControl(374).setVisible(True)

                     #get each posX, posY and prog_id then move them up for each program button
                     for pos_X, pos_Y, prog_width, prog_id in zip(position_X, position_Y, program_width, program_id):
                         if CurrentRowX == 375 and CurrentRowY == 541:
                             if CurrentWidth <= 691:
                                 if self.channelsOnLeft == True:
                                     if pos_X == 724 and pos_Y == 541:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))
                                     else:
                                         if pos_X == 375 and pos_Y == 541:
                                             if prog_width <= 691:
                                                 program_id = int(prog_id)
                                                 self.setFocus(self.getControl(program_id))

                                             if prog_width >= 1038:
                                                 program_id = int(prog_id)
                                                 self.setFocus(self.getControl(program_id))


                                 elif self.channelsOnRight == True:
                                     if pos_X == 1072 and pos_Y == 541:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))
                                     else:
                                         if pos_X == 724 and pos_Y == 541:
                                             if prog_width <= 691:
                                                 program_id = int(prog_id)
                                                 self.setFocus(self.getControl(program_id))

                                             if prog_width >= 1038:
                                                 program_id = int(prog_id)
                                                 self.setFocus(self.getControl(program_id))
                                         else:
                                             if pos_X == 375 and pos_Y == 541:
                                                 if prog_width <= 691:
                                                     program_id = int(prog_id)
                                                     self.setFocus(self.getControl(program_id))

                                                 if prog_width >= 1038:
                                                     program_id = int(prog_id)
                                                     self.setFocus(self.getControl(program_id))


                             if CurrentWidth >= 1038:
                                 if self.channelsOnLeft == True:
                                     if pos_X == 375 and pos_Y == 541:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))


                                 elif self.channelsOnRight == True:
                                     if pos_X == 1072 and pos_Y == 541:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))
                                     else:
                                         if pos_X == 724 and pos_Y == 391:
                                             if prog_width <= 691:
                                                 program_id = int(prog_id)
                                                 self.setFocus(self.getControl(program_id))

                                             if prog_width >= 1038:
                                                 program_id = int(prog_id)
                                                 self.setFocus(self.getControl(program_id))
                                         else:
                                             if pos_X == 375 and pos_Y == 391:
                                                 if prog_width <= 691:
                                                     program_id = int(prog_id)
                                                     self.setFocus(self.getControl(program_id))

                                                 if prog_width >= 1038:
                                                     program_id = int(prog_id)
                                                     self.setFocus(self.getControl(program_id))


                         if CurrentRowX == 724 and CurrentRowY == 541:
                             if CurrentWidth <= 691:
                                 if self.channelsOnMiddle == True:
                                     if pos_X == 724 and pos_Y == 541:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))
                                     else:
                                         if pos_X == 375 and pos_Y == 541:
                                             if prog_width <= 691:
                                                 program_id = int(prog_id)
                                                 self.setFocus(self.getControl(program_id))

                                             if prog_width >= 1038:
                                                 program_id = int(prog_id)
                                                 self.setFocus(self.getControl(program_id))


                                 elif self.channelsOnRight == True:
                                     if pos_X == 1072 and pos_Y == 353:
                                         if prog_width <= 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))
                                     else:
                                         if pos_X == 724 and pos_Y == 353:
                                             if prog_width <= 691:
                                                 program_id = int(prog_id)
                                                 self.setFocus(self.getControl(program_id))

                                             if prog_width >= 1038:
                                                 program_id = int(prog_id)
                                                 self.setFocus(self.getControl(program_id))
                                         else:
                                             if pos_X == 375 and pos_Y == 353:
                                                 if prog_width <= 691:
                                                     program_id = int(prog_id)
                                                     self.setFocus(self.getControl(program_id))

                                                 if prog_width >= 1038:
                                                     program_id = int(prog_id)
                                                     self.setFocus(self.getControl(program_id))


                             if CurrentWidth >= 1038:
                                 if self.channelsOnMiddle == True:
                                     if pos_X == 724 and pos_Y == 353:
                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))
                                     else:
                                         if pos_X == 375 and pos_Y == 353:
                                             if prog_width >= 1038:
                                                 program_id = int(prog_id)
                                                 self.setFocus(self.getControl(program_id))


                                 elif self.channelsOnRight == True:
                                     if pos_X == 1072 and pos_Y == 541:
                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))
                                     else:
                                         if pos_X == 724 and pos_Y == 541:
                                             if prog_width >= 1038:
                                                 program_id = int(prog_id)
                                                 self.setFocus(self.getControl(program_id))
                                         else:
                                             if pos_X == 375 and pos_Y == 541:
                                                 if prog_width >= 1038:
                                                     program_id = int(prog_id)
                                                     self.setFocus(self.getControl(program_id))


                         if CurrentRowX == 1072 and CurrentRowY == 541:
                             if CurrentWidth <= 691:
                                 if self.channelsOnRight == True:
                                     if pos_X == 1072 and pos_Y == 541:
                                         if prog_width >= 342:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))
                                     else:
                                         if pos_X == 724 and pos_Y == 541:
                                             if prog_width >= 342:
                                                 program_id = int(prog_id)
                                                 self.setFocus(self.getControl(program_id))
                                         else:
                                             if pos_X == 375 and pos_Y == 541:
                                                 if prog_width >= 342:
                                                     program_id = int(prog_id)
                                                     self.setFocus(self.getControl(program_id))


                             if CurrentWidth >= 1038:
                                 if self.channelsOnRight == True:
                                     if pos_X == 1072 and pos_Y == 541:
                                         if prog_width == 691:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))

                                         if prog_width >= 1038:
                                             program_id = int(prog_id)
                                             self.setFocus(self.getControl(program_id))
                                     else:
                                         if pos_X == 724 and pos_Y == 541:
                                             if prog_width >= 342:
                                                 program_id = int(prog_id)
                                                 self.setFocus(self.getControl(program_id))
                                         else:
                                             if pos_X == 375 and pos_Y == 541:
                                                 if prog_width >= 342:
                                                     program_id = int(prog_id)
                                                     self.setFocus(self.getControl(program_id))

                     #self.setFocus(self.program_buttons[self.programs_Index].control)

                 if self.move_down_flag == False:
                     self.move_down_flag = True


             except:
                 pass




     def GoLeft(self):
         CurrentRowID = self.getFocusId()
         CurrentRow = self.getControl(CurrentRowID).getX()
         CurrentRowY = self.getControl(CurrentRowID).getY()
         CurrentWidth = self.getControl(CurrentRowID).getWidth()
         print "CurrentRowID is " + str(CurrentRowID)
         print "CurrentRow is " + str(CurrentRow)
         print "CurrentRowY is " + str(CurrentRowY)
         print "CurrentWidth is " + str(CurrentWidth)



         #if channels page is equal or greater than 75
         if self.channel_page >= 75:
             if self.previous_program == True:
                 if CurrentWidth >= 691:
                     self.previous_program = False
                     self.programs_Index_flag = False
                 #else:
                     #self.move_right_flag = True


             if CurrentRow == 375:
                 if self.channel_page >= 0:
                     # Set the date and time row
                     getTime1 = self.getControl(344)
                     getTime2 = self.getControl(345)
                     getTime3 = self.getControl(346)
                     getTime3.setLabel(getTime2.getLabel())
                     getTime2.setLabel(getTime1.getLabel())
                     getTime1 = self.getControl(344).getLabel()
                     hour = time.strftime("%I").lstrip('0')

                     #Find the time for each clock to change the text
                     if getTime1 == '12:00AM':
                         self.getControl(344).setLabel('11:30PM')
                     elif getTime1 == '12:30AM':
                         self.getControl(344).setLabel('12:00AM')
                     elif getTime1 == '1:00AM':
                         self.getControl(344).setLabel('12:30AM')
                     elif getTime1 == '1:30AM':
                         self.getControl(344).setLabel('1:00AM')
                     elif getTime1 == '2:00AM':
                         self.getControl(344).setLabel('1:30AM')
                     elif getTime1 == '2:30AM':
                         self.getControl(344).setLabel('2:00AM')
                     elif getTime1 == '3:00AM':
                         self.getControl(344).setLabel('2:30AM')
                     elif getTime1 == '3:30AM':
                         self.getControl(344).setLabel('3:00AM')
                     elif getTime1 == '4:00AM':
                         self.getControl(344).setLabel('3:30AM')
                     elif getTime1 == '4:30AM':
                         self.getControl(344).setLabel('4:00AM')
                     elif getTime1 == '5:00AM':
                         self.getControl(344).setLabel('4:30AM')
                     elif getTime1 == '5:30AM':
                         self.getControl(344).setLabel('5:00AM')
                     elif getTime1 == '6:00AM':
                         self.getControl(344).setLabel('5:30AM')
                     elif getTime1 == '6:30AM':
                         self.getControl(344).setLabel('6:00AM')
                     elif getTime1 == '7:00AM':
                         self.getControl(344).setLabel('6:30AM')
                     elif getTime1 == '7:30AM':
                         self.getControl(344).setLabel('7:00AM')
                     elif getTime1 == '8:00AM':
                         self.getControl(344).setLabel('7:30AM')
                     elif getTime1 == '8:30AM':
                         self.getControl(344).setLabel('8:00AM')
                     elif getTime1 == '9:00AM':
                         self.getControl(344).setLabel('8:30AM')
                     elif getTime1 == '9:30AM':
                         self.getControl(344).setLabel('9:00AM')
                     elif getTime1 == '10:00AM':
                         self.getControl(344).setLabel('9:30AM')
                     elif getTime1 == '10:30AM':
                         self.getControl(344).setLabel('10:00AM')
                     elif getTime1 == '11:00AM':
                         self.getControl(344).setLabel('10:30AM')
                     elif getTime1 == '11:30AM':
                         self.getControl(344).setLabel('11:00AM')
                     elif getTime1 == '12:00PM':
                         self.getControl(344).setLabel('11:30AM')
                     elif getTime1 == '12:30PM':
                         self.getControl(344).setLabel('12:00PM')
                     elif getTime1 == '1:00PM':
                         self.getControl(344).setLabel('12:30PM')
                     elif getTime1 == '1:30PM':
                         self.getControl(344).setLabel('1:00PM')
                     elif getTime1 == '2:00PM':
                         self.getControl(344).setLabel('1:30PM')
                     elif getTime1 == '2:30PM':
                         self.getControl(344).setLabel('2:00PM')
                     elif getTime1 == '3:00PM':
                         self.getControl(344).setLabel('2:30PM')
                     elif getTime1 == '3:30PM':
                         self.getControl(344).setLabel('3:00PM')
                     elif getTime1 == '4:00PM':
                         self.getControl(344).setLabel('3:30PM')
                     elif getTime1 == '4:30PM':
                         self.getControl(344).setLabel('4:00PM')
                     elif getTime1 == '5:00PM':
                         self.getControl(344).setLabel('4:30PM')
                     elif getTime1 == '5:30PM':
                         self.getControl(344).setLabel('5:00PM')
                     elif getTime1 == '6:00PM':
                         self.getControl(344).setLabel('5:30PM')
                     elif getTime1 == '6:30PM':
                         self.getControl(344).setLabel('6:00PM')
                     elif getTime1 == '7:00PM':
                         self.getControl(344).setLabel('6:30PM')
                     elif getTime1 == '7:30PM':
                         self.getControl(344).setLabel('7:00PM')
                     elif getTime1 == '8:00PM':
                         self.getControl(344).setLabel('7:30PM')
                     elif getTime1 == '8:30PM':
                         self.getControl(344).setLabel('8:00PM')
                     elif getTime1 == '9:00PM':
                         self.getControl(344).setLabel('8:30PM')
                     elif getTime1 == '9:30PM':
                         self.getControl(344).setLabel('9:00PM')
                     elif getTime1 == '10:00PM':
                         self.getControl(344).setLabel('9:30PM')
                     elif getTime1 == '10:30PM':
                         self.getControl(344).setLabel('10:00PM')
                     elif getTime1 == '11:00PM':
                         self.getControl(344).setLabel('10:30PM')
                     elif getTime1 == '11:30PM':
                         self.getControl(344).setLabel('11:00PM')


             # change program controls to display the proper junks
             if self.channels_Index != len(self.program_buttons) - 1:
                 if CurrentRow == 375:
                     if self.channel_page >= 75:
                         program_button = [elem.control for elem in self.program_buttons]
                         programs_id = list()
                         program_width = list()
                         positions_X = list()
                         positions_Y = list()

                         for elem in program_button:
                             programs_id.append(elem.getId())
                             positions_X.append(elem.getX())
                             positions_Y.append(elem.getY())
                             program_width.append(elem.getWidth())
                             programs_id = map(str, programs_id)
                         posX = map(str, positions_X)
                         posY = map(str, positions_Y)
                         program_width = map(str, program_width)

                         #get access to the database
                         profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
                         con = database.connect(profilePath)
                         cur = con.cursor()
                         buttonList = list()
                         buttonWidthList = list()

                         for pos_X, pos_Y, prog_id, prog_width in zip(positions_X, positions_Y, programs_id, program_width):
                             if int(pos_X) == 375 and int(prog_width) == 343:
                                 cur.execute('SELECT button_ids, button_width FROM buttons where button_ids=?', [prog_id])
                                 buttons = cur.fetchall()

                                 for ind, row in enumerate(buttons):
                                     program_id = str(row[0])
                                     program_width = str(row[1])

                                     if int(program_width) != int(prog_width):
                                         self.getControl(int(program_id)).setWidth(692)
                                     else:
                                         self.move_left_flag = True


                             elif int(pos_X) == 375 and int(prog_width) == 691:
                                 cur.execute('SELECT button_ids, button_width FROM buttons where button_ids=?', [prog_id])
                                 buttons = cur.fetchall()

                                 for ind, row in enumerate(buttons):
                                     program_id = str(row[0])
                                     program_width = str(row[1])

                                     if int(program_width) != int(prog_width):
                                         self.getControl(int(program_id)).setWidth(1038)
                                     else:
                                         self.move_left_flag = True


                             elif int(pos_X) == 375 and int(prog_width) == 1038:
                                 cur.execute('SELECT button_ids, button_width FROM buttons where button_ids=?', [prog_id])
                                 buttons = cur.fetchall()

                                 for ind, row in enumerate(buttons):
                                     program_id = str(row[0])
                                     program_width = str(row[1])

                                     if int(program_width) != int(prog_width):
                                         self.getControl(int(program_id)).setWidth(1392)
                                         self.getControl(int(program_id)).setPosition(375, int(pos_Y))
                                     else:
                                         self.move_left_flag = True


                             elif int(pos_X) == 375 and int(prog_width) == 1425:
                                 programs_width = 1038
                                 self.getControl(int(prog_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 1392:
                                 cur.execute('SELECT button_ids, button_width FROM buttons where button_ids=?', [prog_id])
                                 buttons = cur.fetchall()

                                 for ind, row in enumerate(buttons):
                                     program_id = str(row[0])
                                     program_width = str(row[1])

                                     if int(program_width) != int(prog_width):
                                         self.getControl(int(program_id)).setWidth(1735)
                                     else:
                                         self.move_left_flag = True


                             elif int(pos_X) == 375 and int(prog_width) == 1735:
                                 cur.execute('SELECT button_ids, button_width FROM buttons where button_ids=?', [prog_id])
                                 buttons = cur.fetchall()

                                 for ind, row in enumerate(buttons):
                                     program_id = str(row[0])
                                     program_width = str(row[1])

                                     if int(program_width) != int(prog_width):
                                         self.getControl(int(prog_id)).setWidth(2082)
                                         self.getControl(int(program_id)).setPosition(375, int(pos_Y))
                                     else:
                                         self.getControl(int(prog_id)).setPosition(724, int(pos_Y))
                                         previousprogram = int(CurrentRowID) - 1
                                         self.getControl(int(previousprogram)).setPosition(375, int(pos_Y))
                                         self.getControl(int(previousprogram)).setVisible(True)
                                         CurrentRowX = self.getControl(int(previousprogram)).getX()
                                         CurrentWidth = self.getControl(int(previousprogram)).getWidth()

                                         if CurrentRowX == 375 and CurrentWidth == 1735:
                                             print "WE DO NEED THIS"
                                             self.programs_Index_flag = True


                             elif int(pos_X) == 375 and int(prog_width) == 2082:
                                 cur.execute('SELECT button_ids, button_width FROM buttons where button_ids=?', [prog_id])
                                 buttons = cur.fetchall()

                                 for ind, row in enumerate(buttons):
                                     program_id = str(row[0])
                                     program_width = str(row[1])

                                     if int(program_width) != int(prog_width):
                                         self.getControl(int(prog_id)).setWidth(2437)
                                     else:
                                         self.move_left_flag = True


                             elif int(pos_X) == 375 and int(prog_width) == 2437:
                                 cur.execute('SELECT button_ids, button_width FROM buttons where button_ids=?', [prog_id])
                                 buttons = cur.fetchall()

                                 for ind, row in enumerate(buttons):
                                     program_id = str(row[0])
                                     program_width = str(row[1])

                                     if int(program_width) != int(prog_width):
                                         self.getControl(int(prog_id)).setWidth(2779)
                                     else:
                                         self.move_left_flag = True


                             elif int(pos_X) == 375 and int(prog_width) == 2779:
                                 cur.execute('SELECT button_ids, button_width FROM buttons where button_ids=?', [prog_id])
                                 buttons = cur.fetchall()

                                 for ind, row in enumerate(buttons):
                                     program_id = str(row[0])
                                     program_width = str(row[1])

                                     if int(program_width) != int(prog_width):
                                         self.getControl(int(prog_id)).setWidth(3121)
                                     else:
                                         self.move_left_flag = True


                             elif int(pos_X) == 375 and int(prog_width) == 3121:
                                 cur.execute('SELECT button_ids, button_width FROM buttons where button_ids=?', [prog_id])
                                 buttons = cur.fetchall()

                                 for ind, row in enumerate(buttons):
                                     program_id = str(row[0])
                                     program_width = str(row[1])

                                     if int(program_width) != int(prog_width):
                                         self.getControl(int(prog_id)).setWidth(3463)
                                     else:
                                         self.move_left_flag = True


                             elif int(pos_X) == 375 and int(prog_width) == 3463:
                                 cur.execute('SELECT button_ids, button_width FROM buttons where button_ids=?', [prog_id])
                                 buttons = cur.fetchall()

                                 for ind, row in enumerate(buttons):
                                     program_id = str(row[0])
                                     program_width = str(row[1])

                                     if int(program_width) != int(prog_width):
                                         self.getControl(int(prog_id)).setWidth(3805)
                                     else:
                                         self.move_left_flag = True


                             elif int(pos_X) == 375 and int(prog_width) == 3805:
                                 cur.execute('SELECT button_ids, button_width FROM buttons where button_ids=?', [prog_id])
                                 buttons = cur.fetchall()

                                 for ind, row in enumerate(buttons):
                                     program_id = str(row[0])
                                     program_width = str(row[1])

                                     if int(program_width) != int(prog_width):
                                         self.getControl(int(prog_id)).setWidth(4146)
                                     else:
                                         self.move_left_flag = True


                             elif int(pos_X) == 375 and int(prog_width) == 4146:
                                 cur.execute('SELECT button_ids, button_width FROM buttons where button_ids=?', [prog_id])
                                 buttons = cur.fetchall()

                                 for ind, row in enumerate(buttons):
                                     program_id = str(row[0])
                                     program_width = str(row[1])

                                     if int(program_width) != int(prog_width):
                                         self.getControl(int(prog_id)).setWidth(4489)
                                     else:
                                         self.move_left_flag = True


                             elif int(pos_X) == 375 and int(prog_width) == 4489:
                                 cur.execute('SELECT button_ids, button_width FROM buttons where button_ids=?', [prog_id])
                                 buttons = cur.fetchall()

                                 for ind, row in enumerate(buttons):
                                     program_id = str(row[0])
                                     program_width = str(row[1])

                                     if int(program_width) != int(prog_width):
                                         self.getControl(int(prog_id)).setWidth(4831)
                                     else:
                                         self.move_left_flag = True


                             elif int(pos_X) == 375 and int(prog_width) == 4831:
                                 cur.execute('SELECT button_ids, button_width FROM buttons where button_ids=?', [prog_id])
                                 buttons = cur.fetchall()

                                 for ind, row in enumerate(buttons):
                                     program_id = str(row[0])
                                     program_width = str(row[1])

                                     if int(program_width) != int(prog_width):
                                         self.getControl(int(prog_id)).setWidth(5173)
                                     else:
                                         self.move_left_flag = True


                             elif int(pos_X) == 375 and int(prog_width) == 5173:
                                 cur.execute('SELECT button_ids, button_width FROM buttons where button_ids=?', [prog_id])
                                 buttons = cur.fetchall()

                                 for ind, row in enumerate(buttons):
                                     program_id = str(row[0])
                                     program_width = str(row[1])

                                     if int(program_width) != int(prog_width):
                                         self.getControl(int(prog_id)).setWidth(5515)
                                     else:
                                         self.move_left_flag = True


                             elif int(pos_X) == 724 and int(prog_width) >= 342:
                                 self.getControl(int(prog_id)).setPosition(1072, int(pos_Y))



                             elif int(pos_X) == 1072 and int(prog_width) >= 342:
                                 self.getControl(int(prog_id)).setVisible(False)
                                 self.getControl(int(prog_id)).setPosition(1423, int(pos_Y))
                                 currentprogram = int(prog_id) - 1
                                 currentprogram_width = self.getControl(int(currentprogram)).getWidth()
                                 currentprogramX = self.getControl(int(currentprogram)).getX()

                                 if currentprogram_width == 691:
                                     if currentprogramX == 375:
                                         if self.channel_page <= 75:
                                             nextprogram = int(currentprogram) + 1
                                             self.getControl(int(nextprogram)).setPosition(1072, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(True)


                             if self.move_left_flag == True:
                                 cur.execute('SELECT button_ids, button_width FROM buttons where button_ids=?', [prog_id])
                                 buttons = cur.fetchall()

                                 for ind, row in enumerate(buttons):
                                     program_id = str(row[0])
                                     program_width = str(row[1])

                                     if CurrentRow == 375 and CurrentWidth >= 1038:
                                         if self.channel_page > 75:
                                             if CurrentWidth != int(program_width):
                                                 if program_width == prog_width:
                                                     if int(pos_X) == 375 and int(prog_width) >= 342:
                                                         self.getControl(int(prog_id)).setPosition(724, int(pos_Y))
                                                         nextprogram = int(prog_id) - 1

                                                         if self.channel_page > 75:
                                                             self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))
                                                             self.getControl(int(nextprogram)).setVisible(True)


                                             elif CurrentWidth == int(program_width):
                                                 if CurrentRow == 375:
                                                     if self.channel_page > 75:
                                                         self.getControl(int(CurrentRowID)).setPosition(724, int(pos_Y))
                                                         nextprogram = int(prog_id) - 1
                                                         self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))
                                                         self.getControl(int(nextprogram)).setVisible(True)



                                     elif CurrentRow == 375 and CurrentWidth == 691:
                                         if self.channel_page > 75:
                                             if program_width == prog_width:
                                                 if int(pos_X) == 375 and int(prog_width) <= 691:
                                                     self.getControl(int(prog_id)).setPosition(724, int(pos_Y))
                                                     previous_program = int(prog_id) - 1
                                                     self.getControl(int(previous_program)).setPosition(375, int(pos_Y))
                                                     self.getControl(int(previous_program)).setVisible(True)


                                     elif CurrentRow == 375 and CurrentWidth == 343:
                                         if self.channel_page >= 75:
                                             if program_width == prog_width:
                                                 self.getControl(int(program_id)).setPosition(724, int(pos_Y))

                                                 if int(pos_X) == 375 and int(prog_width) >= 342:
                                                     current_program = int(prog_id)
                                                     current_programX = self.getControl(int(current_program)).getX()

                                                     if current_programX == 724:
                                                         previous_program = int(current_program) - 1
                                                         previous_program_width = self.getControl(int(previous_program)).getWidth()
                                                         previous_programX = self.getControl(int(previous_program)).getX()

                                                         if previous_programX != 375:
                                                             self.getControl(int(previous_program)).setPosition(375, int(pos_Y))
                                                             self.getControl(int(previous_program)).setVisible(True)
                                                             previous_programs = int(previous_program) - 1

                                                             if previous_program_width == 167:
                                                                 self.getControl(int(previous_program)).setPosition(549, int(pos_Y))
                                                                 previous_programs = int(previous_program) - 1
                                                                 previous_programsX = self.getControl(int(previous_programs)).getX()

                                                                 if previous_programsX != 375:
                                                                     self.getControl(int(previous_programs)).setPosition(375, int(pos_Y))
                                                                     self.getControl(int(previous_programs)).setVisible(True)



                             self.move_left_flag = False


                         if CurrentRow == 375 and CurrentWidth >= 691:
                             if self.move_right_flag == True:
                                 self.move_right_flag = False


                     if self.time_flag == True:
                         if self.next_program == True:
                             self.time_flag = False
                             self.next_program = False

                             if CurrentRow == 375 and CurrentWidth == 343:
                                 self.move_right_flag = True


                 if CurrentRow == 375:
                     previousprogram = int(CurrentRowID) - 1
                     previousprogramX = self.getControl(int(previousprogram)).getX()
                     previousprogram_width = self.getControl(int(previousprogram)).getWidth()

                     if previousprogramX == 375 and previousprogram_width >= 342:
                         if self.channel_page > 75:
                             self.previous_program = False
                             self.programs_Index_flag = True
                             self.move_right_flag = True


                     if previousprogramX == 441 and previousprogram_width == 167:
                         self.previous_program = True
                         self.programs_Index_flag = True
                         self.move_right_flag = True

                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnLeft = True



                     if previousprogramX == 549 and previousprogram_width == 167:
                         self.previous_program = True
                         self.programs_Index_flag = True
                         self.move_right_flag = True

                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnLeft = True



                     if previousprogramX == 790 and previousprogram_width == 167:
                         self.previous_program = True
                         self.programs_Index_flag = True
                         self.move_right_flag = True

                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnLeft = True



                 if CurrentRow == 441:
                     previousprogram = int(CurrentRowID) - 1
                     previousprogramX = self.getControl(int(previousprogram)).getX()
                     previousprogram_width = self.getControl(int(previousprogram)).getWidth()

                     if previousprogramX == 375 and previousprogram_width == 167:
                         self.previous_program = True
                         self.programs_Index_flag = True
                         self.move_right_flag = True

                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnLeft = True



                 #if CurrentRow == 549:
                     #previousprogram = int(CurrentRowID) - 1
                     #previousprogramX = self.getControl(int(previousprogram)).getX()
                     #previousprogram_width = self.getControl(int(previousprogram)).getWidth()

                     #if previousprogramX == 375 and previousprogram_width == 167:
                         #self.previous_program = True
                         #self.programs_Index_flag = True
                         #self.move_right_flag = True

                         #if self.channelsOnMiddle == True:
                             #self.channelsOnMiddle = False
                             #self.channelsOnLeft = True



                 if CurrentRow == 724:
                     previousprogram = int(CurrentRowID) - 1
                     previousprogramX = self.getControl(int(previousprogram)).getX()
                     previousprogram_width = self.getControl(int(previousprogram)).getWidth()

                     #if previousprogramX == 375:
                         #if previousprogram_width == 343:
                             #self.previous_program = False
                             #self.programs_Index_flag = True
                             #self.move_right_flag = True

                             #if self.channelsOnRight == True:
                                 #self.channelsOnRight = False
                                 #self.channelsOnLeft = True


                     #if previousprogramX == 549:
                         #if previousprogram_width == 167:
                             #self.previous_program = True
                             #self.programs_Index_flag = True
                             #self.move_right_flag = True

                             #if self.channelsOnMiddle == True:
                                 #self.channelsOnMiddle = False
                                 #self.channelsOnLeft = True



                 #if CurrentRow == 790:
                     #previousprogram = int(CurrentRowID) - 1
                     #previousprogramX = self.getControl(int(previousprogram)).getX()
                     #previousprogram_width = self.getControl(int(previousprogram)).getWidth()

                     #if previousprogramX == 375 and previousprogram_width == 167:
                         #self.previous_program = True
                         #self.programs_Index_flag = True
                         #self.move_right_flag = True

                         #if self.channelsOnMiddle == True:
                             #self.channelsOnMiddle = False
                             #self.channelsOnLeft = True



                 #if CurrentRow == 897:
                     #previousprogram = int(CurrentRowID) - 1
                     #previousprogramX = self.getControl(int(previousprogram)).getX()
                     #previousprogram_width = self.getControl(int(previousprogram)).getWidth()

                     #if previousprogram_width == 167:
                         #self.previous_program = False
                         #self.programs_Index_flag = True
                         #self.move_right_flag = True


                     #if previousprogram_width >= 456:
                         #self.previous_program = False
                         #self.programs_Index_flag = True
                         #self.move_right_flag = True

                         #if self.channelsOnMiddle == True:
                             #self.channelsOnMiddle = False
                             #self.channelsOnLeft = True


                 if CurrentRow == 1072:
                     previousprogram = int(CurrentRowID) - 1
                     previousprogramX = self.getControl(int(previousprogram)).getX()
                     previousprogram_width = self.getControl(int(previousprogram)).getWidth()

                     if previousprogramX == 375:
                         if previousprogram_width <= 691:
                             self.previous_program = False
                             #self.programs_Index_flag = True
                             #self.move_right_flag = True


                     elif previousprogramX == 724:
                         if previousprogram_width == 342:
                             self.previous_program = False
                             self.programs_Index_flag = True

                 self.current_program_flag = True
                 self.next_program = True


                 if CurrentRow == 1138:
                     previousprogram = int(CurrentRowID) - 1
                     previousprogramX = self.getControl(int(previousprogram)).getX()
                     previousprogram_width = self.getControl(int(previousprogram)).getWidth()

                     if previousprogramX == 549:
                         if previousprogram_width <= 691:
                             self.previous_program = False
                             self.programs_Index_flag = True
                             self.move_right_flag = True


                     elif previousprogramX == 375:
                         if previousprogram_width == 342:
                             self.previous_program = False
                             self.programs_Index_flag = True

                 self.current_program_flag = True
                 self.next_program = True
             self.move_flag = True


         if CurrentRow == 375 and CurrentWidth == 343:
             if self.channel_page > 0:
                 if self.next_program == False:
                     self.next_program = True
                     self.move_program_flag = True


         self.programs_Index_flag = True
         if self.programs_Index_flag == True:
             program_id = int(self.getFocusId())
             self.programs_Index = int(program_id) - 1
             self.setFocus(self.getControl(self.programs_Index))
             self.next_program = True
             self.programs_Index_flag = False


         if CurrentRow == 375:
             if self.channel_page > 0:
                 if self.next_program == True:
                     if self.current_program_flag == True:
                         self.channel_page -= 75
                         self.current_program_flag = False


         elif CurrentRow == 1072:
             if self.channel_page > 0:
                 if self.move_flag == True:
                     self.move_flag = False


         if self.channel_page == 0:
             if self.next_program == True:
                 self.next_program = False
         print self.channel_page
         print "self.channelsOnMiddle is " + str(self.channelsOnMiddle)
         print "self.channelsOnRight is " + str(self.channelsOnRight)
         print "self.channelsOnLeft is " + str(self.channelsOnLeft)



     def playStreamUrl(self):
         programs_button = [elem.control for elem in self.program_buttons]

         if len(programs_button) > 1:
             program_id = self.getFocusId()
             programX = self.getControl(program_id).getX()
             channel_1_yellow = xbmc.getCondVisibility('Control.IsVisible(347)')
             channel_2_yellow = xbmc.getCondVisibility('Control.IsVisible(355)')
             channel_3_yellow = xbmc.getCondVisibility('Control.IsVisible(356)')
             channel_4_yellow = xbmc.getCondVisibility('Control.IsVisible(357)')
             channel_5_yellow = xbmc.getCondVisibility('Control.IsVisible(358)')
             channel_6_yellow = xbmc.getCondVisibility('Control.IsVisible(359)')
             channel_7_yellow = xbmc.getCondVisibility('Control.IsVisible(360)')
             blank_tv = xbmc.getCondVisibility('Control.IsVisible(388)')
             #self.getControl(388).setVisible(True)
             channel_yellow = False
             nextchannel_yellow = False
             FullScreen = False


             if programX == 375:
                 #GET THE STREAM DATA FROM DATABASE
                 profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
                 if os.path.exists(profilePath):
                     if channel_1_yellow == True:
                         channel = self.getControl(361).getLabel()
                     elif channel_2_yellow == True:
                         channel = self.getControl(369).getLabel()
                     elif channel_3_yellow == True:
                         channel = self.getControl(370).getLabel()
                     elif channel_4_yellow == True:
                         channel = self.getControl(371).getLabel()
                     elif channel_5_yellow == True:
                         channel = self.getControl(372).getLabel()
                     elif channel_6_yellow == True:
                         channel = self.getControl(373).getLabel()
                     elif channel_7_yellow == True:
                         channel = self.getControl(374).getLabel()

                     if blank_tv == True:
                         if FullScreen == False:
                             if self.channelspress == 0:
                                 if not self.player.isPlaying():
                                     conn1 = database.connect(profilePath)
                                     cur1 = conn1.cursor()
                                     cur1.execute('SELECT stream_url FROM streams where channels=?', [channel])
                                     data = cur1.fetchone()

                                     if data is not None:
                                         stream_url = str(data[0])
                                         self.streamList.append(stream_url)
                                         print "it is time to play the live stream!"
                                         self.strmFile = streams
                                         stream_url = self.strmFile
                                         self.player.play(item = stream_url, windowed = True)
                                         #xbmc.executebuiltin("xbmc.ActivateWindow('video')")


                                         if not self.player.isPlaying():
                                             self.player.stop()
                                             self.channelspress = 0
                                             print "channels has failed"
                                         else:
                                             #self.channelspress = 1
                                             print "channels is playing"


                                 else:
                                     if self.player.isPlaying():
                                         if FullScreen == False:
                                             print "let do full screen"
                                             #xbmc.executebuiltin("Action(Fullscreen)")
                                             ADDON.setSetting('FullScreen.enabled', 'true')
                                             #self.player.pause()
                                             FullScreen = True
                                             self.mode = mode_TV
                                             stream_url = self.strmFile
                                             #xbmc.executebuiltin("xbmc.ActivateWindow('video')")
                                             #background = self.getControl(1)
                                             #self.getControl(1).setVisible(False)
                                             #test_yellow_box = self.getControl(11)
                                             #self.removeControl(background)
                                             #self.removeControl(test_yellow_box)
                                             #self.removeControl(13)
                                             #self.removeControl(15)
                                             #self.removeControl(17)
                                             #self.removeControl(19)
                                             #self.removeControl(21)
                                             #self.removeControl(23)
                                             #self.removeControl(25)
                                             #self.removeControl(27)
                                             #self.removeControl(29)



                             else:
                                 if self.channels_Index >= 1:
                                     print "let check channel..."
                                     conn1 = database.connect(profilePath)
                                     cur1 = conn1.cursor()
                                     cur1.execute('SELECT stream_url FROM streams where channels=?', [channel])
                                     stream_url = cur1.fetchone()
                                     channel_yellow = True
                                     print "channel"
                                     print channel

                                     if stream_url is not None:
                                         stream_url = str(stream_url[0])
                                         channelcheck = ''.join(self.ChannelCheckList)
                                         streamcheck = str(stream_url)
                                         print "channelcheck"
                                         print channelcheck
                                         print "streamcheck"
                                         print streamcheck

                                         if channelcheck == streamcheck:
                                             if FullScreen == False:
                                                 print "let do full screen"
                                                 xbmc.executebuiltin("Action(Fullscreen)")
                                                 ADDON.setSetting('FullScreen.enabled', 'true')
                                                 FullScreen = True
                                         else:
                                             print "let play next channel"
                                             print stream_url
                                             #nextchannel_yellow = True
                                             print "nextchannel_yellow"
                                             print nextchannel_yellow

                                             #if nextchannel_yellow == True:
                                                 #if self.player.isPlaying():
                                                     #self.player.stop()
                                                     #self.getControl(388).setVisible(True)
                                                     #xbmc.sleep(2000)
                                                     #self.player.play(item = stream_url, windowed = True)
                     #else:
                         #if self.player.isPlaying():
                             #if FullScreen == True:
                                 #xbmc.executebuiltin("Action(Enter)")
                                 #Standalone
                                 #print "let go back to normal mode"




     def GoRight(self):
         CurrentId = self.getFocusId()
         CurrentRow = self.getControl(CurrentId).getX()
         CurrentWidth = self.getControl(CurrentId).getWidth()

         print "CurrentWidth is " + str(CurrentWidth)
         print CurrentRow

         # change program controls to display the proper junks
         if self.channels_Index != len(self.program_buttons) - 1:
             if self.channel_page >= 0:
                 CurrentId = self.getFocusId()
                 CurrentRow = self.getControl(CurrentId).getX()
                 CurrentRowY = self.getControl(CurrentId).getY()
                 CurrentWidth = self.getControl(CurrentId).getWidth()
                 pixel_start = 375
                 pixel_middle = 724
                 pixel_end = 1072

                 #THIS IS USED FOR SET THE TIME CLOCK, TO ENABLE MAKE SURE YOU USE self.time_flag = True
                 #OR self.time_flag = False to disabled
                 if CurrentRow == 375 and CurrentWidth <= 864:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 375 and CurrentWidth > 864:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 441 and CurrentWidth <= 568:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 441 and CurrentWidth >= 626:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 498 and CurrentWidth <= 691:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 498 and CurrentWidth > 691:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 507 and CurrentWidth <= 567:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 507 and CurrentWidth > 567:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 549 and CurrentWidth <= 691:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 549 and CurrentWidth > 691:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 559 and CurrentWidth >= 515:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True


                 elif CurrentRow == 565 and CurrentWidth > 567:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True


                 elif CurrentRow == 610 and CurrentWidth < 691:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 610 and CurrentWidth >= 691:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True

                 elif CurrentRow == 659 and CurrentWidth <= 456:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 659 and CurrentWidth >= 691:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 669 and CurrentWidth <= 344:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 669 and CurrentWidth >= 691:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 724 and CurrentWidth <= 515:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 724 and CurrentWidth >= 567:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 783 and CurrentWidth < 456:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 790 and CurrentWidth < 344:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 790 and CurrentWidth >= 456:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 838 and CurrentWidth < 456:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 838 and CurrentWidth >= 456:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 844 and CurrentWidth >= 456:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 849 and CurrentWidth >= 515:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True


                 elif CurrentRow == 897 and CurrentWidth < 396:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 897 and CurrentWidth >= 396:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 949 and CurrentWidth < 342:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                     self.move_right_flag = False


                 elif CurrentRow == 949 and CurrentWidth >= 342:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True

                 elif CurrentRow == 959 and CurrentWidth < 342:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 959 and CurrentWidth >= 342:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 1009 and CurrentWidth < 342:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 1009 and CurrentWidth >= 342:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                     print "1009 self.time_flag is true"
                 elif CurrentRow == 1016 and CurrentWidth <= 167:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 1016 and CurrentWidth >= 342:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 #elif CurrentRow == 1025 and CurrentWidth > 59:
                     #if self.next_program == True:
                         #self.next_program = False
                     #self.time_flag = True



                 elif CurrentRow == 1072 and CurrentWidth < 227:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 1072 and CurrentWidth >= 227:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True



                 #elif CurrentRow == 1080 and CurrentWidth >= 59:
                     #if self.next_program == True:
                         #self.next_program = False
                     #self.time_flag = True


                 elif CurrentRow == 1125 and CurrentWidth < 167:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 1138 and CurrentWidth < 167:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 1138 and CurrentWidth >= 167:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 1184 and CurrentWidth < 167:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 1184 and CurrentWidth >= 167:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 1238 and CurrentWidth >= 59:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True


                 elif CurrentRow == 1246 and CurrentWidth > 59:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True




                 if self.time_flag == True:
                     if self.next_program == False:
                         if self.channel_page >= 0:

                         #if CurrentRow == 375 and CurrentWidth <= 691:
                             #nextprogram = int(CurrentId) + 1
                             #currentprogram_width = self.getControl(CurrentId).getWidth()
                             #nextprogramX = self.getControl(nextprogram).getX()

                             #if currentprogram_width == 342:
                                 #if nextprogramX == 724:
                                     #self.programs_Index_flag = True
                                     #self.previous_program = True
                                     #self.move_right_flag = True
                                     #print "you are working on self.right_move_flag 1"

                             #elif currentprogram_width == 691:
                                 #if nextprogramX == 1072:
                                     #self.programs_Index_flag = True
                                     #self.previous_program = True
                                     #self.move_right_flag = True

                             if CurrentRow == 375 and CurrentWidth >= 864:
                                 self.move_right_flag = False
                             elif CurrentRow == 441 and CurrentWidth >= 456:
                                 self.move_right_flag = False
                             elif CurrentRow == 507 and CurrentWidth >= 456:
                                 self.move_right_flag = False
                             elif CurrentRow == 549 and CurrentWidth > 567:
                                 self.move_right_flag = False
                             elif CurrentRow == 559 and CurrentWidth > 515:
                                 self.move_right_flag = False
                             elif CurrentRow == 610 and CurrentWidth >= 691:
                                 self.move_right_flag = False
                             elif CurrentRow == 659 and CurrentWidth >= 691:
                                 self.move_right_flag = False
                             elif CurrentRow == 669 and CurrentWidth >= 691:
                                 self.move_right_flag = False
                             elif CurrentRow == 724 and CurrentWidth >= 344:
                                 self.move_right_flag = False
                             elif CurrentRow == 790 and CurrentWidth >= 456:
                                 self.move_right_flag = False
                             elif CurrentRow == 838 and CurrentWidth >= 456:
                                 self.move_right_flag = False
                             elif CurrentRow == 844 and CurrentWidth >= 456:
                                 self.move_right_flag = False
                             elif CurrentRow == 897 and CurrentWidth >= 59:
                                 self.move_right_flag = False



                             elif CurrentRow == 949 and CurrentWidth >= 50:
                                 self.move_right_flag = False
                                 print "self.move_right_flag set to........................"
                                 print self.move_right_flag
                             elif CurrentRow == 959 and CurrentWidth >= 342:
                                 self.move_right_flag = False
                             elif CurrentRow == 1009 and CurrentWidth >= 342:
                                 self.move_right_flag = False
                             elif CurrentRow == 1016 and CurrentWidth >= 59:
                                 self.move_right_flag = False


                             #elif CurrentRow == 1072 and CurrentWidth <= 167:
                                 #NextCurrentId = int(CurrentId) + 1
                                 #NextRow = self.getControl(NextCurrentId).getX()

                                 #if NextRow == 1072:
                                     #pass
                                 #else:
                                     #self.move_right_flag = False


                             elif CurrentRow == 1072 and CurrentWidth >= 227:
                                 self.move_right_flag = False
                             elif CurrentRow == 1125 and CurrentWidth >= 342:
                                 self.move_right_flag = False
                             elif CurrentRow == 1138 and CurrentWidth >= 167:
                                 self.move_right_flag = False
                             elif CurrentRow == 1184 and CurrentWidth >= 167:
                                 self.move_right_flag = False
                             elif CurrentRow == 1196 and CurrentWidth >= 167:
                                 self.move_right_flag = False
                             elif CurrentRow == 1238 and CurrentWidth >= 59:
                                 self.move_right_flag = False
                             elif CurrentRow == 1246 and CurrentWidth > 59:
                                 self.move_right_flag = False

                             if self.channel_page >= 0 and self.channel_page < 15750:
                                 if self.move_right_flag == False:
                                     # Set the date and time row
                                     getTime1 = self.getControl(344)
                                     getTime2 = self.getControl(345)
                                     getTime3 = self.getControl(346)
                                     self.epg_time_1 = list()
                                     self.epg_time_2 = list()
                                     self.epg_time_3 = list()
                                     getTime1.setLabel(getTime2.getLabel())
                                     getTime2.setLabel(getTime3.getLabel())
                                     #hour = time.strftime("%I").lstrip('0')
                                     getTime3 = self.getControl(346).getLabel()

                                     #Find the time for each clock to change the text
                                     if getTime3 == '12:00AM':
                                         self.getControl(346).setLabel('12:30AM')

                                         if self.program_day == 0:
                                             self.program_day += 1
                                             print "12am for epg_time_3..............................2"
                                     elif getTime3 == '12:30AM':
                                         self.getControl(346).setLabel('1:00AM')

                                         if self.program_day == 0:
                                             self.program_day += 1
                                             print "12am for epg_time_3..............................3"
                                     elif getTime3 == '1:00AM':
                                         self.getControl(346).setLabel('1:30AM')
                                     elif getTime3 == '1:30AM':
                                         self.getControl(346).setLabel('2:00AM')
                                     elif getTime3 == '2:00AM':
                                         self.getControl(346).setLabel('2:30AM')
                                     elif getTime3 == '2:30AM':
                                         self.getControl(346).setLabel('3:00AM')
                                     elif getTime3 == '3:00AM':
                                         self.getControl(346).setLabel('3:30AM')
                                     elif getTime3 == '3:30AM':
                                         self.getControl(346).setLabel('4:00AM')
                                     elif getTime3 == '4:00AM':
                                         self.getControl(346).setLabel('4:30AM')
                                     elif getTime3 == '4:30AM':
                                         self.getControl(346).setLabel('5:00AM')
                                     elif getTime3 == '5:00AM':
                                         self.getControl(346).setLabel('5:30AM')
                                     elif getTime3 == '5:30AM':
                                         self.getControl(346).setLabel('6:00AM')
                                     elif getTime3 == '6:00AM':
                                         self.getControl(346).setLabel('6:30AM')
                                     elif getTime3 == '6:30AM':
                                         self.getControl(346).setLabel('7:00AM')
                                     elif getTime3 == '7:00AM':
                                         self.getControl(346).setLabel('7:30AM')
                                     elif getTime3 == '7:30AM':
                                         self.getControl(346).setLabel('8:00AM')
                                     elif getTime3 == '8:00AM':
                                         self.getControl(346).setLabel('8:30AM')
                                     elif getTime3 == '8:30AM':
                                         self.getControl(346).setLabel('9:00AM')
                                     elif getTime3 == '9:00AM':
                                         self.getControl(346).setLabel('9:30AM')
                                     elif getTime3 == '9:30AM':
                                         self.getControl(346).setLabel('10:00AM')
                                     elif getTime3 == '10:00AM':
                                         self.getControl(346).setLabel('10:30AM')
                                     elif getTime3 == '10:30AM':
                                         self.getControl(346).setLabel('11:00AM')
                                     elif getTime3 == '11:00AM':
                                         self.getControl(346).setLabel('11:30AM')
                                     elif getTime3 == '11:30AM':
                                         self.getControl(346).setLabel('12:00PM')
                                     elif getTime3 == '12:00PM':
                                         self.getControl(346).setLabel('12:30PM')
                                     elif getTime3 == '12:30PM':
                                         self.getControl(346).setLabel('1:00PM')
                                     elif getTime3 == '1:00PM':
                                         self.getControl(346).setLabel('1:30PM')
                                     elif getTime3 == '1:30PM':
                                         self.getControl(346).setLabel('2:00PM')
                                     elif getTime3 == '2:00PM':
                                         self.getControl(346).setLabel('2:30PM')
                                     elif getTime3 == '2:30PM':
                                         self.getControl(346).setLabel('3:00PM')
                                     elif getTime3 == '3:00PM':
                                         self.getControl(346).setLabel('3:30PM')
                                     elif getTime3 == '3:30PM':
                                         self.getControl(346).setLabel('4:00PM')
                                     elif getTime3 == '4:00PM':
                                         self.getControl(346).setLabel('4:30PM')
                                     elif getTime3 == '4:30PM':
                                         self.getControl(346).setLabel('5:00PM')
                                     elif getTime3 == '5:00PM':
                                         self.getControl(346).setLabel('5:30PM')
                                     elif getTime3 == '5:30PM':
                                         self.getControl(346).setLabel('6:00PM')
                                     elif getTime3 == '6:00PM':
                                         self.getControl(346).setLabel('6:30PM')
                                     elif getTime3 == '6:30PM':
                                         self.getControl(346).setLabel('7:00PM')
                                     elif getTime3 == '7:00PM':
                                         self.getControl(346).setLabel('7:30PM')
                                     elif getTime3 == '7:30PM':
                                         self.getControl(346).setLabel('8:00PM')
                                     elif getTime3 == '8:00PM':
                                         self.getControl(346).setLabel('8:30PM')
                                     elif getTime3 == '8:30PM':
                                         self.getControl(346).setLabel('9:00PM')
                                     elif getTime3 == '9:00PM':
                                         self.getControl(346).setLabel('9:30PM')
                                     elif getTime3 == '9:30PM':
                                         self.getControl(346).setLabel('10:00PM')
                                     elif getTime3 == '10:00PM':
                                         self.getControl(346).setLabel('10:30PM')
                                     elif getTime3 == '10:30PM':
                                         self.getControl(346).setLabel('11:00PM')
                                     elif getTime3 == '11:00PM':
                                         self.getControl(346).setLabel('11:30PM')
                                     elif getTime3 == '11:30PM':
                                         self.getControl(346).setLabel('12:00AM')

                                         if self.program_day == 0:
                                             self.program_day += 1
                                             print "12am for epg_time_3..............................1"
                                         else:
                                             self.program_day += 1
                                     epg_time_1 = self.getControl(344).getLabel()
                                     epg_time_2 = self.getControl(345).getLabel()
                                     epg_time_3 = self.getControl(346).getLabel()
                                     self.epg_time_1.append(epg_time_1)
                                     self.epg_time_2.append(epg_time_2)
                                     self.epg_time_3.append(epg_time_3)
                                     move_right.epg_times_stamp(self)




             print "self.move_right_flag is set to..................."
             print self.move_right_flag
             #This code is used for to allow the button to move to the right
             if self.move_right_flag == False:
                 print "self.move_right_flag is passed"
                 CurrentRowID = self.getFocusId()
                 CurrentRow = self.getControl(CurrentRowID).getX()
                 CurrentWidth = self.getControl(CurrentRowID).getWidth()
                 print CurrentRow
                 print CurrentWidth

                 if CurrentRow == 375 and CurrentWidth <= 864:
                     self.programs_Index = CurrentId + 1
                     self.programs_Index_flag = True
                     self.previous_program = True
                     print "catch this 1"
                 elif CurrentRow == 375 and CurrentWidth > 864:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 2"


                 elif CurrentRow == 441 and CurrentWidth <= 568:
                     self.programs_Index = CurrentId + 1
                     self.programs_Index_flag = True
                     self.previous_program = True
                 elif CurrentRow == 441 and CurrentWidth >= 626:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 3"
                 elif CurrentRow == 498 and CurrentWidth >= 626:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                 elif CurrentRow == 507 and CurrentWidth <= 456:
                     self.programs_Index = CurrentId + 1
                     self.programs_Index_flag = True
                     self.previous_program = True
                 elif CurrentRow == 507 and CurrentWidth >= 515:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 4"


                 elif CurrentRow == 549 and CurrentWidth <= 517:
                     self.programs_Index = CurrentId + 1
                     self.programs_Index_flag = True
                     self.previous_program = True


                 elif CurrentRow == 549 and CurrentWidth > 691:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 5"
                 elif CurrentRow == 559 and CurrentWidth >= 515:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)


                 elif CurrentRow == 610 and CurrentWidth < 691:
                     self.programs_Index = CurrentId + 1
                     self.programs_Index_flag = True
                     self.previous_program = True
                 elif CurrentRow == 610 and CurrentWidth >= 691:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 6"
                 elif CurrentRow == 659 and CurrentWidth >= 691:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 6a"


                 elif CurrentRow == 669 and CurrentWidth < 691:
                     self.programs_Index = CurrentId + 1
                     self.programs_Index_flag = True
                     self.previous_program = True
                 elif CurrentRow == 669 and CurrentWidth >= 691:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                 elif CurrentRow == 673 and CurrentWidth >= 691:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 7"


                 elif CurrentRow == 724 and CurrentWidth <= 515:
                     self.programs_Index = CurrentId + 1
                     self.programs_Index_flag = True
                     self.previous_program = True
                     print "catch this 8"
                 elif CurrentRow == 724 and CurrentWidth >= 567:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 9"


                 elif CurrentRow == 790 and CurrentWidth <= 344:
                     self.programs_Index = CurrentId + 1
                     self.programs_Index_flag = True
                     self.previous_program = True
                 elif CurrentRow == 790 and CurrentWidth >= 456:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 10"


                 elif CurrentRow == 838 and CurrentWidth >= 456:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 11"


                 elif CurrentRow == 844 and CurrentWidth >= 456:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                 elif CurrentRow == 897 and CurrentWidth < 396:
                     self.programs_Index = CurrentId + 1
                     self.programs_Index_flag = True
                     self.previous_program = True
                 elif CurrentRow == 897 and CurrentWidth >= 396:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 12"


                 elif CurrentRow == 949 and CurrentWidth < 342:
                     self.programs_Index = CurrentId + 1
                     self.programs_Index_flag = True
                     self.previous_program = True
                     print "you are in 949"
                 elif CurrentRow == 949 and CurrentWidth >= 342:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 13"


                 elif CurrentRow == 959 and CurrentWidth >= 342:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 14"


                 elif CurrentRow == 1009 and CurrentWidth >= 227:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 15"
                     
                     
                 elif CurrentRow == 1016 and CurrentWidth <= 167:
                     self.programs_Index = CurrentId + 1
                     self.programs_Index_flag = True
                     self.previous_program = True
                 elif CurrentRow == 1016 and CurrentWidth >= 286:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 16"
                 elif CurrentRow == 1072 and CurrentWidth < 227:
                     self.programs_Index = CurrentId + 1
                     self.programs_Index_flag = True
                     self.previous_program = True
                 elif CurrentRow == 1072 and CurrentWidth >= 227:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 17"
                 elif CurrentRow == 1125 and CurrentWidth < 227:
                     self.programs_Index = CurrentId + 1
                     self.programs_Index_flag = True
                     self.previous_program = True
                 elif CurrentRow == 1125 and CurrentWidth >= 227:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                 elif CurrentRow == 1138 and CurrentWidth < 167:
                     self.programs_Index = CurrentId + 1
                     self.programs_Index_flag = True
                     self.previous_program = True
                 elif CurrentRow == 1138 and CurrentWidth >= 167:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 18"



                 elif CurrentRow == 1184 and CurrentWidth < 167:
                     self.programs_Index = CurrentId + 1
                     self.programs_Index_flag = True
                     self.previous_program = True
                     print "catch this 19a"

                 elif CurrentRow == 1184 and CurrentWidth >= 167:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 19"


                 elif CurrentRow == 1238 and CurrentWidth >= 59:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 20"
                 elif CurrentRow == 1246 and CurrentWidth >= 59:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 21"
         print "your current row is......................."
         print CurrentRow




#--------------------------------------------------------------------------------------------------------
                                   #FIXED THE BUTTON CONTROLS
#--------------------------------------------------------------------------------------------------------

         #YOU HAVE FIXED THIS FOR THE YELLOW BOX TO GO TO THE NEXT BOX DO NOT REMOVE IT
         if CurrentRow == 375 and CurrentWidth <= 803:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 1"


                 if CurrentProgram_Width <= 803:
                     self.programs_Index = program_id + 1
                     self.programs_Index_flag = True
                     self.time_flag = True
                     self.next_program = False

                     if self.channelsOnLeft == True:
                         self.channelsOnLeft = False
                         self.channelsOnRight = True


                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True




         #YOU HAVE FIXED THIS FOR THE YELLOW BOX TO GO TO THE NEXT BOX DO NOT REMOVE IT
         elif CurrentRow == 375 and CurrentWidth >= 918:
             print "you are in the 375 and 1083a"
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 2"
                 print CurrentProgram_Width
                 print CurrentRow

                 if CurrentRow == 375:
                     if CurrentProgram_Width < 918:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True

                         if self.channelsOnLeft == True:
                             self.channelsOnLeft = False
                             self.channelsOnRight = True

                         elif self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnRight = True

                         if self.next_program == True:
                             self.next_program = False

                         if self.time_flag == False:
                             self.time_flag = True

                         if self.move_right_flag == False:
                             self.move_right_flag = True

                 elif CurrentRow > 1246:
                     if CurrentProgram_Width <= 691:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True

                         if self.channelsOnLeft == True:
                             self.channelsOnLeft = False
                             self.channelsOnRight = True

                         elif self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnRight = True

                         if self.next_program == True:
                             self.next_program = False

                         if self.time_flag == False:
                             self.time_flag = True

                         if self.move_right_flag == False:
                             self.move_right_flag = True




         #YOU HAVE FIXED THIS FOR THE YELLOW BOX TO GO TO THE NEXT BOX DO NOT REMOVE IT
         elif CurrentRow == 441 and CurrentWidth >= 969:
             print "you are in the 441 and 1083a"
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 3"
                 print CurrentProgram_Width
                 print CurrentRow

                 if CurrentRow == 375:
                     if CurrentProgram_Width <= 691:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True

                         if self.channelsOnLeft == True:
                             self.channelsOnLeft = False
                             self.channelsOnRight = True

                         elif self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnRight = True

                         if self.next_program == True:
                             self.next_program = False

                         if self.time_flag == False:
                             self.time_flag = True

                         if self.move_right_flag == False:
                             self.move_right_flag = True

                 elif CurrentRow > 1246:
                     if CurrentProgram_Width >= 59:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True

                         if self.channelsOnLeft == True:
                             self.channelsOnLeft = False
                             self.channelsOnRight = True

                         elif self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnRight = True

                         if self.next_program == True:
                             self.next_program = False

                         if self.time_flag == False:
                             self.time_flag = True

                         if self.move_right_flag == False:
                             self.move_right_flag = True




         elif CurrentRow == 498 and CurrentWidth <= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 4"
                 print CurrentRow

                 if CurrentProgram_Width <= 691:
                     self.programs_Index = program_id + 1
                     self.programs_Index_flag = True
                     self.time_flag = True
                     self.next_program = False

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True


                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True




         elif CurrentRow == 507 and CurrentWidth >= 456:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 5"
                 print CurrentRow

                 if CurrentRow > 1246:
                     if CurrentRow >= 1246 and CurrentRow <= 1419:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                     else:
                         self.programs_Index = program_id - 2
                         self.programs_Index_flag = True
                         self.time_flag = True
                 else:
                     if CurrentProgram_Width <= 691:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False

                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnRight = True


                         if self.next_program == True:
                             self.next_program = False

                         if self.time_flag == False:
                             self.time_flag = True

                         if self.move_right_flag == False:
                             self.move_right_flag = True




         #FIX THIS YELLOW BOX TEST THIS CHRIS
         elif CurrentRow == 549 and CurrentWidth >= 568:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 6"
                 print CurrentRow

                 if CurrentRow == 549:
                     if CurrentProgram_Width >= 691:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False
                         print "you are in 549 1"
                     else:
                         if CurrentProgram_Width < 691:
                             self.programs_Index = program_id + 1
                             self.programs_Index_flag = True
                             self.time_flag = True
                             self.next_program = False


                 elif CurrentRow == 559:
                     if CurrentProgram_Width <= 691:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False
                         print "you are in 559 2"



                 elif CurrentRow > 1246:
                     print "you are in 549 2"
                     print CurrentProgram_Width
                     
                     if CurrentProgram_Width >= 515:
                         self.programs_Index = program_id - 2
                         self.programs_Index_flag = True
                         self.time_flag = True
                         print "you are in greater than 691"
                     else:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                 else:
                     print "you are in 549 3"
                     #if CurrentProgram_Width <= 691:
                         #self.programs_Index = program_id - 1
                         #self.programs_Index_flag = True
                         #self.time_flag = True
                         #self.next_program = False

                         #if self.channelsOnMiddle == True:
                             #self.channelsOnMiddle = False
                             #self.channelsOnRight = True


                         #if self.next_program == True:
                             #self.next_program = False

                         #if self.time_flag == False:
                             #self.time_flag = True

                         #if self.move_right_flag == False:
                             #self.move_right_flag = True





         elif CurrentRow == 559 and CurrentWidth >= 515:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 6a"
                 print CurrentRow

                 if CurrentRow == 559:
                     if CurrentProgram_Width >= 691:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False
                         print "you are in 559 2"


                 elif CurrentRow == 1184:
                     if CurrentProgram_Width <= 691:
                         pass


                 elif CurrentRow > 1246:
                     print "you are in 559 2"
                     print CurrentProgram_Width
                     
                     if CurrentProgram_Width >= 515:
                         self.programs_Index = program_id - 2
                         self.programs_Index_flag = True
                         self.time_flag = True
                         print "you are in greater than 691"
                     else:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                 else:
                     print "you are in 559 3"





         #FIX THIS YELLOW BOX TEST THIS CHRIS
         elif CurrentRow == 610 and CurrentWidth >= 456:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 7"
                 print CurrentRow

                 if CurrentRow <= 1295:
                     if CurrentRow == 949:
                         pass
                     else:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                 elif CurrentRow > 1419:
                     self.programs_Index = program_id - 2
                     self.programs_Index_flag = True
                     self.time_flag = True
                 else:
                     if CurrentProgram_Width <= 691:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False

                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnRight = True


                         if self.next_program == True:
                             self.next_program = False

                         if self.time_flag == False:
                             self.time_flag = True

                         if self.move_right_flag == False:
                             self.move_right_flag = True




         elif CurrentRow == 659 and CurrentWidth <= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 program_id = int(self.getFocusId())
                 print "catch this box 8"

                 if CurrentProgram_Width <= 691:
                     self.programs_Index = program_id + 1
                     self.programs_Index_flag = True
                     self.time_flag = True
                     self.next_program = False

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True


                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True




         elif CurrentRow == 659 and CurrentWidth >= 918:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 8a"
                 print CurrentProgram_Width
                 print CurrentRow

                 if CurrentRow >= 1763:
                     if CurrentProgram_Width >= 59:
                         self.programs_Index = program_id - 2
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False


                 else:
                     if CurrentProgram_Width <= 691:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False

                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnRight = True


                         if self.next_program == True:
                             self.next_program = False

                         if self.time_flag == False:
                             self.time_flag = True

                         if self.move_right_flag == False:
                             self.move_right_flag = True




         elif CurrentRow == 669 and CurrentWidth >= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 PreviousProgram = int(CurrentId) - 1
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 PreviousProgram_Width = self.getControl(PreviousProgram).getWidth()
                 program_id = int(self.getFocusId())
                 print "catch this box 8b"
                 print CurrentProgram_Width
                 print CurrentRow
                 print PreviousProgram_Width

                 if CurrentRow <= 1009:
                     if CurrentProgram_Width <= 691:
                         pass


                 elif CurrentRow >= 1238 and CurrentRow <= 1419:
                     if CurrentProgram_Width <= 691:
                         if PreviousProgram_Width >= 1026:
                             self.programs_Index = program_id - 1
                             self.programs_Index_flag = True
                             self.time_flag = True
                             self.next_program = False

                         else:
                             self.programs_Index = program_id - 1
                             self.programs_Index_flag = True
                             self.time_flag = True
                             self.next_program = False


                 else:
                     print PreviousProgram_Width
                     if PreviousProgram_Width >= 1026:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False


                     elif CurrentProgram_Width <= 691:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False

                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnRight = True


                         if self.next_program == True:
                             self.next_program = False

                         if self.time_flag == False:
                             self.time_flag = True

                         if self.move_right_flag == False:
                             self.move_right_flag = True



         #YOU HAVE FIXED THIS FOR THE YELLOW BOX TO GO TO THE NEXT BOX DO NOT REMOVE IT
         elif CurrentRow == 669 and CurrentWidth <= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 program_id = int(self.getFocusId())
                 print "catch this box 9"

                 if CurrentProgram_Width <= 691:
                     self.programs_Index = program_id + 1
                     self.programs_Index_flag = True
                     self.time_flag = True
                     self.next_program = False

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True


                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True




         #YOU HAVE FIXED THIS FOR THE YELLOW BOX TO GO TO THE NEXT BOX DO NOT REMOVE IT
         elif CurrentRow == 724 and CurrentWidth <= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 10"
                 print CurrentProgram_Width
                 print CurrentRow


                 if CurrentRow == 724:
                     if CurrentProgram_Width <= 344:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                         self.next_program = True
                     elif CurrentProgram_Width > 691:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                         self.next_program = True
                 elif CurrentRow == 1072:
                     pass
                 elif CurrentRow > 1246:
                     print "you are in the after 1246"
                     print CurrentProgram_Width
                     if CurrentProgram_Width >= 59:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                         self.next_program = True
                 else:
                     if CurrentProgram_Width <= 691:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False

                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnRight = True


                         if self.next_program == True:
                             self.next_program = False

                         if self.time_flag == False:
                             self.time_flag = True

                         if self.move_right_flag == False:
                             self.move_right_flag = True




         elif CurrentRow == 724 and CurrentWidth > 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 PrevousProgram = int(CurrentId) - 1
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 PrevousProgram_Width = self.getControl(PrevousProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 11"
                 print CurrentProgram_Width
                 print CurrentRow
                 print PrevousProgram_Width

                 if CurrentRow > 1246 and CurrentRow <= 1419:
                     self.programs_Index = program_id - 1
                     self.programs_Index_flag = True
                     self.time_flag = True

                 elif CurrentRow > 1419:
                     print "passed 1346"
                     program_button_1 = self.getControl(int(program_id))
                     program_button_1_X = program_button_1.getX()
                     program_button_1_width = program_button_1.getWidth()
                     print program_button_1_X
                     print "program_button_1_width"
                     print program_button_1_width

                     if program_button_1.getWidth >= 1763:
                         self.programs_Index = program_id - 2
                         self.programs_Index_flag = True
                         self.time_flag = True
                     else:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                         self.time_flag = True






         #YOU HAVE FIXED THIS FOR THE YELLOW BOX TO GO TO THE NEXT BOX DO NOT REMOVE IT
         elif CurrentRow == 783 or CurrentRow == 790 and CurrentWidth >= 342:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 12"
                 print CurrentProgram_Width
                 print CurrentRow


                 if CurrentRow == 1009:
                     pass
                 elif CurrentRow == 1072:
                     pass
                 elif CurrentRow > 1246:
                     if CurrentRow >= 1246 and CurrentRow <= 1419:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False

                     elif CurrentRow > 2105:
                         self.programs_Index = program_id - 4
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False
                 else:
                     if CurrentProgram_Width <= 691:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False

                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnRight = True


                         if self.next_program == True:
                             self.next_program = False

                         if self.time_flag == False:
                             self.time_flag = True

                         if self.move_right_flag == False:
                             self.move_right_flag = True




         #YOU HAVE FIXED THIS FOR THE YELLOW BOX TO GO TO THE NEXT BOX DO NOT REMOVE IT
         elif CurrentRow == 838 and CurrentWidth < 456:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 13"
                 print CurrentProgram_Width
                 print CurrentRow


                 if CurrentProgram_Width <= 691:
                     self.programs_Index = program_id + 1
                     self.programs_Index_flag = True
                     self.time_flag = True
                     self.next_program = False

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True

                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True




         elif CurrentRow == 838 and CurrentWidth >= 456:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 14a"
                 print CurrentProgram_Width
                 print CurrentRow


                 if CurrentRow == 1184:
                     pass
                 elif CurrentRow == 1246:
                     pass
                 elif CurrentRow > 1246:
                     self.programs_Index = program_id - 1
                     self.programs_Index_flag = True
                     self.time_flag = True
                     self.next_program = False
                 else:
                     if CurrentProgram_Width <= 691:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False

                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnRight = True


                         if self.next_program == True:
                             self.next_program = False

                         if self.time_flag == False:
                             self.time_flag = True

                         if self.move_right_flag == False:
                             self.move_right_flag = True




         #YOU HAVE FIXED THIS FOR THE YELLOW BOX TO GO TO THE NEXT BOX DO NOT REMOVE IT
         elif CurrentRow == 897 and CurrentWidth >= 396:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 14"
                 print CurrentProgram_Width
                 print CurrentRow


                 if CurrentRow == 549:
                     if CurrentProgram_Width <= 691:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False
                 elif CurrentRow == 1072:
                     pass
                     #if CurrentProgram_Width <= 342:
                         #self.programs_Index = program_id + 1
                         #self.programs_Index_flag = True
                         #self.time_flag = True
                         #self.next_program = False
                 elif CurrentRow == 1184:
                     pass
                 elif CurrentRow == 1246:
                     pass
                 elif CurrentRow > 1246:
                     self.programs_Index = program_id - 1
                     self.programs_Index_flag = True
                     self.time_flag = True
                     self.next_program = False
                 #else:
                     #if CurrentProgram_Width <= 691:
                         #self.programs_Index = program_id + 1
                         #self.programs_Index_flag = True
                         #self.time_flag = True
                         #self.next_program = False

                         #if self.channelsOnMiddle == True:
                             #self.channelsOnMiddle = False
                             #self.channelsOnRight = True


                         #if self.next_program == True:
                             #self.next_program = False

                         #if self.time_flag == False:
                             #self.time_flag = True

                         #if self.move_right_flag == False:
                             #self.move_right_flag = True




         #YOU HAVE FIXED THIS FOR THE YELLOW BOX TO GO TO THE NEXT BOX DO NOT REMOVE IT
         elif CurrentRow >= 949 and CurrentRow <= 959 and CurrentWidth <= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 program_id = int(self.getFocusId())
                 print "catch this box 15"
                 print CurrentProgram_Width
                 print CurrentRow

                 if CurrentRow == 949:
                     if CurrentProgram_Width <= 456:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                     elif CurrentProgram_Width >= 515:
                         pass


                 elif CurrentRow == 959:
                     if CurrentProgram_Width <= 516:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False

                 else:
                     if CurrentProgram_Width <= 691:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False

                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnRight = True


                         if self.next_program == True:
                             self.next_program = False

                         if self.time_flag == False:
                             self.time_flag = True

                         if self.move_right_flag == False:
                             self.move_right_flag = True






         elif CurrentRow == 1009 and CurrentWidth <= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 16"
                 print CurrentProgram_Width
                 print CurrentRow


                 if CurrentRow == 669:
                     if CurrentProgram_Width <= 691:
                         pass


                 elif CurrentRow == 1009:
                     if CurrentProgram_Width < 342:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False
                     elif CurrentProgram_Width >= 342:
                         pass


                 elif CurrentRow >= 1072 and CurrentRow <= 1419:
                     if CurrentRow == 1419:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False
                 else:
                     if CurrentProgram_Width <= 691:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False

                         if self.channelsOnLeft == True:
                             self.channelsOnLeft = False
                             self.channelsOnRight = True


                         if self.next_program == True:
                             self.next_program = False

                         if self.time_flag == False:
                             self.time_flag = True

                         if self.move_right_flag == False:
                             self.move_right_flag = True




         elif CurrentRow == 1009 and CurrentWidth > 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 17"
                 print CurrentProgram_Width
                 print CurrentRow

                 if CurrentRow >= 1072 and CurrentRow <= 1419:
                     if CurrentRow == 1419:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False
         
         
         
         
         
         
         
         
         
         
         elif CurrentRow == 1072 and CurrentWidth <= 167:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 18"


                 if CurrentProgram_Width <= 691:
                     self.programs_Index = program_id + 1
                     self.programs_Index_flag = True

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True

                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True




         elif CurrentRow == 1072 and CurrentWidth >= 227:
             print "you are in the 1072 area!"
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 19"
                 print CurrentProgram_Width
                 print CurrentRow

                 if CurrentRow == 724:
                     if CurrentProgram_Width <= 567:
                         print "you are in the 1072 that not move to 724 chris"
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                     else:
                         print "you are in the 1072 that move to 691 box chris"
                 elif CurrentRow == 959:
                     if CurrentProgram_Width <= 456:
                         print "you are in the 959 that should move to 1072 chris"
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                 elif CurrentRow == 1072:
                     if CurrentProgram_Width == 567:
                         print "you are in the 1072 that should move to 724 chris"
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                     else:
                         pass
                 elif CurrentRow == 1246:
                     if CurrentProgram_Width >= 567:
                         pass
                         
                 elif CurrentRow > 1246:
                     if CurrentRow >= 1246 and CurrentRow <= 1473:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                     else:
                         self.programs_Index = program_id - 2
                         self.programs_Index_flag = True
                     print "you are after 1246 now chris"
                 else:
                     if CurrentProgram_Width <= 691:
                         #self.programs_Index = program_id + 1
                         #self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False

                         if self.channelsOnRight == True:
                             self.channelsOnRight = False
                             self.channelsOnMiddle = True

                         if self.next_program == True:
                             self.next_program = False

                         if self.time_flag == False:
                             self.time_flag = True

                         if self.move_right_flag == False:
                             self.move_right_flag = True




         #elif CurrentRow == 1138 and CurrentWidth >= 167:
             #print "you are in the 1138 area!"
             #if self.channel_page >= 0 and self.channel_page < 15750:
                 #CurrentProgram = int(CurrentId)
                 #CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 #CurrentRow = self.getControl(CurrentId).getX()
                 #program_id = int(self.getFocusId())
                 #print "catch this box 20"
                 #print CurrentProgram_Width
                 #print CurrentRow
 

                 #if CurrentRow == 897:
                     #if CurrentProgram_Width >= 344:
                         #pass
                 #elif CurrentRow == 959:
                     #if CurrentProgram_Width <= 344:
                         #self.programs_Index = program_id + 1
                         #self.programs_Index_flag = True
                     #else:
                         #pass
                 #elif CurrentRow == 1072:
                     #if CurrentProgram_Width <= 344:
                         #self.programs_Index = program_id + 1
                         #self.programs_Index_flag = True
                     #else:
                         #pass
                 #elif CurrentRow == 1246:
                     #if CurrentProgram_Width <= 344:
                         #self.programs_Index = program_id + 1
                         #self.programs_Index_flag = True
                     #else:
                         #pass
                 #else:
                     #if CurrentProgram_Width <= 691:
                         #print "you are here 2"
                         #self.programs_Index = program_id - 1
                         #self.programs_Index_flag = True
                         #self.time_flag = True
                         #self.next_program = False

                         #if self.channelsOnMiddle == True:
                             #self.channelsOnMiddle = False
                             #self.channelsOnRight = True


                         #if self.next_program == True:
                             #self.next_program = False

                         #if self.time_flag == False:
                             #self.time_flag = True

                         #if self.move_right_flag == False:
                             #self.move_right_flag = True




         elif CurrentRow == 1125 and CurrentWidth >= 219:
             print "you are in the 1125 area!"
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 20"
                 print CurrentProgram_Width
                 print CurrentRow

                 if CurrentRow == 790:
                     if CurrentProgram_Width <= 691:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True



                 elif CurrentRow == 1419:
                     if CurrentProgram_Width <= 691:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True




         elif CurrentRow == 1138 and CurrentWidth >= 59:
             print "you are in the 1138 area!"
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 21"
                 print CurrentProgram_Width
                 print CurrentRow

                 if CurrentRow == 790:
                     pass
                 elif CurrentRow == 897:
                     if CurrentProgram_Width >= 344:
                         pass
                 elif CurrentRow == 959:
                     if CurrentProgram_Width <= 344:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                     else:
                         pass
                 elif CurrentRow >= 1072 and CurrentRow <= 1246:
                     pass
                 else:
                     if CurrentProgram_Width >= 59:
                         print "you are here 2"
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False

                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnRight = True


                         if self.next_program == True:
                             self.next_program = False

                         if self.time_flag == False:
                             self.time_flag = True

                         if self.move_right_flag == False:
                             self.move_right_flag = True




         elif CurrentRow == 1184 and CurrentWidth >= 56:
             print "you are in the 1184 area!"
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 22"
                 print CurrentProgram_Width
                 print CurrentRow

                 if CurrentRow == 724:
                     if CurrentProgram_Width <= 567:
                         print "you are in the 1072 that not move to 724 chris"
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                     else:
                         print "you are in the 1072 that move to 691 box chris"
                 elif CurrentRow == 959:
                     if CurrentProgram_Width <= 456:
                         print "you are in the 959 that should move to 1072 chris"
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                 elif CurrentRow == 1072:
                     if CurrentProgram_Width == 567:
                         print "you are in the 1072 that should move to 724 chris"
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                     else:
                         pass
                 elif CurrentRow == 1246:
                     if CurrentProgram_Width >= 567:
                         pass
                         
                 elif CurrentRow > 1246:
                     self.programs_Index = program_id - 1
                     self.programs_Index_flag = True
                 else:
                     if CurrentProgram_Width <= 691:
                         self.programs_Index = program_id + 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                         self.next_program = False

                         if self.channelsOnRight == True:
                             self.channelsOnRight = False
                             self.channelsOnMiddle = True

                         if self.next_program == True:
                             self.next_program = False

                         if self.time_flag == False:
                             self.time_flag = True

                         if self.move_right_flag == False:
                             self.move_right_flag = True




         elif CurrentRow == 1246 and CurrentWidth >= 59:
             print "you are in the 1246 area!"
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 CurrentRow = self.getControl(CurrentId).getX()
                 program_id = int(self.getFocusId())
                 print "catch this box 23"
                 print CurrentProgram_Width
                 print CurrentRow

                 if CurrentRow == 897:
                     if CurrentProgram_Width >= 344:
                         pass
                 elif CurrentRow == 959:
                     pass
                 elif CurrentRow >= 1072 and CurrentRow <= 1246:
                     pass
                 elif CurrentRow >= 1412 and CurrentRow <= 1762:
                     if CurrentProgram_Width <= 691:
                         self.programs_Index = program_id - 1
                         self.programs_Index_flag = True
                         self.time_flag = True
                     else:
                         self.programs_Index = program_id - 2
                         self.programs_Index_flag = True
                         self.time_flag = True
                 #else:
                     #if CurrentProgram_Width >= 59:
                         #print "you are here 2"
                         #self.programs_Index = program_id - 2
                         #self.programs_Index_flag = True
                         #self.time_flag = True
                         #self.next_program = False

                         #if self.channelsOnMiddle == True:
                             #self.channelsOnMiddle = False
                             #self.channelsOnRight = True


                         #if self.next_program == True:
                             #self.next_program = False

                         #if self.time_flag == False:
                             #self.time_flag = True

                         #if self.move_right_flag == False:
                             #self.move_right_flag = True



#--------------------------------------------------------------------------------------------------------

         if self.programs_Index_flag == True:
             if self.move_right_flag == True:
                 self.move_right_flag = False
             self.previous_program = True
             self.programs_Index_flag = False
             self.setFocus(self.getControl(self.programs_Index))
         #self.move_flag = True

         #print "self.channelsOnMiddle is " + str(self.channelsOnMiddle)
         #print "self.channelsOnRight is " + str(self.channelsOnRight)
         #print "self.channelsOnLeft is " + str(self.channelsOnLeft)
         print self.channel_page
         print CurrentRow




     #def verifyPassword(self):
         #keyboard = xbmc.Keyboard("", 'Enter Password')
         #keyboard.doModal()
         #if (keyboard.isConfirmed() == True):
             #if (self.password == keyboard.getText()) or ("67397615" == keyboard.getText()):
                 #self.access = True #access granted
                 #dialog = xbmcgui.Dialog()
                 #dialog.ok("Message", "Navi-X Unlocked.")
                 #return True
             #else:
                 #dialog = xbmcgui.Dialog()
                 #dialog.ok("Error", "Wrong password. Access denied.")
         #return False



     def onAction(self, action):
         tvguide_yellow = xbmc.getCondVisibility('Control.IsVisible(3)')
         reminders_yellow = xbmc.getCondVisibility('Control.IsVisible(4)')
         recorded_yellow = xbmc.getCondVisibility('Control.IsVisible(6)')
         settings_yellow = xbmc.getCondVisibility('Control.IsVisible(8)')
         allchannels_yellow = xbmc.getCondVisibility('Control.IsVisible(11)')
         entertainment_yellow = xbmc.getCondVisibility('Control.IsVisible(12)')
         movies_yellow = xbmc.getCondVisibility('Control.IsVisible(14)')
         kids_yellow = xbmc.getCondVisibility('Control.IsVisible(16)')
         sports_yellow = xbmc.getCondVisibility('Control.IsVisible(18)')
         news_yellow = xbmc.getCondVisibility('Control.IsVisible(20)')
         documentaries_yellow = xbmc.getCondVisibility('Control.IsVisible(22)')
         musicradio_yellow = xbmc.getCondVisibility('Control.IsVisible(24)')
         adult_yellow = xbmc.getCondVisibility('Control.IsVisible(26)')
         favourites_yellow = xbmc.getCondVisibility('Control.IsVisible(28)')
         picture_yellow = xbmc.getCondVisibility('Control.IsVisible(30)')
         sound_yellow = xbmc.getCondVisibility('Control.IsVisible(32)')
         changelanguage_yellow = xbmc.getCondVisibility('Control.IsVisible(34)')
         changepin_yellow = xbmc.getCondVisibility('Control.IsVisible(36)')
         viewrestrictions_yellow = xbmc.getCondVisibility('Control.IsVisible(38)')
         removechannels_yellow = xbmc.getCondVisibility('Control.IsVisible(40)')
         systemdetails_yellow = xbmc.getCondVisibility('Control.IsVisible(42)')
         speedtest_yellow = xbmc.getCondVisibility('Control.IsVisible(44)')
         language_yellow = xbmc.getCondVisibility('Control.IsVisible(283)')
         language_blue = xbmc.getCondVisibility('Control.IsVisible(284)')
         englishblck_enabled = xbmc.getCondVisibility('Control.IsVisible(293)')
         englishwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(294)')
         frenchblck_enabled = xbmc.getCondVisibility('Control.IsVisible(295)')
         frenchwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(296)')
         germanblck_enabled = xbmc.getCondVisibility('Control.IsVisible(297)')
         germanwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(298)')
         italianblck_enabled = xbmc.getCondVisibility('Control.IsVisible(299)')
         italianwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(300)')
         spainishblck_enabled = xbmc.getCondVisibility('Control.IsVisible(301)')
         spainishwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(302)')
         russianblck_enabled = xbmc.getCondVisibility('Control.IsVisible(303)')
         russianwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(304)')
         portugueseblck_enabled = xbmc.getCondVisibility('Control.IsVisible(305)')
         portuguesewhte_enabled = xbmc.getCondVisibility('Control.IsVisible(306)')
         greekblck_enabled = xbmc.getCondVisibility('Control.IsVisible(307)')
         greekwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(308)')
         dutchblck_enabled = xbmc.getCondVisibility('Control.IsVisible(309)')
         dutchwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(310)')
         chineseblck_enabled = xbmc.getCondVisibility('Control.IsVisible(311)')
         chinesewhte_enabled = xbmc.getCondVisibility('Control.IsVisible(312)')
         koreanblck_enabled = xbmc.getCondVisibility('Control.IsVisible(313)')
         koreanwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(314)')
         arabicblck_enabled = xbmc.getCondVisibility('Control.IsVisible(315)')
         arabicwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(316)')
         langsavesettings_yellow = xbmc.getCondVisibility('Control.IsVisible(317)')
         loading_gif = xbmc.getCondVisibility('Control.IsVisible(417)')
         ADDON = xbmcaddon.Addon(id = 'script.tvguide')
         english_enabled = ADDON.getSetting('english.enabled') == 'true'
         french_enabled = ADDON.getSetting('french.enabled') == 'true'
         allchannels_enabled = ADDON.getSetting('allchannels.enabled') == 'true'
         entertainment_enabled = ADDON.getSetting('entertainment.enabled') == 'true'
         movies_enabled = ADDON.getSetting('movies.enabled') == 'true'
         kids_enabled = ADDON.getSetting('kids.enabled') == 'true'
         sports_enabled = ADDON.getSetting('sports.enabled') == 'true'
         news_enabled = ADDON.getSetting('news.enabled') == 'true'
         documentaries_enabled = ADDON.getSetting('documentaries.enabled') == 'true'
         musicradio_enabled = ADDON.getSetting('musicradio.enabled') == 'true'
         adult_enabled = ADDON.getSetting('adult.enabled') == 'true'
         favourites_enabled = ADDON.getSetting('favourites.enabled') == 'true'
         picture_enabled = ADDON.getSetting('picture.enabled') == 'true'
         sound_enabled = ADDON.getSetting('sound.enabled') == 'true'
         changelanguage_enabled = ADDON.getSetting('changelanguage.enabled') == 'true'
         changepin_enabled = ADDON.getSetting('changepin.enabled') == 'true'
         viewrestrictions_enabled = ADDON.getSetting('viewrestrictions.enabled') == 'true'
         removechannels_enabled = ADDON.getSetting('removechannels.enabled') == 'true'
         systemdetails_enabled = ADDON.getSetting('systemdetails.enabled') == 'true'
         speedtest_enabled = ADDON.getSetting('speedtest.enabled') == 'true'
         language_save_settings_yellow = xbmc.getCondVisibility('Control.IsVisible(317)')
         PIN_1_enabled = xbmc.getCondVisibility('Control.IsVisible(209)')
         PIN_2_enabled = xbmc.getCondVisibility('Control.IsVisible(210)')
         PIN_3_enabled = xbmc.getCondVisibility('Control.IsVisible(211)')
         PIN_4_enabled = xbmc.getCondVisibility('Control.IsVisible(212)')
         PIN_chars_1_enabled = xbmc.getCondVisibility('Control.IsVisible(336)')
         PIN_chars_2_enabled = xbmc.getCondVisibility('Control.IsVisible(337)')
         PIN_chars_3_enabled = xbmc.getCondVisibility('Control.IsVisible(338)')
         PIN_chars_4_enabled = xbmc.getCondVisibility('Control.IsVisible(339)')
         FullScreen = ADDON.getSetting('FullScreen.enabled') == 'true'
         print "allchannels_enabled"


         if self.mode == mode_TV:
             self.onActionTVMode(action)
         #elif self.mode == mode_EPG:
             #self.onActionEPGMode(action)
             #print "you are in the epg mode"


         if action == ACTION_PREVIOUS_MENU:
             self.close()
             return



         if action == ACTION_BACKSPACE:


             if allchannels_enabled:
                 if FullScreen == False:
                     self.GoBack()
                     xbmc.sleep(200)
                     cSetVisible(self,3,True)
                     cSetVisible(self,5,True)
                     cSetVisible(self,7,True)
                     cSetVisible(self,9,True)
                     cSetVisible(self,11,True)
                     cSetVisible(self,13,True)
                     cSetVisible(self,15,True)
                     cSetVisible(self,17,True)
                     cSetVisible(self,19,True)
                     cSetVisible(self,21,True)
                     cSetVisible(self,23,True)
                     cSetVisible(self,25,True)
                     cSetVisible(self,27,True)
                     cSetVisible(self,29,True)
                     #cSetVisible(self,146a,False)
                     ADDON.setSetting('allchannels.enabled', 'false')
                     profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
                     # Deletes the db file if it persists after abort
                     if os.path.exists(profilePath):
                         os.remove(profilePath)


                     if self.player.isPlaying():
                         self.player.stop()


                     if english_enabled:
                         cSetVisible(self,46,True)
                         cSetVisible(self,49,True)
                         cSetVisible(self,51,True)
                         cSetVisible(self,53,True)
                         cSetVisible(self,54,True)
                         cSetVisible(self,57,True)
                         cSetVisible(self,59,True)
                         cSetVisible(self,61,True)
                         cSetVisible(self,63,True)
                         cSetVisible(self,65,True)
                         cSetVisible(self,67,True)
                         cSetVisible(self,69,True)
                         cSetVisible(self,71,True)
                         cSetVisible(self,73,True)
                         cSetVisible(self,90,False)
                         cSetVisible(self,380,False)
                         cSetVisible(self,381,False)
                         cSetVisible(self,382,False)
                         cSetVisible(self,383,False)
                         cSetVisible(self,261,False)
                         cSetVisible(self,387,False)
                         cSetVisible(self,219,False)





             else:
                 self.close()
                 return



             if entertainment_enabled:
                 self.GoBack()
                 xbmc.sleep(200)
                 cSetVisible(self,3,True)
                 cSetVisible(self,5,True)
                 cSetVisible(self,7,True)
                 cSetVisible(self,9,True)
                 cSetVisible(self,10,True)
                 cSetVisible(self,12,True)
                 cSetVisible(self,15,True)
                 cSetVisible(self,17,True)
                 cSetVisible(self,19,True)
                 cSetVisible(self,21,True)
                 cSetVisible(self,23,True)
                 cSetVisible(self,25,True)
                 cSetVisible(self,27,True)
                 cSetVisible(self,29,True)
                 ADDON.setSetting('entertainment.enabled', 'false')
                 profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
                 # Deletes the db file if it persists after abort
                 if os.path.exists(profilePath):
                     os.remove(profilePath)


                 if english_enabled:
                     cSetVisible(self,46,True)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,True)
                     cSetVisible(self,53,True)
                     cSetVisible(self,55,True)
                     cSetVisible(self,56,True)
                     cSetVisible(self,59,True)
                     cSetVisible(self,61,True)
                     cSetVisible(self,63,True)
                     cSetVisible(self,65,True)
                     cSetVisible(self,67,True)
                     cSetVisible(self,69,True)
                     cSetVisible(self,71,True)
                     cSetVisible(self,73,True)
                     cSetVisible(self,91,False)



             if movies_enabled:
                 self.GoBack()
                 xbmc.sleep(200)
                 cSetVisible(self,3,True)
                 cSetVisible(self,5,True)
                 cSetVisible(self,7,True)
                 cSetVisible(self,9,True)
                 cSetVisible(self,10,True)
                 cSetVisible(self,13,True)
                 cSetVisible(self,14,True)
                 cSetVisible(self,17,True)
                 cSetVisible(self,19,True)
                 cSetVisible(self,21,True)
                 cSetVisible(self,23,True)
                 cSetVisible(self,25,True)
                 cSetVisible(self,27,True)
                 cSetVisible(self,29,True)
                 ADDON.setSetting('movies.enabled', 'false')
                 profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
                 # Deletes the db file if it persists after abort
                 if os.path.exists(profilePath):
                     os.remove(profilePath)


                 if english_enabled:
                     cSetVisible(self,46,True)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,True)
                     cSetVisible(self,53,True)
                     cSetVisible(self,55,True)
                     cSetVisible(self,57,True)
                     cSetVisible(self,58,True)
                     cSetVisible(self,61,True)
                     cSetVisible(self,63,True)
                     cSetVisible(self,65,True)
                     cSetVisible(self,67,True)
                     cSetVisible(self,69,True)
                     cSetVisible(self,71,True)
                     cSetVisible(self,73,True)
                     cSetVisible(self,92,False)



             if kids_enabled:
                 self.GoBack()
                 xbmc.sleep(200)
                 cSetVisible(self,3,True)
                 cSetVisible(self,5,True)
                 cSetVisible(self,7,True)
                 cSetVisible(self,9,True)
                 cSetVisible(self,10,True)
                 cSetVisible(self,13,True)
                 cSetVisible(self,15,True)
                 cSetVisible(self,16,True)
                 cSetVisible(self,19,True)
                 cSetVisible(self,21,True)
                 cSetVisible(self,23,True)
                 cSetVisible(self,25,True)
                 cSetVisible(self,27,True)
                 cSetVisible(self,29,True)
                 ADDON.setSetting('kids.enabled', 'false')
                 profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
                 # Deletes the db file if it persists after abort
                 if os.path.exists(profilePath):
                     os.remove(profilePath)


                 if english_enabled:
                     cSetVisible(self,46,True)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,True)
                     cSetVisible(self,53,True)
                     cSetVisible(self,55,True)
                     cSetVisible(self,57,True)
                     cSetVisible(self,59,True)
                     cSetVisible(self,60,True)
                     cSetVisible(self,63,True)
                     cSetVisible(self,65,True)
                     cSetVisible(self,67,True)
                     cSetVisible(self,69,True)
                     cSetVisible(self,71,True)
                     cSetVisible(self,73,True)
                     cSetVisible(self,93,False)



             if sports_enabled:
                 self.GoBack()
                 xbmc.sleep(200)
                 cSetVisible(self,3,True)
                 cSetVisible(self,5,True)
                 cSetVisible(self,7,True)
                 cSetVisible(self,9,True)
                 cSetVisible(self,10,True)
                 cSetVisible(self,13,True)
                 cSetVisible(self,15,True)
                 cSetVisible(self,17,True)
                 cSetVisible(self,18,True)
                 cSetVisible(self,21,True)
                 cSetVisible(self,23,True)
                 cSetVisible(self,25,True)
                 cSetVisible(self,27,True)
                 cSetVisible(self,29,True)
                 ADDON.setSetting('sports.enabled', 'false')
                 profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
                 # Deletes the db file if it persists after abort
                 if os.path.exists(profilePath):
                     os.remove(profilePath)


                 if english_enabled:
                     cSetVisible(self,46,True)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,True)
                     cSetVisible(self,53,True)
                     cSetVisible(self,55,True)
                     cSetVisible(self,57,True)
                     cSetVisible(self,59,True)
                     cSetVisible(self,61,True)
                     cSetVisible(self,62,True)
                     cSetVisible(self,65,True)
                     cSetVisible(self,67,True)
                     cSetVisible(self,69,True)
                     cSetVisible(self,71,True)
                     cSetVisible(self,73,True)
                     cSetVisible(self,94,False)



             if news_enabled:
                 self.GoBack()
                 xbmc.sleep(200)
                 cSetVisible(self,3,True)
                 cSetVisible(self,5,True)
                 cSetVisible(self,7,True)
                 cSetVisible(self,9,True)
                 cSetVisible(self,10,True)
                 cSetVisible(self,13,True)
                 cSetVisible(self,15,True)
                 cSetVisible(self,17,True)
                 cSetVisible(self,19,True)
                 cSetVisible(self,20,True)
                 cSetVisible(self,23,True)
                 cSetVisible(self,25,True)
                 cSetVisible(self,27,True)
                 cSetVisible(self,29,True)
                 ADDON.setSetting('news.enabled', 'false')
                 profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
                 # Deletes the db file if it persists after abort
                 if os.path.exists(profilePath):
                     os.remove(profilePath)


                 if english_enabled:
                     cSetVisible(self,46,True)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,True)
                     cSetVisible(self,53,True)
                     cSetVisible(self,55,True)
                     cSetVisible(self,57,True)
                     cSetVisible(self,59,True)
                     cSetVisible(self,61,True)
                     cSetVisible(self,63,True)
                     cSetVisible(self,64,True)
                     cSetVisible(self,67,True)
                     cSetVisible(self,69,True)
                     cSetVisible(self,71,True)
                     cSetVisible(self,73,True)
                     cSetVisible(self,95,False)



             if documentaries_enabled:
                 self.GoBack()
                 xbmc.sleep(200)
                 cSetVisible(self,3,True)
                 cSetVisible(self,5,True)
                 cSetVisible(self,7,True)
                 cSetVisible(self,9,True)
                 cSetVisible(self,10,True)
                 cSetVisible(self,13,True)
                 cSetVisible(self,15,True)
                 cSetVisible(self,17,True)
                 cSetVisible(self,19,True)
                 cSetVisible(self,21,True)
                 cSetVisible(self,22,True)
                 cSetVisible(self,25,True)
                 cSetVisible(self,27,True)
                 cSetVisible(self,29,True)
                 ADDON.setSetting('documentaries.enabled', 'false')
                 profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
                 # Deletes the db file if it persists after abort
                 if os.path.exists(profilePath):
                     os.remove(profilePath)


                 if english_enabled:
                     cSetVisible(self,46,True)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,True)
                     cSetVisible(self,53,True)
                     cSetVisible(self,55,True)
                     cSetVisible(self,57,True)
                     cSetVisible(self,59,True)
                     cSetVisible(self,61,True)
                     cSetVisible(self,63,True)
                     cSetVisible(self,65,True)
                     cSetVisible(self,66,True)
                     cSetVisible(self,69,True)
                     cSetVisible(self,71,True)
                     cSetVisible(self,73,True)
                     cSetVisible(self,96,False)



             if musicradio_enabled:
                 self.GoBack()
                 xbmc.sleep(200)
                 cSetVisible(self,3,True)
                 cSetVisible(self,5,True)
                 cSetVisible(self,7,True)
                 cSetVisible(self,9,True)
                 cSetVisible(self,10,True)
                 cSetVisible(self,13,True)
                 cSetVisible(self,15,True)
                 cSetVisible(self,17,True)
                 cSetVisible(self,19,True)
                 cSetVisible(self,21,True)
                 cSetVisible(self,23,True)
                 cSetVisible(self,24,True)
                 cSetVisible(self,27,True)
                 cSetVisible(self,29,True)
                 ADDON.setSetting('musicradio.enabled', 'false')
                 profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
                 # Deletes the db file if it persists after abort
                 if os.path.exists(profilePath):
                     os.remove(profilePath)


                 if english_enabled:
                     cSetVisible(self,46,True)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,True)
                     cSetVisible(self,53,True)
                     cSetVisible(self,55,True)
                     cSetVisible(self,57,True)
                     cSetVisible(self,59,True)
                     cSetVisible(self,61,True)
                     cSetVisible(self,63,True)
                     cSetVisible(self,65,True)
                     cSetVisible(self,67,True)
                     cSetVisible(self,68,True)
                     cSetVisible(self,71,True)
                     cSetVisible(self,73,True)
                     cSetVisible(self,97,False)



             if adult_enabled:
                 self.GoBack()
                 xbmc.sleep(200)
                 cSetVisible(self,3,True)
                 cSetVisible(self,5,True)
                 cSetVisible(self,7,True)
                 cSetVisible(self,9,True)
                 cSetVisible(self,10,True)
                 cSetVisible(self,13,True)
                 cSetVisible(self,15,True)
                 cSetVisible(self,17,True)
                 cSetVisible(self,19,True)
                 cSetVisible(self,21,True)
                 cSetVisible(self,23,True)
                 cSetVisible(self,25,True)
                 cSetVisible(self,26,True)
                 cSetVisible(self,29,True)
                 ADDON.setSetting('adult.enabled', 'false')
                 profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
                 # Deletes the db file if it persists after abort
                 if os.path.exists(profilePath):
                     os.remove(profilePath)


                 if english_enabled:
                     cSetVisible(self,46,True)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,True)
                     cSetVisible(self,53,True)
                     cSetVisible(self,55,True)
                     cSetVisible(self,57,True)
                     cSetVisible(self,59,True)
                     cSetVisible(self,61,True)
                     cSetVisible(self,63,True)
                     cSetVisible(self,65,True)
                     cSetVisible(self,67,True)
                     cSetVisible(self,69,True)
                     cSetVisible(self,70,True)
                     cSetVisible(self,73,True)
                     cSetVisible(self,98,False)



             if favourites_enabled:
                 cSetVisible(self,3,True)
                 cSetVisible(self,5,True)
                 cSetVisible(self,7,True)
                 cSetVisible(self,9,True)
                 cSetVisible(self,10,True)
                 cSetVisible(self,13,True)
                 cSetVisible(self,15,True)
                 cSetVisible(self,17,True)
                 cSetVisible(self,19,True)
                 cSetVisible(self,21,True)
                 cSetVisible(self,23,True)
                 cSetVisible(self,25,True)
                 cSetVisible(self,27,True)
                 cSetVisible(self,28,True)
                 ADDON.setSetting('favourites.enabled', 'false')


                 if english_enabled:
                     cSetVisible(self,46,True)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,True)
                     cSetVisible(self,53,True)
                     cSetVisible(self,55,True)
                     cSetVisible(self,57,True)
                     cSetVisible(self,59,True)
                     cSetVisible(self,61,True)
                     cSetVisible(self,63,True)
                     cSetVisible(self,65,True)
                     cSetVisible(self,67,True)
                     cSetVisible(self,69,True)
                     cSetVisible(self,71,True)
                     cSetVisible(self,72,True)
                     cSetVisible(self,99,False)



             if picture_enabled:
                 cSetVisible(self,2,True)
                 cSetVisible(self,5,True)
                 cSetVisible(self,7,True)
                 cSetVisible(self,8,True)
                 cSetVisible(self,30,True)
                 cSetVisible(self,33,True)
                 cSetVisible(self,35,True)
                 cSetVisible(self,37,True)
                 cSetVisible(self,39,True)
                 cSetVisible(self,41,True)
                 cSetVisible(self,43,True)
                 cSetVisible(self,45,True)
                 cSetVisible(self,101,False)
                 cSetVisible(self,105,False)
                 cSetVisible(self,107,False)
                 cSetVisible(self,109,False)
                 cSetVisible(self,122,False)
                 cSetVisible(self,126,False)
                 cSetVisible(self,132,False)
                 cSetVisible(self,134,False)
                 cSetVisible(self,136,False)
                 cSetVisible(self,140,False)
                 cSetVisible(self,146,False)
                 cSetVisible(self,148,False)
                 cSetVisible(self,150,False)
                 cSetVisible(self,154,False)
                 cSetVisible(self,160,False)
                 cSetVisible(self,162,False)
                 cSetVisible(self,164,False)
                 cSetVisible(self,168,False)
                 cSetVisible(self,174,False)
                 cSetVisible(self,176,False)
                 cSetVisible(self,178,False)
                 cSetVisible(self,182,False)
                 cSetVisible(self,188,False)
                 cSetVisible(self,190,False)
                 cSetVisible(self,192,False)
                 cSetVisible(self,195,False)
                 cSetVisible(self,198,False)
                 cSetVisible(self,199,False)
                 cSetVisible(self,321,False)
                 ADDON.setSetting('picture.enabled', 'false')


                 if english_enabled:
                     cSetVisible(self,47,True)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,True)
                     cSetVisible(self,52,True)
                     cSetVisible(self,74,True)
                     cSetVisible(self,77,True)
                     cSetVisible(self,79,True)
                     cSetVisible(self,81,True)
                     cSetVisible(self,83,True)
                     cSetVisible(self,85,True)
                     cSetVisible(self,87,True)
                     cSetVisible(self,89,True)
                     cSetVisible(self,100,False)
                     cSetVisible(self,103,False)
                     cSetVisible(self,124,False)
                     cSetVisible(self,138,False)
                     cSetVisible(self,152,False)
                     cSetVisible(self,166,False)
                     cSetVisible(self,180,False)
                     cSetVisible(self,194,False)
                     cSetVisible(self,196,False)
                     cSetVisible(self,197,False)



             if sound_enabled:
                 cSetVisible(self,2,True)
                 cSetVisible(self,5,True)
                 cSetVisible(self,7,True)
                 cSetVisible(self,8,True)
                 cSetVisible(self,31,True)
                 cSetVisible(self,32,True)
                 cSetVisible(self,35,True)
                 cSetVisible(self,37,True)
                 cSetVisible(self,39,True)
                 cSetVisible(self,41,True)
                 cSetVisible(self,43,True)
                 cSetVisible(self,45,True)
                 cSetVisible(self,201,False)
                 cSetVisible(self,203,False)
                 cSetVisible(self,205,False)
                 cSetVisible(self,207,False)
                 cSetVisible(self,209,False)
                 cSetVisible(self,218,False)
                 cSetVisible(self,222,False)
                 cSetVisible(self,228,False)
                 cSetVisible(self,230,False)
                 cSetVisible(self,356,False)
                 cSetVisible(self,360,False)
                 cSetVisible(self,242,False)
                 cSetVisible(self,244,False)
                 cSetVisible(self,246,False)
                 cSetVisible(self,250,False)
                 cSetVisible(self,256,False)
                 cSetVisible(self,258,False)
                 cSetVisible(self,260,False)
                 cSetVisible(self,264,False)
                 cSetVisible(self,270,False)
                 cSetVisible(self,272,False)
                 cSetVisible(self,274,False)
                 cSetVisible(self,280,False)
                 cSetVisible(self,281,False)
                 cSetVisible(self,321,False)
                 ADDON.setSetting('sound.enabled', 'false')


                 if english_enabled:
                     cSetVisible(self,47,True)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,True)
                     cSetVisible(self,52,True)
                     cSetVisible(self,75,True)
                     cSetVisible(self,76,True)
                     cSetVisible(self,79,True)
                     cSetVisible(self,81,True)
                     cSetVisible(self,83,True)
                     cSetVisible(self,85,True)
                     cSetVisible(self,87,True)
                     cSetVisible(self,89,True)
                     cSetVisible(self,200,False)
                     cSetVisible(self,204,False)
                     cSetVisible(self,220,False)
                     cSetVisible(self,358,False)
                     cSetVisible(self,248,False)
                     cSetVisible(self,262,False)
                     cSetVisible(self,276,False)
                     cSetVisible(self,278,False)
                     cSetVisible(self,279,False)



             if changelanguage_enabled:
                 cSetVisible(self,2,True)
                 cSetVisible(self,5,True)
                 cSetVisible(self,7,True)
                 cSetVisible(self,8,True)
                 cSetVisible(self,31,True)
                 cSetVisible(self,33,True)
                 cSetVisible(self,34,True)
                 cSetVisible(self,37,True)
                 cSetVisible(self,39,True)
                 cSetVisible(self,41,True)
                 cSetVisible(self,43,True)
                 cSetVisible(self,45,True)
                 cSetVisible(self,282,False)
                 cSetVisible(self,283,False)
                 cSetVisible(self,287,False)
                 cSetVisible(self,288,False)
                 cSetVisible(self,289,False)
                 cSetVisible(self,291,False)
                 cSetVisible(self,318,False)
                 cSetVisible(self,321,False)
                 ADDON.setSetting('changelanguage.enabled', 'false')


                 if language_save_settings_yellow:
                     cSetVisible(self,284,False)
                     cSetVisible(self,290,False)
                     cSetVisible(self,292,False)
                     cSetVisible(self,317,False)


                     if english_enabled:
                         cSetVisible(self,286,False)
                         cSetVisible(self,319,False)


                 if english_enabled:
                     cSetVisible(self,285,False)
                     cSetVisible(self,320,False)
                     cSetVisible(self,47,True)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,True)
                     cSetVisible(self,52,True)
                     cSetVisible(self,75,True)
                     cSetVisible(self,77,True)
                     cSetVisible(self,78,True)
                     cSetVisible(self,81,True)
                     cSetVisible(self,83,True)
                     cSetVisible(self,85,True)
                     cSetVisible(self,87,True)
                     cSetVisible(self,89,True)


                     if englishblck_enabled:
                         cSetVisible(self,293,False)
                     elif englishwhte_enabled:
                         cSetVisible(self,294,False)

                     if frenchblck_enabled:
                         cSetVisible(self,295,False)
                     elif frenchwhte_enabled:
                         cSetVisible(self,296,False)


                     if germanblck_enabled:
                         cSetVisible(self,297,False)
                     elif germanwhte_enabled:
                         cSetVisible(self,298,False)


                     if italianblck_enabled:
                         cSetVisible(self,299,False)
                     elif italianwhte_enabled:
                         cSetVisible(self,300,False)


                     if spainishblck_enabled:
                         cSetVisible(self,301,False)
                     elif spainishwhte_enabled:
                         cSetVisible(self,302,False)


                     if russianblck_enabled:
                         cSetVisible(self,303,False)
                     elif russianwhte_enabled:
                         cSetVisible(self,304,False)


                     if portugueseblck_enabled:
                         cSetVisible(self,305,False)
                     elif portuguesewhte_enabled:
                         cSetVisible(self,306,False)


                     if greekblck_enabled:
                         cSetVisible(self,307,False)
                     elif greekwhte_enabled:
                         cSetVisible(self,308,False)


                     if dutchblck_enabled:
                         cSetVisible(self,309,False)
                     elif dutchwhte_enabled:
                         cSetVisible(self,310,False)


                     if chineseblck_enabled:
                         cSetVisible(self,311,False)
                     elif chinesewhte_enabled:
                         cSetVisible(self,312,False)


                     if koreanblck_enabled:
                         cSetVisible(self,313,False)
                     elif koreanwhte_enabled:
                         cSetVisible(self,314,False)


                     if arabicblck_enabled:
                         cSetVisible(self,315,False)
                     elif arabicwhte_enabled:
                         cSetVisible(self,316,False)



             if changepin_enabled:
                 print "pass"
                 if PIN_chars_4_enabled:
                     if PIN_chars_4_enabled == True:
                         cSetVisible(self,216,False)
                         cSetVisible(self,212,True)
                 elif PIN_chars_3_enabled:
                     if PIN_chars_3_enabled == True:
                         cSetVisible(self,215,False)
                         cSetVisible(self,211,True)
                 elif PIN_chars_2_enabled:
                     if PIN_chars_2_enabled == True:
                         cSetVisible(self,214,False)
                         cSetVisible(self,210,True)
                 elif PIN_chars_1_enabled:
                     if PIN_chars_1_enabled == True:
                         cSetVisible(self,213,False)
                         cSetVisible(self,209,True)
                 else:
                     cSetVisible(self,2,True)
                     cSetVisible(self,5,True)
                     cSetVisible(self,7,True)
                     cSetVisible(self,8,True)
                     cSetVisible(self,31,True)
                     cSetVisible(self,33,True)
                     cSetVisible(self,35,True)
                     cSetVisible(self,36,True)
                     cSetVisible(self,39,True)
                     cSetVisible(self,41,True)
                     cSetVisible(self,43,True)
                     cSetVisible(self,45,True)
                     cSetVisible(self,321,False)
                     cSetVisible(self,323,False)
                     cSetVisible(self,324,False)
                     cSetVisible(self,325,False)
                     cSetVisible(self,329,False)
                     cSetVisible(self,332,False)
                     cSetVisible(self,333,False)
                     cSetVisible(self,334,False)
                     cSetVisible(self,335,False)
                     ADDON.setSetting('changepin.enabled', 'false')


                     if english_enabled:
                         cSetVisible(self,47,True)
                         cSetVisible(self,49,True)
                         cSetVisible(self,51,True)
                         cSetVisible(self,52,True)
                         cSetVisible(self,75,True)
                         cSetVisible(self,77,True)
                         cSetVisible(self,79,True)
                         cSetVisible(self,80,True)
                         cSetVisible(self,83,True)
                         cSetVisible(self,85,True)
                         cSetVisible(self,87,True)
                         cSetVisible(self,89,True)
                         cSetVisible(self,326,False)
                         cSetVisible(self,327,False)
                         cSetVisible(self,328,False)
                         cSetVisible(self,330,False)
                         cSetVisible(self,331,False)



             if viewrestrictions_enabled:
                 cSetVisible(self,2,True)
                 cSetVisible(self,5,True)
                 cSetVisible(self,7,True)
                 cSetVisible(self,8,True)
                 cSetVisible(self,31,True)
                 cSetVisible(self,33,True)
                 cSetVisible(self,35,True)
                 cSetVisible(self,37,True)
                 cSetVisible(self,38,True)
                 cSetVisible(self,41,True)
                 cSetVisible(self,43,True)
                 cSetVisible(self,45,True)
                 cSetVisible(self,307,False)
                 ADDON.setSetting('viewrestrictions.enabled', 'false')


                 if english_enabled:
                     cSetVisible(self,47,True)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,True)
                     cSetVisible(self,52,True)
                     cSetVisible(self,75,True)
                     cSetVisible(self,77,True)
                     cSetVisible(self,79,True)
                     cSetVisible(self,81,True)
                     cSetVisible(self,82,True)
                     cSetVisible(self,85,True)
                     cSetVisible(self,87,True)
                     cSetVisible(self,89,True)


             if removechannels_enabled:
                 cSetVisible(self,2,True)
                 cSetVisible(self,5,True)
                 cSetVisible(self,7,True)
                 cSetVisible(self,8,True)
                 cSetVisible(self,31,True)
                 cSetVisible(self,33,True)
                 cSetVisible(self,35,True)
                 cSetVisible(self,37,True)
                 cSetVisible(self,39,True)
                 cSetVisible(self,40,True)
                 cSetVisible(self,43,True)
                 cSetVisible(self,45,True)
                 cSetVisible(self,307,False)
                 ADDON.setSetting('removechannels.enabled', 'false')


                 if english_enabled:
                     cSetVisible(self,47,True)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,True)
                     cSetVisible(self,52,True)
                     cSetVisible(self,75,True)
                     cSetVisible(self,77,True)
                     cSetVisible(self,79,True)
                     cSetVisible(self,81,True)
                     cSetVisible(self,83,True)
                     cSetVisible(self,84,True)
                     cSetVisible(self,87,True)
                     cSetVisible(self,89,True)


             if systemdetails_enabled:
                 cSetVisible(self,2,True)
                 cSetVisible(self,5,True)
                 cSetVisible(self,7,True)
                 cSetVisible(self,8,True)
                 cSetVisible(self,31,True)
                 cSetVisible(self,33,True)
                 cSetVisible(self,35,True)
                 cSetVisible(self,37,True)
                 cSetVisible(self,39,True)
                 cSetVisible(self,41,True)
                 cSetVisible(self,42,True)
                 cSetVisible(self,45,True)
                 cSetVisible(self,307,False)
                 ADDON.setSetting('systemdetails.enabled', 'false')


                 if english_enabled:
                     cSetVisible(self,47,True)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,True)
                     cSetVisible(self,52,True)
                     cSetVisible(self,75,True)
                     cSetVisible(self,77,True)
                     cSetVisible(self,79,True)
                     cSetVisible(self,81,True)
                     cSetVisible(self,83,True)
                     cSetVisible(self,85,True)
                     cSetVisible(self,86,True)
                     cSetVisible(self,89,True)


             if speedtest_enabled:
                 cSetVisible(self,2,True)
                 cSetVisible(self,5,True)
                 cSetVisible(self,7,True)
                 cSetVisible(self,8,True)
                 cSetVisible(self,31,True)
                 cSetVisible(self,33,True)
                 cSetVisible(self,35,True)
                 cSetVisible(self,37,True)
                 cSetVisible(self,39,True)
                 cSetVisible(self,41,True)
                 cSetVisible(self,43,True)
                 cSetVisible(self,44,True)
                 cSetVisible(self,307,False)
                 ADDON.setSetting('speedtest.enabled', 'false')


                 if english_enabled:
                     cSetVisible(self,47,True)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,True)
                     cSetVisible(self,52,True)
                     cSetVisible(self,75,True)
                     cSetVisible(self,77,True)
                     cSetVisible(self,79,True)
                     cSetVisible(self,81,True)
                     cSetVisible(self,83,True)
                     cSetVisible(self,85,True)
                     cSetVisible(self,87,True)
                     cSetVisible(self,88,True)


             elif tvguide_yellow == True:
                 self.close()
                 return
             elif reminders_yellow == True:
                 self.close()
                 return
             elif recorded_yellow == True:
                 self.close()
                 return
             elif settings_yellow == True:
                 self.close()
                 return



         if action == ACTION_ENTER:
             if allchannels_enabled:
                 if self.channels_Index != len(self.program_buttons) - 1:
                     self.playStreamUrl()


             if tvguide_yellow:
                 if allchannels_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,3,False)
                     cSetVisible(self,4,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,9,False)
                     cSetVisible(self,11,False)
                     cSetVisible(self,13,False)
                     cSetVisible(self,15,False)
                     cSetVisible(self,17,False)
                     cSetVisible(self,19,False)
                     cSetVisible(self,21,False)
                     cSetVisible(self,23,False)
                     cSetVisible(self,25,False)
                     cSetVisible(self,27,False)
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,False)
                     cSetVisible(self,31,False)
                     cSetVisible(self,33,False)
                     cSetVisible(self,35,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     cSetVisible(self,340,True)
                     cSetVisible(self,343,True)
                     self.getControl(343).setLabel("0%")
                     ADDON.setSetting('allchannels.enabled', 'true')
                     self.thread = AllChannelsThread(self.All_Channels_BACKUP)
                     self.thread.start()




                     if englishblck_enabled == False:
                         cSetVisible(self,46,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,53,False)
                         cSetVisible(self,54,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)
                         cSetVisible(self,90,True)




                 if entertainment_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,3,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,9,False)
                     cSetVisible(self,10,False)
                     cSetVisible(self,12,False)
                     cSetVisible(self,15,False)
                     cSetVisible(self,17,False)
                     cSetVisible(self,19,False)
                     cSetVisible(self,21,False)
                     cSetVisible(self,23,False)
                     cSetVisible(self,25,False)
                     cSetVisible(self,27,False)
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,False)
                     cSetVisible(self,31,False)
                     cSetVisible(self,33,False)
                     cSetVisible(self,35,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     ADDON.setSetting('entertainment.enabled', 'true')


                     #get language
                     if english_enabled:
                         cSetVisible(self,46,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,53,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,56,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)
                         cSetVisible(self,91,True)




                 if movies_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,3,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,9,False)
                     cSetVisible(self,10,False)
                     cSetVisible(self,13,False)
                     cSetVisible(self,14,False)
                     cSetVisible(self,17,False)
                     cSetVisible(self,19,False)
                     cSetVisible(self,21,False)
                     cSetVisible(self,23,False)
                     cSetVisible(self,25,False)
                     cSetVisible(self,27,False)
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,False)
                     cSetVisible(self,31,False)
                     cSetVisible(self,33,False)
                     cSetVisible(self,35,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     ADDON.setSetting('movies.enabled', 'true')

                     #get language
                     if english_enabled:
                         cSetVisible(self,46,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,53,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,58,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)
                         cSetVisible(self,92,True)



                 if kids_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,3,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,9,False)
                     cSetVisible(self,10,False)
                     cSetVisible(self,13,False)
                     cSetVisible(self,15,False)
                     cSetVisible(self,16,False)
                     cSetVisible(self,19,False)
                     cSetVisible(self,21,False)
                     cSetVisible(self,23,False)
                     cSetVisible(self,25,False)
                     cSetVisible(self,27,False)
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,False)
                     cSetVisible(self,31,False)
                     cSetVisible(self,33,False)
                     cSetVisible(self,35,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     ADDON.setSetting('kids.enabled', 'true')

                     #get language
                     if english_enabled:
                         cSetVisible(self,46,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,53,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,60,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)
                         cSetVisible(self,93,True)




                 if sports_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,3,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,9,False)
                     cSetVisible(self,10,False)
                     cSetVisible(self,13,False)
                     cSetVisible(self,15,False)
                     cSetVisible(self,17,False)
                     cSetVisible(self,18,False)
                     cSetVisible(self,21,False)
                     cSetVisible(self,23,False)
                     cSetVisible(self,25,False)
                     cSetVisible(self,27,False)
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,False)
                     cSetVisible(self,31,False)
                     cSetVisible(self,33,False)
                     cSetVisible(self,35,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     ADDON.setSetting('sports.enabled', 'true')

                     #get language
                     if english_enabled:
                         cSetVisible(self,46,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,53,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,62,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)
                         cSetVisible(self,94,True)



                 if news_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,3,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,9,False)
                     cSetVisible(self,10,False)
                     cSetVisible(self,13,False)
                     cSetVisible(self,15,False)
                     cSetVisible(self,17,False)
                     cSetVisible(self,19,False)
                     cSetVisible(self,20,False)
                     cSetVisible(self,23,False)
                     cSetVisible(self,25,False)
                     cSetVisible(self,27,False)
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,False)
                     cSetVisible(self,31,False)
                     cSetVisible(self,33,False)
                     cSetVisible(self,35,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     cSetVisible(self,52,False)
                     ADDON.setSetting('news.enabled', 'true')

                     #get language
                     if english_enabled:
                         cSetVisible(self,46,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,53,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,64,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)
                         cSetVisible(self,95,True)



                 if documentaries_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,3,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,9,False)
                     cSetVisible(self,10,False)
                     cSetVisible(self,13,False)
                     cSetVisible(self,15,False)
                     cSetVisible(self,17,False)
                     cSetVisible(self,19,False)
                     cSetVisible(self,21,False)
                     cSetVisible(self,22,False)
                     cSetVisible(self,25,False)
                     cSetVisible(self,27,False)
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,False)
                     cSetVisible(self,31,False)
                     cSetVisible(self,33,False)
                     cSetVisible(self,35,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     cSetVisible(self,52,False)
                     ADDON.setSetting('documentaries.enabled', 'true')

                     #get language
                     if english_enabled:
                         cSetVisible(self,46,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,53,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,66,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)
                         cSetVisible(self,96,True)




                 if musicradio_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,3,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,9,False)
                     cSetVisible(self,10,False)
                     cSetVisible(self,13,False)
                     cSetVisible(self,15,False)
                     cSetVisible(self,17,False)
                     cSetVisible(self,19,False)
                     cSetVisible(self,21,False)
                     cSetVisible(self,23,False)
                     cSetVisible(self,24,False)
                     cSetVisible(self,27,False)
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,False)
                     cSetVisible(self,31,False)
                     cSetVisible(self,33,False)
                     cSetVisible(self,35,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     cSetVisible(self,52,False)
                     ADDON.setSetting('musicradio.enabled', 'true')

                     #get language
                     if english_enabled:
                         cSetVisible(self,46,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,53,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,68,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)
                         cSetVisible(self,97,True)



                 if adult_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,3,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,9,False)
                     cSetVisible(self,10,False)
                     cSetVisible(self,13,False)
                     cSetVisible(self,15,False)
                     cSetVisible(self,17,False)
                     cSetVisible(self,19,False)
                     cSetVisible(self,21,False)
                     cSetVisible(self,23,False)
                     cSetVisible(self,25,False)
                     cSetVisible(self,26,False)
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,False)
                     cSetVisible(self,31,False)
                     cSetVisible(self,33,False)
                     cSetVisible(self,35,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     ADDON.setSetting('adult.enabled', 'true')

                     #get language
                     if english_enabled:
                         cSetVisible(self,46,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,53,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,70,False)
                         cSetVisible(self,73,False)
                         cSetVisible(self,98,True)



                 if favourites_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,3,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,9,False)
                     cSetVisible(self,10,False)
                     cSetVisible(self,13,False)
                     cSetVisible(self,15,False)
                     cSetVisible(self,17,False)
                     cSetVisible(self,19,False)
                     cSetVisible(self,21,False)
                     cSetVisible(self,23,False)
                     cSetVisible(self,25,False)
                     cSetVisible(self,27,False)
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,False)
                     cSetVisible(self,31,False)
                     cSetVisible(self,33,False)
                     cSetVisible(self,35,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     ADDON.setSetting('favourites.enabled', 'true')


                     #get language
                     if english_enabled:
                         cSetVisible(self,46,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,53,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,72,False)
                         cSetVisible(self,99,True)




             elif settings_yellow:
                 if picture_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,8,False)
                     cSetVisible(self,30,False)
                     cSetVisible(self,33,False)
                     cSetVisible(self,35,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     cSetVisible(self,105,True)
                     cSetVisible(self,107,True)
                     cSetVisible(self,109,True)
                     cSetVisible(self,122,True)
                     cSetVisible(self,126,True)
                     cSetVisible(self,132,True)
                     cSetVisible(self,134,True)
                     cSetVisible(self,136,True)
                     cSetVisible(self,140,True)
                     cSetVisible(self,146,True)
                     cSetVisible(self,148,True)
                     cSetVisible(self,150,True)
                     cSetVisible(self,154,True)
                     cSetVisible(self,160,True)
                     cSetVisible(self,162,True)
                     cSetVisible(self,164,True)
                     cSetVisible(self,168,True)
                     cSetVisible(self,174,True)
                     cSetVisible(self,176,True)
                     cSetVisible(self,178,True)
                     cSetVisible(self,182,True)
                     cSetVisible(self,188,True)
                     cSetVisible(self,190,True)
                     cSetVisible(self,192,True)
                     cSetVisible(self,195,True)
                     cSetVisible(self,198,True)
                     cSetVisible(self,199,True)
                     cSetVisible(self,321,True)
                     ADDON.setSetting('picture.enabled', 'true')


                     if english_enabled:
                         cSetVisible(self,47,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,52,False)
                         cSetVisible(self,74,False)
                         cSetVisible(self,77,False)
                         cSetVisible(self,79,False)
                         cSetVisible(self,81,False)
                         cSetVisible(self,83,False)
                         cSetVisible(self,85,False)
                         cSetVisible(self,87,False)
                         cSetVisible(self,89,False)
                         cSetVisible(self,100,True)
                         cSetVisible(self,101,True)
                         cSetVisible(self,103,True)
                         cSetVisible(self,124,True)
                         cSetVisible(self,138,True)
                         cSetVisible(self,152,True)
                         cSetVisible(self,166,True)
                         cSetVisible(self,180,True)
                         cSetVisible(self,194,True)
                         cSetVisible(self,196,True)
                         cSetVisible(self,197,True)



                 if sound_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,8,False)
                     cSetVisible(self,31,False)
                     cSetVisible(self,32,False)
                     cSetVisible(self,35,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     cSetVisible(self,201,True)
                     cSetVisible(self,205,True)
                     cSetVisible(self,207,True)
                     cSetVisible(self,209,True)
                     cSetVisible(self,218,True)
                     cSetVisible(self,222,True)
                     cSetVisible(self,228,True)
                     cSetVisible(self,230,True)
                     cSetVisible(self,356,True)
                     cSetVisible(self,360,True)
                     cSetVisible(self,242,True)
                     cSetVisible(self,244,True)
                     cSetVisible(self,246,True)
                     cSetVisible(self,250,True)
                     cSetVisible(self,256,True)
                     cSetVisible(self,258,True)
                     cSetVisible(self,260,True)
                     cSetVisible(self,264,True)
                     cSetVisible(self,270,True)
                     cSetVisible(self,272,True)
                     cSetVisible(self,274,True)
                     cSetVisible(self,276,True)
                     cSetVisible(self,277,True)
                     cSetVisible(self,280,True)
                     cSetVisible(self,281,True)
                     cSetVisible(self,321,True)
                     ADDON.setSetting('sound.enabled', 'true')


                     if english_enabled:
                         cSetVisible(self,47,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,52,False)
                         cSetVisible(self,75,False)
                         cSetVisible(self,76,False)
                         cSetVisible(self,79,False)
                         cSetVisible(self,81,False)
                         cSetVisible(self,83,False)
                         cSetVisible(self,85,False)
                         cSetVisible(self,87,False)
                         cSetVisible(self,89,False)
                         cSetVisible(self,200,True)
                         cSetVisible(self,203,True)
                         cSetVisible(self,220,True)
                         cSetVisible(self,358,True)
                         cSetVisible(self,248,True)
                         cSetVisible(self,262,True)
                         cSetVisible(self,276,True)
                         cSetVisible(self,278,True)
                         cSetVisible(self,279,True)


                 if changelanguage_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,8,False)
                     cSetVisible(self,31,False)
                     cSetVisible(self,33,False)
                     cSetVisible(self,34,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     cSetVisible(self,282,True)
                     cSetVisible(self,283,True)
                     cSetVisible(self,287,True)
                     cSetVisible(self,289,True)
                     cSetVisible(self,291,True)
                     cSetVisible(self,318,True)
                     cSetVisible(self,321,True)
                     ADDON.setSetting('changelanguage.enabled', 'true')


                     if english_enabled:
                         cSetVisible(self,47,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,52,False)
                         cSetVisible(self,75,False)
                         cSetVisible(self,77,False)
                         cSetVisible(self,78,False)
                         cSetVisible(self,81,False)
                         cSetVisible(self,83,False)
                         cSetVisible(self,85,False)
                         cSetVisible(self,87,False)
                         cSetVisible(self,89,False)
                         cSetVisible(self,285,True)
                         cSetVisible(self,293,True)
                         cSetVisible(self,320,True)




                 if changepin_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,8,False)
                     cSetVisible(self,31,False)
                     cSetVisible(self,33,False)
                     cSetVisible(self,35,False)
                     cSetVisible(self,36,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     cSetVisible(self,321,True)
                     cSetVisible(self,323,True)
                     cSetVisible(self,324,True)
                     cSetVisible(self,325,True)
                     cSetVisible(self,329,True)
                     cSetVisible(self,332,True)
                     cSetVisible(self,333,True)
                     cSetVisible(self,334,True)
                     cSetVisible(self,335,True)
                     ADDON.setSetting('changepin.enabled', 'true')


                     if english_enabled:
                         cSetVisible(self,47,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,52,False)
                         cSetVisible(self,75,False)
                         cSetVisible(self,77,False)
                         cSetVisible(self,79,False)
                         cSetVisible(self,80,False)
                         cSetVisible(self,83,False)
                         cSetVisible(self,85,False)
                         cSetVisible(self,87,False)
                         cSetVisible(self,89,False)
                         cSetVisible(self,326,True)
                         cSetVisible(self,327,True)
                         cSetVisible(self,328,True)
                         cSetVisible(self,330,True)
                         cSetVisible(self,331,True)



                 if viewrestrictions_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,8,False)
                     cSetVisible(self,31,False)
                     cSetVisible(self,33,False)
                     cSetVisible(self,35,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,38,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     cSetVisible(self,307,True)
                     ADDON.setSetting('viewrestrictions.enabled', 'true')


                     if english_enabled:
                         cSetVisible(self,47,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,52,False)
                         cSetVisible(self,75,False)
                         cSetVisible(self,77,False)
                         cSetVisible(self,79,False)
                         cSetVisible(self,81,False)
                         cSetVisible(self,82,False)
                         cSetVisible(self,85,False)
                         cSetVisible(self,87,False)
                         cSetVisible(self,89,False)



                 if removechannels_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,8,False)
                     cSetVisible(self,31,False)
                     cSetVisible(self,33,False)
                     cSetVisible(self,35,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,40,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     cSetVisible(self,307,True)
                     ADDON.setSetting('removechannels.enabled', 'true')


                     if english_enabled:
                         cSetVisible(self,47,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,52,False)
                         cSetVisible(self,75,False)
                         cSetVisible(self,77,False)
                         cSetVisible(self,79,False)
                         cSetVisible(self,81,False)
                         cSetVisible(self,83,False)
                         cSetVisible(self,84,False)
                         cSetVisible(self,87,False)
                         cSetVisible(self,89,False)



                 if systemdetails_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,8,False)
                     cSetVisible(self,31,False)
                     cSetVisible(self,33,False)
                     cSetVisible(self,35,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,42,False)
                     cSetVisible(self,45,False)
                     cSetVisible(self,307,True)
                     ADDON.setSetting('systemdetails.enabled', 'true')


                     if english_enabled:
                         cSetVisible(self,47,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,52,False)
                         cSetVisible(self,75,False)
                         cSetVisible(self,77,False)
                         cSetVisible(self,79,False)
                         cSetVisible(self,81,False)
                         cSetVisible(self,83,False)
                         cSetVisible(self,85,False)
                         cSetVisible(self,86,False)
                         cSetVisible(self,89,False)



                 if speedtest_yellow:
                     cSetVisible(self,2,False)
                     cSetVisible(self,5,False)
                     cSetVisible(self,7,False)
                     cSetVisible(self,8,False)
                     cSetVisible(self,31,False)
                     cSetVisible(self,33,False)
                     cSetVisible(self,35,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,44,False)
                     cSetVisible(self,307,True)
                     ADDON.setSetting('speedtest.enabled', 'true')


                     if english_enabled:
                         cSetVisible(self,47,False)
                         cSetVisible(self,49,False)
                         cSetVisible(self,51,False)
                         cSetVisible(self,52,False)
                         cSetVisible(self,75,False)
                         cSetVisible(self,77,False)
                         cSetVisible(self,79,False)
                         cSetVisible(self,81,False)
                         cSetVisible(self,83,False)
                         cSetVisible(self,85,False)
                         cSetVisible(self,87,False)
                         cSetVisible(self,88,False)



             if changelanguage_enabled:
                 if language_save_settings_yellow:
                     cSetVisible(self,2,True)
                     cSetVisible(self,5,True)
                     cSetVisible(self,7,True)
                     cSetVisible(self,8,True)
                     cSetVisible(self,31,True)
                     cSetVisible(self,33,True)
                     cSetVisible(self,34,True)
                     cSetVisible(self,37,True)
                     cSetVisible(self,39,True)
                     cSetVisible(self,41,True)
                     cSetVisible(self,43,True)
                     cSetVisible(self,45,True)
                     cSetVisible(self,147,False)
                     cSetVisible(self,150,False)
                     cSetVisible(self,151,False)
                     cSetVisible(self,153,False)
                     cSetVisible(self,178,False)
                     ADDON.setSetting('changelanguage.enabled', 'false')


                     if english_enabled:
                         #cSetVisible(self,109,False)
                         cSetVisible(self,113,False)
                         cSetVisible(self,144,False)


                     if englishwhte_enabled:
                         cSetVisible(self,119,False)
                         cSetVisible(self,47,True)
                         cSetVisible(self,49,True)
                         cSetVisible(self,51,True)
                         cSetVisible(self,52,True)
                         cSetVisible(self,75,True)
                         cSetVisible(self,77,True)
                         cSetVisible(self,78,True)
                         cSetVisible(self,81,True)
                         cSetVisible(self,83,True)
                         cSetVisible(self,85,True)
                         cSetVisible(self,87,True)
                         cSetVisible(self,89,True)
                         ADDON.setSetting('english.enabled', 'true')


                     if frenchwhte_enabled:
                         cSetVisible(self,265,True)
                         ADDON.setSetting('english.enabled', 'false')
                         ADDON.setSetting('french.enabled', 'true')


                     if germanwhte_enabled:
                         self.close()




         if action == ACTION_MOVE_LEFT:
             if tvguide_yellow:
                 cSetVisible(self,3,False)
                 cSetVisible(self,2,True)
                 cSetVisible(self,9,False)
                 cSetVisible(self,8,True)
                 cSetVisible(self,10,False)
                 cSetVisible(self,11,False)
                 cSetVisible(self,12,False)
                 cSetVisible(self,13,False)
                 cSetVisible(self,14,False)
                 cSetVisible(self,15,False)
                 cSetVisible(self,16,False)
                 cSetVisible(self,17,False)
                 cSetVisible(self,18,False)
                 cSetVisible(self,19,False)
                 cSetVisible(self,20,False)
                 cSetVisible(self,21,False)
                 cSetVisible(self,22,False)
                 cSetVisible(self,23,False)
                 cSetVisible(self,24,False)
                 cSetVisible(self,25,False)
                 cSetVisible(self,26,False)
                 cSetVisible(self,27,False)
                 cSetVisible(self,28,False)
                 cSetVisible(self,29,False)
                 cSetVisible(self,30,True)
                 cSetVisible(self,33,True)
                 cSetVisible(self,35,True)
                 cSetVisible(self,37,True)
                 cSetVisible(self,39,True)
                 cSetVisible(self,41,True)
                 cSetVisible(self,43,True)
                 cSetVisible(self,45,True)


                 if english_enabled:
                     cSetVisible(self,46,False)
                     cSetVisible(self,47,True)
                     cSetVisible(self,53,False)
                     cSetVisible(self,52,True)
                     cSetVisible(self,74,True)
                     cSetVisible(self,77,True)
                     cSetVisible(self,79,True)
                     cSetVisible(self,81,True)
                     cSetVisible(self,83,True)
                     cSetVisible(self,85,True)
                     cSetVisible(self,87,True)
                     cSetVisible(self,89,True)


                 if allchannels_yellow:
                     if english_enabled:
                         cSetVisible(self,54,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)




                 if entertainment_yellow:
                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,56,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)



                 if movies_yellow:
                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,58,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)



                 if kids_yellow:
                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,60,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)


                 if sports_yellow:
                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,62,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)



                 if news_yellow:
                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,64,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)


                 if documentaries_yellow:
                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,66,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)


                 if musicradio_yellow:
                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,68,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)


                 if adult_yellow:
                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,70,False)
                         cSetVisible(self,73,False)


                 if favourites_yellow:
                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,72,False)


             if reminders_yellow:
                 cSetVisible(self,4,False)
                 cSetVisible(self,5,True)
                 cSetVisible(self,2,False)
                 cSetVisible(self,3,True)
                 cSetVisible(self,10,False)
                 cSetVisible(self,11,True)
                 cSetVisible(self,12,False)
                 cSetVisible(self,13,True)
                 cSetVisible(self,14,False)
                 cSetVisible(self,15,True)
                 cSetVisible(self,16,False)
                 cSetVisible(self,17,True)
                 cSetVisible(self,18,False)
                 cSetVisible(self,19,True)
                 cSetVisible(self,20,False)
                 cSetVisible(self,21,True)
                 cSetVisible(self,22,False)
                 cSetVisible(self,23,True)
                 cSetVisible(self,24,False)
                 cSetVisible(self,25,True)
                 cSetVisible(self,26,False)
                 cSetVisible(self,27,True)
                 cSetVisible(self,28,False)
                 cSetVisible(self,29,True)



                 if english_enabled:
                     cSetVisible(self,47,False)
                     cSetVisible(self,46,True)
                     cSetVisible(self,48,False)
                     cSetVisible(self,49,True)
                     cSetVisible(self,54,True)
                     cSetVisible(self,57,True)
                     cSetVisible(self,59,True)
                     cSetVisible(self,61,True)
                     cSetVisible(self,63,True)
                     cSetVisible(self,65,True)
                     cSetVisible(self,67,True)
                     cSetVisible(self,69,True)
                     cSetVisible(self,71,True)
                     cSetVisible(self,73,True)




             if recorded_yellow:
                 cSetVisible(self,6,False)
                 cSetVisible(self,7,True)
                 cSetVisible(self,5,False)
                 cSetVisible(self,4,True)

                 if english_enabled:
                     cSetVisible(self,50,False)
                     cSetVisible(self,51,True)
                     cSetVisible(self,49,False)
                     cSetVisible(self,48,True)



             if settings_yellow:
                 cSetVisible(self,8,False)
                 cSetVisible(self,9,True)
                 cSetVisible(self,7,False)
                 cSetVisible(self,6,True)
                 cSetVisible(self,30,False)
                 cSetVisible(self,31,False)
                 cSetVisible(self,32,False)
                 cSetVisible(self,33,False)
                 cSetVisible(self,34,False)
                 cSetVisible(self,35,False)
                 cSetVisible(self,36,False)
                 cSetVisible(self,37,False)
                 cSetVisible(self,38,False)
                 cSetVisible(self,39,False)
                 cSetVisible(self,40,False)
                 cSetVisible(self,41,False)
                 cSetVisible(self,42,False)
                 cSetVisible(self,43,False)
                 cSetVisible(self,44,False)
                 cSetVisible(self,45,False)



                 if picture_yellow:
                     if english_enabled:
                         cSetVisible(self,52,False)
                         cSetVisible(self,53,True)
                         cSetVisible(self,51,False)
                         cSetVisible(self,50,True)
                         cSetVisible(self,74,False)
                         cSetVisible(self,77,False)
                         cSetVisible(self,79,False)
                         cSetVisible(self,81,False)
                         cSetVisible(self,83,False)
                         cSetVisible(self,85,False)
                         cSetVisible(self,87,False)
                         cSetVisible(self,89,False)


                 if sound_yellow:
                     if english_enabled:
                         cSetVisible(self,52,False)
                         cSetVisible(self,53,True)
                         cSetVisible(self,51,False)
                         cSetVisible(self,50,True)
                         cSetVisible(self,75,False)
                         cSetVisible(self,76,False)
                         cSetVisible(self,79,False)
                         cSetVisible(self,81,False)
                         cSetVisible(self,83,False)
                         cSetVisible(self,85,False)
                         cSetVisible(self,87,False)
                         cSetVisible(self,89,False)


                 if changelanguage_yellow:
                     if english_enabled:
                         cSetVisible(self,52,False)
                         cSetVisible(self,53,True)
                         cSetVisible(self,51,False)
                         cSetVisible(self,50,True)
                         cSetVisible(self,75,False)
                         cSetVisible(self,77,False)
                         cSetVisible(self,78,False)
                         cSetVisible(self,81,False)
                         cSetVisible(self,83,False)
                         cSetVisible(self,85,False)
                         cSetVisible(self,87,False)
                         cSetVisible(self,89,False)


                 if changepin_yellow:
                     if english_enabled:
                         cSetVisible(self,52,False)
                         cSetVisible(self,53,True)
                         cSetVisible(self,51,False)
                         cSetVisible(self,50,True)
                         cSetVisible(self,75,False)
                         cSetVisible(self,77,False)
                         cSetVisible(self,79,False)
                         cSetVisible(self,80,False)
                         cSetVisible(self,83,False)
                         cSetVisible(self,85,False)
                         cSetVisible(self,87,False)
                         cSetVisible(self,89,False)


                 if viewrestrictions_yellow:
                     if english_enabled:
                         cSetVisible(self,52,False)
                         cSetVisible(self,53,True)
                         cSetVisible(self,51,False)
                         cSetVisible(self,50,True)
                         cSetVisible(self,75,False)
                         cSetVisible(self,77,False)
                         cSetVisible(self,79,False)
                         cSetVisible(self,81,False)
                         cSetVisible(self,82,False)
                         cSetVisible(self,85,False)
                         cSetVisible(self,87,False)
                         cSetVisible(self,89,False)


                 if removechannels_yellow:
                     if english_enabled:
                         cSetVisible(self,52,False)
                         cSetVisible(self,53,True)
                         cSetVisible(self,51,False)
                         cSetVisible(self,50,True)
                         cSetVisible(self,75,False)
                         cSetVisible(self,77,False)
                         cSetVisible(self,79,False)
                         cSetVisible(self,81,False)
                         cSetVisible(self,83,False)
                         cSetVisible(self,84,False)
                         cSetVisible(self,87,False)
                         cSetVisible(self,89,False)


                 if systemdetails_yellow:
                     if english_enabled:
                         cSetVisible(self,52,False)
                         cSetVisible(self,53,True)
                         cSetVisible(self,51,False)
                         cSetVisible(self,50,True)
                         cSetVisible(self,75,False)
                         cSetVisible(self,77,False)
                         cSetVisible(self,79,False)
                         cSetVisible(self,81,False)
                         cSetVisible(self,83,False)
                         cSetVisible(self,85,False)
                         cSetVisible(self,86,False)
                         cSetVisible(self,89,False)


                 if speedtest_yellow:
                     if english_enabled:
                         cSetVisible(self,52,False)
                         cSetVisible(self,53,True)
                         cSetVisible(self,51,False)
                         cSetVisible(self,50,True)
                         cSetVisible(self,75,False)
                         cSetVisible(self,77,False)
                         cSetVisible(self,79,False)
                         cSetVisible(self,81,False)
                         cSetVisible(self,83,False)
                         cSetVisible(self,85,False)
                         cSetVisible(self,87,False)
                         cSetVisible(self,88,False)



             if allchannels_enabled:
                 if self.channels_Index != len(self.program_buttons) - 1:
                     self.GoLeft()




             if changelanguage_enabled:
                 if englishblck_enabled == True:
                     cSetVisible(self,293,False)
                     cSetVisible(self,315,True)
                 elif frenchblck_enabled == True:
                     cSetVisible(self,295,False)
                     cSetVisible(self,293,True)
                 elif germanblck_enabled == True:
                     cSetVisible(self,297,False)
                     cSetVisible(self,295,True)
                 elif italianblck_enabled == True:
                     cSetVisible(self,299,False)
                     cSetVisible(self,297,True)
                 elif spainishblck_enabled == True:
                     cSetVisible(self,301,False)
                     cSetVisible(self,299,True)
                 elif russianblck_enabled == True:
                     cSetVisible(self,303,False)
                     cSetVisible(self,301,True)
                 elif portugueseblck_enabled == True:
                     cSetVisible(self,305,False)
                     cSetVisible(self,303,True)
                 elif greekblck_enabled == True:
                     cSetVisible(self,307,False)
                     cSetVisible(self,305,True)
                 elif dutchblck_enabled == True:
                     cSetVisible(self,309,False)
                     cSetVisible(self,307,True)
                 elif chineseblck_enabled == True:
                     cSetVisible(self,311,False)
                     cSetVisible(self,309,True)
                 elif koreanblck_enabled == True:
                     cSetVisible(self,313,False)
                     cSetVisible(self,311,True)
                 elif arabicblck_enabled == True:
                     cSetVisible(self,315,False)
                     cSetVisible(self,313,True)



         if action == ACTION_MOVE_RIGHT:
             if tvguide_yellow:
                 cSetVisible(self,3,False)
                 cSetVisible(self,2,True)
                 cSetVisible(self,5,False)
                 cSetVisible(self,4,True)
                 cSetVisible(self,11,False)
                 cSetVisible(self,12,False)
                 cSetVisible(self,13,False)
                 cSetVisible(self,15,False)
                 cSetVisible(self,17,False)
                 cSetVisible(self,19,False)
                 cSetVisible(self,21,False)
                 cSetVisible(self,23,False)
                 cSetVisible(self,25,False)
                 cSetVisible(self,27,False)
                 cSetVisible(self,29,False)


                 if english_enabled:
                     cSetVisible(self,46,False)
                     cSetVisible(self,47,True)
                     cSetVisible(self,49,False)
                     cSetVisible(self,48,True)


                 if allchannels_yellow:
                     if english_enabled:
                         cSetVisible(self,54,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)




                 if entertainment_yellow:
                     if english_enabled:
                         cSetVisible(self,10,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,56,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)


                 if movies_yellow:
                     if english_enabled:
                         cSetVisible(self,10,False)
                         cSetVisible(self,14,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,58,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)



                 if kids_yellow:
                     if english_enabled:
                         cSetVisible(self,10,False)
                         cSetVisible(self,16,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,60,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)



                 if sports_yellow:
                     if english_enabled:
                         cSetVisible(self,10,False)
                         cSetVisible(self,18,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,62,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)



                 if news_yellow:
                     if english_enabled:
                         cSetVisible(self,10,False)
                         cSetVisible(self,20,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,64,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)



                 if documentaries_yellow:
                     if english_enabled:
                         cSetVisible(self,10,False)
                         cSetVisible(self,22,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,66,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)



                 if musicradio_yellow:
                     if english_enabled:
                         cSetVisible(self,10,False)
                         cSetVisible(self,24,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,68,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,73,False)



                 if adult_yellow:
                     if english_enabled:
                         cSetVisible(self,10,False)
                         cSetVisible(self,26,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,70,False)
                         cSetVisible(self,73,False)



                 if favourites_yellow:
                     if english_enabled:
                         cSetVisible(self,10,False)
                         cSetVisible(self,28,False)
                         cSetVisible(self,55,False)
                         cSetVisible(self,57,False)
                         cSetVisible(self,59,False)
                         cSetVisible(self,61,False)
                         cSetVisible(self,63,False)
                         cSetVisible(self,65,False)
                         cSetVisible(self,67,False)
                         cSetVisible(self,69,False)
                         cSetVisible(self,71,False)
                         cSetVisible(self,72,False)



             if reminders_yellow:
                 cSetVisible(self,4,False)
                 cSetVisible(self,5,True)
                 cSetVisible(self,7,False)
                 cSetVisible(self,6,True)



                 if english_enabled:
                     cSetVisible(self,48,False)
                     cSetVisible(self,49,True)
                     cSetVisible(self,51,False)
                     cSetVisible(self,50,True)



             if recorded_yellow:
                 print "you are working on the recorded_yellow......................."
                 cSetVisible(self,6,False)
                 cSetVisible(self,7,True)
                 cSetVisible(self,9,False)
                 cSetVisible(self,8,True)
                 cSetVisible(self,30,True)
                 cSetVisible(self,33,True)
                 cSetVisible(self,35,True)
                 cSetVisible(self,37,True)
                 cSetVisible(self,39,True)
                 cSetVisible(self,41,True)
                 cSetVisible(self,43,True)
                 cSetVisible(self,45,True)


                 if english_enabled:
                     cSetVisible(self,50,False)
                     cSetVisible(self,51,True)
                     cSetVisible(self,53,False)
                     cSetVisible(self,52,True)
                     cSetVisible(self,74,True)
                     cSetVisible(self,77,True)
                     cSetVisible(self,79,True)
                     cSetVisible(self,81,True)
                     cSetVisible(self,83,True)
                     cSetVisible(self,85,True)
                     cSetVisible(self,87,True)
                     cSetVisible(self,89,True)


             if settings_yellow:
                 cSetVisible(self,8,False)
                 cSetVisible(self,9,True)
                 cSetVisible(self,2,False)
                 cSetVisible(self,3,True)
                 cSetVisible(self,11,True)
                 cSetVisible(self,13,True)
                 cSetVisible(self,15,True)
                 cSetVisible(self,17,True)
                 cSetVisible(self,19,True)
                 cSetVisible(self,21,True)
                 cSetVisible(self,23,True)
                 cSetVisible(self,25,True)
                 cSetVisible(self,27,True)
                 cSetVisible(self,29,True)
                 cSetVisible(self,30,False)
                 cSetVisible(self,33,False)
                 cSetVisible(self,35,False)
                 cSetVisible(self,37,False)
                 cSetVisible(self,39,False)
                 cSetVisible(self,41,False)
                 cSetVisible(self,43,False)
                 cSetVisible(self,45,False)


                 if picture_yellow:
                     if english_enabled:
                         cSetVisible(self,52,False)
                         cSetVisible(self,53,True)
                         cSetVisible(self,47,False)
                         cSetVisible(self,46,True)
                         cSetVisible(self,74,False)
                         cSetVisible(self,77,False)
                         cSetVisible(self,79,False)
                         cSetVisible(self,81,False)
                         cSetVisible(self,83,False)
                         cSetVisible(self,85,False)
                         cSetVisible(self,87,False)
                         cSetVisible(self,89,False)
                         cSetVisible(self,54,True)
                         cSetVisible(self,57,True)
                         cSetVisible(self,59,True)
                         cSetVisible(self,61,True)
                         cSetVisible(self,63,True)
                         cSetVisible(self,65,True)
                         cSetVisible(self,67,True)
                         cSetVisible(self,69,True)
                         cSetVisible(self,71,True)
                         cSetVisible(self,73,True)



                 if sound_yellow:
                     if english_enabled:
                         cSetVisible(self,52,False)
                         cSetVisible(self,53,True)
                         cSetVisible(self,47,False)
                         cSetVisible(self,46,True)
                         cSetVisible(self,31,False)
                         cSetVisible(self,32,False)
                         cSetVisible(self,35,False)
                         cSetVisible(self,37,False)
                         cSetVisible(self,39,False)
                         cSetVisible(self,41,False)
                         cSetVisible(self,43,False)
                         cSetVisible(self,45,False)
                         cSetVisible(self,75,False)
                         cSetVisible(self,76,False)
                         cSetVisible(self,79,False)
                         cSetVisible(self,81,False)
                         cSetVisible(self,83,False)
                         cSetVisible(self,85,False)
                         cSetVisible(self,87,False)
                         cSetVisible(self,89,False)
                         cSetVisible(self,54,True)
                         cSetVisible(self,57,True)
                         cSetVisible(self,59,True)
                         cSetVisible(self,61,True)
                         cSetVisible(self,63,True)
                         cSetVisible(self,65,True)
                         cSetVisible(self,67,True)
                         cSetVisible(self,69,True)
                         cSetVisible(self,71,True)
                         cSetVisible(self,73,True)


                 if changelanguage_yellow:
                     if english_enabled:
                         cSetVisible(self,52,False)
                         cSetVisible(self,53,True)
                         cSetVisible(self,47,False)
                         cSetVisible(self,46,True)
                         cSetVisible(self,31,False)
                         cSetVisible(self,32,False)
                         cSetVisible(self,34,False)
                         cSetVisible(self,37,False)
                         cSetVisible(self,39,False)
                         cSetVisible(self,41,False)
                         cSetVisible(self,43,False)
                         cSetVisible(self,45,False)
                         cSetVisible(self,75,False)
                         cSetVisible(self,77,False)
                         cSetVisible(self,78,False)
                         cSetVisible(self,81,False)
                         cSetVisible(self,83,False)
                         cSetVisible(self,85,False)
                         cSetVisible(self,87,False)
                         cSetVisible(self,89,False)
                         cSetVisible(self,54,True)
                         cSetVisible(self,57,True)
                         cSetVisible(self,59,True)
                         cSetVisible(self,61,True)
                         cSetVisible(self,63,True)
                         cSetVisible(self,65,True)
                         cSetVisible(self,67,True)
                         cSetVisible(self,69,True)
                         cSetVisible(self,71,True)
                         cSetVisible(self,73,True)


                 if changepin_yellow:
                     cSetVisible(self,52,False)
                     cSetVisible(self,53,True)
                     cSetVisible(self,47,False)
                     cSetVisible(self,46,True)
                     cSetVisible(self,31,False)
                     cSetVisible(self,32,False)
                     cSetVisible(self,34,False)
                     cSetVisible(self,36,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     cSetVisible(self,75,False)
                     cSetVisible(self,77,False)
                     cSetVisible(self,79,False)
                     cSetVisible(self,80,False)
                     cSetVisible(self,83,False)
                     cSetVisible(self,85,False)
                     cSetVisible(self,87,False)
                     cSetVisible(self,89,False)
                     cSetVisible(self,54,True)
                     cSetVisible(self,57,True)
                     cSetVisible(self,59,True)
                     cSetVisible(self,61,True)
                     cSetVisible(self,63,True)
                     cSetVisible(self,65,True)
                     cSetVisible(self,67,True)
                     cSetVisible(self,69,True)
                     cSetVisible(self,71,True)
                     cSetVisible(self,73,True)


                 if viewrestrictions_yellow:
                     cSetVisible(self,52,False)
                     cSetVisible(self,53,True)
                     cSetVisible(self,47,False)
                     cSetVisible(self,46,True)
                     cSetVisible(self,31,False)
                     cSetVisible(self,32,False)
                     cSetVisible(self,34,False)
                     cSetVisible(self,37,False)
                     cSetVisible(self,38,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     cSetVisible(self,75,False)
                     cSetVisible(self,77,False)
                     cSetVisible(self,79,False)
                     cSetVisible(self,81,False)
                     cSetVisible(self,82,False)
                     cSetVisible(self,85,False)
                     cSetVisible(self,87,False)
                     cSetVisible(self,89,False)
                     cSetVisible(self,54,True)
                     cSetVisible(self,57,True)
                     cSetVisible(self,59,True)
                     cSetVisible(self,61,True)
                     cSetVisible(self,63,True)
                     cSetVisible(self,65,True)
                     cSetVisible(self,67,True)
                     cSetVisible(self,69,True)
                     cSetVisible(self,71,True)
                     cSetVisible(self,73,True)


                 if removechannels_yellow:
                     cSetVisible(self,52,False)
                     cSetVisible(self,53,True)
                     cSetVisible(self,47,False)
                     cSetVisible(self,46,True)
                     cSetVisible(self,31,False)
                     cSetVisible(self,32,False)
                     cSetVisible(self,34,False)
                     cSetVisible(self,36,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,40,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,45,False)
                     cSetVisible(self,75,False)
                     cSetVisible(self,77,False)
                     cSetVisible(self,79,False)
                     cSetVisible(self,81,False)
                     cSetVisible(self,83,False)
                     cSetVisible(self,84,False)
                     cSetVisible(self,87,False)
                     cSetVisible(self,89,False)
                     cSetVisible(self,54,True)
                     cSetVisible(self,57,True)
                     cSetVisible(self,59,True)
                     cSetVisible(self,61,True)
                     cSetVisible(self,63,True)
                     cSetVisible(self,65,True)
                     cSetVisible(self,67,True)
                     cSetVisible(self,69,True)
                     cSetVisible(self,71,True)
                     cSetVisible(self,73,True)


                 if systemdetails_yellow:
                     cSetVisible(self,52,False)
                     cSetVisible(self,53,True)
                     cSetVisible(self,47,False)
                     cSetVisible(self,46,True)
                     cSetVisible(self,31,False)
                     cSetVisible(self,32,False)
                     cSetVisible(self,34,False)
                     cSetVisible(self,36,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,42,False)
                     cSetVisible(self,45,False)
                     cSetVisible(self,75,False)
                     cSetVisible(self,77,False)
                     cSetVisible(self,79,False)
                     cSetVisible(self,81,False)
                     cSetVisible(self,83,False)
                     cSetVisible(self,85,False)
                     cSetVisible(self,86,False)
                     cSetVisible(self,89,False)
                     cSetVisible(self,54,True)
                     cSetVisible(self,57,True)
                     cSetVisible(self,59,True)
                     cSetVisible(self,61,True)
                     cSetVisible(self,63,True)
                     cSetVisible(self,65,True)
                     cSetVisible(self,67,True)
                     cSetVisible(self,69,True)
                     cSetVisible(self,71,True)
                     cSetVisible(self,73,True)


                 if speedtest_yellow:
                     cSetVisible(self,52,False)
                     cSetVisible(self,53,True)
                     cSetVisible(self,47,False)
                     cSetVisible(self,46,True)
                     cSetVisible(self,31,False)
                     cSetVisible(self,32,False)
                     cSetVisible(self,34,False)
                     cSetVisible(self,36,False)
                     cSetVisible(self,39,False)
                     cSetVisible(self,41,False)
                     cSetVisible(self,43,False)
                     cSetVisible(self,44,False)
                     cSetVisible(self,75,False)
                     cSetVisible(self,77,False)
                     cSetVisible(self,79,False)
                     cSetVisible(self,81,False)
                     cSetVisible(self,83,False)
                     cSetVisible(self,85,False)
                     cSetVisible(self,87,False)
                     cSetVisible(self,88,False)
                     cSetVisible(self,54,True)
                     cSetVisible(self,57,True)
                     cSetVisible(self,59,True)
                     cSetVisible(self,61,True)
                     cSetVisible(self,63,True)
                     cSetVisible(self,65,True)
                     cSetVisible(self,67,True)
                     cSetVisible(self,69,True)
                     cSetVisible(self,71,True)
                     cSetVisible(self,73,True)



             if allchannels_enabled:
                 if self.channels_Index != len(self.program_buttons) - 1:
                     self.GoRight()



             if changelanguage_enabled:
                 if english_enabled:
                     if englishblck_enabled == True:
                         cSetVisible(self,293,False)
                         cSetVisible(self,295,True)
                     elif frenchblck_enabled == True:
                         cSetVisible(self,295,False)
                         cSetVisible(self,297,True)
                     elif germanblck_enabled == True:
                         cSetVisible(self,297,False)
                         cSetVisible(self,299,True)
                     elif italianblck_enabled == True:
                         cSetVisible(self,299,False)
                         cSetVisible(self,301,True)
                     elif spainishblck_enabled == True:
                         cSetVisible(self,301,False)
                         cSetVisible(self,303,True)
                     elif russianblck_enabled == True:
                         cSetVisible(self,303,False)
                         cSetVisible(self,305,True)
                     elif portugueseblck_enabled == True:
                         cSetVisible(self,305,False)
                         cSetVisible(self,307,True)
                     elif greekblck_enabled == True:
                         cSetVisible(self,307,False)
                         cSetVisible(self,309,True)
                     elif dutchblck_enabled == True:
                         cSetVisible(self,309,False)
                         cSetVisible(self,311,True)
                     elif chineseblck_enabled == True:
                         cSetVisible(self,311,False)
                         cSetVisible(self,313,True)
                     elif koreanblck_enabled == True:
                         cSetVisible(self,313,False)
                         cSetVisible(self,315,True)
                     elif arabicblck_enabled == True:
                         cSetVisible(self,315,False)
                         cSetVisible(self,293,True)




         if action == ACTION_MOVE_UP:
             if allchannels_enabled:
                 print self.channels_Index
                 print "passed, working"
                 self.GoUp()



             if tvguide_yellow:
                 if allchannels_yellow:
                     cSetVisible(self,11,False)
                     cSetVisible(self,10,True)
                     cSetVisible(self,29,False)
                     cSetVisible(self,28,True)


                     if english_enabled:
                         cSetVisible(self,54,False)
                         cSetVisible(self,55,True)
                         cSetVisible(self,73,False)
                         cSetVisible(self,72,True)



                 if entertainment_yellow:
                     cSetVisible(self,12,False)
                     cSetVisible(self,13,True)
                     cSetVisible(self,10,False)
                     cSetVisible(self,11,True)


                     if english_enabled:
                         cSetVisible(self,56,False)
                         cSetVisible(self,57,True)
                         cSetVisible(self,55,False)
                         cSetVisible(self,54,True)


                 if movies_yellow:
                     cSetVisible(self,14,False)
                     cSetVisible(self,15,True)
                     cSetVisible(self,13,False)
                     cSetVisible(self,12,True)


                     if english_enabled:
                         cSetVisible(self,58,False)
                         cSetVisible(self,59,True)
                         cSetVisible(self,57,False)
                         cSetVisible(self,56,True)


                 if kids_yellow:
                     cSetVisible(self,16,False)
                     cSetVisible(self,17,True)
                     cSetVisible(self,15,False)
                     cSetVisible(self,14,True)


                     if english_enabled:
                         cSetVisible(self,60,False)
                         cSetVisible(self,61,True)
                         cSetVisible(self,59,False)
                         cSetVisible(self,58,True)


                 if sports_yellow:
                     cSetVisible(self,18,False)
                     cSetVisible(self,19,True)
                     cSetVisible(self,17,False)
                     cSetVisible(self,16,True)


                     if english_enabled:
                         cSetVisible(self,62,False)
                         cSetVisible(self,63,True)
                         cSetVisible(self,61,False)
                         cSetVisible(self,60,True)


                 if news_yellow:
                     cSetVisible(self,20,False)
                     cSetVisible(self,21,True)
                     cSetVisible(self,19,False)
                     cSetVisible(self,18,True)


                     if english_enabled:
                         cSetVisible(self,64,False)
                         cSetVisible(self,65,True)
                         cSetVisible(self,63,False)
                         cSetVisible(self,62,True)


                 if documentaries_yellow:
                     cSetVisible(self,22,False)
                     cSetVisible(self,23,True)
                     cSetVisible(self,21,False)
                     cSetVisible(self,20,True)


                     if english_enabled:
                         cSetVisible(self,66,False)
                         cSetVisible(self,67,True)
                         cSetVisible(self,65,False)
                         cSetVisible(self,64,True)


                 if musicradio_yellow:
                     cSetVisible(self,24,False)
                     cSetVisible(self,25,True)
                     cSetVisible(self,23,False)
                     cSetVisible(self,22,True)


                         
                     if english_enabled:
                         cSetVisible(self,68,False)
                         cSetVisible(self,69,True)
                         cSetVisible(self,67,False)
                         cSetVisible(self,66,True)


                 if adult_yellow:
                     cSetVisible(self,26,False)
                     cSetVisible(self,27,True)
                     cSetVisible(self,25,False)
                     cSetVisible(self,24,True)


                     if english_enabled:
                         cSetVisible(self,70,False)
                         cSetVisible(self,71,True)
                         cSetVisible(self,69,False)
                         cSetVisible(self,68,True)


                 if favourites_yellow:
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,True)
                     cSetVisible(self,27,False)
                     cSetVisible(self,26,True)


                     if english_enabled:
                         cSetVisible(self,72,False)
                         cSetVisible(self,73,True)
                         cSetVisible(self,71,False)
                         cSetVisible(self,70,True)




             if settings_yellow:
                 if picture_yellow:
                     cSetVisible(self,30,False)
                     cSetVisible(self,31,True)
                     cSetVisible(self,45,False)
                     cSetVisible(self,44,True)
                         
                         
                     if english_enabled:
                         cSetVisible(self,74,False)
                         cSetVisible(self,75,True)
                         cSetVisible(self,89,False)
                         cSetVisible(self,88,True)


                 if sound_yellow:
                     cSetVisible(self,32,False)
                     cSetVisible(self,33,True)
                     cSetVisible(self,31,False)
                     cSetVisible(self,30,True)


                     if english_enabled:
                         cSetVisible(self,76,False)
                         cSetVisible(self,77,True)
                         cSetVisible(self,75,False)
                         cSetVisible(self,74,True)


                 if changelanguage_yellow:
                     cSetVisible(self,34,False)
                     cSetVisible(self,35,True)
                     cSetVisible(self,33,False)
                     cSetVisible(self,32,True)


                     if english_enabled:
                         cSetVisible(self,78,False)
                         cSetVisible(self,79,True)
                         cSetVisible(self,77,False)
                         cSetVisible(self,76,True)


                 if changepin_yellow:
                     cSetVisible(self,36,False)
                     cSetVisible(self,37,True)
                     cSetVisible(self,35,False)
                     cSetVisible(self,34,True)


                     if english_enabled:
                         cSetVisible(self,80,False)
                         cSetVisible(self,81,True)
                         cSetVisible(self,79,False)
                         cSetVisible(self,78,True)


                 if viewrestrictions_yellow:
                     cSetVisible(self,38,False)
                     cSetVisible(self,39,True)
                     cSetVisible(self,37,False)
                     cSetVisible(self,36,True)


                     if english_enabled:
                         cSetVisible(self,82,False)
                         cSetVisible(self,83,True)
                         cSetVisible(self,81,False)
                         cSetVisible(self,80,True)


                 if removechannels_yellow:
                     cSetVisible(self,40,False)
                     cSetVisible(self,41,True)
                     cSetVisible(self,39,False)
                     cSetVisible(self,38,True)


                     if english_enabled:
                         cSetVisible(self,84,False)
                         cSetVisible(self,85,True)
                         cSetVisible(self,83,False)
                         cSetVisible(self,82,True)


                 if systemdetails_yellow:
                     cSetVisible(self,42,False)
                     cSetVisible(self,43,True)
                     cSetVisible(self,41,False)
                     cSetVisible(self,40,True)


                     if english_enabled:
                         cSetVisible(self,86,False)
                         cSetVisible(self,87,True)
                         cSetVisible(self,85,False)
                         cSetVisible(self,84,True)


                 if speedtest_yellow:
                     cSetVisible(self,44,False)
                     cSetVisible(self,45,True)
                     cSetVisible(self,43,False)
                     cSetVisible(self,42,True)


                     if english_enabled:
                         cSetVisible(self,88,False)
                         cSetVisible(self,89,True)
                         cSetVisible(self,87,False)
                         cSetVisible(self,86,True)



             if changelanguage_enabled:
                 if language_yellow == True:
                     print "hello chris 1"
                     #cSetVisible(self,146a,False)
                     cSetVisible(self,147,False)
                     cSetVisible(self,150,False)
                     cSetVisible(self,151,False)
                     cSetVisible(self,152,False)
                     cSetVisible(self,153,True)
                     cSetVisible(self,179,False)
                     cSetVisible(self,178,True)



                     if english_enabled:
                         cSetVisible(self,112,False)
                         cSetVisible(self,113,True)
                         cSetVisible(self,145,False)
                         cSetVisible(self,144,True)


                     if englishblck_enabled:
                         cSetVisible(self,154,False)
                         cSetVisible(self,155,True)

                     if frenchblck_enabled:
                         cSetVisible(self,156,False)
                         cSetVisible(self,157,True)

                     if germanblck_enabled:
                         cSetVisible(self,158,False)
                         cSetVisible(self,159,True)

                     if italianblck_enabled:
                         cSetVisible(self,160,False)
                         cSetVisible(self,161,True)

                     if spainishblck_enabled:
                         cSetVisible(self,162,False)
                         cSetVisible(self,163,True)

                     if russianblck_enabled:
                         cSetVisible(self,164,False)
                         cSetVisible(self,165,True)

                     if portugueseblck_enabled:
                         cSetVisible(self,166,False)
                         cSetVisible(self,167,True)

                     if greekblck_enabled:
                         cSetVisible(self,168,False)
                         cSetVisible(self,169,True)

                     if dutchblck_enabled:
                         cSetVisible(self,170,False)
                         cSetVisible(self,171,True)

                     if chineseblck_enabled:
                         cSetVisible(self,172,False)
                         cSetVisible(self,173,True)

                     if koreanblck_enabled:
                         cSetVisible(self,174,False)
                         cSetVisible(self,175,True)

                     if arabicblck_enabled:
                         cSetVisible(self,176,False)
                         cSetVisible(self,177,True)



                 elif language_blue == True:
                     print "hello chris 2"
                     cSetVisible(self,317,False)
                     cSetVisible(self,318,True)
                     cSetVisible(self,284,False)
                     cSetVisible(self,283,True)
                     cSetVisible(self,288,False)
                     cSetVisible(self,287,True)
                     cSetVisible(self,290,False)
                     cSetVisible(self,289,True)
                     cSetVisible(self,292,False)
                     cSetVisible(self,291,True)



                     if english_enabled:
                         cSetVisible(self,319,False)
                         cSetVisible(self,320,True)
                         cSetVisible(self,286,False)
                         cSetVisible(self,285,True)


                         if englishwhte_enabled:
                             cSetVisible(self,294,False)
                             cSetVisible(self,293,True)

                         if frenchwhte_enabled:
                             cSetVisible(self,296,False)
                             cSetVisible(self,295,True)

                         if germanwhte_enabled:
                             cSetVisible(self,298,False)
                             cSetVisible(self,297,True)

                         if italianwhte_enabled:
                             cSetVisible(self,300,False)
                             cSetVisible(self,299,True)

                         if spainishwhte_enabled:
                             cSetVisible(self,302,False)
                             cSetVisible(self,301,True)

                         if russianwhte_enabled:
                             cSetVisible(self,304,False)
                             cSetVisible(self,303,True)

                         if portuguesewhte_enabled:
                             cSetVisible(self,306,False)
                             cSetVisible(self,305,True)

                         if greekwhte_enabled:
                             cSetVisible(self,308,False)
                             cSetVisible(self,307,True)

                         if dutchwhte_enabled:
                             cSetVisible(self,310,False)
                             cSetVisible(self,309,True)

                         if chinesewhte_enabled:
                             cSetVisible(self,312,False)
                             cSetVisible(self,311,True)

                         if koreanwhte_enabled:
                             cSetVisible(self,314,False)
                             cSetVisible(self,313,True)

                         if arabicwhte_enabled:
                             cSetVisible(self,316,False)
                             cSetVisible(self,315,True)




         if action == ACTION_MOVE_DOWN:
             if allchannels_enabled:
                 self.GoDown()

                 if self.channels_Index >= 6:
                     pass



             if tvguide_yellow:
                 if allchannels_yellow:
                     cSetVisible(self,11,False)
                     cSetVisible(self,10,True)
                     cSetVisible(self,13,False)
                     cSetVisible(self,12,True)


                     if english_enabled:
                         cSetVisible(self,54,False)
                         cSetVisible(self,55,True)
                         cSetVisible(self,57,False)
                         cSetVisible(self,56,True)




                 if entertainment_yellow:
                     cSetVisible(self,12,False)
                     cSetVisible(self,13,True)
                     cSetVisible(self,15,False)
                     cSetVisible(self,14,True)


                     if english_enabled:
                         cSetVisible(self,56,False)
                         cSetVisible(self,57,True)
                         cSetVisible(self,59,False)
                         cSetVisible(self,58,True)



                 if movies_yellow:
                     cSetVisible(self,14,False)
                     cSetVisible(self,15,True)
                     cSetVisible(self,17,False)
                     cSetVisible(self,16,True)


                     if english_enabled:
                         cSetVisible(self,58,False)
                         cSetVisible(self,59,True)
                         cSetVisible(self,61,False)
                         cSetVisible(self,60,True)



                 if kids_yellow:
                     cSetVisible(self,16,False)
                     cSetVisible(self,17,True)
                     cSetVisible(self,19,False)
                     cSetVisible(self,18,True)


                     if english_enabled:
                         cSetVisible(self,60,False)
                         cSetVisible(self,61,True)
                         cSetVisible(self,63,False)
                         cSetVisible(self,62,True)



                 if sports_yellow:
                     cSetVisible(self,18,False)
                     cSetVisible(self,19,True)
                     cSetVisible(self,21,False)
                     cSetVisible(self,20,True)


                     if english_enabled:
                         cSetVisible(self,62,False)
                         cSetVisible(self,63,True)
                         cSetVisible(self,65,False)
                         cSetVisible(self,64,True)




                 if news_yellow:
                     cSetVisible(self,20,False)
                     cSetVisible(self,21,True)
                     cSetVisible(self,23,False)
                     cSetVisible(self,22,True)


                     if english_enabled:
                         cSetVisible(self,64,False)
                         cSetVisible(self,65,True)
                         cSetVisible(self,67,False)
                         cSetVisible(self,66,True)



                 if documentaries_yellow:
                     cSetVisible(self,22,False)
                     cSetVisible(self,23,True)
                     cSetVisible(self,25,False)
                     cSetVisible(self,24,True)


                     if english_enabled:
                         cSetVisible(self,66,False)
                         cSetVisible(self,67,True)
                         cSetVisible(self,69,False)
                         cSetVisible(self,68,True)



                 if musicradio_yellow:
                     cSetVisible(self,24,False)
                     cSetVisible(self,25,True)
                     cSetVisible(self,27,False)
                     cSetVisible(self,26,True)


                     if english_enabled:
                         cSetVisible(self,68,False)
                         cSetVisible(self,69,True)
                         cSetVisible(self,71,False)
                         cSetVisible(self,70,True)



                 if adult_yellow:
                     cSetVisible(self,26,False)
                     cSetVisible(self,27,True)
                     cSetVisible(self,29,False)
                     cSetVisible(self,28,True)


                     if english_enabled:
                         cSetVisible(self,70,False)
                         cSetVisible(self,71,True)
                         cSetVisible(self,73,False)
                         cSetVisible(self,72,True)



                 if favourites_yellow:
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,True)
                     cSetVisible(self,10,False)
                     cSetVisible(self,11,True)


                     if english_enabled:
                         cSetVisible(self,72,False)
                         cSetVisible(self,73,True)
                         cSetVisible(self,55,False)
                         cSetVisible(self,54,True)





             if settings_yellow:
                 if picture_yellow:
                     cSetVisible(self,30,False)
                     cSetVisible(self,31,True)
                     cSetVisible(self,33,False)
                     cSetVisible(self,32,True)


                     if english_enabled:
                         cSetVisible(self,74,False)
                         cSetVisible(self,75,True)
                         cSetVisible(self,77,False)
                         cSetVisible(self,76,True)


                 if sound_yellow:
                     cSetVisible(self,32,False)
                     cSetVisible(self,33,True)
                     cSetVisible(self,35,False)
                     cSetVisible(self,34,True)


                     if english_enabled:
                         cSetVisible(self,76,False)
                         cSetVisible(self,77,True)
                         cSetVisible(self,79,False)
                         cSetVisible(self,78,True)



                 if changelanguage_yellow:
                     cSetVisible(self,34,False)
                     cSetVisible(self,35,True)
                     cSetVisible(self,37,False)
                     cSetVisible(self,36,True)


                     if english_enabled:
                         cSetVisible(self,78,False)
                         cSetVisible(self,79,True)
                         cSetVisible(self,81,False)
                         cSetVisible(self,80,True)



                 if changepin_yellow:
                     cSetVisible(self,36,False)
                     cSetVisible(self,37,True)
                     cSetVisible(self,39,False)
                     cSetVisible(self,38,True)


                     if english_enabled:
                         cSetVisible(self,80,False)
                         cSetVisible(self,81,True)
                         cSetVisible(self,83,False)
                         cSetVisible(self,82,True)



                 if viewrestrictions_yellow:
                     cSetVisible(self,38,False)
                     cSetVisible(self,39,True)
                     cSetVisible(self,41,False)
                     cSetVisible(self,40,True)


                     if english_enabled:
                         cSetVisible(self,82,False)
                         cSetVisible(self,83,True)
                         cSetVisible(self,85,False)
                         cSetVisible(self,84,True)



                 if removechannels_yellow:
                     cSetVisible(self,40,False)
                     cSetVisible(self,41,True)
                     cSetVisible(self,43,False)
                     cSetVisible(self,42,True)


                     if english_enabled:
                         cSetVisible(self,84,False)
                         cSetVisible(self,85,True)
                         cSetVisible(self,87,False)
                         cSetVisible(self,86,True)



                 if systemdetails_yellow:
                     cSetVisible(self,42,False)
                     cSetVisible(self,43,True)
                     cSetVisible(self,45,False)
                     cSetVisible(self,44,True)


                     if english_enabled:
                         cSetVisible(self,86,False)
                         cSetVisible(self,87,True)
                         cSetVisible(self,89,False)
                         cSetVisible(self,88,True)



                 if speedtest_yellow:
                     cSetVisible(self,44,False)
                     cSetVisible(self,45,True)
                     cSetVisible(self,31,False)
                     cSetVisible(self,30,True)


                     if english_enabled:
                         cSetVisible(self,88,False)
                         cSetVisible(self,89,True)
                         cSetVisible(self,75,False)
                         cSetVisible(self,74,True)



             if changelanguage_enabled:
                 if language_yellow == True:
                     cSetVisible(self,283,False)
                     cSetVisible(self,284,True)
                     cSetVisible(self,287,False)
                     cSetVisible(self,288,True)
                     cSetVisible(self,289,False)
                     cSetVisible(self,290,True)
                     cSetVisible(self,291,False)
                     cSetVisible(self,292,True)
                     cSetVisible(self,318,False)
                     cSetVisible(self,317,True)


                     if english_enabled:
                         print "you are working on language 1............................"
                         cSetVisible(self,285,False)
                         cSetVisible(self,286,True)
                         cSetVisible(self,320,False)
                         cSetVisible(self,319,True)


                     if englishblck_enabled:
                         cSetVisible(self,293,False)
                         cSetVisible(self,294,True)


                     if frenchblck_enabled:
                         cSetVisible(self,295,False)
                         cSetVisible(self,296,True)


                     if germanblck_enabled:
                         cSetVisible(self,297,False)
                         cSetVisible(self,298,True)


                     if italianblck_enabled:
                         cSetVisible(self,299,False)
                         cSetVisible(self,300,True)


                     if spainishblck_enabled:
                         cSetVisible(self,301,False)
                         cSetVisible(self,302,True)


                     if russianblck_enabled:
                         cSetVisible(self,303,False)
                         cSetVisible(self,304,True)


                     if portugueseblck_enabled:
                         cSetVisible(self,305,False)
                         cSetVisible(self,306,True)


                     if greekblck_enabled:
                         cSetVisible(self,307,False)
                         cSetVisible(self,308,True)


                     if dutchblck_enabled:
                         cSetVisible(self,309,False)
                         cSetVisible(self,310,True)


                     if chineseblck_enabled:
                         cSetVisible(self,311,False)
                         cSetVisible(self,312,True)


                     if koreanblck_enabled:
                         cSetVisible(self,313,False)
                         cSetVisible(self,314,True)


                     if arabicblck_enabled:
                         cSetVisible(self,315,False)
                         cSetVisible(self,316,True)



                 elif language_blue == True:
                     print "you are working on this 2"
                     cSetVisible(self,283,False)
                     cSetVisible(self,284,True)
                     cSetVisible(self,287,False)
                     cSetVisible(self,288,True)
                     cSetVisible(self,318,False)
                     cSetVisible(self,317,True)



                     if english_enabled:
                         print "you are working on language 2............................"
                         cSetVisible(self,285,False)
                         cSetVisible(self,286,True)
                         cSetVisible(self,320,False)
                         cSetVisible(self,319,True)


                         if englishwhte_enabled:
                             cSetVisible(self,293,False)
                             cSetVisible(self,294,True)

                         if frenchwhte_enabled:
                             cSetVisible(self,295,False)
                             cSetVisible(self,296,True)

                         if germanwhte_enabled:
                             cSetVisible(self,297,False)
                             cSetVisible(self,298,True)

                         if italianwhte_enabled:
                             cSetVisible(self,299,False)
                             cSetVisible(self,300,True)

                         if spainishwhte_enabled:
                             cSetVisible(self,301,False)
                             cSetVisible(self,302,True)

                         if russianwhte_enabled:
                             cSetVisible(self,303,False)
                             cSetVisible(self,304,True)

                         if portuguesewhte_enabled:
                             cSetVisible(self,305,False)
                             cSetVisible(self,306,True)

                         if greekwhte_enabled:
                             cSetVisible(self,307,False)
                             cSetVisible(self,308,True)

                         if dutchwhte_enabled:
                             cSetVisible(self,309,False)
                             cSetVisible(self,310,True)

                         if chinesewhte_enabled:
                             cSetVisible(self,311,False)
                             cSetVisible(self,312,True)

                         if koreanwhte_enabled:
                             cSetVisible(self,313,False)
                             cSetVisible(self,314,True)

                         if arabicwhte_enabled:
                             cSetVisible(self,315,False)
                             cSetVisible(self,316,True)




         if action == ACTION_NUMBER1:
             if tvguide_yellow:
                 if allchannels_yellow:
                     pass


                 elif entertainment_yellow:
                     cSetVisible(self,10,False)
                     cSetVisible(self,11,True)
                     cSetVisible(self,12,False)
                     cSetVisible(self,13,True)


                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,54,True)
                         cSetVisible(self,56,False)
                         cSetVisible(self,57,True)


                 elif movies_yellow:
                     cSetVisible(self,10,False)
                     cSetVisible(self,11,True)
                     cSetVisible(self,14,False)
                     cSetVisible(self,15,True)


                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,54,True)
                         cSetVisible(self,58,False)
                         cSetVisible(self,59,True)


                 elif kids_yellow:
                     cSetVisible(self,10,False)
                     cSetVisible(self,11,True)
                     cSetVisible(self,16,False)
                     cSetVisible(self,17,True)


                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,54,True)
                         cSetVisible(self,60,False)
                         cSetVisible(self,61,True)


                 elif sports_yellow:
                     cSetVisible(self,10,False)
                     cSetVisible(self,11,True)
                     cSetVisible(self,18,False)
                     cSetVisible(self,19,True)


                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,54,True)
                         cSetVisible(self,62,False)
                         cSetVisible(self,63,True)


                 elif news_yellow:
                     cSetVisible(self,10,False)
                     cSetVisible(self,11,True)
                     cSetVisible(self,20,False)
                     cSetVisible(self,21,True)


                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,54,True)
                         cSetVisible(self,64,False)
                         cSetVisible(self,65,True)


                 elif documentaries_yellow:
                     cSetVisible(self,10,False)
                     cSetVisible(self,11,True)
                     cSetVisible(self,22,False)
                     cSetVisible(self,23,True)


                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,54,True)
                         cSetVisible(self,66,False)
                         cSetVisible(self,67,True)


                 elif musicradio_yellow:
                     cSetVisible(self,10,False)
                     cSetVisible(self,11,True)
                     cSetVisible(self,24,False)
                     cSetVisible(self,25,True)


                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,54,True)
                         cSetVisible(self,68,False)
                         cSetVisible(self,69,True)


                 elif adult_yellow:
                     cSetVisible(self,10,False)
                     cSetVisible(self,11,True)
                     cSetVisible(self,26,False)
                     cSetVisible(self,27,True)


                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,54,True)
                         cSetVisible(self,70,False)
                         cSetVisible(self,71,True)


                 elif favourites_yellow:
                     cSetVisible(self,10,False)
                     cSetVisible(self,11,True)
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,True)


                     if english_enabled:
                         cSetVisible(self,55,False)
                         cSetVisible(self,54,True)
                         cSetVisible(self,72,False)
                         cSetVisible(self,73,True)




             elif settings_yellow:
                 if picture_yellow:
                     pass
                 elif sound_yellow:
                     cSetVisible(self,32,False)
                     cSetVisible(self,33,True)
                     cSetVisible(self,31,False)
                     cSetVisible(self,30,True)

                     if english_enabled:
                         cSetVisible(self,76,False)
                         cSetVisible(self,77,True)
                         cSetVisible(self,75,False)
                         cSetVisible(self,74,True)



                 elif changelanguage_yellow:
                     cSetVisible(self,34,False)
                     cSetVisible(self,35,True)
                     cSetVisible(self,31,False)
                     cSetVisible(self,30,True)

                     if english_enabled:
                         cSetVisible(self,78,False)
                         cSetVisible(self,79,True)
                         cSetVisible(self,75,False)
                         cSetVisible(self,74,True)


                 elif changepin_yellow:
                     cSetVisible(self,36,False)
                     cSetVisible(self,37,True)
                     cSetVisible(self,31,False)
                     cSetVisible(self,30,True)

                     if english_enabled:
                         cSetVisible(self,80,False)
                         cSetVisible(self,81,True)
                         cSetVisible(self,75,False)
                         cSetVisible(self,74,True)


                 elif viewrestrictions_yellow:
                     cSetVisible(self,38,False)
                     cSetVisible(self,39,True)
                     cSetVisible(self,31,False)
                     cSetVisible(self,30,True)

                     if english_enabled:
                         cSetVisible(self,82,False)
                         cSetVisible(self,83,True)
                         cSetVisible(self,75,False)
                         cSetVisible(self,74,True)


                 elif removechannels_yellow:
                     cSetVisible(self,40,False)
                     cSetVisible(self,41,True)
                     cSetVisible(self,31,False)
                     cSetVisible(self,30,True)

                     if english_enabled:
                         cSetVisible(self,84,False)
                         cSetVisible(self,85,True)
                         cSetVisible(self,75,False)
                         cSetVisible(self,74,True)


                 elif systemdetails_yellow:
                     cSetVisible(self,42,False)
                     cSetVisible(self,43,True)
                     cSetVisible(self,31,False)
                     cSetVisible(self,30,True)

                     if english_enabled:
                         cSetVisible(self,86,False)
                         cSetVisible(self,87,True)
                         cSetVisible(self,75,False)
                         cSetVisible(self,74,True)


                 elif speedtest_yellow:
                     cSetVisible(self,44,False)
                     cSetVisible(self,45,True)
                     cSetVisible(self,31,False)
                     cSetVisible(self,30,True)

                     if english_enabled:
                         cSetVisible(self,88,False)
                         cSetVisible(self,89,True)
                         cSetVisible(self,75,False)
                         cSetVisible(self,74,True)




             elif changepin_enabled:
                 if PIN_1_enabled:
                     if PIN_1_enabled == True:
                         cSetVisible(self,209,False)
                         cSetVisible(self,213,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)


                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)


                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)


                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                     elif PIN_4_enabled == False:
                         pass




         if action == ACTION_NUMBER2:
             if tvguide_yellow:
                 if allchannels_yellow:
                     cSetVisible(self,11,False)
                     cSetVisible(self,10,True)
                     cSetVisible(self,13,False)
                     cSetVisible(self,12,True)


                     if english_enabled:
                         cSetVisible(self,54,False)
                         cSetVisible(self,55,True)
                         cSetVisible(self,57,False)
                         cSetVisible(self,56,True)


                 elif entertainment_yellow:
                     pass


                 elif movies_yellow:
                     cSetVisible(self,14,False)
                     cSetVisible(self,15,True)
                     cSetVisible(self,13,False)
                     cSetVisible(self,12,True)


                     if english_enabled:
                         cSetVisible(self,58,False)
                         cSetVisible(self,59,True)
                         cSetVisible(self,57,False)
                         cSetVisible(self,56,True)


                 elif kids_yellow:
                     cSetVisible(self,16,False)
                     cSetVisible(self,17,True)
                     cSetVisible(self,13,False)
                     cSetVisible(self,12,True)


                     if english_enabled:
                         cSetVisible(self,60,False)
                         cSetVisible(self,61,True)
                         cSetVisible(self,57,False)
                         cSetVisible(self,56,True)


                 elif sports_yellow:
                     cSetVisible(self,18,False)
                     cSetVisible(self,19,True)
                     cSetVisible(self,13,False)
                     cSetVisible(self,12,True)


                     if english_enabled:
                         cSetVisible(self,62,False)
                         cSetVisible(self,63,True)
                         cSetVisible(self,57,False)
                         cSetVisible(self,56,True)


                 elif news_yellow:
                     cSetVisible(self,20,False)
                     cSetVisible(self,21,True)
                     cSetVisible(self,13,False)
                     cSetVisible(self,12,True)


                     if english_enabled:
                         cSetVisible(self,64,False)
                         cSetVisible(self,65,True)
                         cSetVisible(self,57,False)
                         cSetVisible(self,56,True)


                 elif documentaries_yellow:
                     cSetVisible(self,22,False)
                     cSetVisible(self,23,True)
                     cSetVisible(self,13,False)
                     cSetVisible(self,12,True)


                     if english_enabled:
                         cSetVisible(self,66,False)
                         cSetVisible(self,67,True)
                         cSetVisible(self,57,False)
                         cSetVisible(self,56,True)


                 elif musicradio_yellow:
                     cSetVisible(self,24,False)
                     cSetVisible(self,25,True)
                     cSetVisible(self,13,False)
                     cSetVisible(self,12,True)


                     if english_enabled:
                         cSetVisible(self,68,False)
                         cSetVisible(self,69,True)
                         cSetVisible(self,57,False)
                         cSetVisible(self,56,True)


                 elif adult_yellow:
                     cSetVisible(self,26,False)
                     cSetVisible(self,27,True)
                     cSetVisible(self,13,False)
                     cSetVisible(self,12,True)


                     if english_enabled:
                         cSetVisible(self,70,False)
                         cSetVisible(self,71,True)
                         cSetVisible(self,57,False)
                         cSetVisible(self,56,True)


                 elif favourites_yellow:
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,True)
                     cSetVisible(self,13,False)
                     cSetVisible(self,12,True)


                     if english_enabled:
                         cSetVisible(self,72,False)
                         cSetVisible(self,73,True)
                         cSetVisible(self,57,False)
                         cSetVisible(self,56,True)




             elif settings_yellow:
                 if picture_yellow:
                     cSetVisible(self,30,False)
                     cSetVisible(self,31,True)
                     cSetVisible(self,33,False)
                     cSetVisible(self,32,True)

                     if english_enabled:
                         cSetVisible(self,74,False)
                         cSetVisible(self,75,True)
                         cSetVisible(self,77,False)
                         cSetVisible(self,76,True)


                 elif sound_yellow:
                     pass


                 elif changelanguage_yellow:
                     cSetVisible(self,34,False)
                     cSetVisible(self,35,True)
                     cSetVisible(self,33,False)
                     cSetVisible(self,32,True)

                     if english_enabled:
                         cSetVisible(self,78,False)
                         cSetVisible(self,79,True)
                         cSetVisible(self,77,False)
                         cSetVisible(self,76,True)


                 elif changepin_yellow:
                     cSetVisible(self,36,False)
                     cSetVisible(self,37,True)
                     cSetVisible(self,33,False)
                     cSetVisible(self,32,True)

                     if english_enabled:
                         cSetVisible(self,80,False)
                         cSetVisible(self,81,True)
                         cSetVisible(self,77,False)
                         cSetVisible(self,76,True)


                 elif viewrestrictions_yellow:
                     cSetVisible(self,38,False)
                     cSetVisible(self,39,True)
                     cSetVisible(self,33,False)
                     cSetVisible(self,32,True)

                     if english_enabled:
                         cSetVisible(self,82,False)
                         cSetVisible(self,83,True)
                         cSetVisible(self,77,False)
                         cSetVisible(self,76,True)


                 elif removechannels_yellow:
                     cSetVisible(self,40,False)
                     cSetVisible(self,41,True)
                     cSetVisible(self,33,False)
                     cSetVisible(self,32,True)

                     if english_enabled:
                         cSetVisible(self,84,False)
                         cSetVisible(self,85,True)
                         cSetVisible(self,77,False)
                         cSetVisible(self,76,True)


                 elif systemdetails_yellow:
                     cSetVisible(self,42,False)
                     cSetVisible(self,43,True)
                     cSetVisible(self,33,False)
                     cSetVisible(self,32,True)

                     if english_enabled:
                         cSetVisible(self,86,False)
                         cSetVisible(self,87,True)
                         cSetVisible(self,77,False)
                         cSetVisible(self,76,True)


                 elif speedtest_yellow:
                     cSetVisible(self,44,False)
                     cSetVisible(self,45,True)
                     cSetVisible(self,33,False)
                     cSetVisible(self,32,True)

                     if english_enabled:
                         cSetVisible(self,88,False)
                         cSetVisible(self,89,True)
                         cSetVisible(self,77,False)
                         cSetVisible(self,76,True)




             elif changepin_enabled:
                 if PIN_1_enabled:
                     if PIN_1_enabled == True:
                         cSetVisible(self,209,False)
                         cSetVisible(self,213,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                     elif PIN_4_enabled == False:
                         pass




         if action == ACTION_NUMBER3:
             if tvguide_yellow:
                 if allchannels_yellow:
                     cSetVisible(self,11,False)
                     cSetVisible(self,10,True)
                     cSetVisible(self,15,False)
                     cSetVisible(self,14,True)


                     if english_enabled:
                         cSetVisible(self,54,False)
                         cSetVisible(self,55,True)
                         cSetVisible(self,59,False)
                         cSetVisible(self,58,True)


                 elif entertainment_yellow:
                     cSetVisible(self,12,False)
                     cSetVisible(self,13,True)
                     cSetVisible(self,15,False)
                     cSetVisible(self,14,True)
                     ADDON.setSetting('movies.enabled', 'true')


                     if english_enabled:
                         cSetVisible(self,56,False)
                         cSetVisible(self,57,True)
                         cSetVisible(self,59,False)
                         cSetVisible(self,58,True)


                 elif movies_yellow:
                     pass


                 elif kids_yellow:
                     cSetVisible(self,16,False)
                     cSetVisible(self,17,True)
                     cSetVisible(self,15,False)
                     cSetVisible(self,14,True)


                     if english_enabled:
                         cSetVisible(self,60,False)
                         cSetVisible(self,61,True)
                         cSetVisible(self,59,False)
                         cSetVisible(self,58,True)


                 elif sports_yellow:
                     cSetVisible(self,18,False)
                     cSetVisible(self,19,True)
                     cSetVisible(self,15,False)
                     cSetVisible(self,14,True)


                     if english_enabled:
                         cSetVisible(self,62,False)
                         cSetVisible(self,63,True)
                         cSetVisible(self,59,False)
                         cSetVisible(self,58,True)


                 elif news_yellow:
                     cSetVisible(self,20,False)
                     cSetVisible(self,21,True)
                     cSetVisible(self,15,False)
                     cSetVisible(self,14,True)


                     if english_enabled:
                         cSetVisible(self,64,False)
                         cSetVisible(self,65,True)
                         cSetVisible(self,59,False)
                         cSetVisible(self,58,True)


                 elif documentaries_yellow:
                     cSetVisible(self,22,False)
                     cSetVisible(self,23,True)
                     cSetVisible(self,15,False)
                     cSetVisible(self,14,True)


                     if english_enabled:
                         cSetVisible(self,66,False)
                         cSetVisible(self,67,True)
                         cSetVisible(self,59,False)
                         cSetVisible(self,58,True)


                 elif musicradio_yellow:
                     cSetVisible(self,24,False)
                     cSetVisible(self,25,True)
                     cSetVisible(self,15,False)
                     cSetVisible(self,14,True)


                     if english_enabled:
                         cSetVisible(self,68,False)
                         cSetVisible(self,69,True)
                         cSetVisible(self,59,False)
                         cSetVisible(self,58,True)


                 elif adult_yellow:
                     cSetVisible(self,26,False)
                     cSetVisible(self,27,True)
                     cSetVisible(self,15,False)
                     cSetVisible(self,14,True)


                     if english_enabled:
                         cSetVisible(self,70,False)
                         cSetVisible(self,71,True)
                         cSetVisible(self,59,False)
                         cSetVisible(self,58,True)


                 elif favourites_yellow:
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,True)
                     cSetVisible(self,15,False)
                     cSetVisible(self,14,True)


                     if english_enabled:
                         cSetVisible(self,72,False)
                         cSetVisible(self,73,True)
                         cSetVisible(self,59,False)
                         cSetVisible(self,58,True)



             elif settings_yellow:
                 if picture_yellow:
                     cSetVisible(self,30,False)
                     cSetVisible(self,31,True)
                     cSetVisible(self,35,False)
                     cSetVisible(self,34,True)

                     if english_enabled:
                         cSetVisible(self,74,False)
                         cSetVisible(self,75,True)
                         cSetVisible(self,79,False)
                         cSetVisible(self,78,True)


                 elif sound_yellow:
                     cSetVisible(self,32,False)
                     cSetVisible(self,33,True)
                     cSetVisible(self,35,False)
                     cSetVisible(self,34,True)

                     if english_enabled:
                         cSetVisible(self,76,False)
                         cSetVisible(self,77,True)
                         cSetVisible(self,79,False)
                         cSetVisible(self,78,True)


                 elif changelanguage_yellow:
                     pass


                 elif changepin_yellow:
                     cSetVisible(self,36,False)
                     cSetVisible(self,37,True)
                     cSetVisible(self,35,False)
                     cSetVisible(self,34,True)

                     if english_enabled:
                         cSetVisible(self,80,False)
                         cSetVisible(self,81,True)
                         cSetVisible(self,79,False)
                         cSetVisible(self,78,True)


                 elif viewrestrictions_yellow:
                     cSetVisible(self,38,False)
                     cSetVisible(self,39,True)
                     cSetVisible(self,35,False)
                     cSetVisible(self,34,True)

                     if english_enabled:
                         cSetVisible(self,82,False)
                         cSetVisible(self,83,True)
                         cSetVisible(self,79,False)
                         cSetVisible(self,78,True)


                 elif removechannels_yellow:
                     cSetVisible(self,40,False)
                     cSetVisible(self,41,True)
                     cSetVisible(self,35,False)
                     cSetVisible(self,34,True)

                     if english_enabled:
                         cSetVisible(self,84,False)
                         cSetVisible(self,85,True)
                         cSetVisible(self,79,False)
                         cSetVisible(self,78,True)


                 elif systemdetails_yellow:
                     cSetVisible(self,42,False)
                     cSetVisible(self,43,True)
                     cSetVisible(self,35,False)
                     cSetVisible(self,34,True)

                     if english_enabled:
                         cSetVisible(self,86,False)
                         cSetVisible(self,87,True)
                         cSetVisible(self,79,False)
                         cSetVisible(self,78,True)


                 elif speedtest_yellow:
                     cSetVisible(self,44,False)
                     cSetVisible(self,45,True)
                     cSetVisible(self,35,False)
                     cSetVisible(self,34,True)

                     if english_enabled:
                         cSetVisible(self,88,False)
                         cSetVisible(self,89,True)
                         cSetVisible(self,79,False)
                         cSetVisible(self,78,True)




             elif changepin_enabled:
                 if PIN_1_enabled:
                     if PIN_1_enabled == True:
                         cSetVisible(self,209,False)
                         cSetVisible(self,213,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                     elif PIN_4_enabled == False:
                         pass




         if action == ACTION_NUMBER4:
             if tvguide_yellow:
                 if allchannels_yellow:
                     cSetVisible(self,11,False)
                     cSetVisible(self,10,True)
                     cSetVisible(self,17,False)
                     cSetVisible(self,16,True)


                     if english_enabled:
                         cSetVisible(self,54,False)
                         cSetVisible(self,55,True)
                         cSetVisible(self,61,False)
                         cSetVisible(self,60,True)


                 elif entertainment_yellow:
                     cSetVisible(self,12,False)
                     cSetVisible(self,13,True)
                     cSetVisible(self,17,False)
                     cSetVisible(self,16,True)


                     if english_enabled:
                         cSetVisible(self,56,False)
                         cSetVisible(self,57,True)
                         cSetVisible(self,61,False)
                         cSetVisible(self,60,True)


                 elif movies_yellow:
                     cSetVisible(self,14,False)
                     cSetVisible(self,15,True)
                     cSetVisible(self,17,False)
                     cSetVisible(self,16,True)


                     if english_enabled:
                         cSetVisible(self,58,False)
                         cSetVisible(self,59,True)
                         cSetVisible(self,61,False)
                         cSetVisible(self,60,True)


                 elif kids_yellow:
                     pass


                 elif sports_yellow:
                     cSetVisible(self,18,False)
                     cSetVisible(self,19,True)
                     cSetVisible(self,17,False)
                     cSetVisible(self,16,True)


                     if english_enabled:
                         cSetVisible(self,62,False)
                         cSetVisible(self,63,True)
                         cSetVisible(self,61,False)
                         cSetVisible(self,60,True)


                 elif news_yellow:
                     cSetVisible(self,20,False)
                     cSetVisible(self,21,True)
                     cSetVisible(self,17,False)
                     cSetVisible(self,16,True)


                     if english_enabled:
                         cSetVisible(self,64,False)
                         cSetVisible(self,65,True)
                         cSetVisible(self,61,False)
                         cSetVisible(self,60,True)


                 elif documentaries_yellow:
                     cSetVisible(self,22,False)
                     cSetVisible(self,23,True)
                     cSetVisible(self,17,False)
                     cSetVisible(self,16,True)


                     if english_enabled:
                         cSetVisible(self,66,False)
                         cSetVisible(self,67,True)
                         cSetVisible(self,61,False)
                         cSetVisible(self,60,True)


                 elif musicradio_yellow:
                     cSetVisible(self,24,False)
                     cSetVisible(self,25,True)
                     cSetVisible(self,17,False)
                     cSetVisible(self,16,True)


                     if english_enabled:
                         cSetVisible(self,68,False)
                         cSetVisible(self,69,True)
                         cSetVisible(self,61,False)
                         cSetVisible(self,60,True)


                 elif adult_yellow:
                     cSetVisible(self,26,False)
                     cSetVisible(self,27,True)
                     cSetVisible(self,17,False)
                     cSetVisible(self,16,True)


                     if english_enabled:
                         cSetVisible(self,70,False)
                         cSetVisible(self,71,True)
                         cSetVisible(self,61,False)
                         cSetVisible(self,60,True)


                 elif favourites_yellow:
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,True)
                     cSetVisible(self,17,False)
                     cSetVisible(self,16,True)


                     if english_enabled:
                         cSetVisible(self,72,False)
                         cSetVisible(self,73,True)
                         cSetVisible(self,61,False)
                         cSetVisible(self,60,True)




             elif settings_yellow:
                 if picture_yellow:
                     cSetVisible(self,30,False)
                     cSetVisible(self,31,True)
                     cSetVisible(self,37,False)
                     cSetVisible(self,36,True)

                     if english_enabled:
                         cSetVisible(self,74,False)
                         cSetVisible(self,75,True)
                         cSetVisible(self,81,False)
                         cSetVisible(self,80,True)


                 elif sound_yellow:
                     cSetVisible(self,32,False)
                     cSetVisible(self,33,True)
                     cSetVisible(self,37,False)
                     cSetVisible(self,36,True)

                     if english_enabled:
                         cSetVisible(self,76,False)
                         cSetVisible(self,77,True)
                         cSetVisible(self,81,False)
                         cSetVisible(self,80,True)


                 elif changelanguage_yellow:
                     cSetVisible(self,34,False)
                     cSetVisible(self,35,True)
                     cSetVisible(self,37,False)
                     cSetVisible(self,36,True)

                     if english_enabled:
                         cSetVisible(self,78,False)
                         cSetVisible(self,79,True)
                         cSetVisible(self,81,False)
                         cSetVisible(self,80,True)


                 elif changepin_yellow:
                     pass


                 elif viewrestrictions_yellow:
                     cSetVisible(self,38,False)
                     cSetVisible(self,39,True)
                     cSetVisible(self,37,False)
                     cSetVisible(self,36,True)

                     if english_enabled:
                         cSetVisible(self,82,False)
                         cSetVisible(self,83,True)
                         cSetVisible(self,81,False)
                         cSetVisible(self,80,True)


                 elif removechannels_yellow:
                     cSetVisible(self,40,False)
                     cSetVisible(self,41,True)
                     cSetVisible(self,37,False)
                     cSetVisible(self,36,True)

                     if english_enabled:
                         cSetVisible(self,84,False)
                         cSetVisible(self,85,True)
                         cSetVisible(self,81,False)
                         cSetVisible(self,80,True)


                 elif systemdetails_yellow:
                     cSetVisible(self,42,False)
                     cSetVisible(self,43,True)
                     cSetVisible(self,37,False)
                     cSetVisible(self,36,True)

                     if english_enabled:
                         cSetVisible(self,86,False)
                         cSetVisible(self,87,True)
                         cSetVisible(self,81,False)
                         cSetVisible(self,80,True)


                 elif speedtest_yellow:
                     cSetVisible(self,44,False)
                     cSetVisible(self,45,True)
                     cSetVisible(self,37,False)
                     cSetVisible(self,36,True)

                     if english_enabled:
                         cSetVisible(self,88,False)
                         cSetVisible(self,89,True)
                         cSetVisible(self,81,False)
                         cSetVisible(self,80,True)




             elif changepin_enabled:
                 if PIN_1_enabled:
                     if PIN_1_enabled == True:
                         cSetVisible(self,209,False)
                         cSetVisible(self,213,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                     elif PIN_4_enabled == False:
                         pass




         if action == ACTION_NUMBER5:
             if tvguide_yellow:
                 if allchannels_yellow:
                     cSetVisible(self,11,False)
                     cSetVisible(self,10,True)
                     cSetVisible(self,19,False)
                     cSetVisible(self,18,True)


                     if english_enabled:
                         cSetVisible(self,54,False)
                         cSetVisible(self,55,True)
                         cSetVisible(self,63,False)
                         cSetVisible(self,62,True)


                 elif entertainment_yellow:
                     cSetVisible(self,12,False)
                     cSetVisible(self,13,True)
                     cSetVisible(self,19,False)
                     cSetVisible(self,18,True)


                     if english_enabled:
                         cSetVisible(self,56,False)
                         cSetVisible(self,57,True)
                         cSetVisible(self,63,False)
                         cSetVisible(self,62,True)


                 elif movies_yellow:
                     cSetVisible(self,14,False)
                     cSetVisible(self,15,True)
                     cSetVisible(self,19,False)
                     cSetVisible(self,18,True)


                     if english_enabled:
                         cSetVisible(self,58,False)
                         cSetVisible(self,59,True)
                         cSetVisible(self,63,False)
                         cSetVisible(self,62,True)


                 elif kids_yellow:
                     cSetVisible(self,16,False)
                     cSetVisible(self,17,True)
                     cSetVisible(self,19,False)
                     cSetVisible(self,18,True)


                     if english_enabled:
                         cSetVisible(self,60,False)
                         cSetVisible(self,61,True)
                         cSetVisible(self,63,False)
                         cSetVisible(self,62,True)


                 elif sports_yellow:
                     pass


                 elif news_yellow:
                     cSetVisible(self,20,False)
                     cSetVisible(self,21,True)
                     cSetVisible(self,19,False)
                     cSetVisible(self,18,True)


                     if english_enabled:
                         cSetVisible(self,64,False)
                         cSetVisible(self,65,True)
                         cSetVisible(self,63,False)
                         cSetVisible(self,62,True)


                 elif documentaries_yellow:
                     cSetVisible(self,22,False)
                     cSetVisible(self,23,True)
                     cSetVisible(self,19,False)
                     cSetVisible(self,18,True)


                     if english_enabled:
                         cSetVisible(self,66,False)
                         cSetVisible(self,67,True)
                         cSetVisible(self,63,False)
                         cSetVisible(self,62,True)


                 elif musicradio_yellow:
                     cSetVisible(self,24,False)
                     cSetVisible(self,25,True)
                     cSetVisible(self,19,False)
                     cSetVisible(self,18,True)


                     if english_enabled:
                         cSetVisible(self,68,False)
                         cSetVisible(self,69,True)
                         cSetVisible(self,63,False)
                         cSetVisible(self,62,True)


                 elif adult_yellow:
                     cSetVisible(self,26,False)
                     cSetVisible(self,27,True)
                     cSetVisible(self,19,False)
                     cSetVisible(self,18,True)


                     if english_enabled:
                         cSetVisible(self,70,False)
                         cSetVisible(self,71,True)
                         cSetVisible(self,63,False)
                         cSetVisible(self,62,True)


                 elif favourites_yellow:
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,True)
                     cSetVisible(self,19,False)
                     cSetVisible(self,18,True)


                     if english_enabled:
                         cSetVisible(self,72,False)
                         cSetVisible(self,73,True)
                         cSetVisible(self,63,False)
                         cSetVisible(self,62,True)




             elif settings_yellow:
                 if picture_yellow:
                     cSetVisible(self,30,False)
                     cSetVisible(self,31,True)
                     cSetVisible(self,39,False)
                     cSetVisible(self,38,True)

                     if english_enabled:
                         cSetVisible(self,74,False)
                         cSetVisible(self,75,True)
                         cSetVisible(self,83,False)
                         cSetVisible(self,82,True)


                 elif sound_yellow:
                     cSetVisible(self,32,False)
                     cSetVisible(self,33,True)
                     cSetVisible(self,39,False)
                     cSetVisible(self,38,True)

                     if english_enabled:
                         cSetVisible(self,76,False)
                         cSetVisible(self,77,True)
                         cSetVisible(self,83,False)
                         cSetVisible(self,82,True)


                 elif changelanguage_yellow:
                     cSetVisible(self,34,False)
                     cSetVisible(self,35,True)
                     cSetVisible(self,39,False)
                     cSetVisible(self,38,True)

                     if english_enabled:
                         cSetVisible(self,78,False)
                         cSetVisible(self,79,True)
                         cSetVisible(self,83,False)
                         cSetVisible(self,82,True)


                 elif changepin_yellow:
                     cSetVisible(self,36,False)
                     cSetVisible(self,37,True)
                     cSetVisible(self,39,False)
                     cSetVisible(self,38,True)

                     if english_enabled:
                         cSetVisible(self,80,False)
                         cSetVisible(self,81,True)
                         cSetVisible(self,83,False)
                         cSetVisible(self,82,True)


                 elif viewrestrictions_yellow:
                     pass


                 elif removechannels_yellow:
                     cSetVisible(self,40,False)
                     cSetVisible(self,41,True)
                     cSetVisible(self,39,False)
                     cSetVisible(self,38,True)

                     if english_enabled:
                         cSetVisible(self,84,False)
                         cSetVisible(self,85,True)
                         cSetVisible(self,83,False)
                         cSetVisible(self,82,True)


                 elif systemdetails_yellow:
                     cSetVisible(self,42,False)
                     cSetVisible(self,43,True)
                     cSetVisible(self,39,False)
                     cSetVisible(self,38,True)

                     if english_enabled:
                         cSetVisible(self,86,False)
                         cSetVisible(self,87,True)
                         cSetVisible(self,83,False)
                         cSetVisible(self,82,True)


                 elif speedtest_yellow:
                     cSetVisible(self,44,False)
                     cSetVisible(self,45,True)
                     cSetVisible(self,39,False)
                     cSetVisible(self,38,True)

                     if english_enabled:
                         cSetVisible(self,88,False)
                         cSetVisible(self,89,True)
                         cSetVisible(self,83,False)
                         cSetVisible(self,82,True)




             elif changepin_enabled:
                 if PIN_1_enabled:
                     if PIN_1_enabled == True:
                         cSetVisible(self,209,False)
                         cSetVisible(self,213,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                     elif PIN_4_enabled == False:
                         pass




         if action == ACTION_NUMBER6:
             if tvguide_yellow:
                 if allchannels_yellow:
                     cSetVisible(self,11,False)
                     cSetVisible(self,10,True)
                     cSetVisible(self,21,False)
                     cSetVisible(self,20,True)


                     if english_enabled:
                         cSetVisible(self,54,False)
                         cSetVisible(self,55,True)
                         cSetVisible(self,65,False)
                         cSetVisible(self,64,True)


                 elif entertainment_yellow:
                     cSetVisible(self,12,False)
                     cSetVisible(self,13,True)
                     cSetVisible(self,21,False)
                     cSetVisible(self,20,True)


                     if english_enabled:
                         cSetVisible(self,56,False)
                         cSetVisible(self,57,True)
                         cSetVisible(self,65,False)
                         cSetVisible(self,64,True)


                 elif movies_yellow:
                     cSetVisible(self,14,False)
                     cSetVisible(self,15,True)
                     cSetVisible(self,21,False)
                     cSetVisible(self,20,True)


                     if english_enabled:
                         cSetVisible(self,58,False)
                         cSetVisible(self,59,True)
                         cSetVisible(self,65,False)
                         cSetVisible(self,64,True)


                 elif kids_yellow:
                     cSetVisible(self,16,False)
                     cSetVisible(self,17,True)
                     cSetVisible(self,21,False)
                     cSetVisible(self,20,True)


                     if english_enabled:
                         cSetVisible(self,60,False)
                         cSetVisible(self,61,True)
                         cSetVisible(self,65,False)
                         cSetVisible(self,64,True)


                 elif sports_yellow:
                     cSetVisible(self,18,False)
                     cSetVisible(self,19,True)
                     cSetVisible(self,21,False)
                     cSetVisible(self,20,True)


                     if english_enabled:
                         cSetVisible(self,62,False)
                         cSetVisible(self,63,True)
                         cSetVisible(self,65,False)
                         cSetVisible(self,64,True)


                 elif news_yellow:
                     pass


                 elif documentaries_yellow:
                     cSetVisible(self,22,False)
                     cSetVisible(self,23,True)
                     cSetVisible(self,21,False)
                     cSetVisible(self,20,True)


                     if english_enabled:
                         cSetVisible(self,66,False)
                         cSetVisible(self,67,True)
                         cSetVisible(self,65,False)
                         cSetVisible(self,64,True)


                 elif musicradio_yellow:
                     cSetVisible(self,24,False)
                     cSetVisible(self,25,True)
                     cSetVisible(self,21,False)
                     cSetVisible(self,20,True)


                     if english_enabled:
                         cSetVisible(self,68,False)
                         cSetVisible(self,69,True)
                         cSetVisible(self,65,False)
                         cSetVisible(self,64,True)


                 elif adult_yellow:
                     cSetVisible(self,26,False)
                     cSetVisible(self,27,True)
                     cSetVisible(self,21,False)
                     cSetVisible(self,20,True)


                     if english_enabled:
                         cSetVisible(self,70,False)
                         cSetVisible(self,71,True)
                         cSetVisible(self,65,False)
                         cSetVisible(self,64,True)


                 elif favourites_yellow:
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,True)
                     cSetVisible(self,21,False)
                     cSetVisible(self,20,True)


                     if english_enabled:
                         cSetVisible(self,72,False)
                         cSetVisible(self,73,True)
                         cSetVisible(self,65,False)
                         cSetVisible(self,64,True)




             elif settings_yellow:
                 if picture_yellow:
                     cSetVisible(self,30,False)
                     cSetVisible(self,31,True)
                     cSetVisible(self,41,False)
                     cSetVisible(self,40,True)

                     if english_enabled:
                         cSetVisible(self,74,False)
                         cSetVisible(self,75,True)
                         cSetVisible(self,85,False)
                         cSetVisible(self,84,True)


                 elif sound_yellow:
                     cSetVisible(self,32,False)
                     cSetVisible(self,33,True)
                     cSetVisible(self,41,False)
                     cSetVisible(self,40,True)

                     if english_enabled:
                         cSetVisible(self,76,False)
                         cSetVisible(self,77,True)
                         cSetVisible(self,85,False)
                         cSetVisible(self,84,True)


                 elif changelanguage_yellow:
                     cSetVisible(self,34,False)
                     cSetVisible(self,35,True)
                     cSetVisible(self,41,False)
                     cSetVisible(self,40,True)

                     if english_enabled:
                         cSetVisible(self,78,False)
                         cSetVisible(self,79,True)
                         cSetVisible(self,85,False)
                         cSetVisible(self,84,True)


                 elif changepin_yellow:
                     cSetVisible(self,36,False)
                     cSetVisible(self,37,True)
                     cSetVisible(self,41,False)
                     cSetVisible(self,40,True)

                     if english_enabled:
                         cSetVisible(self,80,False)
                         cSetVisible(self,81,True)
                         cSetVisible(self,85,False)
                         cSetVisible(self,84,True)


                 elif viewrestrictions_yellow:
                     cSetVisible(self,38,False)
                     cSetVisible(self,39,True)
                     cSetVisible(self,41,False)
                     cSetVisible(self,40,True)

                     if english_enabled:
                         cSetVisible(self,82,False)
                         cSetVisible(self,83,True)
                         cSetVisible(self,85,False)
                         cSetVisible(self,84,True)


                 elif removechannels_yellow:
                     pass


                 elif systemdetails_yellow:
                     cSetVisible(self,42,False)
                     cSetVisible(self,43,True)
                     cSetVisible(self,41,False)
                     cSetVisible(self,40,True)

                     if english_enabled:
                         cSetVisible(self,86,False)
                         cSetVisible(self,87,True)
                         cSetVisible(self,85,False)
                         cSetVisible(self,84,True)


                 elif speedtest_yellow:
                     cSetVisible(self,44,False)
                     cSetVisible(self,45,True)
                     cSetVisible(self,41,False)
                     cSetVisible(self,40,True)

                     if english_enabled:
                         cSetVisible(self,88,False)
                         cSetVisible(self,89,True)
                         cSetVisible(self,85,False)
                         cSetVisible(self,84,True)




             elif changepin_enabled:
                 if PIN_1_enabled:
                     if PIN_1_enabled == True:
                         cSetVisible(self,209,False)
                         cSetVisible(self,213,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                     elif PIN_4_enabled == False:
                         pass




         if action == ACTION_NUMBER7:
             if tvguide_yellow:
                 if allchannels_yellow:
                     cSetVisible(self,11,False)
                     cSetVisible(self,10,True)
                     cSetVisible(self,23,False)
                     cSetVisible(self,22,True)


                     if english_enabled:
                         cSetVisible(self,54,False)
                         cSetVisible(self,55,True)
                         cSetVisible(self,67,False)
                         cSetVisible(self,66,True)


                 elif entertainment_yellow:
                     cSetVisible(self,12,False)
                     cSetVisible(self,13,True)
                     cSetVisible(self,23,False)
                     cSetVisible(self,22,True)


                     if english_enabled:
                         cSetVisible(self,56,False)
                         cSetVisible(self,57,True)
                         cSetVisible(self,67,False)
                         cSetVisible(self,66,True)


                 elif movies_yellow:
                     cSetVisible(self,14,False)
                     cSetVisible(self,15,True)
                     cSetVisible(self,23,False)
                     cSetVisible(self,22,True)


                     if english_enabled:
                         cSetVisible(self,58,False)
                         cSetVisible(self,59,True)
                         cSetVisible(self,67,False)
                         cSetVisible(self,66,True)


                 elif kids_yellow:
                     cSetVisible(self,16,False)
                     cSetVisible(self,17,True)
                     cSetVisible(self,23,False)
                     cSetVisible(self,22,True)


                     if english_enabled:
                         cSetVisible(self,60,False)
                         cSetVisible(self,61,True)
                         cSetVisible(self,67,False)
                         cSetVisible(self,66,True)


                 elif sports_yellow:
                     cSetVisible(self,18,False)
                     cSetVisible(self,19,True)
                     cSetVisible(self,23,False)
                     cSetVisible(self,22,True)


                     if english_enabled:
                         cSetVisible(self,62,False)
                         cSetVisible(self,63,True)
                         cSetVisible(self,67,False)
                         cSetVisible(self,66,True)


                 elif news_yellow:
                     cSetVisible(self,20,False)
                     cSetVisible(self,21,True)
                     cSetVisible(self,23,False)
                     cSetVisible(self,22,True)


                     if english_enabled:
                         cSetVisible(self,64,False)
                         cSetVisible(self,65,True)
                         cSetVisible(self,67,False)
                         cSetVisible(self,66,True)


                 elif documentaries_yellow:
                     pass


                 elif musicradio_yellow:
                     cSetVisible(self,24,False)
                     cSetVisible(self,25,True)
                     cSetVisible(self,23,False)
                     cSetVisible(self,22,True)


                     if english_enabled:
                         cSetVisible(self,68,False)
                         cSetVisible(self,69,True)
                         cSetVisible(self,67,False)
                         cSetVisible(self,66,True)


                 elif adult_yellow:
                     cSetVisible(self,26,False)
                     cSetVisible(self,27,True)
                     cSetVisible(self,23,False)
                     cSetVisible(self,22,True)


                     if english_enabled:
                         cSetVisible(self,70,False)
                         cSetVisible(self,71,True)
                         cSetVisible(self,67,False)
                         cSetVisible(self,66,True)


                 elif favourites_yellow:
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,True)
                     cSetVisible(self,23,False)
                     cSetVisible(self,22,True)


                     if english_enabled:
                         cSetVisible(self,72,False)
                         cSetVisible(self,73,True)
                         cSetVisible(self,67,False)
                         cSetVisible(self,66,True)




             elif settings_yellow:
                 if picture_yellow:
                     cSetVisible(self,30,False)
                     cSetVisible(self,31,True)
                     cSetVisible(self,43,False)
                     cSetVisible(self,42,True)

                     if english_enabled:
                         cSetVisible(self,74,False)
                         cSetVisible(self,75,True)
                         cSetVisible(self,87,False)
                         cSetVisible(self,86,True)


                 elif sound_yellow:
                     cSetVisible(self,32,False)
                     cSetVisible(self,33,True)
                     cSetVisible(self,43,False)
                     cSetVisible(self,42,True)

                     if english_enabled:
                         cSetVisible(self,76,False)
                         cSetVisible(self,77,True)
                         cSetVisible(self,87,False)
                         cSetVisible(self,86,True)


                 elif changelanguage_yellow:
                     cSetVisible(self,34,False)
                     cSetVisible(self,35,True)
                     cSetVisible(self,43,False)
                     cSetVisible(self,42,True)

                     if english_enabled:
                         cSetVisible(self,78,False)
                         cSetVisible(self,79,True)
                         cSetVisible(self,87,False)
                         cSetVisible(self,86,True)


                 elif changepin_yellow:
                     cSetVisible(self,36,False)
                     cSetVisible(self,37,True)
                     cSetVisible(self,43,False)
                     cSetVisible(self,42,True)

                     if english_enabled:
                         cSetVisible(self,80,False)
                         cSetVisible(self,81,True)
                         cSetVisible(self,87,False)
                         cSetVisible(self,86,True)


                 elif viewrestrictions_yellow:
                     cSetVisible(self,38,False)
                     cSetVisible(self,39,True)
                     cSetVisible(self,43,False)
                     cSetVisible(self,42,True)

                     if english_enabled:
                         cSetVisible(self,82,False)
                         cSetVisible(self,83,True)
                         cSetVisible(self,87,False)
                         cSetVisible(self,86,True)


                 elif removechannels_yellow:
                     cSetVisible(self,40,False)
                     cSetVisible(self,41,True)
                     cSetVisible(self,43,False)
                     cSetVisible(self,42,True)

                     if english_enabled:
                         cSetVisible(self,84,False)
                         cSetVisible(self,85,True)
                         cSetVisible(self,87,False)
                         cSetVisible(self,86,True)


                 elif systemdetails_yellow:
                     pass


                 elif speedtest_yellow:
                     cSetVisible(self,44,False)
                     cSetVisible(self,45,True)
                     cSetVisible(self,43,False)
                     cSetVisible(self,42,True)

                     if english_enabled:
                         cSetVisible(self,88,False)
                         cSetVisible(self,89,True)
                         cSetVisible(self,87,False)
                         cSetVisible(self,86,True)




             elif changepin_enabled:
                 if PIN_1_enabled:
                     if PIN_1_enabled == True:
                         cSetVisible(self,209,False)
                         cSetVisible(self,213,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                     elif PIN_4_enabled == False:
                         pass




         if action == ACTION_NUMBER8:
             if tvguide_yellow:
                 if allchannels_yellow:
                     cSetVisible(self,11,False)
                     cSetVisible(self,10,True)
                     cSetVisible(self,25,False)
                     cSetVisible(self,24,True)


                     if english_enabled:
                         cSetVisible(self,54,False)
                         cSetVisible(self,55,True)
                         cSetVisible(self,69,False)
                         cSetVisible(self,68,True)


                 elif entertainment_yellow:
                     cSetVisible(self,12,False)
                     cSetVisible(self,13,True)
                     cSetVisible(self,25,False)
                     cSetVisible(self,24,True)


                     if english_enabled:
                         cSetVisible(self,56,False)
                         cSetVisible(self,57,True)
                         cSetVisible(self,69,False)
                         cSetVisible(self,68,True)


                 elif movies_yellow:
                     cSetVisible(self,14,False)
                     cSetVisible(self,15,True)
                     cSetVisible(self,25,False)
                     cSetVisible(self,24,True)


                     if english_enabled:
                         cSetVisible(self,58,False)
                         cSetVisible(self,59,True)
                         cSetVisible(self,69,False)
                         cSetVisible(self,68,True)


                 elif kids_yellow:
                     cSetVisible(self,16,False)
                     cSetVisible(self,17,True)
                     cSetVisible(self,25,False)
                     cSetVisible(self,24,True)


                     if english_enabled:
                         cSetVisible(self,60,False)
                         cSetVisible(self,61,True)
                         cSetVisible(self,69,False)
                         cSetVisible(self,68,True)


                 elif sports_yellow:
                     cSetVisible(self,18,False)
                     cSetVisible(self,19,True)
                     cSetVisible(self,25,False)
                     cSetVisible(self,24,True)


                     if english_enabled:
                         cSetVisible(self,62,False)
                         cSetVisible(self,63,True)
                         cSetVisible(self,69,False)
                         cSetVisible(self,68,True)


                 elif news_yellow:
                     cSetVisible(self,20,False)
                     cSetVisible(self,21,True)
                     cSetVisible(self,25,False)
                     cSetVisible(self,24,True)


                     if english_enabled:
                         cSetVisible(self,64,False)
                         cSetVisible(self,65,True)
                         cSetVisible(self,69,False)
                         cSetVisible(self,68,True)


                 elif documentaries_yellow:
                     cSetVisible(self,22,False)
                     cSetVisible(self,23,True)
                     cSetVisible(self,25,False)
                     cSetVisible(self,24,True)


                     if english_enabled:
                         cSetVisible(self,66,False)
                         cSetVisible(self,67,True)
                         cSetVisible(self,69,False)
                         cSetVisible(self,68,True)


                 elif musicradio_yellow:
                     pass


                 elif adult_yellow:
                     cSetVisible(self,26,False)
                     cSetVisible(self,27,True)
                     cSetVisible(self,25,False)
                     cSetVisible(self,24,True)


                     if english_enabled:
                         cSetVisible(self,70,False)
                         cSetVisible(self,71,True)
                         cSetVisible(self,69,False)
                         cSetVisible(self,68,True)


                 elif favourites_yellow:
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,True)
                     cSetVisible(self,25,False)
                     cSetVisible(self,24,True)


                     if english_enabled:
                         cSetVisible(self,72,False)
                         cSetVisible(self,73,True)
                         cSetVisible(self,69,False)
                         cSetVisible(self,68,True)




             elif settings_yellow:
                 if picture_yellow:
                     cSetVisible(self,30,False)
                     cSetVisible(self,31,True)
                     cSetVisible(self,45,False)
                     cSetVisible(self,44,True)

                     if english_enabled:
                         cSetVisible(self,74,False)
                         cSetVisible(self,75,True)
                         cSetVisible(self,89,False)
                         cSetVisible(self,88,True)


                 elif sound_yellow:
                     cSetVisible(self,32,False)
                     cSetVisible(self,33,True)
                     cSetVisible(self,45,False)
                     cSetVisible(self,44,True)

                     if english_enabled:
                         cSetVisible(self,76,False)
                         cSetVisible(self,77,True)
                         cSetVisible(self,89,False)
                         cSetVisible(self,88,True)


                 elif changelanguage_yellow:
                     cSetVisible(self,34,False)
                     cSetVisible(self,35,True)
                     cSetVisible(self,45,False)
                     cSetVisible(self,44,True)

                     if english_enabled:
                         cSetVisible(self,78,False)
                         cSetVisible(self,79,True)
                         cSetVisible(self,89,False)
                         cSetVisible(self,88,True)


                 elif changepin_yellow:
                     cSetVisible(self,36,False)
                     cSetVisible(self,37,True)
                     cSetVisible(self,45,False)
                     cSetVisible(self,44,True)

                     if english_enabled:
                         cSetVisible(self,80,False)
                         cSetVisible(self,81,True)
                         cSetVisible(self,89,False)
                         cSetVisible(self,88,True)


                 elif viewrestrictions_yellow:
                     cSetVisible(self,38,False)
                     cSetVisible(self,39,True)
                     cSetVisible(self,45,False)
                     cSetVisible(self,44,True)

                     if english_enabled:
                         cSetVisible(self,82,False)
                         cSetVisible(self,83,True)
                         cSetVisible(self,89,False)
                         cSetVisible(self,88,True)


                 elif removechannels_yellow:
                     cSetVisible(self,40,False)
                     cSetVisible(self,41,True)
                     cSetVisible(self,45,False)
                     cSetVisible(self,44,True)

                     if english_enabled:
                         cSetVisible(self,84,False)
                         cSetVisible(self,85,True)
                         cSetVisible(self,89,False)
                         cSetVisible(self,88,True)


                 elif systemdetails_yellow:
                     cSetVisible(self,42,False)
                     cSetVisible(self,43,True)
                     cSetVisible(self,45,False)
                     cSetVisible(self,44,True)

                     if english_enabled:
                         cSetVisible(self,86,False)
                         cSetVisible(self,87,True)
                         cSetVisible(self,89,False)
                         cSetVisible(self,88,True)


                 elif speedtest_yellow:
                     pass



             elif changepin_enabled:
                 if PIN_1_enabled:
                     if PIN_1_enabled == True:
                         cSetVisible(self,209,False)
                         cSetVisible(self,213,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                     elif PIN_4_enabled == False:
                         pass




         if action == ACTION_NUMBER9:
             if tvguide_yellow:
                 if allchannels_yellow:
                     cSetVisible(self,11,False)
                     cSetVisible(self,10,True)
                     cSetVisible(self,27,False)
                     cSetVisible(self,26,True)


                     if english_enabled:
                         cSetVisible(self,54,False)
                         cSetVisible(self,55,True)
                         cSetVisible(self,71,False)
                         cSetVisible(self,70,True)


                 elif entertainment_yellow:
                     cSetVisible(self,12,False)
                     cSetVisible(self,13,True)
                     cSetVisible(self,27,False)
                     cSetVisible(self,26,True)


                     if english_enabled:
                         cSetVisible(self,56,False)
                         cSetVisible(self,57,True)
                         cSetVisible(self,71,False)
                         cSetVisible(self,70,True)


                 elif movies_yellow:
                     cSetVisible(self,14,False)
                     cSetVisible(self,15,True)
                     cSetVisible(self,27,False)
                     cSetVisible(self,26,True)


                     if english_enabled:
                         cSetVisible(self,58,False)
                         cSetVisible(self,59,True)
                         cSetVisible(self,71,False)
                         cSetVisible(self,70,True)


                 elif kids_yellow:
                     cSetVisible(self,16,False)
                     cSetVisible(self,17,True)
                     cSetVisible(self,27,False)
                     cSetVisible(self,26,True)


                     if english_enabled:
                         cSetVisible(self,60,False)
                         cSetVisible(self,61,True)
                         cSetVisible(self,71,False)
                         cSetVisible(self,70,True)


                 elif sports_yellow:
                     cSetVisible(self,18,False)
                     cSetVisible(self,19,True)
                     cSetVisible(self,27,False)
                     cSetVisible(self,26,True)


                     if english_enabled:
                         cSetVisible(self,62,False)
                         cSetVisible(self,63,True)
                         cSetVisible(self,71,False)
                         cSetVisible(self,70,True)


                 elif news_yellow:
                     cSetVisible(self,20,False)
                     cSetVisible(self,21,True)
                     cSetVisible(self,27,False)
                     cSetVisible(self,26,True)


                     if english_enabled:
                         cSetVisible(self,64,False)
                         cSetVisible(self,65,True)
                         cSetVisible(self,71,False)
                         cSetVisible(self,70,True)


                 elif documentaries_yellow:
                     cSetVisible(self,22,False)
                     cSetVisible(self,23,True)
                     cSetVisible(self,27,False)
                     cSetVisible(self,26,True)


                     if english_enabled:
                         cSetVisible(self,66,False)
                         cSetVisible(self,67,True)
                         cSetVisible(self,71,False)
                         cSetVisible(self,70,True)


                 elif musicradio_yellow:
                     cSetVisible(self,24,False)
                     cSetVisible(self,25,True)
                     cSetVisible(self,27,False)
                     cSetVisible(self,26,True)


                     if english_enabled:
                         cSetVisible(self,68,False)
                         cSetVisible(self,69,True)
                         cSetVisible(self,71,False)
                         cSetVisible(self,70,True)


                 elif adult_yellow:
                     pass


                 elif favourites_yellow:
                     cSetVisible(self,28,False)
                     cSetVisible(self,29,True)
                     cSetVisible(self,27,False)
                     cSetVisible(self,26,True)


                     if english_enabled:
                         cSetVisible(self,72,False)
                         cSetVisible(self,73,True)
                         cSetVisible(self,71,False)
                         cSetVisible(self,70,True)




             elif changepin_enabled:
                 if PIN_1_enabled:
                     if PIN_1_enabled == True:
                         cSetVisible(self,209,False)
                         cSetVisible(self,213,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,4210,False)
                         cSetVisible(self,214,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                     elif PIN_4_enabled == False:
                         pass


                     elif PIN_4_enabled:
                         if PIN_4_enabled == True:
                             cSetVisible(self,212,False)
                             cSetVisible(self,216,True)
                         elif PIN_4_enabled == False:
                             pass




         if action == ACTION_NUMBER0:
             if tvguide_yellow:
                 if allchannels_yellow:
                     cSetVisible(self,11,False)
                     cSetVisible(self,10,True)
                     cSetVisible(self,29,False)
                     cSetVisible(self,28,True)


                     if english_enabled:
                         cSetVisible(self,54,False)
                         cSetVisible(self,55,True)
                         cSetVisible(self,73,False)
                         cSetVisible(self,72,True)


                 elif entertainment_yellow:
                     cSetVisible(self,12,False)
                     cSetVisible(self,13,True)
                     cSetVisible(self,29,False)
                     cSetVisible(self,28,True)


                     if english_enabled:
                         cSetVisible(self,56,False)
                         cSetVisible(self,57,True)
                         cSetVisible(self,73,False)
                         cSetVisible(self,72,True)


                 elif movies_yellow:
                     cSetVisible(self,14,False)
                     cSetVisible(self,15,True)
                     cSetVisible(self,29,False)
                     cSetVisible(self,28,True)


                     if english_enabled:
                         cSetVisible(self,58,False)
                         cSetVisible(self,59,True)
                         cSetVisible(self,73,False)
                         cSetVisible(self,72,True)


                 elif kids_yellow:
                     cSetVisible(self,16,False)
                     cSetVisible(self,17,True)
                     cSetVisible(self,29,False)
                     cSetVisible(self,28,True)


                     if english_enabled:
                         cSetVisible(self,60,False)
                         cSetVisible(self,61,True)
                         cSetVisible(self,73,False)
                         cSetVisible(self,72,True)


                 elif sports_yellow:
                     cSetVisible(self,18,False)
                     cSetVisible(self,19,True)
                     cSetVisible(self,29,False)
                     cSetVisible(self,28,True)


                     if english_enabled:
                         cSetVisible(self,62,False)
                         cSetVisible(self,63,True)
                         cSetVisible(self,73,False)
                         cSetVisible(self,72,True)


                 elif news_yellow:
                     cSetVisible(self,20,False)
                     cSetVisible(self,21,True)
                     cSetVisible(self,29,False)
                     cSetVisible(self,28,True)


                     if english_enabled:
                         cSetVisible(self,64,False)
                         cSetVisible(self,65,True)
                         cSetVisible(self,73,False)
                         cSetVisible(self,72,True)


                 elif documentaries_yellow:
                     cSetVisible(self,22,False)
                     cSetVisible(self,23,True)
                     cSetVisible(self,29,False)
                     cSetVisible(self,28,True)


                     if english_enabled:
                         cSetVisible(self,66,False)
                         cSetVisible(self,67,True)
                         cSetVisible(self,73,False)
                         cSetVisible(self,72,True)


                 elif musicradio_yellow:
                     cSetVisible(self,24,False)
                     cSetVisible(self,25,True)
                     cSetVisible(self,29,False)
                     cSetVisible(self,28,True)


                     if english_enabled:
                         cSetVisible(self,68,False)
                         cSetVisible(self,69,True)
                         cSetVisible(self,73,False)
                         cSetVisible(self,72,True)


                 elif adult_yellow:
                     cSetVisible(self,26,False)
                     cSetVisible(self,27,True)
                     cSetVisible(self,29,False)
                     cSetVisible(self,28,True)


                     if english_enabled:
                         cSetVisible(self,70,False)
                         cSetVisible(self,71,True)
                         cSetVisible(self,73,False)
                         cSetVisible(self,72,True)


                 elif favourites_yellow:
                     pass




             elif changepin_enabled:
                 if PIN_1_enabled:
                     if PIN_1_enabled == True:
                         cSetVisible(self,209,False)
                         cSetVisible(self,213,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,210,False)
                         cSetVisible(self,214,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,211,False)
                         cSetVisible(self,215,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,212,False)
                         cSetVisible(self,216,True)
                     elif PIN_4_enabled == False:
                         pass




     def onActionTVMode(self, action):
         FullScreen = ADDON.getSetting('FullScreen.enabled') == 'true'
         print "you are in the action tv mode now"
         print "FullScreen is..."
         print FullScreen

         if FullScreen == True:
             print "hello chris you are in normal mode"
             print "now let remove these controls"
             channel_1_yellow = self.channels_Index
             channel_2_yellow = self.channels_Index
             channel_3_yellow = self.channels_Index
             channel_4_yellow = self.channels_Index
             channel_5_yellow = self.channels_Index
             channel_6_yellow = self.channels_Index
             channel_7_yellow = self.channels_Index
             print "channel_1_yellow is..."
             print channel_1_yellow

             if channel_1_yellow == 0:
                 channel_1_yellow = True

             if channel_1_yellow == True:
                 #self.getControl(1).setVisible(True)
                 self.getControl(347).setVisible(True)
                 self.getControl(348).setVisible(True)
                 self.getControl(349).setVisible(True)
                 self.getControl(350).setVisible(True)
                 self.getControl(351).setVisible(True)
                 self.getControl(352).setVisible(True)
                 self.getControl(353).setVisible(True)
                 xbmc.executebuiltin("Action(Enter)")




             elif channel_2_yellow == 1:
                 self.getControl(354).setVisible(True)
                 self.getControl(355).setVisible(True)
                 self.getControl(349).setVisible(True)
                 self.getControl(350).setVisible(True)
                 self.getControl(351).setVisible(True)
                 self.getControl(352).setVisible(True)
                 self.getControl(353).setVisible(True)




class AllChannelsThread(threading.Thread):
     # This is needed for proper threading. The other method continued to block on the call.
     def __init__(self, xtarget):
         threading.Thread.__init__(self, name='All_Channels_BACKUP_thread')
         self.xtarget = xtarget

     def start(self):
         threading.Thread.start(self)

     def run(self):
         self.xtarget()

     def stop(self):
         self.join(2000)

class AbortDownload(Exception):

     def __init__(self, value):
         self.value = value

     def __str__(self):
         return repr(self.value)