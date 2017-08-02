import datetime
import time
import xbmc
import xbmcgui
import os
from sqlite3 import dbapi2 as database



def get_programming_times(self):
     #global self.program_stop_minutes, self.program_stop_time, self.epg_time_1, self.epg_time_2, self.epg_time_3
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


     for pos_X, pos_Y, prog_id, prog_width in zip(positions_X, positions_Y, programs_id, program_width):
         if self.select_db_flag == True:
             self.select_db_flag = False
             profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
             conn1 = database.connect(profilePath)
             cur1 = conn1.cursor()
             cur1.execute('SELECT stop_date FROM programs where button_id=?', [self.program_id])
             stop_date = cur1.fetchone()

             if stop_date is not None:
                 stop_date = str(stop_date[0])
                 stop_time = time.strptime(str(stop_date), '%Y%m%d%H%M%S')
                 stop_time = datetime.datetime.fromtimestamp(time.mktime(stop_time))
                 program_stop_hours = stop_time.strftime('%H')
                 self.program_stop_minutes = stop_time.strftime('%M')
                 program_AM_PM = stop_time.strftime('%p')
                 half_hour = str(self.getControl(344).getLabel())
                 one_hour = str(self.getControl(345).getLabel())
                 one_hour_half = str(self.getControl(346).getLabel())
                 self.epg_time_1 = time.strptime(half_hour, '%I:%M%p')
                 self.epg_time_2 = time.strptime(one_hour, '%I:%M%p')
                 self.epg_time_3 = time.strptime(one_hour_half, '%I:%M%p')

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


                 self.program_stop_time = program_stop_hours +':' + self.program_stop_minutes + program_AM_PM
                 self.program_stop_time = time.strptime(self.program_stop_time, '%I:%M%p')


         return self.program_stop_minutes, self.program_stop_time




