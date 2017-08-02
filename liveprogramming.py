import datetime
import time
import _strptime
from itertools import izip_longest


def programs_remaining(self):
     #if_program_remaining == true codes goes here

     if self.program_remaining == True:
         self.program_remaining = False
         #posX = list()
         #posY = list()
         programs_button = [elem.control for elem in self.program_buttons]
         print "you are working on this for live programming........................."
         program_stop_time_list = list()
         self.epg_time_1 = list()
         self.epg_time_2 = list()
         self.epg_time_3 = list()


         #Now let change the programming button size for real time
         for program_end_time in self.program_end_time:
             half_hour = str(self.getControl(344).getLabel())
             one_hour = str(self.getControl(345).getLabel())
             one_hour_half = str(self.getControl(346).getLabel())
             program_stop_hours = str(program_end_time.hour)
             program_stop_minutes = str(program_end_time.minute)
             program_stop_days = str(program_end_time.day)
             program_stop_months = str(program_end_time.month)
             program_stop_year = str(program_end_time.year)
             print "half_hour"
             print half_hour


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


             if program_stop_minutes == "0":
                 program_stop_minutes = "00"

             if half_hour == "12:00AM":
                 today_day = time.strftime("%d")

                 if today_day != today_day:
                     today_day = int(today_day) + 1

                 today_month = time.strftime("%m")
                 today_year = time.strftime("%Y")
                 epg_time_1_days = int(today_day)
                 epg_time_1_days = str(epg_time_1_days)
                 epg_time_1_months = str(today_month)
                 epg_time_1_year = str(today_year)
                 epg_time_2_days = int(today_day)
                 epg_time_2_days = str(epg_time_2_days)
                 epg_time_2_months = str(today_month)
                 epg_time_2_year = str(today_year)
                 epg_time_3_days = str(epg_time_2_days)
                 epg_time_3_months = str(today_month)
                 epg_time_3_year = str(today_year)
                 print "you are in the epg_time_1........................1"


             elif one_hour == "12:00AM":
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
                 print "you are in the epg_time_1........................2"


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
                 print "you are in the epg_time_1........................3"


             else:
                 today_day = time.strftime("%d")
                 today_month = time.strftime("%m")
                 today_year = time.strftime("%Y")
                 epg_time_1_days = str(today_day)
                 epg_time_1_months = str(today_month)
                 epg_time_1_year = str(today_year)
                 epg_time_2_days = str(epg_time_1_days)
                 epg_time_2_months = str(epg_time_1_months)
                 epg_time_2_year = str(epg_time_1_year)
                 epg_time_3_days = str(epg_time_2_days)
                 epg_time_3_months = str(epg_time_2_months)
                 epg_time_3_year = str(epg_time_2_year)
                 print "you are in the epg_time_1........................4"
             half_hour_date = str(epg_time_1_days + "/" + epg_time_1_months + "/" + epg_time_1_year + " " + half_hour)
             one_hour_date = str(epg_time_2_days + "/" + epg_time_2_months + "/" + epg_time_2_year + " " + one_hour)
             one_hour_half_date = str(epg_time_3_days + "/" + epg_time_3_months + "/" + epg_time_3_year + " " + one_hour_half)
             program_times = str(program_stop_hours + ':' + program_stop_minutes + program_AM_PM)
             stop_times = str(program_stop_days + "/" + program_stop_months + "/" + program_stop_year + " " + program_times)
             program_stop_time_list.append(stop_times)
         epg_time_1 = time.strptime(half_hour_date, '%d/%m/%Y %I:%M%p')
         epg_time_2 = time.strptime(one_hour_date, '%d/%m/%Y %I:%M%p')
         epg_time_3 = time.strptime(one_hour_half_date, '%d/%m/%Y %I:%M%p')
         self.epg_time_1.append(epg_time_1)
         self.epg_time_2.append(epg_time_2)
         self.epg_time_3.append(epg_time_3)
         print "epg_time_1"
         print epg_time_1
         print "epg_time_2"
         print epg_time_2
         print "epg_time_3"
         print epg_time_3



         for program_id, program_stop_times, program_finished in zip(self.prog_id_list, program_stop_time_list, self.program_finished):
             current_time = int(time.strftime("%M"))
             program_width = self.getControl(int(program_id)).getWidth()
             program_stop_time = time.strptime(program_stop_times, '%d/%m/%Y %I:%M%p')
             programX = self.getControl(int(program_id)).getX()
             nextprogram = int(program_id) + 1
             nextprogramX = self.getControl(int(nextprogram)).getX()
             nextprogram_width = self.getControl(int(nextprogram)).getWidth()
             nextprogram_label = self.getControl(int(nextprogram)).getLabel()
             nextprogram1 = int(nextprogram) + 1
             nextprogram1X = self.getControl(int(nextprogram1)).getX()
             nextprogram1_width = self.getControl(int(nextprogram1)).getWidth()
             nextprogram2 = int(nextprogram1) + 1
             nextprogram2X = self.getControl(int(nextprogram2)).getX()
             nextprogram2_width = self.getControl(int(nextprogram2)).getWidth()
             nextprogram3 = int(nextprogram2) + 1
             nextprogram3X = self.getControl(int(nextprogram3)).getX()
             nextprogram3_width = self.getControl(int(nextprogram3)).getWidth()
             pos_Y = self.getControl(int(program_id)).getY()
             print "----------- Begin Data ----------"
             print "program_stop_time"
             print program_stop_time


             if programX == 375:
                 if programX == 375 and program_width == 59:
                     if nextprogramX == 441:
                         if nextprogram_width == 691:
                             self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))


                 elif programX == 375 and program_width == 167:
                     if nextprogram_width == 515:
                         self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))


                     elif nextprogram_width == 691:
                         self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))


                 elif programX == 375 and program_width >= 342 and program_width <= 344:
                     program_width = 344
                     self.getControl(int(program_id)).setWidth(program_width)

                     if nextprogramX == 1072:
                         self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))

                         if nextprogramX == 724 and program_width >= 342 and program_width <= 344:
                             nextprogram_width = 344
                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)



                 elif programX == 375 and program_width == 626:
                     if nextprogramX != 1009:
                         self.getControl(int(nextprogram)).setPosition(1009, int(pos_Y))


                     elif nextprogramX == 1009:
                         self.getControl(int(nextprogram)).setPosition(1009, int(pos_Y))



                 elif programX == 375 and program_width == 691:
                     if nextprogramX == 1072:
                         program_width = 691
                         self.getControl(int(program_id)).setWidth(program_width)
                         self.getControl(int(nextprogram)).setPosition(1072, int(pos_Y))
                         print "you are in the 1072"


                     elif nextprogramX != 1072:
                         program_width = 691
                         self.getControl(int(program_id)).setWidth(program_width)
                         self.getControl(int(nextprogram)).setPosition(1072, int(pos_Y))



                 elif programX == 375 and nextprogram_width == 167 and nextprogram1X == 723:
                     nextprogram_width = 169
                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)
                     self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))


                 elif programX == 375 and program_width == 277:
                     program_width = 279
                     self.getControl(int(program_id)).setWidth(program_width)

                     if nextprogramX != 610:
                         self.getControl(int(nextprogram)).setPosition(610, int(pos_Y))

                         if nextprogram_width == 342:
                             nextprogram_width = 344
                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)



                 elif programX == 375 and program_width == 399:
                     program_width = 408
                     self.getControl(int(program_id)).setWidth(program_width)

                     if nextprogramX != 790:
                         self.getControl(int(nextprogram)).setPosition(790, int(pos_Y))

                         if nextprogram_width == 59:
                             nextprogram_width = 47
                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                             if nextprogram_width == 47:
                                 self.getControl(int(nextprogram1)).setPosition(844, int(pos_Y))



             if program_stop_time == epg_time_1:
                 print "here 1a"
                 print "program_finished"
                 print program_finished

                 if program_finished == '00':
                     if programX == 375 and program_width == 456:
                         print "passed 1"
                         if nextprogram_width == 227:
                             print "passed 2"
                             if nextprogram1X != 1072:
                                 self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))
                                 print "passed 3"




                     elif programX == 375 and program_width == 342:
                         nextprogram_label = self.getControl(int(program_id)).getLabel()
                         self.getControl(int(program_id)).setWidth(nextprogram_width)
                         self.getControl(int(program_id)).setLabel(nextprogram_label)
                         #self.getControl(int(program_id)).setLabel(nextprogram_label, 'font14', '0xFFFFFFFF', '0xFFFF3300', '0xFF000000')
                         #self.getControl(int(program_id)).setVisible(False)
                         #self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                         #self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))



                 elif program_finished == '30':
                     if programX == 375 and program_width == 117:
                         self.getControl(int(program_id)).setWidth(nextprogram_width)
                         self.getControl(int(program_id)).setLabel(nextprogram_label)
                         self.getControl(int(nextprogram)).setPosition(507, int(pos_Y))


                     elif programX == 375 and program_width == 167:
                         if nextprogram_width == 396:
                             self.getControl(int(nextprogram)).setPosition(949, int(pos_Y))


                     #elif programX == 375 and program_width >= 342:
                         #programs_width = 342
                         #self.getControl(int(program_id)).setWidth(programs_width)
                         #self.getControl(int(program_id)).setVisible(False)
                         #self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                         #self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))

                         #if nextprogram_width == 344:
                             #self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))


                         #elif nextprogram_width == 691:
                             #self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))



             elif program_stop_time == epg_time_2:
                 print "here 2a"
                 print program_finished

                 if program_finished == '00':
                     if program_stop_time == epg_time_2:
                         if programX == 375 and program_width >= 342:
                             programs_width = 344
                             self.getControl(int(program_id)).setWidth(programs_width)
                             self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))
                             print "you are in the epg_time2 pass 2"

                             if nextprogram_width == 168:
                                 nextprogram_width = 168
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 168:
                                     self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))


                                 elif nextprogram_width == 167:
                                     self.getControl(int(nextprogram1)).setPosition(546, int(pos_Y))


                                 elif nextprogram_width == 286:
                                     self.getControl(int(nextprogram1)).setPosition(1009, int(pos_Y))

                                 elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                     self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))

                                 elif nextprogram_width == 456:
                                     nextprogram_width = 454
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 454:
                                         self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))




                             elif programX == 375 and program_width >= 286:
                                 programs_width = 343
                                 self.getControl(int(program_id)).setWidth(programs_width)
                                 self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))
                                 print "you are in the epg_time2 pass 3 a"
                                 print "nextprogram_width"
                                 print nextprogram_width

                                 if nextprogram_width == 286 and nextprogram1_width == 59:
                                     programs_width = 279
                                     self.getControl(int(nextprogram)).setWidth(programs_width)

                                     if programs_width == 279:
                                         self.getControl(int(nextprogram1)).setPosition(1009, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             nextprogram1_width = 56
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 56:
                                                 self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))



                                 elif nextprogram_width == 59:
                                     self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))

                                     if nextprogram1_width == 344:
                                         self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))



                                 elif nextprogram_width == 117:
                                     self.getControl(int(nextprogram1)).setPosition(849, int(pos_Y))



                                 elif nextprogram_width == 148:
                                     nextprogram_width = 167
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)
                                     print "you are here 1 chris"

                                     if nextprogram_width == 167:
                                         self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))

                                         if nextprogram1_width == 79:
                                             nextprogram1_width = 59
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 59:
                                                 self.getControl(int(nextprogram2)).setPosition(963, int(pos_Y))



                                 elif nextprogram_width == 167:
                                     self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))
                                     print "you are here 2 chris"

                                     if nextprogram1_width == 117:
                                         self.getControl(int(nextprogram2)).setPosition(1023, int(pos_Y))


                                     elif nextprogram1_width == 167:
                                         nextprogram1_width = 169
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 169:
                                             self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))



                                     elif nextprogram1_width == 344:
                                         nextprogram1_width = 342
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 342:
                                             self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                 elif nextprogram_width == 227:
                                     nextprogram_width = 228
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if int(nextprogram_width) == 228:
                                         self.getControl(int(nextprogram1)).setPosition(959, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             nextprogram1_width = 107
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 107:
                                                 self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))



                                 elif nextprogram_width >= 270 and nextprogram_width <= 286:
                                     print "you are here in 279"
                                     nextprogram_width = 293
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 293:
                                         self.getControl(int(nextprogram1)).setPosition(1023, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             self.getControl(int(nextprogram2)).setPosition(1146, int(pos_Y))



                                 elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                     nextprogram_width = 342
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 342:
                                         self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))


                                         elif nextprogram1_width == 117:
                                             nextprogram1_width = 106
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 106:
                                                 self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))


                                         elif nextprogram1_width == 167:
                                             self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                 elif nextprogram_width == 396:
                                     nextprogram_width = 407
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 407:
                                         self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             nextprogram1_width = 101
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 101:
                                                 self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                 elif nextprogram_width == 456:
                                     nextprogram_width = 454
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 454:
                                         self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))



                                 elif nextprogram_width == 515:
                                     self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))



                                 elif nextprogram_width == 691:
                                     nextprogram_width = 691
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 691:
                                         self.getControl(int(nextprogram1)).setPosition(1420, int(pos_Y))




                 elif program_finished >= '15' and program_finished <= '17':
                     if programX == 375 and program_width == 691:
                         programs_width = 342
                         self.getControl(int(program_id)).setWidth(programs_width)
                         self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))



                 elif program_finished == '25':
                     if programX == 375 and program_width == 456:
                         programs_width = 287
                         self.getControl(int(program_id)).setWidth(programs_width)



                 elif program_finished == '30':
                     if programX == 375 and program_width >= 342:
                         programs_width = 344
                         self.getControl(int(program_id)).setWidth(programs_width)
                         self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))

                         if nextprogram_width == 59:
                             self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))


                         elif nextprogram_width == 117:
                             nextprogram_width = 118
                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                             if nextprogram_width == 118:
                                 self.getControl(int(nextprogram1)).setPosition(849, int(pos_Y))

                                 if nextprogram1_width == 227:
                                     nextprogram1_width = 219
                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                     if nextprogram1_width == 117:
                                         self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))


                                     elif nextprogram1_width == 219:
                                         self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))


                         elif nextprogram_width == 167:
                             self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))

                             if nextprogram1_width == 59:
                                 nextprogram1_width = 55
                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                 if nextprogram1_width == 55:
                                     self.getControl(int(nextprogram2)).setPosition(959, int(pos_Y))


                             elif nextprogram1_width == 167:
                                 nextprogram1_width = 169
                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                 if nextprogram1_width == 169:
                                     self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))


                             elif nextprogram1_width >= 342 and nextprogram1_width <= 344:
                                 nextprogram1_width = 342
                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                 if nextprogram1_width == 342:
                                     self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))


                         elif nextprogram_width == 227:
                             self.getControl(int(nextprogram1)).setPosition(958, int(pos_Y))

                             if nextprogram1_width == 117:
                                 nextprogram1_width = 108
                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                 if nextprogram1_width == 108:
                                     self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))



                         elif nextprogram_width == 286:
                             nextprogram_width = 279
                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                             if nextprogram_width == 279:
                                 self.getControl(int(nextprogram1)).setPosition(1009, int(pos_Y))

                                 if nextprogram1_width == 59:
                                     nextprogram1_width = 57
                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                     if nextprogram1_width == 57:
                                         self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))



                         elif nextprogram_width >= 342 and nextprogram_width <= 344:
                             nextprogram_width = 342
                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                             if nextprogram_width == 342:
                                 self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))

                                 if nextprogram1_width == 59:
                                     self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))


                                 elif nextprogram1_width == 167:
                                     self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                         elif nextprogram_width == 396:
                             nextprogram_width = 407
                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                             if nextprogram_width == 407:
                                 self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))



                         elif nextprogram_width == 456:
                             nextprogram_width = 454
                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                             if nextprogram_width == 454:
                                 self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))


                         elif nextprogram_width == 515:
                             self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))




                 elif program_finished == '35':
                     print "you are in the 35 past now chris"




             elif program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                 print "here 3a"
                 print program_finished
                 nextprogram_label = self.getControl(int(program_id)).getLabel()
                 print "nextprogram_label"
                 print nextprogram_label

                 if program_finished == '00':
                     if program_stop_time == epg_time_1:
                         if programX == 375 and program_width <= 741:
                             programs_width = 342
                             self.getControl(int(program_id)).setWidth(programs_width)
                             self.getControl(int(program_id)).setVisible(False)
                             self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                             self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))

                             if nextprogram_width == 344:
                                 if nextprogram1X != 724:
                                     self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))


                     elif program_stop_time == epg_time_2 or program_stop_time > epg_time_2:
                         if programX == 375 and program_width >= 741:
                             programs_width = 342
                             self.getControl(int(program_id)).setWidth(programs_width)
                             self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))

                             if nextprogram_width == 342:
                                 if nextprogram1X != 1072:
                                     self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))



                     elif program_stop_time == epg_time_3:
                         if programX == 375 and program_width >= 741:
                             programs_width = 691
                             self.getControl(int(program_id)).setWidth(programs_width)
                             self.getControl(int(nextprogram)).setPosition(1072, int(pos_Y))




                 elif program_finished == '05':
                     if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                         if programX == 375 and program_width >= 227:
                             print "you are here for channel 4"
                             programs_width = 59
                             self.getControl(int(program_id)).setWidth(programs_width)


                             if programs_width == 59:
                                 self.getControl(int(nextprogram)).setPosition(441, int(pos_Y))

                                 if nextprogram_width == 59:
                                     self.getControl(int(nextprogram1)).setPosition(507, int(pos_Y))

                                     if nextprogram1_width == 626:
                                         self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))


                                 elif nextprogram_width == 117:
                                     nextprogram_width = 102
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 102:
                                         self.getControl(int(nextprogram1)).setPosition(549, int(pos_Y))

                                         if nextprogram1_width == 167:
                                             nextprogram1_width = 170
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 170:
                                                 self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))

                                                 if nextprogram2_width == 342:
                                                     self.getControl(int(nextprogram3)).setPosition(1072, int(pos_Y))


                                                 elif nextprogram2_width >= 515:
                                                     self.getControl(int(nextprogram3)).setPosition(1419, int(pos_Y))


                                         elif nextprogram1_width == 691:
                                             self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))


                                 elif nextprogram_width == 167:
                                     nextprogram_width = 162
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 162:
                                         self.getControl(int(nextprogram1)).setPosition(610, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             nextprogram1_width = 110
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 110:
                                                 self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))


                                         elif nextprogram1_width == 167:
                                             self.getControl(int(nextprogram2)).setPosition(790, int(pos_Y))


                                         elif nextprogram1_width == 626:
                                             nextprogram1_width = 629
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 629:
                                                 self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))


                                 elif nextprogram_width == 227:
                                     nextprogram_width = 211
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 211:
                                         self.getControl(int(nextprogram1)).setPosition(659, int(pos_Y))



                                 elif nextprogram_width == 286:
                                     nextprogram_width = 278
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 278:
                                         self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))

                                         if nextprogram1_width == 344:
                                             nextprogram1_width = 342
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 342:
                                                 self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))



                                 elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                     nextprogram_width = 342
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 342:
                                         self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             nextprogram1_width = 47
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 47:
                                                 self.getControl(int(nextprogram2)).setPosition(844, int(pos_Y))



                                         elif nextprogram1_width == 167:
                                             nextprogram1_width = 162
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 162:
                                                 self.getControl(int(nextprogram2)).setPosition(959, int(pos_Y))
                                         
                                         
                                         
                                         elif nextprogram1_width == 342:
                                             nextprogram1_width = 338

                                             if nextprogram1_width == 338:
                                                 self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))



                                 elif nextprogram_width == 396:
                                     self.getControl(int(nextprogram1)).setPosition(842, int(pos_Y))



                                 elif nextprogram_width == 456:
                                     nextprogram_width = 449
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 449:
                                         self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))



                                 elif nextprogram_width == 567:
                                     nextprogram_width = 562
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 562:
                                         self.getControl(int(nextprogram1)).setPosition(1009, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             nextprogram1_width = 57

                                             if nextprogram1_width == 57:
                                                 self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))




                                 elif nextprogram_width == 626:
                                     nextprogram_width = 625
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 625:
                                         self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))

                                         if nextprogram1_width == 167:
                                             self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                 elif nextprogram_width == 691:
                                     nextprogram_width = 691
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 691:
                                         self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             self.getControl(int(nextprogram2)).setPosition(1204, int(pos_Y))


                                         elif nextprogram1_width == 117:
                                             self.getControl(int(nextprogram2)).setPosition(1262, int(pos_Y))



                                 elif nextprogram_width == 741:
                                     nextprogram_width = 742
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 742:
                                         self.getControl(int(nextprogram1)).setPosition(1189, int(pos_Y))



                 elif program_finished == '10':
                     if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                         if programX == 375 and program_width == 117:
                             programs_width = 125
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 125:
                                 self.getControl(int(nextprogram)).setPosition(507, int(pos_Y))



                         elif programX == 375 and program_width == 167:
                             programs_width = 167
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 167:
                                 self.getControl(int(nextprogram)).setPosition(549, int(pos_Y))

                                 if nextprogram_width == 117:
                                     nextprogram_width = 113
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 113:
                                         self.getControl(int(nextprogram1)).setPosition(669, int(pos_Y))



                         elif programX == 375 and program_width == 227:
                             programs_width = 227
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 227:
                                 self.getControl(int(nextprogram)).setPosition(610, int(pos_Y))

                                 if nextprogram_width == 59:
                                     nextprogram_width = 53
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 53:
                                         self.getControl(int(nextprogram1)).setPosition(669, int(pos_Y))



                         elif programX == 375 and program_width >= 286:
                             programs_width = 117
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 117:
                                 self.getControl(int(nextprogram)).setPosition(498, int(pos_Y))

                                 if nextprogram_width == 59:
                                     self.getControl(int(nextprogram1)).setPosition(564, int(pos_Y))

                                     if nextprogram1_width == 167:
                                         nextprogram1_width = 153
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 153:
                                             self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))


                                 elif nextprogram_width == 117:
                                     self.getControl(int(nextprogram1)).setPosition(621, int(pos_Y))

                                     if nextprogram1_width == 117:
                                         nextprogram1_width = 97
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 97:
                                             self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))



                                 elif nextprogram_width == 286:
                                     nextprogram_width = 282
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 282:
                                         self.getControl(int(nextprogram1)).setPosition(786, int(pos_Y))

                                         if nextprogram1_width == 456:
                                             nextprogram1_width = 454
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 454:
                                                 self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                 elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                     nextprogram_width = 332
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 332:
                                         self.getControl(int(nextprogram1)).setPosition(838, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             nextprograms1_width = 114
                                             self.getControl(int(nextprogram1)).setWidth(nextprograms1_width)

                                             if nextprograms1_width == 114:
                                                 self.getControl(int(nextprogram2)).setPosition(959, int(pos_Y))

                                                 if nextprogram2_width == 117:
                                                     nextprograms2_width = 107
                                                     self.getControl(int(nextprogram2)).setWidth(nextprograms2_width)

                                                     if nextprograms2_width == 107:
                                                         self.getControl(int(nextprogram3)).setPosition(1072, int(pos_Y))


                                         elif nextprogram1_width == 344:
                                             self.getControl(int(nextprogram2)).setPosition(1186, int(pos_Y))



                                 elif nextprogram_width == 396:
                                     nextprogram_width = 393
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 393:
                                         self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))

                                         if nextprogram1_width == 286:
                                             nextprogram1_width = 282
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 282:
                                                 self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))



                                         elif nextprogram_width >= 691:
                                             self.getControl(int(nextprogram2)).setPosition(1419, int(pos_Y))



                                 elif nextprogram_width == 456:
                                     nextprogram_width = 455
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 455:
                                         self.getControl(int(nextprogram1)).setPosition(959, int(pos_Y))

                                         if nextprogram1_width == 167:
                                             nextprogram1_width = 172
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 172:
                                                 self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))

                                                 if nextprogram2_width == 117:
                                                     self.getControl(int(nextprogram3)).setPosition(1262, int(pos_Y))




                                 elif nextprogram_width == 515:
                                     nextprogram_width = 511
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 511:
                                         self.getControl(int(nextprogram1)).setPosition(1016, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             nextprogram1_width = 50
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 50:
                                                 self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))


                                 elif nextprogram_width == 567:
                                     nextprogram_width = 568
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 568:
                                         self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))


                                 elif nextprogram_width == 626:
                                     nextprogram_width = 633
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)
                                     self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))



                                 elif nextprogram_width == 691:
                                     nextprogram_width = 691
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 691:
                                         self.getControl(int(nextprogram1)).setPosition(1196, int(pos_Y))




                     elif program_stop_time > epg_time_3:
                         if programX == 375 and program_width >= 1037:
                             programs_width = 798
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 798:
                                 self.getControl(int(nextprogram)).setPosition(1180, int(pos_Y))



                 elif program_finished == '15':
                     if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                         if programX == 375 and program_width >= 167:
                             programs_width = 167
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 167:
                                 self.getControl(int(nextprogram)).setPosition(549, int(pos_Y))

                                 if nextprogram_width == 59:
                                     nextprogram_width = 54
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 54:
                                         self.getControl(int(nextprogram1)).setPosition(610, int(pos_Y))

                                         if nextprogram1_width == 456:
                                             self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))


                                 elif nextprogram_width == 117:
                                     nextprogram_width = 113
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 113:
                                         self.getControl(int(nextprogram1)).setPosition(669, int(pos_Y))

                                         if nextprogram1_width == 286:
                                             nextprogram1_width = 279
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 279:
                                                 self.getControl(int(nextprogram2)).setPosition(959, int(pos_Y))



                                 elif nextprogram_width == 167:
                                     nextprogram_width = 169
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 169:
                                         self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             nextprogram1_width = 114
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 114:
                                                 self.getControl(int(nextprogram2)).setPosition(844, int(pos_Y))


                                         elif nextprogram1_width == 344:
                                             nextprogram1_width = 342
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 342:
                                                 self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))



                                 elif nextprogram_width == 227:
                                     nextprogram_width = 234
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 234:
                                         self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))

                                         if nextprogram1_width == 286:
                                             nextprogram1_width = 276
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 276:
                                                 self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))



                                         elif nextprogram1_width == 342:
                                             nextprogram1_width = 342
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 342:
                                                 self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))



                                 elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                     nextprogram_width = 342
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 342:
                                         self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             self.getControl(int(nextprogram2)).setPosition(1020, int(pos_Y))


                                         elif nextprogram1_width == 227:
                                             nextprogram1_width = 226
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 226:
                                                 self.getControl(int(nextprogram2)).setPosition(1130, int(pos_Y))



                                         elif nextprogram1_width == 342:
                                             self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                 elif nextprogram_width == 396:
                                     nextprogram_width = 404
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 404:
                                         self.getControl(int(nextprogram1)).setPosition(959, int(pos_Y))

                                         if nextprogram1_width == 167:
                                             nextprogram1_width = 171
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 171:
                                                 self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))



                                         elif nextprogram1_width == 227:
                                             nextprogram1_width = 219
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 219:
                                                 self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))

                                                 if nextprogram2_width == 59:
                                                     nextprogram2_width = 56
                                                     self.getControl(int(nextprogram2)).setWidth(nextprogram2_width)

                                                     if nextprogram2_width == 56:
                                                         self.getControl(int(nextprogram3)).setPosition(1246, int(pos_Y))



                                 elif nextprogram_width == 456:
                                     nextprogram_width = 454
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 454:
                                         self.getControl(int(nextprogram1)).setPosition(1009, int(pos_Y))

                                         if nextprogram1_width == 167:
                                             nextprogram1_width = 169
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 169:
                                                 self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))


                                         elif nextprogram1_width >= 691:
                                             self.getControl(int(nextprogram2)).setPosition(1704, int(pos_Y))



                                 elif nextprogram_width == 515:
                                     nextprogram_width = 517
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 517:
                                         self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))



                                 elif nextprogram_width == 567:
                                     nextprogram_width = 582
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 582:
                                         self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))



                                 elif nextprogram_width == 626:
                                     self.getControl(int(nextprogram1)).setPosition(1182, int(pos_Y))


                                 elif nextprogram_width == 691:
                                     nextprogram_width = 691
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 691:
                                         self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))




                 elif program_finished == '20':
                     print "20 has passed"
                     if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                         if program_width >= 227:
                             programs_width = 228
                             self.getControl(int(program_id)).setWidth(programs_width)
                             print nextprogram_width

                             if programs_width == 228:
                                 self.getControl(int(nextprogram)).setPosition(610, int(pos_Y))

                                 if nextprogram_width == 59:
                                     nextprogram_width = 52
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 52:
                                         self.getControl(int(nextprogram1)).setPosition(669, int(pos_Y))

                                         if nextprogram1_width == 515:
                                             nextprogram1_width = 509
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 509:
                                                 self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))


                                 elif nextprogram_width == 117:
                                     nextprogram_width = 108
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 108:
                                         self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             self.getControl(int(nextprogram2)).setPosition(849, int(pos_Y))


                                         elif nextprogram1_width == 456:
                                             nextprogram1_width = 459
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 459:
                                                 self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))



                                         elif nextprogram1_width == 515:
                                             self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                 elif nextprogram_width == 167:
                                     self.getControl(int(nextprogram1)).setPosition(783, int(pos_Y))



                                 elif nextprogram_width == 227:
                                     nextprogram_width = 221
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 221:
                                         self.getControl(int(nextprogram1)).setPosition(838, int(pos_Y))




                                 elif nextprogram_width == 286:
                                     nextprogram_width = 281
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 281:
                                         self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))

                                         if nextprogram1_width == 167:
                                             nextprogram1_width = 169
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 169:
                                                 self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))

                                                 if nextprogram2_width == 167:
                                                     nextprogram2_width = 164
                                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                     if nextprogram2_width == 164:
                                                         self.getControl(int(nextprogram3)).setPosition(1246, int(pos_Y))



                                 elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                     nextprogram_width = 340
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 340:
                                         self.getControl(int(nextprogram1)).setPosition(959, int(pos_Y))

                                         if nextprogram1_width == 167:
                                             nextprogram1_width == 171
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 171:
                                                 self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))


                                 elif nextprogram_width == 399:
                                     self.getControl(int(nextprogram1)).setPosition(1016, int(pos_Y))


                                 elif nextprogram_width == 456:
                                     self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))


                                 elif nextprogram_width == 515:
                                     nextprogram_width = 502
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 502:
                                         self.getControl(int(nextprogram1)).setPosition(1118, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))


                                 elif nextprogram_width == 516:
                                     nextprogram_width = 502
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 502:
                                         self.getControl(int(nextprogram1)).setPosition(1118, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))


                                 elif nextprogram_width == 567:
                                     nextprogram_width = 568
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 568:
                                         self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))


                                 elif nextprogram_width == 626:
                                     nextprogram_width = 630
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 630:
                                         self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))


                                 elif nextprogram_width == 691:
                                     nextprogram_width = 691

                                     if nextprogram_width == 691:
                                         self.getControl(int(nextprogram1)).setPosition(1308, int(pos_Y))



                         elif programX == 375 and program_width == 227 and nextprogram_width == 117:
                             programs_width = 228
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 228:
                                 self.getControl(int(nextprogram)).setPosition(610, int(pos_Y))

                                 if nextprogram_width == 117:
                                     nextprogram_width = 108
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 108:
                                         self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))


                                         if nextprogram1_width == 456:
                                             nextprogram1_width = 454
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 454:
                                                 self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))



                 elif program_finished == '25':
                     if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                         print "it have change the size here 2a"
                         print "program_width"
                         print program_width
                         print nextprogram_width
                         print program_stop_time

                         if program_width >= 344 and nextprogram_width >= 117:
                             print "here channel 4 now chris"
                             programs_width = 277
                             self.getControl(int(program_id)).setWidth(programs_width)
                             print "you are here 1"

                             if programs_width == 277:
                                 self.getControl(int(nextprogram)).setPosition(659, int(pos_Y))

                                 if nextprogram_width == 59:
                                     self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))

                                     if nextprogram1_width == 344:
                                         nextprogram1_width = 342
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 342:
                                             self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))


                                 elif nextprogram_width == 117:
                                     nextprogram_width = 124
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 124:
                                         self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             nextprogram1_width = 101
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 101:
                                                 self.getControl(int(nextprogram2)).setPosition(897, int(pos_Y))



                                 elif nextprogram_width == 167:
                                     nextprogram_width = 182
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 182:
                                         self.getControl(int(nextprogram1)).setPosition(849, int(pos_Y))

                                         if nextprogram1_width == 227:
                                             nextprogram1_width = 219
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)
                                             self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))



                                 elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                     nextprogram_width = 343
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 343:
                                         self.getControl(int(nextprogram1)).setPosition(1009, int(pos_Y))

                                         if nextprogram1_width == 167:
                                             nextprogram1_width = 169
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 169:
                                                 self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))



                                 elif nextprogram_width >= 390 and nextprogram_width <= 396:
                                     nextprogram_width = 406
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 406:
                                         self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))



                                 elif nextprogram_width == 515:
                                     nextprogram_width = 520
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 520:
                                         self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))



                                 elif nextprogram_width == 567:
                                     nextprogram_width = 572
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 572:
                                         self.getControl(int(nextprogram1)).setPosition(1238, int(pos_Y))



                                 elif nextprogram_width >= 691:
                                     self.getControl(int(nextprogram1)).setPosition(1419, int(pos_Y))



                         elif program_width == 285 and nextprogram_width == 227:
                             programs_width = 277
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 277:
                                 self.getControl(int(nextprogram)).setPosition(659, int(pos_Y))

                                 if nextprogram_width == 59:
                                     self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))

                                     if nextprogram1_width == 344:
                                         nextprogram1_width = 342
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 342:
                                             self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))


                                 elif nextprogram_width == 167:
                                     self.getControl(int(nextprogram1)).setPosition(830, int(pos_Y))

 
                                 elif nextprogram_width == 227:
                                     self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))


                                 elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                     self.getControl(int(nextprogram1)).setPosition(1009, int(pos_Y))


                                 elif nextprogram_width == 456:
                                     self.getControl(int(nextprogram1)).setPosition(1124, int(pos_Y))


                                 elif nextprogram_width == 516:
                                     self.getControl(int(nextprogram1)).setPosition(1179, int(pos_Y))


                                 elif nextprogram_width == 567:
                                     nextprogram_width = 677
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 577:
                                         self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))


                                 elif nextprogram_width == 626:
                                     self.getControl(int(nextprogram1)).setPosition(1289, int(pos_Y))


                                 elif nextprogram_width >= 691:
                                     self.getControl(int(nextprogram1)).setPosition(1354, int(pos_Y))



                         elif program_width >= 285 and program_width <= 287 and nextprogram_width <= 227:
                             programs_width = 277
                             self.getControl(int(program_id)).setWidth(programs_width)
                             print "you are here 2......................................................"

                             if programs_width == 277:
                                 self.getControl(int(nextprogram)).setPosition(659, int(pos_Y))

                                 if nextprogram_width == 59:
                                     self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))

                                     if nextprogram1_width == 342:
                                         self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))


                                 elif nextprogram_width == 167:
                                     self.getControl(int(nextprogram1)).setPosition(830, int(pos_Y))


                                 elif nextprogram_width == 227:
                                     nextprogram_width = 234
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 234:
                                         self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))


                                 elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                     self.getControl(int(nextprogram1)).setPosition(1009, int(pos_Y))


                                 elif nextprogram_width == 456:
                                     self.getControl(int(nextprogram1)).setPosition(1124, int(pos_Y))


                                 elif nextprogram_width == 516:
                                     self.getControl(int(nextprogram1)).setPosition(1179, int(pos_Y))


                                 elif nextprogram_width == 567:
                                     nextprogram_width = 677
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 577:
                                         self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))


                                 elif nextprogram_width == 626:
                                     self.getControl(int(nextprogram1)).setPosition(1289, int(pos_Y))


                                 elif nextprogram_width >= 691:
                                     self.getControl(int(nextprogram1)).setPosition(1354, int(pos_Y))




                         elif program_width >= 285 and program_width <= 287 and nextprogram_width == 117:
                             programs_width = 275
                             self.getControl(int(program_id)).setWidth(programs_width)
                             print "you are here 32......................................................"

                             if programs_width == 275:
                                 self.getControl(int(nextprogram)).setPosition(659, int(pos_Y))

                                 if nextprogram_width == 59:
                                     self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))

                                     if nextprogram1_width == 344:
                                         nextprogram1_width = 342
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 342:
                                             self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))


                                 elif nextprogram_width == 117:
                                     nextprogram_width = 124
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)
                                     self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))



                                 elif nextprogram_width == 167:
                                     self.getControl(int(nextprogram1)).setPosition(830, int(pos_Y))


                                 elif nextprogram_width == 227:
                                     nextprogram_width = 234
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 234:
                                         self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))


                                 elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                     self.getControl(int(nextprogram1)).setPosition(1009, int(pos_Y))


                                 elif nextprogram_width == 456:
                                     self.getControl(int(nextprogram1)).setPosition(1124, int(pos_Y))


                                 elif nextprogram_width == 516:
                                     self.getControl(int(nextprogram1)).setPosition(1179, int(pos_Y))


                                 elif nextprogram_width == 567:
                                     nextprogram_width = 677
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 577:
                                         self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))


                                 elif nextprogram_width == 626:
                                     self.getControl(int(nextprogram1)).setPosition(1289, int(pos_Y))


                                 elif nextprogram_width >= 691:
                                     self.getControl(int(nextprogram1)).setPosition(1354, int(pos_Y))




                 elif program_finished == '30':
                     if program_stop_time == epg_time_3:
                         if programX == 375 and program_width >= 1038:
                             programs_width = 691
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 691:
                                 self.getControl(int(nextprogram)).setPosition(1072, int(pos_Y))



                 elif program_finished == '35':
                     if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                         if int(current_time) >= 0 and int(current_time) < 29:
                             if programX == 375 and program_width >= 741:
                                 print "you are here 1"
                                 programs_width = 408
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 408:
                                     self.getControl(int(nextprogram)).setPosition(790, int(pos_Y))

                                     if nextprogram_width == 286:
                                         self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))



                         elif int(current_time) >= 30 and int(current_time) < 59:
                             if programX == 375 and program_width >= 117:
                                 print "you are here 2c"
                                 programs_width = 59
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 59:
                                     self.getControl(int(nextprogram)).setPosition(441, int(pos_Y))

                                     if nextprogram_width == 59:
                                         self.getControl(int(nextprogram1)).setPosition(507, int(pos_Y))

                                         if nextprogram1_width == 626:
                                             nextprogram1_width = 624
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 624:
                                                 self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))


                                     elif nextprogram_width == 117:
                                         nextprogram_width = 101
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 101:
                                             self.getControl(int(nextprogram1)).setPosition(549, int(pos_Y))

                                             if nextprogram1_width == 117:
                                                 self.getControl(int(nextprogram2)).setPosition(674, int(pos_Y))

                                                 if nextprogram2_width == 567:
                                                     nextprogram2_width = 565
                                                     self.getControl(int(nextprogram2)).setWidth(nextprogram2_width)

                                                     if nextprogram2_width == 565:
                                                         self.getControl(int(nextprogram3)).setPosition(1246, int(pos_Y))


                                             elif nextprogram1_width == 167:
                                                 nextprogram1_width = 169
                                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                 if nextprogram1_width == 169:
                                                     self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))


                                             elif nextprogram1_width == 691:
                                                 nextprogram1_width = 691
                                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                 if nextprogram1_width == 691:
                                                     self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                     elif nextprogram_width == 167:
                                         nextprogram_width = 162
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 162:
                                             self.getControl(int(nextprogram1)).setPosition(610, int(pos_Y))

                                             if nextprogram1_width == 117:
                                                 nextprogram1_width = 109
                                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                 if nextprogram1_width == 109:
                                                     self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))



                                     elif nextprogram_width == 286:
                                         nextprogram_width = 277
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 277:
                                             self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))



                                     elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                         nextprogram_width = 336
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 336:
                                             self.getControl(int(nextprogram1)).setPosition(783, int(pos_Y))



                                     elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                         nextprogram_width = 336
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 336:
                                             self.getControl(int(nextprogram1)).setPosition(783, int(pos_Y))

                                             if nextprogram1_width == 59:
                                                 self.getControl(int(nextprogram2)).setPosition(856, int(pos_Y))


                                             elif nextprogram1_width == 344:
                                                 nextprogram1_width = 344
                                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                 if nextprogram1_width == 344:
                                                     self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))



                                     elif nextprogram_width == 396:
                                         nextprogram_width = 390
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 390:
                                             self.getControl(int(nextprogram1)).setPosition(838, int(pos_Y))

                                             if nextprogram1_width == 396:
                                                 nextprogram1_width = 393
                                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                 if nextprogram1_width == 393:
                                                     self.getControl(int(nextprogram2)).setPosition(1238, int(pos_Y))



                                     elif nextprogram_width == 456:
                                         nextprogram_width = 450
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 450:
                                             self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))



                                     elif nextprogram_width == 515:
                                         nextprogram_width = 513
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 513:
                                             self.getControl(int(nextprogram1)).setPosition(959, int(pos_Y))



                                     elif nextprogram_width == 567:
                                         nextprogram_width = 568
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 568:
                                             self.getControl(int(nextprogram1)).setPosition(1016, int(pos_Y))



                                     elif nextprogram_width == 626:
                                         nextprogram_width = 625
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 625:
                                             self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))

                                             if nextprogram1_width == 167:
                                                 self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))


                                     elif nextprogram_width == 691:
                                         nextprogram_width = 691
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 691:
                                             self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))



                                     elif nextprogram_width == 741:
                                         nextprogram_width = 738
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 738:
                                             self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))

                                             if nextprogram1_width == 59:
                                                 nextprogram1_width = 57
                                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                 if nextprogram1_width == 57:
                                                     self.getControl(int(nextprogram1)).setPosition(1146, int(pos_Y))




                     elif program_stop_time > epg_time_3:
                         if programX == 375 and program_width >= 741:
                             programs_width = 750
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 750:
                                 self.getControl(int(nextprogram)).setPosition(1132, int(pos_Y))




                 elif program_finished == '40':
                     if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                         if programX == 375 and program_width == 59:
                             print "passed 2a"
                             if program_width == 59 and nextprogram_width == 227:
                                 print "nextprogram1X"
                                 print nextprogram1X
                                 self.nextprogram_id = list()
                                 self.nextprogram_id.append(nextprogram)
                                 self.select_db_flag = True
                                 self.select_db()
                                 nextprogram_clock = ''.join(str(x) for x in self.nextprogram_clock)
                                 nextprogram_clock = str(nextprogram_clock)
                                 nextprogram_stop_clock = ''.join(str(x) for x in self.nextprogram_stop_clock)
                                 nextprogram_stop_clock = str(nextprogram_stop_clock)
                                 program_stop_time = time.strptime(nextprogram_clock, '%d/%m/%Y %I:%M%p')
                                 print "program_stop_time"
                                 print program_stop_time


                                 if program_stop_time == epg_time_2:
                                     if nextprogram1X == 675:
                                         nextprogram_width = 276
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 276:
                                             self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))


                         #DO NOT CHANGE IT
                         elif programX == 375 and program_width >= 59:
                             programs_width = 125
                             self.getControl(int(program_id)).setWidth(programs_width)
                             print "program changed to 125 passed 1"

                             if programs_width == 125:
                                 self.getControl(int(nextprogram)).setPosition(507, int(pos_Y))
                                 print "program changed to 125 passed 2"
                                 print nextprogram_width

                                 if nextprogram_width == 59:
                                     self.getControl(int(nextprogram1)).setPosition(573, int(pos_Y))

                                     if nextprogram1_width == 342:
                                         nextprogram1_width = 318
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 318:
                                             self.getControl(int(nextprogram2)).setPosition(897, int(pos_Y))



                                     elif nextprogram1_width == 396:
                                         nextprogram1_width = 399
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 399:
                                             self.getControl(int(nextprogram2)).setPosition(978, int(pos_Y))


                                 elif nextprogram_width == 117 and nextprogram1_width == 117:
                                     nextprogram_width = 108
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 108:
                                         self.getControl(int(nextprogram1)).setPosition(621, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             nextprogram1_width = 97
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 97:
                                                 self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))



                                 elif nextprogram_width == 117:
                                     nextprogram_width = self.getControl(int(nextprogram)).getWidth()

                                     if nextprogram_width == 567:
                                         nextprogram_width = 563
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 563:
                                             self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))

                                             if nextprogram1_width == 117:
                                                 nextprogram1_width = 100
                                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                 if nextprogram1_width == 100:
                                                     self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))



                                 elif nextprogram_width == 167:
                                     nextprogram_width = 147
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 147:
                                         self.getControl(int(nextprogram1)).setPosition(659, int(pos_Y))



                                 elif nextprogram_width == 227:
                                     nextprogram_width = 211
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 211:
                                         self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))

                                         if nextprogram1_width == 342:
                                             self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))



                                 elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                     self.getControl(int(nextprogram1)).setPosition(856, int(pos_Y))

                                     if nextprogram1_width == 344:
                                         nextprogram1_width = 332
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 332:
                                             self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))


                                 elif nextprogram_width >= 390 and nextprogram_width <= 400:
                                     nextprogram_width = 384
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 384:
                                         self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))

                                         if nextprogram1_width == 167:
                                             nextprogram1_width = 168
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 168:
                                                 self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))

                                                 if nextprogram2_width == 117:
                                                     nextprogram2_width = 107
                                                     self.getControl(int(nextprogram2)).setWidth(nextprogram2_width)

                                                     if nextprogram2_width == 107:
                                                         self.getControl(int(nextprogram3)).setPosition(1184, int(pos_Y))


                                         elif nextprogram1_width == 344:
                                             nextprogram1_width = 332
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 332:
                                                 self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))




                                 elif nextprogram_width == 515:
                                     self.getControl(int(nextprogram1)).setPosition(1020, int(pos_Y))


                                 elif nextprogram_width == 567:
                                     print "you are in the 563!"
                                     nextprogram_width = 559
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 559:
                                         self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             nextprogram1_width = 100
                                             self.getControl(int(nextprogram)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 100:
                                                 self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))



                                 elif nextprogram_width == 626:
                                     nextprogram_width = 625
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 625:
                                         self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             self.getControl(int(nextprogram2)).setPosition(1263, int(pos_Y))



                                 elif nextprogram_width == 691:
                                     nextprogram_width = 672
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 672:
                                         self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             nextprograms1_width = 56
                                             self.getControl(int(nextprogram1)).setWidth(nextprograms1_width)

                                             if nextprograms1_width == 56:
                                                 self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                 elif nextprogram_width == 741:
                                     nextprogram_width = 733
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 733:
                                         self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))



                 elif program_finished == '45':
                     print "hello chrisa"
                     if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                         if programX == 375 and program_width >= 167:
                             programs_width = 167
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 167:
                                 self.getControl(int(nextprogram)).setPosition(549, int(pos_Y))
                                 nextprogram_width = self.getControl(int(nextprogram)).getWidth()

                                 if nextprogram_width == 59:
                                     nextprogram_width = 54
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 54:
                                         self.getControl(int(nextprogram1)).setPosition(610, int(pos_Y))



                                 elif nextprogram_width == 167:
                                     nextprogram_width = 169
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 169:
                                         self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))



                                 elif nextprogram_width == 227:
                                     nextprogram_width = 234
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 234:
                                         self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             nextprograms1_width = 101
                                             self.getControl(int(nextprogram1)).setWidth(nextprograms1_width)

                                             if nextprograms1_width == 101:
                                                 self.getControl(int(nextprogram2)).setPosition(897, int(pos_Y))


                                 elif nextprogram_width == 286:
                                     nextprogram_width = 282
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 282:
                                         self.getControl(int(nextprogram1)).setPosition(838, int(pos_Y))

                                         if nextprogram1_width == 286:
                                             nextprogram1_width = 280
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 280:
                                                 self.getControl(int(nextprogram2)).setPosition(1125, int(pos_Y))


                                         elif nextprogram1_width == 342:
                                             nextprogram1_width = 340
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 340:
                                                 self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))

                                                 if nextprogram2_width == 59:
                                                     nextprogram2_width = 55
                                                     self.getControl(int(nextprogram2)).setWidth(nextprogram2_width)

                                                     if nextprogram2_width == 55:
                                                         self.getControl(int(nextprogram3)).setPosition(1246, int(pos_Y))



                                 elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                     nextprogram_width = 342
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 342:
                                         self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             nextprogram1_width = 56
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 56:
                                                 self.getControl(int(nextprogram2)).setPosition(959, int(pos_Y))



                                         elif nextprogram1_width == 117:
                                             self.getControl(int(nextprogram2)).setPosition(1020, int(pos_Y))


                                         elif nextprogram1_width == 227:
                                             nextprogram1_width = 226
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 226:
                                                 self.getControl(int(nextprogram2)).setPosition(1130, int(pos_Y))



                                         elif nextprogram1_width >= 342 and nextprogram1_width <= 344:
                                             nextprogram1_width = 342
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 342:
                                                 self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                 elif nextprogram_width == 396:
                                     nextprogram_width = 404
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 404:
                                         self.getControl(int(nextprogram1)).setPosition(959, int(pos_Y))

                                         if nextprogram1_width == 167:
                                             nextprogram1_width = 171
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 171:
                                                 self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))



                                 elif nextprogram_width == 456:
                                     nextprogram_width = 454
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 454:
                                         self.getControl(int(nextprogram1)).setPosition(1009, int(pos_Y))



                                 elif nextprogram_width == 515:
                                     nextprogram_width = 517
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 517:
                                         self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))



                                         elif nextprogram1_width == 167:
                                             self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                 elif nextprogram_width == 567:
                                     nextprogram_width = 569
                                     self.getControl(int(nextprogram)).setWidth(int(nextprogram_width))

                                     if nextprogram_width == 569:
                                         self.getControl(int(nextprogram1)).setPosition(1125, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             nextprogram1_width = 54
                                             self.getControl(int(nextprogram1)).setWidth(int(nextprogram1_width))

                                             if nextprogram1_width == 54:
                                                 self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))


                                         #elif nextprogram1_width == 117:
                                             #self.getControl(int(nextprogram2)).setPosition(1263, int(pos_Y))



                                 elif nextprogram_width == 626:
                                     nextprogram_width = 630
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 630:
                                         self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             nextprogram1_width = 55
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 55:
                                                 self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                 elif nextprogram_width == 691:
                                     nextprogram_width = 691
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 691:
                                         self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))



                                 elif nextprogram_width >= 741:
                                     self.getControl(int(nextprogram1)).setPosition(1419, int(pos_Y))




                     elif program_stop_time > epg_time_2 and program_stop_time < epg_time_3:
                         if programX == 375 and program_width >= 342:
                             programs_width = 516
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 516:
                                 self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))

                             elif nextprogram_width == 515:
                                 nextprogram_width = 516
                                 self.getControl(int(nextprogram)).setWidth(programs_width)

                                 if nextprogram_width == 516:
                                     self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))



                     elif program_stop_time == epg_time_3:
                         if programX == 375 and program_width >= 691:
                             programs_width = 691
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 691:
                                 self.getControl(int(nextprogram)).setPosition(1072, int(pos_Y))



                 elif program_finished == '50':
                     print "50 has passed"
                     if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                         if program_width >= 227:
                             programs_width = 228
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 228:
                                 self.getControl(int(nextprogram)).setPosition(610, int(pos_Y))

                                 if nextprogram_width == 59:
                                     nextprogram_width = 51
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 51:
                                         self.getControl(int(nextprogram1)).setPosition(669, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             nextprogram1_width = 50
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 50:
                                                 self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))

                                                 if nextprogram2_width == 167:
                                                     self.getControl(int(nextprogram3)).setPosition(897, int(pos_Y))



                                 elif nextprogram_width == 117:
                                     nextprogram_width = 114
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 114:
                                         self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             nextprogram1_width = 114
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 114:
                                                 self.getControl(int(nextprogram2)).setPosition(849, int(pos_Y))



                                 elif nextprogram_width == 167:
                                     self.getControl(int(nextprogram1)).setPosition(783, int(pos_Y))

                                     if nextprogram1_width == 117:
                                         nextprogram1_width = 108
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 108:
                                             self.getControl(int(nextprogram2)).setPosition(897, int(pos_Y))

                                             if nextprogram2_width == 167:
                                                 nextprogram2_width = 160
                                                 self.getControl(int(nextprogram2)).setWidth(nextprogram2_width)

                                                 #if nextprogram2_width == 160:
                                                     #self.getControl(int(nextprogram3)).setPosition(1072, int(pos_Y))



                                 elif nextprogram_width == 227:
                                     nextprogram_width = 221
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 221:
                                         self.getControl(int(nextprogram1)).setPosition(838, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             nextprogram1_width = 53
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 53:
                                                 self.getControl(int(nextprogram2)).setPosition(897, int(pos_Y))



                                 elif nextprogram_width == 286:
                                     nextprogram_width = 281
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 281:
                                         self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))



                                 elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                     nextprogram_width = 343
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)
                                     print "you are in the 343 1"

                                     if nextprogram_width == 343:
                                         self.getControl(int(nextprogram1)).setPosition(959, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             self.getControl(int(nextprogram2)).setPosition(1025, int(pos_Y))



                                         elif nextprogram1_width == 117:
                                             nextprogram1_width = 112
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 112:
                                                 self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))


                                         elif nextprogram1_width == 167:
                                             nextprogram1_width = 171
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 171:
                                                 self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))


                                 elif nextprogram_width == 399:
                                     self.getControl(int(nextprogram1)).setPosition(1016, int(pos_Y))


                                 elif nextprogram_width == 456:
                                     self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))


                                 elif nextprogram_width == 515:
                                     nextprogram_width = 502
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 502:
                                         self.getControl(int(nextprogram1)).setPosition(1118, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))


                                 elif nextprogram_width == 516:
                                     nextprogram_width = 502
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 502:
                                         self.getControl(int(nextprogram1)).setPosition(1118, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))


                                 elif nextprogram_width == 567:
                                     nextprogram_width = 569
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 569:
                                         self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))


                                 elif nextprogram_width == 626:
                                     self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))


                                 elif nextprogram_width == 691:
                                     nextprogram_width = 691

                                     if nextprogram_width == 691:
                                         self.getControl(int(nextprogram1)).setPosition(1308, int(pos_Y))



                         elif programX == 375 and program_width == 227 and nextprogram_width == 117:
                             programs_width = 224
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 224:
                                 self.getControl(int(nextprogram)).setPosition(606, int(pos_Y))

                                 if nextprogram_width == 117:
                                     programs_width = 111
                                     self.getControl(int(nextprogram)).setWidth(programs_width)
                                     self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))


                                     if nextprogram1_width == 456:
                                         nextprogram1_width = 454
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 454:
                                             self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))



                 elif program_finished == '55':
                     if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                         if int(current_time) >= 00 and int(current_time) < 29:
                             if programX == 375 and program_width >= 286:

                                 if nextprogram_width == 59:
                                     programs_width = 277
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 277:
                                         self.getControl(int(nextprogram)).setPosition(659, int(pos_Y))

                                         if nextprogram1X >= 1072:
                                             self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))


                                     else:
                                         programs_width = 283
                                         self.getControl(int(program_id)).setWidth(programs_width)

                                         if programs_width == 283:
                                             self.getControl(int(nextprogram)).setPosition(664, int(pos_Y))



                         else:
                             print "you need to fix the button size that are 286 or more with the next program 5 mins 1"
                             print "program_width"
                             print program_width

                             if programX == 375 and program_width >= 286:
                                 programs_width = 277
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if nextprogram_width == 59:
                                     nextprogram_width = 59
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 59:
                                         self.getControl(int(nextprogram)).setPosition(659, int(pos_Y))

                                         if nextprogram1X != 724:
                                             self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))

                                             if nextprogram1_width == 286:
                                                 self.getControl(int(nextprogram2)).setPosition(1018, int(pos_Y))

                                                 if nextprogram2_width == 227:
                                                     self.getControl(int(nextprogram3)).setPosition(1251, int(pos_Y))


                                             elif nextprogram1_width == 344:
                                                 nextprogram1_width = 342
                                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                 if nextprogram1_width == 342:
                                                     self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))


                                             elif nextprogram1_width == 515:
                                                 nextprogram1_width = 516
                                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                 if nextprogram1_width == 516:
                                                     self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                 elif nextprogram_width > 59:
                                     self.getControl(int(nextprogram)).setPosition(659, int(pos_Y))

                                     if nextprogram_width == 167:
                                         nextprogram_width = 172
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 172:
                                             self.getControl(int(nextprogram1)).setPosition(838, int(pos_Y))

                                             if nextprogram1_width == 344:
                                                 self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))


                                     elif nextprogram_width == 227:
                                         nextprogram_width = 232
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 232:
                                             self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))



                                     elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                         nextprogram_width = 344
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 344:
                                             self.getControl(int(nextprogram1)).setPosition(1009, int(pos_Y))


                                     elif nextprogram_width >= 380 and nextprogram_width <= 408:
                                         nextprogram_width = 406
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 406:
                                             self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))


                                     elif nextprogram_width == 456:
                                         self.getControl(int(nextprogram1)).setPosition(1124, int(pos_Y))


                                     elif nextprogram_width == 515:
                                         self.getControl(int(nextprogram1)).setPosition(1180, int(pos_Y))


                                     elif nextprogram_width == 567:
                                         self.getControl(int(nextprogram1)).setPosition(1233, int(pos_Y))




             elif program_stop_time > epg_time_2 and program_stop_time < epg_time_3:
                 print "here 4a"
                 print program_finished

                 if program_finished == '00':
                     if programX == 375 and program_width == 342:
                         programs_width = 342
                         self.getControl(int(program_id)).setWidth(programs_width)

                         if programs_width == 342:
                             self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))



                 elif program_finished == '05':
                     print "you are in 4:05 now 1"
                     print "program_width"
                     print program_width

                     if programX == 375 and program_width >= 396:
                         programs_width = 408
                         self.getControl(int(program_id)).setWidth(programs_width)
                         print "you are in 4:05 now 2"

                         if programs_width == 408 and nextprogram_width == 344:
                             print "you are in the programs_width and nextprogram_width"
                             nextprogram_width = 342
                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)
                             self.getControl(int(nextprogram)).setPosition(790, int(pos_Y))

                             if nextprogram_width == 342:
                                 self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))



                         elif programs_width == 408:
                             self.getControl(int(nextprogram)).setPosition(790, int(pos_Y))

                             if nextprogram_width == 59:
                                 nextprogram_width = 42
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 42:
                                     self.getControl(int(nextprogram1)).setPosition(838, int(pos_Y))

                                     if nextprogram1_width == 117:
                                         nextprograms1_width = 114
                                         self.getControl(int(nextprogram1)).setWidth(nextprograms1_width)

                                         if nextprograms1_width == 114:
                                             self.getControl(int(nextprogram2)).setPosition(959, int(pos_Y))



                             elif nextprogram_width == 117:
                                 nextprogram_width = 110
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 110:
                                     self.getControl(int(nextprogram1)).setPosition(907, int(pos_Y))

                                     if nextprogram1_width == 167:
                                         nextprogram1_width = 159
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 159:
                                             self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))


                             elif nextprogram_width == 167:
                                 nextprogram_width = 171
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if int(nextprogram_width) == 171:
                                     self.getControl(int(nextprogram1)).setPosition(959, int(pos_Y))

                                     if nextprogram1_width == 117:
                                         self.getControl(int(nextprogram2)).setPosition(1136, int(pos_Y))


                                     elif nextprogram1_width == 167:
                                         self.getControl(int(nextprogram2)).setPosition(1128, int(pos_Y))


                             elif nextprogram_width == 227:
                                 self.getControl(int(nextprogram1)).setPosition(1023, int(pos_Y))



                             elif nextprogram_width == 286:
                                 nextprogram_width = 276
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 276:
                                     self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))



                             elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                 self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))

                                 if nextprogram1_width == 59:
                                     self.getControl(int(nextprogram2)).setPosition(1204, int(pos_Y))



                             elif nextprogram_width == 396:
                                 nextprogram_width = 392
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 392:
                                     self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))



                 elif program_finished == '10':
                     if programX == 375 and program_width >= 227:
                         programs_width = 456
                         self.getControl(int(program_id)).setWidth(programs_width)
                         print "itv code here"

                         if programs_width == 456:
                             self.getControl(int(nextprogram)).setPosition(838, int(pos_Y))

                             if nextprogram_width == 59:
                                 nextprogram_width = 54
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 54:
                                     self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))

                                     if nextprogram1_width == 167:
                                         nextprogram1_width = 169
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 169:
                                             self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))


                             elif nextprogram_width == 117:
                                 self.getControl(int(nextprogram1)).setPosition(959, int(pos_Y))

                                 if nextprogram1_width == 117:
                                     nextprogram1_width = 107
                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                     if nextprogram1_width == 107:
                                         self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))



                             elif nextprogram_width == 286:
                                 nextprogram_width = 284
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 284:
                                     self.getControl(int(nextprogram1)).setPosition(1127, int(pos_Y))



                             elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                 nextprogram_width = 341
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 341:
                                     self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))



                             elif nextprogram_width == 396:
                                 nextprogram_width = 401
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 401:
                                     self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))



                 elif program_finished == '15':
                     print "you are in the 15 mins now chris"
                     if programX == 375 and program_width >= 515:
                         programs_width = 516
                         self.getControl(int(program_id)).setWidth(programs_width)

                         if programs_width == 516:
                             self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))

                             if nextprogram_width == 59:
                                 nextprogram_width = 56
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 56:
                                     self.getControl(int(nextprogram1)).setPosition(959, int(pos_Y))


                             elif nextprogram_width == 117:
                                 nextprogram_width = 118
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 118:
                                     self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))


                             elif nextprogram_width == 227:
                                 nextprogram_width = 234
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 234:
                                     self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))



                             elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                 nextprogram_width = 343
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)
                                 print "you are in the 343 2"

                                 if nextprogram_width == 343:
                                     self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))



                 elif program_finished == '20':
                     if program_width == 515:
                         programs_width = 516
                         self.getControl(int(program_id)).setWidth(programs_width)



                     elif programX == 375 and program_width >= 626:
                         programs_width = 577
                         self.getControl(int(program_id)).setWidth(programs_width)

                         if programs_width == 577:
                             self.getControl(int(nextprogram)).setPosition(959, int(pos_Y))

                             if nextprogram_width == 59:
                                 self.getControl(int(nextprogram1)).setPosition(1025, int(pos_Y))


                             elif nextprogram_width == 117:
                                 nextprogram_width = 108
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 108:
                                     self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))



                             elif nextprogram_width == 227:
                                 nextprogram_width = 221
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 221:
                                     self.getControl(int(nextprogram1)).setPosition(1186, int(pos_Y))



                             elif nextprogram_width == 286:
                                 nextprogram_width = 282
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 282:
                                     self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))



                 elif program_finished == '25':
                     if programX == 375 and program_width >= 625:
                         programs_width = 627
                         self.getControl(int(program_id)).setWidth(programs_width)

                         if programs_width == 627 and nextprogram_width == 59:
                             programs_width = 627
                             self.getControl(int(program_id)).setWidth(programs_width)
                             print "here 1 for 25 a"

                             if programs_width == 627:
                                 self.getControl(int(nextprogram)).setPosition(1009, int(pos_Y))
                                 print "here 1 for 25 b"

                                 if nextprogram_width == 59:
                                     nextprogram_width = 57
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 57:
                                         self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))


                         elif programs_width == 627 and nextprogram_width == 59:
                             self.getControl(int(nextprogram)).setPosition(1023, int(pos_Y))

                             if nextprogram_width == 59:
                                 nextprogram_width = 42
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 42:
                                     self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))



                         elif nextprogramX != 1009:
                             self.getControl(int(nextprogram)).setPosition(1009, int(pos_Y))

                             if nextprogram_width == 59:
                                 nextprogram_width = 55
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 55:
                                     self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))


                             elif nextprogram_width == 117:
                                 nextprogram_width = 115
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 115:
                                     self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))

                                     if nextprogram1_width == 117:
                                         nextprogram1_width = 102
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 102:
                                              self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))


                             elif nextprogram_width == 167:
                                 self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))


                             elif nextprogram_width == 227:
                                 self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))


                             elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                 self.getControl(int(nextprogram1)).setPosition(1355, int(pos_Y))



                 elif program_finished == '30':
                     if programX == 375 and program_width >= 1038:
                         programs_width = 342
                         self.getControl(int(program_id)).setWidth(programs_width)



                 elif program_finished == '35':
                     if programX == 375 and program_width >= 396:
                         print "you are under 396 2"
                         programs_width = 408
                         self.getControl(int(program_id)).setWidth(programs_width)

                         if programs_width == 408:
                             self.getControl(int(nextprogram)).setPosition(790, int(pos_Y))

                             if nextprogram_width == 59:
                                 nextprogram_width = 42
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 42:
                                     self.getControl(int(nextprogram1)).setPosition(838, int(pos_Y))


                             if program_width == 396 and nextprogram_width == 117:
                                 nextprogram_width = 113
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 113:
                                     self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))


                             elif nextprogram_width == 117:
                                 self.getControl(int(nextprogram1)).setPosition(913, int(pos_Y))

                                 if nextprogram1_width == 117:
                                     self.getControl(int(nextprogram2)).setPosition(1036, int(pos_Y))


                                 elif nextprogram1_width == 167:
                                     nextprogram1_width = 153
                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                     if nextprogram1_width == 153:
                                         self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))


                             elif nextprogram_width == 167:
                                 if nextprogram_width == 167 and nextprogram1_width == 117:
                                     self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))
                                 else:
                                     nextprogram_width = 171
                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                     if nextprogram_width == 171:
                                         self.getControl(int(nextprogram1)).setPosition(959, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             nextprogram1_width = 111
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 111:
                                                 self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))



                             elif nextprogram_width == 286:
                                 nextprogram_width = 276
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)


                                 if nextprogram_width == 276:
                                     self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))


                             elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                 nextprogram_width = 342
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)


                                 if nextprogram_width == 342:
                                     self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))



                             elif nextprogram_width == 270:
                                 nextprogram_width = 277
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)


                                 if nextprogram_width == 277:
                                     self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))



                 elif program_finished == '40':
                     if programX == 375 and program_width >= 691:
                         programs_width = 456
                         self.getControl(int(program_id)).setWidth(programs_width)

                         if programs_width == 456:
                             self.getControl(int(nextprogram)).setPosition(838, int(pos_Y))

                             if nextprogram_width == 59:
                                 programs_width = 456
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 456:
                                     self.getControl(int(nextprogram)).setPosition(838, int(pos_Y))

                                     if nextprogram_width == 59:
                                         nextprogram_width = 53
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 53:
                                             self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))

                                             if nextprogram1_width == 342:
                                                 self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                             elif nextprogram_width == 117:
                                 nextprogram_width = 115
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 115:
                                     self.getControl(int(nextprogram1)).setPosition(959, int(pos_Y))

                                     if nextprogram1_width == 117:
                                         nextprogram1_width = 107
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 107:
                                             self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))



                             elif nextprogram_width == 227:
                                 nextprogram_width = 228
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 228:
                                     self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))
                                     print "passed 3"



                             elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                 nextprogram_width = 343
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)
                                 print "you are in the 343 4"

                                 if nextprogram_width == 343:
                                     self.getControl(int(nextprogram1)).setPosition(1186, int(pos_Y))



                             elif nextprogram_width >= 390 and nextprogram_width <= 400:
                                 nextprogram_width = 393
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)
                                 print "you are in the 393 4"

                                 if nextprogram_width == 393:
                                     self.getControl(int(nextprogram1)).setPosition(1238, int(pos_Y))




                 elif program_finished == '45':
                     if programX == 375 and program_width >= 515:
                         programs_width = 577
                         self.getControl(int(program_id)).setWidth(programs_width)

                         if programs_width == 577:
                             self.getControl(int(nextprogram)).setPosition(959, int(pos_Y))

                             if nextprogram_width == 59:
                                 nextprogram_width = 50
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 50:
                                     self.getControl(int(nextprogram1)).setPosition(1016, int(pos_Y))

                                     if nextprogram1_width == 117:
                                         self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))


                             elif nextprogram_width == 117:
                                 self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))



                             elif nextprogram_width == 167:
                                 self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))



                             elif nextprogram_width == 227:
                                 nextprograms_width = 220
                                 self.getControl(int(nextprogram)).setWidth(nextprograms_width)

                                 if nextprograms_width == 220:
                                     self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))



                             elif nextprogram_width == 286:
                                 nextprograms_width = 280
                                 self.getControl(int(nextprogram)).setWidth(nextprograms_width)

                                 if nextprograms_width == 280:
                                     self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))



                 elif program_finished == '50':
                     if program_width >= 515:
                         programs_width = 577
                         self.getControl(int(program_id)).setWidth(programs_width)

                         if programs_width == 577:
                             self.getControl(int(nextprogram)).setPosition(959, int(pos_Y))

                             if nextprogram_width == 59:
                                 self.getControl(int(nextprogram1)).setPosition(1025, int(pos_Y))

                                 if nextprogram1_width == 59:
                                     nextprogram1_width = 40
                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                     if nextprogram1_width == 40:
                                         self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))



                             if nextprogram_width == 117:
                                 nextprogram_width = 107
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 107:
                                     self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))

                                     if nextprogram1_width >= 342:
                                         self.getControl(int(nextprogram2)).setPosition(1419, int(pos_Y))






                             elif nextprogram_width == 167:
                                 nextprogram_width = 172
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 172:
                                     self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))

                                     if nextprogram1_width == 117:
                                         self.getControl(int(nextprogram2)).setPosition(1262, int(pos_Y))


                             elif nextprogram_width == 286:
                                 self.getControl(int(nextprogram1)).setPosition(1251, int(pos_Y))



                 elif program_finished == '55':
                     print "sort this out chris"

                     if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                         print "you are here now chrissssssss 1"
                         if program_width >= 286:
                             programs_width = 276
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 276:
                                 self.getControl(int(nextprogram)).setPosition(655, int(pos_Y))

                                 if nextprogram_width == 59:
                                     self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))



                     elif program_stop_time > epg_time_2 and program_stop_time < epg_time_3:
                         print "you are here now chrissssssss 2"

                         if programX == 375 and program_width >= 286:
                             print "you are here now chrissssssss"
                             programs_width = 628
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 628:
                                 self.getControl(int(nextprogram)).setPosition(1009, int(pos_Y))

                                 if nextprogram_width == 59:
                                    nextprogram_width = 57
                                    self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                    if nextprogram_width == 57:
                                         self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))

                                         if nextprogram1_width == 344:
                                             self.getControl(int(nextprogram2)).setPosition(1419, int(pos_Y))



             elif program_stop_time == epg_time_3:
                 print "here 5a"
                 print program_finished
                 epg_time3_hour = epg_time_3.tm_hour
                 program_stop_hour = program_stop_time.tm_hour

                 print "epg_time3_hour"
                 print epg_time3_hour
                 print ''
                 print "program_stop_hour"
                 print program_stop_hour


                 if epg_time3_hour == program_stop_hour:
                     print "passed 1"
                     if program_finished == '00':
                         print "passed 2"
                         if programX == 375 and program_width >= 691:
                             programs_width = 691
                             self.getControl(int(program_id)).setWidth(programs_width)
                             print "passed 3"

                             if programs_width == 691:
                                 self.getControl(int(nextprogram)).setPosition(1072, int(pos_Y))
                                 print "passed 4"

                                 if nextprogram_width == 59:
                                     nextprogram_width = 60
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 60:
                                         self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))



                                 elif nextprogram_width == 117:
                                     nextprogram_width = 118
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 118:
                                         self.getControl(int(nextprogram1)).setPosition(1196, int(pos_Y))


                                 elif nextprogram_width == 167:
                                     self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))


                             elif nextprogramX >= 1072:
                                 self.getControl(int(nextprogram)).setPosition(1072, int(pos_Y))

                                 if nextprogram_width == 59:
                                     nextprogram_width = 60
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 60:
                                         self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))



                         elif programX == 375 and program_width >= 626:
                             programs_width = 691
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 691:
                                 self.getControl(int(nextprogram)).setPosition(1072, int(pos_Y))

                                 if nextprogram_width == 59:
                                     self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))


                                 elif nextprogram_width == 117:
                                     self.getControl(int(nextprogram1)).setPosition(1196, int(pos_Y))


                                 elif nextprogram_width == 168:
                                     nextprogram_width = 168
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 168:
                                         self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))


                                 elif nextprogram_width == 167:
                                     self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))



                     elif program_finished == '30':
                         if programX == 375 and program_width == 344:
                             programs_width = 344
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 344:
                                 self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))

                                 if nextprogram_width == 342:
                                     nextprograms_width = 342
                                     self.getControl(int(nextprogram)).setWidth(nextprograms_width)

                                     if nextprograms_width == 342:
                                         self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))



                         elif programX == 375 and program_width >= 515:
                             programs_width = 691
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 691:
                                 self.getControl(int(nextprogram)).setPosition(1072, int(pos_Y))

                                 if nextprogram_width == 59:
                                     self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))

                                 elif nextprogram_width == 117:
                                     nextprogram_width = 100
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 100:
                                         self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))


                                 elif nextprogram_width == 167:
                                     self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))




             elif program_stop_time > epg_time_3:
                 print "here 6b"
                 print program_finished
                 epg_time3 = str(self.getControl(346).getLabel())
                 epg_time3 = epg_time3.split(':')[1].replace('PM', '').replace('AM', '')
                 epg_time3_hour = epg_time_3.tm_hour
                 program_stop_hour = program_stop_time.tm_hour
                 program_width = self.getControl(int(program_id)).getWidth()
                 print "nextprogram_width"
                 print nextprogram_width
                 print program_stop_time

                 if programX == 375 and nextprogramX == 726:
                     if program_width == 344 and nextprogram_width == 344:
                         self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))

                         if nextprogram1X == 1077:
                             self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))


                 elif programX == 375 and nextprogramX == 1123:
                     if program_width == 741:
                         programs_width = 743
                         self.getControl(int(program_id)).setWidth(programs_width)

                         if programs_width == 743:
                             self.getControl(int(nextprogram)).setPosition(1125, int(pos_Y))



                 elif programX == 375 and program_width == 691:
                     print "you are here 100a"

                     if nextprogramX == 1073:
                         self.getControl(int(nextprogram)).setPosition(1072, int(pos_Y))
                         print "nextprogram_width"
                         print nextprogram_width



                 elif programX == 375 and program_width == 396:
                     programs_width = 408
                     self.getControl(int(program_id)).setWidth(programs_width)

                     if programs_width == 408:
                         self.getControl(int(nextprogram)).setPosition(790, int(pos_Y))

                         if nextprogram_width == 342:
                             self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))
                             



                 elif programX == 375 and program_width == 344:
                     programs_width = 344
                     self.getControl(int(program_id)).setWidth(programs_width)

                     if programs_width == 344:
                         self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))

                         if nextprogram_width == 342:
                             nextprograms_width = 344
                             self.getControl(int(program_id)).setWidth(nextprograms_width)

                             if nextprograms_width == 344:
                                 self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))



                 if epg_time3_hour == program_stop_hour:
                     print "passed epg_time3 1"
                     if epg_time3 == '00':
                         print "passed epg_time3 2"

                         if program_finished == '00':
                             print "you are in here6b 1"
                             if programX == 375 and program_width >= 691:
                                 programs_width = 691
                                 self.getControl(int(program_id)).setWidth(programs_width)
                                 print "you are in here6b 2"

                                 if programs_width == 691:
                                     self.getControl(int(nextprogram)).setPosition(1072, int(pos_Y))
                                     print "you are in here6b 3"


                         elif program_finished == '05':
                             if programX == 375 and program_width >= 691:
                                 programs_width = 757
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 757:
                                     self.getControl(int(nextprogram)).setPosition(1138, int(pos_Y))

                                     if nextprogram_width == 59:
                                         nextprogram_width = 40
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 40:
                                             self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))



                         elif program_finished == '10':
                             if programX == 375 and program_width >= 691:
                                 programs_width = 804
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 804:
                                     self.getControl(int(nextprogram)).setPosition(1184, int(pos_Y))

                                     if nextprogram_width == 59:
                                         nextprogram_width = 56
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 56:
                                             self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))



                         elif program_finished == '15':
                             if programX == 375 and program_width >= 691:
                                 programs_width = 864
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 864:
                                     self.getControl(int(nextprogram)).setPosition(1246, int(pos_Y))



                         elif program_finished == '30':
                             if program_stop_time == epg_time_2:
                                 if programX == 375 and program_width >= 342:
                                     programs_width = 344
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 344:
                                         self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))

                                         if programs_width == 344 and nextprogram_width == 344:
                                             nextprogram_width = 342
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 342:
                                                 self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))



                                         elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                             nextprogram_width = 340
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 340:
                                                 self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))




                         elif program_finished == '50':
                             if program_stop_time > epg_time_2 and program_stop_time < epg_time_3:
                                 if programX == 375 and program_width >= 691:
                                     programs_width = 568
                                     self.getControl(int(program_id)).setWidth(programs_width)
                                     print "channel 5 here 2"

                                     if programs_width == 568:
                                         self.getControl(int(nextprogram)).setPosition(949, int(pos_Y))

                                         if nextprogram_width == 117:
                                             self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))

                                             if nextprogram1_width == 117:
                                                 nextprogram1_width = 106
                                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                 if nextprogram1_width == 106:
                                                     self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))



                                         elif nextprogram_width == 286:
                                             nextprograms_width = 290
                                             self.getControl(int(nextprogram)).setWidth(nextprograms_width)

                                             if nextprograms_width == 290:
                                                 self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))




                     elif epg_time3 == '30':
                         if program_finished == '00':
                             if programX == 375 and program_width > 691:
                                 programs_width = 1033
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 1033:
                                     self.getControl(int(nextprogram)).setPosition(1419, int(pos_Y))



                         elif program_finished == '05':
                             if programX == 375 and program_width > 691:
                                 programs_width = 1093
                                 self.getControl(int(program_id)).setWidth(programs_width)



                         elif program_finished == '10':
                             if programX == 375 and program_width >= 1037:
                                 programs_width = 804
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 804:
                                     self.getControl(int(nextprogram)).setPosition(1184, int(pos_Y))



                         elif program_finished == '15':
                             if programX == 375 and program_width >= 1037:
                                 programs_width = 864
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 864:
                                     self.getControl(int(nextprogram)).setPosition(1246, int(pos_Y))



                         elif program_finished == '30':
                             if programX == 375 and program_width > 691:
                                 programs_width = 691
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 691:
                                     self.getControl(int(nextprogram)).setPosition(1072, int(pos_Y))



                         elif program_finished == '35':
                             if programX == 375 and program_width > 691:
                                 programs_width = 757
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 757:
                                     self.getControl(int(nextprogram)).setPosition(1138, int(pos_Y))

                                     if nextprogram_width == 59:
                                         nextprogram_width = 40
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 40:
                                             self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))



                         elif program_finished == '40':
                             if programX == 375 and program_width >= 691:
                                 programs_width = 803
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 803:
                                     self.getControl(int(nextprogram)).setPosition(1184, int(pos_Y))

                                     if nextprogram_width == 59:
                                         nextprogram_width = 56
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 56:
                                             self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))



                         elif program_finished == '45':
                             if programX == 375 and program_width >= 855:
                                 programs_width = 864
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 864:
                                     self.getControl(int(nextprogram)).setPosition(1246, int(pos_Y))



                         elif program_finished == '50':
                             print "channel 5 here 3"
                             if programX == 375 and program_width >= 691:
                                 programs_width = 918
                                 self.getControl(int(program_id)).setWidth(programs_width)
                                 print "channel 5 here 4"

                                 if programs_width == 918:
                                     self.getControl(int(nextprogram)).setPosition(1297, int(pos_Y))



                         elif program_finished == '55':
                             if programX == 375 and program_width >= 691:
                                 programs_width = 978
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 978:
                                     self.getControl(int(nextprogram)).setPosition(1357, int(pos_Y))




                 if program_stop_time == epg_time_3:
                     print "you are in the epg_time 3 equals 2"
                     if epg_time3_hour != program_stop_hour:
                         print "passed epg_time3 3"
                         if epg_time3 == '00':
                             print "passed epg_time3 4"
                             if program_finished == '00':
                                 print "you are in here6b 3"
                                 if programX == 375 and program_width >= 691:
                                     programs_width = 691
                                     self.getControl(int(program_id)).setWidth(programs_width)
                                     print "you are in here6b 4"

                                     if programs_width == 691:
                                         self.getControl(int(nextprogram)).setPosition(1072, int(pos_Y))
                                         print "you are in here6b 5"



                             elif program_finished == '05':
                                 print "passed epg_time3 5a"

                                 if programX == 375 and program_width >= 342:
                                     print "passed epg_time3 7"
                                     programs_width = 59
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 59:
                                         self.getControl(int(nextprogram)).setPosition(441, int(pos_Y))

                                         if nextprogram_width == 59:
                                             self.getControl(int(nextprogram1)).setPosition(507, int(pos_Y))

                                             if nextprogram1_width == 626:
                                                 self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))


                                         elif nextprogram_width == 117:
                                             nextprogram_width = 102
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 102:
                                                 self.getControl(int(nextprogram1)).setPosition(549, int(pos_Y))

                                                 if nextprogram1_width == 167:
                                                     nextprogram1_width = 170
                                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                     if nextprogram1_width == 170:
                                                         self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))

                                                         if nextprogram2_width == 342:
                                                             self.getControl(int(nextprogram3)).setPosition(1072, int(pos_Y))


                                                         elif nextprogram2_width >= 515:
                                                             self.getControl(int(nextprogram3)).setPosition(1419, int(pos_Y))


                                                 elif nextprogram1_width == 691:
                                                     self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))


                                         elif nextprogram_width == 167:
                                             nextprogram_width = 162
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 162:
                                                 self.getControl(int(nextprogram1)).setPosition(610, int(pos_Y))

                                                 if nextprogram1_width == 167:
                                                     self.getControl(int(nextprogram2)).setPosition(790, int(pos_Y))


                                                 elif nextprogram1_width == 626:
                                                     self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))


                                         elif nextprogram_width == 227:
                                             nextprogram_width = 211
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 211:
                                                 self.getControl(int(nextprogram1)).setPosition(659, int(pos_Y))



                                         elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                             nextprogram_width = 342
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 342:
                                                 self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))

                                                 if nextprogram1_width == 59:
                                                     nextprogram1_width = 47
                                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                     if nextprogram1_width == 47:
                                                         self.getControl(int(nextprogram2)).setPosition(844, int(pos_Y))



                                                 elif nextprogram1_width == 344:
                                                     nextprogram1_width = 338

                                                     if nextprogram1_width == 338:
                                                         self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))



                                         elif nextprogram_width == 396:
                                             self.getControl(int(nextprogram1)).setPosition(842, int(pos_Y))



                                         elif nextprogram_width == 456:
                                             nextprogram_width = 449
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 449:
                                                 self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))



                                         elif nextprogram_width == 567:
                                             self.getControl(int(nextprogram1)).setPosition(1013, int(pos_Y))




                                         elif nextprogram_width == 626:
                                             nextprogram_width = 625
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 625:
                                                 self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))

                                                 if nextprogram1_width == 167:
                                                     self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                         elif nextprogram_width == 691:
                                             nextprogram_width = 691
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 691:
                                                 self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))

                                                 if nextprogram1_width == 59:
                                                     self.getControl(int(nextprogram2)).setPosition(1204, int(pos_Y))


                                                 elif nextprogram1_width == 117:
                                                     self.getControl(int(nextprogram2)).setPosition(1262, int(pos_Y))



                                         elif nextprogram_width == 741:
                                             nextprogram_width = 742
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 742:
                                                 self.getControl(int(nextprogram1)).setPosition(1189, int(pos_Y))



                         elif epg_time3 == '30':
                             print "passed epg_time3 5"

                             if program_finished == '00' or program_finished == '30':
                                 print "you are in here6b 6"
                                 if program_stop_time == epg_time_2:
                                     if programX == 375 and program_width >= 456:
                                         programs_width = 343
                                         self.getControl(int(program_id)).setWidth(programs_width)
                                         self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))
                                         print "you are in the epg_time2 pass 2"

                                         if nextprogram_width == 168:
                                             nextprogram_width = 168
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 168:
                                                 self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))


                                             elif nextprogram_width == 167:
                                                 self.getControl(int(nextprogram1)).setPosition(546, int(pos_Y))


                                             elif nextprogram_width == 286:
                                                 self.getControl(int(nextprogram1)).setPosition(1009, int(pos_Y))

                                             elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                                 self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))

                                             elif nextprogram_width == 456:
                                                 nextprogram_width = 454
                                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                 if nextprogram_width == 454:
                                                     self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))



                                         elif programX == 375 and program_width >= 286:
                                             programs_width = 343
                                             self.getControl(int(program_id)).setWidth(programs_width)
                                             self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))
                                             print "you are in the epg_time2 pass 3 b"
                                             print nextprogram_width

                                             if nextprogram_width == 286 and nextprogram1_width == 59:
                                                 programs_width = 279
                                                 self.getControl(int(nextprogram)).setWidth(programs_width)

                                                 if programs_width == 279:
                                                     self.getControl(int(nextprogram1)).setPosition(1009, int(pos_Y))

                                                     if nextprogram2X != 1072:
                                                         self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))



                                             elif nextprogram_width == 59:
                                                 self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))

                                                 if nextprogram1_width == 344:
                                                     self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))



                                             elif nextprogram_width == 148:
                                                 nextprogram_width = 167
                                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)
                                                 print "you are here 1 chris"

                                                 if nextprogram_width == 167:
                                                     self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))

                                                     if nextprogram1_width == 79:
                                                         nextprogram1_width = 59
                                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                         if nextprogram1_width == 59:
                                                             self.getControl(int(nextprogram2)).setPosition(963, int(pos_Y))



                                             elif nextprogram_width == 167:
                                                 self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))
                                                 print "you are here 2 chris"

                                                 if nextprogram1_width == 117:
                                                     self.getControl(int(nextprogram2)).setPosition(1023, int(pos_Y))


                                                 elif nextprogram1_width == 167:
                                                     nextprogram1_width = 169
                                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                     if nextprogram1_width == 169:
                                                         self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))



                                             elif nextprogram_width == 227:
                                                 nextprogram_width = 231
                                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                 if nextprogram_width == 231:
                                                     self.getControl(int(nextprogram1)).setPosition(959, int(pos_Y))

                                                     if nextprogram1_width == 117:
                                                         nextprogram1_width = 109
                                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                         if nextprogram1_width == 109:
                                                             self.getControl(int(nextprogram2)).setPosition(1072, int(pos_Y))



                                             elif nextprogram_width == 286:
                                                 nextprogram_width = 293
                                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                 if nextprogram_width == 293:
                                                     self.getControl(int(nextprogram1)).setPosition(1023, int(pos_Y))

                                                     if nextprogram1_width == 117:
                                                         self.getControl(int(nextprogram2)).setPosition(1146, int(pos_Y))



                                             elif nextprogram_width >= 342 and nextprogram_width <= 344:
                                                 nextprogram_width = 342
                                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)
                                                 print "you are in the 344 number 1 chris"

                                                 if nextprogram_width == 342:
                                                     self.getControl(int(nextprogram1)).setPosition(1072, int(pos_Y))
                                                     print "you are in the 344 number 2 chris"

                                                     if nextprogram1_width == 117:
                                                         nextprogram1_width = 100
                                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                         if nextprogram1_width == 100:
                                                             self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))


                                                     elif nextprogram1_width == 167:
                                                         self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                             elif nextprogram_width == 396:
                                                 nextprogram_width = 409
                                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                 if nextprogram_width == 409:
                                                     self.getControl(int(nextprogram1)).setPosition(1140, int(pos_Y))



                                             elif nextprogram_width == 456:
                                                 nextprogram_width = 454
                                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                 if nextprogram_width == 454:
                                                     self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))



                                             elif nextprogram_width == 515:
                                                 self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))



                                 elif program_stop_time == epg_time_3:
                                     if programX == 375 and program_width >= 691:
                                         programs_width = 691
                                         self.getControl(int(program_id)).setWidth(programs_width)

                                         if programs_width == 691:
                                             self.getControl(int(nextprogram)).setPosition(1072, int(pos_Y))
                                             print "LOOK AT THE EPG FOR THAT PROGRAM TO SEE IF DATA NED TO BE DELETE FROM DATABASE"



                 self.program_remaining = False


         #except:
             #pass


         program_stop_list = list()
         #self.program_remaining = False
