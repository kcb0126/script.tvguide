import xbmc
import xbmcgui
import xbmcaddon
import datetime
import time

ADDON = xbmcaddon.Addon(id = 'script.tvguide')

class MyClass(xbmcgui.WindowXML):

     def __new__(cls):
         return super(MyClass, cls).__new__(cls, 'script-tvguide-mainmenu.xml', ADDON.getAddonInfo('path'))
         
     def onInit(self):
         print "WTH"
         
         #
         self.PIXELS_PER_MINUTE = 2400 / 300 # pixels (the area we want to display in) / minutes (how many minutes we want to display in that given area)
         
         #
         button_nofocus = 'channels_bar1.png'
         button_focus = 'channels_bar1.png'
         
         #
         self.PROGRAM_AREA_X = 50
         self.PROGRAM_AREA_Y = 100
         self.PROGRAM_HEIGHT = 50
         self.GAP            = 10
         
         #
         # Channel #1
         #
         
         #1 starts at 00:00 for 30 minutes
         self.displayProgram({ 'channel': 1, 'program': 1, 'title': '#1-#1', 'start': 0 * 60     , 'length': 30})

         #2 starts at 00:30 for 60 minutes
         self.displayProgram({ 'channel': 1, 'program': 2, 'title': '#1-#2', 'start': 0 * 60 + 30, 'length': 60})
         
         #3 starts at 01:30 for 15 minutes
         self.displayProgram({ 'channel': 1, 'program': 3, 'title': '#1-#3', 'start': 1 * 60 + 30, 'length': 15})
         
         #
         # Channel #2
         #
         
         #1 starts at 00:00 for 45 minutes
         self.displayProgram({ 'channel': 2, 'program': 1, 'title': '#2-#1', 'start': 0 * 60     , 'length': 45})

         #2 starts at 00:45 for 20 minutes
         self.displayProgram({ 'channel': 2, 'program': 2, 'title': '#2-#2', 'start': 0 * 60 + 45, 'length': 20})
         
         #3 starts at 01:05 for 40 minutes
         self.displayProgram({ 'channel': 2, 'program': 3, 'title': '#2-#3', 'start': 1 * 60 +  5, 'length': 40})
         
     def displayProgram(self, program):
        channel_index  = program['channel']
        program_index  = program['program']             # index in channel (not sure how you're going to define it, but let's stick with it for now)
        program_start  = program['start']               # in minutes
        program_length = program['length']              # in minutes
        program_title  = program['title']
        
        print program_start
        print program_length
        print program_title
        
        pos_x  = self.PROGRAM_AREA_X + (program_start * self.PIXELS_PER_MINUTE) + ((program_index - 1) * self.GAP)
        pos_y  = self.PROGRAM_AREA_Y + (channel_index * self.PROGRAM_HEIGHT)    + ((channel_index - 1) * self.GAP)
        width  = program_length * self.PIXELS_PER_MINUTE
        height = self.PROGRAM_HEIGHT
       
        button = xbmcgui.ControlButton(
            pos_x, 
            pos_y, 
            width, 
            height, 
            program_title, 
            focusTexture = 'channels_bar1.png', 
            noFocusTexture = 'channels_bar1.png'
        )
        self.addControl(button)