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