import datetime
import time
import _strptime
from itertools import izip_longest


def programs_test(self):
     #if_program_remaining == true codes goes here
     if self.program_remaining == True:
         self.program_remaining = False
         
         print "hello"


def programs_remaining(self):
     #if_program_remaining == true codes goes here
     if self.program_remaining == True:
         self.program_remaining = False
         self.program_finished_flag = False
         self.program_width = list()
         progId = list()
         posX = list()
         posY = list()
         program_length = list()
         prog_id_list = list()
         prog_length_list = list()
         pos_X_list = list()
         programs_button = [elem.control for elem in self.program_buttons]

         for elem in programs_button:
             progId.append(elem.getId())
             posX.append(elem.getX())
             posY.append(elem.getY())
             program_length.append(elem.getWidth())
         progId = map(str, progId)
         posX = map(str, posX)
         posY = map(str, posY)
         program_length = map(str, program_length)
         channel_1 = list()
         current_program_clock_list = list()
         prog_index = list()


         #Store the list of strings in the lists
         for i in range(len(posX)):
             pos_X = posX[i]


             if pos_X == '375':
                 #prog_index.append(self.program_index_)
                 prog_id_list.append(progId[i])
                 prog_length_list.append(program_length[i])
                 pos_X_list.append(posX[i])





         for pos_X, pos_Y, prog_id in zip(posX, posY, progId):
             if int(pos_X) == 375:
                 prog_index = self.program_index_


                 if len(self.program_index_) >= 1:
                     for index in prog_index:
                         prog_id = self.prog_id_list[index]
                         prog_length = prog_length_list[index]
                         prog_length = int(prog_length)
                         self.program_id = list()
                         self.program_id.append(prog_id)
                         self.program_width.append(prog_length)


         #Now let change the programming button size for real time
         for program_end_time in self.current_program_end_time:
             half_hour = str(self.getControl(344).getLabel())
             one_hour = str(self.getControl(345).getLabel())
             one_hour_half = str(self.getControl(346).getLabel())
             program_stop_hours = str(program_end_time.hour)
             program_stop_minutes = str(program_end_time.minute)
             program_stop_days = str(program_end_time.day)
             program_stop_months = str(program_end_time.month)
             program_stop_year = str(program_end_time.year)


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

             program_times = str(program_stop_hours + ':' + program_stop_minutes + program_AM_PM)
             stop_times = str(program_stop_days + "/" + program_stop_months + "/" + program_stop_year + " " + program_times)
             current_program_clock_list.append(stop_times)
         program_id = ''.join(str(x) for x in self.program_id)



         for program_stop_clock, program_stop_times, program_width in izip_longest(self.program_finished_clock, current_program_clock_list, self.program_width, fillvalue=''):
             epg_time_1 = time.strptime(half_hour_date, '%d/%m/%Y %I:%M%p')
             epg_time_2 = time.strptime(one_hour_date, '%d/%m/%Y %I:%M%p')
             epg_time_3 = time.strptime(one_hour_half_date, '%d/%m/%Y %I:%M%p')



             try:
                 program_stop_time = time.strptime(program_stop_times, '%d/%m/%Y %I:%M%p')
                 current_time = int(time.strftime("%M"))
                 program_finished = program_stop_clock
                 programX = self.getControl(int(program_id)).getX()
                 nextprogram = int(program_id) + 1
                 nextprogramX = self.getControl(int(nextprogram)).getX()
                 nextprogram_width = self.getControl(int(nextprogram)).getWidth()
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
                 print program_finished


                 if int(programX) == 375:
                     if programX == 375 and program_width == 342:
                         if nextprogramX == 1073:
                             self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))


                     elif programX == 375 and program_width == 626:
                         if nextprogramX != 1008:
                             self.getControl(int(nextprogram)).setPosition(1008, int(pos_Y))


                         elif nextprogramX == 1008:
                             self.getControl(int(nextprogram)).setPosition(1007, int(pos_Y))



                     elif programX == 375 and program_width == 692:
                         if nextprogramX == 1073:
                             program_width = 691
                             self.getControl(int(program_id)).setWidth(program_width)
                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))


                         elif nextprogramX != 1073:
                             program_width = 691
                             self.getControl(int(program_id)).setWidth(program_width)
                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))



                 if program_stop_time == epg_time_1:
                     print "here 1"

                     if program_finished == '00':
                         if programX == 375 and program_width >= 342:
                             programs_width = 342
                             self.getControl(int(program_id)).setWidth(programs_width)
                             self.getControl(int(program_id)).setVisible(False)
                             self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                             self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))



                     elif program_finished == '30':
                         if programX == 375 and program_width >= 342:
                             programs_width = 342
                             self.getControl(int(program_id)).setWidth(programs_width)
                             self.getControl(int(program_id)).setVisible(False)
                             self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                             self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))

                             if nextprogram_width == 342:
                                 self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))


                             elif nextprogram_width == 692:
                                 self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))



                 elif program_stop_time == epg_time_2:
                     print "here 2b"

                     if program_finished == '00':
                         if program_stop_time == epg_time_2:
                             if programX == 375 and program_width >= 456:
                                 programs_width = 342
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
                                         self.getControl(int(nextprogram1)).setPosition(1014, int(pos_Y))

                                     elif nextprogram_width == 342:
                                         self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))

                                     elif nextprogram_width == 456:
                                         self.getControl(int(nextprogram1)).setPosition(1188, int(pos_Y))



                                 elif programX == 375 and program_width >= 286:
                                     programs_width = 342
                                     self.getControl(int(program_id)).setWidth(programs_width)
                                     self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))
                                     print "you are in the epg_time2 pass 3"

                                     if nextprogram_width == 286 and nextprogram1_width == 59:
                                         programs_width = 277
                                         self.getControl(int(nextprogram)).setWidth(programs_width)
                                         self.getControl(int(nextprogram1)).setPosition(1007, int(pos_Y))

                                         if nextprogram2X != 1073:
                                             self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))



                                     elif nextprogram_width == 59:
                                         self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))

                                         if nextprogram1_width == 342:
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
                                             self.getControl(int(nextprogram2)).setPosition(1021, int(pos_Y))


                                         elif nextprogram1_width == 167:
                                             nextprogram1_width = 169
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 169:
                                                 self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))



                                     elif nextprogram_width == 227:
                                         self.getControl(int(nextprogram1)).setPosition(957, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             nextprogram1_width = 109
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 109:
                                                 self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))



                                     elif nextprogram_width == 342:
                                         self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             self.getControl(int(nextprogram2)).setPosition(1197, int(pos_Y))


                                         elif nextprogram1_width == 167:
                                             self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                     elif nextprogram_width == 396:
                                         nextprogram_width = 409
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 409:
                                             self.getControl(int(nextprogram1)).setPosition(1140, int(pos_Y))



                                     elif nextprogram_width == 456:
                                         self.getControl(int(nextprogram1)).setPosition(1187, int(pos_Y))



                                     elif nextprogram_width == 515:
                                         self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))




                     elif program_finished >= '15' and program_finished <= '17':
                         if programX == 375 and program_width == 692:
                             programs_width = 342
                             self.getControl(int(program_id)).setWidth(programs_width)
                             self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))

                             #if nextprograms_width == 342:
                                 #if nextprogram_width == 286 and nextprograms_width == 59:
                                     #nextprogram_width = 276
                                     #self.getControl(int(nextprogram)).setWidth(nextprogram_width)



                     elif program_finished == '25':
                         if programX == 375 and program_width == 456:
                             programs_width = 287
                             self.getControl(int(program_id)).setWidth(programs_width)



                     elif program_finished == '30':
                         if programX == 375 and program_width >= 342:
                             programs_width = 342
                             self.getControl(int(program_id)).setWidth(programs_width)
                             self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))

                             if nextprogram_width == 59:
                                 self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))


                             elif nextprogram_width == 117:
                                 self.getControl(int(nextprogram1)).setPosition(847, int(pos_Y))

                                 if nextprogram1_width == 227:
                                     nextprogram1_width = 219
                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                     if nextprogram1_width == 117:
                                         self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))


                                     elif nextprogram1_width == 219:
                                         self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))


                             elif nextprogram_width == 167:
                                 self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))

                                 if nextprogram1_width == 167:
                                     nextprogram1_width = 169
                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                     if nextprogram1_width == 169:
                                         self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))


                             elif nextprogram_width == 227:
                                 self.getControl(int(nextprogram1)).setPosition(958, int(pos_Y))

                                 if nextprogram1_width == 117:
                                     nextprogram1_width = 108
                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                     if nextprogram1_width == 108:
                                         self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))



                             elif nextprogram_width == 286:
                                 nextprogram_width = 277
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 277:
                                     self.getControl(int(nextprogram1)).setPosition(1007, int(pos_Y))

                                     if nextprogram1_width == 59:
                                         self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))



                             elif nextprogram_width == 342:
                                 self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))

                                 if nextprogram1_width == 167:
                                     self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                             elif nextprogram_width == 456:
                                 self.getControl(int(nextprogram1)).setPosition(1188, int(pos_Y))


                             elif nextprogram_width == 515:
                                 self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))






                 elif program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                     print "here 3a"

                     if program_finished == '00':
                         if program_stop_time == epg_time_1:
                             if programX == 375 and program_width <= 741:
                                 programs_width = 342
                                 self.getControl(int(program_id)).setWidth(programs_width)
                                 self.getControl(int(program_id)).setVisible(False)
                                 self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                                 self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))

                                 if nextprogram_width == 342:
                                     if nextprogram1X != 724:
                                         self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))


                         elif program_stop_time == epg_time_2 or program_stop_time > epg_time_2:
                             if programX == 375 and program_width >= 741:
                                 programs_width = 342
                                 self.getControl(int(program_id)).setWidth(programs_width)
                                 self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))

                                 if nextprogram_width == 342:
                                     if nextprogram1X != 1073:
                                         self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))



                         elif program_stop_time == epg_time_3:
                             if programX == 375 and program_width >= 741:
                                 programs_width = 692
                                 self.getControl(int(program_id)).setWidth(programs_width)
                                 self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))




                     elif program_finished == '05':
                         if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                             if programX == 375 and program_width >= 342:
                                 print "you are here for channel 4"
                                 programs_width = 59
                                 self.getControl(int(program_id)).setWidth(programs_width)


                                 if programs_width == 59:
                                     self.getControl(int(nextprogram)).setPosition(441, int(pos_Y))

                                     if nextprogram_width == 167:
                                         self.getControl(int(nextprogram1)).setPosition(614, int(pos_Y))

                                         if nextprogram1_width == 167:
                                             self.getControl(int(nextprogram2)).setPosition(789, int(pos_Y))


                                     elif nextprogram_width == 342:
                                         self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))

                                         if nextprogram1_width == 59:
                                             self.getControl(int(nextprogram2)).setPosition(856, int(pos_Y))


                                         elif nextprogram1_width == 342:
                                             self.getControl(int(nextprogram2)).setPosition(1130, int(pos_Y))



                                     elif nextprogram_width == 396:
                                         self.getControl(int(nextprogram1)).setPosition(842, int(pos_Y))



                                     elif nextprogram_width == 567:
                                         self.getControl(int(nextprogram1)).setPosition(1015, int(pos_Y))




                                     elif nextprogram_width == 626:
                                         nextprogram_width = 625
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 625:
                                             self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))

                                             if nextprogram1_width == 167:
                                                 self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))


                                     elif nextprogram_width == 692:
                                         nextprogram_width = 691
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 691:
                                             self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))



                                     elif nextprogram_width == 741:
                                         self.getControl(int(nextprogram1)).setPosition(1189, int(pos_Y))



                     elif program_finished == '10':
                         if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                             if programX == 375 and program_width >= 286:
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



                                     elif nextprogram_width == 342:
                                         nextprogram_width = 332
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 332:
                                             self.getControl(int(nextprogram1)).setPosition(847, int(pos_Y))


                                     elif nextprogram_width == 456:
                                         self.getControl(int(nextprogram1)).setPosition(958, int(pos_Y))


                                     elif nextprogram_width == 515:
                                         nextprogram_width = 516
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 516:
                                             self.getControl(int(nextprogram1)).setPosition(1021, int(pos_Y))

                                             if nextprogram1_width == 59:
                                                 self.getControl(int(nextprogram2)).setPosition(1087, int(pos_Y))


                                     elif nextprogram_width == 567:
                                         nextprogram_width = 568
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 568:
                                             self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))


                                     elif nextprogram_width == 692:
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
                             if programX == 375 and program_width >= 286:
                                 programs_width = 167
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 167:
                                     self.getControl(int(nextprogram)).setPosition(549, int(pos_Y))

                                     if nextprogram_width == 227:
                                         nextprogram_width = 236
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 236:
                                             self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))


                                     elif nextprogram_width == 342:
                                         self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             self.getControl(int(nextprogram2)).setPosition(1020, int(pos_Y))


                                         elif nextprogram1_width == 227:
                                             nextprogram1_width = 226
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 226:
                                                 self.getControl(int(nextprogram2)).setPosition(1130, int(pos_Y))



                                     elif nextprogram_width == 396:
                                         nextprogram_width = 399
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 399:
                                             self.getControl(int(nextprogram1)).setPosition(955, int(pos_Y))

                                             if nextprogram1_width == 167:
                                                 nextprogram1_width = 171
                                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                 if nextprogram1_width == 171:
                                                     self.getControl(int(nextprogram2)).setPosition(1134, int(pos_Y))



                                     elif nextprogram_width == 515:
                                         nextprogram_width = 517
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 517:
                                             self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))



                                     elif nextprogram_width == 567:
                                         nextprogram_width = 582
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 582:
                                             self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))



                                     elif nextprogram_width == 626:
                                         self.getControl(int(nextprogram1)).setPosition(1182, int(pos_Y))


                                     elif nextprogram_width == 692:
                                         nextprogram_width = 691
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 691:
                                             self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))



                     elif program_finished == '20':
                         if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                             if programX == 375 and program_width >= 227:
                                 programs_width = 228
                                 self.getControl(int(program_id)).setWidth(programs_width)


                                 if programs_width == 228:
                                     self.getControl(int(nextprogram)).setPosition(609, int(pos_Y))

                                     if nextprogram_width == 59:
                                         self.getControl(int(nextprogram1)).setPosition(675, int(pos_Y))


                                     elif nextprogram_width == 117:
                                         nextprogram_width = 108
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)


                                         if nextprogram_width == 108:
                                             self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))


                                             if nextprogram1_width == 117:
                                                 nextprogram1_width = 107
                                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                 if nextprogram1_width == 107:
                                                     self.getControl(int(nextprogram2)).setPosition(837, int(pos_Y))



                                             elif nextprogram1_width == 342:
                                                 self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))



                                     elif nextprogram_width == 167:
                                         self.getControl(int(nextprogram1)).setPosition(830, int(pos_Y))



                                     elif nextprogram_width == 286:
                                         self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))



                                     elif nextprogram_width == 342:
                                         self.getControl(int(nextprogram1)).setPosition(958, int(pos_Y))


                                     elif nextprogram_width == 456:
                                         nextprogram_width = 457
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 457:
                                             self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))


                                     elif nextprogram_width == 626:
                                         self.getControl(int(nextprogram1)).setPosition(1242, int(pos_Y))


                                     elif nextprogram_width == 692:
                                         nextprogram_width = 691

                                         if nextprogram_width == 691:
                                             self.getControl(int(nextprogram1)).setPosition(1308, int(pos_Y))





                     elif program_finished == '25':
                         if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                             if programX == 375 and program_width >= 286:
                                 if self.program_finished_flag == False:
                                     print "it have change the size here 2"
                                     programs_width = 277
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 277:
                                         self.getControl(int(nextprogram)).setPosition(659, int(pos_Y))

                                         if nextprogram_width == 59:
                                             self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))

                                             if nextprogram1_width == 342:
                                                 self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))


                                         elif nextprogram_width == 167:
                                             self.getControl(int(nextprogram1)).setPosition(830, int(pos_Y))


                                         elif nextprogram_width == 342:
                                             self.getControl(int(nextprogram1)).setPosition(1007, int(pos_Y))


                                         elif nextprogram_width == 456:
                                             self.getControl(int(nextprogram1)).setPosition(1124, int(pos_Y))


                                         elif nextprogram_width == 516:
                                             self.getControl(int(nextprogram1)).setPosition(1179, int(pos_Y))


                                         elif nextprogram_width == 567:
                                             self.getControl(int(nextprogram1)).setPosition(1232, int(pos_Y))


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
                                     self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))



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
                                             self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))



                             elif int(current_time) >= 30 and int(current_time) < 59:
                                 if programX == 375 and program_width >= 117:
                                     print "you are here 2"
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

                                                 if nextprogram1_width == 692:
                                                     nextprogram1_width = 691
                                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                     if nextprogram1_width == 691:
                                                         self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                         elif nextprogram_width == 167:
                                             nextprogram_width = 160
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 160:
                                                 self.getControl(int(nextprogram1)).setPosition(609, int(pos_Y))

                                                 if nextprogram1_width == 117:
                                                     nextprogram1_width = 109
                                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                     if nextprogram1_width == 109:
                                                         self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))



                                         elif nextprogram_width == 227:
                                             nextprogram_width = 234
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 234:
                                                 self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))


                                         elif nextprogram_width == 342:
                                             self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))

                                             if nextprogram1_width == 342:
                                                 nextprogram1_width = 338

                                                 if nextprogram1_width == 338:
                                                     self.getControl(int(nextprogram2)).setPosition(1134, int(pos_Y))



                                         elif nextprogram_width == 456:
                                             nextprogram_width = 449
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 449:
                                                 self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))



                                         elif nextprogram_width == 567:
                                             self.getControl(int(nextprogram1)).setPosition(1016, int(pos_Y))




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

                                 if programs_width == 125:
                                     self.getControl(int(nextprogram)).setPosition(507, int(pos_Y))

                                     if nextprogram_width == 59:
                                         self.getControl(int(nextprogram1)).setPosition(568, int(pos_Y))


                                     if nextprogram_width == 117 and nextprogram1_width == 117:
                                         nextprogram_width = 108
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 108:
                                             self.getControl(int(nextprogram1)).setPosition(621, int(pos_Y))

                                             if nextprogram1_width == 117:
                                                 nextprogram1_width = 97
                                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                 if nextprogram1_width == 97:
                                                     self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))



                                     elif nextprogram_width == 167:
                                         nextprogram_width = 147
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 147:
                                             self.getControl(int(nextprogram1)).setPosition(659, int(pos_Y))



                                     elif nextprogram_width == 342:
                                         self.getControl(int(nextprogram1)).setPosition(853, int(pos_Y))

                                         if nextprogram1_width == 342:
                                             self.getControl(int(nextprogram2)).setPosition(1196, int(pos_Y))


                                     elif nextprogram_width == 515:
                                         self.getControl(int(nextprogram1)).setPosition(1020, int(pos_Y))


                                     elif nextprogram_width == 567:
                                         self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             self.getControl(int(nextprogram2)).setPosition(1197, int(pos_Y))


                                     elif nextprogram_width == 692:
                                         nextprogram_width = 687
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 687:
                                             self.getControl(int(nextprogram1)).setPosition(1197, int(pos_Y))




                     elif program_finished == '45':
                         print "hello chris"
                         if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                             if programX == 375 and program_width >= 342:
                                 programs_width = 167
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 167:
                                     self.getControl(int(nextprogram)).setPosition(549, int(pos_Y))

                                     if nextprogram_width == 59:
                                         self.getControl(int(nextprogram1)).setPosition(614, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             nextprogram1_width = 103
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 103:
                                                 self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))



                                     elif nextprogram_width == 227:
                                         nextprogram_width = 234
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 234:
                                             self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))


                                     elif nextprogram_width == 342:
                                         self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))


                                     elif nextprogram_width >= 515:
                                         nextprogram_width = 517
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 517:
                                             self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))

                                             if nextprogram1_width == 59:
                                                 self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))


                                     elif nextprogram_width == 567:
                                         nextprogram_width = 579
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 579:
                                             self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))


                                     elif nextprogram_width == 626:
                                         self.getControl(int(nextprogram1)).setPosition(1183, int(pos_Y))



                                     elif nextprogram_width == 692:
                                         nextprogram_width = 691
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 691:
                                             self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))



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
                                         self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))



                         elif program_stop_time == epg_time_3:
                             if programX == 375 and program_width >= 692:
                                 programs_width = 691
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 691:
                                     self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))



                     elif program_finished == '50':
                         print "50 has passed"
                         if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                             if program_width >= 567:
                                 programs_width = 228
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 228:
                                     self.getControl(int(nextprogram)).setPosition(610, int(pos_Y))

                                     if nextprogram_width == 59:
                                         self.getControl(int(nextprogram1)).setPosition(676, int(pos_Y))


                                     elif nextprogram_width == 167:
                                         self.getControl(int(nextprogram1)).setPosition(783, int(pos_Y))



                                     elif nextprogram_width == 286:
                                         nextprogram_width = 281
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 281:
                                             self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))



                                     elif nextprogram_width == 342:
                                         self.getControl(int(nextprogram1)).setPosition(959, int(pos_Y))

                                         if nextprogram1_width == 167:
                                             self.getControl(int(nextprogram2)).setPosition(1134, int(pos_Y))


                                     elif nextprogram_width == 399:
                                         self.getControl(int(nextprogram1)).setPosition(1016, int(pos_Y))


                                     elif nextprogram_width == 456:
                                         self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))


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
                                         self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))


                                     elif nextprogram_width == 626:
                                         self.getControl(int(nextprogram1)).setPosition(1243, int(pos_Y))



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
                                             self.getControl(int(nextprogram2)).setPosition(1187, int(pos_Y))



                     elif program_finished == '55':
                         if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                             if int(current_time) >= 00 and int(current_time) < 29:
                                 if programX == 375 and program_width >= 286:

                                     if nextprogram_width == 59:
                                         programs_width = 277
                                         self.getControl(int(program_id)).setWidth(programs_width)

                                         if programs_width == 277:
                                             self.getControl(int(nextprogram)).setPosition(659, int(pos_Y))

                                             if nextprogram1X >= 1073:
                                                 self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))


                                         else:
                                             programs_width = 283
                                             self.getControl(int(program_id)).setWidth(programs_width)

                                             if programs_width == 283:
                                                 self.getControl(int(nextprogram)).setPosition(664, int(pos_Y))



                                 #if program_length == 798:
                                     #prog_width = 692
                                     #self.getControl(int(program_id)).setWidth(prog_width)



                             else:
                                 print "you need to fix the button size that are 286 or more with the next program 5 mins"
                                 print "program_width"
                                 print program_width

                                 if programX == 375 and program_width >= 286:
                                     programs_width = 277
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if nextprogram_width == 59:
                                         self.getControl(int(nextprogram)).setPosition(659, int(pos_Y))

                                         if nextprogram1X != 724:
                                             self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))

                                             if nextprogram1_width == 286:
                                                 self.getControl(int(nextprogram2)).setPosition(1018, int(pos_Y))

                                                 if nextprogram2_width == 227:
                                                     self.getControl(int(nextprogram3)).setPosition(1251, int(pos_Y))


                                             elif nextprogram1_width == 342:
                                                 self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))



                                     elif nextprogram_width > 59:
                                         self.getControl(int(nextprogram)).setPosition(659, int(pos_Y))

                                         if nextprogram_width == 167:
                                             self.getControl(int(nextprogram1)).setPosition(832, int(pos_Y))

                                             if nextprogram1_width == 342:
                                                 self.getControl(int(nextprogram2)).setPosition(1180, int(pos_Y))


                                         elif nextprogram_width == 342:
                                             self.getControl(int(nextprogram1)).setPosition(1007, int(pos_Y))


                                         elif nextprogram_width == 399:
                                             self.getControl(int(nextprogram1)).setPosition(1062, int(pos_Y))


                                         elif nextprogram_width == 456:
                                             self.getControl(int(nextprogram1)).setPosition(1124, int(pos_Y))


                                         elif nextprogram_width == 515:
                                             self.getControl(int(nextprogram1)).setPosition(1180, int(pos_Y))


                                         elif nextprogram_width == 567:
                                             self.getControl(int(nextprogram1)).setPosition(1230, int(pos_Y))




                 elif program_stop_time > epg_time_2 and program_stop_time < epg_time_3:
                     print "here 4b"

                     if program_finished == '00':
                         if programX == 375 and program_width >= 342:
                             programs_width = 342
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 342:
                                 self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))



                     elif program_finished == '05':
                         print "you are in 4:05 now 1"
                         print "program_width"
                         print program_width

                         if programX == 375 and program_width >= 456:
                             programs_width = 408
                             self.getControl(int(program_id)).setWidth(programs_width)
                             print "you are in 4:05 now 2"

                             if programs_width == 408:
                                 self.getControl(int(nextprogram)).setPosition(790, int(pos_Y))

                                 if nextprogram_width == 167:
                                     self.getControl(int(nextprogram1)).setPosition(955, int(pos_Y))

                                     if nextprogram1_width == 117:
                                         self.getControl(int(nextprogram2)).setPosition(1136, int(pos_Y))


                                     elif nextprogram1_width == 167:
                                         self.getControl(int(nextprogram2)).setPosition(1128, int(pos_Y))


                                 elif nextprogram_width == 342:
                                     self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))

                                     if nextprogram1_width == 59:
                                         self.getControl(int(nextprogram2)).setPosition(1204, int(pos_Y))



                                 elif nextprogram_width == 396:
                                     nextprogram_width = 409
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 409:
                                         self.getControl(int(nextprogram1)).setPosition(1197, int(pos_Y))



                     elif program_finished == '10':
                         if programX == 375 and program_width >= 227:
                             programs_width = 456
                             self.getControl(int(program_id)).setWidth(programs_width)
                             print "itv code here"

                             if programs_width == 456:
                                 self.getControl(int(nextprogram)).setPosition(837, int(pos_Y))

                                 if nextprogram_width == 59:
                                     nextprogram_width = 54
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 54:
                                         self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))

                                         if nextprogram1_width == 167:
                                             nextprogram1_width = 169
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 169:
                                                 self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))


                                 elif nextprogram_width == 117:
                                     self.getControl(int(nextprogram1)).setPosition(959, int(pos_Y))

                                     if nextprogram1_width == 117:
                                         nextprogram1_width = 107
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 107:
                                             self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))


                                 elif nextprogram_width == 342:
                                     nextprogram_width = 341
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 341:
                                         self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))



                     elif program_finished == '15':
                         print "you are in the 15 mins now chris"
                         if programX == 375 and program_width >= 515:
                             programs_width = 516
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 516:
                                 self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))

                                 if nextprogram_width == 342:
                                     self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))



                     elif program_finished == '20':
                         if program_width == 515:
                             programs_width = 516
                             self.getControl(int(program_id)).setWidth(programs_width)



                         elif programX == 375 and program_width >= 626:
                             programs_width = 577
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 577:
                                 self.getControl(int(nextprogram)).setPosition(958, int(pos_Y))

                                 if nextprogram_width == 59:
                                     self.getControl(int(nextprogram1)).setPosition(1024, int(pos_Y))


                                 elif nextprogram_width == 117:
                                     nextprogram_width = 108
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 108:
                                         self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))



                     elif program_finished == '25':
                         if programX == 375 and program_width >= 691:
                             programs_width = 627
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if nextprogramX != 949:
                                 self.getControl(int(nextprogram)).setPosition(1008, int(pos_Y))

                                 if nextprogram_width == 59:
                                     self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))


                                 elif nextprogram_width == 167:
                                     self.getControl(int(nextprogram1)).setPosition(1182, int(pos_Y))



                     elif program_finished == '30':
                         if programX == 375 and program_width >= 1038:
                             programs_width = 342
                             self.getControl(int(program_id)).setWidth(programs_width)



                     elif program_finished == '35':
                         if programX == 375 and program_width <= 396:
                             if program_width == 396 and nextprogram_width == 117:
                                 nextprogram_width = 113
                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                 if nextprogram_width == 113:
                                     self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))



                         elif programX == 375 and program_width >= 515:
                             programs_width = 408
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 408:
                                 self.getControl(int(nextprogram)).setPosition(790, int(pos_Y))

                                 if nextprogram_width == 59:
                                     self.getControl(int(nextprogram1)).setPosition(856, int(pos_Y))


                                 elif nextprogram_width == 167:
                                     self.getControl(int(nextprogram1)).setPosition(955, int(pos_Y))

                                     if nextprogram1_width == 117:
                                         nextprogram1_width = 111
                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                         if nextprogram1_width == 111:
                                             self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))



                                 elif nextprogram_width == 286:
                                     self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))


                                 elif nextprogram_width == 342:
                                     self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))



                     elif program_finished == '40':
                         if programX == 375 and program_width > 692:
                             programs_width = 456
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 456:
                                 self.getControl(int(nextprogram)).setPosition(837, int(pos_Y))

                                 if nextprogram_width == 59:
                                     programs_width = 450
                                     self.getControl(int(program_id)).setWidth(programs_width)
                                     self.getControl(int(nextprogram)).setPosition(832, int(pos_Y))
                                     self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))



                                 elif nextprogram_width == 117:
                                     nextprogram_width = 115
                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                     if nextprogram_width == 115:
                                         self.getControl(int(nextprogram1)).setPosition(959, int(pos_Y))

                                         if nextprogram1_width == 117:
                                             nextprogram1_width = 107
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 107:
                                                 self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))



                                 elif nextprogram_width == 342:
                                     self.getControl(int(nextprogram1)).setPosition(1186, int(pos_Y))





                     elif program_finished == '45':
                         if programX == 375 and program_width >= 515:
                             programs_width = 577
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 577:
                                 self.getControl(int(nextprogram)).setPosition(958, int(pos_Y))

                                 if nextprogram_width == 59:
                                     self.getControl(int(nextprogram1)).setPosition(1024, int(pos_Y))

                                     if nextprogram1_width == 117:
                                         self.getControl(int(nextprogram2)).setPosition(1147, int(pos_Y))


                                 elif nextprogram_width == 167:
                                     self.getControl(int(nextprogram1)).setPosition(1131, int(pos_Y))



                     elif program_finished == '50':
                         if program_width >= 515:
                             programs_width = 577
                             self.getControl(int(program_id)).setWidth(programs_width)

                             if programs_width == 577:
                                 self.getControl(int(nextprogram)).setPosition(959, int(pos_Y))

                                 if nextprogram_width == 286:
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
                                 programs_width = 626
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 626:
                                     self.getControl(int(nextprogram)).setPosition(1007, int(pos_Y))

                                     if nextprogram_width == 59:
                                         self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))

                                         if nextprogram1_width == 342:
                                             self.getControl(int(nextprogram2)).setPosition(1419, int(pos_Y))




                 elif program_stop_time == epg_time_3:
                     print "here 5a"
                     epg_time3_hour = epg_time_3.tm_hour
                     program_stop_hour = program_stop_time.tm_hour
                     #program_width = self.getControl(program_id).getWidth()


                     if epg_time3_hour == program_stop_hour:
                         if program_finished == '00':
                             if programX == 375 and program_width == 692:
                                 print "passed 2"
                                 if nextprogramX != 1073:
                                     self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))



                             elif programX == 375 and program_width >= 626:
                                 programs_width = 691
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 691:
                                     self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))

                                     if nextprogram_width == 117:
                                         self.getControl(int(nextprogram1)).setPosition(1196, int(pos_Y))


                                     elif nextprogram_width == 168:
                                         nextprogram_width = 168
                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                         if nextprogram_width == 168:
                                             self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))


                                     elif nextprogram_width == 167:
                                         self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))



                         elif program_finished == '30':
                             if programX == 375 and program_width >= 515:
                                 programs_width = 691
                                 self.getControl(int(program_id)).setWidth(programs_width)

                                 if programs_width == 691:
                                     self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))

                                     if nextprogram_width == 59:
                                         self.getControl(int(nextprogram1)).setPosition(1139, int(pos_Y))


                                     elif nextprogram_width == 117:
                                         self.getControl(int(nextprogram1)).setPosition(1197, int(pos_Y))


                                     elif nextprogram_width == 167:
                                         self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))




                 elif program_stop_time > epg_time_3:
                     print "here 6b"
                     epg_time3 = str(self.getControl(346).getLabel())
                     epg_time3 = epg_time3.split(':')[1].replace('PM', '').replace('AM', '')
                     epg_time3_hour = epg_time_3.tm_hour
                     program_stop_hour = program_stop_time.tm_hour
                     #print "program_finished"
                     #print program_finished


                     if epg_time3_hour == program_stop_hour:
                         if epg_time3 == '00':
                             if program_finished == '05':
                                 if programX == 375 and program_width >= 691:
                                     programs_width = 750
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 750:
                                         self.getControl(int(nextprogram)).setPosition(1131, int(pos_Y))

                                         if nextprogram_width == 59:
                                             self.getControl(int(nextprogram1)).setPosition(1197, int(pos_Y))



                             elif program_finished == '10':
                                 if programX == 375 and program_width >= 691:
                                     programs_width = 806
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 806:
                                         self.getControl(int(nextprogram)).setPosition(1188, int(pos_Y))

                                         if nextprogram_width == 59:
                                             self.getControl(int(nextprogram1)).setPosition(1253, int(pos_Y))



                             if program_finished == '15':
                                 if programX == 375 and program_width >= 691:
                                     programs_width = 862
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 862:
                                         self.getControl(int(nextprogram)).setPosition(1243, int(pos_Y))




                             elif program_finished == '50':
                                 print "channel 5 here 1"
                                 if programX == 375 and program_width >= 691:
                                     programs_width = 570
                                     self.getControl(int(program_id)).setWidth(programs_width)
                                     print "channel 5 here 2"

                                     if programs_width == 570:
                                         self.getControl(int(nextprogram)).setPosition(949, int(pos_Y))




                         elif epg_time3 == '30':
                             if program_finished == '00':
                                 if programX == 375 and program_width > 692:
                                     programs_width = 1033
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 1033:
                                         self.getControl(int(nextprogram)).setPosition(1412, int(pos_Y))



                             elif program_finished == '05':
                                 if programX == 375 and program_width > 692:
                                     programs_width = 1093
                                     self.getControl(int(program_id)).setWidth(programs_width)



                             elif program_finished == '10':
                                 if programX == 375 and program_width >= 1037:
                                     programs_width = 798
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 798:
                                         self.getControl(int(nextprogram)).setPosition(1180, int(pos_Y))



                             elif program_finished == '30':
                                 if programX == 375 and program_width > 691:
                                     programs_width = 691
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 691:
                                          self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))



                             elif program_finished == '35':
                                 if programX == 375 and program_width > 691:
                                     programs_width = 750
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 750:
                                          self.getControl(int(nextprogram)).setPosition(1131, int(pos_Y))

                                          if nextprogram_width == 59:
                                             self.getControl(int(nextprogram1)).setPosition(1198, int(pos_Y))



                             elif program_finished == '40':
                                 if programX == 375 and program_width >= 691:
                                     programs_width = 803
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 803:
                                         self.getControl(int(nextprogram)).setPosition(1184, int(pos_Y))

                                         if nextprogram_width == 59:
                                             self.getControl(int(nextprogram1)).setPosition(1249, int(pos_Y))



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




             except:
                 pass

         current_program_clock_list = list()
         self.program_remaining = False