def GoRight(self):
     

     # change program controls to display the proper junks
     if self.channels_Index != len(self.program_buttons) - 1:
         if self.channel_page >= 0:
             CurrentId = self.getFocusId()
             CurrentRow = self.getControl(CurrentId).getX()
             CurrentRowY = self.getControl(CurrentId).getY()
             CurrentWidth = self.getControl(CurrentId).getWidth()
             pixel_start = 375
             pixel_middle = 724
             pixel_end = 1073


             if self.move_right_flag == False:
                 if self.channel_page == 15750:
                     pass
             else:
                 if CurrentRow:
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


                     #Store the list of strings in the lists
                     for i in range(len(posX)):
                         pos_X = posX[i]

                         if pos_X == '375':
                             self.program_id = list()
                             self.program_id.append(programs_id[i])
                             program_id = ''.join(str(x) for x in self.program_id)
                             pos_Y = self.getControl(int(program_id)).getY()
                             prog_width = self.getControl(int(program_id)).getWidth()
                             nextprogram = int(program_id) + 1
                             nextprogramX = self.getControl(int(nextprogram)).getX()
                             nextprogram_width = self.getControl(int(nextprogram)).getWidth()
                             nextprogram_label = self.getControl(int(nextprogram)).getLabel()
                             nextprogram1 = int(nextprogram) + 1
                             nextprogram1_width = self.getControl(int(nextprogram1)).getWidth()
                             nextprogram1_label = self.getControl(int(nextprogram1)).getLabel()
                             nextprogram2 = int(nextprogram1) + 1
                             nextprogram2_width = self.getControl(int(nextprogram2)).getWidth()
                             nextprogram2_label = self.getControl(int(nextprogram2)).getLabel()
                             nextprogram3 = int(nextprogram2) + 1
                             nextprogram3_width = self.getControl(int(nextprogram3)).getWidth()
                             nextprogram3_label = self.getControl(int(nextprogram3)).getLabel()
                             CurrentRowID = self.getFocusId()
                             CurrentRow = self.getControl(CurrentRowID).getX()
                             CurrentWidth = self.getControl(CurrentRowID).getWidth()


                     #for pos_X, pos_Y, prog_id, prog_width in zip(positions_X, positions_Y, programs_id, program_width):
                         #if CurrentRow:
                             #pos_Y = self.getControl(int(program_id)).getY()


                             if int(pos_X) == 375 and int(prog_width) == 5515:
                                 programs_width = 5173
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 5344:
                                 programs_width = 5002
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 5173:
                                 programs_width = 4831
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 5002:
                                 programs_width = 4660
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 4831:
                                 programs_width = 4489
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 4660:
                                 programs_width = 4318
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 4489:
                                 programs_width = 4147
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 4317:
                                 programs_width = 3975
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 4146:
                                 programs_width = 3804
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 3976:
                                 programs_width = 3634
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 3805:
                                 programs_width = 3463
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 3634:
                                 programs_width = 3292
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 3463:
                                 programs_width = 3121
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 3292:
                                 programs_width = 2947
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 3121:
                                 programs_width = 2779
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 3078:
                                 programs_width = 2736
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 2947:
                                 programs_width = 2608
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 2779:
                                 programs_width = 2437
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 2736:
                                 programs_width = 2394
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 2608:
                                 programs_width = 2253
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 2394:
                                 programs_width = 2052
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 2253:
                                 programs_width = 1906
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 2082:
                                 programs_width = 1735
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 2052:
                                 programs_width = 1710
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 1906:
                                 programs_width = 1563
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 1735:
                                 programs_width = 1392
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 1710:
                                 programs_width = 1368
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 1563:
                                 programs_width = 1221
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 1425:
                                 programs_width = 1038
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 1392:
                                 programs_width = 1038
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                             elif int(pos_X) == 375 and int(prog_width) == 1368:
                                 programs_width = 1026
                                 self.getControl(int(program_id)).setWidth(int(programs_width))
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getWidth()
                                 nextprogram_width = self.getControl(int(nextprogram)).getX()
                                 
                                 
                                 self.program_id = int(program_id)
                                 self.select_db_flag = True
                                 self.program_stop_minutes,self.program_stop_time = get_programming_times(self)

                                 if self.program_stop_time > self.epg_time_3:
                                     if self.program_stop_minutes == '10':
                                         if int(prog_width) == 1368:
                                             programs_width = 804
                                             self.getControl(int(program_id)).setWidth(int(programs_width))
 
                                             if nextprogramX != 1186:
                                                 pos_Y = self.getControl(int(nextprogram)).getY()
                                                 self.getControl(int(nextprogram)).setPosition(1186, int(pos_Y))
                                                 self.getControl(int(nextprogram)).setVisible(True)




                             elif int(pos_X) == 375 and int(prog_width) == 1311:
                                 programs_width = 969
                                 self.getControl(int(program_id)).setWidth(int(programs_width))
                                 self.program_id = int(program_id)
                                 self.select_db_flag = True
                                 self.program_stop_minutes,self.program_stop_time = get_programming_times(self)
                                 print "self.program_stop_minutes"
                                 print self.program_stop_minutes

                                 #if self.program_stop_time == self.epg_time_3:
                                     #if self.program_stop_minutes == '00':
                                         #if program_width == 969:
                                             #program_width = 691
                                             #self.getControl(int(program_id)).setWidth(int(program_width))
                                             #nextprogram = int(program_id) + 1
                                             #pos_Y = self.getControl(int(nextprogram)).getY()
                                             #self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                             #self.getControl(int(nextprogram)).setVisible(True)



                             elif int(pos_X) == 375 and int(prog_width) == 1254:
                                 programs_width = 804
                                 self.getControl(int(program_id)).setWidth(int(programs_width))
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 nextprogram_width = self.getControl(int(nextprogram)).getWidth()

                                 if programs_width == 804:
                                     if nextprogramX != 1186:
                                         pos_Y = self.getControl(int(nextprogram)).getY()
                                         self.getControl(int(nextprogram)).setPosition(1186, int(pos_Y))
                                         self.getControl(int(nextprogram)).setVisible(True)




                             elif int(pos_X) == 375 and int(prog_width) == 1221:
                                 programs_width = 879
                                 self.getControl(int(program_id)).setWidth(int(programs_width))

                                 if int(programs_width) == 879:
                                     nextprogram = int(CurrentId) + 1
                                     #self.getControl(int(nextprogram)).setVisible(False)



                             elif int(pos_X) == 375 and int(prog_width) == 1083:
                                 programs_width = 626
                                 self.getControl(int(program_id)).setWidth(int(programs_width))
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 nextprogram_Width = self.getControl(int(nextprogram)).getWidth()

                                 if nextprogramX != 1008:
                                     pos_Y = self.getControl(int(nextprogram)).getY()
                                     self.getControl(int(nextprogram)).setPosition(1008, int(pos_Y))
                                     self.getControl(int(nextprogram)).setVisible(True)


                                     if nextprogram_Width == 59:
                                         nextprograms = int(nextprogram) + 1
                                         nextprogramsX = self.getControl(int(nextprograms)).getX()

                                         if nextprogramsX != 1080:
                                             pos_Y = self.getControl(int(nextprograms)).getY()
                                             self.getControl(int(nextprograms)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprograms)).setVisible(True)



                             elif int(pos_X) == 375 and int(prog_width) == 1038:
                                 programs_width = 691
                                 self.getControl(int(program_id)).setWidth(int(programs_width))
                                 program_width = self.getControl(int(program_id)).getWidth()
                                 program_id = int(program_id)
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 nextprogram_width = self.getControl(int(nextprogram)).getWidth()
                                 nextprograms = int(nextprogram) + 1
                                 nextprogramsX = self.getControl(int(nextprograms)).getX()
                                 nextprograms_width = self.getControl(int(nextprograms)).getWidth()
                                 self.select_db_flag = True
                                 self.program_stop_minutes,self.program_stop_time = get_programming_times(self)

                                 if self.program_stop_time < self.epg_time_3:
                                     if self.program_stop_minutes == '55':
                                         if int(prog_width) == 1038:
                                             programs_width = 626
                                             self.getControl(int(program_id)).setWidth(int(programs_width))
                                             pos_Y = self.getControl(int(program_id)).getY()

                                             if nextprogram_width == 117:
                                                 if nextprogramX != 1008:
                                                     pos_Y = self.getControl(int(nextprogram)).getY()
                                                     self.getControl(int(nextprogram)).setPosition(1008, int(pos_Y))
                                                     self.getControl(int(nextprogram)).setVisible(True)

                                                     if nextprogramsX != 1132:
                                                         pos_Y = self.getControl(int(nextprograms)).getY()
                                                         self.getControl(int(nextprograms)).setPosition(1132, int(pos_Y))
                                                         self.getControl(int(nextprograms)).setVisible(True)


                                 elif self.program_stop_time >= self.epg_time_3:
                                     if self.program_stop_minutes == '05':
                                         if int(prog_width) == 1038:
                                             programs_width = 750
                                             self.getControl(int(program_id)).setWidth(int(programs_width))

                                             if nextprogramX != 1132:
                                                 pos_Y = self.getControl(int(nextprogram)).getY()
                                                 self.getControl(int(nextprogram)).setPosition(1132, int(pos_Y))
                                                 self.getControl(int(nextprogram)).setVisible(True)



                                 elif self.program_stop_time == self.epg_time_3:
                                     if self.program_stop_minutes == '00':
                                         if int(prog_width) == 1038:
                                             programs_width = 691
                                             self.getControl(int(program_id)).setWidth(int(programs_width))

                                             if nextprogramX != 1073:
                                                 pos_Y = self.getControl(int(nextprogram)).getY()
                                                 self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                                 self.getControl(int(nextprogram)).setVisible(True)




                             elif int(pos_X) == 375 and int(prog_width) == 1026:
                                 programs_width = 691
                                 self.getControl(int(program_id)).setWidth(int(programs_width))
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 nextprogram_Width = self.getControl(int(nextprogram)).getWidth()
                                 pos_Y = self.getControl(int(nextprogram)).getY()

                                 if nextprogramX != 375:
                                     pos_Y = self.getControl(int(nextprogram)).getY()
                                     self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))
                                     nextprograms = int(nextprogram) + 1
                                     nextprogramsX = self.getControl(int(nextprograms)).getX()
                                     self.getControl(int(program_id)).setWidth(int(programs_width))
                                     program_id = int(program_id) + 1
                                     self.select_db_flag = True
                                     self.program_stop_minutes,self.program_stop_time = get_programming_times(self)
                                     print "self.program_stop_minutes"
                                     print self.program_stop_minutes

                                     if self.program_stop_time > self.epg_time_3:
                                         if self.program_stop_minutes == '10':
                                             if int(prog_width) == 1026:
                                                 programs_width = 806
                                                 self.getControl(int(nextprogram)).setWidth(int(programs_width))
                                                 #pos_Y = self.getControl(int(nextprograms)).getY()
                                                 #self.getControl(int(nextprograms)).setPosition(838, int(pos_Y))
                                                 #self.getControl(int(nextprograms)).setVisible(True)
                                                 #nextprograms1 = int(nextprograms) + 1
                                                 #nextprogramsWidth1 = self.getControl(int(nextprograms)).getWidth()
                                                 #pos_Y = self.getControl(int(nextprograms1)).getY()

                                                 #if nextprogramsWidth1 == 344:
                                                     #pos_Y = self.getControl(int(nextprograms1)).getY()
                                                     #self.getControl(int(nextprograms1)).setPosition(1189, int(pos_Y))
                                                     #.getControl(int(nextprograms1)).setVisible(True)



                                     if self.program_stop_time < self.epg_time_3:
                                         if self.program_stop_minutes == '10':
                                             if nextprogram_Width == 691:
                                                 programs_width = 456
                                                 self.getControl(int(nextprogram)).setWidth(int(programs_width))
                                                 pos_Y = self.getControl(int(nextprograms)).getY()
                                                 self.getControl(int(nextprograms)).setPosition(838, int(pos_Y))
                                                 self.getControl(int(nextprograms)).setVisible(True)
                                                 nextprograms1 = int(nextprograms) + 1
                                                 nextprogramsWidth1 = self.getControl(int(nextprograms)).getWidth()
                                                 pos_Y = self.getControl(int(nextprograms1)).getY()

                                                 if nextprogramsWidth1 == 344:
                                                     pos_Y = self.getControl(int(nextprograms1)).getY()
                                                     self.getControl(int(nextprograms1)).setPosition(1189, int(pos_Y))
                                                     self.getControl(int(nextprograms1)).setVisible(True)


                                         elif self.program_stop_minutes == '40':
                                             if nextprogram_Width == 691:
                                                 programs_width = 456
                                                 self.getControl(int(nextprogram)).setWidth(int(programs_width))
                                                 pos_Y = self.getControl(int(nextprograms)).getY()
                                                 self.getControl(int(nextprograms)).setPosition(838, int(pos_Y))
                                                 self.getControl(int(nextprograms)).setVisible(True)
                                                 nextprograms1 = int(nextprograms) + 1
                                                 nextprogramsWidth1 = self.getControl(int(nextprograms)).getWidth()

                                                 if nextprogramsWidth1 == 344:
                                                     pos_Y = self.getControl(int(nextprogram1)).getY()
                                                     self.getControl(int(nextprograms1)).setPosition(1189, int(pos_Y))
                                                     self.getControl(int(nextprograms1)).setVisible(True)


                                     if nextprogramX != 1073:
                                         pos_Y = self.getControl(int(nextprogram)).getY()
                                         self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                         self.getControl(int(nextprogram)).setVisible(True)



                             elif int(pos_X) == 375 and int(prog_width) == 969:
                                 programs_width = 626
                                 self.getControl(int(program_id)).setWidth(int(programs_width))

                                 if programs_width == 626:
                                     self.getControl(int(nextprogram)).setPosition(1009, int(pos_Y))
                                     self.programs_Index_flag = True
                                     self.previous_program = True



                             elif int(pos_X) == 375 and int(prog_width) == 879:
                                 programs_width = 516
                                 self.getControl(int(program_id)).setWidth(int(programs_width))
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 nextprogramWidth = self.getControl(int(nextprogram)).getWidth()
                                 pos_Y = self.getControl(int(nextprogram)).getY()

                                 if nextprogramX != 897:
                                     pos_Y = self.getControl(int(nextprogram)).getY()
                                     self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))
                                     self.getControl(int(nextprogram)).setVisible(True)



                             elif int(pos_X) == 375 and int(prog_width) == 804:
                                 programs_width = 456
                                 self.getControl(int(program_id)).setWidth(int(programs_width))
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 nextprogram_width = self.getControl(int(nextprogram)).getWidth()

                                 if programs_width == 456:
                                     if nextprogramX != 838:
                                         pos_Y = self.getControl(int(nextprogram)).getY()
                                         self.getControl(int(nextprogram)).setPosition(838, int(pos_Y))
                                         self.getControl(int(nextprogram)).setVisible(True)



                             elif int(pos_X) == 375 and int(prog_width) >= 741 and int(prog_width) <= 750:
                                 programs_width = 399
                                 self.getControl(int(program_id)).setWidth(int(programs_width))
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 nextprogramWidth = self.getControl(int(nextprogram)).getWidth()
                                 pos_Y = self.getControl(int(nextprogram)).getY()

                                 if nextprogramX != 780:
                                     pos_Y = self.getControl(int(nextprogram)).getY()
                                     self.getControl(int(nextprogram)).setPosition(780, int(pos_Y))
                                     self.getControl(int(nextprogram)).setVisible(True)




                             elif int(pos_X) == 375 and int(prog_width) == 691:
                                 programs_width = 344
                                 self.getControl(int(program_id)).setWidth(int(programs_width))

                                 if programs_width == 344:
                                     self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))

                                     if nextprogram_width == 344:
                                         nextprogram_width = 343
                                         self.getControl(int(nextprogram)).setWidth(int(nextprogram_width))
                                         self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))


                                 #pos_Y = self.getControl(int(program_id)).getY()
                                 #self.getControl(int(program_id)).setPosition(375, int(pos_Y))
                                 #nextprogram = int(program_id) + 1
                                 #nextprogram_width = self.getControl(int(nextprogram)).getWidth()
                                 #nextprogramX = self.getControl(int(nextprogram)).getX()
                                 #pos_Y = self.getControl(int(nextprogram)).getY()

                                 #if nextprogramX == 1073:
                                     #pos_Y = self.getControl(int(nextprogram)).getY()
                                     #self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))

                                     #if nextprogram_width == 344:
                                         #nextprograms = int(nextprogram) + 1
                                         #pos_Y = self.getControl(int(nextprograms)).getY()
                                         #self.getControl(int(nextprograms)).setPosition(1073, int(pos_Y))
                                         #self.getControl(int(nextprograms)).setVisible(True)

                                     #if nextprogram_width == 167:
                                         #pos_Y = self.getControl(int(nextprogram)).getY()
                                         #self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))


                                     #elif nextprogram_width <= 567:
                                         #pos_Y = self.getControl(int(nextprogram)).getY()
                                         #self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))
                                         #self.getControl(int(nextprogram)).setVisible(True)


                                     #elif nextprogram_width == 691:
                                         #pos_Y = self.getControl(int(nextprogram)).getY()
                                         #self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                         #self.getControl(int(nextprogram)).setVisible(True)



                             elif int(pos_X) == 375 and int(prog_width) == 626:
                                 programs_width = 276
                                 self.getControl(int(program_id)).setWidth(int(programs_width))
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 nextprogramWidth = self.getControl(int(nextprogram)).getWidth()
                                 pos_Y = self.getControl(int(nextprogram)).getY()

                                 if nextprogramX > 724:
                                     nextprograms = int(nextprogram) + 1
                                     nextprogramsX = self.getControl(int(nextprograms)).getX()
                                     nextprogramsWidth = self.getControl(int(nextprograms)).getWidth()
                                     pos_Y = self.getControl(int(nextprogram)).getY()
                                     self.getControl(int(nextprogram)).setPosition(657, int(pos_Y))

                                     if nextprogramWidth == 59:
                                         pos_Y = self.getControl(int(nextprograms)).getY()
                                         self.getControl(int(nextprograms)).setPosition(737, int(pos_Y))
                                     elif nextprogramWidth == 117:
                                         pos_Y = self.getControl(int(nextprograms)).getY()
                                         self.getControl(int(nextprograms)).setPosition(780, int(pos_Y))


                                     #elif nextprogramX > 1032:
                                         #self.getControl(int(nextprogram)).setPosition(1032, int(pos_Y))



                             elif int(pos_X) == 375 and int(prog_width) == 577:
                                 programs_width = 235
                                 self.getControl(int(program_id)).setWidth(int(programs_width))
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 pos_Y = self.getControl(int(nextprogram)).getY()

                                 if nextprogramX > 724:
                                     posX = int(nextprogramX) - 344
                                     posY = self.getControl(int(nextprogram)).getY()
                                     self.getControl(int(nextprogram)).setPosition(posX, int(posY))
                                     nextprogram_width = self.getControl(int(nextprogram)).getWidth()

                                     if nextprogram_width == 515:
                                         nextprograms = int(nextprogram) + 1
                                         nextprogramsX = self.getControl(int(nextprograms)).getX()
                                         posX = int(nextprogramsX) - 344
                                         posY = self.getControl(int(nextprograms)).getY()
                                         self.getControl(int(nextprograms)).setPosition(posX, int(posY))
                                         self.getControl(int(nextprograms)).setVisible(True)



                             elif int(pos_X) == 375 and int(prog_width) == 567:
                                 print "fix this goright 1"
                                 programs_width = 232
                                 self.getControl(int(program_id)).setWidth(int(programs_width))
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 nextprogramwidth = self.getControl(int(nextprogram)).getWidth()

                                 if nextprogramX == 724:
                                     posY = self.getControl(int(nextprogram)).getY()
                                     self.getControl(int(nextprogram)).setPosition(1073, int(posY))
                                     self.getControl(int(nextprogram)).setVisible(True)


                                 elif nextprogramX == 949:
                                     posY = self.getControl(int(nextprogram)).getY()
                                     self.getControl(int(nextprogram)).setPosition(614, int(posY))
                                     self.getControl(int(nextprogram)).setVisible(True)
                                     nextprograms = int(nextprogram) + 1
                                     nextprogramsX = self.getControl(int(nextprograms)).getX()
                                     nextprograms_width = self.getControl(int(nextprograms)).getWidth()

                                     if nextprogramwidth == 567:
                                         if nextprogramsX != 1188:
                                             pos_Y = self.getControl(int(nextprograms)).getY()
                                             self.getControl(int(nextprograms)).setPosition(1188, int(posY))
                                             self.getControl(int(nextprograms)).setVisible(True)


                                     elif nextprogramwidth == 286:
                                         if nextprogramsX != 907:
                                             pos_Y = self.getControl(int(nextprograms)).getY()
                                             self.getControl(int(nextprograms)).setPosition(907, int(posY))
                                             self.getControl(int(nextprograms)).setVisible(True)
                                             nextprograms1 = int(nextprograms) + 1
                                             nextprogramsX1 = self.getControl(int(nextprograms1)).getX()
                                             program_id = int(nextprograms) + 1
                                             self.select_db_flag = True
                                             self.program_stop_minutes,self.program_stop_time = get_programming_times(self)
                                             print "self.program_stop_minutes"
                                             print self.program_stop_minutes

                                             if self.program_stop_time > self.epg_time_3:
                                                 print "passed 1"
                                                 if self.program_stop_minutes == '10':
                                                     print "passed 2"
                                                     if nextprograms_width == 227:
                                                         print "passed 3"
                                                         programs_width = 286
                                                         self.getControl(int(nextprograms)).setWidth(programs_width)

                                                         if nextprogramsX1 != 1142:
                                                             pos_Y = self.getControl(int(nextprograms1)).getY()
                                                             self.getControl(int(nextprograms1)).setPosition(1142, int(posY))
                                                             self.getControl(int(nextprograms1)).setVisible(True)




                             elif int(pos_X) == 375 and int(prog_width) >= 515 and int(prog_width) <= 517:
                                 programs_width = 167
                                 self.getControl(int(program_id)).setWidth(int(programs_width))


                                 if nextprogramX != 549:
                                     self.getControl(int(nextprogram)).setPosition(549, int(pos_Y))

                                     if nextprogram_width == 344:
                                         self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))


                                     elif nextprogram_width == 567:
                                         self.getControl(int(nextprogram1)).setPosition(1122, int(pos_Y))

                                         if CurrentRow == 549 and CurrentWidth >= 342:
                                             self.programs_Index_flag = True
                                             self.previous_program = True
                                             print "you are in the CurrentRow"





                             elif int(pos_X) == 375 and int(prog_width) == 456:
                                 programs_width = 117
                                 self.getControl(int(program_id)).setWidth(int(programs_width))
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 nextprogram_width = self.getControl(int(nextprogram)).getWidth()

                                 if nextprogramX != 499:
                                     pos_Y = self.getControl(int(nextprogram)).getY()
                                     self.getControl(int(nextprogram)).setPosition(499, int(pos_Y))

                                     if nextprogram_width == 344:
                                         nextprograms = int(nextprogram) + 1
                                         pos_Y = self.getControl(int(nextprograms)).getY()
                                         self.getControl(int(nextprograms)).setPosition(848, int(pos_Y))
                                         self.getControl(int(nextprograms)).setVisible(True)


                                     elif nextprogram_width == 567:
                                         nextprograms = int(nextprogram) + 1
                                         pos_Y = self.getControl(int(nextprograms)).getY()
                                         self.getControl(int(nextprograms)).setPosition(1073, int(pos_Y))
                                         self.getControl(int(nextprograms)).setVisible(True)



                             elif int(pos_X) == 375 and int(prog_width) == 399:
                                 programs_width = 59
                                 self.getControl(int(program_id)).setWidth(int(programs_width))
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 nextprogram_width = self.getControl(int(nextprogram)).getWidth()

                                 if nextprogramX != 440:
                                     programs_width = self.getControl(int(program_id)).getWidth()

                                     if programs_width == 59:
                                         if nextprogram_width == 691:
                                             programs_width = 672
                                             self.getControl(int(nextprogram)).setWidth(int(programs_width))


                                     pos_Y = self.getControl(int(nextprogram)).getY()
                                     self.getControl(int(nextprogram)).setPosition(440, int(pos_Y))
                                     nextprogram_width = self.getControl(int(nextprogram)).getWidth()
                                     nextprogramsX = self.getControl(int(nextprogram)).getX()
                                     pos_Y = self.getControl(int(nextprograms)).getY()

                                     if nextprogram_width == 691:
                                         if nextprogramsX != 1116:
                                             nextprograms = int(nextprogram) + 1
                                             pos_Y = self.getControl(int(nextprograms)).getY()
                                             self.getControl(int(nextprograms)).setPosition(1138, int(pos_Y))
                                             self.getControl(int(nextprograms)).setVisible(True)



                             elif int(pos_X) == 375 and int(prog_width) == 344:
                                 self.getControl(int(program_id)).setLabel(nextprogram_label)
                                 self.getControl(int(program_id)).setWidth(nextprogram_width)
                                 print nextprogram_width


                                 if nextprogram_width == 691:
                                     self.getControl(int(nextprogram)).setLabel(nextprogram_label)
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)



                                 #if nextprogramX != 375:
                                     #pos_Y = self.getControl(int(nextprogram)).getY()
                                     #self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))
                                     #nextprograms = int(nextprogram) + 1
                                     #nextprogramsX = self.getControl(int(nextprograms)).getX()
                                     #nextprograms_width = self.getControl(int(nextprograms)).getWidth()
                                     #nextprograms1 = int(nextprograms) + 1
                                     #nextprogramsX1 = self.getControl(int(nextprograms1)).getX()
                                     #nextprograms_width1 = self.getControl(int(nextprograms1)).getWidth()

                                     #if nextprogram_width == 286:
                                         #if nextprogramsX != 665:
                                             #pos_Y = self.getControl(int(nextprograms)).getY()
                                             #self.getControl(int(nextprograms)).setPosition(668, int(pos_Y))

                                             #if nextprograms_width == 227:
                                                 #if nextprogramsX1 != 901:
                                                     #pos_Y = self.getControl(int(nextprograms1)).getY()
                                                     #self.getControl(int(nextprograms1)).setPosition(901, int(pos_Y))
                                                     #self.getControl(int(nextprograms1)).setVisible(True)


                                     #elif nextprogram_width == 344:
                                         #if nextprogramsX != 724:
                                             #pos_Y = self.getControl(int(nextprograms)).getY()
                                             #self.getControl(int(nextprograms)).setPosition(724, int(pos_Y))

                                             #if nextprograms_width == 344:
                                                 #if nextprogramsX1 != 1073:
                                                     #pos_Y = self.getControl(int(nextprograms1)).getY()
                                                     #self.getControl(int(nextprograms1)).setPosition(1073, int(pos_Y))
                                                     #self.getControl(int(nextprograms1)).setVisible(True)



                                     #elif nextprogram_width == 515:
                                         #pos_Y = self.getControl(int(nextprograms)).getY()
                                         #self.getControl(int(nextprograms)).setPosition(897, int(pos_Y))
                                         #self.getControl(int(nextprograms)).setVisible(True)



                                     #elif nextprogram_width == 567:
                                         #if nextprogramsX != 949:
                                             #pos_Y = self.getControl(int(nextprograms)).getY()
                                             #self.getControl(int(nextprograms)).setPosition(949, int(pos_Y))
                                             #self.getControl(int(nextprograms)).setVisible(True)


                                     #elif nextprogram_width == 626:
                                         #if nextprogramsX != 949:
                                             #pos_Y = self.getControl(int(nextprograms)).getY()
                                             #self.getControl(int(nextprograms)).setPosition(1008, int(pos_Y))
                                             #self.getControl(int(nextprograms)).setVisible(True)



                                     #elif nextprogram_width == 691:
                                         #if nextprogramsX != 1073:
                                             #pos_Y = self.getControl(int(nextprograms)).getY()
                                             #self.getControl(int(nextprograms)).setPosition(1073, int(pos_Y))
                                             #self.getControl(int(nextprograms)).setVisible(True)


                                     #elif nextprogram_width == 741:
                                         #if nextprogramsX != 1124:
                                             #pos_Y = self.getControl(int(nextprograms)).getY()
                                             #self.getControl(int(nextprograms)).setPosition(1124, int(pos_Y))
                                             #self.getControl(int(nextprograms)).setVisible(True)




                             elif int(pos_X) == 375 and int(prog_width) == 286:
                                 self.getControl(int(program_id)).setVisible(False)
                                 self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 nextprogram_Width = self.getControl(int(nextprogram)).getWidth()
                                 pos_Y = self.getControl(int(nextprogram)).getY()

                                 if nextprogramX != 375:
                                     pos_Y = self.getControl(int(nextprogram)).getY()
                                     self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))
                                     program_id = int(program_id) + 1
                                     nextprograms = int(nextprogram) + 1
                                     nextprogramsX = self.getControl(int(nextprograms)).getX()
                                     program_id = int(program_id)
                                     self.select_db_flag = True
                                     self.program_stop_minutes,self.program_stop_time = get_programming_times(self)

                                     if self.program_stop_time < self.epg_time_3:
                                         if self.program_stop_minutes == '40':
                                             if nextprogram_Width == 567:
                                                 programs_width = 456
                                                 self.getControl(int(nextprogram)).setWidth(int(programs_width))
                                                 pos_Y = self.getControl(int(nextprograms)).getY()
                                                 self.getControl(int(nextprograms)).setPosition(838, int(pos_Y))
                                                 self.getControl(int(nextprograms)).setVisible(True)
                                                 nextprograms1 = int(nextprograms) + 1
                                                 nextprogramsWidth1 = self.getControl(int(nextprograms)).getWidth()

                                                 if nextprogramsWidth1 == 344:
                                                     pos_Y = self.getControl(int(nextprograms1)).getY()
                                                     self.getControl(int(nextprograms1)).setPosition(1189, int(pos_Y))
                                                     self.getControl(int(nextprograms1)).setVisible(True)

                                         else:
                                             if nextprogram_Width == 458:
                                                 if nextprogramsX != 949:
                                                     pos_Y = self.getControl(int(nextprograms)).getY()
                                                     pos_Y = self.getControl(int(nextprograms)).getY()
                                                     self.getControl(int(nextprograms)).setPosition(614, int(pos_Y))
                                                     self.getControl(int(nextprograms)).setVisible(True)


                                             elif nextprogram_Width == 626:
                                                 if nextprogramsX > 1008:
                                                     pos_Y = self.getControl(int(nextprograms)).getY()
                                                     
                                                     if int(pos_Y) == 315:
                                                         self.getControl(int(nextprograms)).setPosition(1008, 315)
                                                         self.getControl(int(nextprograms)).setVisible(True)
                                                     elif int(pos_Y) == 353:
                                                         print "catch this 4"
                                                         self.getControl(int(nextprograms)).setPosition(1008, 353)
                                                         self.getControl(int(nextprograms)).setVisible(True)
                                                     elif int(pos_Y) == 391:
                                                         self.getControl(int(nextprograms)).setPosition(1008, 391)
                                                         self.getControl(int(nextprograms)).setVisible(True)
                                                     elif int(pos_Y) == 428:
                                                         print "catch this troubleshoot 2"
                                                         self.getControl(int(nextprograms)).setPosition(1008, 428)
                                                         self.getControl(int(nextprograms)).setVisible(True)
                                                     elif int(pos_Y) == 466:
                                                         self.getControl(int(nextprograms)).setPosition(1008, 466)
                                                         self.getControl(int(nextprograms)).setVisible(True)
                                                     elif int(pos_Y) == 503:
                                                         self.getControl(int(nextprograms)).setPosition(1008, 503)
                                                         self.getControl(int(nextprograms)).setVisible(True)
                                                     elif int(pos_Y) == 541:
                                                         self.getControl(int(nextprograms)).setPosition(1008, 541)
                                                         self.getControl(int(nextprograms)).setVisible(True)



                                             elif nextprogram_Width == 567:
                                                 if nextprogramsX != 949:
                                                     pos_Y = self.getControl(int(nextprograms)).getY()
                                                     self.getControl(int(nextprograms)).setPosition(949, int(pos_Y))
                                                     self.getControl(int(nextprograms)).setVisible(True)




                             elif int(pos_X) == 375 and int(prog_width) >= 276 or int(prog_width) <= 278:
                                 self.getControl(int(program_id)).setLabel(nextprogram_label)
                                 self.getControl(int(program_id)).setWidth(nextprogram_width)
                                 self.getControl(int(nextprogram)).setLabel(nextprogram1_label)
                                 self.getControl(int(nextprogram)).setWidth(nextprogram1_width)
                                 program_width = self.getControl(int(program_id)).getWidth()

                                 print "prog_width"
                                 print prog_width

                                 if program_width == 572:
                                     program_width = 567
                                     self.getControl(int(program_id)).setWidth(program_width)
                                 
                                 
                                 
                                 programX = self.getControl(int(program_id)).getX()
                                 #nextprogram = int(program_id) + 1
                                 #nextprogramX = self.getControl(int(nextprogram)).getX()
                                 #nextprogram_width = self.getControl(int(nextprogram)).getWidth()
                                 #nextprograms = int(nextprogram) + 1
                                 #nextprogramsX = self.getControl(int(nextprograms)).getX()
                                 #nextprograms_width = self.getControl(int(nextprograms)).getWidth()
                                 #nextprograms1 = int(nextprograms) + 1
                                 #nextprograms1X = self.getControl(int(nextprograms1)).getX()
                                 #nextprograms1_width = self.getControl(int(nextprograms1)).getWidth()
                                 #pos_Y = self.getControl(int(nextprogram)).getY()


                                 #if nextprogramX == 440:
                                     #if nextprogram_width == 59:
                                         #self.getControl(int(program_id)).setVisible(False)
                                         #pos_Y = self.getControl(int(program_id)).getY()
                                         #self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))


                                 #if programX < 375:
                                     #if nextprogramX != 375:
                                         #self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))
                                         #nextprograms = int(nextprogram) + 1


                                         #if nextprogram_width == 59:
                                             #self.getControl(int(nextprogram)).setVisible(False)
                                             #self.getControl(int(nextprogram)).setPosition(int(pos_X) - 350, int(pos_Y))


                                         #elif nextprogram_width == 567:
                                             #program_id = int(nextprogram)
                                             #self.select_db_flag = True
                                             #self.program_stop_minutes,self.program_stop_time = get_programming_times(self)

                                             #if self.program_stop_time > self.epg_time_2:
                                                 #if self.program_stop_minutes == '40':
                                                     #if nextprogram_width == 567:
                                                         #programs_width = 456
                                                         #self.getControl(int(nextprogram)).setWidth(int(programs_width))

                                                         #if nextprogramX != 837:
                                                             #pos_Y = self.getControl(int(nextprograms)).getY()
                                                             #self.getControl(int(nextprograms)).setPosition(837, int(pos_Y))
                                                             #self.getControl(int(nextprograms)).setVisible(True)

                                                             #if nextprograms_width == 344:
                                                                 #if nextprogramsX != 1186:
                                                                     #self.getControl(int(nextprograms1)).setPosition(1186, int(pos_Y))
                                                                     #self.getControl(int(nextprograms1)).setVisible(True)



                                         #elif nextprogram_width == 626:
                                             #if nextprogramX != 1008:
                                                 #pos_Y = self.getControl(int(nextprograms)).getY()
                                                 #self.getControl(int(nextprograms)).setPosition(1008, int(pos_Y))
                                                 #self.getControl(int(nextprograms)).setVisible(True)


                                         #if nextprogram_width == 344:
                                             #nextprograms = int(nextprogram) + 1
                                             #self.getControl(int(nextprograms)).setPosition(724, int(pos_Y))
                                             #self.getControl(int(nextprograms)).setVisible(True)




                             elif int(pos_X) == 375 and int(prog_width) == 235:
                                 self.getControl(int(program_id)).setVisible(False)
                                 self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 nextprogram_width = self.getControl(int(nextprogram)).getWidth()
                                 pos_Y = self.getControl(int(nextprogram)).getY()


                                 if nextprogramX != 375:
                                     pos_Y = self.getControl(int(nextprogram)).getY()
                                     self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))
                                     nextprograms = int(nextprogram) + 1
                                     nextprogramsWidth = self.getControl(int(nextprograms)).getWidth()
                                     nextprogramsX = self.getControl(int(nextprograms)).getX()

                                     if nextprogram_width == 515:
                                         program_id = int(program_id) + 1
                                         self.select_db_flag = True
                                         self.program_stop_minutes,self.program_stop_time = get_programming_times(self)


                                         if self.program_stop_time > self.epg_time_2:
                                             if self.program_stop_minutes == '05':
                                                 if nextprogram_width == 515:
                                                     programs_width = 399
                                                     self.getControl(int(program_id)).setWidth(programs_width)

                                                     if nextprogramsX == 1138:
                                                         pos_Y = self.getControl(int(nextprograms)).getY()
                                                         self.getControl(int(nextprograms)).setPosition(764, int(pos_Y))




                             elif int(pos_X) == 375 and int(prog_width) == 232:
                                 self.getControl(int(program_id)).setVisible(False)
                                 self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 nextprogramWidth = self.getControl(int(nextprogram)).getWidth()

                                 if nextprogramX != 375:
                                     pos_Y = self.getControl(int(nextprogram)).getY()
                                     self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))
                                     nextprograms = int(nextprogram) + 1
                                     nextprogramsX = self.getControl(int(nextprograms)).getX()
                                     nextprogramsWidth = self.getControl(int(nextprograms)).getWidth()

                                     if nextprogramsX == 1073:
                                         print "fix this 1"
                                         #self.getControl(int(nextprograms)).setPosition(724, int(pos_Y))


                                     elif nextprogramsX == 1291:
                                         print "fix this 2"
                                         #self.getControl(int(nextprograms)).setPosition(949, int(pos_Y))


                                     elif nextprogramsX == 1188 or nextprogramsX == 1189:
                                         if nextprogramWidth == 567:
                                             pos_Y = self.getControl(int(nextprograms)).getY()
                                             self.getControl(int(nextprograms)).setPosition(949, int(pos_Y))


                                     elif nextprogramsX == 963:
                                         if nextprogramWidth == 344:
                                             pos_Y = self.getControl(int(nextprograms)).getY()
                                             self.getControl(int(nextprograms)).setPosition(724, int(pos_Y))



                             elif int(pos_X) == 375 and int(prog_width) == 167:
                                 pass
                                 #ass1a

                                #self.getControl(int(program_id)).setVisible(False)
                                 #self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                                 #nextprogram = int(program_id) + 1
                                 #nextprogramX = self.getControl(int(nextprogram)).getX()
                                 #nextprogramWidth = self.getControl(int(nextprogram)).getWidth()

                                 #if nextprogramX != 375:
                                     #if nextprogramX == 549:
                                         #if nextprogramWidth == 344:
                                             #program_width = 167
                                             #self.getControl(int(nextprogram)).setWidth(program_width)
                                             #pos_Y = self.getControl(int(nextprogram)).getY()
                                             #self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))
                                             #nextprograms = int(nextprogram) + 1
                                             #nextprogramsX = self.getControl(int(nextprograms)).getX()
                                             #nextprogramsWidth = self.getControl(int(nextprograms)).getWidth()

                                             #if nextprogramX != 897:
                                                 #pos_Y = self.getControl(int(nextprograms)).getY()
                                                 #self.getControl(int(nextprograms)).setPosition(549, int(pos_Y))
                                                 #self.getControl(int(nextprograms)).setVisible(True)

                                                 #if nextprogramsWidth == 396:
                                                     #nextprograms1 = int(nextprograms) + 1
                                                     #pos_Y = self.getControl(int(nextprograms1)).getY()
                                                     #self.getControl(int(nextprograms1)).setPosition(952, int(pos_Y))
                                                     #self.getControl(int(nextprograms1)).setVisible(True)



                                         #elif nextprogramWidth == 691:
                                             #program_width = 515
                                             #self.getControl(int(nextprogram)).setWidth(program_width)
                                             #pos_Y = self.getControl(int(nextprogram)).getY()
                                             #self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))
                                             #nextprograms = int(nextprogram) + 1
                                             #nextprogramsX = self.getControl(int(nextprograms)).getX()

                                             #if nextprogramsX != 897:
                                                 #pos_Y = self.getControl(int(nextprograms)).getY()
                                                 #self.getControl(int(nextprograms)).setPosition(897, int(pos_Y))
                                                 #self.getControl(int(nextprograms)).setVisible(True)



                                         #elif nextprogramWidth > 691:
                                             #pos_Y = self.getControl(int(nextprogram)).getY()

                                             #if int(pos_Y) == 353:
                                                 #self.getControl(int(nextprogram)).setPosition(375, 353)

                                             #self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))
                                             #self.getControl(int(nextprogram)).setVisible(True)



                             elif int(pos_X) == 375 and int(prog_width) == 117:
                                 self.getControl(int(program_id)).setVisible(False)
                                 self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 nextprogram_width = self.getControl(int(nextprogram)).getWidth()
                                 pos_Y = self.getControl(int(nextprogram)).getY()

                                 if nextprogramX != 375:
                                     pos_Y = self.getControl(int(nextprogram)).getY()
                                     self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))

                                     if nextprogram_width == 344:
                                         program_width = 117
                                         self.getControl(int(nextprogram)).setWidth(int(program_width))
                                         nextprograms = int(nextprogram) + 1
                                         nextprogramsX = self.getControl(int(nextprograms)).getX()
                                         nextprogramsWidth = self.getControl(int(nextprograms)).getWidth()

                                         if nextprogramsX != 499:
                                             pos_Y = self.getControl(int(nextprograms)).getY()
                                             self.getControl(int(nextprograms)).setPosition(499, int(pos_Y))


                                     elif nextprogram_width >= 691:
                                         program_width = int(nextprogram_width) - 114
                                         self.getControl(int(nextprogram)).setWidth(int(program_width))




                             elif int(pos_X) == 375 and int(prog_width) == 59:
                                 self.getControl(int(program_id)).setVisible(False)
                                 self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 nextprogramWidth = self.getControl(int(nextprogram)).getWidth()
                                 pos_Y = self.getControl(int(nextprogram)).getY()

                                 if nextprogramX != 375:
                                     if nextprogramWidth == 286:
                                         self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                                         self.getControl(int(nextprogram)).setVisible(False)
                                         self.getControl(int(nextprogram)).setPosition(int(pos_X) - 350, int(pos_Y))
                                         nextprograms = int(nextprogram) + 1
                                         nextprogramsX = self.getControl(int(nextprograms)).getX()
                                         nextprogramsWidth = self.getControl(int(nextprograms)).getWidth()


                                         if nextprogramsX != 375:
                                             if nextprogramsWidth >= 59:
                                                 pos_Y = self.getControl(int(nextprograms)).getY()
                                                 self.getControl(int(nextprograms)).setPosition(375, int(pos_Y))



                                     elif nextprogramWidth > 691:
                                         pos_Y = self.getControl(int(nextprogram)).getY()
                                         self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))



                                     elif nextprogramWidth == 691:
                                         self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))
                                         nextprograms = int(nextprogram) + 1
                                         nextprogramsX = self.getControl(int(nextprograms)).getX()
                                         nextprogramsWidth = self.getControl(int(nextprograms)).getWidth()

                                         if nextprogramsX != 1073:
                                             pos_Y = self.getControl(int(nextprograms)).getY()
                                             self.getControl(int(nextprograms)).setPosition(1073, int(pos_Y))


                                     elif nextprogramWidth == 676:
                                         programs_width = 399
                                         self.getControl(int(nextprogram)).setWidth(int(programs_width))
                                         self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))
                                         nextprograms = int(nextprogram) + 1
                                         nextprogramsX = self.getControl(int(nextprograms)).getX()
                                         nextprogramsWidth = self.getControl(int(nextprograms)).getWidth()

                                         if nextprogramsX != 778:
                                             if nextprogramsWidth == 286:
                                                 pos_Y = self.getControl(int(nextprograms)).getY()
                                                 self.getControl(int(nextprograms)).setPosition(780, int(pos_Y))
                                                 nextprograms1 = int(nextprograms) + 1
                                                 nextprograms1X = self.getControl(int(nextprograms1)).getX()
                                                 nextprograms1Width = self.getControl(int(nextprograms1)).getWidth()

                                                 if nextprograms1X != 1124:
                                                     pos_Y = self.getControl(int(nextprograms1)).getY()
                                                     self.getControl(int(nextprograms1)).setPosition(1073, int(pos_Y))
                                                     self.getControl(int(nextprograms1)).setVisible(True)


                                             elif nextprogramsWidth == 344:
                                                 pos_Y = self.getControl(int(nextprograms)).getY()
                                                 self.getControl(int(nextprograms)).setPosition(780, int(pos_Y))
                                                 nextprograms1 = int(nextprograms) + 1
                                                 nextprograms1X = self.getControl(int(nextprograms1)).getX()
                                                 nextprograms1Width = self.getControl(int(nextprograms1)).getWidth()

                                                 if nextprograms1X != 1124:
                                                     pos_Y = self.getControl(int(nextprograms1)).getY()
                                                     self.getControl(int(nextprograms1)).setPosition(1124, int(pos_Y))
                                                     self.getControl(int(nextprograms1)).setVisible(True)


                                     elif nextprogramWidth == 626:
                                         programs_width = 286
                                         self.getControl(int(nextprogram)).setWidth(int(programs_width))
                                         self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))
                                         nextprograms = int(nextprogram) + 1
                                         nextprogramsX = self.getControl(int(nextprograms)).getX()
                                         nextprogramsWidth = self.getControl(int(nextprograms)).getWidth()

                                         if nextprogramsX != 669:
                                             pos_Y = self.getControl(int(nextprograms)).getY()
                                             self.getControl(int(nextprograms)).setPosition(669, int(pos_Y))



                             elif int(pos_X) == 440 and int(prog_width) >= 59:
                                 program_width = self.getControl(int(program_id)).getWidth()
                                 program_id = int(program_id)
                                 self.select_db_flag = True
                                 self.program_stop_minutes,self.program_stop_time = get_programming_times(self)


                                 if self.program_stop_time == self.epg_time_1:
                                     if self.program_stop_minutes == '30':
                                         if program_width == 286:
                                             self.getControl(int(program_id)).setVisible(False)
                                             self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                                             nextprogram = int(program_id) + 1
                                             pos_Y = self.getControl(int(nextprogram)).getY()
                                             self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))


                                 elif self.program_stop_time <= self.epg_time_2:
                                     if program_stop_minutes == '40':
                                         if program_width == 567:
                                             self.getControl(int(program_id)).setPosition(375, int(pos_Y))
                                             program_width = 232
                                             self.getControl(int(program_id)).setWidth(program_width)
                                             nextprogram = int(program_id) + 1
                                             pos_Y = self.getControl(int(nextprogram)).getY()
                                             self.getControl(int(nextprogram)).setPosition(607, int(pos_Y))




                             elif int(pos_X) == 499 and int(prog_width) >= 59:
                                 self.getControl(int(program_id)).setPosition(375, int(pos_Y))
                                 program_width = self.getControl(int(program_id)).getWidth()
                                 program_id = int(program_id)
                                 self.select_db_flag = True
                                 self.program_stop_minutes,self.program_stop_time = get_programming_times(self)


                                 if self.program_stop_time == self.epg_time_2:
                                     if self.program_stop_minutes == '00':
                                         if program_width == 567:
                                             program_width = 344
                                             self.getControl(int(program_id)).setWidth(program_width)
                                             nextprogram = int(program_id) + 1
                                             nextprogramWidth = self.getControl(int(nextprogram)).getWidth()
                                             pos_Y = self.getControl(int(nextprogram)).getY()
                                             self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))
                                             nextprograms = int(nextprogram) + 1
                                             nextprogramsWidth = self.getControl(int(nextprograms)).getWidth()

                                             if nextprogramWidth == 286:
                                                 pos_Y = self.getControl(int(nextprograms)).getY()
                                                 self.getControl(int(nextprograms)).setPosition(1016, int(pos_Y))
                                                 self.getControl(int(nextprograms)).setVisible(True)




                             elif int(pos_X) == 549 and int(prog_width) <= 452:
                                 self.getControl(int(program_id)).setPosition(375, int(pos_Y))
                                 program_width = self.getControl(int(program_id)).getWidth()
                                 program_id = int(program_id)
                                 self.select_db_flag = True
                                 self.program_stop_minutes,self.program_stop_time = get_programming_times(self)


                                 if self.program_stop_time < self.epg_time_2:
                                     if self.program_stop_minutes == '15':
                                         if program_width == 344:
                                             prog_width = 167
                                             self.getControl(int(program_id)).setWidth(prog_width)
                                             nextprogram = int(program_id) + 1
                                             nextprogramX = self.getControl(int(nextprogram)).getX()
                                             nextprogram_Width = self.getControl(int(nextprogram)).getWidth()
                                             pos_Y = self.getControl(int(nextprogram)).getY()

                                             if nextprogramX != 549:
                                                 if nextprogram_Width == 396:
                                                     prog_width = 452
                                                     self.getControl(int(nextprogram)).setWidth(prog_width)
                                                     nextprogramY = self.getControl(int(nextprogram)).getY()
                                                     pos_Y = self.getControl(int(nextprogram)).getY()
                                                     self.getControl(int(nextprogram)).setPosition(549, int(nextprogramY))
                                                     self.getControl(int(nextprogram)).setVisible(True)
                                                     nextprograms = int(nextprogram) + 1
                                                     nextprogramX = self.getControl(int(nextprograms)).getX()

                                                     if nextprogramX != 897:
                                                         pos_Y = self.getControl(int(nextprograms)).getY()

                                                         if int(pos_Y) == 315:
                                                             self.getControl(int(nextprograms)).setPosition(1008, 315)
                                                             self.getControl(int(nextprograms)).setVisible(True)
                                                         elif int(pos_Y) == 353:
                                                             print "catch this 6"
                                                             self.getControl(int(nextprograms)).setPosition(1008, 353)
                                                             self.getControl(int(nextprograms)).setVisible(True)
                                                         elif int(pos_Y) == 391:
                                                             self.getControl(int(nextprograms)).setPosition(1008, 391)
                                                             self.getControl(int(nextprograms)).setVisible(True)
                                                         elif int(pos_Y) == 428:
                                                             print "catch this troubleshoot 4"
                                                             self.getControl(int(nextprograms)).setPosition(1008, 428)
                                                             self.getControl(int(nextprograms)).setVisible(True)
                                                         elif int(pos_Y) == 466:
                                                             self.getControl(int(nextprograms)).setPosition(1008, 466)
                                                             self.getControl(int(nextprograms)).setVisible(True)
                                                         elif int(pos_Y) == 503:
                                                             self.getControl(int(nextprograms)).setPosition(1008, 503)
                                                             self.getControl(int(nextprograms)).setVisible(True)
                                                         elif int(pos_Y) == 541:
                                                             self.getControl(int(nextprograms)).setPosition(1008, 541)
                                                             self.getControl(int(nextprograms)).setVisible(True)


                                 elif self.program_stop_time > self.epg_time_1:
                                     if self.program_stop_minutes == '45':
                                         if program_width == 344:
                                             prog_width = 167
                                             self.getControl(int(program_id)).setWidth(prog_width)
                                             nextprogram = int(program_id) + 1
                                             nextprogramX = self.getControl(int(nextprogram)).getX()
                                             pos_Y = self.getControl(int(nextprogram)).getY()

                                             if nextprogramX != 549:
                                                 pos_Y = self.getControl(int(nextprogram)).getY()
                                                 self.getControl(int(nextprogram)).setPosition(549, int(nextprogramY))
                                                 self.getControl(int(nextprogram)).setVisible(True)


                                     elif self.program_stop_minutes == '50':
                                         if program_width == 396:
                                             prog_width = 232
                                             self.getControl(int(program_id)).setWidth(prog_width)
                                             nextprogram = int(program_id) + 1
                                             nextprogramX = self.getControl(int(nextprogram)).getX()
                                             pos_Y = self.getControl(int(nextprogram)).getY()

                                             if nextprogramX != 614:
                                                 pos_Y = self.getControl(int(nextprogram)).getY()
                                                 self.getControl(int(nextprogram)).setPosition(614, int(pos_Y))
                                                 self.getControl(int(nextprogram)).setVisible(True)


                                         elif program_width == 452:
                                             prog_width = 232
                                             self.getControl(int(program_id)).setWidth(prog_width)
                                             nextprogram = int(program_id) + 1
                                             nextprogramX = self.getControl(int(nextprogram)).getX()
                                             pos_Y = self.getControl(int(nextprogram)).getY()

                                             if nextprogramX != 614:
                                                 pos_Y = self.getControl(int(nextprogram)).getY()
                                                 self.getControl(int(nextprogram)).setPosition(614, int(pos_Y))
                                                 self.getControl(int(nextprogram)).setVisible(True)




                             #elif int(pos_X) == 549 and int(prog_width) >= 691:
                                 #self.getControl(int(program_id)).setPosition(375, int(pos_Y))
                                 #program_id = int(program_id)
                                 #self.select_db_flag = True
                                 #self.program_stop_minutes,self.program_stop_time = get_programming_times(self)

                                 #if self.program_stop_time < self.epg_time_2:
                                     #if self.program_stop_minutes == '45':
                                         #prog_width = 167
                                         #self.getControl(int(program_id)).setWidth(prog_width)
                                         #nextprogram = int(program_id) + 1
                                         #nextprogramX = self.getControl(int(nextprogram)).getX()

                                         #if nextprogramX != 549:
                                             #nextprogramY = self.getControl(int(nextprogram)).getY()
                                             #self.getControl(int(nextprogram)).setPosition(549, int(nextprogramY))
                                             #self.getControl(int(nextprogram)).setVisible(True)



                                 #elif self.program_stop_time < self.epg_time_3:
                                     #if self.program_stop_minutes == '45':
                                         #prog_width = 515
                                         #self.getControl(int(program_id)).setWidth(prog_width)
                                         #nextprogram = int(program_id) + 1
                                         #nextprogramX = self.getControl(int(nextprogram)).getX()

                                         #if nextprogramX == 1073:
                                             #pos_Y = self.getControl(int(nextprogram)).getY()
                                             #self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))
                                             #self.getControl(int(nextprogram)).setVisible(True)



                                 #elif self.program_stop_time == self.epg_time_2:
                                     #if self.program_stop_minutes == '45':
                                         #if program_width == 691:
                                             #program_width = 515
                                             #self.getControl(int(program_id)).setWidth(program_width)




                             elif int(pos_X) == 616 and int(prog_width) == 515 or int(prog_width) == 517:
                                 previousprogram = int(program_id) - 1
                                 previousprogram_width = self.getControl(int(previousprogram)).getWidth()

                                 if previousprogram_width == 235:
                                     program_width = 399
                                     self.getControl(int(program_id)).setWidth(program_width)
                                     program_X = self.getControl(int(program_id)).getX()
                                     nextprogram = int(program_id) + 1
                                     nextprogramX = self.getControl(int(nextprogram)).getX()

                                     if program_X == 375:
                                         if nextprogramX == 1138:
                                             pos_Y = self.getControl(int(nextprogram)).getY()
                                             self.getControl(int(nextprogram)).setPosition(780, int(pos_Y))


                                 program_id = int(program_id)
                                 self.select_db_flag = True
                                 self.program_stop_minutes,self.program_stop_time = get_programming_times(self)

                                 if self.program_stop_minutes == '0':
                                     program_id = int(program_id)
                                     self.select_db_flag = True
                                     self.program_stop_minutes,self.program_stop_time = get_programming_times(self)


                                 if self.program_stop_time > self.epg_time_2:
                                     if self.program_stop_minutes == '05':
                                         if nextprogram_width == 515:
                                             programs_width = 399
                                             self.getControl(int(program_id)).setWidth(programs_width)

                                             if nextprogramsX == 1138:
                                                 pos_Y = self.getControl(int(nextprograms)).getY()
                                                 self.getControl(int(nextprograms)).setPosition(780, int(pos_Y))




                             elif int(pos_X) == 668 and int(prog_width) >= 344:
                                 program_id = int(program_id)
                                 self.select_db_flag = True
                                 self.program_stop_minutes,self.program_stop_time = get_programming_times(self)

                                 if self.program_stop_time < self.epg_time_3:
                                     if self.program_stop_minutes == '40':
                                         programs_width = 456
                                         self.getControl(int(program_id)).setWidth(int(programs_width))

                                         if nextprogram_Width == 567:
                                             if nextprogramsX > 837:
                                                 pos_X = int(837)
                                                 pos_Y = self.getControl(int(nextprograms)).getY()
                                                 self.getControl(int(nextprograms)).setPosition(pos_X, int(pos_Y))
                                                 self.getControl(int(nextprograms)).setVisible(True)
                                                 nextprograms_width = self.getControl(int(nextprograms)).getWidth()

                                                 if nextprograms_width == 344:
                                                     nextprograms1 = int(nextprograms) + 1
                                                     nextprogramsX1 = self.getControl(int(nextprograms1)).getX()

                                                     if nextprogramsX1 != 1189:
                                                         pos_X = int(1189)
                                                         pos_Y = self.getControl(int(nextprograms1)).getY()
                                                         self.getControl(int(nextprograms1)).setPosition(pos_X, int(pos_Y))
                                                         self.getControl(int(nextprograms1)).setVisible(True)




                                 else:
                                     if self.program_stop_minutes == '05':
                                         programs_width = 399
                                         self.getControl(int(program_id)).setWidth(int(programs_width))
                                         nextprogram = int(program_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()
                                         pos_Y = self.getControl(int(nextprograms)).getY()
                                         nextprogram_width = self.getControl(int(nextprogram)).getWidth()
                                         self.getControl(int(nextprograms)).setPosition(780, int(pos_Y))




                             elif int(pos_X) == 724 and int(prog_width) == 344:
                                 programsX = self.getControl(int(program_id)).getX()

                                 if programsX == 724:
                                     pos_Y = self.getControl(int(program_id)).getY()
                                     self.getControl(int(program_id)).setPosition(375, int(pos_Y))

                                     if int(prog_width) == 344:
                                         nextprogram = int(program_id) + 1
                                         nextprogram_width = self.getControl(int(nextprogram)).getWidth()
                                         nextprogramX = self.getControl(int(nextprogram)).getX()
                                         pos_Y = self.getControl(int(nextprogram)).getY()

                                         if nextprogram_width == 344:
                                             if nextprogramX == 1073:
                                                 pos_Y = self.getControl(int(nextprogram)).getY()
                                                 self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))
                                                 nextprograms = int(nextprogram) + 1
                                                 self.getControl(int(nextprograms)).setPosition(1073, int(pos_Y))
                                                 self.getControl(int(nextprograms)).setVisible(True)



                             elif int(pos_X) == 724 and int(prog_width) >= 691:
                                 self.getControl(int(program_id)).setPosition(375, int(pos_Y))
                                 program_width = self.getControl(int(program_id)).getWidth()
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getWidth()
                                 pos_Y = self.getControl(int(nextprogram)).getY()

                                 if program_width == 691:
                                     if nextprogramX != 1073:
                                         pos_Y = self.getControl(int(nextprogram)).getY()
                                         self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                         self.getControl(int(nextprogram)).setVisible(True)
                                 elif program_width == 741:
                                     if nextprogramX != 1124:
                                         pos_Y = self.getControl(int(nextprogram)).getY()
                                         self.getControl(int(nextprogram)).setPosition(1124, int(pos_Y))
                                         self.getControl(int(nextprogram)).setVisible(True)



                             elif int(pos_X) == 780 and int(prog_width) == 691:
                                 program_id = int(program_id)
                                 self.select_db_flag = True
                                 self.program_stop_minutes,self.program_stop_time = get_programming_times(self)

                                 if self.program_stop_time > self.epg_time_3:
                                     if self.program_stop_minutes == '05':
                                         programs_width = 676
                                         self.getControl(int(program_id)).setWidth(int(programs_width))
                                         nextprogram = int(program_id) + 1
                                         pos_X = self.getControl(int(nextprogram)).getX()

                                         if int(pos_X) != 1093:
                                             pos_Y = self.getControl(int(nextprogram)).getY()
                                             self.getControl(int(nextprogram)).setPosition(1124, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(True)



                             elif int(pos_X) == 897 and int(prog_width) >= 344:
                                 if int(prog_width) == 344:
                                     if nextprogramX != 549:
                                         pos_Y = self.getControl(int(program_id)).getY()
                                         self.getControl(int(program_id)).setPosition(549, int(pos_Y))
                                 elif int(prog_width) == 452:
                                     if nextprogramX != 549:
                                         pos_Y = self.getControl(int(program_id)).getY()
                                         self.getControl(int(program_id)).setPosition(549, int(pos_Y))


                                 program_width = self.getControl(int(program_id)).getWidth()
                                 nextprogram = int(program_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                 nextprogramWidth = self.getControl(int(nextprogram)).getWidth()

                                 if nextprogramX != 897:
                                     if program_width == 344:
                                         pos_Y = self.getControl(int(nextprogram)).getY()
                                         self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))
                                         self.getControl(int(nextprogram)).setVisible(True)
                                 elif program_width == 452:
                                     pos_Y = self.getControl(int(nextprogram)).getY()

                                     if int(pos_Y) == 315:
                                         self.getControl(int(nextprogram)).setPosition(1008, 315)
                                         self.getControl(int(nextprogram)).setVisible(True)
                                     elif int(pos_Y) == 353:
                                         print "catch this 7"
                                         self.getControl(int(nextprogram)).setPosition(1008, 353)
                                         self.getControl(int(nextprogram)).setVisible(True)
                                     elif int(pos_Y) == 391:
                                         self.getControl(int(nextprogram)).setPosition(1008, 391)
                                         self.getControl(int(nextprogram)).setVisible(True)
                                     elif int(pos_Y) == 428:
                                         print "catch this troubleshoot 5"
                                         self.getControl(int(nextprogram)).setPosition(1008, 428)
                                         self.getControl(int(nextprogram)).setVisible(True)
                                     elif int(pos_Y) == 466:
                                         self.getControl(int(nextprogram)).setPosition(1008, 466)
                                         self.getControl(int(nextprogram)).setVisible(True)
                                     elif int(pos_Y) == 503:
                                         self.getControl(int(nextprogram)).setPosition(1008, 503)
                                         self.getControl(int(nextprogram)).setVisible(True)
                                     elif int(pos_Y) == 541:
                                         self.getControl(int(nextprogram)).setPosition(1008, 541)
                                         self.getControl(int(nextprogram)).setVisible(True)



                             elif int(pos_X) == 949 and int(prog_width) >= 167 or int(pos_X) == 952 and int(prog_width) >= 167:
                                 self.getControl(int(program_id)).setPosition(614, int(pos_Y))
                                 nextprogram = int(program_id) + 1
                                 program_width = self.getControl(int(program_id)).getWidth()

                                 if program_width == 344:
                                     pos_Y = self.getControl(int(nextprogram)).getY()
                                     self.getControl(int(nextprogram)).setPosition(963, int(pos_Y))
                                     self.getControl(int(nextprogram)).setVisible(True)




                             elif int(pos_X) == 1073 and int(prog_width) == 167:
                                 self.getControl(int(program_id)).setPosition(724, int(pos_Y))
                                 nextprogram = int(program_id) + 1
                                 nextprogram_width = self.getControl(int(nextprogram)).getWidth()
                                 nextprogramX = self.getControl(int(nextprogram)).getX()

                                 if nextprogramX != 1073:
                                     pos_Y = self.getControl(int(nextprogram)).getY()
                                     self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                     self.getControl(int(nextprogram)).setVisible(True)



                             elif int(pos_X) == 1073 and int(prog_width) == 344:
                                 self.getControl(int(program_id)).setPosition(724, int(pos_Y))
                                 nextprogram = int(program_id) + 1
                                 nextprogram_width = self.getControl(int(nextprogram)).getWidth()
                                 nextprogramX = self.getControl(int(nextprogram)).getX()

                                 if nextprogramX != 1073:
                                     pos_Y = self.getControl(int(nextprogram)).getY()
                                     self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                     self.getControl(int(nextprogram)).setVisible(True)



                             elif int(pos_X) == 1073 and int(prog_width) >= 691:
                                 previous_prog_id = int(program_id) - 1
                                 previousprogram_X = self.getControl(int(previous_prog_id)).getX()

                                 if previousprogram_X == 440:
                                     pos_Y = self.getControl(int(program_id)).getY()
                                     self.getControl(int(program_id)).setPosition(733, int(pos_Y))
                                 else:
                                     pos_Y = self.getControl(int(program_id)).getY()
                                     self.getControl(int(program_id)).setPosition(724, int(pos_Y))




                             elif int(pos_X) == 1247 and int(prog_width) >= 59:
                                 pos_Y = self.getControl(int(program_id)).getY()
                                 self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))



                             elif int(pos_X) < 375:
                                 self.getControl(int(program_id)).setVisible(False)
                                 pos_Y = self.getControl(int(program_id)).getY()
                                 self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))