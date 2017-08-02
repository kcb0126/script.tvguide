
                         for pos_X, pos_Y, prog_id, prog_width in zip(positions_X, positions_Y, programs_id, program_width):





                         if CurrentRow == 375 and CurrentWidth == 692:
                             nextprogram = int(CurrentId) + 1
                             nextprogramX = self.getControl(int(nextprogram)).getX()
                             nextprogramY = self.getControl(int(nextprogram)).getY()

                             if nextprogramX == 375:
                                 self.getControl(int(nextprogram)).setPosition(1073, int(nextprogramY))
                                 nextprograms = int(nextprogram) + 1
                                 nextprogramsX = self.getControl(int(nextprograms)).getX()

                                 if nextprogramsX == 1073:
                                     self.getControl(int(nextprograms)).setVisible(True)

                                     
                         if CurrentRow == 375 and CurrentWidth == 879:
                             programs_width = 515
                             self.getControl(int(CurrentId)).setWidth(int(programs_width))
                             nextprogram = int(CurrentId) + 1
                             nextprogramX = self.getControl(int(nextprogram)).getX()

                             if nextprogramX != 897:
                                 self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))
                                 self.getControl(int(nextprogram)).setVisible(True)
                                 nextprograms = int(nextprogram) + 1
                                 nextprogramsX = self.getControl(int(nextprograms)).getX()
                                 nextprogramsWidth = self.getControl(int(nextprograms)).getWidth()

                                 if nextprogramsWidth <= 167:
                                     self.getControl(int(nextprograms)).setPosition(1073, int(pos_Y))
                                     self.getControl(int(nextprograms)).setVisible(True)




                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     



                                     






                             
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                             elif int(pos_X) == 724 and int(prog_width) == 692:
                                 self.getControl(int(prog_id)).setPosition(375, int(pos_Y))
                                 nextprogram = int(prog_id) + 1
                                 nextprogramX = self.getControl(int(nextprogram)).getX()

                                 if nextprogramX != 1073:
                                     self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                     self.getControl(int(nextprogram)).setVisible(True)

                                 print "sort this out chrussssssssssssssssss"



                             elif int(pos_X) == 724 and int(prog_width) == 567:
                                 self.getControl(int(prog_id)).setWidth(int(programs_width))
                                 program_width = self.getControl(int(prog_id)).getWidth()
                                 profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
                                 conn1 = database.connect(profilePath)
                                 cur1 = conn1.cursor()
                                 cur1.execute('SELECT stop_date FROM programs where button_id=?', [prog_id])
                                 stop_date = cur1.fetchone()

                                 if stop_date is not None:
                                     stop_date = str(stop_date[0])
                                     stop_time = time.strptime(str(stop_date), '%Y%m%d%H%M%S')
                                     stop_time = datetime.datetime.fromtimestamp(time.mktime(stop_time))
                                     program_stop_hours = stop_time.strftime('%H')
                                     program_stop_minutes = stop_time.strftime('%M')
                                     program_AM_PM = stop_time.strftime('%p')
                                     half_hour = str(self.getControl(344).getLabel())
                                     one_hour = str(self.getControl(345).getLabel())
                                     one_hour_half = str(self.getControl(346).getLabel())
                                     epg_time_1 = time.strptime(half_hour, '%I:%M%p')
                                     epg_time_2 = time.strptime(one_hour, '%I:%M%p')
                                     epg_time_3 = time.strptime(one_hour_half, '%I:%M%p')

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

                                     program_stop_time = program_stop_hours +':' + program_stop_minutes + program_AM_PM
                                     program_stop_time = time.strptime(program_stop_time, '%I:%M%p')


                                     if program_stop_time <= epg_time_3:
                                         if program_stop_minutes == '40':
                                             if program_width == 567:
                                                 program_width = 510
                                                 self.getControl(int(prog_id)).setWidth(int(program_width))















                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 

                                     
                                     








                                 elif int(pos_X) == 723:
                                     if int(prog_width) == 692:
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX != 1073:
                                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(True)



                                 elif int(pos_X) == 724:
                                     print "you are working on here now 2"

                                     if int(prog_width) == 692:
                                         print "you are here"
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX != 1073:
                                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(True)



                                     elif int(prog_width) == 626:
                                         print "you are here 2"
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX > 1073:
                                             self.getControl(int(nextprogram)).setPosition(1008, int(pos_Y))




                                 
                                 elif int(pos_X) == 1073:
                                     #self.getControl(int(prog_id)).setVisible(False)


                                     if int(prog_width) == 167:
                                         print "you are working on here now 3"
                                         currentProgram = int(prog_id)
                                         currentProgramX = self.getControl(int(currentProgram)).getX()

                                         if currentProgramX == 1073:
                                             print "you are working on here now 4"
                                             currentProgram2 = int(prog_id) - 2
                                             currentProgram2X = self.getControl(int(currentProgram2)).getX()
                                             currentProgram2_Width = self.getControl(int(currentProgram2)).getWidth()

                                             if currentProgram2X == 724 and currentProgram2_Width == 167:
                                                 self.getControl(int(currentProgram2)).setPosition(375, int(pos_Y))
                                                 currentProgram1 = int(prog_id) - 1
                                                 currentProgram1X = self.getControl(int(currentProgram1)).getX()
                                                 currentProgram1_Width = self.getControl(int(currentProgram1)).getWidth()

                                                 if currentProgram1X == 897 and currentProgram1_Width == 167:
                                                     self.getControl(int(currentProgram1)).setPosition(549, int(pos_Y))
                                                     currentProgramX = self.getControl(int(currentProgram)).getX()
                                                     currentProgram_Width = self.getControl(int(currentProgram)).getWidth()

                                                     if currentProgramX == 1073 and currentProgram_Width == 167:
                                                         self.getControl(int(currentProgram)).setPosition(724, int(pos_Y))
                                                         nextprogram = int(currentProgram) + 1
                                                         self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))
                                                         self.getControl(int(nextprogram)).setVisible(True)
                                                         nextprogramX = self.getControl(int(nextprogram)).getX()
                                                         nextprogram_Width = self.getControl(int(nextprogram)).getWidth()

                                                         if nextprogram_Width == 167:
                                                             nextprograms = int(nextprogram) + 1
                                                             self.getControl(int(nextprograms)).setPosition(1073, int(pos_Y))
                                                             self.getControl(int(nextprograms)).setVisible(True)


                                             else:
                                                 self.getControl(int(currentProgram)).setPosition(724, int(pos_Y))
                                                 CurrentprogramX = self.getControl(int(currentProgram)).getX()
                                                 nextprogram = int(currentProgram) + 1
                                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                                 nextprogram_Width = self.getControl(int(nextprogram)).getWidth()
                                                 print "CurrentprogramX"
                                                 print CurrentprogramX


                                                 if CurrentprogramX == 1073:
                                                     print "passed"
                                                     self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))
                                                     self.getControl(int(nextprogram)).setVisible(True)


                                                     if int(pos_X) == 375:
                                                         self.getControl(int(prog_id)).setVisbile(False)
                                                         



                                                 if nextprogram_Width == 167:
                                                     if nextprogram_Width != 897:
                                                         self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))
                                                         self.getControl(int(nextprogram)).setVisible(True)
                                                         nextprogram1 = int(nextprogram) + 1
                                                         nextprogram1X = self.getControl(int(nextprogram1)).getX()
                                                         nextprogram1_Width = self.getControl(int(nextprogram1)).getWidth()

                                                         if nextprogram1_Width == 167:
                                                             if nextprogram1X != 1073:
                                                                 self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))
                                                                 self.getControl(int(nextprogram1)).setVisible(True)
                                                                 print "catch this 3"
                                                             else:
                                                                 print "catch this 4"



                                         elif currentProgramX == 724:
                                             print "you are working on here now 5"
                                             currentProgramWidth = self.getControl(int(prog_id)).getWidth()
                                             print currentProgramWidth

                                             if currentProgramWidth == 167:
                                                 nextprogram = int(prog_id) + 1
                                                 nextprogramX = self.getControl(int(nextprogram)).getX()

                                                 if nextprogramX > 1073:
                                                     print "you are working on here now 6"
                                                     self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))
                                                     self.getControl(int(nextprogram)).setVisible(True)



                                     elif int(prog_width) == 342:
                                         self.getControl(int(prog_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                                         CurrentRowX = self.getControl(int(prog_id)).getX()

                                         if CurrentRowX == 723:
                                             self.getControl(int(prog_id)).setPosition(724, int(pos_Y))

                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX != 1073:
                                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(True)


                                     else:
                                         self.getControl(int(prog_id)).setPosition(724, int(pos_Y))



                                         
                                         


                                 

                                 elif int(pos_X) == 724:
                                     if int(prog_width) == 167:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))


                                     elif int(prog_width) == 342:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX != 724:
                                             self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))


                                     elif int(prog_width) == 692:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX != 1073:
                                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(True)



                                     elif int(prog_width) > 692:
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX == 1073:
                                             self.getControl(int(nextprogram)).setPosition(int(pos_X) - 350, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(False)




                                 elif int(pos_X) == 897:
                                     if int(prog_width) == 167:
                                         self.getControl(int(prog_id)).setPosition(549, int(pos_Y))


                                 elif int(pos_X) == 1073:
                                     if int(prog_width) == 167:
                                         self.getControl(int(prog_id)).setPosition(897, int(pos_Y))


                                     elif int(prog_width) == 342:
                                         self.getControl(int(prog_id)).setPosition(724, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX != 1073:
                                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(True)


                                     elif int(prog_width) == 692:
                                         self.getControl(int(prog_id)).setPosition(724, int(pos_Y))


                                     elif int(prog_width) > 692:
                                         self.getControl(int(prog_id)).setPosition(724, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()


                                         if nextprogramX == 1073:
                                             self.getControl(int(nextprogram)).setPosition(int(pos_X) - 350, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(False)




                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             


                                             


                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                



                                 



                                 



                                 



                                 



                                 
                                 
                                 elif int(pos_X) == 549 and int(prog_width) >= 59:
                                     self.getControl(int(prog_id)).setVisible(False)
                                     self.getControl(int(prog_id)).setPosition(int(pos_X) - 350, int(pos_Y))



                                 elif int(pos_X) == 723:
                                     if int(prog_width) == 167:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))


                                     elif int(prog_width) == 342:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogram_Width = self.getControl(int(nextprogram)).getWidth()

                                         if nextprogram_Width == 342:
                                             nextprograms = int(nextprogram) + 1
                                             self.getControl(int(nextprograms)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprograms)).setVisible(True)


                                     elif int(prog_width) == 692:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX != 1073:
                                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(True)


                                     elif int(prog_width) > 692:
                                         nextprogram = int(prog_id) + 1


                                 elif int(pos_X) == 724:
                                     if int(prog_width) == 167:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))


                                     elif int(prog_width) == 342:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogram_Width = self.getControl(int(nextprogram)).getWidth()

                                         if nextprogram_Width == 342:
                                             nextprograms = int(nextprogram) + 1
                                             self.getControl(int(nextprograms)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprograms)).setVisible(True)


                                     elif int(prog_width) == 692:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX != 1073:
                                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(True)


                                     elif int(prog_width) > 692:
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX == 1073:
                                             self.getControl(int(nextprogram)).setPosition(int(pos_X) - 350, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(False)


                                 elif int(pos_X) == 897:
                                     if int(prog_width) == 167:
                                         self.getControl(int(prog_id)).setPosition(549, int(pos_Y))
                                         previousprogram = int(prog_id) - 1
                                         previousprogramX = self.getControl(int(previousprogram)).getX()
                                         previousprogramWidth = self.getControl(int(previousprogram)).getWidth()

                                         if previousprogramX == 724 and previousprogramWidth == 167:
                                             self.getControl(int(previousprogram)).setPosition(375, int(pos_Y))


                                 elif int(pos_X) == 549 and int(prog_width) >= 59:
                                     self.getControl(int(prog_id)).setVisible(False)
                                     self.getControl(int(prog_id)).setPosition(int(pos_X) - 350, int(pos_Y))



                                 elif int(pos_X) == 1073:
                                     if int(prog_width) == 167:
                                         self.getControl(int(prog_id)).setPosition(897, int(pos_Y))


                                     elif int(prog_width) == 342:
                                         self.getControl(int(prog_id)).setPosition(724, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogram_Width = self.getControl(int(nextprogram)).getWidth()

                                         if nextprogram_Width == 342:
                                             nextprograms = int(nextprogram) + 1
                                             self.getControl(int(nextprograms)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprograms)).setVisible(True)


                                     elif int(prog_width) == 692:
                                         self.getControl(int(prog_id)).setPosition(724, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogram_Width = self.getControl(int(nextprogram)).getWidth()


                                     elif int(prog_width) > 692:
                                         self.getControl(int(prog_id)).setPosition(724, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()


                                         if nextprogramX == 1073:
                                             self.getControl(int(nextprogram)).setPosition(int(pos_X) - 350, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(False)



                                 elif int(pos_X) == 1247 and int(prog_width) >= 59:
                                     self.getControl(int(prog_id)).setPosition(int(pos_X) - 350, int(pos_Y))



                                 elif int(pos_X) < 375:
                                     self.getControl(int(prog_id)).setVisible(False)
                                     self.getControl(int(prog_id)).setPosition(int(pos_X) - 350, int(pos_Y))



                         if self.time_flag == False:
                             if self.next_program == True:
                                 self.next_program = False
                             self.time_flag = True












             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             



                                
                                 

                                 elif int(pos_X) == 723:
                                     if int(prog_width) == 692:
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX != 1073:
                                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(True)



                                 elif int(pos_X) == 724:
                                     print "you are working on here now 2"

                                     if int(prog_width) == 692:
                                         print "you are here"
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX != 1073:
                                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(True)



                                     elif int(prog_width) == 626:
                                         print "you are here 2"
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX > 1073:
                                             self.getControl(int(nextprogram)).setPosition(1008, int(pos_Y))




                                 
                                 elif int(pos_X) == 1073:
                                     #self.getControl(int(prog_id)).setVisible(False)
                                     print "prog_width"
                                     print prog_width
                                     
                                     if int(prog_width) == 167:
                                         print "you are working on here now 3"
                                         currentProgram = int(prog_id)
                                         currentProgramX = self.getControl(int(currentProgram)).getX()

                                         if currentProgramX == 1073:
                                             print "you are working on here now 4"
                                             currentProgram2 = int(prog_id) - 2
                                             currentProgram2X = self.getControl(int(currentProgram2)).getX()
                                             currentProgram2_Width = self.getControl(int(currentProgram2)).getWidth()

                                             if currentProgram2X == 724 and currentProgram2_Width == 167:
                                                 self.getControl(int(currentProgram2)).setPosition(375, int(pos_Y))
                                                 currentProgram1 = int(prog_id) - 1
                                                 currentProgram1X = self.getControl(int(currentProgram1)).getX()
                                                 currentProgram1_Width = self.getControl(int(currentProgram1)).getWidth()

                                                 if currentProgram1X == 897 and currentProgram1_Width == 167:
                                                     self.getControl(int(currentProgram1)).setPosition(549, int(pos_Y))
                                                     currentProgramX = self.getControl(int(currentProgram)).getX()
                                                     currentProgram_Width = self.getControl(int(currentProgram)).getWidth()

                                                     if currentProgramX == 1073 and currentProgram_Width == 167:
                                                         self.getControl(int(currentProgram)).setPosition(724, int(pos_Y))
                                                         nextprogram = int(currentProgram) + 1
                                                         self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))
                                                         self.getControl(int(nextprogram)).setVisible(True)
                                                         nextprogramX = self.getControl(int(nextprogram)).getX()
                                                         nextprogram_Width = self.getControl(int(nextprogram)).getWidth()

                                                         if nextprogram_Width == 167:
                                                             nextprograms = int(nextprogram) + 1
                                                             self.getControl(int(nextprograms)).setPosition(1073, int(pos_Y))
                                                             self.getControl(int(nextprograms)).setVisible(True)


                                             else:
                                                 self.getControl(int(currentProgram)).setPosition(724, int(pos_Y))
                                                 CurrentprogramX = self.getControl(int(currentProgram)).getX()
                                                 nextprogram = int(currentProgram) + 1
                                                 nextprogramX = self.getControl(int(nextprogram)).getX()
                                                 nextprogram_Width = self.getControl(int(nextprogram)).getWidth()
                                                 print "CurrentprogramX"
                                                 print CurrentprogramX


                                                 if CurrentprogramX == 1073:
                                                     print "passed"
                                                     self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))
                                                     self.getControl(int(nextprogram)).setVisible(True)


                                                     if int(pos_X) == 375:
                                                         self.getControl(int(prog_id)).setVisbile(False)
                                                         



                                                 if nextprogram_Width == 167:
                                                     if nextprogram_Width != 897:
                                                         self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))
                                                         self.getControl(int(nextprogram)).setVisible(True)
                                                         nextprogram1 = int(nextprogram) + 1
                                                         nextprogram1X = self.getControl(int(nextprogram1)).getX()
                                                         nextprogram1_Width = self.getControl(int(nextprogram1)).getWidth()

                                                         if nextprogram1_Width == 167:
                                                             if nextprogram1X != 1073:
                                                                 self.getControl(int(nextprogram1)).setPosition(1073, int(pos_Y))
                                                                 self.getControl(int(nextprogram1)).setVisible(True)
                                                                 print "catch this 3"
                                                             else:
                                                                 print "catch this 4"



                                         elif currentProgramX == 724:
                                             print "you are working on here now 5"
                                             currentProgramWidth = self.getControl(int(prog_id)).getWidth()
                                             print currentProgramWidth

                                             if currentProgramWidth == 167:
                                                 nextprogram = int(prog_id) + 1
                                                 nextprogramX = self.getControl(int(nextprogram)).getX()

                                                 if nextprogramX > 1073:
                                                     print "you are working on here now 6"
                                                     self.getControl(int(nextprogram)).setPosition(897, int(pos_Y))
                                                     self.getControl(int(nextprogram)).setVisible(True)




                                         #if nextprogramsX == 724:
                                             #nextprogram2 = int(nextprogram1) + 1
                                             #self.getControl(int(nextprogram2)).setPosition(698, int(pos_Y))
                                         #else:
                                             #self.getControl(int(nextprogram1)).setPosition(897, int(pos_Y))
                                             #self.getControl(int(nextprogram1)).setVisible(True)


                                         #if nextprograms_width == 167:
                                             #nextprogram2 = int(nextprogram1) + 1
                                             #self.getControl(int(nextprogram2)).setPosition(1073, int(pos_Y))
                                             #self.getControl(int(nextprogram2)).setVisible(True)


                                     #if CurrentRow == 723:
                                         #print "fuckkkkkk you"
                                         #self.getControl(int(prog_id)).setPosition(724, int(pos_Y))


                                     elif int(prog_width) == 342:
                                         self.getControl(int(prog_id)).setPosition(int(pos_X) - 350, int(pos_Y))
                                         CurrentRowX = self.getControl(int(prog_id)).getX()

                                         if CurrentRowX == 723:
                                             self.getControl(int(prog_id)).setPosition(724, int(pos_Y))

                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX != 1073:
                                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(True)


                                     else:
                                         self.getControl(int(prog_id)).setPosition(int(pos_X) - 350, int(pos_Y))



                                 elif int(pos_X) == 1247 and int(prog_width) >= 59:
                                     self.getControl(int(prog_id)).setPosition(int(pos_X) - 350, int(pos_Y))



                                 elif int(pos_X) < 375:
                                     self.getControl(int(prog_id)).setVisible(False)
                                     self.getControl(int(prog_id)).setPosition(int(pos_X) - 350, int(pos_Y))




                             



 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 








 
 
 
 
 
 
 
 



                                 



                                 


                                 elif int(pos_X) == 549 and int(prog_width) >= 59:
                                     self.getControl(int(prog_id)).setVisible(False)
                                     self.getControl(int(prog_id)).setPosition(int(pos_X) - 350, int(pos_Y))



                                 elif int(pos_X) == 724:
                                     if int(prog_width) == 167:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))


                                     elif int(prog_width) == 342:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX != 724:
                                             self.getControl(int(nextprogram)).setPosition(724, int(pos_Y))


                                     elif int(prog_width) == 692:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX != 1073:
                                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(True)



                                     elif int(prog_width) > 692:
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX == 1073:
                                             self.getControl(int(nextprogram)).setPosition(int(pos_X) - 350, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(False)


                                 elif int(pos_X) == 723:
                                     if int(prog_width) == 692:
                                         print "move itttttttttttttt"


                                 elif int(pos_X) == 897:
                                     if int(prog_width) == 167:
                                         self.getControl(int(prog_id)).setPosition(549, int(pos_Y))


                                 elif int(pos_X) == 1073:
                                     if int(prog_width) == 167:
                                         self.getControl(int(prog_id)).setPosition(897, int(pos_Y))


                                     elif int(prog_width) == 342:
                                         self.getControl(int(prog_id)).setPosition(724, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX != 1073:
                                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(True)


                                     elif int(prog_width) == 692:
                                         self.getControl(int(prog_id)).setPosition(724, int(pos_Y))


                                     elif int(prog_width) > 692:
                                         self.getControl(int(prog_id)).setPosition(724, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()


                                         if nextprogramX == 1073:
                                             self.getControl(int(nextprogram)).setPosition(int(pos_X) - 350, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(False)



                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             









                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             



                                 



                                 




                                 



                                 



                                 



                                 elif int(pos_X) == 549 and int(prog_width) >= 59:
                                     self.getControl(int(prog_id)).setVisible(False)
                                     self.getControl(int(prog_id)).setPosition(int(pos_X) - 350, int(pos_Y))



                                 elif int(pos_X) == 723:
                                     if int(prog_width) == 167:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))


                                     elif int(prog_width) == 342:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogram_Width = self.getControl(int(nextprogram)).getWidth()

                                         if nextprogram_Width == 342:
                                             nextprograms = int(nextprogram) + 1
                                             self.getControl(int(nextprograms)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprograms)).setVisible(True)


                                     elif int(prog_width) == 692:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX != 1073:
                                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(True)


                                     elif int(prog_width) > 692:
                                         nextprogram = int(prog_id) + 1


                                 elif int(pos_X) == 724:
                                     if int(prog_width) == 167:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))


                                     elif int(prog_width) == 342:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogram_Width = self.getControl(int(nextprogram)).getWidth()

                                         if nextprogram_Width == 342:
                                             nextprograms = int(nextprogram) + 1
                                             self.getControl(int(nextprograms)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprograms)).setVisible(True)


                                     elif int(prog_width) == 692:
                                         self.getControl(int(prog_id)).setPosition(375, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX != 1073:
                                             self.getControl(int(nextprogram)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(True)


                                     elif int(prog_width) > 692:
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()

                                         if nextprogramX == 1073:
                                             self.getControl(int(nextprogram)).setPosition(int(pos_X) - 350, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(False)


                                 elif int(pos_X) == 897:
                                     if int(prog_width) == 167:
                                         self.getControl(int(prog_id)).setPosition(549, int(pos_Y))
                                         previousprogram = int(prog_id) - 1
                                         previousprogramX = self.getControl(int(previousprogram)).getX()
                                         previousprogramWidth = self.getControl(int(previousprogram)).getWidth()

                                         if previousprogramX == 724 and previousprogramWidth == 167:
                                             self.getControl(int(previousprogram)).setPosition(375, int(pos_Y))


                                 elif int(pos_X) == 549 and int(prog_width) >= 59:
                                     self.getControl(int(prog_id)).setVisible(False)
                                     self.getControl(int(prog_id)).setPosition(int(pos_X) - 350, int(pos_Y))



                                 elif int(pos_X) == 1073:
                                     if int(prog_width) == 167:
                                         self.getControl(int(prog_id)).setPosition(897, int(pos_Y))


                                     elif int(prog_width) == 342:
                                         self.getControl(int(prog_id)).setPosition(724, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogram_Width = self.getControl(int(nextprogram)).getWidth()

                                         if nextprogram_Width == 342:
                                             nextprograms = int(nextprogram) + 1
                                             self.getControl(int(nextprograms)).setPosition(1073, int(pos_Y))
                                             self.getControl(int(nextprograms)).setVisible(True)


                                     elif int(prog_width) == 692:
                                         self.getControl(int(prog_id)).setPosition(724, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogram_Width = self.getControl(int(nextprogram)).getWidth()


                                     elif int(prog_width) > 692:
                                         self.getControl(int(prog_id)).setPosition(724, int(pos_Y))
                                         nextprogram = int(prog_id) + 1
                                         nextprogramX = self.getControl(int(nextprogram)).getX()


                                         if nextprogramX == 1073:
                                             self.getControl(int(nextprogram)).setPosition(int(pos_X) - 350, int(pos_Y))
                                             self.getControl(int(nextprogram)).setVisible(False)



                                 elif int(pos_X) == 1247 and int(prog_width) >= 59:
                                     self.getControl(int(prog_id)).setPosition(int(pos_X) - 350, int(pos_Y))



                                 elif int(pos_X) < 375:
                                     self.getControl(int(prog_id)).setVisible(False)
                                     self.getControl(int(prog_id)).setPosition(int(pos_X) - 350, int(pos_Y))



                         if self.time_flag == False:
                             if self.next_program == True:
                                 self.next_program = False
                             self.time_flag = True



         if CurrentRow >= 59:
             program_button = [elem.control for elem in self.program_buttons]
             program_id = list()
             program_width = list()
             programs_stop_time = list()
             posX = list()
             posY = list()


             for stop_time in self.program_stop_clock:
                 programs_stop_time.append(stop_time)


             for elem in program_button:
                 program_id.append(elem.getId())
                 posX.append(elem.getX())
                 posY.append(elem.getY())
                 program_width.append(elem.getWidth())
             program_id = map(str, program_id)
             posX = map(str, posX)
             posY = map(str, posY)
             program_width = map(str, program_width)
             programs_stop_time = map(str, programs_stop_time)
             half_hour = str(self.getControl(344).getLabel())
             one_hour = str(self.getControl(345).getLabel())
             one_hour_half = str(self.getControl(346).getLabel())
             epg_time_1 = time.strptime(half_hour, '%I:%M%p')
             epg_time_2 = time.strptime(one_hour, '%I:%M%p')
             epg_time_3 = time.strptime(one_hour_half, '%I:%M%p')


             for pos_X, prog_width, prog_id in zip(posX, program_width, program_id):
                 prog_width = int(prog_width)



             #for pos_X, pos_Y, prog_width, prog_id, prog_stop_time in zip(posX, posY, program_width, program_id, programs_stop_time):
                 #program_stop_time = time.strptime(prog_stop_time, '%I:%M%p')
                 
                 #print prog_width

                 if int(pos_X) == 375:

                     #2 hours
                     if int(prog_width) == 1368:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')

                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time == epg_time_3:
                                 prog_width = 692
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 677
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #2 hours 10 minutes
                     elif int(prog_width) == 1482:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')

                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 456
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))


                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 1026
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #2 hours 20 minutes
                     elif int(prog_width) == 1596:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')

                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 567
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 1026
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #2 hours 30 minutes
                     elif int(prog_width) == 1710:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')

                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))


                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time == epg_time_3:
                                 prog_width = 692
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 1019
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #2 hours 40 minutes
                     elif int(prog_width) == 1824:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')

                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 456
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 1368
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))




                     #2 hours 45 minutes
                     elif int(prog_width) == 1881:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')

                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 515
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if pos_X >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 1364
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #3 hours
                     elif int(prog_width) == 2052:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time == epg_time_3:
                                 prog_width = 692
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 1361
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #3 hours 10 minutes
                     elif int(prog_width) == 2166:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 456
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 1710
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #3 hours 20 minutes
                     elif int(prog_width) == 2320:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 567
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 1710
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #3 hours 30 minutes
                     elif int(prog_width) == 2394:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time == epg_time_3:
                                 prog_width = 692
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 1703
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #3 hours 40 minutes
                     elif int(prog_width) == 2508:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 456
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 2052
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #3 hours 45 minutes
                     elif int(prog_width) == 2565:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 515
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 2048
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #4 hours
                     elif int(prog_width) == 2736:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time == epg_time_3:
                                 prog_width = 692
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 2045
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #4 hours 10 minutes
                     elif int(prog_width) == 2964:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 456
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 2508
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #4 hours 20 minutes
                     elif int(prog_width) == 3078:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 567
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 2508
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #4 hours 30 minutes
                     elif int(prog_width) == 3192:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time == epg_time_3:
                                 prog_width = 692
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 2501
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #4 hours 40 minutes
                     elif int(prog_width) == 3306:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 456
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 2850
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #4 hours 45 minutes
                     elif int(prog_width) == 3363:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 515
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 2846
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #5 hours
                     elif int(prog_width) == 3420:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time == epg_time_3:
                                 prog_width = 692
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 2729
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #5 hours 10 minutes
                     elif int(prog_width) == 3534:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 456
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 3078
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #5 hours 20 minutes
                     elif int(prog_width) == 3648:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 567
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 3078
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #5 hours 30 minutes
                     elif int(prog_width) == 3762:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time == epg_time_3:
                                 prog_width = 692
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 3071
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #5 hours 40 minutes
                     elif int(prog_width) == 3876:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 456
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 3420
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #5 hours 45 minutes
                     elif int(prog_width) == 3933:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 515
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 3416
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #6 hours
                     elif int(prog_width) == 4104:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time == epg_time_3:
                                 prog_width = 692
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 3413
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #6 hours 10 minutes
                     elif int(prog_width) == 4218:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 456
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 3762
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #6 hours 20 minutes
                     elif int(prog_width) == 4332:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 567
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 3762
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #6 hours 30 minutes
                     elif int(prog_width) == 4446:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time == epg_time_3:
                                 prog_width = 692
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 3755
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #6 hours 40 minutes
                     elif int(prog_width) == 4560:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 456
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 4104
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #6 hours 45 minutes
                     elif int(prog_width) == 4617:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 515
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 4100
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #7 hours
                     elif int(prog_width) == 4788:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time == epg_time_3:
                                 prog_width = 692
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 4097
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #7 hours 10 minutes
                     elif int(prog_width) == 4902:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 456
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 4446
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #7 hours 20 minutes
                     elif int(prog_width) == 5016:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 567
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 4446
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #7 hours 30 minutes
                     elif int(prog_width) == 5130:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time == epg_time_3:
                                 prog_width = 692
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 4439
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #7 hours 40 minutes
                     elif int(prog_width) == 5244:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 456
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 4788
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #7 hours 45 minutes
                     elif int(prog_width) == 5301:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time < epg_time_3:
                                 prog_width = 515
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 4784
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     #8 hours
                     elif int(prog_width) == 5472:
                         if self.channelsOnRight == True:
                             posY = int(self.getControl(int(prog_id)).getY())
                             index = 0

                             if int(posY) == 315:
                                 index = 0
                             elif int(posY) == 353:
                                 index = 1
                             elif int(posY) == 391:
                                 index = 2
                             elif int(posY) == 428:
                                 index = 3
                             elif int(posY) == 466:
                                 index = 4
                             elif int(posY) == 504:
                                 index = 5
                             elif int(posY) == 542:
                                 index = 6

                             program_clock_time = self.program_stop_clock
                             program_stop_time = time.strptime(program_clock_time[index], '%I:%M%p')


                             if program_stop_time > epg_time_3:
                                 prog_width = self.getControl(int(prog_id)).getWidth()
                                 prog_width - prog_width - 342
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 348
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                             elif program_stop_time == epg_time_3:
                                 prog_width = 692
                                 self.getControl(int(prog_id)).setWidth(prog_width)
                                 program_id = list()
                                 posX = list()
                                 posY = list()
                                 program_button = [elem.control for elem in self.program_buttons]
                                 pos_X = self.getControl(int(prog_id)).getX()
                                 pos_Y = self.getControl(int(prog_id)).getY()
                                 self.getControl(int(prog_id)).setPosition(int(pos_X), int(pos_Y))

                                 for elem in program_button:
                                     program_id.append(elem.getId())
                                     posX.append(elem.getX())
                                     posY.append(elem.getY())

                                 program_id = map(str, program_id)
                                 posX = map(str, posX)
                                 posY = map(str, posY)
                                 getY = self.getControl(int(prog_id)).getY()

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, program_id):
                                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                         posX = int(pos_X) - 4781
                                         posY = int(getY)
                                         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))                                        

