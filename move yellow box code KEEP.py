#THIS IS USED FOR SET THE TIME CLOCK, TO ENABLE MAKE SURE YOU USE self.time_flag = True
                 #OR self.time_flag = False to disabled
                 if CurrentRow == 375 and CurrentWidth <= 344:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 375 and CurrentWidth >= 691:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 441 and CurrentWidth <= 344:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 441 and CurrentWidth >= 456:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True

                 
                 elif CurrentRow == 549 and CurrentWidth <= 567:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 549 and CurrentWidth > 567:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 
                 
                 elif CurrentRow == 610 and CurrentWidth >= 691:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 659 and CurrentWidth <= 344:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 
                      
                     
                 elif CurrentRow == 659 and CurrentWidth >= 691:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 724 and CurrentWidth <= 344:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 elif CurrentRow == 724 and CurrentWidth >= 567:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                     print "you are in the 724 and 691 area 2"
                 
                 
                 
                 elif CurrentRow == 790 and CurrentWidth >= 691:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 elif CurrentRow == 837 and CurrentWidth >= 691:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True

                 elif CurrentRow == 897 and CurrentWidth >= 691:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True

                 
                 
                 elif CurrentRow == 949 and CurrentWidth >= 344:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 
                 
                 
                 elif CurrentRow == 959 and CurrentWidth >= 344:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                     
                     
                 elif CurrentRow == 1009 and CurrentWidth <= 567:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 
                 elif CurrentRow == 1009 and CurrentWidth >= 692:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 1025 and CurrentWidth > 59:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 1072 and CurrentWidth < 342:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = False
                 
                 
                 elif CurrentRow == 1072 and CurrentWidth >= 342:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 
                 
                 
                 elif CurrentRow == 1080 and CurrentWidth >= 59:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 1138 and CurrentWidth >= 59:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 1189 and CurrentWidth >= 691:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 elif CurrentRow == 1238 and CurrentWidth >= 59:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True
                 
                 
                 elif CurrentRow == 1246 and CurrentWidth >= 59:
                     if self.next_program == True:
                         self.next_program = False
                     self.time_flag = True






---------------------------------------------------------------------------------------------------

             #This code is used for to allow the button to move to the right
             if self.move_right_flag == False:
                 if CurrentRow == 375 and CurrentWidth <= 691:
                     self.programs_Index_flag = True
                     self.previous_program = True

                 elif CurrentRow == 375 and CurrentWidth > 691:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)


                 #elif CurrentRow == 441 and CurrentWidth <= 691:
                     #self.previous_program = True
                     #self.programs_Index_flag = True
                     
                     #print "disable this 22"
                     
                 elif CurrentRow == 441 and CurrentWidth > 691:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     
                     print "disable this 2"
                 
                 
                 
                 
                 #FIX THIS CHRIS TEST IT
                 elif CurrentRow == 549 and CurrentWidth >= 691:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                 
                 
                 
                 
                 #elif CurrentRow == 610 and CurrentWidth < 691:
                     #self.previous_program = True
                     #self.programs_Index_flag = True
                     
                     #print "disable this 21"
                     
                 elif CurrentRow == 610 and CurrentWidth >= 691:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     
                     print "disable this 3"
                 elif CurrentRow == 659 and CurrentWidth <= 691:
                     self.programs_Index_flag = True
                     self.previous_program = True
                     
                     print "disable this 20"
                 elif CurrentRow == 659 and CurrentWidth > 691:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     
                     print "disable this 4"
                     
                     
                 #elif CurrentRow == 724 and CurrentWidth < 691:
                     #self.programs_Index_flag = True
                     #self.previous_program = True
                     #print "disable this 19"
                 elif CurrentRow == 724 and CurrentWidth >= 691:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "disable this 5"
                 
                 
                 #elif CurrentRow == 790 and CurrentWidth < 567:
                     #self.previous_program = True
                     #self.programs_Index_flag = True
                     
                     #print "disable this 21"
                     
                 elif CurrentRow == 790 and CurrentWidth >= 626:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                 
                 
                 
                 
                 
                 
                 elif CurrentRow == 837 and CurrentWidth >= 691:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "disable this 7"

                     
                     
                     
                 elif CurrentRow == 847 and CurrentWidth <= 567:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "disable this 8"

                 elif CurrentRow == 897 and CurrentWidth >= 691:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "catch this 1"
                 


                 #FIX THIS CHRIS TEST IT
                 elif CurrentRow == 949 and CurrentWidth >= 342:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)


                 
                 #FIX THIS CHRIS TEST IT
                 elif CurrentRow == 959 and CurrentWidth >= 342:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     print "disable this 9"
                 
                 
                 
                 
                 elif CurrentRow == 1009 and CurrentWidth >= 342:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     
                     print "disable this 10"
                     
                 elif CurrentRow == 1025 and CurrentWidth >= 342:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                 
                     print "disable this 11"
                     
                 elif CurrentRow == 1072 and CurrentWidth >= 227:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     
                     print "catch this 2"
                 
                 
                 elif CurrentRow == 1138 and CurrentWidth >= 117:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     
                     print "disable this 13"
                     
                 elif CurrentRow == 1189 and CurrentWidth >= 691:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                 
                     print "disable this 14"
                 
                 elif CurrentRow == 1238 and CurrentWidth >= 59:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                 
                     print "disable this 15"
                 
                 #FIX THE PROGRAM BUTTON DISABLE THE SELF.PROGRAM_INDEX TO STOP YELLOW BUTTON TO MOVE TO THE NEXT BUTTON FOR THE BIG BUTTON
                 elif CurrentRow == 1246 and CurrentWidth >= 59:
                     self.previous_program = True
                     self.move_right_flag = True
                     move_right.GoRight(self)
                     
                     print "disable this 16"



         if self.channel_page >= 0 and self.channel_page < 15750:
             if self.move_right_flag == False:
                 self.channel_page += 75

             if self.previous_program == True:
                 self.next_program = True



         if self.channel_page == 15750:
             if CurrentRow == 724 and CurrentWidth <= 691:
                 if self.lastchannels == False:
                     self.lastchannels = True
                     self.programs_Index_flag = True

             if CurrentRow == 1072 and CurrentWidth == 342:
                 if self.lastchannels == False:
                     self.lastchannels = True
                     self.programs_Index_flag = True



