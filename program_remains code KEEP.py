            if self.program_remaining == True:
                 self.program_remaining = False
                 progId = list()
                 posX = list()
                 posY = list()
                 program_length = list()
                 prog_id_list = list()
                 prog_length_list = list()
                 pos_X_list = list()

                 for elem in programs_button:
                     progId.append(elem.getId())
                     posX.append(elem.getX())
                     posY.append(elem.getY())
                     program_length.append(elem.getWidth())
                 progId = map(str, progId)
                 posX = map(str, posX)
                 posY = map(str, posY)
                 program_length = map(str, program_length)
                 prog_index_list = map(str, program_index_)
                 channel_1 = list()
                 current_program_clock_list = list()


                 #Store the list of strings in the lists
                 for i in range(len(posX)):
                     pos_X = posX[i]

                     if pos_X == '375':
                         prog_id_list.append(progId[i])
                         prog_length_list.append(program_length[i])
                         pos_X_list.append(posX[i])



                 #for pos_X, pos_Y, prog_id, prog_index in izip_longest(posX, posY, progId, program_index_, fillvalue=''):
                 for pos_X, pos_Y, prog_id in zip(posX, posY, progId):
                     if int(pos_X) == 375:
                         prog_index = [program_index_]

                         if len(program_index_) >= 1:
                             for index in prog_index[0]:
                                 prog_ids = prog_id_list[index]
                                 prog_length = prog_length_list[index]
                                 prog_length = int(prog_length)
                                 self.program_id.append(prog_ids)
                                 self.program_width.append(prog_length)




                     #-----------------------my orginal code keep
                     #if int(pos_X) == 375:
                         #next_posX = int(pos_X) + 1
                         #program_width = self.getControl(int(prog_id)).getWidth()

                         #if int(next_posX) == 606:
                             #if program_width == 232:
                                 #next_progId = prog_id + 1
                                 #posY = self.getControl(int(next_progId)).getY()
                                 #self.getControl(int(next_progId)).setPosition(897, int(posY))



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

                     if one_hour == "12:00AM":
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



                 for program_stop_clock, program_stop_times, program_width, program_id in izip_longest(self.program_finished_clock, current_program_clock_list, self.program_width, self.program_id, fillvalue=''):
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
                             print "here 2"

                             if program_finished == '00':
                                 if program_stop_time == epg_time_2:
                                     if programX == 375 and program_width == 692:
                                         programs_width = 342
                                         self.getControl(int(program_id)).setWidth(programs_width)
                                         self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))

                                         if nextprogram_width == 342:
                                             self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))

                                         elif nextprogram_width == 456:
                                             self.getControl(int(nextprogram1)).setPosition(1188, int(pos_Y))


                                     elif programX == 375 and program_width > 342:
                                         programs_width = 342
                                         self.getControl(int(program_id)).setWidth(programs_width)
                                         self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))

                                         if nextprogram_width == 342:
                                             self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))



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
                                 if programX == 375 and program_width == 342:
                                     print program_finished




                         elif program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                             print "here 3"

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
                                 if program_stop_time > epg_time_1:
                                     if programX == 375 and program_width <= 741:
                                         programs_width = 59
                                         self.getControl(int(program_id)).setWidth(programs_width)
                                         self.getControl(int(nextprogram)).setPosition(440, int(pos_Y))

                                         if nextprogram_width == 396:
                                             self.getControl(int(nextprogram1)).setPosition(842, int(pos_Y))

                                         elif nextprogram_width == 626:
                                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))



                             elif program_finished == '10':
                                 if program_stop_time > epg_time_3:
                                     if programX == 375 and program_width >= 1037:
                                         programs_width = 798
                                         self.getControl(int(program_id)).setWidth(programs_width)
                                         self.getControl(int(nextprogram)).setPosition(1180, int(pos_Y))



                             elif program_finished == '20':
                                 if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                                     if programX == 375 and program_width >= 232:
                                         programs_width = 232
                                         self.getControl(int(program_id)).setWidth(programs_width)
                                         self.getControl(int(program_id)).setVisible(False)
                                         self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                                         self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))

                                         if nextprogram_width == 692:
                                             self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))



                                     #elif programX == 375 and program_width >= 342:
                                         #programs_width = 232
                                         #self.getControl(int(program_id)).setWidth(programs_width)
                                         #self.getControl(int(nextprogram)).setPosition(614, int(pos_Y))



                             elif program_finished == '25':
                                 if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                                     if programX == 375 and program_width >= 456:
                                         programs_width = 278
                                         self.getControl(int(program_id)).setWidth(programs_width)
                                         self.getControl(int(nextprogram)).setPosition(660, int(pos_Y))

                                         if nextprogram_width == 456:
                                             self.getControl(int(nextprogram1)).setPosition(1124, int(pos_Y))



                             elif program_finished == '30':
                                 if program_stop_time == epg_time_3:
                                     if programX == 375 and program_width >= 1038:
                                         programs_width = 692
                                         self.getControl(int(program_id)).setWidth(programs_width)
                                         self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))



                             elif program_finished == '35':
                                 if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                                     if int(current_time) >= 0 and int(current_time) < 29:
                                         if programX == 375 and program_width >= 741:
                                             programs_width = 399
                                             self.getControl(int(program_id)).setWidth(programs_width)
                                             self.getControl(int(nextprogram)).setPosition(780, int(pos_Y))

                                             if nextprogram_width == 286:
                                                 self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))
                                                 #self.getControl(int(nextprogram1)).setVisible(True)


                                     elif int(current_time) >= 30 and int(current_time) < 59:
                                         if programX == 375 and program_width >= 741:
                                             self.getControl(int(program_id)).setVisible(False)
                                             self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                                             self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))

                                             if nextprogram_width == 286:
                                                 programs_width = 342
                                                 self.getControl(int(nextprogram)).setWidth(programs_width)
                                                 self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))
                                                 self.getControl(int(nextprogram1)).setVisible(True)



                                 elif program_stop_time > epg_time_3:
                                     if programX == 375 and program_width >= 741:
                                         programs_width = 750
                                         self.getControl(int(program_id)).setWidth(programs_width)
                                         self.getControl(int(nextprogram)).setPosition(1132, int(pos_Y))




                             elif program_finished == '40':
                                 if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                                     if programX == 375 and program_width == 59:
                                         print "passed 2"
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
                                                     programs_width = 276
                                                     self.getControl(int(nextprogram)).setWidth(programs_width)
                                                     self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))



                                     elif programX == 375 and program_width >= 342:
                                         programs_width = 117
                                         self.getControl(int(program_id)).setWidth(programs_width)
                                         self.getControl(int(nextprogram)).setPosition(499, int(pos_Y))

                                         if nextprogram_width == 515:
                                             self.getControl(int(nextprogram1)).setPosition(1020, int(pos_Y))



                             elif program_finished == '45':
                                 print "hello chris"
                                 if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                                     if programX == 375 and program_width >= 342:
                                         programs_width = 167
                                         self.getControl(int(program_id)).setWidth(programs_width)
                                         self.getControl(int(nextprogram)).setPosition(549, int(pos_Y))

                                         if nextprogram_width == 515:
                                             programs_width = 517
                                             self.getControl(int(nextprogram)).setWidth(programs_width)
                                             self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))


                                 elif program_stop_time > epg_time_2 and program_stop_time < epg_time_3:
                                     if programX == 375 and program_width >= 342:
                                         programs_width = 516
                                         self.getControl(int(program_id)).setWidth(programs_width)
                                         self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))

                                         #if nextprogram_width == 515:
                                             #programs_width = 517
                                             #self.getControl(int(nextprogram)).setWidth(programs_width)
                                             #self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))



                                 elif program_stop_time == epg_time_3:
                                     if programX == 375 and program_width >= 692:
                                         programs_width = 691
                                         self.getControl(int(program_id)).setWidth(programs_width)
                                         self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))



                             elif program_finished == '50':
                                 if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                                     if programX == 375 and program_width == 227 and nextprogram_width == 117:
                                         programs_width = 224
                                         self.getControl(int(program_id)).setWidth(programs_width)
                                         self.getControl(int(nextprogram)).setPosition(606, int(pos_Y))

                                         if nextprogram_width == 117:
                                             programs_width = 111
                                             self.getControl(int(nextprogram)).setWidth(programs_width)
                                             self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))



                                     elif programX == 375 and program_width >= 626:
                                         programs_width = 227
                                         self.getControl(int(program_id)).setWidth(programs_width)


                                         if nextprogram_width == 117:
                                             programs_width = 112
                                             self.getControl(int(nextprogram)).setWidth(programs_width)


                             elif program_finished == '55':
                                 if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                                     if programX == 375 and program_width >= 342:

                                         if nextprogram_width == 59:
                                             programs_width = 277
                                             self.getControl(int(program_id)).setWidth(programs_width)
                                             self.getControl(int(nextprogram)).setPosition(659, int(pos_Y))

                                             if nextprogram1X == 1073:
                                                 self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))


                                         else:
                                             programs_width = 283
                                             self.getControl(int(program_id)).setWidth(programs_width)
                                             self.getControl(int(nextprogram)).setPosition(664, int(pos_Y))



                                     #if program_length == 798:
                                         #prog_width = 692
                                         #self.getControl(int(program_id)).setWidth(prog_width)




                         elif program_stop_time > epg_time_2 and program_stop_time < epg_time_3:
                             print "here 4"

                             if program_finished == '00':
                                 if programX == 375 and program_width == 342:
                                     programs_width = 342
                                     self.getControl(int(program_id)).setWidth(programs_width)
                                     self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))



                                 elif programX == 375 and program_width >= 515:
                                     programs_width = 342
                                     self.getControl(int(program_id)).setWidth(programs_width)
                                     self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))


                             elif program_finished == '10':
                                 if programX == 375 and program_width <= 692:
                                     programs_width = 456
                                     #self.getControl(int(program_id)).setWidth(programs_width)
                                     #self.getControl(int(nextprogram)).setPosition(837, int(pos_Y))


                             elif program_finished == '20':
                                 if programX == 375 and program_width >= 1038:
                                     programs_width = 577
                                     self.getControl(int(program_id)).setWidth(programs_width)



                             elif program_finished == '25':
                                 if programX == 375 and program_width >= 969:
                                     programs_width = 627
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if nextprogramX != 949:
                                         self.getControl(int(nextprogram)).setPosition(1008, int(pos_Y))



                             elif program_finished == '30':
                                 if programX == 375 and program_width >= 1038:
                                     programs_width = 342
                                     self.getControl(int(program_id)).setWidth(programs_width)



                             elif program_finished == '35':
                                 if programX == 375 and program_width >= 1038:
                                     programs_width = 399
                                     self.getControl(int(program_id)).setWidth(programs_width)
                                     self.getControl(int(nextprogram)).setPosition(780, int(pos_Y))

                                     if nextprogram_width == 286:
                                         self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))



                             elif program_finished == '40':
                                 if programX == 375 and program_width > 692:
                                     programs_width = 456
                                     self.getControl(int(program_id)).setWidth(programs_width)
                                     self.getControl(int(nextprogram)).setPosition(838, int(pos_Y))



                             elif program_finished == '45':
                                 if programX == 375 and program_width >= 691:
                                     programs_width = 577
                                     self.getControl(int(program_id)).setWidth(programs_width)
                                     self.getControl(int(nextprogram)).setPosition(958, int(pos_Y))



                             #if int(current_time) >= 00 and int(current_time) < 29:
                                 #if program_finished == '05':
                                     #if program_width >= 515:
                                         #programs_width = 396
                                         #self.getControl(int(program_id)).setWidth(programs_width)
                                         #self.getControl(int(nextprogram)).setPosition(779, int(pos_Y))


                                 #elif program_finished == '10':
                                     #if program_width >= 692:
                                         #programs_width = 456
                                         #self.getControl(int(program_id)).setWidth(programs_width)


                                 #elif program_finished == '15':
                                     #if program_width == 692:
                                         #programs_width = 515
                                         #self.getControl(int(program_id)).setWidth(programs_width)


                                     #elif program_width == 515:
                                         #programs_width = 167
                                         #self.getControl(int(program_id)).setWidth(programs_width)
                                         #self.getControl(int(nextprogram)).setPosition(549, int(pos_Y))



                                     #elif program_width == 567:
                                         #programs_width = 167
                                         #self.getControl(int(program_id)).setWidth(programs_width)
                                         #self.getControl(int(nextprogram)).setPosition(838, int(pos_Y))



                                 #elif program_finished == '20':
                                     #if program_width == 692:
                                         #programs_width = 567
                                         #self.getControl(int(program_id)).setWidth(programs_width)



                                 #elif program_finished == '30':
                                     #if program_width >= 515:
                                         #prog_width = 342
                                         #self.getControl(int(program_id)).setWidth(prog_width)

                                         #if nextprograms_width == 342:
                                             #if nextprogram_width == 286 and nextprograms_width == 59:
                                                 #programs_width = 276
                                                 #self.getControl(int(nextprogram)).setWidth(programs_width)



                                 #elif program_finished == '45':
                                     #if program_width >= 692:
                                         #programs_width = 515
                                         #self.getControl(int(program_id)).setWidth(programs_width)
                                         #self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))



                                 #elif program_finished == '50':
                                     #if program_width == 1083:
                                         #programs_width = 741
                                         #self.getControl(int(program_id)).setWidth(programs_width)


                                     #elif program_width == 1368:
                                         #programs_width = 1026
                                         #self.getControl(int(program_id)).setWidth(programs_width)



                                     #elif program_width == 692:
                                         #programs_width = 577
                                         #self.getControl(int(program_id)).setWidth(programs_width)



                                     #elif program_width == 626:
                                         #programs_width = 286
                                         #self.getControl(int(program_id)).setWidth(programs_width)


                                     #elif program_width == 342:
                                         #programs_width = 232
                                         #self.getControl(int(program_id)).setWidth(programs_width)



                             #if int(current_time) >= 30 and int(current_time) < 59:
                                 #if program_finished == '15':
                                     #if program_width >= 567:
                                         #programs_width = 515
                                         #self.getControl(int(program_id)).setWidth(programs_width)
                                         #self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))



                             #if program_stop_time > epg_time_3:
                                 #if program_finished == '00':
                                     #if program_width == 1368:
                                         #programs_width = 1026
                                         #self.getControl(int(program_id)).setWidth(programs_width)




                         elif program_stop_time == epg_time_3:
                             print "here 5"

                             if program_finished == '00':
                                 if programX == 375 and program_width == 692:
                                     if nextprogramX != 1073:
                                         self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))



                                 elif programX == 375 and program_width >= 1038:
                                     programs_width = 691
                                     self.getControl(int(program_id)).setWidth(programs_width)
                                     self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))



                             elif program_finished == '30':
                                 if programX == 375 and program_width >= 1038:
                                     programs_width = 692
                                     self.getControl(int(program_id)).setWidth(programs_width)
                                     self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))




                         elif program_stop_time > epg_time_3:
                             print "here 6"
                             epg_time3 = str(self.getControl(346).getLabel())
                             epg_time3 = epg_time3.split(":")[1].replace('AM', '').replace('PM', '')


                             if epg_time3 == '00':
                                 if program_finished == '05':
                                     if programX == 375 and program_width > 692:
                                         programs_width = 751
                                         self.getControl(int(program_id)).setWidth(programs_width)


                                 elif program_finished == '10':
                                     if programX == 375 and program_width >= 1037:
                                         programs_width = 798
                                         self.getControl(int(program_id)).setWidth(programs_width)
                                         self.getControl(int(nextprogram)).setPosition(1180, int(pos_Y))



                             elif epg_time3 == '30':
                                 if program_finished == '35':
                                     if programX == 375 and program_width >= 1038:
                                         programs_width = 750
                                         self.getControl(int(program_id)).setWidth(programs_width)
                                         self.getControl(int(nextprogram)).setPosition(1131, int(pos_Y))



                     except:
                         pass

                 current_program_clock_list = list()
                 self.program_remaining = False