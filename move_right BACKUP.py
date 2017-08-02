import datetime
import time
import xbmc
import xbmcgui
import os
from sqlite3 import dbapi2 as database
cont = 0


def get_programming_times(self):
     #global self.program_stop_minutes, self.program_stop_time, self.epg_time_1, self.epg_time_2, self.epg_time_3
     #print "you are now calling the get_programming_times function now chrisssssssssssssssss"

     if self.select_db_flag == True:
         self.select_db_flag = False
         self.program_stop_time = list()
         program_id = ''.join(str(x) for x in self.program_id)
         profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
         conn1 = database.connect(profilePath)
         cur1 = conn1.cursor()
         cur1.execute('SELECT stop_date FROM programs where program_id=?', [program_id])
         data = cur1.fetchone()

         if data is not None:
             stop_date = str(data[0])
             stop_time = time.strptime(stop_date, '%Y%m%d%H%M%S')
             stop_time = datetime.datetime.fromtimestamp(time.mktime(stop_time))
             program_stop_hours = str(stop_time.hour)
             program_stop_minutes = str(stop_time.minute)
             program_stop_days = str(stop_time.day)
             program_stop_months = str(stop_time.month)
             program_stop_year = str(stop_time.year)
             print "print finished at "
             print program_stop_minutes

             if program_stop_minutes == "0":
                 program_stop_minutes = "00"


             if program_stop_hours == "0":
                 program_stop_hours = "12"
                 program_AM_PM = 'AM'
             elif program_stop_hours == "1":
                 program_stop_hours = "1"
                 program_AM_PM = 'AM'
             elif program_stop_hours == "2":
                 program_stop_hours = "2"
                 program_AM_PM = 'AM'
             elif program_stop_hours == "3":
                 program_stop_hours = "3"
                 program_AM_PM = 'AM'
             elif program_stop_hours == "4":
                 program_stop_hours = "4"
                 program_AM_PM = 'AM'
             elif program_stop_hours == "5":
                 program_stop_hours = "5"
                 program_AM_PM = 'AM'
             elif program_stop_hours == "6":
                 program_stop_hours = "6"
                 program_AM_PM = 'AM'
             elif program_stop_hours == "7":
                 program_stop_hours = "7"
                 program_AM_PM = 'AM'
             elif program_stop_hours == "8":
                 program_stop_hours = "8"
                 program_AM_PM = 'AM'
             elif program_stop_hours == "9":
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

             program_times = str(program_stop_hours + ':' + program_stop_minutes + program_AM_PM)
             program_date_format = str(program_stop_days + "/" + program_stop_months + "/" + program_stop_year + " " + program_times)
             program_date_format = time.strptime(program_date_format, '%d/%m/%Y %I:%M%p')
             self.program_stop_time.append(program_date_format)
             self.program_finished.append(program_stop_hours)
             #print "program_date_format timestamp"
             #print program_date_format

         #return self.program_stop_minutes, self.program_stop_time




def epg_times_stamp(self):
     half_hour = str(self.getControl(344).getLabel())
     one_hour = str(self.getControl(345).getLabel())
     one_hour_half = str(self.getControl(346).getLabel())


     if one_hour == "12:00AM":
         today_day = time.strftime("%d")
         today_month = time.strftime("%m")
         today_year = time.strftime("%Y")
         epg_time_1_days = int(today_day)
         epg_time_1_days = str(epg_time_1_days)
         epg_time_1_months = str(today_month)
         epg_time_1_year = str(today_year)
         epg_time_2_days = int(today_day) + 1
         epg_time_2_days = str(epg_time_2_days)
         epg_time_2_months = str(today_month)
         epg_time_2_year = str(today_year)
         epg_time_3_days = str(epg_time_2_days)
         epg_time_3_months = str(today_month)
         epg_time_3_year = str(today_year)
         half_hour_date = str(epg_time_1_days + "/" + epg_time_1_months + "/" + epg_time_1_year + " " + half_hour)
         one_hour_date = str(epg_time_2_days + "/" + epg_time_2_months + "/" + epg_time_2_year + " " + one_hour)
         one_hour_half_date = str(epg_time_2_days + "/" + epg_time_2_months + "/" + epg_time_2_year + " " + one_hour_half)


     elif one_hour_half == "12:00AM":
         today_day = time.strftime("%d")
         today_month = time.strftime("%m")
         today_year = time.strftime("%Y")
         epg_time_1_days = int(today_day)
         epg_time_1_days = str(epg_time_1_days)
         epg_time_1_months = str(today_month)
         epg_time_1_year = str(today_year)
         epg_time_2_days = str(epg_time_1_days)
         epg_time_2_months = str(epg_time_1_months)
         epg_time_2_year = str(today_year)
         epg_time_3_days = int(epg_time_2_days) + 1
         epg_time_3_days = str(epg_time_3_days)
         epg_time_3_months = str(epg_time_1_months)
         epg_time_3_year = str(today_year)
         half_hour_date = str(epg_time_1_days + "/" + epg_time_1_months + "/" + epg_time_1_year + " " + half_hour)
         one_hour_date = str(epg_time_2_days + "/" + epg_time_2_months + "/" + epg_time_2_year + " " + one_hour)
         one_hour_half_date = str(epg_time_3_days + "/" + epg_time_3_months + "/" + epg_time_3_year + " " + one_hour_half)


     else:
         today_day = time.strftime("%d")
         today_month = time.strftime("%m")
         today_year = time.strftime("%Y")
         epg_time_1_days = str(today_day)
         epg_time_1_months = str(today_month)
         epg_time_1_year = str(today_year)
         epg_time_2_days = str(today_day)
         epg_time_2_months = str(today_month)
         epg_time_2_year = str(today_year)
         half_hour_date = str(epg_time_1_days + "/" + epg_time_1_months + "/" + epg_time_1_year + " " + half_hour)
         one_hour_date = str(epg_time_2_days + "/" + epg_time_2_months + "/" + epg_time_2_year + " " + one_hour)
         one_hour_half_date = str(epg_time_2_days + "/" + epg_time_2_months + "/" + epg_time_2_year + " " + one_hour_half)
     self.epg_time_1 = list()
     self.epg_time_2 = list()
     self.epg_time_3 = list()
     epg_time_1 = time.strptime(half_hour_date, '%d/%m/%Y %I:%M%p')
     epg_time_2 = time.strptime(one_hour_date, '%d/%m/%Y %I:%M%p')
     epg_time_3 = time.strptime(one_hour_half_date, '%d/%m/%Y %I:%M%p')
     self.epg_time_1.append(epg_time_1)
     self.epg_time_2.append(epg_time_2)
     self.epg_time_3.append(epg_time_3)