def programs_finished(self):

     if self.program_finished == True:
         self.program_finished = False
         self.program_finished_flag = True
         prog_index = [self.program_index_]
         half_hour = str(self.getControl(344).getLabel())
         one_hour = str(self.getControl(345).getLabel())
         one_hour_half = str(self.getControl(346).getLabel())
         program_stop_clock_list = list()
         program_id_list = list()
         half_hour_date_list = list()
         one_hour_date_list = list()
         one_hour_half_date_list = list()
         progId = list()
         posX = list()
         posY = list()
         programs_button = [elem.control for elem in self.program_buttons]

         for elem in programs_button:
             progId.append(elem.getId())
             posX.append(elem.getX())
             posY.append(elem.getY())
         progId = map(str, progId)
         posX = map(str, posX)
         posY = map(str, posY)


         for program_end_time in self.program_end_time:
             program_stop_hours = str(program_end_time.hour)
             program_stop_minutes = str(program_end_time.minute)
             program_stop_days = str(program_end_time.day)
             program_stop_months = str(program_end_time.month)
             program_stop_year = str(program_end_time.year)

             if program_stop_hours == "0":
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


             if program_stop_minutes == "0":
                 program_stop_minutes = "00"



             if half_hour == "11:30PM":
                 if one_hour == "12:00AM":
                     today_day = time.strftime("%d")
                     today_month = time.strftime("%m")
                     today_year = time.strftime("%Y")
                     epg_time_1_days = str(today_day)
                     epg_time_1_months = str(today_month)
                     epg_time_1_year = str(today_year)
                     epg_time_2_days = int(epg_time_1_days) + 1
                     epg_time_2_days = str(epg_time_2_days)
                     epg_time_2_months = str(epg_time_1_months)
                     epg_time_2_year = str(epg_time_1_year)
                     half_hour_date = str(epg_time_1_days + "/" + epg_time_1_months + "/" + epg_time_1_year + " " + half_hour)
                     one_hour_date = str(epg_time_2_days + "/" + epg_time_2_months + "/" + epg_time_2_year + " " + one_hour)
                     one_hour_half_date = str(epg_time_2_days + "/" + epg_time_2_months + "/" + epg_time_2_year + " " + one_hour_half)
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


             program_stop_times = str(program_stop_hours + ':' + program_stop_minutes + program_AM_PM)
             stop_time = str(program_stop_days + "/" + program_stop_months + "/" + program_stop_year + " " + program_stop_times)
             program_stop_clock_list.append(stop_time)
             half_hour_date_list.append(half_hour_date)
             one_hour_date_list.append(one_hour_date)
             one_hour_half_date_list.append(one_hour_half_date)



         for i in range(len(posX)):
             pos_X = posX[i]

             if pos_X == '375':
                 self.program_id_end_list.append(progId[i])


         if len(prog_index) >= 1:
             for index in prog_index[0]:
                 program_id_list.append(self.program_id_end_list[index])
                 program_id = self.program_id_end_list[index]
                 programX = self.getControl(int(program_id)).getX()
                 program_width = self.getControl(int(program_id)).getWidth()
                 nextprogram = int(program_id) + 1
                 nextprogramX = self.getControl(int(nextprogram)).getX()
                 nextprogram_width = self.getControl(int(nextprogram)).getWidth()
                 pos_Y = self.getControl(int(program_id)).getY()


                 if programX == 375 and program_width == 626:
                     if nextprogramX != 1008:
                         self.getControl(int(nextprogram)).setPosition(1008, int(pos_Y))


                     elif nextprogramX == 1008:
                         self.getControl(int(nextprogram)).setPosition(1007, int(pos_Y))



                 elif programX == 375 and program_width == 692:

                     if nextprogramX == 1073:
                         program_width = 691
                         self.getControl(int(program_id)).setWidth(program_width)

                         if programs_width == 691:
                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))


                     elif nextprogramX != 1073:
                         program_width = 691
                         self.getControl(int(program_id)).setWidth(program_width)

                         if program_width == 691:
                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))




         for stop_time, program_id in zip(program_stop_clock_list, program_id_list):
         #for stop_time, program_id, epg_time_1, epg_time_2, epg_time_3 in izip_longest(program_stop_clock_list, program_id_list, half_hour_date_list, one_hour_date_list, one_hour_half_date_list, fillvalue=''):
             program_stop_time = time.strptime(stop_time, '%d/%m/%Y %I:%M%p')
             half_hour = str(self.getControl(344).getLabel())
             one_hour = str(self.getControl(345).getLabel())
             one_hour_half = str(self.getControl(346).getLabel())


             if one_hour == "12:00AM":
                 #print "you are in one_hour"
                 today_day = time.strftime("%d")
                 today_month = time.strftime("%m")
                 today_year = time.strftime("%Y")
                 epg_time_1_days = int(today_day)
                 epg_time_1_days = str(epg_time_1_days)
                 epg_time_1_months = str(today_month)
                 epg_time_1_year = str(today_year)
                 epg_time_2_days = int(epg_time_1_days) + 1
                 epg_time_2_days = str(epg_time_2_days)
                 epg_time_2_months = str(today_month)
                 epg_time_2_year = str(today_year)
                 epg_time_3_days = str(epg_time_2_days)
                 epg_time_3_months = str(today_month)
                 epg_time_3_year = str(today_year)
                 half_hour_date = str(epg_time_1_days + "/" + epg_time_1_months + "/" + epg_time_1_year + " " + half_hour)
                 one_hour_date = str(epg_time_2_days + "/" + epg_time_2_months + "/" + epg_time_2_year + " " + one_hour)
                 one_hour_half_date = str(epg_time_2_days + "/" + epg_time_2_months + "/" + epg_time_2_year + " " + one_hour_half)
                 epg_time_1 = time.strptime(half_hour_date, '%d/%m/%Y %I:%M%p')
                 epg_time_2 = time.strptime(one_hour_date, '%d/%m/%Y %I:%M%p')
                 epg_time_3 = time.strptime(one_hour_half_date, '%d/%m/%Y %I:%M%p')


             elif one_hour_half == "12:00AM":
                 today_day = time.strftime("%d")
                 today_month = time.strftime("%m")
                 today_year = time.strftime("%Y")
                 epg_time_1_days = int(today_day)
                 epg_time_1_days = str(epg_time_1_days)
                 epg_time_1_months = str(today_month)
                 epg_time_1_year = str(today_year)
                 epg_time_2_days = str(epg_time_2_days)
                 epg_time_2_months = str(epg_time_1_months)
                 epg_time_2_year = str(epg_time_1_year)
                 epg_time_3_days = int(epg_time_2_days) + 1
                 epg_time_3_days = str(epg_time_3_days)
                 epg_time_3_months = str(epg_time_2_months)
                 epg_time_3_year = str(epg_time_2_year)
                 half_hour_date = str(epg_time_1_days + "/" + epg_time_1_months + "/" + epg_time_1_year + " " + half_hour)
                 one_hour_date = str(epg_time_2_days + "/" + epg_time_2_months + "/" + epg_time_2_year + " " + one_hour)
                 one_hour_half_date = str(epg_time_3_days + "/" + epg_time_3_months + "/" + epg_time_3_year + " " + one_hour_half)
                 epg_time_1 = time.strptime(half_hour_date, '%d/%m/%Y %I:%M%p')
                 epg_time_2 = time.strptime(one_hour_date, '%d/%m/%Y %I:%M%p')
                 epg_time_3 = time.strptime(one_hour_half_date, '%d/%m/%Y %I:%M%p')

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
                 epg_time_1 = time.strptime(half_hour_date, '%d/%m/%Y %I:%M%p')
                 epg_time_2 = time.strptime(one_hour_date, '%d/%m/%Y %I:%M%p')
                 epg_time_3 = time.strptime(one_hour_half_date, '%d/%m/%Y %I:%M%p')


             if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                 print("Now you are working on resize on the button")
                 nextprogram = int(program_id) + 1
                 nextprogram_exist = self.getControl(int(nextprogram))
                 program_width = self.getControl(int(program_id)).getWidth()
                 nextprogram_width = self.getControl(int(nextprogram)).getWidth()
                 nextprogram1 = int(nextprogram) + 1
                 nextprogram1X = self.getControl(int(nextprogram1)).getX()
                 nextprogram1_width = self.getControl(int(nextprogram1)).getWidth()
                 nextprogram2 = int(nextprogram1) + 1
                 nextprogram2X = self.getControl(int(nextprogram2)).getX()
                 nextprogram2_width = self.getControl(int(nextprogram2)).getWidth()
                 pos_X = self.getControl(int(program_id)).getX()
                 pos_Y = self.getControl(int(program_id)).getY()
                 self.nextprogram_clock = list()
                 self.nextprogram_clock.append(program_id)
                 self.nextprogram_id = list()
                 self.nextprogram_id.append(program_id)
                 self.select_db_flag = True
                 self.select_db()
                 program_clock = ''.join(str(x) for x in self.nextprogram_clock)
                 program_clock = str(program_clock)
                 program_stop_clock = ''.join(str(x) for x in self.nextprogram_stop_clock)
                 program_stop_clock = str(program_stop_clock)
                 program_stop_time = time.strptime(program_clock, '%d/%m/%Y %I:%M%p')
                 program_finished = program_stop_clock.split(':')[1].replace('PM', '').replace('AM', '')
                 print "program_finished for working on resize"
                 #print program_finished


                 if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                     if program_finished == '05':
                         if programX == 375 and program_width >= 342:
                             self.program_remaining = True
                             programs_remaining(self)


                     elif program_finished == '10':
                         if programX == 375 and program_width >= 286:
                             self.program_remaining = True
                             programs_remaining(self)



                     elif program_finished == '15':
                         if programX == 375 and program_width >= 515:
                             self.program_remaining = True
                             programs_remaining(self)



                     elif program_finished == '20':
                         if programX == 375 and program_width >= 456:
                             self.program_remaining = True
                             programs_remaining(self)




                     elif program_finished == '25':
                         if programX == 375 and program_width >= 515:
                             self.program_remaining = True
                             programs_remaining(self)



                     elif program_finished == '35':
                         if programX == 375 and program_width >= 117:
                             self.program_remaining = True
                             programs_remaining(self)
                             self.nextprogram_id.append(program_id)
                             print "fi this programs remaining for channel 5"



                     elif program_finished == '40':
                         if program_width == 59 and nextprogram_width == 227:
                             if nextprogram1X == 675:
                                 self.program_remaining = True
                                 programs_remaining(self)



                         elif program_width >= 515:
                             self.program_remaining = True
                             programs_remaining(self)



                     elif program_finished == '45':
                         if program_width >= 286:
                             self.program_remaining = True
                             programs_remaining(self)



                     elif program_finished == '50':
                         if program_width == 167 and nextprogram_width == 117:
                             if nextprogram1X == 673:
                                 self.program_remaining = True
                                 programs_remaining(self)



                         elif program_width == 227 and nextprogram_width == 117:
                             if nextprogram1X == 733:
                                 self.program_remaining = True
                                 programs_remaining(self)



                         elif program_width >= 567:
                             self.program_remaining = True
                             programs_remaining(self)




                     elif program_finished == '55':
                         if program_width >= 286:
                             self.program_remaining = True
                             programs_remaining(self)




             elif program_stop_time <= epg_time_1:
                 print("Now you are working on to remove the data in the database")