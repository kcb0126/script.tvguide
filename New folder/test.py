import xbmc
import xbmcgui
import xbmcaddon
import os
import datetime
import time
import _strptime
import threading
import urllib2
import StringIO
import sqlite3
from sqlite3 import dbapi2 as database
from xml.etree import ElementTree
import xml.etree.ElementTree as ET
from UserDict import DictMixin

# two separate flags to kill the AllChannelsThread and the TimerThread
__killthread__ = False
CHANNELS_PER_PAGE = 7


#get actioncodes from keyboard.xml
ACTION_MOVE_LEFT = 1
ACTION_MOVE_RIGHT = 2
ACTION_MOVE_UP = 3
ACTION_MOVE_DOWN = 4
ACTION_ENTER = 7
ACTION_PREVIOUS_MENU = 10
ACTION_BACKSPACE = 110
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

class ControlProgramList(object):
    def __init__(self, control, program):
        self.control = control
        self.program = program




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



class MyClass(xbmcgui.WindowXML):

     def __new__(cls):
         return super(MyClass, cls).__new__(cls, 'script-tvguide-mainmenu.xml', ADDON.getAddonInfo('path'))


     def __init__(self):
         self._timel = []
         self.thread = None
         self.program_buttons = []



     def onInit(self):
         self.getControl(3).setAnimations([('fade', 'effect=fade start=0 end=100 time=1500')])
         self.getControl(5).setAnimations([('fade', 'effect=fade start=0 end=100 time=1500')])
         self.getControl(7).setAnimations([('fade', 'effect=fade start=0 end=100 time=1500')])
         self.getControl(9).setAnimations([('fade', 'effect=fade start=0 end=100 time=1500')])
         self.getControl(4).setVisible(False)
         self.getControl(6).setVisible(False)
         self.getControl(8).setVisible(False)
         self.getControl(10).setVisible(False)
         cSetVisible(self,110,False)
         changelanguage_yellow_BOX = self.getControl(110)
         changelanguage_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/changelang_yellow.png")
         cSetVisible(self,111,False)
         changelanguage_blue_BOX = self.getControl(111)
         changelanguage_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/changelang_blue.png")
         self.getControl(142).setVisible(False)
         savesettings_yellow_BOX = self.getControl(142)
         savesettings_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/savesettings_yellow.png")
         self.getControl(143).setVisible(False)
         savesettings_blue_BOX = self.getControl(143)
         savesettings_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/savesettings_blue.png")
         cSetVisible(self,146,False)
         self.getControl(146).setLabel('$INFO[System.Date(ddd dd mmm)]'  + ' ' + time.strftime("%I").lstrip('0') + time.strftime(":%M%p"))
         self.getControl(116).setVisible(False)
         language_yellow_BOX = self.getControl(116)
         language_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/lang_yellow.png")
         self.getControl(117).setVisible(False)
         language_blue_BOX = self.getControl(117)
         language_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/lang_blue.png")
         self.getControl(114).setVisible(False)
         leftarrowlang_control = self.getControl(114)
         leftarrowlang_control.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/left-arrow.png")
         self.getControl(115).setVisible(False)
         rightarrowlang_control = self.getControl(115)
         rightarrowlang_control.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/right-arrow.png")
         cSetVisible(self,11,True)
         allchannels_yellow_BOX = self.getControl(11)
         allchannels_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_yellow.png")
         cSetVisible(self,10,False)
         allchannels_blue_BOX = self.getControl(10)
         allchannels_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_blue.png")
         cSetVisible(self,12,False)
         entertainment_yellow_BOX = self.getControl(12)
         entertainment_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_yellow.png")
         cSetVisible(self,13,True)
         entertainment_blue_BOX = self.getControl(13)
         entertainment_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_blue.png")
         cSetVisible(self,14,False)
         movies_yellow_BOX = self.getControl(14)
         movies_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_yellow.png")
         cSetVisible(self,15,True)
         movies_blue_BOX = self.getControl(15)
         movies_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_blue.png")
         cSetVisible(self,16,False)
         kids_yellow_BOX = self.getControl(16)
         kids_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_yellow.png")
         cSetVisible(self,17,True)
         kids_blue_BOX = self.getControl(17)
         kids_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_blue.png")
         cSetVisible(self,18,False)
         sports_yellow_BOX = self.getControl(18)
         sports_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_yellow.png")
         cSetVisible(self,19,True)
         sports_blue_BOX = self.getControl(19)
         sports_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_blue.png")
         cSetVisible(self,20,False)
         news_yellow_BOX = self.getControl(20)
         news_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_yellow.png")
         cSetVisible(self,21,True)
         news_blue_BOX = self.getControl(21)
         news_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_blue.png")
         cSetVisible(self,22,False)
         documentaries_yellow_BOX = self.getControl(22)
         documentaries_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_yellow.png")
         cSetVisible(self,23,True)
         documentaries_blue_BOX = self.getControl(23)
         documentaries_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_blue.png")
         cSetVisible(self,24,False)
         musicradio_yellow_BOX = self.getControl(24)
         musicradio_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_yellow.png")
         cSetVisible(self,25,True)
         musicradio_blue_BOX = self.getControl(25)
         musicradio_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_blue.png")
         cSetVisible(self,26,False)
         adult_yellow_BOX = self.getControl(26)
         adult_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_yellow.png")
         cSetVisible(self,27,True)
         adult_blue_BOX = self.getControl(27)
         adult_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_blue.png")
         cSetVisible(self,28,False)
         favourites_yellow_BOX = self.getControl(28)
         favourites_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_yellow.png")
         cSetVisible(self,29,True)
         favourites_blue_BOX = self.getControl(29)
         favourites_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_blue.png")
         cSetVisible(self,30,False)
         picture_yellow_BOX = self.getControl(30)
         picture_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/allsettings_yellow.png")
         cSetVisible(self,31,False)
         picture_blue_BOX = self.getControl(31)
         picture_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/allsettings_blue.png")
         cSetVisible(self,32,False)
         sound_yellow_BOX = self.getControl(32)
         sound_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/allsettings_yellow.png")
         cSetVisible(self,33,False)
         sound_blue_BOX = self.getControl(33)
         sound_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/allsettings_blue.png")
         cSetVisible(self,34,False)
         changelanguage_yellow_BOX = self.getControl(34)
         changelanguage_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/allsettings_yellow.png")
         cSetVisible(self,35,False)
         changelanguage_blue_BOX = self.getControl(35)
         changelanguage_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/allsettings_blue.png")
         cSetVisible(self,36,False)
         changepin_yellow_BOX = self.getControl(36)
         changepin_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/allsettings_yellow.png")
         cSetVisible(self,37,False)
         changepin_blue_BOX = self.getControl(37)
         changepin_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/allsettings_blue.png")
         cSetVisible(self,38,False)
         viewrestrictions_yellow_BOX = self.getControl(38)
         viewrestrictions_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/allsettings_yellow.png")
         cSetVisible(self,39,False)
         viewrestrictions_blue_BOX = self.getControl(39)
         viewrestrictions_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/allsettings_blue.png")
         cSetVisible(self,40,False)
         removechannels_yellow_BOX = self.getControl(40)
         removechannels_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/allsettings_yellow.png")
         cSetVisible(self,41,False)
         removechannels_blue_BOX = self.getControl(41)
         removechannels_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/allsettings_blue.png")
         cSetVisible(self,42,False)
         systemdetails_yellow_BOX = self.getControl(42)
         systemdetails_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/allsettings_yellow.png")
         cSetVisible(self,43,False)
         systemdetails_blue_BOX = self.getControl(43)
         systemdetails_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/allsettings_blue.png")
         cSetVisible(self,44,False)
         speedtest_yellow_BOX = self.getControl(44)
         speedtest_yellow_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/allsettings_yellow.png")
         cSetVisible(self,45,False)
         speedtest_blue_BOX = self.getControl(45)
         speedtest_blue_BOX.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/allsettings_blue.png")
         cSetVisible(self,4000,False)
         enterpin_yellow = self.getControl(4000)
         enterpin_yellow.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/enterpin_yellow.png")
         cSetVisible(self,4001,False)
         enterpin_blue = self.getControl(4001)
         enterpin_blue.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/enterpin_blue1.png")
         cSetVisible(self,4002,False)
         enterpin_bottom_blue = self.getControl(4002)
         enterpin_bottom_blue.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/enterpin_blue1.png")
         cSetVisible(self,4006,False)
         pin_press_back = self.getControl(4006)
         pin_press_back.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/pressback3.png")
         cSetVisible(self,4009,False)
         enterpin_blank_1 = self.getControl(4009)
         enterpin_blank_1.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/pin_numb1.png")
         cSetVisible(self,4010,False)
         enterpin_blank_2 = self.getControl(4010)
         enterpin_blank_2.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/pin_numb2.png")
         cSetVisible(self,4011,False)
         enterpin_blank_3 = self.getControl(4011)
         enterpin_blank_3.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/pin_numb3.png")
         cSetVisible(self,4012,False)
         enterpin_blank_4 = self.getControl(4012)
         enterpin_blank_4.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/pin_numb4.png")
         cSetVisible(self,4013,False)
         enterpin_chars_1 = self.getControl(4013)
         enterpin_chars_1.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/pin_1.png")
         cSetVisible(self,4014,False)
         enterpin_chars_2 = self.getControl(4014)
         enterpin_chars_2.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/pin_2.png")
         cSetVisible(self,4015,False)
         enterpin_chars_3 = self.getControl(4015)
         enterpin_chars_3.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/pin_3.png")
         cSetVisible(self,4016,False)
         enterpin_chars_4 = self.getControl(4016)
         enterpin_chars_4.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/pin_4.png")
         cSetVisible(self,4200,False)
         loading_gif = self.getControl(4200)
         loading_gif.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/tvguide-loading.gif")
         cSetVisible(self,4203,False)
         tvguide_time_bar = self.getControl(4203)
         tvguide_time_bar.setImage("special://home/addons/script.tvguide/resources/skins/Default/media/channels_bar1.png")
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
         self.getControl(54).setVisible(False)
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
         self.getControl(101).setVisible(False)
         self.getControl(101).setLabel(self.getString(30035))
         self.getControl(101).setVisible(False)
         self.getControl(101).setLabel(self.getString(30035))
         self.getControl(109).setVisible(False)
         self.getControl(109).setLabel(self.getString(30045))
         self.getControl(112).setVisible(False)
         self.getControl(112).setLabel(self.getString(30046))
         self.getControl(113).setVisible(False)
         self.getControl(113).setLabel(self.getString(30046))
         self.getControl(118).setVisible(False)
         self.getControl(118).setLabel(self.getString(30047))
         self.getControl(119).setVisible(False)
         self.getControl(119).setLabel(self.getString(30047))
         self.getControl(120).setVisible(False)
         self.getControl(120).setLabel(self.getString(30048))
         self.getControl(121).setVisible(False)
         self.getControl(121).setLabel(self.getString(30048))
         self.getControl(122).setVisible(False)
         self.getControl(122).setLabel(self.getString(30049))
         self.getControl(123).setVisible(False)
         self.getControl(123).setLabel(self.getString(30049))
         self.getControl(124).setVisible(False)
         self.getControl(124).setLabel(self.getString(30050))
         self.getControl(125).setVisible(False)
         self.getControl(125).setLabel(self.getString(30050))
         self.getControl(126).setVisible(False)
         self.getControl(126).setLabel(self.getString(30051))
         self.getControl(127).setVisible(False)
         self.getControl(127).setLabel(self.getString(30051))
         self.getControl(128).setVisible(False)
         self.getControl(128).setLabel(self.getString(30052))
         self.getControl(129).setVisible(False)
         self.getControl(129).setLabel(self.getString(30052))
         self.getControl(130).setVisible(False)
         self.getControl(130).setLabel(self.getString(30053))
         self.getControl(131).setVisible(False)
         self.getControl(131).setLabel(self.getString(30053))
         self.getControl(132).setVisible(False)
         self.getControl(132).setLabel(self.getString(30054))
         self.getControl(133).setVisible(False)
         self.getControl(133).setLabel(self.getString(30054))
         self.getControl(134).setVisible(False)
         self.getControl(134).setLabel(self.getString(30055))
         self.getControl(135).setVisible(False)
         self.getControl(135).setLabel(self.getString(30055))
         self.getControl(136).setVisible(False)
         self.getControl(136).setLabel(self.getString(30056))
         self.getControl(137).setVisible(False)
         self.getControl(137).setLabel(self.getString(30056))
         self.getControl(138).setVisible(False)
         self.getControl(138).setLabel(self.getString(30057))
         self.getControl(139).setVisible(False)
         self.getControl(139).setLabel(self.getString(30057))
         self.getControl(140).setVisible(False)
         self.getControl(140).setLabel(self.getString(30058))
         self.getControl(141).setVisible(False)
         self.getControl(141).setLabel(self.getString(30058))
         self.getControl(144).setVisible(False)
         self.getControl(144).setLabel(self.getString(30041))
         self.getControl(145).setVisible(False)
         self.getControl(145).setLabel(self.getString(30041))
         self.getControl(264).setVisible(False)
         self.getControl(264).setLabel(self.getString(31001))
         self.getControl(265).setVisible(False)
         self.getControl(265).setLabel(self.getString(31001))
         self.getControl(42011).setVisible(True)
         self.getControl(42011).setLabel(self.getString(30060))
         self.getControl(4003).setVisible(False)
         self.getControl(4003).setLabel(self.getString(30100))
         self.getControl(4004).setVisible(False)
         self.getControl(4004).setLabel(self.getString(30101))
         self.getControl(4005).setVisible(False)
         self.getControl(4005).setLabel(self.getString(30102))
         self.getControl(4007).setVisible(False)
         self.getControl(4007).setLabel(self.getString(30103))
         self.getControl(4008).setVisible(False)
         self.getControl(4008).setLabel(self.getString(30104))
         cSetVisible(self,42011,False)
         cSetVisible(self,42021,False)
         cSetVisible(self,42041,False)
         cSetVisible(self,42051,False)
         cSetVisible(self,42061,False)




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



         if french_enabled:
             cSetVisible(self,264,True)




     def parseDateTimeToMinutesSinceEpoch(self, p_datetime):
         datetime = time.strptime(p_datetime, "%Y%m%d%H%M%S")
         seconds_epoch = time.mktime(datetime)
         minutes_epoch = int(seconds_epoch / 60)
         return minutes_epoch



     def abortdownload(self):
         global __killthread__
         __killthread__ = True
         if self.thread is not None:
            self.thread.join(3000)
         del self.thread
         self.thread = None




     def All_Channels(self):
         yellow_flag = True
         channelData = []
         button_Start = 0
         button_End = 0
         program = None
         Channel_id = 0
         
         global __killthread__
         self.getControl(42021).setLabel("0%")
         try:
             # DOWNLOAD THE XML SOURCE HERE
             url = ADDON.getSetting('allchannel.url')
             data = ''
             response = urllib2.urlopen(url)
             meta = response.info()
             file_size = int(meta.getheaders("Content-Length")[0])
             file_size_dl = 0
             block_size = 2048
             while True and not __killthread__:
                 mbuffer = response.read(block_size)
                 if not mbuffer:
                     break
                 file_size_dl += len(mbuffer)
                 data += mbuffer
                 state = int(file_size_dl * 10.0 / file_size)
                 self.getControl(42021).setLabel(str(state) + '%')
             else:
                 if __killthread__:
                     raise AbortDownload('downloading')
             del response

             # CREATE DATABASE
             profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
             if os.path.exists(profilePath):
                 os.remove(profilePath)
             con = database.connect(profilePath)
             cur = con.cursor()
             cur.execute('CREATE TABLE programs(channel TEXT, title TEXT, start_date TIMESTAMP, stop_date TIMESTAMP, description TEXT)')
             con.commit()

             # Get the loaded data
             total_count = data.count('programme')/2
             tv_elem = ElementTree.parse(StringIO.StringIO(data)).getroot()
             cur = con.cursor()
             count = 1
             channels = OrderedDict()

             for channel in tv_elem.findall('channel'):
                 channel_name = channel.find('display-name').text
                 for program in channel.findall('programme'):
                     if __killthread__:
                         raise AbortDownload('filling')
                     title = program.find('title').text
                     start_time = program.get("start")
                     stop_time = program.get("stop")
                     cur.execute("INSERT INTO programs(channel, title, start_date, stop_date)" + " VALUES(?, ?, ?, ?)", [channel_name, title, start_time, stop_time])
                     status = 10 + int(float(count)/float(total_count) * 90.0)
                     self.getControl(42021).setLabel(str(status) + '%')
                     xbmc.sleep(10)
                     count += 1
                 con.commit()
             print 'Channels have been successfully stored into the database!'
             self.getControl(42021).setLabel('100%')
             xbmc.sleep(3000)

             # Set the date and time row
             current_time = time.time() # now (in seconds)
             half_hour = current_time + 60*30  # now + 30 minutes
             one_hour = current_time + 60*60  # now + 60 minutes

             for t in [current_time,half_hour,one_hour]:
                 if (0 <= datetime.datetime.now().minute <= 29):
                     self.getControl(42041).setLabel(time.strftime("%I").lstrip('0') + ':00' + time.strftime("%p"))
                     self.getControl(42051).setLabel(time.strftime("%I").lstrip('0') + ':30' + time.strftime("%p"))
                     self.getControl(42061).setLabel(time.strftime("%I" + ":00%p",time.localtime(t)).lstrip("0"))
                 else:
                     self.getControl(42041).setLabel(time.strftime("%I").lstrip('0') + ':30' + time.strftime("%p"))
                     self.getControl(42051).setLabel(time.strftime("%I" + ":00%p",time.localtime(t)).lstrip("0"))
                     self.getControl(42061).setLabel(time.strftime("%I" + ":30%p",time.localtime(t)).lstrip("0"))


             #Pull the data from the database
             channelList = list()
             database_path = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))

             if os.path.exists(database_path):
                 #get the channels list
                 cur.execute('SELECT channel FROM programs WHERE channel GROUP BY channel')

                 for row in cur:
                     channels = row[0].encode('ascii')
                     channelList.append(channels)

                 # set the channels text
                 for index in range(0, CHANNELS_PER_PAGE):
                     channel = channelList[index]
                     channel_index = index

                     if channel is not None:
                         pass
                         #print 4127 + 2 + index
                         #self.getControl(4127 + 2 + index).setLabel(channel)
                         #print button
                         #self.button.setLabel(channel, 'font14', '0xFFFFFFFF', '0xFFFF3300', '0xFF000000')

                     #get the programs list
                     cur.execute('SELECT channel, title, start_date, stop_date FROM programs WHERE channel=?', [channel])
                     programList = list()
                     programs = cur.fetchall()
                     start_pos = 368    # indent for first program

                     for row in programs:
                         program = row[1].encode('ascii'), str(row[2]), str(row[3])
                         title = row[1].encode('ascii')
                         program_start_date = str(row[2])
                         program_end_date = str(row[3])

                         #convert the date formats into minutes
                         minutes_start = self.parseDateTimeToMinutesSinceEpoch(program_start_date)
                         minutes_end = self.parseDateTimeToMinutesSinceEpoch(program_end_date)
                         minutes_length = minutes_end - minutes_start

                         program_length = minutes_length
                         program_notification = program
                         programs_top = 315
                         program_height = 34.5
                         program_gap = 2.5
                         position_start = start_pos
                         position_top = programs_top + channel_index * (program_height + program_gap)


                         if 10 <= program_length < 60:
                            program_width = 342.5
                         elif 60 <= program_length < 90:
                             program_width = 690
                         elif 90 <= program_length < 105:
                             program_width = 1050
                         elif 105 <= program_length < 120:
                             program_width = 1400
                         elif 120 <= program_length < 150:
                             program_width = 1750
                         elif 150 <= program_length < 180:
                             program_width = 2100
                         elif 180 <= program_length < 210:
                             program_width = 2450
                         elif 210 <= program_length < 240:
                             program_width = 2800
                         elif 240 <= program_length < 270:
                             program_width = 3150
                         elif 270 <= program_length < 300:
                             program_width = 3500
                         elif 300 <= program_length < 330:
                             program_width = 3850
                         elif 330 <= program_length < 360:
                             program_width = 4200
                         elif 360 <= program_length < 390:
                             program_width = 3250
                         elif 390 <= program_length < 420:
                             program_width = 4550
                         elif 420 <= program_length < 450:
                             program_width = 4900
                         elif 450 <= program_length < 480:
                             program_width = 5250

                         start_pos += program_width + 2 * program_gap

                         if program_width > 1:
                             if yellow_flag:
                                 if program_notification:
                                     button_nofocus = 'changelang_yellow.png'
                                     button_focus = 'channels_bar1.png'
                                 else:
                                     button_nofocus = 'changelang_yellow.png'
                                     button_focus = 'channels_bar1.png'
                                 yellow_flag = False
                                 text_color = '0xFF000000'

                             else:
                                 if program_notification:
                                     button_nofocus = 'channels_bar1.png'
                                     button_focus = 'channels_yellow.png'
                                 else:
                                     button_nofocus = 'channels_bar1.png'
                                     button_focus = 'channels_yellow.png'
                                 text_color = '0xFFFFFFFF'

                             if program_width < 1:
                                 program_title = ''
                             else:
                                 program_title = '[B]' + title + '[/B]'


                             program_controls = xbmcgui.ControlButton(
                                 position_start, 
                                 position_top, 
                                 program_width, 
                                 program_height, 
                                 program_title,
                                 textColor = text_color,
                                 focusTexture = button_focus, 
                                 noFocusTexture = button_nofocus
                             )
                         self.addControl(program_controls)
                     cur.close()



             #Enabled EPG and other controls
             self.getControl(4200).setVisible(False)
             self.getControl(42021).setVisible(False)
             self.getControl(4203).setVisible(False)
             self.getControl(42041).setVisible(True)
             self.getControl(42051).setVisible(True)
             self.getControl(42061).setVisible(True)



         except AbortDownload, e:
             __killthread__ = False
             if e.value == 'downloading':
                 try:
                    if response is not None:
                         self.thread = AllChannelsThread(self.All_Channels)
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



     def getChannel(self, controlId):
         control = self.getControl(controlId)
         print control



     def setControlImage(self, controlId, image):
         control = self.getControl(controlId)
         if control:
             control.setImage(image)




     def getCurrentProgram(self, channel):
         program = None
         now = datetime.datetime.now()
         c = self.conn.cursor()
         c.execute('SELECT * FROM programs WHERE channel=? AND startDate <= ? AND endDate >= ? LIMIT 1', [channel, now, now])
         row = c.fetchone()
         if row:
             program = Program(row["id"], channel, row["title"], row["startDate"], row["endDate"], row["description"], row["episode"], row["genre"])
         c.close()

         if program.description == "":
             xbmc.log('[script.tvcatchup] Possible empty channel, checking...',xbmc.LOGDEBUG)
             IsEmpty = TVC.GetEmptyChannelTitle(channel)
             xbmc.log('[script.tvcatchup] ' + IsEmpty,xbmc.LOGDEBUG)
             if IsEmpty == program.title:
                 xbmc.log("[script.tvcatchup] It's Empty, let's ask TVC for the info",xbmc.LOGDEBUG)
                 missingInfo = TVC.getMissingNow(channel)
                 program.title = missingInfo[0]
                 if missingInfo[1]<>"Offline":
                     program.startDate = self.parseDate(missingInfo[1])
                 if missingInfo[2]<>"Offline":
                     program.endDate =  self.parseDate(missingInfo[2])

         return program




     def All_Channels_BACKUP(self):
         yellow_flag = True
         global __killthread__
         self.getControl(42021).setLabel("0%")
         try:
             # DOWNLOAD THE XML SOURCE HERE
             url = ADDON.getSetting('allchannel.url')
             data = ''
             response = urllib2.urlopen(url)
             meta = response.info()
             file_size = int(meta.getheaders("Content-Length")[0])
             file_size_dl = 0
             block_size = 2048
             while True and not __killthread__:
                 mbuffer = response.read(block_size)
                 if not mbuffer:
                     break
                 file_size_dl += len(mbuffer)
                 data += mbuffer
                 state = int(file_size_dl * 10.0 / file_size)
                 self.getControl(42021).setLabel(str(state) + '%')
             else:
                 if __killthread__:
                     raise AbortDownload('downloading')
             del response

             # CREATE DATABASE
             profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
             if os.path.exists(profilePath):
                 os.remove(profilePath)
             con = database.connect(profilePath)
             cur = con.cursor()
             cur.execute('CREATE TABLE programs(channel TEXT, title TEXT, start_date TIMESTAMP, stop_date TIMESTAMP, description TEXT)')
             con.commit()

             # Get the loaded data
             total_count = data.count('programme')/2
             tv_elem = ElementTree.parse(StringIO.StringIO(data)).getroot()
             cur = con.cursor()
             count = 1
             channels = OrderedDict()

             for channel in tv_elem.findall('channel'):
                 channel_name = channel.find('display-name').text
                 for program in channel.findall('programme'):
                     if __killthread__:
                         raise AbortDownload('filling')
                     title = program.find('title').text
                     start_time = program.get("start")
                     stop_time = program.get("stop")
                     cur.execute("INSERT INTO programs(channel, title, start_date, stop_date)" + " VALUES(?, ?, ?, ?)", [channel_name, title, start_time, stop_time])
                     status = 10 + int(float(count)/float(total_count) * 90.0)
                     self.getControl(42021).setLabel(str(status) + '%')
                     xbmc.sleep(10)
                     count += 1
                 con.commit()
             print 'Channels have been successfully stored into the database!'
             self.getControl(42021).setLabel('100%')
             xbmc.sleep(3000)

             # Set the date and time row
             current_time = time.time() # now (in seconds)
             half_hour = current_time + 60*30  # now + 30 minutes
             one_hour = current_time + 60*60  # now + 60 minutes

             for t in [current_time,half_hour,one_hour]:
                 if (0 <= datetime.datetime.now().minute <= 29):
                     self.getControl(42041).setLabel(time.strftime("%I").lstrip('0') + ':00' + time.strftime("%p"))
                     self.getControl(42051).setLabel(time.strftime("%I").lstrip('0') + ':30' + time.strftime("%p"))
                     self.getControl(42061).setLabel(time.strftime("%I" + ":00%p",time.localtime(t)).lstrip("0"))
                 else:
                     self.getControl(42041).setLabel(time.strftime("%I").lstrip('0') + ':30' + time.strftime("%p"))
                     self.getControl(42051).setLabel(time.strftime("%I" + ":00%p",time.localtime(t)).lstrip("0"))
                     self.getControl(42061).setLabel(time.strftime("%I" + ":30%p",time.localtime(t)).lstrip("0"))


             #Pull the data from the database
             channelList = list()
             database_path = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))

             if os.path.exists(database_path):
                 #get the channels list
                 cur.execute('SELECT channel FROM programs WHERE channel GROUP BY channel')

                 for row in cur:
                     channels = row[0].encode('ascii')
                     channelList.append(channels)

                 # set the channels text
                 for index in range(0, CHANNELS_PER_PAGE):
                     channel = channelList[index]
                     channel_index = index

                     if channel is not None:
                         self.getControl(4110 + index).setLabel(channel)

                     #get the programs list
                     cur = con.cursor()
                     cur.execute('SELECT channel, title, start_date, stop_date FROM programs WHERE channel=?', [channel])
                     programList = list()
                     programs = cur.fetchall()
                     start_pos = 375    # indent for first program

                     for ind, row in enumerate(programs):
                         program = row[1].encode('ascii'), str(row[2]), str(row[3])
                         title = row[1].encode('ascii')
                         program_start_date = str(row[2])
                         program_end_date = str(row[3])
                         
                         #convert the date formats into minutes
                         minutes_start = self.parseDateTimeToMinutesSinceEpoch(program_start_date)
                         minutes_end = self.parseDateTimeToMinutesSinceEpoch(program_end_date)
                         minutes_length = minutes_end - minutes_start

                         program_length = minutes_length
                         program_notification = program
                         programs_top = 315
                         program_height = 33
                         program_gap = 3
                         position_start = start_pos
                         position_top = programs_top + channel_index * (program_height + program_gap + 1.5)

                         #create width size for per program button
                         if 10 <= program_length < 60:
                            program_width = 342.5
                         elif 60 <= program_length < 90:
                             program_width = 690
                         elif 90 <= program_length < 105:
                             program_width = 1050
                         elif 105 <= program_length < 120:
                             program_width = 1400
                         elif 120 <= program_length < 150:
                             program_width = 1750
                         elif 150 <= program_length < 180:
                             program_width = 2100
                         elif 180 <= program_length < 210:
                             program_width = 2450
                         elif 210 <= program_length < 240:
                             program_width = 2800
                         elif 240 <= program_length < 270:
                             program_width = 3150
                         elif 270 <= program_length < 300:
                             program_width = 3500
                         elif 300 <= program_length < 330:
                             program_width = 3850
                         elif 330 <= program_length < 360:
                             program_width = 4200
                         elif 360 <= program_length < 390:
                             program_width = 3250
                         elif 390 <= program_length < 420:
                             program_width = 4550
                         elif 420 <= program_length < 450:
                             program_width = 4900
                         elif 450 <= program_length < 480:
                             program_width = 5250

                         start_pos += program_width + 2 * program_gap + 1

                         if program_width > 1:
                             if yellow_flag:
                                 if program_notification:
                                     button_nofocus = 'changelang_yellow.png'
                                     button_focus = 'channels_yellow.png'
                                 else:
                                     button_nofocus = 'changelang_yellow.png'
                                     button_focus = 'channels_yellow.png'
                                 yellow_flag = False
                                 text_color = '0xFF000000'
                                 
                             else:
                                 if program_notification:
                                     button_nofocus = 'channels_bar1.png'
                                     button_focus = 'channels_yellow.png'
                                 else:
                                     button_nofocus = 'channels_bar1.png'
                                     button_focus = 'channels_yellow.png'
                                 text_color = '0xFFFFFFFF'

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
                                 focusTexture = button_focus, 
                                 noFocusTexture = button_nofocus,
                                 textColor = text_color,
                             )
                             self.program_buttons.append(ControlProgramList(program_controls, programs))
                             self.addControl(program_controls)
                     cur.close()

             #set the program focus control
             self.addControl(xbmcgui.ControlImage(1248, 0, 38, 720, 'hide-channels.png'))



             #Enabled EPG and other controls
             self.getControl(4200).setVisible(False)
             self.getControl(42021).setVisible(False)
             self.getControl(4203).setVisible(False)
             self.getControl(42041).setVisible(True)
             self.getControl(42051).setVisible(True)
             self.getControl(42061).setVisible(True)



         except AbortDownload, e:
             __killthread__ = False
             if e.value == 'downloading':
                 try:
                    if response is not None:
                         self.thread = AllChannelsThread(self.All_Channels)
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





     def BACKUP_________(self):
         yellow_flag = True
         global __killthread__
         self.getControl(42021).setLabel("0%")
         try:
             # DOWNLOAD THE XML SOURCE HERE
             url = ADDON.getSetting('allchannel.url')
             data = ''
             response = urllib2.urlopen(url)
             meta = response.info()
             file_size = int(meta.getheaders("Content-Length")[0])
             file_size_dl = 0
             block_size = 2048
             while True and not __killthread__:
                 mbuffer = response.read(block_size)
                 if not mbuffer:
                     break
                 file_size_dl += len(mbuffer)
                 data += mbuffer
                 state = int(file_size_dl * 10.0 / file_size)
                 self.getControl(42021).setLabel(str(state) + '%')
             else:
                 if __killthread__:
                     raise AbortDownload('downloading')
             del response

             # CREATE DATABASE
             profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
             if os.path.exists(profilePath):
                 os.remove(profilePath)
             con = database.connect(profilePath)
             cur = con.cursor()
             cur.execute('CREATE TABLE programs(channel TEXT, title TEXT, start_date TIMESTAMP, stop_date TIMESTAMP, description TEXT)')
             con.commit()

             # Get the loaded data
             total_count = data.count('programme')/2
             tv_elem = ElementTree.parse(StringIO.StringIO(data)).getroot()
             cur = con.cursor()
             count = 1
             channels = OrderedDict()

             for channel in tv_elem.findall('channel'):
                 channel_name = channel.find('display-name').text
                 for program in channel.findall('programme'):
                     if __killthread__:
                         raise AbortDownload('filling')
                     title = program.find('title').text
                     start_time = program.get("start")
                     stop_time = program.get("stop")
                     cur.execute("INSERT INTO programs(channel, title, start_date, stop_date)" + " VALUES(?, ?, ?, ?)", [channel_name, title, start_time, stop_time])
                     status = 10 + int(float(count)/float(total_count) * 90.0)
                     self.getControl(42021).setLabel(str(status) + '%')
                     xbmc.sleep(10)
                     count += 1
                 con.commit()
             print 'Channels have been successfully stored into the database!'
             self.getControl(42021).setLabel('100%')
             xbmc.sleep(3000)
             
             # Set the date and time row
             current_time = time.time() # now (in seconds)
             half_hour = current_time + 60*30  # now + 30 minutes
             one_hour = current_time + 60*60  # now + 60 minutes

             for t in [current_time,half_hour,one_hour]:
                 if (0 <= datetime.datetime.now().minute <= 29):
                     self.getControl(42041).setLabel(time.strftime("%I").lstrip('0') + ':00' + time.strftime("%p"))
                     self.getControl(42051).setLabel(time.strftime("%I").lstrip('0') + ':30' + time.strftime("%p"))
                     self.getControl(42061).setLabel(time.strftime("%I" + ":00%p",time.localtime(t)).lstrip("0"))
                 else:
                     self.getControl(42041).setLabel(time.strftime("%I").lstrip('0') + ':30' + time.strftime("%p"))
                     self.getControl(42051).setLabel(time.strftime("%I" + ":00%p",time.localtime(t)).lstrip("0"))
                     self.getControl(42061).setLabel(time.strftime("%I" + ":30%p",time.localtime(t)).lstrip("0"))


             #Pull the data from the database
             channelList = list()
             database_path = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))

             if os.path.exists(database_path):
                 #get the channels list
                 cur.execute('SELECT channel FROM programs WHERE channel GROUP BY channel')

                 for row in cur:
                     channels = row[0].encode('ascii')
                     channelList.append(channels)


                 # set the channels text
                 for index in range(0, CHANNELS_PER_PAGE):
                     channel = channelList[index]
                     channel_index = index

                     if channel is not None:
                         channels_list = 4325
                         channel_controls = self.getControl(channels_list)
                         channel_controls.addItem(channel) #Set the channel texts
                         channel_controls.selectItem(0)


                     #get the programs list
                     cur.execute('SELECT channel, title, start_date, stop_date FROM programs WHERE channel=?', [channel])
                     programList = list()
                     programs = cur.fetchall()
                     start_pos = 368    # indent for first program

                     for row in programs:
                         program = row[1].encode('ascii'), str(row[2]), str(row[3])
                         title = row[1].encode('ascii')
                         program_start_date = str(row[2])
                         program_end_date = str(row[3])

                         #convert the date formats into minutes
                         minutes_start = self.parseDateTimeToMinutesSinceEpoch(program_start_date)
                         minutes_end = self.parseDateTimeToMinutesSinceEpoch(program_end_date)
                         minutes_length = minutes_end - minutes_start

                         program_length = minutes_length
                         program_notification = program
                         programs_top = 315
                         program_height = 34.5
                         program_gap = 2.5
                         position_start = start_pos
                         position_top = programs_top + channel_index * (program_height + program_gap)


                         #create width size for per program button
                         if 10 <= program_length < 60:
                            program_width = 342.5
                         elif 60 <= program_length < 90:
                             program_width = 690
                         elif 90 <= program_length < 105:
                             program_width = 1050
                         elif 105 <= program_length < 120:
                             program_width = 1400
                         elif 120 <= program_length < 150:
                             program_width = 1750
                         elif 150 <= program_length < 180:
                             program_width = 2100
                         elif 180 <= program_length < 210:
                             program_width = 2450
                         elif 210 <= program_length < 240:
                             program_width = 2800
                         elif 240 <= program_length < 270:
                             program_width = 3150
                         elif 270 <= program_length < 300:
                             program_width = 3500
                         elif 300 <= program_length < 330:
                             program_width = 3850
                         elif 330 <= program_length < 360:
                             program_width = 4200
                         elif 360 <= program_length < 390:
                             program_width = 3250
                         elif 390 <= program_length < 420:
                             program_width = 4550
                         elif 420 <= program_length < 450:
                             program_width = 4900
                         elif 450 <= program_length < 480:
                             program_width = 5250

                         start_pos += program_width + 2 * program_gap

                         if program_width > 1:
                             if yellow_flag:
                                 if program_notification:
                                     button_nofocus = 'changelang_yellow.png'
                                     button_focus = 'channels_bar1.png'
                                 else:
                                     button_nofocus = 'changelang_yellow.png'
                                     button_focus = 'channels_bar1.png'
                                 yellow_flag = False
                                 text_color = '0xFF000000'

                             else:
                                 if program_notification:
                                     button_nofocus = 'channels_bar1.png'
                                     button_focus = 'channels_yellow.png'
                                 else:
                                     button_nofocus = 'channels_bar1.png'
                                     button_focus = 'channels_yellow.png'
                                 text_color = '0xFFFFFFFF'

                             if program_width < 1:
                                 program_title = ''
                             else:
                                 program_title = '[B]' + title + '[/B]'


                             program_controls = xbmcgui.ControlButton(
                                 position_start, 
                                 position_top, 
                                 program_width, 
                                 program_height, 
                                 program_title,
                                 textColor = text_color,
                                 focusTexture = button_focus, 
                                 noFocusTexture = button_nofocus
                             )
                             self.addControl(program_controls)
                     cur.close()
                             





             #Enabled EPG and other controls
             self.getControl(4200).setVisible(False)
             self.getControl(42021).setVisible(False)
             self.getControl(4203).setVisible(False)
             self.getControl(42041).setVisible(True)
             self.getControl(42051).setVisible(True)
             self.getControl(42061).setVisible(True)



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




     #def showepg(self, channels, page_no):
         #self.last_page = False
        # self.removeControls(self.buttonList)
         #self.buttonList = []
         #channel = 0
         #page_no = 0
 
         #self.button = [[0 for x in xrange(69)] for x in xrange(69)]
         #self.pdata = [[dict() for x in xrange(69)] for x in xrange(69)]

         #row = 0
         #for channel in range(page_no, 7):
         #for channel in channels[page_no*7:page_no*7+7]:
             #print "pass"
             #self.pdata[row][0]['url'] = channel['url']
             #self.pdata[row][0]['cname'] = xbmcgui.ControlLabel(0, self.startPos + 17 + (row * row_height), 100, row_height, channel['callSign'])
             #self.pdata[row][0]['cicon']  = channel['thumbnail'].replace('\\','')
             #self.pdata[row][0]['cimage'] = xbmcgui.ControlImage(100, self.startPos + (row * row_height), logo_width, logo_width,self.pdata[row][0]['cicon'])
             #self.buttonList.append(self.pdata[row][0]['cimage'])
             #self.buttonList.append(self.pdata[row][0]['cname'])
 
             #events = channel['events']
             #col = 0
             #coffset = 0
             #for event in events:
                 #try:
                     #self.pdata[row][col]['desc'] = '%s - %s\n%s' % (event['startTimeDisplay'], event['endTimeDisplay'], str(event['program']['description']))
                 #except:
                     #self.pdata[row][col]['desc'] = ""
                     #self.pdata[row][col]['duration'] = str(event['duration'])
                     #self.pdata[row][col]['eptitle'] = '%s - %s : %s' % (event['startTimeDisplay'], event['endTimeDisplay'], event['eptitle'])
 
                     #cwidth = int((float(event['percentWidth']) / 100) * progs_width)
                     #self.button[row][col] = xbmcgui.ControlButton(poffset + coffset, self.startPos + (row * row_height), cwidth, row_height, event['program']['title'])
                     #self.buttonList.append(self.button[row][col])
                     #coffset = coffset + cwidth
                     #col = col + 1
                 #row =  row + 1
         
                 #if row == MAXIMUMROW:
                     #break
 
         #self.addControls(self.buttonList)
 
         #if row == 0:
             #self.current_page = 0
             #self.showepg(channels, 0) # hack to display first page after last page - could be problem for empty epg
             #return
 
         #elif row < MAXIMUMROW:
             #self.last_page = True
 
         #maxrow = row
         #for row in range(maxrow + 1):
             #for col in range(20):
                 #if self.button[row][col] == 0:
                     #break
                 #else:
                     #if row < maxrow-1:
                         #self.button[row][col].controlDown(self.button[row+1][0])
                     #if row == maxrow-1:
                         #if maxrow == MAXIMUMROW:
                             #self.button[row][col].controlDown(self.button[row][col])
                     #if col > 0:
                         #self.button[row][col].controlLeft(self.button[row][col-1])
                         #self.button[row][col-1].controlRight(self.button[row][col])
                     #if row > 0:
                         #self.button[row][col].controlUp(self.button[row-1][0])
                     #if row == 0:
                         #self.button[row][col].controlUp(self.button[row][col])
 
 
         #self.topRow = True
         #self.bottomRow = False
         #control = self.button[0][0]
         #self.setFocus(control)
         #self.updateEpg(control)




     def Entertainment(self):
         pass



     def Movies(self):
         pass



     def Kids(self):
         pass



     def Sports(self):
         pass



     def News(self):
         pass



     def Documentaries(self):
         pass



     def MusicAndRadio(self):
         pass



     def Adult(self):
         pass



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
             self.getControl(4000).setVisible(True)
             self.getControl(4001).setVisible(True)
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
                 self.getControl(4004).setVisible(True)
                 self.getControl(4005).setVisible(True)
                 self.getControl(4007).setVisible(True)
                 self.getControl(4008).setVisible(True)



     def View_Restrictions(self):
         pass                 



     def Remove_Channels(self):
         pass



     def System_Details(self):
         pass



     def Speed_Test(self):
         pass



     def onAction(self, action):
         tvguide_table = xbmc.getCondVisibility('Control.IsVisible(5000)')
         tvguide_1 = xbmc.getCondVisibility('Control.IsVisible(5001)')
         tvguide_2 = xbmc.getCondVisibility('Control.IsVisible(42011)')
         tvguide_3 = xbmc.getCondVisibility('Control.IsVisible(4001)')
         tvguide_4 = xbmc.getCondVisibility('Control.IsVisible(4002)')
         tvguide_5 = xbmc.getCondVisibility('Control.IsVisible(4003)')
         tvguide_6 = xbmc.getCondVisibility('Control.IsVisible(4004)')
         tvguide_7 = xbmc.getCondVisibility('Control.IsVisible(4011)')
         tvguide_8 = xbmc.getCondVisibility('Control.IsVisible(4012)')
         tvguide_9 = xbmc.getCondVisibility('Control.IsVisible(4013)')
         tvguide_10 = xbmc.getCondVisibility('Control.IsVisible(4014)')
         tvguide_11 = xbmc.getCondVisibility('Control.IsVisible(4020)')
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
         lang_yellow = xbmc.getCondVisibility('Control.IsVisible(116)')
         lang_blue = xbmc.getCondVisibility('Control.IsVisible(117)')
         englishblck_enabled = xbmc.getCondVisibility('Control.IsVisible(118)')
         englishwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(119)')
         frenchblck_enabled = xbmc.getCondVisibility('Control.IsVisible(120)')
         frenchwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(121)')
         germanblck_enabled = xbmc.getCondVisibility('Control.IsVisible(122)')
         germanwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(123)')
         italianblck_enabled = xbmc.getCondVisibility('Control.IsVisible(124)')
         italianwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(125)')
         spainishblck_enabled = xbmc.getCondVisibility('Control.IsVisible(126)')
         spainishwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(127)')
         russianblck_enabled = xbmc.getCondVisibility('Control.IsVisible(128)')
         russianwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(129)')
         portugueseblck_enabled = xbmc.getCondVisibility('Control.IsVisible(130)')
         portuguesewhte_enabled = xbmc.getCondVisibility('Control.IsVisible(131)')
         greekblck_enabled = xbmc.getCondVisibility('Control.IsVisible(132)')
         greekwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(133)')
         dutchblck_enabled = xbmc.getCondVisibility('Control.IsVisible(134)')
         dutchwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(135)')
         chineseblck_enabled = xbmc.getCondVisibility('Control.IsVisible(136)')
         chinesewhte_enabled = xbmc.getCondVisibility('Control.IsVisible(137)')
         koreanblck_enabled = xbmc.getCondVisibility('Control.IsVisible(138)')
         koreanwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(139)')
         arabicblck_enabled = xbmc.getCondVisibility('Control.IsVisible(140)')
         arabicwhte_enabled = xbmc.getCondVisibility('Control.IsVisible(141)')
         langsavesettings_yellow = xbmc.getCondVisibility('Control.IsVisible(142)')
         loading_gif = xbmc.getCondVisibility('Control.IsVisible(4200)')
         #self.strAction = xbmcgui.ControlLabel(300, 200, 600, 200, '', 'font14', '0xFF00FF00')
         #self.addControl(self.strAction)
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
         savesettings_yellow_enabled = xbmc.getCondVisibility('Control.IsVisible(142)')
         PIN_1_enabled = xbmc.getCondVisibility('Control.IsVisible(4009)')
         PIN_2_enabled = xbmc.getCondVisibility('Control.IsVisible(4010)')
         PIN_3_enabled = xbmc.getCondVisibility('Control.IsVisible(4011)')
         PIN_4_enabled = xbmc.getCondVisibility('Control.IsVisible(4012)')
         PIN_chars_1_enabled = xbmc.getCondVisibility('Control.IsVisible(4013)')
         PIN_chars_2_enabled = xbmc.getCondVisibility('Control.IsVisible(4014)')
         PIN_chars_3_enabled = xbmc.getCondVisibility('Control.IsVisible(4015)')
         PIN_chars_4_enabled = xbmc.getCondVisibility('Control.IsVisible(4016)')
         channel_1_yellow = xbmc.getCondVisibility('Control.IsVisible(4207)')
         channel_2_yellow = xbmc.getCondVisibility('Control.IsVisible(4208)')
         channel_3_yellow = xbmc.getCondVisibility('Control.IsVisible(4209)')
         channel_4_yellow = xbmc.getCondVisibility('Control.IsVisible(4210)')
         channel_5_yellow = xbmc.getCondVisibility('Control.IsVisible(4211)')
         channel_6_yellow = xbmc.getCondVisibility('Control.IsVisible(4212)')
         channel_7_yellow = xbmc.getCondVisibility('Control.IsVisible(4213)')
         main_loading = 4200
         main_loading_progress = 42011
         main_loading_time_left = 42021


         if action == ACTION_PREVIOUS_MENU:
             self.close()
             return



         if action == ACTION_BACKSPACE:
             if allchannels_enabled:
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
                 cSetVisible(self,146,False)
                 cSetVisible(self,4200,False)
                 cSetVisible(self,42011,False)
                 cSetVisible(self,42021,False)
                 self.getControl(42021).setLabel("")
                 ADDON.setSetting('allchannels.enabled', 'false')
                 self.abortdownload()
                 self.getControl(42021).setLabel('')
                 self.getControl(4203).setVisible(False)
                 self.getControl(42041).setVisible(False)
                 self.getControl(42051).setVisible(False)
                 self.getControl(42061).setVisible(False)
                 profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
                 # Deletes the db file if it persists after abort
                 if os.path.exists(profilePath):
                     os.remove(profilePath)


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




             if entertainment_enabled:
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
                 cSetVisible(self,114,False)
                 cSetVisible(self,115,False)
                 cSetVisible(self,116,False)
                 cSetVisible(self,143,False)
                 ADDON.setSetting('changelanguage.enabled', 'false')


                 if savesettings_yellow_enabled:
                     cSetVisible(self,111,False)
                     cSetVisible(self,117,False)
                     cSetVisible(self,142,False)
                     
                     
                     if english_enabled:
                         cSetVisible(self,113,False)
                         cSetVisible(self,144,False)


                 if english_enabled:
                     cSetVisible(self,109,False)
                     cSetVisible(self,110,False)
                     cSetVisible(self,112,False)
                     cSetVisible(self,145,False)
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
                         cSetVisible(self,118,False)
                     elif englishwhte_enabled:
                         cSetVisible(self,119,False)

                     if frenchblck_enabled:
                         cSetVisible(self,120,False)
                     elif frenchwhte_enabled:
                         cSetVisible(self,121,False)


                     if germanblck_enabled:
                         cSetVisible(self,122,False)
                     elif germanwhte_enabled:
                         cSetVisible(self,123,False)


                     if italianblck_enabled:
                         cSetVisible(self,124,False)
                     elif italianwhte_enabled:
                         cSetVisible(self,125,False)


                     if spainishblck_enabled:
                         cSetVisible(self,126,False)
                     elif spainishwhte_enabled:
                         cSetVisible(self,127,False)


                     if russianblck_enabled:
                         cSetVisible(self,128,False)
                     elif russianwhte_enabled:
                         cSetVisible(self,129,False)


                     if portugueseblck_enabled:
                         cSetVisible(self,130,False)
                     elif portuguesewhte_enabled:
                         cSetVisible(self,131,False)


                     if greekblck_enabled:
                         cSetVisible(self,132,False)
                     elif greekwhte_enabled:
                         cSetVisible(self,133,False)


                     if dutchblck_enabled:
                         cSetVisible(self,134,False)
                     elif dutchwhte_enabled:
                         cSetVisible(self,135,False)


                     if chineseblck_enabled:
                         cSetVisible(self,136,False)
                     elif chinesewhte_enabled:
                         cSetVisible(self,137,False)


                     if koreanblck_enabled:
                         cSetVisible(self,138,False)
                     elif koreanwhte_enabled:
                         cSetVisible(self,139,False)


                     if arabicblck_enabled:
                         cSetVisible(self,140,False)
                     elif arabicwhte_enabled:
                         cSetVisible(self,141,False)



             if changepin_enabled:
                 if PIN_chars_4_enabled:
                     if PIN_chars_4_enabled == True:
                         cSetVisible(self,4016,False)
                         cSetVisible(self,4012,True)
                 elif PIN_chars_3_enabled:
                     if PIN_chars_3_enabled == True:
                         cSetVisible(self,4015,False)
                         cSetVisible(self,4011,True)
                 elif PIN_chars_2_enabled:
                     if PIN_chars_2_enabled == True:
                         cSetVisible(self,4014,False)
                         cSetVisible(self,4010,True)
                 elif PIN_chars_1_enabled:
                     if PIN_chars_1_enabled == True:
                         cSetVisible(self,4013,False)
                         cSetVisible(self,4009,True)
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
                     cSetVisible(self,4000,False)
                     cSetVisible(self,4001,False)
                     cSetVisible(self,4002,False)
                     cSetVisible(self,4006,False)
                     cSetVisible(self,4009,False)
                     cSetVisible(self,4010,False)
                     cSetVisible(self,4011,False)
                     cSetVisible(self,4012,False)
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
                         cSetVisible(self,4003,False)
                         cSetVisible(self,4004,False)
                         cSetVisible(self,4005,False)
                         cSetVisible(self,4007,False)
                         cSetVisible(self,4008,False)


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
                     ADDON.setSetting('allchannels.enabled', 'true')
                     cSetVisible(self,146,True)
                     cSetVisible(self,4200,True)
                     cSetVisible(self,42011,True)
                     cSetVisible(self,42021,True)
                     self.getControl(42021).setLabel("0%")
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
                     cSetVisible(self,110,True)
                     cSetVisible(self,114,True)
                     cSetVisible(self,115,True)
                     cSetVisible(self,116,True)
                     cSetVisible(self,143,True)
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
                         cSetVisible(self,109,True)
                         cSetVisible(self,112,True)
                         cSetVisible(self,118,True)
                         cSetVisible(self,145,True)





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
                     cSetVisible(self,4000,True)
                     cSetVisible(self,4001,True)
                     cSetVisible(self,4002,True)
                     cSetVisible(self,4006,True)
                     cSetVisible(self,4009,True)
                     cSetVisible(self,4010,True)
                     cSetVisible(self,4011,True)
                     cSetVisible(self,4012,True)
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
                         cSetVisible(self,4003,True)
                         cSetVisible(self,4004,True)
                         cSetVisible(self,4005,True)
                         cSetVisible(self,4007,True)
                         cSetVisible(self,4008,True)





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
                 if savesettings_yellow_enabled:
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
                     cSetVisible(self,111,False)
                     cSetVisible(self,114,False)
                     cSetVisible(self,115,False)
                     cSetVisible(self,117,False)
                     cSetVisible(self,142,False)
                     ADDON.setSetting('changelanguage.enabled', 'false')


                     if english_enabled:
                         cSetVisible(self,109,False)
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




             if allchannels_enabled:

                 if channel_1_yellow:
                     getcontrolId = self.program_controls.getId
                     controlId = self.getControl(getcontrolId)
                     print controlId
                     
                 elif channel_2_yellow:
                     pass


                 elif channel_3_yellow:
                     pass


                 elif channel_4_yellow:
                     pass


                 elif channel_5_yellow:
                     pass


                 elif channel_6_yellow:
                     pass




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



             if changelanguage_enabled:
                 if englishblck_enabled == True:
                     cSetVisible(self,118,False)
                     cSetVisible(self,140,True)
                 elif frenchblck_enabled == True:
                     cSetVisible(self,120,False)
                     cSetVisible(self,118,True)
                 elif germanblck_enabled == True:
                     cSetVisible(self,122,False)
                     cSetVisible(self,120,True)
                 elif italianblck_enabled == True:
                     cSetVisible(self,124,False)
                     cSetVisible(self,122,True)
                 elif spainishblck_enabled == True:
                     cSetVisible(self,126,False)
                     cSetVisible(self,124,True)
                 elif russianblck_enabled == True:
                     cSetVisible(self,128,False)
                     cSetVisible(self,126,True)
                 elif portugueseblck_enabled == True:
                     cSetVisible(self,130,False)
                     cSetVisible(self,128,True)
                 elif greekblck_enabled == True:
                     cSetVisible(self,132,False)
                     cSetVisible(self,130,True)
                 elif dutchblck_enabled == True:
                     cSetVisible(self,134,False)
                     cSetVisible(self,132,True)
                 elif chineseblck_enabled == True:
                     cSetVisible(self,136,False)
                     cSetVisible(self,134,True)
                 elif koreanblck_enabled == True:
                     cSetVisible(self,138,False)
                     cSetVisible(self,136,True)
                 elif arabicblck_enabled == True:
                     cSetVisible(self,140,False)
                     cSetVisible(self,138,True)




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



             if allchannels_enabled:
                 if channel_1_yellow:
                     pass




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



             if changelanguage_enabled:
                 if english_enabled:
                     if englishblck_enabled == True:
                         self.getControl(118).setVisible(False)
                         self.getControl(120).setVisible(True)
                     elif frenchblck_enabled == True:
                         self.getControl(120).setVisible(False)
                         self.getControl(122).setVisible(True)
                     elif germanblck_enabled == True:
                         self.getControl(122).setVisible(False)
                         self.getControl(124).setVisible(True)
                     elif italianblck_enabled == True:
                         self.getControl(124).setVisible(False)
                         self.getControl(126).setVisible(True)
                     elif spainishblck_enabled == True:
                         self.getControl(126).setVisible(False)
                         self.getControl(128).setVisible(True)
                     elif russianblck_enabled == True:
                         self.getControl(128).setVisible(False)
                         self.getControl(130).setVisible(True)
                     elif portugueseblck_enabled == True:
                         self.getControl(130).setVisible(False)
                         self.getControl(132).setVisible(True)
                     elif greekblck_enabled == True:
                         self.getControl(132).setVisible(False)
                         self.getControl(134).setVisible(True)
                     elif dutchblck_enabled == True:
                         self.getControl(134).setVisible(False)
                         self.getControl(136).setVisible(True)
                     elif chineseblck_enabled == True:
                         self.getControl(136).setVisible(False)
                         self.getControl(138).setVisible(True)
                     elif koreanblck_enabled == True:
                         self.getControl(138).setVisible(False)
                         self.getControl(140).setVisible(True)
                     elif arabicblck_enabled == True:
                         self.getControl(140).setVisible(False)
                         self.getControl(118).setVisible(True)



         if action == ACTION_MOVE_UP:
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
                 if lang_yellow == True:
                     cSetVisible(self,110,False)
                     cSetVisible(self,111,True)
                     cSetVisible(self,114,False)
                     cSetVisible(self,115,False)
                     cSetVisible(self,116,False)
                     cSetVisible(self,117,True)
                     cSetVisible(self,143,False)
                     cSetVisible(self,142,True)



                     if english_enabled:
                         cSetVisible(self,112,False)
                         cSetVisible(self,113,True)
                         cSetVisible(self,145,False)
                         cSetVisible(self,144,True)


                     if englishblck_enabled:
                         cSetVisible(self,118,False)
                         cSetVisible(self,119,True)

                     if frenchblck_enabled:
                         cSetVisible(self,120,False)
                         cSetVisible(self,121,True)

                     if germanblck_enabled:
                         cSetVisible(self,122,False)
                         cSetVisible(self,123,True)

                     if italianblck_enabled:
                         cSetVisible(self,124,False)
                         cSetVisible(self,125,True)

                     if spainishblck_enabled:
                         cSetVisible(self,126,False)
                         cSetVisible(self,127,True)

                     if russianblck_enabled:
                         cSetVisible(self,128,False)
                         cSetVisible(self,129,True)

                     if portugueseblck_enabled:
                         cSetVisible(self,130,False)
                         cSetVisible(self,131,True)

                     if greekblck_enabled:
                         cSetVisible(self,132,False)
                         cSetVisible(self,133,True)

                     if dutchblck_enabled:
                         cSetVisible(self,134,False)
                         cSetVisible(self,135,True)

                     if chineseblck_enabled:
                         cSetVisible(self,136,False)
                         cSetVisible(self,137,True)

                     if koreanblck_enabled:
                         cSetVisible(self,138,False)
                         cSetVisible(self,139,True)

                     if arabicblck_enabled:
                         cSetVisible(self,140,False)
                         cSetVisible(self,141,True)



                 elif lang_blue == True:
                     cSetVisible(self,142,False)
                     cSetVisible(self,143,True)
                     cSetVisible(self,111,False)
                     cSetVisible(self,110,True)
                     cSetVisible(self,114,True)
                     cSetVisible(self,115,True)
                     cSetVisible(self,117,False)
                     cSetVisible(self,116,True)



                     if english_enabled:
                         cSetVisible(self,113,False)
                         cSetVisible(self,112,True)
                         cSetVisible(self,144,False)
                         cSetVisible(self,145,True)


                         if englishwhte_enabled:
                             cSetVisible(self,119,False)
                             cSetVisible(self,118,True)

                         if frenchwhte_enabled:
                             cSetVisible(self,121,False)
                             cSetVisible(self,120,True)

                         if germanwhte_enabled:
                             cSetVisible(self,123,False)
                             cSetVisible(self,122,True)

                         if italianwhte_enabled:
                             cSetVisible(self,125,False)
                             cSetVisible(self,124,True)

                         if spainishwhte_enabled:
                             cSetVisible(self,127,False)
                             cSetVisible(self,126,True)

                         if russianwhte_enabled:
                             cSetVisible(self,129,False)
                             cSetVisible(self,128,True)

                         if portuguesewhte_enabled:
                             cSetVisible(self,131,False)
                             cSetVisible(self,130,True)

                         if greekwhte_enabled:
                             cSetVisible(self,133,False)
                             cSetVisible(self,132,True)

                         if dutchwhte_enabled:
                             cSetVisible(self,135,False)
                             cSetVisible(self,134,True)

                         if chinesewhte_enabled:
                             cSetVisible(self,137,False)
                             cSetVisible(self,136,True)

                         if koreanwhte_enabled:
                             cSetVisible(self,139,False)
                             cSetVisible(self,138,True)

                         if arabicwhte_enabled:
                             cSetVisible(self,141,False)
                             cSetVisible(self,140,True)




         if action == ACTION_MOVE_DOWN:
             if allchannels_enabled:
                 #Set the focus of the channel and program controls
                 channels_list = 4325
                 channel_controls = self.getControl(channels_list)
                 channel_controls.selectItem(1)
                 print "working"
                 #self.Channel_Down(self.channelIdx + CHANNELS_PER_PAGE, focusFunction = self.findControlBelow)




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
                 if lang_yellow == True:
                     cSetVisible(self,110,False)
                     cSetVisible(self,111,True)
                     cSetVisible(self,114,False)
                     cSetVisible(self,115,False)
                     cSetVisible(self,116,False)
                     cSetVisible(self,117,True)
                     cSetVisible(self,143,False)
                     cSetVisible(self,142,True)



                     if english_enabled:
                         cSetVisible(self,112,False)
                         cSetVisible(self,113,True)
                         cSetVisible(self,145,False)
                         cSetVisible(self,144,True)
                     
                     
                     if englishblck_enabled:
                         cSetVisible(self,118,False)
                         cSetVisible(self,119,True)

                     if frenchblck_enabled:
                         cSetVisible(self,120,False)
                         cSetVisible(self,121,True)

                     if germanblck_enabled:
                         cSetVisible(self,122,False)
                         cSetVisible(self,123,True)

                     if italianblck_enabled:
                         cSetVisible(self,124,False)
                         cSetVisible(self,125,True)

                     if spainishblck_enabled:
                         cSetVisible(self,126,False)
                         cSetVisible(self,127,True)

                     if russianblck_enabled:
                         cSetVisible(self,128,False)
                         cSetVisible(self,129,True)

                     if portugueseblck_enabled:
                         cSetVisible(self,130,False)
                         cSetVisible(self,131,True)

                     if greekblck_enabled:
                         cSetVisible(self,132,False)
                         cSetVisible(self,133,True)

                     if dutchblck_enabled:
                         cSetVisible(self,134,False)
                         cSetVisible(self,135,True)

                     if chineseblck_enabled:
                         cSetVisible(self,136,False)
                         cSetVisible(self,137,True)

                     if koreanblck_enabled:
                         cSetVisible(self,138,False)
                         cSetVisible(self,139,True)

                     if arabicblck_enabled:
                         cSetVisible(self,140,False)
                         cSetVisible(self,141,True)



                 elif lang_blue == True:
                     cSetVisible(self,142,False)
                     cSetVisible(self,143,True)
                     cSetVisible(self,111,False)
                     cSetVisible(self,110,True)
                     cSetVisible(self,114,True)
                     cSetVisible(self,115,True)
                     cSetVisible(self,117,False)
                     cSetVisible(self,116,True)



                     if english_enabled:
                         cSetVisible(self,113,False)
                         cSetVisible(self,112,True)
                         cSetVisible(self,144,False)
                         cSetVisible(self,145,True)


                         if englishwhte_enabled:
                             cSetVisible(self,119,False)
                             cSetVisible(self,118,True)

                         if frenchwhte_enabled:
                             cSetVisible(self,121,False)
                             cSetVisible(self,120,True)

                         if germanwhte_enabled:
                             cSetVisible(self,123,False)
                             cSetVisible(self,122,True)

                         if italianwhte_enabled:
                             cSetVisible(self,125,False)
                             cSetVisible(self,124,True)

                         if spainishwhte_enabled:
                             cSetVisible(self,127,False)
                             cSetVisible(self,126,True)

                         if russianwhte_enabled:
                             cSetVisible(self,129,False)
                             cSetVisible(self,128,True)

                         if portuguesewhte_enabled:
                             cSetVisible(self,131,False)
                             cSetVisible(self,130,True)

                         if greekwhte_enabled:
                             cSetVisible(self,133,False)
                             cSetVisible(self,132,True)

                         if dutchwhte_enabled:
                             cSetVisible(self,135,False)
                             cSetVisible(self,134,True)

                         if chinesewhte_enabled:
                             cSetVisible(self,137,False)
                             cSetVisible(self,136,True)

                         if koreanwhte_enabled:
                             cSetVisible(self,139,False)
                             cSetVisible(self,138,True)

                         if arabicwhte_enabled:
                             cSetVisible(self,141,False)
                             cSetVisible(self,140,True)



         #try:
             #control = self.getFocus()
         #except:
             #control = self.button[0][0]
         #self.updateEpg(control)



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
                         cSetVisible(self,4009,False)
                         cSetVisible(self,4013,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)


                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)


                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)


                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
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
                         cSetVisible(self,4009,False)
                         cSetVisible(self,4013,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
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
                         cSetVisible(self,4009,False)
                         cSetVisible(self,4013,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
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
                         cSetVisible(self,4009,False)
                         cSetVisible(self,4013,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
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
                         cSetVisible(self,4009,False)
                         cSetVisible(self,4013,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
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
                         cSetVisible(self,4009,False)
                         cSetVisible(self,4013,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
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
                         cSetVisible(self,4009,False)
                         cSetVisible(self,4013,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
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
                         cSetVisible(self,4009,False)
                         cSetVisible(self,4013,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
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
                         cSetVisible(self,4009,False)
                         cSetVisible(self,4013,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
                     elif PIN_4_enabled == False:
                         pass


                     elif PIN_4_enabled:
                         if PIN_4_enabled == True:
                             cSetVisible(self,4012,False)
                             cSetVisible(self,4016,True)
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
                         cSetVisible(self,4009,False)
                         cSetVisible(self,4013,True)
                     elif PIN_1_enabled == False:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                 elif PIN_2_enabled:
                     if PIN_2_enabled == True:
                         cSetVisible(self,4010,False)
                         cSetVisible(self,4014,True)
                     elif PIN_2_enabled == False:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                 elif PIN_3_enabled:
                     if PIN_3_enabled == True:
                         cSetVisible(self,4011,False)
                         cSetVisible(self,4015,True)
                     elif PIN_3_enabled == False:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
                 elif PIN_4_enabled:
                     if PIN_4_enabled == True:
                         cSetVisible(self,4012,False)
                         cSetVisible(self,4016,True)
                     elif PIN_4_enabled == False:
                         pass




     def updateEpg(self, control):
         if control != 0:
             for row in range(7):
                 for col in range(69):
                     if control == self.button[row][col]:
                         name = control.getLabel()
                         plot = self.pdata[row][col]['desc']
                         self.current_plot.reset()
                         self.current_plot.setText( '%s\n%s' % (name, plot) )
                         if row == 0:
                             self.topRow = True
                             self.bottomRow = False
                         elif row == 7:
                             self.topRow = False
                             self.bottomRow = True
                         else:
                             self.topRow = False
                             self.bottomRow = False




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