for program_stop_clock, program_width, program_id in izip_longest(self.program_finished_clock, self.program_width, self.program_id, fillvalue=''):
                         print "program_stop_clock"
                         print program_stop_clock

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




                         elif program_stop_time > epg_time_1 and program_stop_time < epg_time_2 or program_stop_time > epg_time_2:
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
                                     if programX == 375 and program_width >= 342:
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




                         elif program_stop_time > epg_time_2 and program_stop_time < epg_time_3 or program_stop_time > epg_time_2 and program_stop_time > epg_time_3:
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
                                         #self.getControl(int(nextprogram1)).setVisible(True)



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




                         elif program_stop_time == epg_time_3 or program_stop_time > epg_time_3:
                             print "here 5"

                             if program_finished == '00':
                                 if programX == 375 and program_width > 1038:
                                     programs_width = 691
                                     self.getControl(int(program_id)).setWidth(programs_width)
                                     self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))




                         elif program_stop_time > epg_time_3:
                             print "here 6"

                             if program_finished == '05':
                                 if programX == 375 and program_width > 692:
                                     programs_width = 751
                                     self.getControl(int(program_id)).setWidth(programs_width)



                             elif program_finished == '10':
                                 if programX == 375 and program_width >= 1037:
                                     programs_width = 798
                                     self.getControl(int(program_id)).setWidth(programs_width)
                                     self.getControl(int(nextprogram)).setPosition(1180, int(pos_Y))



                             elif program_finished == '25':
                                 if programX == 375 and program_width == 567:
                                     programs_width = 278
                                     self.getControl(int(program_id)).setWidth(programs_width)
                                     self.getControl(int(nextprogram)).setPosition(660, int(pos_Y))

                                     if nextprogram_width == 456:
                                         self.getControl(int(nextprogram1)).setPosition(1124, int(pos_Y))



                             elif program_finished == '45':
                                 if programX == 375 and program_width == 741:
                                     programs_width = 167
                                     self.getControl(int(program_id)).setWidth(programs_width)
                                     self.getControl(int(nextprogram)).setPosition(549, int(pos_Y))



                             elif program_finished == '55':
                                 if programX == 375 and program_width == 1311:
                                     programs_width = 976
                                     self.getControl(int(program_id)).setWidth(programs_width)



                         elif program_stop_time == epg_time_3: 
                             print "here 7"

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