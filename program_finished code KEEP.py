if self.program_finished == True:
                 self.program_finished = False
                 self.program_finished_flag = True
                 prog_index = [self.program_index_list]
                 half_hour = str(self.getControl(344).getLabel())
                 one_hour = str(self.getControl(345).getLabel())
                 one_hour_half = str(self.getControl(346).getLabel())
                 program_stop_clock_list = list()
                 program_id_list = list()
                 half_hour_date_list = list()
                 one_hour_date_list = list()
                 one_hour_half_date_list = list()


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

                                 if programs_width == 691:
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
                         print program_finished
                         print "self.nextprogram_clock"
                         print self.nextprogram_clock


                         #ass6a
                         if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                             if program_finished == '05':
                                 if programX == 375 and program_width >= 342:
                                     programs_width = 59
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 59:
                                         self.getControl(int(nextprogram)).setPosition(441, int(pos_Y))
                                         print "you are here now chris"

                                         if nextprogram_width == 59:
                                             self.getControl(int(nextprogram1)).setPosition(504, int(pos_Y))


                                         elif nextprogram_width == 167:
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
                                             self.getControl(int(nextprogram1)).setPosition(844, int(pos_Y))

                                             if nextprogram1_width == 167:
                                                 self.getControl(int(nextprogram2)).setPosition(1018, int(pos_Y))


                                             elif nextprogram1_width == 342:
                                                 self.getControl(int(nextprogram2)).setPosition(1190, int(pos_Y))



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


                                         elif nextprogram_width == 342:
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



                             elif program_finished == '15':
                                 if programX == 375 and program_width >= 515:
                                     programs_width = 167
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 167:
                                         self.getControl(int(nextprogram)).setPosition(549, int(pos_Y))

                                         if nextprogram_width == 227:
                                             nextprogram_width = 221
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 221:
                                                 self.getControl(int(nextprogram1)).setPosition(774, int(pos_Y))

                                                 if nextprogram1_width == 117:
                                                     self.getControl(int(nextprogram2)).setPosition(897, int(pos_Y))


                                         elif nextprogram_width == 342:
                                             self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))

                                             if nextprogram1_width == 117:
                                                 self.getControl(int(nextprogram2)).setPosition(1020, int(pos_Y))


                                             elif nextprogram1_width == 227:
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



                                         elif nextprogram_width == 567:
                                             nextprogram_width = 582
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 582:
                                                 self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))



                                         elif nextprogram_width == 515:
                                             nextprogram_width = 517
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 517:
                                                 self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))


                                         elif nextprogram_width == 692:
                                             nextprogram_width = 691
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 691:
                                                 self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))



                             elif program_finished == '20':
                                 if programX == 375 and program_width >= 456:
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



                                         elif nextprogram_width == 342:
                                             nextprogram_width = 332
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 332:
                                                 self.getControl(int(nextprogram1)).setPosition(949, int(pos_Y))


                                         elif nextprogram_width == 399:
                                                 self.getControl(int(nextprogram1)).setPosition(1016, int(pos_Y))


                                         elif nextprogram_width == 456:
                                             nextprogram_width = 457
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 457:
                                                 self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))


                                         elif nextprogram_width == 516:
                                                 self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))


                                         elif nextprogram_width == 567:
                                                 self.getControl(int(nextprogram1)).setPosition(1134, int(pos_Y))


                                         elif nextprogram_width == 626:
                                             self.getControl(int(nextprogram1)).setPosition(1242, int(pos_Y))




                             elif program_finished == '25':
                                 if programX == 375 and program_width >= 515:
                                     programs_width = 277
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 277:
                                         self.getControl(int(nextprogram)).setPosition(659, int(pos_Y))

                                         if nextprogram_width == 59:
                                             self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))


                                         elif nextprogram_width == 342:
                                             self.getControl(int(nextprogram1)).setPosition(1007, int(pos_Y))


                                         elif nextprogram_width == 399:
                                             self.getControl(int(nextprogram1)).setPosition(1119, int(pos_Y))


                                         elif nextprogram_width == 456:
                                             self.getControl(int(nextprogram1)).setPosition(1230, int(pos_Y))


                                         elif nextprogram_width == 567:
                                             self.getControl(int(nextprogram1)).setPosition(1232, int(pos_Y))



                             elif program_finished == '35':
                                 if programX == 375 and program_width >= 117:
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

                                                 if nextprogram1_width == 342:
                                                     self.getControl(int(nextprogram2)).setPosition(897, int(pos_Y))


                                                 elif nextprogram1_width == 692:
                                                     nextprogram1_width = 691
                                                     self.getControl(int(nextprogram2)).setWidth(nextprogram1_width)

                                                     if nextprogram1_width == 691:
                                                         self.getControl(int(nextprogram3)).setPosition(1246, int(pos_Y))



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



                                             elif nextprogram_width == 567:
                                                 self.getControl(int(nextprogram1)).setPosition(1016, int(pos_Y))


                                             elif nextprogram_width == 692:
                                                 nextprogram_width = 689
                                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                 if nextprogram_width == 689:
                                                     self.getControl(int(nextprogram1)).setPosition(1138, int(pos_Y))



                                         elif nextprogram_width == 286:
                                             nextprogram_width = 277
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 277:
                                                 self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))



                                         elif nextprogram_width == 342:
                                             nextprogram_width = 342
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 342:
                                                 self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))

                                                 if nextprogram1_width == 342:
                                                     nextprogram1_width = 336
                                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                     if nextprogram1_width == 336:
                                                         self.getControl(int(nextprogram2)).setPosition(1134, int(pos_Y))



                                         elif nextprogram_width == 456:
                                             nextprogram_width = 449
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 449:
                                                 self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))



                                         elif nextprogram_width == 626:
                                             nextprogram1_width = 624
                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                             if nextprogram1_width == 624:
                                                 self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))



                             elif program_finished == '40':
                                 if program_width == 59 and nextprogram_width == 227:
                                     if nextprogram1X == 675:
                                         self.nextprogram_id = list()
                                         self.nextprogram_id.append(nextprogram)
                                         self.select_db_flag = True
                                         self.select_db()
                                         nextprogram_clock = ''.join(str(x) for x in self.nextprogram_clock)
                                         nextprogram_clock = str(nextprogram_clock)
                                         nextprogram_stop_clock = ''.join(str(x) for x in self.nextprogram_stop_clock)
                                         nextprogram_stop_clock = str(nextprogram_stop_clock)
                                         program_stop_time = time.strptime(nextprogram_clock, '%d/%m/%Y %I:%M%p')


                                         if program_stop_time == epg_time_2:
                                             if nextprogram1X == 675:
                                                 programs_width = 276
                                                 self.getControl(int(nextprogram)).setWidth(programs_width)

                                                 if programs_width == 276:
                                                     self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))



                                 elif program_width >= 515:
                                     programs_width = 125
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 125:
                                         self.getControl(int(nextprogram)).setPosition(507, int(pos_Y))

                                         if nextprogram_width == 59:
                                             self.getControl(int(nextprogram1)).setPosition(568, int(pos_Y))


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


                                         elif nextprogram_width == 342:
                                             self.getControl(int(nextprogram1)).setPosition(847, int(pos_Y))

                                             if nextprogram1_width == 342:
                                                 self.getControl(int(nextprogram2)).setPosition(1196, int(pos_Y))



                                         elif nextprogram_width == 515:
                                             nextprogram_width = 502
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)


                                         elif nextprogram_width == 516:
                                             nextprogram_width = 502
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)


                                         elif nextprogram_width == 567:
                                             self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))

                                             if nextprogram1_width == 117:
                                                 self.getControl(int(nextprogram2)).setPosition(1197, int(pos_Y))



                                         elif nextprogram_width == 692:
                                             nextprogram_width = 691
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 691:
                                                 self.getControl(int(nextprogram1)).setPosition(1197, int(pos_Y))



                             elif program_finished == '45':
                                 if program_width >= 286:
                                     programs_width = 167
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 167:
                                         self.getControl(int(nextprogram)).setPosition(549, int(pos_Y))

                                         if nextprogram_width == 59:
                                             self.getControl(int(nextprogram1)).setPosition(615, int(pos_Y))

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



                                         elif nextprogram_width == 626:
                                             self.getControl(int(nextprogram1)).setPosition(1183, int(pos_Y))


                                         elif nextprogram_width == 692:
                                             nextprogram_width = 691
                                             self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                             if nextprogram_width == 691:
                                                 self.getControl(int(nextprogram1)).setPosition(1246, int(pos_Y))



                             elif program_finished == '50':
                                 if program_width == 167 and nextprogram_width == 117:
                                     if nextprogram1X == 673:
                                         self.getControl(int(nextprogram1)).setPosition(672, int(pos_Y))



                                 elif program_width == 227 and nextprogram_width == 117:
                                     if nextprogram1X == 733:
                                         self.nextprogram_id = list()
                                         self.nextprogram_id.append(nextprogram)
                                         self.select_db_flag = True
                                         self.select_db()
                                         nextprogram_clock = ''.join(str(x) for x in self.nextprogram_clock)
                                         nextprogram_clock = str(nextprogram_clock)
                                         nextprogram_stop_clock = ''.join(str(x) for x in self.nextprogram_stop_clock)
                                         nextprogram_stop_clock = str(nextprogram_stop_clock)
                                         program_stop_time = time.strptime(nextprogram_clock, '%d/%m/%Y %I:%M%p')


                                         if program_stop_time == epg_time_2:
                                             programs_width = 224
                                             self.getControl(int(program_id)).setWidth(programs_width)

                                             if programs_width == 224:
                                                 self.getControl(int(nextprogram)).setPosition(606, int(pos_Y))

                                                 if nextprogram_width == 117:
                                                     nextprogram_width = 111
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 111:
                                                         self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))



                                 elif program_width >= 567:
                                     programs_width = 228
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 228:
                                         self.getControl(int(nextprogram)).setPosition(610, int(pos_Y))

                                         if nextprogram_width == 59:
                                             self.getControl(int(nextprogram1)).setPosition(676, int(pos_Y))
 
 
 
                                         elif nextprogram_width == 167:
                                             self.getControl(int(nextprogram1)).setPosition(783, int(pos_Y))


                                         elif nextprogram_width == 342:
                                             self.getControl(int(nextprogram1)).setPosition(958, int(pos_Y))


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


                                         elif nextprogram_width == 567:
                                             self.getControl(int(nextprogram1)).setPosition(1184, int(pos_Y))


                                         elif nextprogram_width == 626:
                                                 self.getControl(int(nextprogram1)).setPosition(1243, int(pos_Y))




                             elif program_finished == '55':
                                 if program_width >= 286:
                                     programs_width = 276
                                     self.getControl(int(program_id)).setWidth(programs_width)

                                     if programs_width == 276:
                                         self.getControl(int(nextprogram)).setPosition(659, int(pos_Y))

                                         if nextprogram_width == 59:
                                             self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))

                                             if nextprogram1_width == 286:
                                                 self.getControl(int(nextprogram2)).setPosition(1018, int(pos_Y))

                                                 if nextprogram2_width == 227:
                                                     self.getControl(int(nextprogram3)).setPosition(1251, int(pos_Y))


                                             elif nextprogram1_width == 342:
                                                 self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))


                                             elif nextprogram1_width >= 399:
                                                 self.getControl(int(nextprogram2)).setPosition(1421, int(pos_Y))



                                         elif nextprogram_width == 342:
                                             self.getControl(int(nextprogram1)).setPosition(957, int(pos_Y))



                     #elif program_stop_time <= epg_time_1:
                     elif program_stop_time <= epg_time_1:
                         print("Now you are working on to remove the button")
                         nextprogram = int(program_id) + 1
                         program_width = self.getControl(int(program_id)).getWidth()
                         programX = self.getControl(int(program_id)).getX()
                         nextprogram_width = self.getControl(int(nextprogram)).getWidth()
                         nextprogram1 = int(nextprogram) + 1
                         nextprogram1_X = self.getControl(int(nextprogram1)).getX()
                         nextprogram1_width = self.getControl(int(nextprogram1)).getWidth()
                         nextprogram2 = int(nextprogram1) + 1
                         nextprogram2_X = self.getControl(int(nextprogram2)).getX()
                         nextprogram2_width = self.getControl(int(nextprogram2)).getWidth()
                         nextprogram3 = int(nextprogram2) + 1
                         nextprogram3_X = self.getControl(int(nextprogram3)).getX()
                         nextprogram3_width = self.getControl(int(nextprogram3)).getWidth()
                         nextprogram4 = int(nextprogram3) + 1
                         nextprogram4_X = self.getControl(int(nextprogram4)).getX()
                         nextprogram4_width = self.getControl(int(nextprogram4)).getWidth()
                         pos_X = self.getControl(int(program_id)).getX()
                         pos_Y = self.getControl(int(program_id)).getY()
                         today_day = time.strftime("%d")
                         today_month = time.strftime("%m")
                         today_year = time.strftime("%Y")
                         self.nextprogram_id = list()
                         self.nextprogram_id.append(program_id)
                         self.select_db_flag = True
                         self.select_db()
                         nextprogram_clock = ''.join(str(x) for x in self.nextprogram_clock)
                         nextprogram_clock = str(nextprogram_clock)
                         nextprogram_stop_clock = ''.join(str(x) for x in self.nextprogram_stop_clock)
                         nextprogram_stop_clock = str(nextprogram_stop_clock)
                         program_stop_time = time.strptime(nextprogram_clock, '%d/%m/%Y %I:%M%p')
                         program_finished = nextprogram_stop_clock.split(':')[1].replace('PM', '').replace('AM', '')
                         print "program_finished"
                         print program_finished


                         if program_stop_time <= epg_time_1:
                             self.remove_controls = list()

                             try:
                             #if self.program_finished_flag == True:
                                 program_button = self.getControl(int(program_id))

                                 if program_button:
                                     print "let remove program_button"
                                     self.remove_controls = list()
                                     removeButtons = self.getControl(int(program_id))
                                     self.remove_controls.append(removeButtons)
                                     self.Remove_Buttons()

                                     if nextprogram_width >= 59:
                                         self.nextprogram_id = list()
                                         self.nextprogram_id.append(nextprogram)
                                         self.select_db_flag = True
                                         self.select_db()
                                         nextprogram_clock = ''.join(str(x) for x in self.nextprogram_clock)
                                         nextprogram_clock = str(nextprogram_clock)
                                         nextprogram_stop_clock = ''.join(str(x) for x in self.nextprogram_stop_clock)
                                         nextprogram_stop_clock = str(nextprogram_stop_clock)
                                         nextprogram_stop_time = time.strptime(nextprogram_clock, '%d/%m/%Y %I:%M%p')
                                         nextprogram_finished = nextprogram_stop_clock.split(':')[1].replace('PM', '').replace('AM', '')
                                         print "nextprogram_stop_time"
                                         print nextprogram_stop_time


                                         if nextprogram_stop_time <= epg_time_1:
                                             self.remove_controls = list()
                                             removeButtons = self.getControl(int(nextprogram))
                                             self.remove_controls.append(removeButtons)
                                             self.Remove_Buttons()
                                             self.getControl(int(nextprogram1)).setPosition(375, int(pos_Y))


                                             if nextprogram1_width < 692:
                                                 print "692 you are here 1"
                                                 self.nextprogram_id = list()
                                                 self.nextprogram_id.append(nextprogram1)
                                                 self.select_db_flag = True
                                                 self.select_db()
                                                 nextprogram1_clock = ''.join(str(x) for x in self.nextprogram_clock)
                                                 nextprogram1_clock = str(nextprogram1_clock)
                                                 nextprogram1_stop_clock = ''.join(str(x) for x in self.nextprogram_stop_clock)
                                                 nextprogram1_stop_clock = str(nextprogram1_stop_clock)
                                                 nextprogram1_stop_time = time.strptime(nextprogram1_clock, '%d/%m/%Y %I:%M%p')
                                                 program_finished = nextprogram1_stop_clock.split(':')[1].replace('PM', '').replace('AM', '')
                                                 print "program_finished"
                                                 print program_finished
                                                 print "nextprogram1_stop_time"
                                                 print nextprogram1_stop_time


                                                 if nextprogram1_stop_time > epg_time_1 and nextprogram1_stop_time < epg_time_2:
                                                     print "here chris code here"

                                                     if program_finished == '25':
                                                         if nextprogram1_width == 286:
                                                             self.getControl(int(nextprogram2)).setPosition(667, int(pos_Y))

                                                             if nextprogram2_width == 227:
                                                                 nextprogram2_width = 224
                                                                 self.getControl(int(nextprogram2)).setWidth(nextprogram2_width)

                                                                 if nextprogram2_width == 224:
                                                                     self.getControl(int(nextprogram3)).setPosition(897, int(pos_Y))


                                                     if program_finished == '55':
                                                         if nextprogram1_width >= 342:
                                                             nextprogram1_width = 276
                                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                             if nextprogram1_width == 276:
                                                                 self.getControl(int(nextprogram2)).setPosition(659, int(pos_Y))

                                                                 if nextprogram2_width == 59:
                                                                     self.getControl(int(nextprogram3)).setPosition(724, int(pos_Y))



                                                 elif nextprogram1_stop_time == epg_time_1:
                                                     if nextprogram1_width == 342:
                                                         self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))

                                                         if nextprogram2_width == 342:
                                                             self.getControl(int(nextprogram3)).setPosition(1073, int(pos_Y))



                                                 elif nextprogram1_stop_time == epg_time_2:
                                                     print "passed 1a"
                                                     nextprogram1_width = 342
                                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                     if nextprogram1_width == 342:
                                                         self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))

                                                         if nextprogram2_width == 286:
                                                             nextprogram2_width = 276
                                                             self.getControl(int(nextprogram2)).setWidth(nextprogram2_width)

                                                             if nextprogram2_width == 276:
                                                                 self.getControl(int(nextprogram3)).setPosition(1007, int(pos_Y))

                                                                 if nextprogram3_width == 59:
                                                                     self.getControl(int(nextprogram4)).setPosition(1073, int(pos_Y))


                                                         elif nextprogram2_width == 342:
                                                             self.getControl(int(nextprogram3)).setPosition(1073, int(pos_Y))



                                                         elif nextprogram2_width == 396:
                                                             self.getControl(int(nextprogram3)).setPosition(1126, int(pos_Y))

                                                             if nextprogram3_width == 117:
                                                                 self.getControl(int(nextprogram4)).setPosition(1251, int(pos_Y))



                                                 elif nextprogram1_stop_time > epg_time_2 and nextprogram1_stop_time < epg_time_3:
                                                     print "bbc one program_finished"
                                                     print program_finished

                                                     if program_finished == '10':
                                                         if nextprogram1_width >= 342:
                                                             nextprogram1_width = 456
                                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                             if nextprogram1_width == 456:
                                                                 self.getControl(int(nextprogram2)).setPosition(837, int(pos_Y))


                                                     elif program_finished == '15':
                                                         if nextprogram1_width >= 342:
                                                             self.getControl(int(nextprogram2)).setPosition(897, int(pos_Y))



                                                     elif program_finished == '40':
                                                         if nextprogram1_width >= 342:
                                                             nextprogram1_width = 456
                                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                             if nextprogram1_width == 456:
                                                                 self.getControl(int(nextprogram2)).setPosition(837, int(pos_Y))


                                                             elif nextprogram1_width == 515:
                                                                 self.getControl(int(nextprogram2)).setPosition(897, int(pos_Y))



                                             elif nextprogram1_width >= 692:
                                                 print "692 you are here 2"
                                                 self.nextprogram_id = list()
                                                 self.nextprogram_id.append(nextprogram1)
                                                 self.select_db_flag = True
                                                 self.select_db()
                                                 nextprogram1_clock = ''.join(str(x) for x in self.nextprogram_clock)
                                                 nextprogram1_clock = str(nextprogram1_clock)
                                                 nextprogram1_stop_clock = ''.join(str(x) for x in self.nextprogram_stop_clock)
                                                 nextprogram1_stop_clock = str(nextprogram1_stop_clock)
                                                 nextprogram1_stop_time = time.strptime(nextprogram1_clock, '%d/%m/%Y %I:%M%p')
                                                 program_finished = nextprogram1_stop_clock.split(':')[1].replace('PM', '').replace('AM', '')
                                                 print "nextprogram1_stop_time"
                                                 print nextprogram1_stop_time


                                                 if nextprogram1_stop_time == epg_time_2:
                                                     print "passed 2b"
                                                     nextprogram1_width = 342
                                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                     if nextprogram1_width == 342:
                                                         self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))



                                                 elif nextprogram1_stop_time == epg_time_3:
                                                     nextprogram1_width = 691
                                                     self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                     if nextprogram1_width == 691:
                                                         self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))



                                                 elif nextprogram1_stop_time > epg_time_2 and nextprogram1_stop_time < epg_time_3:
                                                     if program_finished == '10':
                                                         nextprogram1_width = 456
                                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                         if nextprogram1_width == 456:
                                                             self.getControl(int(nextprogram2)).setPosition(837, int(pos_Y))


                                                     elif program_finished == '35':
                                                         nextprogram1_width = 408
                                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                         if nextprogram1_width == 408:
                                                             self.getControl(int(nextprogram2)).setPosition(790, int(pos_Y))



                                                 elif nextprogram1_stop_time > epg_time_1 and nextprogram1_stop_time < epg_time_2:
                                                     if program_finished == '35':
                                                         print "35 here now work on it"
                                                         nextprogram1_width = 59
                                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                         if nextprogram1_width == 59:
                                                             self.getControl(int(nextprogram2)).setPosition(441, int(pos_Y))

                                                             if nextprogram2_width == 286:
                                                                 nextprogram2_width = 277
                                                                 self.getControl(int(nextprogram2)).setWidth(nextprogram2_width)

                                                                 if nextprogram2_width == 277:
                                                                     self.getControl(int(nextprogram3)).setPosition(724, int(pos_Y))



                                         elif nextprogram_stop_time > epg_time_1 and nextprogram_stop_time < epg_time_2:
                                             print "fix here chris 1"
                                             self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))

                                             if nextprogram_finished == '05':
                                                 if nextprogram_width >= 59:
                                                     nextprogram_width = 59
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 59:
                                                         self.getControl(int(nextprogram1)).setPosition(441, int(pos_Y))

                                                         if nextprogram1_width == 342:
                                                             self.getControl(int(nextprogram2)).setPosition(790, int(pos_Y))

                                                             if nextprogram2_width == 342:
                                                                 self.getControl(int(nextprogram3)).setPosition(1134, int(pos_Y))
                                                                 #ass2a


                                                         elif nextprogram1_width == 456:
                                                             self.getControl(int(nextprogram2)).setPosition(897, int(pos_Y))


                                                         elif nextprogram1_width == 516:
                                                             nextprogram1_width = 512
                                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                             if nextprogram1_width == 512:
                                                                 self.getControl(int(nextprogram2)).setPosition(958, int(pos_Y))


                                                         elif nextprogram1_width == 567:
                                                             nextprogram1_width = 558
                                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                             if nextprogram1_width == 558:
                                                                 self.getControl(int(nextprogram2)).setPosition(1007, int(pos_Y))

                                                                 if nextprogram2_width == 59:
                                                                     self.getControl(int(nextprogram3)).setPosition(1073, int(pos_Y))


                                                         elif nextprogram1_width == 626:
                                                             nextprogram1_width = 624
                                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                             if nextprogram1_width == 624:
                                                                 self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))



                                             elif nextprogram_finished == '10':
                                                 if nextprogram_width >= 342:
                                                     nextprogram_width = 114
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 114:
                                                         self.getControl(int(nextprogram1)).setPosition(495, int(pos_Y))

                                                         if nextprogram1_width == 342:
                                                             self.getControl(int(nextprogram2)).setPosition(844, int(pos_Y))

                                                             if nextprogram2_width == 342:
                                                                 self.getControl(int(nextprogram3)).setPosition(1193, int(pos_Y))


                                                         elif nextprogram1_width == 692:
                                                             nextprogram1_width = 691
                                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                             if nextprogram1_width == 691:
                                                                 self.getControl(int(nextprogram2)).setPosition(1192, int(pos_Y))



                                             elif nextprogram_finished >= '13' and nextprogram_finished <= '17':
                                                 if nextprogram_width >= 148:
                                                     nextprogram_width = 167
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 167:
                                                         self.getControl(int(nextprogram1)).setPosition(549, int(pos_Y))

                                                         if nextprogram1_width == 79:
                                                             nextprogram1_width = 59
                                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                             if nextprogram1_width == 59:
                                                                 self.getControl(int(nextprogram2)).setPosition(614, int(pos_Y))



                                                         elif nextprogram1_width == 227:
                                                             self.getControl(int(nextprogram1)).setPosition(780, int(pos_Y))
                                                             #ass3a


                                                         elif nextprogram1_width == 515:
                                                             nextprogram1_width = 517
                                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                             if nextprogram1_width == 517:
                                                                 self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))



                                                 elif nextprogram_width == 342:
                                                     if nextprogram1X != 724:
                                                         self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))

                                                         if nextprogram1_width == 515:
                                                             self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                             elif nextprogram_finished == '20':
                                                 if nextprogram_width >= 342:
                                                     nextprogram_width = 228
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 228:
                                                         self.getControl(int(nextprogram1)).setPosition(609, int(pos_Y))

                                                         if nextprogram1_width == 515:
                                                             self.getControl(int(nextprogram2)).setPosition(1126, int(pos_Y))


                                                         elif nextprogram1_width == 626:
                                                             self.getControl(int(nextprogram2)).setPosition(1241, int(pos_Y))



                                             elif nextprogram_finished == '25':
                                                 nextprogram_width = 277
                                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                 if nextprogram_width == 277:
                                                     self.getControl(int(nextprogram1)).setPosition(659, int(pos_Y))

                                                     if nextprogram1_width == 59:
                                                         self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))

                                                         if nextprogram2_width == 342:
                                                             self.getControl(int(nextprogram3)).setPosition(1073, int(pos_Y))


                                                     elif nextprogram1_width == 117:
                                                         nextprogram1_width = 112
                                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                         if nextprogram1_width == 112:
                                                             self.getControl(int(nextprogram2)).setPosition(778, int(pos_Y))



                                                     elif nextprogram1_width == 227:
                                                         nextprogram1_width = 230
                                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                         if nextprogram1_width == 230:
                                                             self.getControl(int(nextprogram2)).setPosition(897, int(pos_Y))



                                             elif nextprogram_finished == '30':
                                                 print "passed 3"



                                             elif nextprogram_finished == '35':
                                                 nextprogram_width = 59
                                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                 if nextprogram_width == 59:
                                                     self.getControl(int(nextprogram1)).setPosition(441, int(pos_Y))

                                                     if nextprogram1_width == 342:
                                                         self.getControl(int(nextprogram2)).setPosition(790, int(pos_Y))



                                             elif nextprogram_finished == '40':
                                                 nextprogram_width = 114
                                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)
                                                 print "sky living code here"

                                                 if nextprogram_width == 114:
                                                     self.getControl(int(nextprogram1)).setPosition(495, int(pos_Y))

                                                     if nextprogram1_width == 227:
                                                         nextprogram1_width = 222
                                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                         if nextprogram1_width == 222:
                                                             self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))


                                                     elif nextprogram1_width == 515:
                                                         self.getControl(int(nextprogram2)).setPosition(1014, int(pos_Y))
                                                         #ass1a


                                                     elif nextprogram1_width == 567:
                                                         self.getControl(int(nextprogram2)).setPosition(1069, int(pos_Y))


                                                     elif nextprogram1_width == 692:
                                                         nextprogram1_width = 691
                                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                         if nextprogram1_width == 691:
                                                             self.getControl(int(nextprogram2)).setPosition(1193, int(pos_Y))




                                             elif nextprogram_finished == '45':
                                                 if nextprogram_width == 167:
                                                     self.getControl(int(nextprogram1)).setPosition(549, int(pos_Y))

                                                     if nextprogram1_width == 167:
                                                         nextprogram1_width = 169
                                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                         if nextprogram1_width == 169:
                                                             self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))

                                                             if nextprogram2_width == 342:
                                                                 self.getControl(int(nextprogram3)).setPosition(1073, int(pos_Y))


                                                     elif nextprogram1_width == 342:
                                                         self.getControl(int(nextprogram2)).setPosition(897, int(pos_Y))

                                                         if nextprogram2_width == 342:
                                                             self.getControl(int(nextprogram3)).setPosition(1248, int(pos_Y))


                                                     elif nextprogram1_width == 515:
                                                         nextprogram1_width = 516
                                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                         if nextprogram1_width == 516:
                                                             self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))



                                                     elif nextprogram1_width == 692:
                                                         nextprogram1_width = 691
                                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                         if nextprogram1_width == 691:
                                                             self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                                 elif nextprogram_width >= 286:
                                                     nextprogram_width = 167
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 167:
                                                         self.getControl(int(nextprogram1)).setPosition(549, int(pos_Y))

                                                         if nextprogram1_width == 515:
                                                             nextprogram1_width = 517
                                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                             if nextprogram1_width == 517:
                                                                 self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))



                                                         elif nextprogram1_width == 567:
                                                             self.getControl(int(nextprogram2)).setPosition(1123, int(pos_Y))



                                             elif nextprogram_finished == '50':
                                                 if nextprogram_width >= 227:
                                                     nextprogram_width = 228
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 228:
                                                         self.getControl(int(nextprogram1)).setPosition(609, int(pos_Y))

                                                         if nextprogram1_width == 117:
                                                             nextprogram1_width = 108
                                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                             if nextprogram1_width == 108:
                                                                 self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))

                                                                 if nextprogram2_width == 342:
                                                                     self.getControl(int(nextprogram3)).setPosition(1073, int(pos_Y))



                                                         elif nextprogram1_width == 342:
                                                             self.getControl(int(nextprogram2)).setPosition(957, int(pos_Y))


                                                         elif nextprogram1_width == 515:
                                                             self.getControl(int(nextprogram2)).setPosition(1130, int(pos_Y))



                                             elif nextprogram_finished == '55':
                                                 if nextprogram_width >= 286:
                                                     nextprogram_width = 277
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 277:
                                                         self.getControl(int(nextprogram1)).setPosition(659, int(pos_Y))
                                                         print "channel 4 code here"

                                                         if nextprogram1_width == 59:
                                                             self.getControl(int(nextprogram2)).setPosition(724, int(pos_Y))

                                                             if nextprogram2_width == 117:
                                                                 self.getControl(int(nextprogram3)).setPosition(847, int(pos_Y))


                                                             elif nextprogram2_width == 167:
                                                                 self.getControl(int(nextprogram3)).setPosition(897, int(pos_Y))


                                                             elif nextprogram2_width == 227:
                                                                 self.getControl(int(nextprogram3)).setPosition(955, int(pos_Y))


                                                             elif nextprogram2_width == 286:
                                                                 self.getControl(int(nextprogram3)).setPosition(960, int(pos_Y))


                                                             elif nextprogram2_width == 342:
                                                                 self.getControl(int(nextprogram3)).setPosition(1073, int(pos_Y))


                                                             elif nextprogram2_width == 399:
                                                                 self.getControl(int(nextprogram3)).setPosition(1127, int(pos_Y))



                                                         elif nextprogram1_width == 117:
                                                             self.getControl(int(nextprogram2)).setPosition(847, int(pos_Y))


                                                         elif nextprogram1_width == 167:
                                                             self.getControl(int(nextprogram2)).setPosition(897, int(pos_Y))


                                                         elif nextprogram1_width == 227:
                                                             self.getControl(int(nextprogram2)).setPosition(955, int(pos_Y))


                                                         elif nextprogram1_width == 286:
                                                             self.getControl(int(nextprogram2)).setPosition(960, int(pos_Y))


                                                         elif nextprogram1_width == 342:
                                                             self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))


                                                         elif nextprogram1_width == 399:
                                                             self.getControl(int(nextprogram2)).setPosition(1127, int(pos_Y))



                                         elif nextprogram_stop_time > epg_time_2 and nextprogram_stop_time < epg_time_3:
                                             print "fix here chris 2"
                                             self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))

                                             if nextprogram_finished == '05':
                                                 if nextprogram_width >= 567:
                                                     print "bbc two code here"
                                                     nextprogram_width = 408
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 408:
                                                         self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))

                                                         if nextprogram1_width == 342:
                                                             self.getControl(int(nextprogram2)).setPosition(1136, int(pos_Y))



                                             elif nextprogram_finished == '10':
                                                 if nextprogram_width >= 456:
                                                     print "channel 5 code here"
                                                     nextprogram_width = 456
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 456:
                                                         self.getControl(int(nextprogram1)).setPosition(837, int(pos_Y))



                                             elif nextprogram_finished == '15':
                                                 if nextprogram_width >= 515:
                                                     nextprogram_width = 516
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 516:
                                                         self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))

                                                         if nextprogram1_width == 59:
                                                             self.getControl(int(nextprogram2)).setPosition(963, int(pos_Y))


                                                         elif nextprogram1_width == 227:
                                                             self.getControl(int(nextprogram2)).setPosition(1130, int(pos_Y))

                                                 #self.getControl(int(nextprogram1)).setPosition(948, int(pos_Y))



                                             elif nextprogram_finished == '20':
                                                 if nextprogram_stop_time > epg_time_2 and nextprogram_stop_time < epg_time_3:
                                                     if nextprogram_width >= 228:
                                                         nextprogram_width = 577
                                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                         if nextprogram_width == 577:
                                                             self.getControl(int(nextprogram1)).setPosition(959, int(pos_Y))

                                                             if nextprogram1_width == 59:
                                                                 self.getControl(int(nextprogram2)).setPosition(1022, int(pos_Y))


                                                             elif nextprogram1_width == 286:
                                                                 nextprogram1_width = 283
                                                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                                 if nextprogram1_width == 283:
                                                                     self.getControl(int(nextprogram2)).setPosition(1248, int(pos_Y))



                                                             elif nextprogram1_width >= 399:
                                                                 self.getControl(int(nextprogram2)).setPosition(1550, int(pos_Y))



                                                 elif nextprogram_stop_time > epg_time_1 and nextprogram_stop_time < epg_time_2:
                                                     if nextprogram_width >= 515:
                                                         nextprogram_width = 228
                                                         self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                         if nextprogram_width == 228:
                                                             self.getControl(int(nextprogram1)).setPosition(609, int(pos_Y))

                                                             if nextprogram1_width == 286:
                                                                 nextprogram1_width = 282
                                                                 self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                                 if nextprogram1_width == 282:
                                                                     self.getControl(int(nextprogram2)).setPosition(897, int(pos_Y))



                                                             elif nextprogram1_width == 626:
                                                                 self.getControl(int(nextprogram2)).setPosition(1241, int(pos_Y))



                                             elif nextprogram_finished == '25':
                                                 if nextprogram_width >= 515:
                                                     nextprogram_width = 285
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 285:
                                                         self.getControl(int(nextprogram1)).setPosition(667, int(pos_Y))




                                             elif nextprogram_finished == '35':
                                                 if nextprogram_width >= 396:
                                                     nextprogram_width = 408
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 408:
                                                         self.getControl(int(nextprogram1)).setPosition(790, int(pos_Y))

                                                         if nextprogram1_width == 59:
                                                             self.getControl(int(nextprogram2)).setPosition(849, int(pos_Y))


                                                         elif nextprogram1_width == 117:
                                                             self.getControl(int(nextprogram2)).setPosition(897, int(pos_Y))


                                                         elif nextprogram1_width == 167:
                                                             self.getControl(int(nextprogram2)).setPosition(955, int(pos_Y))



                                             elif nextprogram_finished == '40':
                                                 if nextprogram_width >= 515:
                                                     nextprogram_width = 456
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 456:
                                                         self.getControl(int(nextprogram1)).setPosition(838, int(pos_Y))

                                                         if nextprogram1_width == 167:
                                                             self.getControl(int(nextprogram2)).setPosition(1012, int(pos_Y))



                                             elif nextprogram_finished == '45':
                                                 print "you are here now chris"
                                                 if programs_width == 117 and nextprogram_width == 626:
                                                     nextprogram_width = 625
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)
                                                     print "you are here now chris 1"

                                                     if nextprogram_width == 625:
                                                         self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))
                                                         print "you are here now chris 2"


                                                 elif nextprogram_width >= 515:
                                                     nextprogram_width = 516
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 516:
                                                         self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))

                                                     #self.getControl(int(nextprogram1)).setPosition(948, int(pos_Y))



                                             elif nextprogram_finished == '50':
                                                 print "passed 1b"
                                                 if nextprogram_width >= 516:
                                                     nextprogram_width = 567
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 567:
                                                         self.getControl(int(nextprogram1)).setPosition(949, int(pos_Y))
                                                         print "passed 2c"


                                                         if nextprogram1_width == 117:
                                                             self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))

                                                             if nextprogram2_width == 117:
                                                                 self.getControl(int(nextprogram3)).setPosition(1196, int(pos_Y))



                                                         elif nextprogram1_width == 167:
                                                             self.getControl(int(nextprogram2)).setPosition(1123, int(pos_Y))



                                                         elif nextprogram1_width == 286:
                                                             nextprogram1_width = 290
                                                             self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                             if nextprogram1_width == 290:
                                                                 self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))




                                             elif nextprogram_finished == '55':
                                                 self.getControl(int(nextprogram1)).setPosition(1007, int(pos_Y))

                                                 if nextprogram1_width == 59:
                                                     self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))



                                         elif nextprogram_stop_time == epg_time_2:
                                             print "the code is for sky one and sky living"
                                             self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))


                                             if nextprogram_finished == '00':
                                                 print "you are working on this now"
                                                 nextprogram_width = 342
                                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                 if nextprogram_width == 342:
                                                     self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))

                                                     if nextprogram1_width == 59:
                                                         self.getControl(int(nextprogram2)).setPosition(790, int(pos_Y))



                                                     elif nextprogram1_width == 117:
                                                         nextprogram1_width = 113
                                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                         if nextprogram1_width == 113:
                                                             self.getControl(int(nextprogram2)).setPosition(844, int(pos_Y))



                                                     elif nextprogram1_width == 167:
                                                         self.getControl(int(nextprogram2)).setPosition(897, int(pos_Y))


                                                     elif nextprogram1_width == 227:
                                                         self.getControl(int(nextprogram2)).setPosition(958, int(pos_Y))


                                                     elif nextprogram1_width == 342:
                                                         self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))

                                                         if nextprogram2_width == 117:
                                                             self.getControl(int(nextprogram3)).setPosition(1197, int(pos_Y))



                                                     elif nextprogram1_width == 396:
                                                         self.getControl(int(nextprogram2)).setPosition(1127, int(pos_Y))


                                                     elif nextprogram1_width == 456:
                                                         self.getControl(int(nextprogram2)).setPosition(1184, int(pos_Y))


                                                     elif nextprogram1_width == 515:
                                                         self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))




                                             elif nextprogram_finished == '30':
                                                 nextprogram_width = 342
                                                 self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                 if nextprogram_width == 342:
                                                     self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))
                                                     print "you are here now chris"

                                                     if nextprogram1_width == 117:
                                                         nextprogram1_width = 113
                                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                         if nextprogram1_width == 113:
                                                             self.getControl(int(nextprogram2)).setPosition(844, int(pos_Y))



                                                     elif nextprogram1_width == 167:
                                                         self.getControl(int(nextprogram2)).setPosition(897, int(pos_Y))


                                                     elif nextprogram1_width == 286:
                                                         nextprogram1_width = 277
                                                         self.getControl(int(nextprogram1)).setWidth(nextprogram1_width)

                                                         if nextprogram1_width == 277:
                                                             self.getControl(int(nextprogram2)).setPosition(1007, int(pos_Y))

                                                         if nextprogram2_width == 59:
                                                             self.getControl(int(nextprogram3)).setPosition(1073, int(pos_Y))



                                                     elif nextprogram1_width == 342:
                                                         self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))


                                                     elif nextprogram1_width == 396:
                                                         self.getControl(int(nextprogram2)).setPosition(1126, int(pos_Y))


                                                     elif nextprogram1_width == 515:
                                                         self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))




                                         elif nextprogram_stop_time == epg_time_3:
                                             print "the code is jumping on here"
                                             self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))

                                             if nextprogram_finished == '00':
                                                 if nextprogram_width > 691:
                                                     nextprogram_width = 691
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 691:
                                                         self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))

                                                         if nextprogram1_width == 59:
                                                             self.getControl(int(nextprogram2)).setPosition(1138, int(pos_Y))



                                                         elif nextprogram1_width == 167:
                                                             self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                             elif nextprogram_finished == '30':
                                                 if nextprogram_width > 691:
                                                     nextprogram_width = 691
                                                     self.getControl(int(nextprogram)).setWidth(nextprogram_width)

                                                     if nextprogram_width == 691:
                                                         self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))

                                                         if nextprogram1_width == 167:
                                                             self.getControl(int(nextprogram2)).setPosition(1246, int(pos_Y))



                                         elif nextprogram_stop_time > epg_time_3:
                                             self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))

                                             if nextprogram_width == 741:
                                                 self.getControl(int(nextprogram1)).setPosition(1123, int(pos_Y))



                             #self.program_finished_flag = True
                             except:
                             #elif self.program_finished == False:
                                 pass
                                 #print "let do something"
                             

                             #try:
                                 #program_button = self.getControl(int(program_id))

                                 #if program_button:
                                     #removeButtons = self.getControl(int(program_id))
                                     #self.remove_controls.append(removeButtons)
                                     #self.Remove_Buttons()
                                     #

                                     #self.nextprogram_id = list()
                                     #self.nextprogram_id.append(nextprogram)
                                     #self.select_db_flag = True
                                     #self.select_db()
                                     #nextprogram_clock = ''.join(str(x) for x in self.nextprogram_clock)
                                     #nextprogram_clock = str(nextprogram_clock)
                                     #nextprogram_stop_clock = ''.join(str(x) for x in self.nextprogram_stop_clock)
                                     #nextprogram_stop_clock = str(nextprogram_stop_clock)
                                     #program_stop_time = time.strptime(nextprogram_clock, '%d/%m/%Y %I:%M%p')
                                     #print "nextprogram_stop_time"
                                     #print program_stop_time
                                     #nextprogram_button = self.getControl(int(nextprogram))
                                     #ass1a


                                     #print "you are here now chris let move programs to 375"


                             #except Exception:
                                 #pass



                         elif program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                             print "program finished here 1"

                             #if program_finished == '20':
                                 #if program_width == 227 and nextprogram_width == 117:
                                     #print "you are here 2c"

                                     #if program_stop_time <= epg_time_1:
                                         #self.remove_controls = list()
                                         #removeButtons = self.getControl(int(program_id))
                                         #self.remove_controls.append(removeButtons)
                                         #self.Remove_Buttons()
                                     #else:
                                         #self.getControl(int(program_id)).setVisible(False)
                                         #self.getControl(int(program_id)).setPosition(int(pos_X) - 700, int(pos_Y))
                                     #self.getControl(int(nextprogram)).setVisible(False)
                                     #self.getControl(int(nextprogram)).setPosition(int(pos_X) - 350, int(pos_Y))
                                     #self.getControl(int(nextprogram1)).setPosition(375, int(pos_Y))

                                     #if nextprogram1_width == 692:
                                         #self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))
                                         #self.getControl(int(nextprogram2)).setVisible(True)


                                     #elif nextprogram1_width == 741:
                                         #self.getControl(int(nextprogram2)).setPosition(1124, int(pos_Y))
                                         #self.getControl(int(nextprogram2)).setVisible(True)



                             if program_finished == '40':
                                 if nextprogram_width >= 456:
                                     programs_width = 117
                                     self.getControl(int(nextprogram)).setWidth(programs_width)

                                     if nextprogram1_X > 499:
                                         self.getControl(int(nextprogram1)).setPosition(499, int(pos_Y))

                                         if nextprogram1_width == 692:
                                             self.getControl(int(nextprogram2)).setPosition(1197, int(pos_Y))



                             elif program_finished == '55':
                                 if program_width == 626:
                                     print "you are here 3"
                                     program_width = 284
                                     self.getControl(int(program_id)).setWidth(program_width)


                                     #if nextprogram_width == 59:
                                         #self.getControl(int(program_id)).setPosition(int(pos_X) - 700, int(pos_Y))
                                     #else:
                                         #self.getControl(int(program_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                                     #self.getControl(int(program_id)).setWidth(program_width)
                                     #self.getControl(int(program_id)).setVisible(False)

                                     #if nextprogram_width == 59:
                                         #self.getControl(int(program_id)).setPosition(int(pos_X) - 700, int(pos_Y))
                                         #self.getControl(int(nextprogram)).setVisible(False)
                                         #self.getControl(int(nextprogram)).setPosition(int(pos_X) - 350, int(pos_Y))
                                         #self.getControl(int(nextprogram1)).setPosition(375, int(pos_Y))

                                         #if nextprogram1_width == 692:
                                             #program_width = 691
                                             #self.getControl(int(nextprogram1)).setWidth(program_width)
                                             #self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))


                                     #else:
                                         #print "you are here 4"
                                         #self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))

                                         #if nextprogram_width == 567:
                                             #self.getControl(int(nextprogram1)).setPosition(948, int(pos_Y))



                         elif program_stop_time > epg_time_2 and program_stop_time < epg_time_3:
                             print "program finished here 2"

                             if program_finished == '15':
                                 if nextprogram_width >= 567:
                                     programs_width = 516
                                     self.getControl(int(nextprogram)).setWidth(programs_width)

                                     if nextprogram1_X > 897:
                                         self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))



                             elif program_finished == '40':

                                 if nextprogram_width == 456 and nextprogram1_X > 837:
                                     self.getControl(int(nextprogram1)).setPosition(837, int(pos_Y))


                                 elif nextprogram_width >= 691:
                                     programs_width = 456
                                     self.getControl(int(nextprogram)).setWidth(programs_width)


                                     if nextprogram1_X > 837:
                                         self.getControl(int(nextprogram1)).setPosition(837, int(pos_Y))



                                 #if nextprogram_width == 692:
                                     #if nextprogram1_X > 1073:
                                         #program_width = 691
                                         #self.getControl(int(nextprogram)).setWidth(program_width)
                                         #self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))



                         elif program_stop_time == epg_time_2:
                             print "program finished here 3"

                             if program_finished == '00':
                                 if nextprogram_width >= 691:
                                     programs_width = 342
                                     self.getControl(int(nextprogram)).setWidth(programs_width)

                                     if nextprogram1_X > 724:
                                         self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))



                         elif program_stop_time == epg_time_3:
                             print "program finished here 4"

                             if program_finished == '00':
                                 if nextprogram_width >= 691:
                                     programs_width = 691
                                     self.getControl(int(nextprogram)).setWidth(programs_width)

                                     if nextprogram1_X > 1073:
                                         self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))




                         #elif program_width >= 691:
                             #print "you are here 5"
                             #self.nextprogram_id = list()
                             #self.nextprogram_id.append(program_id)
                             #self.select_db_flag = True
                             #self.select_db()
                             #nextprogram_clock = ''.join(str(x) for x in self.nextprogram_clock)
                             #nextprogram_clock = str(nextprogram_clock)
                             #nextprogram_stop_clock = ''.join(str(x) for x in self.nextprogram_stop_clock)
                             #nextprogram_stop_clock = str(nextprogram_stop_clock)
                             #program_stop_time = time.strptime(nextprogram_clock, '%d/%m/%Y %I:%M%p')
                             #program_finished = nextprogram_stop_clock.split(':')[1].replace('PM', '').replace('AM', '')
                             #print program_finished


                             #if program_stop_time <= epg_time_1:
                                 #print "now you are in the epg_time1 chris "
                                 #self.getControl(int(program_id)).setPosition(375, 15)
                                 #self.remove_controls = list()
                                 #removeButtons = self.getControl(int(program_id))
                                 #self.remove_controls.append(removeButtons)
                                 #self.Remove_Buttons()
                                 #self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))

                                 #if nextprogram_width == 692:
                                     #self.nextprogram_id = list()
                                     #self.nextprogram_id.append(nextprogram)
                                     #self.select_db_flag = True
                                     #self.select_db()
                                     #nextprogram_clock = ''.join(str(x) for x in self.nextprogram_clock)
                                     #nextprogram_clock = str(nextprogram_clock)
                                     #nextprogram_stop_clock = ''.join(str(x) for x in self.nextprogram_stop_clock)
                                     #nextprogram_stop_clock = str(nextprogram_stop_clock)
                                     #program_stop_time = time.strptime(nextprogram_clock, '%d/%m/%Y %I:%M%p')
                                     #program_finished = nextprogram_stop_clock.split(':')[1].replace('PM', '').replace('AM', '')

                                     #if program_stop_time == epg_time_2:
                                         #program_width = 342
                                         #self.getControl(int(nextprogram)).setWidth(program_width)
                                         #self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))

                                     #else:
                                         #program_width = 691
                                         #self.getControl(int(nextprogram)).setWidth(program_width)
                                         #self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))



                             #if program_stop_time == epg_time_2:
                                 #self.getControl(int(program_id)).setVisible(False)
                                 #program_width = 342
                                 #self.getControl(int(program_id)).setWidth(program_width)
                                 #self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))



                             #elif program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                                 #print "you are here now chris 1"

                                 #if program_finished == '00':
                                     #self.remove_controls = list()
                                     #removeButtons = self.getControl(int(program_id))
                                     #self.remove_controls.append(removeButtons)
                                     #self.Remove_Buttons()
                                     #self.getControl(int(nextprogram)).setPosition(375, int(pos_Y))

                                     #if nextprogram_width == 692:
                                         #program_width = 691
                                         #self.getControl(int(nextprogram)).setWidth(program_width)

                                         #if nextprogram1_X != 1073:
                                             #self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))

                                             #self.nextprogram_id = list()
                                             #self.nextprogram_id.append(nextprogram)
                                             #self.select_db_flag = True
                                             #self.select_db()
                                             #nextprogram_clock = ''.join(str(x) for x in self.nextprogram_clock)
                                             #nextprogram_clock = str(nextprogram_clock)
                                             #nextprogram_stop_clock = ''.join(str(x) for x in self.nextprogram_stop_clock)
                                             #nextprogram_stop_clock = str(nextprogram_stop_clock)
                                             #program_stop_time = time.strptime(nextprogram_clock, '%d/%m/%Y %I:%M%p')
                                             #program_stop_time = time.strptime(program_stop_clock, '%I:%M%p')
                                             #program_finished = nextprogram_stop_clock.split(':')[1].replace('PM', '').replace('AM', '')
                                             #print program_finished



                                         #if program_stop_time == epg_time_2:
                                             #programs_width = 342
                                             #self.getControl(int(nextprogram)).setWidth(programs_width)
                                             #self.getControl(int(nextprogram1)).setPosition(724, int(pos_Y))



                                 #if program_finished == '45':
                                     #programs_width = 171
                                     #self.getControl(int(program_id)).setWidth(programs_width)
                                     #self.getControl(int(nextprogram)).setPosition(549, int(pos_Y))


                             #else:
                                 #print "you are here now chris 2"
                                 #self.nextprogram_id = list()
                                 #self.nextprogram_id.append(nextprogram)
                                 #self.select_db_flag = True
                                 #self.select_db()
                                 #nextprogram_clock = ''.join(str(x) for x in self.nextprogram_clock)
                                 #nextprogram_clock = str(nextprogram_clock)
                                 #nextprogram_stop_clock = ''.join(str(x) for x in self.nextprogram_stop_clock)
                                 #nextprogram_stop_clock = str(nextprogram_stop_clock)
                                 #program_stop_time = time.strptime(nextprogram_clock, '%d/%m/%Y %I:%M%p')
                                 #program_stop_time = time.strptime(program_stop_clock, '%I:%M%p')
                                 #program_finished = nextprogram_stop_clock.split(':')[1].replace('PM', '').replace('AM', '')
                                 #print program_finished


                                 #if program_stop_time == epg_time_2:
                                     #programs_width = 342
                                     #self.getControl(int(nextprogram)).setWidth(programs_width)


                                 #if nextprogram_width == 167:
                                     #self.getControl(int(nextprogram1)).setPosition(549, int(pos_Y))


                                 #elif nextprogram_width == 567:
                                     #self.getControl(int(nextprogram1)).setPosition(949, int(pos_Y))

                                     #if nextprogram1_width == 117:
                                         #self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))


                                 #elif nextprogram_width == 626:
                                     #self.getControl(int(nextprogram1)).setPosition(1007, int(pos_Y))

                                     #if nextprogram1_width == 59:
                                         #self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))
                                         #self.getControl(int(nextprogram2)).setVisible(True)


                                 #elif nextprogram_width == 692:
                                     #program_width = 691
                                     #self.getControl(int(nextprogram)).setWidth(program_width)
                                     #self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))




                     program_stop_clock_list = list()
                     half_hour_date_list = list()
                     one_hour_date_list = list()
                     one_hour_half_date_list = list()
                 self.program_finished_flag = False
             #for ids, width in zip(programs_id, program_width):
                 #cur.execute("INSERT INTO buttons(button_ids, button_width)" + " VALUES(?, ?)", [ids, width])
             #con.commit()
             #cur.close()