def update_buttons(self):
     profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
     conn1 = database.connect(profilePath)
     cur = conn1.cursor()
     program_id = ''.join(str(x) for x in self.program_id)
     nextprogram = int(program_id) + 1
     nextprogram1 = int(nextprogram) + 1
     nextprogram2 = int(nextprogram1) + 1
     nextprogram3 = int(nextprogram2) + 1
     nextprogram4 = int(nextprogram3) + 1
     nextprogram5 = int(nextprogram4) + 1
     nextprogram6 = int(nextprogram5) + 1
     nextprogram7 = int(nextprogram6) + 1
     program_button_1 = self.getControl(int(program_id))
     program_button_2 = self.getControl(int(nextprogram))
     program_button_3 = self.getControl(int(nextprogram1))
     program_button_4 = self.getControl(int(nextprogram2))
     program_button_5 = self.getControl(int(nextprogram3))
     program_button_6 = self.getControl(int(nextprogram4))
     program_button_7 = self.getControl(int(nextprogram5))
     program_button_8 = self.getControl(int(nextprogram6))
     program_button_9 = self.getControl(int(nextprogram7))
     nextprogram_width = program_button_2.getWidth()
     nextprogram_label = program_button_2.getLabel()
     nextprogram1_width = program_button_3.getWidth()
     nextprogram1_label = program_button_3.getLabel()
     nextprogram2_width = program_button_4.getWidth()
     nextprogram2_label = program_button_4.getLabel()
     nextprogram3_width = program_button_5.getWidth()
     nextprogram3_label = program_button_5.getLabel()
     nextprogram4_width = program_button_6.getWidth()
     nextprogram4_label = program_button_6.getLabel()
     nextprogram5_width = program_button_7.getWidth()
     nextprogram5_label = program_button_7.getLabel()
     nextprogram6_width = program_button_8.getWidth()
     nextprogram6_label = program_button_8.getLabel()
     nextprogram7_width = program_button_9.getWidth()
     nextprogram7_label = program_button_9.getLabel()
     program_button_1.setLabel(nextprogram_label)
     program_button_1.setWidth(nextprogram_width)
     program_button_2.setLabel(nextprogram1_label)
     program_button_2.setWidth(nextprogram1_width)
     program_button_3.setLabel(nextprogram2_label)
     program_button_3.setWidth(nextprogram2_width)
     program_button_4.setLabel(nextprogram3_label)
     program_button_4.setWidth(nextprogram3_width)
     program_button_5.setLabel(nextprogram4_label)
     program_button_5.setWidth(nextprogram4_width)
     program_button_6.setLabel(nextprogram5_label)
     program_button_6.setWidth(nextprogram5_width)
     program_button_7.setLabel(nextprogram6_label)
     program_button_7.setWidth(nextprogram6_width)
     program_button_8.setLabel(nextprogram7_label)
     program_button_8.setWidth(nextprogram7_width)
     update_in_database(self)

     #if data is not None:
         #pass




def update_in_database(self):
     profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
     conn1 = database.connect(profilePath)
     cur = conn1.cursor()
     print "you are calling update_in_database"
     print self.program_id
     program_id = ''.join(str(x) for x in self.program_id)
     #cur.execute('SELECT channel, program_id FROM programs WHERE program_id=?;', (program_id))
     cur.execute('SELECT channel, program_id FROM programs')
     data = cur.fetchone()

     if data is not None:
         value = program_id
         for i in range(0,10):
             if value == program_id:
                 cur.execute("UPDATE programs set program_id=? WHERE program_id=?",('',value))
             else:
                 cur.execute("UPDATE programs set program_id=? WHERE program_id=?",(value-1,value))
             value = int(value) + 1
         cur.execute("SELECT channel , stop_date FROM programs WHERE program_id=?;",(value-2,))
         data = cur.fetchone()
         cur.execute("UPDATE programs set program_id=? WHERE channel=? and start_date=? ",(value-1,data[0],data[1]))
         conn1.commit()