------------------------------------------------------------------------------------------------
         #FIX THIS YELLOW BOX TEST THIS CHRIS
         #if CurrentRow == 375 and CurrentWidth <= 691:
             #print "you are in the 375 and 691a for the yellow button"
             #if self.channel_page >= 0:
                 #self.programs_Index_flag = True
                 #self.previous_program = True

                 #if self.next_program == True:
                     #self.next_program = False

                     #if self.time_flag == False:
                         #self.time_flag = True

                     #if self.move_right_flag == False:
                         #self.move_right_flag = True



         #NOT REALLY SURE IF NEED TO KEEP THIS AS THE CODE ARE WRITTEN ON ABOVE <= 691 WHICH IS NOW <= 857
         #if CurrentRow == 375 and CurrentWidth == 691:
             #print "you are in the 375 and 691"
             #if self.channel_page > 0:
                 #if self.move_program_flag == True:
                     #self.move_program_flag = False

             #if self.channel_page >= 0 and self.channel_page < 15750:
                 #CurrentProgram = int(CurrentId)
                 #CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 #if CurrentProgram_Width <= 691:
                     #self.programs_Index_flag = True

                 #if self.channelsOnLeft == True:
                     #self.channelsOnLeft = False
                     #self.channelsOnRight = True

                 #elif self.channelsOnMiddle == True:
                     #self.channelsOnMiddle = False
                     #self.channelsOnRight = True

                 #if self.next_program == True:
                     #self.next_program = False

                 #if self.time_flag == False:
                     #self.time_flag = True

                 #if self.move_right_flag == False:
                     #self.move_right_flag = True



         #if CurrentRow == 375 and CurrentWidth >= 857 and CurrentWidth <= 918:
             #if self.channel_page >= 0 and self.channel_page < 15750:
                 #print "you are in 517"
                 #self.programs_Index_flag = True
                 #self.previous_program = True

                 #if self.next_program == True:
                     #self.next_program = False

                 #if self.time_flag == False:
                     #self.time_flag = True

                 #if self.move_right_flag == False:
                     #self.move_right_flag = True



         





         #if CurrentRow == 441 and CurrentWidth == 167:
             #if self.channel_page >= 0 and self.channel_page < 15750:
                 #self.programs_Index_flag = True
                 #self.previous_program = True



         #if CurrentRow == 441 and CurrentWidth == 396:
             #if self.channel_page >= 0 and self.channel_page < 15750:
                 #CurrentProgram = int(CurrentId)
                 #CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 #if CurrentProgram_Width <= 691:
                     #self.programs_Index_flag = True
                     #self.time_flag = True
                     #self.next_program = False

                     #if self.channelsOnMiddle == True:
                         #self.channelsOnMiddle = False
                         #self.channelsOnRight = True



         #FIX THIS YELLOW BOX TEST THIS CHRIS
         elif CurrentRow == 441 and CurrentWidth <= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 if CurrentProgram_Width <= 691:
                     self.programs_Index_flag = True
                     self.time_flag = True
                     self.next_program = False

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True



         #FIX THIS YELLOW BOX TEST THIS CHRIS
         elif CurrentRow == 441 and CurrentWidth > 1038:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 if self.channelsOnMiddle == True:
                     self.channelsOnMiddle = False
                     self.channelsOnLeft = True

                 if self.next_program == True:
                     self.next_program = False

                 if self.time_flag == False:
                     self.time_flag = True




         #FIX THIS YELLOW BOX TEST THIS CHRIS
         elif CurrentRow >= 549 and CurrentWidth <= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 if CurrentProgram_Width <= 691:
                     self.programs_Index_flag = True
                     self.time_flag = True
                     self.next_program = False

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True


                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True



         #FIX FOR YELLOW BOX TEST THIS CHRIS
         elif CurrentRow >= 549 and CurrentWidth >= 1026:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 if CurrentProgram_Width <= 691:
                     self.programs_Index_flag = True

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True
                     else:
                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnLeft = True

                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True



         #FIX THIS YELLOW BOX TEST THIS CHRIS
         elif CurrentRow == 610 and CurrentWidth <= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 if self.channelsOnLeft == True:
                     self.channelsOnLeft = False
                     self.channelsOnRight = True

                 if self.next_program == True:
                     self.next_program = False

                 if self.time_flag == False:
                     self.time_flag = True

                 if self.move_right_flag == False:
                     self.move_right_flag = True




         #if CurrentRow == 659 and CurrentWidth == 167:
             #if self.channel_page >= 0 and self.channel_page < 15750:
                 #self.programs_Index_flag = True
                 #self.previous_program = True



         #if CurrentRow == 659 and CurrentWidth == 396:
             #if self.channel_page >= 0 and self.channel_page < 15750:
                 #CurrentProgram = int(CurrentId)
                 #CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 #if CurrentProgram_Width <= 691:
                     #self.programs_Index_flag = True
                     #self.time_flag = True
                     #self.next_program = False

                     #if self.channelsOnMiddle == True:
                         #self.channelsOnMiddle = False
                         #self.channelsOnRight = True



         #if CurrentRow == 659 and CurrentWidth == 342:
             #if self.channel_page >= 0 and self.channel_page < 15750:
                 #CurrentProgram = int(CurrentId)
                 #CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 #if CurrentProgram_Width <= 691:
                     #self.programs_Index_flag = True
                     #self.time_flag = True
                     #self.next_program = False

                     #if self.channelsOnMiddle == True:
                         #self.channelsOnMiddle = False
                         #self.channelsOnRight = True



         #FIX THIS YELLOW BOX TEST THIS CHRIS
         elif CurrentRow == 659 and CurrentWidth <= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 if CurrentProgram_Width <= 691:
                     self.programs_Index_flag = True

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True

                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True
             else:
                 if self.lastchannels == True:
                     self.lastchannels = False



         #FIX THIS YELLOW BOX TEST THIS CHRIS
         elif CurrentRow == 659 and CurrentWidth >= 1026:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 if CurrentProgram_Width <= 691:
                     self.programs_Index_flag = True

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True
                     else:
                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = Fals
                             self.channelsOnLeft = True

                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True



         #if CurrentRow == 724 and CurrentWidth <= 227:
             #if self.channel_page >= 0 and self.channel_page < 15750:
                 #CurrentProgram = int(CurrentId)
                 #CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 #if CurrentProgram_Width <= 691:
                     #self.programs_Index_flag = True

                     #if self.channelsOnMiddle == True:
                         #self.channelsOnMiddle = False
                         #self.channelsOnLeft = True

                     #if self.next_program == True:
                         #self.next_program = False

                     #if self.time_flag == False:
                         #self.time_flag = True

                     #if self.move_right_flag == False:
                         #self.move_right_flag = True



         #if CurrentRow == 724 and CurrentWidth == 342:
             #if self.channel_page == 15750:
                 #self.programs_Index_flag = True




         #FIX THIS YELLOW BOX TEST THIS CHRIS
         elif CurrentRow == 724 and CurrentWidth <= 691:
             print "you are in the 724 and 691 area 5"
             if self.channel_page >= 0 and self.channel_page < 15750:
                 if self.channelsOnLeft == True:
                     self.channelsOnLeft = False
                     self.channelsOnRight = True

                 if self.next_program == True:
                     self.next_program = False

                 if self.time_flag == False:
                     self.time_flag = True

                 if self.move_right_flag == False:
                     self.move_right_flag = True




         #FIX THIS YELLOW BOX TEST THIS CHRIS
         elif CurrentRow == 724 and CurrentWidth >= 1038:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 if CurrentProgram_Width <= 691:
                     self.programs_Index_flag = True

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True
                     else:
                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = Fals
                             self.channelsOnLeft = True

                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True



         #FIX THIS YELLOW BOX TEST THIS CHRIS
         elif CurrentRow == 790 and CurrentWidth <= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 if self.channelsOnLeft == True:
                     self.channelsOnLeft = False
                     self.channelsOnRight = True

                 if self.next_program == True:
                     self.next_program = False

                 if self.time_flag == False:
                     self.time_flag = True

                 if self.move_right_flag == False:
                     self.move_right_flag = True


         #if CurrentRow == 790 and CurrentWidth == 396:
             #if self.channel_page >= 0 and self.channel_page < 15750:
                 #CurrentProgram = int(CurrentId)
                 #CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 #if CurrentProgram_Width <= 691:
                     #self.programs_Index_flag = True
                     #self.time_flag = True
                     #self.next_program = False

                     #if self.channelsOnMiddle == True:
                         #self.channelsOnMiddle = False
                         #self.channelsOnRight = True



         #FIX THIS YELLOW BOX TEST THIS CHRIS
         elif CurrentRow == 790 and CurrentWidth <= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 if CurrentProgram_Width <= 691:
                     self.programs_Index_flag = True
                     self.time_flag = True
                     self.next_program = False

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True



         #FIX THIS YELLOW BOX TEST THIS CHRIS
         elif CurrentRow == 790 and CurrentWidth >= 1038:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 if self.channelsOnMiddle == True:
                     self.channelsOnMiddle = False
                     self.channelsOnLeft = True

                 if self.next_program == True:
                     self.next_program = False

                 if self.time_flag == False:
                     self.time_flag = True



         #FIX THIS YELLOW BOX TEST THIS CHRIS
         elif CurrentRow == 837 and CurrentWidth <= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 if CurrentProgram_Width <= 691:
                     self.programs_Index_flag = True
                     self.time_flag = True
                     self.next_program = False

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True




         #FIX THIS YELLOW BOX TEST THIS CHRIS
         elif CurrentRow == 837 and CurrentWidth >= 1038:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 if CurrentProgram_Width <= 691:
                     self.programs_Index_flag = True

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True
                     else:
                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = Fals
                             self.channelsOnLeft = True

                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True




         #if CurrentRow == 897 and CurrentWidth <= 342:
             #print "you are in the 897 and 342"
             #if self.channel_page >= 0 and self.channel_page < 15750:
                 #self.programs_Index_flag = True
                 #print "you are in the 897 and 691 area 4"

                 #if self.channelsOnLeft == True:
                     #self.channelsOnLeft = False
                     #self.channelsOnRight = True

                 #if self.next_program == True:
                     #self.next_program = False

                 #if self.time_flag == False:
                     #self.time_flag = True

                 #if self.move_right_flag == True:
                     #self.move_right_flag = False



         #YOU HAVE FIXED THIS FOR THE YELLOW BOX TO GO TO THE NEXT BOX DO NOT REMOVE IT
         #if CurrentRow == 897 and CurrentWidth >= 691:
             #if self.channel_page >= 0 and self.channel_page < 15750:
                 #CurrentProgram = int(CurrentId)
                 #CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 #print "you are in the 897 and 691 area 5"
                 #self.programs_Index_flag = False

                 #if CurrentProgram_Width >= 691:
                     #self.programs_Index_flag = True


                     #if self.channelsOnMiddle == True:
                         #self.channelsOnMiddle = False
                         #self.channelsOnRight = True
                     #else:
                         #if self.channelsOnMiddle == True:
                             #self.channelsOnMiddle = False
                             #self.channelsOnLeft = True

                     #if self.next_program == True:
                         #self.next_program = False

                     #if self.time_flag == False:
                         #self.time_flag = True

                     #if self.move_right_flag == False:
                         #self.move_right_flag = True





         #YOU HAVE FIXED THIS FOR THE YELLOW BOX TO GO TO THE NEXT BOX DO NOT REMOVE IT
         elif CurrentRow == 897 and CurrentWidth >= 1038:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 if CurrentProgram_Width <= 691:
                     self.programs_Index_flag = True

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True
                     else:
                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = Fals
                             self.channelsOnLeft = True

                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True





         #if CurrentRow == 949 and CurrentWidth == 167 or CurrentRow == 955 or CurrentRow == 959 and CurrentWidth == 167:
             #if self.channel_page >= 0 and self.channel_page < 15750:
                 #CurrentProgram = int(CurrentId)
                 #CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 #if CurrentProgram_Width <= 691:
                     #self.programs_Index_flag = True
                     #self.time_flag = True
                     #self.next_program = False

                     #if self.channelsOnMiddle == True:
                         #self.channelsOnMiddle = False
                         #self.channelsOnRight = True



         #if CurrentRow == 949 or CurrentRow == 955 or CurrentRow == 959 and CurrentWidth == 342 or CurrentRow == 959 and CurrentWidth == 342:
             #if self.channel_page >= 0 and self.channel_page < 15750:
                 #CurrentProgram = int(CurrentId)
                 #CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 #if #CurrentProgram_Width <= 691:
                     #self.programs_Index_flag = True
                     #self.time_flag = True
                     #self.next_program = False

                     #if self.channelsOnMiddle == True:
                         #self.channelsOnMiddle = False
                         #self.channelsOnRight = True



         #YOU HAVE FIXED THIS FOR THE YELLOW BOX TO GO TO THE NEXT BOX DO NOT REMOVE IT
         elif CurrentRow >= 949 and CurrentRow <= 959 and CurrentWidth <= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 if CurrentProgram_Width <= 691:
                     self.programs_Index_flag = True
                     self.time_flag = True
                     self.next_program = False

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True


                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True



         #FIX FOR YELLOW BOX TEST THIS CHRIS
         elif CurrentRow >= 949 and CurrentRow <= 959 and CurrentWidth >= 1038:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 if CurrentProgram_Width <= 691:
                     self.programs_Index_flag = True

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True
                     else:
                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = False
                             self.channelsOnLeft = True

                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True



         #if CurrentRow == 959 and CurrentWidth <= 344:
             #if self.channel_page >= 0 and self.channel_page < 15750:
                 #CurrentProgram = int(CurrentId)
                 #CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 #self.programs_Index_flag = True
                 #self.previous_program = True


                 #if CurrentProgram_Width <= 691:
                     #self.programs_Index_flag = True
                     #self.time_flag = False
                     #self.next_program = False

                     #if self.channelsOnLeft == True:
                         #self.channelsOnLeft = False
                         #self.channelsOnMiddle = True



         elif CurrentRow == 1009 and CurrentWidth >= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 if CurrentProgram_Width <= 691:
                     self.programs_Index_flag = True
                     self.time_flag = True
                     self.next_program = False

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True


                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True



         elif CurrentRow == 1009 and CurrentWidth >= 1038:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 if CurrentProgram_Width <= 691:
                     self.programs_Index_flag = True

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True
                     else:
                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = Fals
                             self.channelsOnLeft = True

                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True



         #if CurrentRow == 1009 and CurrentWidth <= 167:
             #if self.channel_page >= 0 and self.channel_page < 15750:
                 #CurrentProgram = int(CurrentId)
                 #CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                 #print "CurrentProgram_Width"
                 #print CurrentProgram_Width

                 #if CurrentProgram_Width <= 167:
                     #self.programs_Index_flag = True
                     #self.time_flag = True
                     #self.next_program = False
                     #print "self.programs_Index_flag"
                     #print self.programs_Index_flag

                     #if self.channelsOnMiddle == True:
                         #self.channelsOnMiddle = False
                         #self.channelsOnRight = True



         elif CurrentRow == 1025 and CurrentWidth <= 691:
             if self.channel_page >= 0:
                 self.programs_Index_flag = True
                 self.previous_program = True

                 if self.next_program == True:
                     self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True




         elif CurrentRow == 1072 and CurrentWidth <= 167:
             if self.channel_page >= 0:
                 self.programs_Index_flag = True
                 self.previous_program = True

                 if self.next_program == True:
                     self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     if self.move_right_flag == False:
                         self.move_right_flag = True




         elif CurrentRow == 1072 and CurrentWidth <= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 if CurrentWidth <= 567:
                     pass
                 #else:
                     #CurrentProgram = int(CurrentId)
                     #CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()
                     #print "you have catch this chris"

                     #if CurrentProgram_Width <= 691:
                         #self.programs_Index_flag = True

                         #if self.channelsOnMiddle == True:
                             #self.channelsOnMiddle = False
                             #self.channelsOnRight = True
                         #else:
                             #if self.channelsOnMiddle == True:
                                 #self.channelsOnMiddle = False
                                 #self.channelsOnLeft = True

                         #if self.next_program == True:
                             #self.next_program = False

                         #if self.time_flag == False:
                             #self.time_flag = True

                         #if self.move_right_flag == False:
                             #self.move_right_flag = True




         elif CurrentRow == 1072 and CurrentWidth > 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 print "you are using 1072 2"

                 if self.channelsOnRight == True:
                     self.channelsOnRight = False
                     self.channelsOnMiddle = True

                 elif self.channelsOnMiddle == True:
                     self.channelsOnMiddle = False
                     self.channelsOnRight = True

                 if self.next_program == True:
                     self.next_program = False

                 if self.time_flag == False:
                     self.time_flag = True

                 if self.move_right_flag == False:
                     self.move_right_flag = True



         elif CurrentRow == 1138 and CurrentWidth >= 59:
             if self.channel_page >= 0 and self.channel_page < 15750:

                 if self.channelsOnRight == True:
                     self.channelsOnRight = False
                     self.channelsOnMiddle = True

                 elif self.channelsOnMiddle == True:
                     self.channelsOnMiddle = False
                     self.channelsOnRight = True

                 if self.next_program == True:
                     self.next_program = False

                 if self.time_flag == False:
                     self.time_flag = True

                 if self.move_right_flag == False:
                     self.move_right_flag = True




         elif CurrentRow == 1238 and CurrentWidth >= 59:
             if self.channel_page >= 0 and self.channel_page < 15750:

                 if self.channelsOnRight == True:
                     self.channelsOnRight = False
                     self.channelsOnMiddle = True

                 elif self.channelsOnMiddle == True:
                     self.channelsOnMiddle = False
                     self.channelsOnRight = True

                 if self.next_program == True:
                     self.next_program = False

                 if self.time_flag == False:
                     self.time_flag = True

                 if self.move_right_flag == False:
                     self.move_right_flag = True




         #if CurrentRow == 1246 and CurrentWidth == 167:
             #if self.channel_page >= 0 and self.channel_page < 15750:
                 #CurrentProgram = int(CurrentId)
                 #CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 #if CurrentProgram_Width <= 691:
                     #self.programs_Index_flag = True
                     #self.time_flag = True
                     #self.next_program = False

                     #if self.channelsOnMiddle == True:
                         #self.channelsOnMiddle = False
                         #self.channelsOnRight = True




         elif CurrentRow == 1246 and CurrentWidth <= 691:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 print "you are using 1246 nowwwwwwwwwwwww chris"

                 print "self.next_program"
                 print self.next_program

                 print "self.time_flag"
                 print self.time_flag

                 print "self.move_right_flag"
                 print self.move_right_flag



         elif CurrentRow == 1246 and CurrentWidth >= 1038:
             if self.channel_page >= 0 and self.channel_page < 15750:
                 CurrentProgram = int(CurrentId)
                 CurrentProgram_Width = self.getControl(CurrentProgram).getWidth()

                 if CurrentProgram_Width <= 691:
                     self.programs_Index_flag = True

                     if self.channelsOnMiddle == True:
                         self.channelsOnMiddle = False
                         self.channelsOnRight = True
                     else:
                         if self.channelsOnMiddle == True:
                             self.channelsOnMiddle = Fals
                             self.channelsOnLeft = True

                     if self.next_program == True:
                         self.next_program = False

                     if self.time_flag == False:
                         self.time_flag = True

                     #if self.move_right_flag == False:
                         #self.move_right_flag = True