def GoRight(self):
     print "self.move_right_flag"
     print self.move_right_flag


     # change program controls to display the proper junks
     if self.channels_Index != len(self.program_buttons) - 1:
         if self.channel_page >= 0:
             CurrentId = self.getFocusId()
             CurrentRow = self.getControl(CurrentId).getX()
             CurrentRowY = self.getControl(CurrentId).getY()
             CurrentWidth = self.getControl(CurrentId).getWidth()
             epg_time_1 = ''.join(str(x) for x in self.epg_time_1)
             epg_time_2 = ''.join(str(x) for x in self.epg_time_2)
             epg_time_3 = ''.join(str(x) for x in self.epg_time_1)
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
                     positions_X = list()
                     self.program_id = list()
                     self.program_finished_clock = list()
                     epg_times_stamp(self)
                     epg_time_1 = ''.join(str(x) for x in self.epg_time_1)
                     epg_time_2 = ''.join(str(x) for x in self.epg_time_2)
                     epg_time_3 = ''.join(str(x) for x in self.epg_time_3)


                     for program_id in self.prog_id_list:
                         nextprogram = int(program_id) + 1
                         nextprogram1 = int(nextprogram) + 1
                         nextprogram2 = int(nextprogram1) + 1
                         nextprogram3 = int(nextprogram2) + 1
                         nextprogram4 = int(nextprogram3) + 1
                         nextprogram5 = int(nextprogram4) + 1
                         nextprogram6 = int(nextprogram5) + 1
                         nextprogram7 = int(nextprogram6) + 1
                         program_button_1 = self.getControl(int(program_id))
                         program_button_2 = self.getControl(int(nextprogram))
                         program_button_3 = self.getControl(int(nextprogram1))
                         program_button_4 = self.getControl(int(nextprogram2))
                         program_button_5 = self.getControl(int(nextprogram3))
                         program_button_6 = self.getControl(int(nextprogram4))
                         program_button_7 = self.getControl(int(nextprogram5))
                         program_button_8 = self.getControl(int(nextprogram6))
                         program_button_9 = self.getControl(int(nextprogram7))
                         program_width = program_button_1.getWidth()
                         programX = program_button_1.getX()
                         pos_X = program_button_1.getX()
                         pos_Y = program_button_1.getY()
                         pos1_Y = program_button_2.getY()
                         pos2_Y = program_button_3.getY()
                         pos3_Y = program_button_4.getY()
                         pos4_Y = program_button_5.getY()
                         CurrentRowID = self.getFocusId()
                         CurrentRow = self.getControl(CurrentRowID).getX()
                         CurrentWidth = self.getControl(CurrentRowID).getWidth()
                         self.program_id = list()
                         self.program_id.append(program_id)
                         self.select_db_flag = True
                         get_programming_times(self)
                         program_stop_time = ''.join(str(x) for x in self.program_stop_time)
                         program_finished = ''.join(str(x) for x in self.program_finished) 
                         print "----------- Begin Data ----------"
                         print "program_stop_time"
                         print program_stop_time


                         if program_stop_time <= epg_time_1:
                             print "here 7b"
                             self.program_id = list()
                             self.program_id.append(program_id)

                             if programX == 375 and int(program_width) >= 167:
                                 #call update buttons
                                 update_buttons(self)
                                 program_width = program_button_1.getWidth()
                                 nextprogram_width = program_button_2.getWidth()
                                 nextprogram1_width = program_button_3.getWidth()
                                 nextprogram2_width = program_button_4.getWidth()
                                 nextprogram3_width = program_button_5.getWidth()
                                 print "program_finished"
                                 print program_finished

                                 if int(program_width) >= 342 and int(program_width) <= 342:
                                     programs_width = 344
                                     program_button_1.setWidth(int(programs_width))

                                     if int(programs_width) == 344:
                                         program_button_2.setPosition(724, int(pos1_Y))

                                         if int(nextprogram_width) == 117:
                                             nextprograms_width = 118
                                             program_button_2.setWidth(int(nextprograms_width))

                                             if int(nextprograms_width) == 118:
                                                 program_button_3.setPosition(849, int(pos2_Y))

                                                 if int(nextprogram1_width) == 342:
                                                     program_button_4.setPosition(1197, int(pos3_Y))


                                         elif int(nextprogram_width) == 167:
                                             nextprograms_width = 165
                                             program_button_2.setWidth(int(nextprograms_width))

                                             if int(nextprograms_width) == 165:
                                                 program_button_3.setPosition(897, int(pos2_Y))

                                                 if int(nextprogram1_width) >= 515:
                                                     program_button_4.setPosition(1592, int(pos3_Y))



                                         elif int(nextprogram_width) == 456:
                                             nextprograms_width = 454
                                             program_button_2.setWidth(int(nextprograms_width))

                                             if int(nextprograms_width) == 454:
                                                 program_button_3.setPosition(1184, int(pos2_Y))


                                         elif int(nextprogram_width) == 515:
                                             program_button_3.setPosition(1246, int(pos2_Y))


                                         elif int(nextprogram_width) == 741:
                                             program_button_3.setPosition(1122, int(pos2_Y))


                                         elif int(nextprogram_width) == 691:
                                             program_button_3.setPosition(1419, int(pos2_Y))


                                         elif int(nextprogram_width) >= 1026:
                                             program_button_3.setPosition(1754, int(pos2_Y))



                                 if program_finished == '00':
                                     print "you are in the program_finished 00"
                                     if int(program_width) >= 454 and int(program_width) <= 456:
                                         programs_width = 117
                                         program_button_1.setWidth(int(programs_width))

                                         if int(programs_width) == 117:
                                             program_button_2.setPosition(497, int(pos1_Y))

                                             if int(nextprogram_width) == 167:
                                                 program_button_3.setPosition(669, int(pos1_Y))

                                                 if int(nextprogram1_width) >= 691:
                                                     program_button_4.setPosition(1364, int(pos1_Y))



                                 elif program_finished == '15':
                                     if int(program_width) >= 454 and int(program_width) <= 456:
                                         programs_width = 456
                                         program_button_1.setWidth(int(programs_width))

                                         if int(programs_width) == 456:
                                             program_button_2.setPosition(837, int(pos1_Y))

                                             if int(nextprogram_width) == 167:
                                                 program_button_3.setPosition(1009, int(pos1_Y))

                                                 if int(nextprogram1_width) >= 691:
                                                     program_button_4.setPosition(1704, int(pos1_Y))



                                 elif int(program_width) == 691:
                                     program_button_2.setPosition(1072, int(pos1_Y))


                                 elif int(program_width) == 741:
                                     program_button_2.setPosition(1122, int(pos1_Y))


                                 elif int(program_width) >= 1026:
                                     program_button_2.setPosition(1405, int(pos1_Y))




                         elif program_stop_time == epg_time_2:
                             print "here 8b"
                             self.program_id = list()
                             self.program_id.append(program_id)

                             if programX == 375 and int(program_width) >= 342:
                                 program_width = program_button_1.getWidth()
                                 nextprogram_width = program_button_2.getWidth()
                                 nextprogram1_width = program_button_3.getWidth()
                                 nextprogram2_width = program_button_4.getWidth()
                                 nextprogram3_width = program_button_5.getWidth()
                                 print "you are working on 344 button"
                                 print program_id


                                 if int(program_width) >= 342:
                                     programs_width = 344
                                     program_button_1.setWidth(int(programs_width))

                                     if int(programs_width) == 344:
                                         program_button_2.setPosition(724, int(pos1_Y))
                                         print "you are working on 344 button 1"
                                         print "nextprogram_width"
                                         print nextprogram_width

                                         if int(nextprogram_width) == 167:
                                             program_button_3.setPosition(897, int(pos2_Y))

                                             if int(nextprogram1_width) == 117:
                                                 program_button_4.setPosition(1020, int(pos3_Y))


                                             elif int(nextprogram1_width) >= 515:
                                                 program_button_4.setPosition(1412, int(pos3_Y))



                                         elif int(nextprogram_width) == 227:
                                             nextprograms_width = 228
                                             program_button_2.setWidth(int(nextprograms_width))

                                             if int(nextprograms_width) == 228:
                                                 program_button_3.setPosition(959, int(pos2_Y))

                                                 if int(nextprogram1_width) == 117:
                                                     nextprogram1_width = 107
                                                     program_button_3.setWidth(int(nextprogram1_width))

                                                     if int(nextprogram1_width) == 107:
                                                         program_button_4.setPosition(1072, int(pos3_Y))




                                         elif int(nextprogram_width) >= 342 and int(nextprogram_width) <= 344:
                                             nextprograms_width = 342
                                             program_button_2.setWidth(int(nextprograms_width))
                                             print "you are working on 344 button 3"

                                             if int(nextprograms_width) == 342:
                                                 program_button_3.setPosition(1072, int(pos2_Y))

                                                 if int(nextprogram1_width) == 117:
                                                     program_button_4.setPosition(1196, int(pos3_Y))


                                                 elif int(nextprogram1_width) == 167:
                                                     program_button_4.setPosition(1246, int(pos3_Y))



                                         elif int(nextprogram_width) == 408:
                                             program_button_3.setPosition(787, int(pos2_Y))


                                             if int(nextprogram1_width) == 691:
                                                 program_button_4.setPosition(1482, int(pos3_Y))



                                         elif int(nextprogram_width) == 456:
                                             program_button_3.setPosition(1184, int(pos2_Y))


                                         elif int(nextprogram_width) == 515:
                                             program_button_3.setPosition(1246, int(pos2_Y))



                                         elif int(nextprogram_width) == 626:
                                             program_button_3.setPosition(1419, int(pos2_Y))



                                         elif int(nextprogram_width) >= 691:
                                             program_button_3.setPosition(1419, int(pos2_Y))



                                 elif int(program_width) == 167:
                                     program_button_2.setPosition(549, int(pos1_Y))

                                     if int(nextprogram_width) == 342:
                                         program_button_3.setPosition(897, int(pos2_Y))

                                         if int(nextprogram1_width) == 691:
                                             program_button_4.setPosition(1592, int(pos3_Y))



                                     elif int(nextprogram_width) == 691:
                                         program_button_3.setPosition(1246, int(pos2_Y))




                                 elif int(program_width) == 228:
                                     program_button_2.setPosition(610, int(pos1_Y))

                                     if int(nextprogram_width) == 107:
                                         program_button_3.setPosition(724, int(pos2_Y))

                                         if int(nextprogram1_width) == 456:
                                             program_button_4.setPosition(1186, int(pos3_Y))



                                 elif int(program_width) == 408:
                                     program_button_2.setPosition(787, int(pos1_Y))



                                 elif int(program_width) == 456:
                                     program_button_2.setPosition(837, int(pos1_Y))

                                     if int(nextprogram_width) >= 1197:
                                         program_button_3.setPosition(1572, int(pos2_Y))



                                 elif int(program_width) == 515:
                                     programs_width = 516
                                     program_button_1.setWidth(int(programs_width))

                                     if int(programs_width) == 516:
                                         program_button_2.setPosition(897, int(pos1_Y))

                                         if int(nextprogram_width) == 59:
                                             nextprograms_width = 56
                                             program_button_2.setWidth(int(nextprograms_width))

                                             if int(nextprograms_width) == 56:
                                                 program_button_3.setPosition(959, int(pos2_Y))


                                         elif int(nextprogram_width) >= 515:
                                             program_button_3.setPosition(1572, int(pos2_Y))



                                 elif int(program_width) == 567:
                                     program_button_2.setPosition(949, int(pos1_Y))



                                 elif int(program_width) == 626:
                                     programs_width = 627
                                     program_button_1.setWidth(int(programs_width))

                                     if int(programs_width) == 627:
                                         program_button_2.setPosition(1009, int(pos1_Y))

                                         if int(nextprogram_width) == 59:
                                             nextprograms_width = 56
                                             program_button_2.setWidth(int(nextprograms_width))

                                             if int(nextprograms_width) == 56:
                                                 program_button_3.setPosition(1072, int(pos2_Y))



                                 elif int(program_width) >= 691 and int(program_width) <= 692:
                                     programs_width = 691
                                     program_button_1.setWidth(int(programs_width))

                                     if int(programs_width) == 691:
                                         program_button_2.setPosition(1072, int(pos1_Y))



                                 elif int(program_width) >= 741:
                                     program_button_2.setPosition(1124, int(pos1_Y))



                                 elif int(program_width) > 1072:
                                     program_button_2.setPosition(1618, int(pos1_Y))








                         elif program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                             print "here 9b"
                             self.program_id = list()
                             self.program_id.append(program_id)

                             if programX == 375 and int(program_width) >= 803 and int(program_width) <= 814:
                                 programs_width = 456
                                 program_button_1.setWidth(int(programs_width))

                                 if int(programs_width) == 456:
                                     program_button_2.setPosition(839, int(pos1_Y))
                                     nextprogram_width = program_button_2.getWidth()
                                     nextprogram1_width = program_button_3.getWidth()
                                     nextprogram2_width = program_button_4.getWidth()
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram_width) == 56:
                                         nextprograms_width = 52
                                         program_button_2.setWidth(int(nextprograms_width))

                                         if int(nextprograms_width) == 52: 
                                             program_button_3.setPosition(897, int(pos2_Y))



                             elif programX == 375 and int(program_width) >= 741 and int(program_width) <= 757:
                                 programs_width = 399
                                 program_button_1.setWidth(int(programs_width))

                                 if int(programs_width) == 399:
                                     program_button_2.setPosition(782, int(pos1_Y))




                             elif programX == 375 and int(program_width) >= 625 and int(program_width) <= 630:
                                 programs_width = 277
                                 program_button_1.setWidth(int(programs_width))

                                 if int(programs_width) == 277:
                                     program_button_2.setPosition(659, int(pos1_Y))
                                     nextprogram_width = program_button_2.getWidth()
                                     nextprogram1_width = program_button_3.getWidth()
                                     nextprogram2_width = program_button_4.getWidth()
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram_width) == 56:
                                         nextprograms_width = 59
                                         program_button_2.setWidth(int(nextprograms_width))

                                         if int(nextprograms_width) == 59:
                                             program_button_3.setPosition(724, int(pos2_Y))

                                             if int(nextprogram1_width) == 344:
                                                 nextprograms1_width = 342
                                                 program_button_3.setWidth(int(nextprograms1_width))

                                                 if int(nextprograms1_width) == 342:
                                                         program_button_4.setPosition(1072, int(pos3_Y))




                             elif programX == 375 and int(program_width) == 577:
                                 programs_width = 167
                                 program_button_1.setWidth(int(programs_width))

                                 if int(programs_width) == 167:
                                     program_button_2.setPosition(549, int(pos1_Y))
                                     nextprogram_width = program_button_2.getWidth()
                                     nextprogram1_width = program_button_3.getWidth()
                                     nextprogram2_width = program_button_4.getWidth()
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram_width) == 59:
                                         program_button_3.setPosition(610, int(pos2_Y))


                                     elif int(nextprogram_width) == 172:
                                         nextprograms_width = 167
                                         program_button_2.setWidth(int(nextprograms_width))

                                         if int(nextprograms_width) == 167:
                                             program_button_3.setPosition(783, int(pos2_Y))

                                             if int(nextprogram1_width) == 117:
                                                 nextprograms1_width = 108
                                                 program_button_3.setWidth(int(nextprograms1_width))

                                                 if int(nextprograms1_width) == 108:
                                                     program_button_4.setPosition(897, int(pos3_Y))



                                     elif int(nextprogram_width) == 344:
                                         nextprograms_width = 342
                                         program_button_2.setWidth(int(nextprograms_width))

                                         if int(nextprograms_width) == 342:
                                             program_button_3.setPosition(959, int(pos2_Y))



                                     elif int(nextprogram_width) == 515:
                                         nextprograms_width = 516
                                         program_button_2.setWidth(int(nextprograms_width))

                                         if int(nextprograms_width) == 516:
                                             program_button_3.setPosition(1072, int(pos2_Y))



                                     elif int(nextprogram_width) == 567:
                                         nextprograms_width = 570
                                         program_button_2.setWidth(int(nextprograms_width))

                                         if int(nextprograms_width) == 570:
                                             program_button_3.setPosition(1125, int(pos2_Y))

                                             if int(nextprogram1_width) == 59:
                                                 nextprograms1_width = 41
                                                 program_button_2.setWidth(int(nextprograms1_width))

                                                 if int(nextprograms1_width) == 41:
                                                     program_button_3.setPosition(1175, int(pos2_Y))



                                     elif int(nextprogram_width) == 626:
                                         nextprograms_width = 629
                                         program_button_2.setWidth(int(nextprograms_width))

                                         if int(nextprograms_width) == 629:
                                             program_button_3.setPosition(1246, int(pos2_Y))



                             elif programX == 375 and programX == 375 and int(program_width) == 567:
                                 programs_width = 232
                                 program_button_1.setWidth(int(programs_width))

                                 if int(int(programs_width)) == 232:
                                     program_button_2.setPosition(609, int(pos1_Y))




                             elif programX == 375 and int(program_width) >= 515 and int(program_width) <= 517:
                                 programs_width = 167
                                 program_button_1.setWidth(int(programs_width))
                                 program_width = program_button_1.getWidth()

                                 if int(programs_width) == 167:
                                     program_button_2.setPosition(549, int(pos1_Y))
                                     nextprogram_width = program_button_2.getWidth()
                                     nextprogram1_width = program_button_3.getWidth()
                                     nextprogram2_width = program_button_4.getWidth()
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram_width) == 56:
                                         nextprograms_width = 53
                                         program_button_2.setWidth(int(nextprograms_width))

                                         if int(nextprograms_width) == 53:
                                             program_button_3.setPosition(609, int(pos2_Y))


                                     elif int(nextprogram_width) == 515:
                                         program_button_3.setPosition(1072, int(pos2_Y))


                                     elif int(nextprogram_width) == 691:
                                         program_button_3.setPosition(1246, int(pos2_Y))



                                 elif int(program_width) == 691:
                                     programs_width = 691
                                     program_button_1.setWidth(int(programs_width))

                                     if int(programs_width) == 691:
                                         program_button_2.setPosition(1246, int(pos1_Y))




                             #WRITE THE CODE FOR 40 MINS COPY FROM LIVEPROGRAMMING BETWEEN PROGRAM_STOP_TIME > EPG_TIME_1 AND PROGRAM_STOP_TIME < EPG_TIME_2
                             elif program_finished == '40':
                                 if programX == 375 and int(program_width) >= 450 and int(program_width) <= 456:
                                     programs_width = 125
                                     program_button_1.setWidth(int(programs_width))
                                     program_width = program_button_1.getWidth()

                                     if int(programs_width) == 125:
                                         program_button_2.setPosition(507, int(pos1_Y))
                                         nextprogram_width = program_button_2.getWidth()
                                         nextprogram1_width = program_button_3.getWidth()
                                         nextprogram2_width = program_button_4.getWidth()
                                         nextprogram3_width = program_button_5.getWidth()

                                         if int(nextprogram_width) >= 53 and int(nextprogram_width) <= 55:
                                             nextprograms_width = 59
                                             program_button_2.setWidth(int(nextprograms_width))

                                             if int(nextprograms_width) == 59:
                                                 program_button_3.setPosition(573, int(pos2_Y))

                                                 if int(nextprogram1_width) == 396:
                                                     nextprograms1_width = 399
                                                     program_button_3.setWidth(int(nextprograms1_width))

                                                     if int(nextprograms1_width) == 399:
                                                         program_button_3.setPosition(978, int(pos2_Y))



                                         elif int(nextprogram_width) == 567:
                                             nextprograms_width = 565
                                             program_button_3.setWidth(int(nextprograms_width))

                                             if int(nextprograms_width) == 565:
                                                 program_button_3.setPosition(1072, int(pos2_Y))



                                         elif int(nextprogram_width) == 626:
                                             nextprograms_width = 633
                                             program_button_2.setWidth(int(nextprograms_width))

                                             if int(nextprograms_width) == 633:
                                                 program_button_3.setPosition(1138, int(pos2_Y))

                                                 if int(nextprogram1_width) == 117:
                                                     program_button_4.setPosition(1263, int(pos3_Y))



                                         elif int(nextprogram_width) == 691:
                                             nextprograms_width = 692
                                             program_button_2.setWidth(int(nextprograms_width))

                                             if int(nextprograms_width) == 691:
                                                 program_button_3.setPosition(1197, int(pos2_Y))




                             elif programX == 375 and int(program_width) >= 399 and int(program_width) <= 408:
                                 programs_width = 59
                                 program_button_1.setWidth(int(programs_width))
                                 program_width = program_button_1.getWidth()

                                 if int(programs_width) == 59:
                                     program_button_2.setPosition(441, int(pos1_Y))
                                     nextprogram_width = program_button_2.getWidth()
                                     nextprogram1_width = program_button_3.getWidth()
                                     nextprogram2_width = program_button_4.getWidth()
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram_width) == 41:
                                         nextprograms_width = 53
                                         program_button_2.setWidth(int(nextprograms_width))

                                         if int(nextprograms_width) == 53:
                                             program_button_3.setPosition(509, int(pos2_Y))

                                             if int(nextprogram1_width) > 691:
                                                 program_button_4.setPosition(1572, int(pos3_Y))



                                     elif int(nextprogram_width) == 276:
                                         nextprograms_width = 277
                                         program_button_2.setWidth(int(nextprograms_width))

                                         if int(nextprogram_width) == 277:
                                             program_button_3.setPosition(724, int(pos2_Y))

                                             if int(nextprogram1_width) == 344:
                                                 nextprograms1_width = 342
                                                 program_button_3.setWidth(int(nextprograms1_width))

                                                 if int(nextprogram1_width) == 342:
                                                     program_button_4.setPosition(1072, int(pos3_Y))



                                     elif int(nextprogram_width) == 342:
                                         program_button_3.setPosition(790, int(pos2_Y))



                                     elif int(nextprogram_width) == 567:
                                         nextprograms_width = 562
                                         program_button_2.setWidth(int(nextprograms_width))

                                         if int(nextprograms_width) == 562:
                                             program_button_3.setPosition(1007, int(pos2_Y))

                                             if int(nextprogram1_width) == 59:
                                                 program_button_4.setPosition(1072, int(pos3_Y))



                                     elif int(nextprogram_width) == 626:
                                         program_button_3.setPosition(1072, int(pos2_Y))




                             elif programX == 375 and int(program_width) >= 276 and int(program_width) <= 278:
                                 #call update_buttons function if the print appears
                                 print "you are working on 276 and 278"
                                 program_width = program_button_1.getWidth()

                                 if int(program_width) == 59:
                                     program_button_2.setPosition(441, int(pos1_Y))
                                     nextprogram_width = program_button_2.getWidth()
                                     nextprogram1_width = program_button_3.getWidth()
                                     nextprogram2_width = program_button_4.getWidth()
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram_width) == 691:
                                         program_button_3.setPosition(1138, int(pos2_Y))

                                         if int(nextprogram1_width) == 59:
                                             program_button_4.setPosition(1201, int(pos3_Y))



                                 elif int(program_width) > 1072:
                                     program_button_2.setPosition(1618, int(pos1_Y))





                             elif programX == 375 and int(program_width) >= 228 and int(program_width) <= 235:

                                 if int(program_width) == 228 and int(program_width) == 108:
                                     #call update_buttons function if the print appears
                                     print "you are working on 228 and 108"
                                     program_width = program_button_1.getWidth()

                                     if int(program_width) == 459:
                                         programs_width = 456
                                         program_button_1.setWidth(programs_width)

                                         if int(programs_width) == 456:
                                             program_button_2.setPosition(837, int(pos1_Y))
                                             nextprogram_width = program_button_2.getWidth()
                                             nextprogram1_width = program_button_3.getWidth()
                                             nextprogram2_width = program_button_4.getWidth()
                                             nextprogram3_width = program_button_5.getWidth()

                                             if int(nextprogram_width) > 691:
                                                 program_button_3.setPosition(1572, int(pos2_Y))
                                                 program_button_4.setPosition(1874, int(pos3_Y))
                                                 program_button_5.setPosition(2216, int(pos4_Y))


                                 else:
                                     #call update_buttons function if the print appears
                                     print "you are working on 228 and 108 else statement"
                                     program_width = program_button_1.getWidth()
                                     nextprogram_width = program_button_2.getWidth()
                                     nextprogram1_width = program_button_3.getWidth()
                                     nextprogram2_width = program_button_4.getWidth()
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(program_width) == 167:
                                         program_button_2.setPosition(549, int(pos1_Y))

                                         if int(nextprogram_width) == 108:
                                             nextprograms_width = 118
                                             program_button_2.setWidth(int(nextprograms_width))

                                             if int(nextprograms_width) == 118:
                                                 program_button_3.setPosition(673, int(pos2_Y))

                                                 if int(nextprogram1_width) == 691:
                                                     program_button_4.setPosition(1369, int(pos3_Y))



                                     elif int(program_width) == 228:
                                         program_button_2.setPosition(410, int(pos1_Y))

                                         if int(nextprogram_width) == 108:
                                             nextprograms_width = 118
                                             program_button_2.setWidth(int(nextprograms_width))

                                             if int(nextprograms_width) == 118:
                                                 program_button_3.setPosition(710, int(pos2_Y))



                                     elif int(program_width) == 459:
                                         print "you are in the 459 box"



                                     elif int(program_width) == 691:
                                         program_button_2.setPosition(1072, int(pos1_Y))

                                         if int(nextprogram_width) == 167:
                                             program_button_3.setPosition(1246, int(pos2_Y))




                             elif programX == 375 and int(program_width) == 167:
                                 #call update_buttons function if the print appears
                                 print "you are working on 167"
                                 program_width = program_button_1.getWidth()
                                 nextprogram_width = program_button_2.getWidth()
                                 nextprogram1_width = program_button_3.getWidth()
                                 nextprogram2_width = program_button_4.getWidth()
                                 nextprogram3_width = program_button_5.getWidth()

                                 if int(program_width) == 167:
                                     program_button_2.setPosition(549, int(pos1_Y))

                                     if int(nextprogram_width) == 59:
                                         nextprograms_width = 56
                                         program_button_2.setWidth(int(nextprograms_width))

                                         if int(nextprogram_width) == 56:
                                             program_button_3.setPosition(610, int(pos2_Y))



                                 elif int(program_width) == 342:
                                     programs_width = 344
                                     program_button_1.setWidth(int(programs_width))

                                     if int(programs_width) >= 342 and int(programs_width) <= 344:
                                         program_button_2.setPosition(724, int(pos1_Y))

                                         if int(nextprogram_width) == 396:
                                             nextprograms_width = 408
                                             program_button_2.setWidth(int(nextprograms_width))

                                             if int(nextprograms_width) == 408:
                                                 program_button_3.setPosition(1138, int(pos2_Y))



                                         elif int(nextprogram_width) == 515:
                                             program_button_3.setPosition(1246, int(pos2_Y))



                                         elif int(nextprogram_width) == 691:
                                             program_button_3.setPosition(1419, int(pos2_Y))




                                 elif int(program_width) >= 515 and int(program_width) <= 517:
                                     programs_width = 344
                                     program_button_1.setWidth(int(programs_width))

                                     if int(programs_width) == 344:
                                         program_button_2.setPosition(724, int(pos1_Y))

                                         if int(nextprogram_width) == 167:
                                             nextprograms_width = 168
                                             program_button_3.setWidth(int(nextprograms_width))

                                             if int(nextprograms_width) == 168:
                                                 program_button_3.setPosition(1072, int(pos2_Y))

                                                 if int(nextprogram1_width) == 691:
                                                     program_button_4.setPosition(1767, int(pos3_Y))




                                         elif int(nextprogram_width) >= 342 and int(nextprogram_width) <= 344:
                                             nextprograms_width = 342
                                             program_button_2.setWidth(int(nextprograms_width))

                                             if int(nextprograms_width) == 342:
                                                 program_button_3.setPosition(1072, int(pos2_Y))



                                             elif int(nextprogram_width) >= 691:
                                                 program_button_3.setPosition(1572, int(pos2_Y))



                                         elif int(nextprogram_width) >= 515 and int(nextprogram_width) <= 517:
                                             program_button_3.setPosition(1246, int(pos2_Y))




                                 elif int(program_width) == 691:
                                     programs_width = 516
                                     program_button_1.setWidth(int(programs_width))
                                     program_button_2.setPosition(1072, int(pos1_Y))

                                     if int(nextprogram_width) == 516:
                                         program_button_2.setPosition(897, int(pos2_Y))



                                 elif int(program_width) >= 1197:
                                     program_button_2.setPosition(1572, int(pos1_Y))




                             elif programX == 375 and int(program_width) == 286:
                                 #call update_buttons function if the print appears
                                 print "you are working on 286"
                                 program_width = program_button_1.getWidth()
                                 nextprogram_width = program_button_2.getWidth()
                                 nextprogram1_width = program_button_3.getWidth()
                                 nextprogram2_width = program_button_4.getWidth()
                                 nextprogram3_width = program_button_5.getWidth()


                                 if int(program_width) == 286:
                                     print "here 1 for 286"

                                 elif int(program_width) == 344:
                                     print "here 2 for 344"




                             elif programX == 375 and int(program_width) == 59:
                                 #call update_buttons function if the print appears
                                 print "you are working on 59"
                                 program_width = program_button_1.getWidth()
                                 nextprogram_width = program_button_2.getWidth()
                                 nextprogram1_width = program_button_3.getWidth()
                                 nextprogram2_width = program_button_4.getWidth()
                                 nextprogram3_width = program_button_5.getWidth()

                                 if int(program_width) == 59 and int(nextprogram_width) >= 560 and nextprogram_width <= 567:
                                     nextprograms_width = 277
                                     program_button_2.setWidth(int(nextprograms_width))

                                     if int(nextprograms_width) == 277:
                                         program_button_2.setPosition(659, int(pos1_Y))




                                 elif int(program_width) == 59 and nextprogram_width == 278:
                                     program_button_2.setPosition(724, int(pos1_Y))

                                     if int(program_width) == 342:
                                         program_button_3.setPosition(1072, int(pos2_Y))



                                 elif int(program_width) >= 277 and int(program_width) <= 278:
                                     program_button_2.setPosition(659, int(pos1_Y))

                                     if int(nextprogram_width) == 342:
                                         program_button_3.setPosition(724, int(pos2_Y))



                                 elif int(program_width) == 342:
                                     program_button_3.setPosition(724, int(pos2_Y))

                                     if int(nextprogram_width) == 344:
                                         program_button_4.setPosition(1072, int(pos3_Y))



                                 elif int(program_width) == 567:
                                     program_button_2.setPosition(959, int(pos1_Y))

                                     if int(nextprogram_width) == 59:
                                         program_button_3.setPosition(1022, int(pos2_Y))

                                         if int(nextprogram1_width) == 691:
                                             program_button_4.setPosition(1718, int(pos3_Y))



                                 elif int(program_width) == 741:
                                     programs_width = 399
                                     program_button_1.setWidth(programs_width)

                                     if int(programs_width) == 399:
                                         program_button_2.setPosition(782, int(pos1_Y))

                                         if int(nextprogram_width) > 1072:
                                             program_button_3.setPosition(1856, int(pos2_Y))


                                 elif int(program_width) >= 1197:
                                     program_button_2.setPosition(1419, int(pos1_Y))







                         elif program_stop_time > epg_time_2 and program_stop_time < epg_time_3:
                             print "here 10b"
                             self.program_id = list()
                             self.program_id.append(program_id)

                             if programX == 375 and int(program_width) >= 969 and int(program_width) <= 1083:
                                 programs_width = 626
                                 program_button_1.setWidth(int(programs_width))

                                 if int(programs_width) == 626:
                                     program_button_2.setPosition(1009, int(pos1_Y))




                             elif programX == 375 and int(program_width) >= 847 and int(program_width) <= 879:
                                 programs_width = 516
                                 program_button_1.setWidth(int(programs_width))

                                 if int(programs_width) == 516:
                                     program_button_2.setPosition(897, int(pos1_Y))




                             elif programX == 375 and int(program_width) == 117:
                                 pass






                         elif program_stop_time == epg_time_3:
                             print "here 11b"
                             self.program_id = list()
                             self.program_id.append(program_id)

                             if programX == 375 and int(program_width) >= 1026:
                                 programs_width = 691
                                 program_button_1.setWidth(int(programs_width))
                                 program_width = program_button_1.getWidth()
                                 nextprogram_width = program_button_2.getWidth()

                                 if int(programs_width) == 691:
                                     program_button_2.setPosition(1072, int(pos1_Y))
 



                         elif program_stop_time > epg_time_3:
                             print "here 12b"
                             self.program_id = list()
                             self.program_id.append(program_id)

                             if programX == 375 and int(program_width) >= 1191:
                                 programs_width = 857
                                 program_button_1.setWidth(int(programs_width))
                                 program_width = program_button_1.getWidth()
                                 nextprogram_width = program_button_2.getWidth()

                                 if int(programs_width) == 857:
                                     program_button_2.setPosition(1238, int(pos1_Y))




                         #update_in_database(self)