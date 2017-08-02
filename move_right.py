import datetime
import time
import xbmc
import xbmcgui
import os
from sqlite3 import dbapi2 as database
#cont = 0

def EPG_time_2(self):
     program_finished = ''.join(str(x) for x in self.program_finished)
     program_id = ''.join(str(x) for x in self.program_id)
     print "you are calling EPG_time_2"
     print program_id
     nextprogram = int(program_id) + 1
     nextprogram1 = int(nextprogram) + 1
     nextprogram2 = int(nextprogram1) + 1
     nextprogram3 = int(nextprogram2) + 1
     nextprogram4 = int(nextprogram3) + 1
     nextprogram5 = int(nextprogram4) + 1
     nextprogram6 = int(nextprogram5) + 1
     nextprogram7 = int(nextprogram6) + 1
     nextprogram8 = int(nextprogram7) + 1
     program_button_1 = self.getControl(int(program_id))
     program_button_2 = self.getControl(int(nextprogram))
     program_button_3 = self.getControl(int(nextprogram1))
     program_button_4 = self.getControl(int(nextprogram2))
     program_button_5 = self.getControl(int(nextprogram3))
     program_button_6 = self.getControl(int(nextprogram4))
     program_button_7 = self.getControl(int(nextprogram5))
     program_button_8 = self.getControl(int(nextprogram6))
     program_button_9 = self.getControl(int(nextprogram7))
     program_button_10 = self.getControl(int(nextprogram8))
     programs_width = 344
     program_button_1.setWidth(int(programs_width))
     pos_Y = program_button_1.getY()


     if int(programs_width) == 344:
         program_button_2.setPosition(724, int(pos_Y))
         nextprogram_width = program_button_2.getWidth()
         print "344 program width size for nextprogram"
         print nextprogram_width

         if int(nextprogram_width) >= 40 and int(nextprogram_width) <= 60:
             nextprograms_width = 60
             program_button_2.setWidth(int(nextprograms_width))

             if int(nextprograms_width) == 60:
                 program_button_3.setPosition(790, int(pos_Y))
                 nextprogram1_width = program_button_3.getWidth()

                 if int(nextprogram1_width) >= 101 and int(nextprogram1_width) <= 117:
                     program_button_4.setPosition(897, int(pos_Y))



                 elif int(nextprogram1_width) >= 691:
                     program_button_4.setPosition(1419, int(pos_Y))




         elif int(nextprogram_width) >= 100 and nextprogram_width <= 123:
             nextprograms_width = 108
             program_button_2.setWidth(int(nextprograms_width))

             if int(nextprograms_width) == 108:
                 program_button_3.setPosition(838, int(pos_Y))
                 nextprogram1_width = program_button_3.getWidth()

                 if int(nextprogram1_width) == 117:
                     nextprograms1_width = 114
                     program_button_3.setWidth(int(nextprograms1_width))

                     if int(nextprograms1_width) == 114:
                         program_button_4.setPosition(959, int(pos_Y))
                         nextprogram2_width = program_button_4.getWidth()

                         if int(nextprogram2_width) == 117:
                             nextprograms2_width = 108
                             program_button_4.setWidth(int(nextprograms2_width))

                             if int(nextprograms2_width) == 108:
                                 program_button_5.setPosition(1072, int(pos_Y))
                                 nextprogram3_width = program_button_5.getWidth()

                                 if int(nextprogram3_width) == 59:
                                     nextprograms3_width = 60
                                     program_button_5.setWidth(int(nextprograms3_width))

                                     if int(nextprograms3_width) == 60:
                                         program_button_6.setPosition(1138, int(pos_Y))



                         elif int(nextprogram2_width) == 167:
                             nextprograms2_width = 162
                             program_button_4.setWidth(int(nextprograms2_width))

                             if int(nextprograms2_width) == 162:
                                 program_button_5.setPosition(1125, int(pos_Y))
                                 nextprogram3_width = program_button_5.getWidth()

                                 if int(nextprogram3_width) == 59:
                                     nextprograms3_width = 54
                                     program_button_5.setWidth(int(nextprograms3_width))

                                     if int(nextprograms3_width) == 54:
                                         program_button_6.setPosition(1184, int(pos_Y))




                 elif int(nextprogram1_width) == 167:
                     nextprograms1_width = 171
                     program_button_3.setWidth(int(nextprograms1_width))

                     if int(nextprograms1_width) == 171:
                         program_button_4.setPosition(1016, int(pos_Y))
                         nextprogram2_width = program_button_4.getWidth()

                         if int(nextprogram2_width) == 117:
                             nextprograms2_width = 116
                             program_button_4.setWidth(int(nextprograms2_width))

                             if int(nextprograms2_width) == 116:
                                 program_button_5.setPosition(1138, int(pos_Y))



                 elif int(nextprogram1_width) == 227:
                     nextprograms1_width = 229
                     program_button_3.setWidth(int(nextprograms1_width))

                     if int(nextprograms1_width) == 229:
                         program_button_4.setPosition(1072, int(pos_Y))




                 elif int(nextprogram1_width) == 342:
                     nextprograms1_width = 340
                     program_button_3.setWidth(int(nextprograms1_width))

                     if int(nextprograms1_width) == 340:
                         program_button_4.setPosition(1184, int(pos_Y))



                 elif int(nextprogram1_width) >= 456:
                     program_button_4.setPosition(1419, int(pos_Y))




         elif int(nextprogram_width) >= 160 and int(nextprogram_width) <= 173:
             nextprograms_width = 169
             program_button_2.setWidth(int(nextprograms_width))

             if int(nextprograms_width) == 169:
                 program_button_3.setPosition(897, int(pos_Y))
                 nextprogram1_width = program_button_3.getWidth()

                 if int(nextprogram1_width) == 59:
                     nextprograms1_width = 55
                     program_button_3.setWidth(int(nextprograms1_width))

                     if int(nextprograms1_width) == 55:
                         program_button_4.setPosition(959, int(pos_Y))


                 elif int(nextprogram1_width) == 117:
                     program_button_4.setPosition(1016, int(pos_Y))



                 elif int(nextprogram1_width) == 342:
                     nextprograms1_width = 344
                     program_button_3.setWidth(int(nextprograms1_width))

                     if int(nextprograms1_width) == 344:
                         program_button_4.setPosition(1246, int(pos_Y))



                 elif int(nextprogram1_width) > 342:
                     program_button_4.setPosition(1419, int(pos_Y))



         elif int(nextprogram_width) >= 221 and int(nextprogram_width) <= 231:
             nextprograms_width = 228
             program_button_2.setWidth(int(nextprograms_width))

             if int(nextprograms_width) == 228:
                 program_button_3.setPosition(959, int(pos_Y))
                 nextprogram1_width = program_button_3.getWidth()

                 if int(nextprogram1_width) == 117:
                     nextprograms1_width = 107
                     program_button_3.setWidth(int(nextprograms1_width))

                     if int(nextprograms1_width) == 107:
                         program_button_4.setPosition(1072, int(pos_Y))




         elif int(nextprogram_width) >= 270 and int(nextprogram_width) <= 286:
             nextprograms_width = 280
             program_button_2.setWidth(int(nextprograms_width))
             print "286 passed 1"

             if int(nextprograms_width) == 280:
                 program_button_3.setPosition(1009, int(pos_Y))
                 nextprogram1_width = program_button_3.getWidth()
                 print "286 passed 2"

                 if int(nextprogram1_width) == 59:
                     nextprograms1_width = 58
                     program_button_3.setWidth(int(nextprograms1_width))
                     print "286 passed 3"

                     if (nextprograms1_width) == 58:
                         program_button_4.setPosition(1072, int(pos_Y))
                         nextprogram2_width = program_button_4.getWidth()
                         print "nextprogram2_width is 59"

                         if (nextprogram2_width) == 59:
                             nextprograms2_width = 52
                             program_button_4.setWidth(int(nextprograms2_width))
                             print "59 passed"

                             if (nextprograms2_width) == 52:
                                 program_button_5.setPosition(1125, int(pos_Y))



                 elif int(nextprogram1_width) == 117:
                     nextprograms1_width = 122
                     program_button_3.setWidth(int(nextprograms1_width))

                     if (nextprograms1_width) == 122:
                         program_button_4.setPosition(1138, int(pos_Y))



                 elif int(nextprogram1_width) == 227:
                     nextprograms1_width = 231
                     program_button_3.setWidth(int(nextprograms1_width))

                     if (nextprograms1_width) == 231:
                         program_button_4.setPosition(1246, int(pos_Y))



                 elif int(nextprogram1_width) == 342:
                     program_button_4.setPosition(1419, int(pos_Y))




         elif int(nextprogram_width) >= 342 and int(nextprogram_width) <= 344:
             nextprograms_width = 342
             program_button_2.setWidth(int(nextprograms_width))

             if int(nextprograms_width) == 342:
                 program_button_3.setPosition(1072, int(pos_Y))
                 nextprogram1_width = program_button_3.getWidth()

                 if int(nextprogram1_width) == 59:
                     nextprograms1_width = 60
                     program_button_3.setWidth(int(nextprograms1_width))

                     if (nextprograms1_width) == 60:
                         program_button_4.setPosition(1138, int(pos_Y))


                 elif int(nextprogram1_width) == 117:
                     nextprograms1_width = 106
                     program_button_3.setWidth(int(nextprograms1_width))

                     if (nextprograms1_width) == 106:
                         program_button_4.setPosition(1184, int(pos_Y))


                 elif int(nextprogram1_width) == 167:
                     nextprograms1_width = 168
                     program_button_3.setWidth(int(nextprograms1_width))

                     if (nextprograms1_width) == 168:
                         program_button_4.setPosition(1246, int(pos_Y))



                 elif int(nextprogram1_width) >= 342:
                     program_button_5.setPosition(1419, int(pos_Y))
                     program_button_6.setPosition(1762, int(pos_Y))




         elif int(nextprogram_width) == 396:
             nextprograms_width = 409
             program_button_2.setWidth(int(nextprograms_width))

             if int(nextprograms_width) == 409:
                 program_button_3.setPosition(1138, int(pos_Y))
                 nextprogram1_width = program_button_3.getWidth()

                 if int(nextprogram1_width) >= 286:
                     program_button_4.setPosition(1419, int(pos_Y))



         elif int(nextprogram_width) == 456:
             nextprograms_width = 454
             program_button_2.setWidth(int(nextprograms_width))

             if int(nextprograms_width) == 454:
                 program_button_3.setPosition(1184, int(pos_Y))



         elif int(nextprogram_width) == 515:
             nextprograms_width = 517
             program_button_2.setWidth(int(nextprograms_width))

             if int(nextprograms_width) == 517:
                 program_button_3.setPosition(1246, int(pos_Y))
                 nextprogram1_width = program_button_3.getWidth()

                 if int(nextprogram1_width) >= 59:
                     program_button_4.setPosition(1419, int(pos_Y))



         elif int(nextprogram_width) >= 567:
             program_button_3.setPosition(1419, int(pos_Y))
             program_button_4.setPosition(1762, int(pos_Y))





def EPG_time_1_and_EPG_time_2(self):
     program_finished = ''.join(str(x) for x in self.program_finished)
     program_id = ''.join(str(x) for x in self.program_id)
     nextprogram = int(program_id) + 1
     nextprogram1 = int(nextprogram) + 1
     nextprogram2 = int(nextprogram1) + 1
     nextprogram3 = int(nextprogram2) + 1
     nextprogram4 = int(nextprogram3) + 1
     nextprogram5 = int(nextprogram4) + 1
     nextprogram6 = int(nextprogram5) + 1
     nextprogram7 = int(nextprogram6) + 1
     nextprogram8 = int(nextprogram7) + 1
     program_button_1 = self.getControl(int(program_id))
     program_button_2 = self.getControl(int(nextprogram))
     program_button_3 = self.getControl(int(nextprogram1))
     program_button_4 = self.getControl(int(nextprogram2))
     program_button_5 = self.getControl(int(nextprogram3))
     program_button_6 = self.getControl(int(nextprogram4))
     program_button_7 = self.getControl(int(nextprogram5))
     program_button_8 = self.getControl(int(nextprogram6))
     program_button_9 = self.getControl(int(nextprogram7))
     program_button_10 = self.getControl(int(nextprogram8))
     pos_Y = program_button_1.getY()
     print pos_Y
     print program_finished

     if program_finished == '05' or program_finished == '35':
         programs_width = 60
         program_button_1.setWidth(int(programs_width))

         if int(programs_width) == 60:
             program_button_2.setPosition(441, int(pos_Y))
             nextprogram_width = program_button_2.getWidth()

             if int(nextprogram_width) >= 40 and int(nextprogram_width) <= 59:
                 nextprograms_width = 59
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 59:
                     program_button_3.setPosition(507, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 41 and int(nextprogram1_width) <= 59:
                         nextprograms1_width = 45
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 45:
                             program_button_4.setPosition(559, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 112:
                                 nextprograms2_width = 102
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 102:
                                     program_button_5.setPosition(669, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 116:
                                         nextprograms3_width = 114
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 114:
                                             program_button_6.setPosition(790, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 117:
                                                 nextprograms4_width = 101
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 101:
                                                     program_button_7.setPosition(897, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 117:
                                                         nextprograms5_width = 112
                                                         program_button_7.setWidth(int(nextprograms5_width))

                                                         if int(nextprograms5_width) == 112:
                                                             program_button_8.setPosition(1016, int(pos_Y))
                                                             nextprogram6_width = program_button_8.getWidth()

                                                             if int(nextprogram6_width) == 167:
                                                                 nextprograms6_width = 162
                                                                 program_button_8.setWidth(int(nextprograms6_width))

                                                                 if int(nextprograms6_width) == 162:
                                                                     program_button_9.setPosition(1184, int(pos_Y))



                                     elif int(nextprogram3_width) == 162:
                                         nextprograms3_width = 162
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 162:
                                             program_button_6.setPosition(838, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) >= 100 and int(nextprogram4_width) <= 117:
                                                 nextprograms4_width = 104
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 104:
                                                     program_button_7.setPosition(949, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 117:
                                                         program_button_8.setPosition(1072, int(pos_Y))
                                                         nextprogram6_width = program_button_8.getWidth()

                                                         if int(nextprogram6_width) == 59:
                                                             nextprograms6_width = 59
                                                             program_button_8.setWidth(int(nextprograms6_width))

                                                             if int(nextprograms6_width) == 59:
                                                                 program_button_9.setPosition(1138, int(pos_Y))




                     elif int(nextprogram1_width) >= 110 and int(nextprogram1_width) <= 114:
                         nextprograms1_width = 96
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 96:
                             program_button_4.setPosition(610, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) >= 167 and int(nextprogram2_width) <= 174:
                                 nextprograms2_width = 173
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 173:
                                     program_button_5.setPosition(790, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 167:
                                         nextprograms3_width = 162
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 162:
                                             program_button_6.setPosition(959, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()
                                             print "nextprogram4_width"
                                             print nextprogram4_width

                                             if int(nextprogram4_width) == 167:
                                                 nextprograms4_width = 172
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 172:
                                                     program_button_7.setPosition(1138, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 167:
                                                         nextprograms5_width = 172
                                                         program_button_7.setWidth(int(nextprograms5_width))

                                                         if int(nextprograms5_width) == 172:
                                                             program_button_8.setPosition(1419, int(pos_Y))



                     elif int(nextprogram1_width) >= 150 and int(nextprogram1_width) <= 170:
                         nextprograms1_width = 155
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 155:
                             program_button_4.setPosition(669, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) >= 100 and int(nextprogram2_width) <= 117:
                                 nextprograms2_width = 114
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 114:
                                     program_button_5.setPosition(790, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 157:
                                         nextprograms3_width = 152
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 152:
                                             program_button_6.setPosition(949, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 117:
                                                 nextprograms4_width = 116
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 116:
                                                     program_button_7.setPosition(1072, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 167:
                                                         program_button_8.setPosition(1246, int(pos_Y))


                                                     elif int(nextprogram5_width) >= 227:
                                                         program_button_8.setPosition(1419, int(pos_Y))



                                             elif int(nextprogram4_width) == 167:
                                                 nextprograms4_width = 169
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 169:
                                                     program_button_7.setPosition(1125, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 167:
                                                         program_button_8.setPosition(1286, int(pos_Y))




                     elif int(nextprogram1_width) == 691:
                         nextprograms1_width = 671
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 671:
                             program_button_4.setPosition(1184, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 59:
                                 nextprograms2_width = 56
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 56:
                                     program_button_5.setPosition(1246, int(pos_Y))



                     elif int(nextprogram1_width) > 691:
                         program_button_4.setPosition(1419, int(pos_Y))




             elif int(nextprogram_width) >= 90 and int(nextprogram_width) <= 117:
                 nextprograms_width = 111
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 111:
                     program_button_3.setPosition(559, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 40 and int(nextprogram1_width) <= 59:
                         nextprograms1_width = 45
                         program_button_3.setWidth(nextprograms1_width)

                         if int(nextprograms1_width) == 45:
                             program_button_4.setPosition(610, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) >= 40 and int(nextprogram2_width) <= 59:
                                 nextprograms2_width = 53
                                 program_button_4.setWidth(nextprograms2_width)

                                 if int(nextprograms2_width) == 53:
                                     program_button_5.setPosition(669, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) >= 101 and int(nextprogram3_width) <= 123:
                                         nextprograms3_width = 115
                                         program_button_5.setWidth(nextprograms3_width)

                                         if int(nextprograms3_width) == 115:
                                             program_button_6.setPosition(790, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 117:
                                                 nextprograms4_width = 115
                                                 program_button_6.setWidth(nextprograms4_width)

                                                 if int(nextprograms4_width) == 115:
                                                     program_button_7.setPosition(910, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 167:
                                                         nextprograms5_width = 155
                                                         program_button_7.setWidth(nextprograms5_width)

                                                         if int(nextprograms5_width) == 155:
                                                             program_button_8.setPosition(1072, int(pos_Y))
                                                             nextprogram6_width = program_button_8.getWidth()

                                                             if int(nextprogram6_width) == 117:
                                                                 nextprograms6_width = 112
                                                                 program_button_8.setWidth(nextprograms6_width)

                                                                 if int(nextprograms6_width) == 112:
                                                                     program_button_9.setPosition(1189, int(pos_Y))
                                                                     nextprogram7_width = program_button_9.getWidth()

                                                                     if int(nextprogram7_width) == 59:
                                                                         nextprograms7_width = 52
                                                                         program_button_9.setWidth(nextprograms7_width)

                                                                         if int(nextprograms7_width) == 52:
                                                                             program_button_10.setPosition(1246, int(pos_Y))




                             elif int(nextprogram2_width) >= 100 and int(nextprogram2_width) <= 117:
                                 nextprograms2_width = 108
                                 program_button_4.setWidth(nextprograms2_width)

                                 if int(nextprograms2_width) == 108:
                                     program_button_5.setPosition(724, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 167:
                                         program_button_6.setPosition(897, int(pos_Y))
                                         nextprogram4_width = program_button_6.getWidth()

                                         if int(nextprogram4_width) >= 515:
                                             program_button_7.setPosition(1419, int(pos_Y))
                                             program_button_8.setPosition(1762, int(pos_Y))



                             elif int(nextprogram2_width) == 342:
                                 program_button_5.setPosition(1072, int(pos_Y))



                             elif int(nextprogram2_width) >= 515:
                                program_button_5.setPosition(1419, int(pos_Y))



                     elif int(nextprogram1_width) >= 100 and int(nextprogram1_width) <= 117:
                         nextprograms1_width = 104
                         program_button_3.setWidth(nextprograms1_width)

                         if int(nextprograms1_width) == 104:
                             program_button_4.setPosition(669, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 104:
                                 nextprograms2_width = 115
                                 program_button_4.setWidth(nextprograms2_width)

                                 if int(nextprograms2_width) == 115:
                                     program_button_5.setPosition(790, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 115:
                                         nextprograms3_width = 103
                                         program_button_5.setWidth(nextprograms3_width)

                                         if int(nextprograms3_width) == 103:
                                             program_button_6.setPosition(897, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 167:
                                                 nextprograms4_width = 169
                                                 program_button_6.setWidth(nextprograms4_width)

                                                 if int(nextprograms4_width) == 169:
                                                     program_button_7.setPosition(1072, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 167:
                                                         nextprograms5_width = 169
                                                         program_button_7.setWidth(nextprograms5_width)

                                                         if int(nextprograms5_width) == 169:
                                                             program_button_8.setPosition(1246, int(pos_Y))




                             elif int(nextprogram2_width) >= 691:
                                 program_button_5.setPosition(1419, int(pos_Y))



                         elif int(nextprogram1_width) == 159:
                             nextprograms1_width = 170
                             program_button_4.setWidth(int(nextprograms1_width))

                             if int(nextprograms1_width) == 170:
                                 program_button_4.setPosition(724, int(pos_Y))
                                 nextprogram2_width = program_button_4.getWidth()

                                 if int(nextprogram2_width) == 342:
                                     program_button_5.setPosition(1072, int(pos_Y))

                                     if int(nextprogram2_width) >= 515:
                                         program_button_5.setPosition(1419, int(pos_Y))



                         elif int(nextprogram1_width) == 342:
                             nextprograms1_width = 344
                             program_button_3.setWidth(int(nextprograms1_width))

                             if int(nextprograms1_width) == 344:
                                 program_button_4.setPosition(897, int(pos_Y))
                                 nextprogram2_width = program_button_4.getWidth()
                                 print "nextprogram2_width murder she wrote a"
                                 print nextprogram2_width

                                 if int(nextprogram2_width) >= 342 and int(nextprogram2_width) <= 344:
                                     nextprograms2_width = 342
                                     program_button_4.setWidth(int(nextprograms2_width))

                                     if int(nextprograms2_width) == 342:
                                         program_button_5.setPosition(1246, int(pos_Y))


                                 elif int(nextprogram2_width) >= 396:
                                     program_button_5.setPosition(1419, int(pos_Y))



                         elif int(nextprogram1_width) == 396:
                             nextprograms1_width = 393
                             program_button_3.setWidth(int(nextprograms1_width))

                             if int(nextprograms1_width) == 393:
                                 program_button_4.setPosition(949, int(pos_Y))
                                 nextprogram2_width = program_button_4.getWidth()
                                 print "nextprogram2_width murder she wrote b"
                                 print nextprogram2_width



                         elif int(nextprogram1_width) == 691:
                             program_button_4.setPosition(1246, int(pos_Y))




                     elif int(nextprogram1_width) >= 151 and int(nextprogram1_width) <= 175:
                         nextprograms1_width = 159
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 159:
                             program_button_4.setPosition(724, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 59:
                                 program_button_5.setPosition(790, int(pos_Y))
                                 nextprogram3_width = program_button_5.getWidth()

                                 if int(nextprogram3_width) == 164:
                                     nextprograms3_width = 161
                                     program_button_5.setWidth(int(nextprograms3_width))

                                     if int(nextprograms3_width) == 161:
                                         program_button_6.setPosition(959, int(pos_Y))
                                         nextprogram4_width = program_button_6.getWidth()

                                         if int(nextprogram4_width) == 167:
                                             nextprograms4_width = 162
                                             program_button_6.setWidth(int(nextprograms4_width))

                                             if int(nextprograms4_width) == 162:
                                                 program_button_7.setPosition(1125, int(pos_Y))
                                                 nextprogram5_width = program_button_7.getWidth()

                                                 if int(nextprogram5_width) == 227:
                                                     program_button_8.setPosition(1419, int(pos_Y))
                                                     program_button_9.setPosition(1620, int(pos_Y))
                                                     program_button_10.setPosition(1840, int(pos_Y))




                             elif int(nextprogram2_width) >= 101 and int(nextprogram2_width) <= 117:
                                 nextprograms2_width = 108
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 108:
                                     program_button_5.setPosition(838, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) >= 49 and int(nextprogram3_width) <= 60:
                                         nextprograms3_width = 54
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 54:
                                             program_button_6.setPosition(897, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) >= 49 and int(nextprogram4_width) <= 60:
                                                 nextprograms4_width = 55
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 55:
                                                     program_button_7.setPosition(959, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 227:
                                                         nextprograms5_width = 221
                                                         program_button_7.setWidth(int(nextprograms5_width))

                                                         if int(nextprograms5_width) == 221:
                                                             program_button_8.setPosition(1186, int(pos_Y))
                                                             nextprogram6_width = program_button_8.getWidth()

                                                             if int(nextprogram6_width) >= 342:
                                                                 program_button_9.setPosition(1419, int(pos_Y))
                                                                 program_button_10.setPosition(1762, int(pos_Y))





                             elif int(nextprogram2_width) >= 160 and int(nextprogram2_width) <= 173:
                                 nextprograms2_width = 168
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 168:
                                     program_button_5.setPosition(897, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 167:
                                         nextprograms3_width = 169
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 169:
                                             program_button_6.setPosition(1072, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) >= 286:
                                                 program_button_7.setPosition(1419, int(pos_Y))
                                                 program_button_8.setPosition(1762, int(pos_Y))




                                     elif int(nextprogram3_width) >= 567:
                                         program_button_6.setPosition(1419, int(pos_Y))
                                         program_button_7.setPosition(1762, int(pos_Y))
                                         program_button_8.setPosition(1943, int(pos_Y))
                                         print "you are under 567"




                     elif int(nextprogram1_width) >= 280 and int(nextprogram1_width) <= 286:
                         nextprograms1_width = 284
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 284:
                             program_button_4.setPosition(849, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 286:
                                 nextprograms2_width = 284
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 284:
                                     program_button_5.setPosition(1138, int(pos_Y))
                                     nextprogram3_width = program_button_6.getWidth()

                                     if int(nextprogram3_width) == 286:
                                         program_button_5.setPosition(1419, int(pos_Y))




                     elif int(nextprogram1_width) == 691:
                         nextprograms1_width = 682
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 682:
                             program_button_4.setPosition(1246, int(pos_Y))



                     elif int(nextprogram1_width) > 691:
                         program_button_4.setPosition(1419, int(pos_Y))




             elif int(nextprogram_width) >= 150 and int(nextprogram_width) <= 173:
                 nextprograms_width = 163
                 program_button_2.setWidth(int(nextprograms_width))
                 print "you are working on channel 4 button wedding town b"

                 if int(nextprograms_width) == 163:
                     program_button_3.setPosition(610, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()
                     print nextprogram1_width
                     print "heloooooooooooooooooooooooooooo"

                     if int(nextprogram1_width) >= 101 and int(nextprogram1_width) <= 117:
                         nextprograms1_width = 108
                         program_button_3.setWidth(int(nextprograms1_width))
                         print "programme is 108........................................."

                         if int(nextprograms1_width) == 108:
                             program_button_4.setPosition(724, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()
                             print "nextprogram2_width for 59 is........................."
                             print nextprogram2_width

                             if int(nextprogram2_width) >= 59 and int(nextprogram2_width) <= 60:
                                 nextprograms2_width = 60
                                 program_button_4.setWidth(int(nextprograms2_width))
                                 nextprogram3_width = program_button_5.getWidth()
                                 print "nextprogram3_width for itv........."
                                 print nextprogram3_width

                                 if int(nextprograms2_width) == 60:
                                     program_button_5.setPosition(790, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()
                                     print "nextprogram3_width for itv........."
                                     print nextprogram3_width

                                     if int(nextprogram3_width) >= 101 and int(nextprogram3_width) <= 117:
                                         nextprograms3_width = 115
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 115:
                                             program_button_6.setPosition(910, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 167:
                                                 nextprograms4_width = 156
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 156:
                                                     program_button_7.setPosition(1072, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 167:
                                                         nextprograms5_width = 168
                                                         program_button_7.setWidth(int(nextprograms5_width))

                                                         if int(nextprograms5_width) == 168:
                                                             program_button_8.setPosition(1246, int(pos_Y))



                                     elif int(nextprogram3_width) >= 160 and int(nextprogram3_width) <= 167:
                                         nextprograms3_width = 162
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 162:
                                             program_button_6.setPosition(959, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 167:
                                                 nextprograms4_width = 161
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 161:
                                                     program_button_7.setPosition(1125, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 167:
                                                         program_button_8.setPosition(1419, int(pos_Y))
                                                         program_button_9.setPosition(1762, int(pos_Y))
                                     
                                     



                             elif int(nextprogram2_width) == 167:
                                 program_button_5.setPosition(897, int(pos_Y))
                                 nextprogram3_width = program_button_5.getWidth()

                                 if int(nextprogram3_width) == 117:
                                     nextprograms3_width = 106
                                     program_button_5.setWidth(int(nextprograms3_width))

                                     if int(nextprograms3_width) == 106:
                                         program_button_6.setPosition(1009, int(pos_Y))
                                         nextprogram4_width = program_button_6.getWidth()

                                         if int(nextprogram4_width) == 117:
                                             nextprograms4_width = 110
                                             program_button_6.setWidth(int(nextprograms4_width))

                                             if int(nextprograms4_width) == 110:
                                                 program_button_7.setPosition(1125, int(pos_Y))
                                                 nextprogram5_width = program_button_7.getWidth()

                                                 if int(nextprogram5_width) == 117:
                                                     nextprograms5_width = 114
                                                     program_button_7.setWidth(int(nextprograms5_width))

                                                     if int(nextprograms5_width) == 114:
                                                         program_button_8.setPosition(1246, int(pos_Y))



                                         elif int(nextprogram4_width) == 167:
                                             nextprograms4_width = 169
                                             program_button_6.setWidth(int(nextprograms4_width))

                                             if int(nextprograms4_width) == 169:
                                                 program_button_7.setPosition(1184, int(pos_Y))
                                                 nextprogram5_width = program_button_7.getWidth()




                                         elif int(nextprogram4_width) >= 515:
                                             program_button_6.setPosition(1419, int(pos_Y))
                                             program_button_7.setPosition(1762, int(pos_Y))



                                 elif int(nextprogram3_width) >= 515:
                                     program_button_6.setPosition(1419, int(pos_Y))
                                     program_button_7.setPosition(1762, int(pos_Y))



                             elif int(nextprogram2_width) == 227:
                                 program_button_5.setPosition(959, int(pos_Y))
                                 nextprogram3_width = program_button_5.getWidth()

                                 if int(nextprogram3_width) == 117:
                                     nextprograms3_width = 107
                                     program_button_5.setWidth(nextprograms3_width)

                                     if int(nextprograms3_width) == 107:
                                         program_button_6.setPosition(1072, int(pos_Y))
                                         nextprogram4_width = program_button_6.getWidth()

                                         if int(nextprogram4_width) == 167:
                                             program_button_7.setPosition(1246, int(pos_Y))




                     elif int(nextprogram1_width) >= 160 and int(nextprogram1_width) <= 172:
                         nextprograms1_width = 174
                         program_button_3.setWidth(nextprograms1_width)
                         print "you are in 160 for channel 5"

                         if int(nextprograms1_width) == 174:
                             program_button_4.setPosition(790, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) >= 101 and int(nextprogram2_width) <= 117:
                                 nextprograms2_width = 115
                                 program_button_4.setWidth(nextprograms2_width)

                                 if int(nextprograms2_width) == 115:
                                     program_button_5.setPosition(910, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 117:
                                         nextprograms3_width = 102
                                         program_button_5.setWidth(nextprograms3_width)

                                         if int(nextprograms3_width) == 102:
                                             program_button_6.setPosition(1016, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 117:
                                                 nextprograms4_width = 104
                                                 program_button_6.setWidth(nextprograms4_width)

                                                 if int(nextprograms4_width) == 104:
                                                     program_button_7.setPosition(1125, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 117:
                                                         nextprograms5_width = 115
                                                         program_button_7.setWidth(nextprograms5_width)

                                                         if int(nextprograms5_width) == 115:
                                                             program_button_8.setPosition(1246, int(pos_Y))




                             elif int(nextprogram2_width) >= 160 and int(nextprogram2_width) <= 172:
                                 nextprograms2_width = 162
                                 program_button_4.setWidth(nextprograms2_width)

                                 if int(nextprograms2_width) == 162:
                                     program_button_5.setPosition(959, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 117:
                                         nextprograms3_width = 107
                                         program_button_5.setWidth(nextprograms3_width)

                                         if int(nextprograms3_width) == 107:
                                             program_button_6.setPosition(1072, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 167:
                                                 program_button_7.setPosition(1246, int(pos_Y))
                                                 nextprogram5_width = program_button_7.getWidth()




                                     elif int(nextprogram3_width) == 167:
                                         nextprograms3_width = 161
                                         program_button_5.setWidth(nextprograms3_width)

                                         if int(nextprograms3_width) == 161:
                                             program_button_6.setPosition(1125, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 117:
                                                 nextprograms4_width = 115
                                                 program_button_6.setWidth(nextprograms4_width)

                                                 if int(nextprograms4_width) == 115:
                                                     program_button_7.setPosition(1246, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 117:
                                                         program_button_8.setPosition(1419, int(pos_Y))



                             elif int(nextprogram2_width) >= 160 and int(nextprogram2_width) <= 167:
                                 nextprograms2_width = 164
                                 program_button_4.setWidth(nextprograms2_width)

                                 if int(nextprograms2_width) == 164:
                                     program_button_5.setPosition(959, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 117:
                                         nextprograms3_width = 114
                                         program_button_5.setWidth(nextprograms3_width)

                                         if int(nextprograms3_width) == 114:
                                             program_button_6.setPosition(1138, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 117:
                                                 program_button_7.setPosition(1246, int(pos_Y))
                             
                             
                             
                             
                             
                             
                             
                             
                             elif int(nextprogram2_width) >= 220 and int(nextprogram2_width) <= 227:
                                 nextprograms2_width = 224
                                 program_button_4.setWidth(nextprograms2_width)

                                 if int(nextprograms2_width) == 224:
                                     program_button_5.setPosition(1019, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 117:
                                         nextprograms3_width = 114
                                         program_button_5.setWidth(nextprograms3_width)

                                         if int(nextprograms3_width) == 114:
                                             program_button_6.setPosition(1138, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 227:
                                                 program_button_7.setPosition(1419, int(pos_Y))




                     elif int(nextprogram1_width) >= 221 and int(nextprogram1_width) <= 231:
                         nextprograms1_width = 227
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 227:
                             program_button_4.setPosition(838, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 227:
                                 nextprograms2_width = 224
                                 program_button_5.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 224:
                                     program_button_6.setPosition(1072, int(pos_Y))
                                     program_button_7.setPosition(1138, int(pos_Y))
                                     program_button_8.setPosition(1246, int(pos_Y))
                                     program_button_9.setPosition(1419, int(pos_Y))




                     elif int(nextprogram1_width) == 626:
                         nextprograms1_width = 630
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 630:
                             program_button_4.setPosition(1246, int(pos_Y))



                     elif int(nextprogram1_width) >= 691:
                         program_button_4.setPosition(1419, int(pos_Y))




             elif int(nextprogram_width) >= 219 and int(nextprogram_width) <= 227:
                 nextprograms_width = 221
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 221:
                     program_button_3.setPosition(669, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 114:
                         nextprograms1_width = 113
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 113:
                             program_button_4.setPosition(790, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 117:
                                 nextprograms2_width = 102
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 102:
                                     program_button_5.setPosition(897, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 167:
                                         nextprograms3_width = 169
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 169:
                                             program_button_6.setPosition(1072, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 167:
                                                 nextprograms4_width = 168
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 168:
                                                     program_button_7.setPosition(1246, int(pos_Y))






                             elif int(nextprogram2_width) == 227:
                                 nextprograms2_width = 224
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 224:
                                     program_button_5.setPosition(1019, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 117:
                                         nextprograms3_width = 114
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 114:
                                             program_button_6.setPosition(1138, int(pos_Y))



                     elif int(nextprogram1_width) == 342:
                         nextprograms1_width = 340
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 340:
                             program_button_4.setPosition(1016, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 59:
                                 nextprograms2_width = 49
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 49:
                                     program_button_5.setPosition(1072, int(pos_Y))



             elif int(nextprogram_width) >= 260 and int(nextprogram_width) <= 293:
                 nextprograms_width = 277
                 program_button_2.setWidth(int(nextprograms_width))
                 print "you are working on channel 4 button wedding town a"

                 if int(nextprograms_width) == 277:
                     program_button_3.setPosition(724, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 40 and int(nextprogram1_width) <= 59:
                         program_button_4.setPosition(790, int(pos_Y))
                         nextprogram2_width = program_button_4.getWidth()

                         if int(nextprogram2_width) == 41:
                             nextprograms2_width = 41
                             program_button_4.setWidth(int(nextprograms2_width))

                             if int(nextprograms2_width) == 41:
                                 program_button_5.setPosition(838, int(pos_Y))
                                 nextprogram3_width = program_button_5.getWidth()

                                 if int(nextprogram3_width) >= 50 and int(nextprogram3_width) <= 59:
                                     nextprograms3_width = 53
                                     program_button_5.setWidth(int(nextprograms3_width))

                                     if int(nextprograms3_width) == 53:
                                         program_button_6.setPosition(897, int(pos_Y))
                                         nextprogram4_width = program_button_6.getWidth()

                                         if int(nextprogram4_width) == 117:
                                             nextprograms4_width = 112
                                             program_button_6.setWidth(int(nextprograms4_width))

                                             if int(nextprograms4_width) == 112:
                                                 program_button_7.setPosition(1016, int(pos_Y))
                                                 nextprogram5_width = program_button_7.getWidth()

                                                 if int(nextprogram5_width) == 117:
                                                     nextprograms5_width = 116
                                                     program_button_7.setWidth(int(nextprograms5_width))

                                                     if int(nextprograms5_width) == 116:
                                                         program_button_8.setPosition(1138, int(pos_Y))



                                                 elif int(nextprogram5_width) == 167:
                                                     nextprograms5_width = 162
                                                     program_button_7.setWidth(int(nextprograms5_width))

                                                     if int(nextprograms5_width) == 162:
                                                         program_button_8.setPosition(1184, int(pos_Y))



                     elif int(nextprogram1_width) >= 107 and int(nextprogram1_width) <= 114:
                         nextprograms1_width = 108
                         program_button_3.setWidth(int(nextprograms1_width))
                         print "you are working on channel 4 button wedding town a"

                         if int(nextprograms1_width) == 108:
                             program_button_4.setPosition(838, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 59:
                                 nextprograms2_width = 55
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 55:
                                     program_button_5.setPosition(897, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 59:
                                         nextprograms3_width = 56
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 56:
                                             program_button_6.setPosition(959, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 59:
                                                 nextprograms4_width = 54
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 54:
                                                     program_button_7.setPosition(1018, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()
                                                     print "you are in the 1018"

                                                     if int(nextprogram5_width) >= 101 and int(nextprogram5_width) <= 117:
                                                         nextprograms5_width = 115
                                                         program_button_7.setWidth(int(nextprograms5_width))

                                                         if int(nextprograms5_width) == 115:
                                                             program_button_8.setPosition(1138, int(pos_Y))
                                                             nextprogram6_width = program_button_8.getWidth()

                                                             if int(nextprogram6_width) == 117:
                                                                 nextprograms6_width = 102
                                                                 program_button_8.setWidth(int(nextprograms6_width))

                                                                 if int(nextprograms6_width) == 102:
                                                                     program_button_9.setPosition(1246, int(pos_Y))




                             elif int(nextprogram2_width) == 117:
                                 nextprograms2_width = 114
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 114:
                                     program_button_5.setPosition(959, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()
                                     print "after 114 size for nextprogram3 is......."
                                     print nextprogram3_width

                                     if int(nextprogram3_width) == 117:
                                         nextprograms3_width = 107
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 107:
                                             program_button_6.setPosition(1072, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()
                                             print "nextprogram4_width"
                                             print nextprogram4_width

                                             if int(nextprogram4_width) == 59:
                                                 program_button_7.setPosition(1138, int(pos_Y))
                                                 nextprogram5_width = program_button_7.getWidth()

                                                 if int(nextprogram5_width) == 59:
                                                     nextprograms5_width = 40
                                                     program_button_7.setWidth(int(nextprograms5_width))

                                                     if int(nextprograms5_width) == 40:
                                                         program_button_8.setPosition(1184, int(pos_Y))



                             elif int(nextprogram2_width) == 167:
                                 nextprograms2_width = 166
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 166:
                                     program_button_5.setPosition(1009, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 59:
                                         program_button_6.setPosition(1072, int(pos_Y))
                                         nextprogram4_width = program_button_6.getWidth()

                                         if int(nextprogram4_width) == 59:
                                              program_button_7.setPosition(1138, int(pos_Y))



                     elif int(nextprogram1_width) == 167:
                         nextprograms1_width = 167
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprogram1_width) == 167:
                             program_button_4.setPosition(897, int(pos_Y))




                     elif int(nextprogram1_width) >= 278 and int(nextprogram1_width) <= 293:
                         nextprograms1_width = 280
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 280:
                             program_button_4.setPosition(1009, int(pos_Y))



                     elif int(nextprogram1_width) >= 330 and int(nextprogram1_width) <= 344:
                         nextprograms1_width = 342
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 342:
                             program_button_4.setPosition(1072, int(pos_Y))



                     elif int(nextprogram1_width) == 396:
                         nextprograms1_width = 408
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 408:
                             program_button_4.setPosition(1138, int(pos_Y))



                     elif int(nextprogram1_width) == 456:
                         program_button_4.setPosition(1246, int(pos_Y))



                     elif int(nextprogram1_width) == 515:
                         nextprograms1_width = 515
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 515:
                             program_button_4.setPosition(1246, int(pos_Y))





             elif int(nextprogram_width) >= 330 and int(nextprogram_width) <= 396:
                 nextprograms_width = 343
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 343:
                     program_button_3.setPosition(790, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()
                     print "you are in 342 for channel 4"

                     if int(nextprogram1_width) == 167:
                         nextprograms1_width = 162
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 162:
                             program_button_4.setPosition(959, int(pos_Y))



                     elif int(nextprogram1_width) == 286:
                         nextprograms1_width = 276
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 276:
                             program_button_4.setPosition(1072, int(pos_Y))



                     elif int(nextprogram1_width) == 342:
                         nextprograms1_width = 342
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 342:
                             program_button_4.setPosition(1138, int(pos_Y))



                     elif int(nextprogram1_width) == 396:
                         nextprograms1_width = 388
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 388:
                             program_button_4.setPosition(1184, int(pos_Y))



                     elif int(nextprogram1_width) >= 515:
                         program_button_4.setPosition(1419, int(pos_Y))




             elif int(nextprogram_width) >= 451 and int(nextprogram_width) <= 456:
                 nextprograms_width = 451
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 451:
                     program_button_3.setPosition(897, int(pos_Y))



             elif int(nextprogram_width) >= 515 and int(nextprogram_width) <= 520:
                 nextprograms_width = 512
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 512:
                     program_button_3.setPosition(959, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 286:
                         nextprograms1_width = 276
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 276:
                             program_button_4.setPosition(1238, int(pos_Y))



             elif int(nextprogram_width) == 567:
                 nextprograms_width = 562
                 program_button_2.setWidth(nextprograms_width)

                 if int(nextprograms_width) == 562:
                     program_button_3.setPosition(1009, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 59:
                         nextprogram1s_width = 57
                         program_button_3.setWidth(int(nextprogram1s_width))

                         if int(nextprogram1s_width) == 57:
                             program_button_4.setPosition(1072, int(pos_Y))




             elif int(nextprogram_width) == 626:
                 nextprograms_width = 625
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 625:
                     program_button_3.setPosition(1072, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 59:
                         nextprograms1_width = 60
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 60:
                             program_button_4.setPosition(1138, int(pos_Y))



             elif int(nextprogram_width) == 691:
                 program_button_3.setPosition(1138, int(pos_Y))
                 nextprogram1_width = program_button_3.getWidth()

                 if int(nextprogram1_width) == 59:
                     nextprograms1_width = 41
                     program_button_3.setWidth(int(nextprograms1_width))

                     if int(nextprograms1_width) == 41:
                         program_button_4.setPosition(1184, int(pos_Y))



             elif int(nextprogram_width) == 741:
                 nextprograms_width = 737
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 737:
                     program_button_3.setPosition(1184, int(pos_Y))



             elif int(nextprogram_width) > 741:
                 program_button_3.setPosition(1419, int(pos_Y))




     elif program_finished == '10' or program_finished == '40':
         programs_width = 126
         program_button_1.setWidth(int(programs_width))

         if int(programs_width) == 126:
             program_button_2.setPosition(507, int(pos_Y))
             nextprogram_width = program_button_2.getWidth()

             if int(nextprogram_width) >= 40 and int(nextprogram_width) <= 59:
                 nextprograms_width = 45
                 program_button_2.setWidth(nextprograms_width)

                 if int(nextprograms_width) == 45:
                     program_button_3.setPosition(559, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 50 and int(nextprogram1_width) <= 59:
                         nextprograms1_width = 45
                         program_button_3.setWidth(nextprograms1_width)

                         if int(nextprograms1_width) == 45:
                             program_button_4.setPosition(610, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 54:
                                 nextprograms2_width = 52
                                 program_button_4.setWidth(nextprograms2_width)

                                 if int(nextprograms2_width) == 52:
                                     program_button_5.setPosition(669, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) >= 101 and int(nextprogram3_width) <= 117:
                                         nextprograms3_width = 115
                                         program_button_5.setWidth(nextprograms3_width)

                                         if int(nextprograms3_width) == 115:
                                             program_button_6.setPosition(790, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) >= 101 and int(nextprogram4_width) <= 117:
                                                 nextprograms4_width = 103
                                                 program_button_6.setWidth(nextprograms4_width)

                                                 if int(nextprograms4_width) == 103:
                                                     program_button_7.setPosition(897, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 167:
                                                         nextprograms5_width = 169
                                                         program_button_7.setWidth(nextprograms5_width)

                                                         if int(nextprograms5_width) == 169:
                                                             program_button_8.setPosition(1072, int(pos_Y))
                                                             nextprogram6_width = program_button_8.getWidth()

                                                             if int(nextprogram6_width) == 59:
                                                                 program_button_9.setPosition(1138, int(pos_Y))
                                                                 nextprogram7_width = program_button_9.getWidth()

                                                                 if int(nextprogram7_width) == 167:
                                                                     nextprograms7_width = 164
                                                                     program_button_9.setWidth(nextprograms7_width)

                                                                     if int(nextprograms7_width) == 164:
                                                                         program_button_10.setPosition(1419, int(pos_Y))



                             elif int(nextprogram2_width) == 221:
                                 nextprograms2_width = 222
                                 program_button_4.setWidth(nextprograms2_width)

                                 if int(nextprograms2_width) == 222:
                                     program_button_5.setPosition(838, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 342:
                                         nextprograms3_width = 341
                                         program_button_5.setWidth(nextprograms3_width)

                                         if int(nextprograms3_width) == 341:
                                             program_button_6.setPosition(1184, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 167:
                                                 program_button_7.setPosition(1419, int(pos_Y))
                                                 program_button_8.setPosition(1762, int(pos_Y))




                     elif int(nextprogram1_width) == 167:
                         nextprograms1_width = 153
                         program_button_3.setWidth(nextprograms1_width)

                         if int(nextprograms1_width) == 153:
                             program_button_4.setPosition(724, int(pos_Y))



                     elif int(nextprogram1_width) == 342:
                         nextprograms1_width = 334
                         program_button_3.setWidth(nextprograms1_width)

                         if nextprograms1_width == 334:
                             program_button_4.setPosition(897, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 396:
                                 nextprograms2_width = 56
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 56:
                                     program_button_5.setPosition(959, int(pos_Y))




                     elif int(nextprogram1_width) == 626:
                         nextprograms1_width = 620
                         program_button_3.setWidth(nextprograms1_width)

                         if nextprograms1_width == 620:
                             program_button_4.setPosition(1184, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 59:
                                 nextprograms2_width = 56
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 56:
                                     program_button_5.setPosition(1246, int(pos_Y))




                     elif int(nextprogram1_width) == 691:
                         nextprograms1_width = 681
                         program_button_3.setWidth(nextprograms1_width)

                         if nextprograms1_width == 681:
                             program_button_4.setPosition(1246, int(pos_Y))



                     elif int(nextprogram1_width) >= 691:
                         program_button_4.setPosition(1419, int(pos_Y))




             elif int(nextprogram_width) >= 100 and int(nextprogram_width) <= 117:
                 nextprograms_width = 97
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 97:
                     program_button_3.setPosition(610, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 49 and int(nextprogram1_width) <= 60:
                         nextprograms1_width = 53
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 53:
                             program_button_4.setPosition(669, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 117:
                                 nextprograms2_width = 115
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 115:
                                     program_button_5.setPosition(790, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 167:
                                         nextprograms3_width = 154
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 154:
                                             program_button_6.setPosition(949, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 117:
                                                 program_button_7.setPosition(1072, int(pos_Y))
                                                 nextprogram5_width = program_button_7.getWidth()

                                                 if int(nextprogram5_width) == 59:
                                                     nextprograms5_width = 60
                                                     program_button_7.setWidth(int(nextprograms5_width))

                                                     if int(nextprogram5_width) == 59:
                                                         program_button_8.setPosition(1138, int(pos_Y))




                     elif int(nextprogram1_width) >= 106 and int(nextprogram1_width) <= 117:
                         nextprograms1_width = 108
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 108:
                             program_button_4.setPosition(724, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) >= 50 and int(nextprogram2_width) <= 60:
                                 nextprograms2_width = 60
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 60:
                                     program_button_5.setPosition(790, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 40:
                                         nextprograms3_width = 42
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 42:
                                             program_button_6.setPosition(838, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 117:
                                                 nextprograms4_width = 114
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 114:
                                                     program_button_7.setPosition(959, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 167:
                                                         nextprograms5_width = 172
                                                         program_button_7.setWidth(int(nextprograms5_width))

                                                         if int(nextprograms5_width) == 172:
                                                             program_button_8.setPosition(1138, int(pos_Y))



                                             elif int(nextprogram4_width) == 167:
                                                 nextprograms4_width = 165
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 165:
                                                     program_button_7.setPosition(1009, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 117:
                                                         nextprograms5_width = 110
                                                         program_button_7.setWidth(int(nextprograms5_width))

                                                         if int(nextprograms5_width) == 110:
                                                             program_button_8.setPosition(1125, int(pos_Y))
                                                             nextprogram6_width = program_button_8.getWidth()

                                                             if int(nextprogram6_width) == 167:
                                                                 nextprograms6_width = 157
                                                                 program_button_8.setWidth(int(nextprograms6_width))

                                                                 if int(nextprograms6_width) == 157:
                                                                     program_button_9.setPosition(1419, int(pos_Y))



                                     elif int(nextprogram3_width) == 167:
                                         nextprograms3_width = 163
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 163:
                                             program_button_6.setPosition(959, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 117:
                                                 nextprograms4_width = 107
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 107:
                                                     program_button_7.setPosition(1072, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 59:
                                                         nextprograms5_width = 60
                                                         program_button_7.setWidth(int(nextprograms5_width))

                                                         if int(nextprograms5_width) == 60:
                                                             program_button_8.setPosition(1138, int(pos_Y))





                             elif int(nextprogram2_width) == 106:
                                 nextprograms2_width = 108
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 108:
                                     program_button_5.setPosition(838, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 57:
                                         nextprograms3_width = 55
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 55:
                                             program_button_6.setPosition(897, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 59:
                                                 nextprograms4_width = 55
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 55:
                                                     program_button_7.setPosition(959, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 59:
                                                         nextprograms5_width = 54
                                                         program_button_7.setWidth(int(nextprograms5_width))

                                                         if int(nextprograms5_width) == 54:
                                                             program_button_8.setPosition(1019, int(pos_Y))
                                                             nextprogram6_width = program_button_8.getWidth()

                                                             if int(nextprogram6_width) == 117:
                                                                 nextprograms6_width = 113
                                                                 program_button_8.setWidth(int(nextprograms6_width))

                                                                 if int(nextprograms6_width) == 113:
                                                                     program_button_9.setPosition(1138, int(pos_Y))
                                                                     nextprogram7_width = program_button_9.getWidth()

                                                                     if int(nextprogram7_width) == 117:
                                                                         nextprograms7_width = 101
                                                                         program_button_9.setWidth(int(nextprograms7_width))

                                                                         if int(nextprograms7_width) == 101:
                                                                             program_button_10.setPosition(1246, int(pos_Y))





                                     elif int(nextprogram3_width) == 117:
                                         nextprograms3_width = 104
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 104:
                                             program_button_6.setPosition(949, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 117:
                                                 nextprograms4_width = 117
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 117:
                                                     program_button_7.setPosition(1072, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 59:
                                                         nextprograms5_width = 60
                                                         program_button_7.setWidth(int(nextprograms5_width))

                                                         if int(nextprograms5_width) == 60:
                                                             program_button_8.setPosition(1138, int(pos_Y))
                                                             nextprogram6_width = program_button_8.getWidth()

                                                             if int(nextprogram6_width) == 59:
                                                                 nextprograms6_width = 40
                                                                 program_button_8.setWidth(int(nextprograms6_width))

                                                                 if int(nextprograms6_width) == 40:
                                                                     program_button_9.setPosition(1184, int(pos_Y))




             elif int(nextprogram_width) >= 160 and int(nextprogram_width) <= 172:
                 nextprograms_width = 156
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 156:
                     program_button_3.setPosition(669, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 49 and int(nextprogram1_width) <= 59:
                         nextprograms1_width = 50
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 50:
                             program_button_4.setPosition(724, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 59:
                                 nextprograms2_width = 60
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 60:
                                     program_button_5.setPosition(790, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 117:
                                         nextprograms3_width = 115
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 115:
                                             program_button_6.setPosition(910, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 59:
                                                 nextprograms4_width = 43
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 43:
                                                     program_button_7.setPosition(959, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 59:
                                                         nextprograms5_width = 46
                                                         program_button_7.setWidth(int(nextprograms5_width))

                                                         if int(nextprograms5_width) == 46:
                                                             program_button_8.setPosition(1009, int(pos_Y))
                                                             nextprogram6_width = program_button_8.getWidth()

                                                             if int(nextprogram6_width) == 117:
                                                                 nextprograms6_width = 123
                                                                 program_button_8.setWidth(int(nextprograms6_width))

                                                                 if int(nextprograms6_width) == 123:
                                                                     program_button_9.setPosition(1138, int(pos_Y))



                             elif int(nextprogram2_width) == 227:
                                 nextprograms2_width = 220
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 220:
                                     program_button_5.setPosition(949, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprograms2_width) >= 515:
                                         program_button_6.setPosition(1419, int(pos_Y))




                     elif int(nextprogram1_width) >= 100 and int(nextprogram1_width) <= 123:
                         nextprograms1_width = 115
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 115:
                             program_button_4.setPosition(790, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) >= 40 and int(nextprogram2_width) <= 60:
                                 nextprograms2_width = 48
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 48:
                                     program_button_5.setPosition(842, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) >= 49 and int(nextprogram3_width) <= 60:
                                         nextprograms3_width = 50
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 50:
                                             program_button_6.setPosition(897, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 117:
                                                 nextprograms4_width = 107
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 107:
                                                     program_button_7.setPosition(1009, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 167:
                                                         nextprograms5_width = 169
                                                         program_button_7.setWidth(int(nextprograms5_width))

                                                         if int(nextprograms5_width) == 169:
                                                             program_button_8.setPosition(1184, int(pos_Y))



                             
                             elif int(nextprogram2_width) >= 100 and int(nextprogram2_width) <= 117:
                                 nextprograms2_width = 101
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 101:
                                     program_button_5.setPosition(897, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 117:
                                         nextprograms3_width = 112
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 112:
                                             program_button_6.setPosition(1016, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 59:
                                                 nextprograms4_width = 50
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 50:
                                                     program_button_7.setPosition(1072, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 167:
                                                         nextprograms5_width = 159
                                                         program_button_7.setWidth(int(nextprograms5_width))

                                                         if int(nextprograms5_width) == 159:
                                                             program_button_8.setPosition(1238, int(pos_Y))



             elif int(nextprogram_width) >= 220 and int(nextprogram_width) <= 232:
                 nextprograms_width = 211
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 211:
                     program_button_3.setPosition(724, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 286:
                         nextprograms1_width = 281
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 281:
                             program_button_4.setPosition(1009, int(pos_Y))



                     elif int(nextprogram1_width) >= 691:
                         program_button_4.setPosition(1419, int(pos_Y))






             elif int(nextprogram_width) >= 270 and int(nextprogram_width) <= 295:
                 nextprograms_width = 277
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 277:
                     program_button_3.setPosition(790, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 286:
                         nextprograms1_width = 276
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 276:
                             program_button_4.setPosition(1072, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 59:
                                 program_button_5.setPosition(1138, int(pos_Y))
                                 nextprogram3_width = program_button_5.getWidth()

                                 if int(nextprogram3_width) == 59:
                                     nextprograms3_width = 41
                                     program_button_5.setWidth(int(nextprograms3_width))

                                     if int(nextprograms3_width) == 41:
                                         program_button_6.setPosition(1184, int(pos_Y))
                                         nextprogram4_width = program_button_6.getWidth()

                                         if int(nextprogram4_width) == 59:
                                             nextprograms4_width = 55
                                             program_button_6.setWidth(int(nextprograms4_width))

                                             if int(nextprograms4_width) == 55:
                                                 program_button_7.setPosition(1246, int(pos_Y))



                             elif int(nextprogram2_width) == 117:
                                 nextprograms2_width = 107
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 107:
                                     program_button_5.setPosition(1184, int(pos_Y))




                     elif int(nextprogram1_width) == 456:
                         nextprograms1_width = 454
                         program_button_2.setWidth(nextprograms1_width)

                         if int(nextprograms1_width) == 454:
                             program_button_3.setPosition(1246, int(pos_Y))



                     elif int(nextprogram1_width) >= 515:
                         program_button_4.setPosition(1419, int(pos_Y))




             elif int(nextprogram_width) >= 330 and int(nextprogram_width) <= 344:
                 nextprograms_width = 325
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 325:
                     program_button_3.setPosition(838, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()
                     print "nextprogram1_width for channel 4........................"
                     print nextprogram1_width

                     if int(nextprogram1_width) == 167:
                         nextprogram1s_width = 164
                         program_button_3.setWidth(int(nextprogram1s_width))

                         if int(nextprogram1s_width) == 164:
                             program_button_4.setPosition(1009, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 59:
                                 nextprograms2_width = 57
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 57:
                                     program_button_5.setPosition(1072, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 227:
                                         program_button_6.setPosition(1290, int(pos_Y))



                     elif int(nextprogram1_width) == 286:
                         nextprogram1s_width = 295
                         program_button_3.setWidth(int(nextprogram1s_width))

                         if int(nextprogram1s_width) == 295:
                             program_button_4.setPosition(1138, int(pos_Y))



                     elif int(nextprogram1_width) == 342:
                         nextprogram1s_width = 342
                         program_button_3.setWidth(int(nextprogram1s_width))

                         if int(nextprogram1s_width) == 342:
                             program_button_4.setPosition(1184, int(pos_Y))



                     elif int(nextprogram1_width) >= 515:
                         program_button_4.setPosition(1419, int(pos_Y))



             elif int(nextprogram_width) >= 390 and int(nextprogram_width) <= 396:
                 nextprograms_width = 392
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 392:
                     program_button_3.setPosition(897, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()




             elif int(nextprogram_width) == 456:
                 nextprograms_width = 445
                 program_button_2.setWidth(nextprograms_width)

                 if int(nextprograms_width) == 445:
                     program_button_3.setPosition(959, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 167:
                         nextprograms1_width = 172
                         program_button_3.setWidth(nextprograms1_width)

                         if int(nextprograms1_width) == 172:
                             program_button_4.setPosition(1138, int(pos_Y))

                             if int(nextprogram2_width) == 117:
                                 program_button_5.setPosition(1246, int(pos_Y))



                     elif int(nextprogram1_width) == 286:
                         nextprograms1_width = 282
                         program_button_3.setWidth(nextprograms1_width)

                         if int(nextprograms1_width) == 282:
                             program_button_4.setPosition(1246, int(pos_Y))




             elif int(nextprogram_width) == 515:
                 nextprograms_width = 502
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 502:
                     program_button_3.setPosition(1016, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 59:
                         program_button_4.setPosition(1072, int(pos_Y))



             elif int(nextprogram_width) == 567:
                 nextprograms_width = 559
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 559:
                     program_button_3.setPosition(1072, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 342:
                         program_button_4.setPosition(1419, int(pos_Y))




             elif int(nextprogram_width) >= 620 and int(nextprogram_width) <= 640:
                 nextprograms_width = 625
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 625:
                     program_button_3.setPosition(1138, int(pos_Y))



             elif int(nextprogram_width) == 691:
                 nextprograms_width = 671
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 671:
                     program_button_3.setPosition(1184, int(pos_Y))
                     program_button_4.setPosition(1419, int(pos_Y))





             elif int(nextprogram_width) == 741:
                 nextprograms_width = 733
                 program_button_2.setWidth(nextprograms_width)

                 if int(nextprograms_width) == 733:
                     program_button_3.setPosition(1246, int(pos_Y))




             elif int(nextprogram_width) > 741:
                 program_button_3.setPosition(1419, int(pos_Y))
                 program_button_4.setPosition(1762, int(pos_Y))




     elif program_finished == '15' or program_finished == '45':
         programs_width = 177
         program_button_1.setWidth(int(programs_width))

         if int(programs_width) == 177:
             program_button_2.setPosition(559, int(pos_Y))
             nextprogram_width = program_button_2.getWidth()

             if int(nextprogram_width) >= 40 and int(nextprogram_width) <= 59:
                 nextprograms_width = 46
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 46:
                     program_button_3.setPosition(610, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 456:
                         program_button_4.setPosition(1072, int(pos_Y))



                     elif int(nextprogram1_width) >= 691:
                         program_button_4.setPosition(1419, int(pos_Y))
                         program_button_5.setPosition(1624, int(pos_Y))
                         print "you are in the 691 now chris.........................."





             elif int(nextprogram_width) >= 90 and int(nextprogram_width) <= 117:
                 nextprograms_width = 104
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 104:
                     program_button_3.setPosition(669, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 51 and int(nextprogram1_width) <= 60:
                         nextprograms1_width = 51
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 51:
                             program_button_4.setPosition(724, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 567:
                                 nextprograms2_width = 570
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 570:
                                     program_button_5.setPosition(1419, int(pos_Y))




                     elif int(nextprogram1_width) >= 100 and int(nextprogram1_width) <= 117:
                         nextprograms1_width = 114
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 114:
                             program_button_4.setPosition(790, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) >= 100 and int(nextprogram2_width) <= 117:
                                 nextprograms2_width = 101
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 101:
                                     program_button_5.setPosition(897, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 59:
                                         nextprograms3_width = 56
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 56:
                                             program_button_6.setPosition(959, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 117:
                                                 nextprograms4_width = 106
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 106:
                                                     program_button_7.setPosition(1072, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 167:
                                                         nextprograms5_width = 167
                                                         program_button_7.setWidth(int(nextprograms5_width))

                                                         if int(nextprograms5_width) == 167:
                                                             program_button_8.setPosition(1246, int(pos_Y))




                                     elif int(nextprogram3_width) == 167:
                                         nextprograms3_width = 175
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 175:
                                             program_button_6.setPosition(1072, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 167:
                                                 program_button_7.setPosition(1246, int(pos_Y))



                                 elif int(nextprogram2_width) == 167:
                                     nextprograms2_width = 163
                                     program_button_4.setWidth(int(nextprograms2_width))

                                     if int(nextprograms2_width) == 163:
                                         program_button_5.setPosition(959, int(pos_Y))
                                         nextprogram3_width = program_button_5.getWidth()

                                         if int(nextprogram3_width) == 117:
                                             nextprograms3_width = 107
                                             program_button_5.setWidth(int(nextprograms3_width))

                                             if int(nextprograms3_width) == 107:
                                                 program_button_6.setPosition(1072, int(pos_Y))
                                                 nextprogram4_width = program_button_6.getWidth()

                                                 if int(nextprogram4_width) == 167:
                                                     program_button_7.setPosition(1246, int(pos_Y))



                             elif int(nextprogram2_width) == 167:
                                 nextprograms2_width = 162
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 162:
                                     program_button_5.setPosition(959, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 117:
                                         nextprograms3_width = 106
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 106:
                                             program_button_6.setPosition(1072, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 167:
                                                 program_button_7.setPosition(1246, int(pos_Y))
                                                 nextprogram5_width = program_button_7.getWidth()

                                                 if int(nextprogram5_width) >= 117:
                                                     program_button_8.setPosition(1419, int(pos_Y))
                                                     program_button_9.setPosition(1762, int(pos_Y))



                             elif int(nextprogram2_width) >= 567:
                                 program_button_4.setPosition(1419, int(pos_Y))



                     elif int(nextprogram1_width) == 167:
                         program_button_4.setPosition(838, int(pos_Y))
                         nextprogram2_width = program_button_4.getWidth()

                         if int(nextprogram2_width) == 117:
                             program_button_5.setPosition(959, int(pos_Y))


                     elif int(nextprogram1_width) >= 567:
                         program_button_4.setPosition(1419, int(pos_Y))




             elif int(nextprogram_width) >= 160 and int(nextprogram_width) <= 170:
                 nextprograms_width = 160
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 160:
                     program_button_3.setPosition(724, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 100 and int(nextprogram1_width) <= 117:
                         nextprograms1_width = 108
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 108:
                             program_button_4.setPosition(838, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 117:
                                 nextprograms2_width = 114
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 114:
                                     program_button_5.setPosition(959, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 59:
                                         nextprograms3_width = 53
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 53:
                                             program_button_6.setPosition(1016, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 117:
                                                 program_button_7.setPosition(1138, int(pos_Y))




                             elif int(nextprogram2_width) == 167:
                                 nextprograms2_width = 167
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 167:
                                     program_button_5.setPosition(1009, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 117:
                                         nextprograms3_width = 123
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 123:
                                             program_button_6.setPosition(1138, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 59:
                                                 nextprograms4_width = 42
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 42:
                                                     program_button_7.setPosition(1186, int(pos_Y))
                                                     nextprogram5_width = program_button_7.getWidth()

                                                     if int(nextprogram5_width) == 59:
                                                         nextprograms5_width = 54
                                                         program_button_7.setWidth(int(nextprograms5_width))

                                                         if int(nextprograms5_width) == 54:
                                                             program_button_8.setPosition(1246, int(pos_Y))




                             elif int(nextprogram2_width) >= 515:
                                 program_button_5.setPosition(1419, int(pos_Y))



                     elif int(nextprogram1_width) == 167:
                         program_button_4.setPosition(959, int(pos_Y))
                         nextprogram2_width = program_button_4.getWidth()

                         if int(nextprogram2_width) == 59:
                             program_button_5.setPosition(1019, int(pos_Y))



                     elif int(nextprogram1_width) == 286:
                         nextprograms1_width = 281
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 281:
                             program_button_4.setPosition(1009, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 59:
                                 nextprograms2_width = 57
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 57:
                                     program_button_5.setPosition(1072, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 59:
                                         program_button_6.setPosition(1128, int(pos_Y))



                                     elif int(nextprogram3_width) >= 286:
                                         program_button_6.setPosition(1419, int(pos_Y))
                                         program_button_7.setPosition(1762, int(pos_Y))



                     elif int(nextprogram1_width) == 515:
                         nextprograms1_width = 517
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 517:
                             program_button_4.setPosition(1246, int(pos_Y))




                     elif int(nextprogram1_width) >= 691:
                         program_button_4.setPosition(1419, int(pos_Y))



             elif int(nextprogram_width) >= 220 and int(nextprogram_width) <= 234:
                 nextprograms_width = 234
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 234:
                     program_button_3.setPosition(790, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 101:
                         program_button_4.setPosition(897, int(pos_Y))


                     elif int(nextprogram1_width) == 286:
                         nextprograms1_width = 275
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 275:
                             program_button_4.setPosition(1072, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) >= 279:
                                 program_button_5.setPosition(1419, int(pos_Y))


                     elif int(nextprogram1_width) == 342:
                         program_button_4.setPosition(1138, int(pos_Y))



             elif int(nextprogram_width) >= 277 and int(nextprogram_width) <= 284:
                 nextprograms_width = 273
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 273:
                     program_button_3.setPosition(838, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 117:
                         nextprograms1_width = 115
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 115:
                             program_button_4.setPosition(959, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 117:
                                 nextprograms2_width = 106
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 106:
                                     program_button_5.setPosition(1072, int(pos_Y))
                                     nextprogram3_width = program_button_5.getWidth()

                                     if int(nextprogram3_width) == 59:
                                         nextprograms3_width = 59
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 59:
                                             program_button_6.setPosition(1138, int(pos_Y))



                                     elif int(nextprogram3_width) == 117:
                                         nextprograms3_width = 106
                                         program_button_5.setWidth(int(nextprograms3_width))

                                         if int(nextprograms3_width) == 106:
                                             program_button_6.setPosition(1184, int(pos_Y))
                                             nextprogram4_width = program_button_6.getWidth()

                                             if int(nextprogram4_width) == 59:
                                                 nextprograms4_width = 57
                                                 program_button_6.setWidth(int(nextprograms4_width))

                                                 if int(nextprograms4_width) == 57:
                                                     program_button_7.setPosition(1246, int(pos_Y))



                     elif int(nextprogram1_width) == 286:
                         nextprograms1_width = 282
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 282:
                             program_button_4.setPosition(1125, int(pos_Y))



                     elif int(nextprogram1_width) == 342:
                         nextprograms1_width = 340
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 340:
                             program_button_4.setPosition(1184, int(pos_Y))



                     elif int(nextprogram1_width) >= 515:
                         program_button_4.setPosition(1419, int(pos_Y))





             elif int(nextprogram_width) >= 330 and int(nextprogram_width) <= 344:
                 nextprograms_width = 333
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 333:
                     program_button_3.setPosition(897, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 342:
                         nextprograms1_width = 343
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 343:
                             program_button_4.setPosition(1246, int(pos_Y))


                     elif int(nextprogram1_width) >= 515:
                         program_button_4.setPosition(1419, int(pos_Y))
                         program_button_5.setPosition(1624, int(pos_Y))



             elif int(nextprogram_width) >= 390 and int(nextprogram_width) <= 408:
                 nextprograms_width = 384
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 384:
                     program_button_3.setPosition(949, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 167:
                         nextprograms1_width = 171
                         program_button_3.setWidth(int(nextprograms_width))

                         if int(nextprograms_width) == 171:
                             program_button_4.setPosition(1125, int(pos_Y))



             elif int(nextprogram_width) == 456:
                 nextprograms_width = 445
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 445:
                     program_button_3.setPosition(1009, int(pos_Y))
                     nextprogram2_width = program_button_4.getWidth()

                     if int(nextprogram2_width) == 286:
                         nextprograms2_width = 282
                         program_button_3.setWidth(int(nextprograms2_width))

                         if int(nextprograms2_width) == 282:
                             program_button_4.setPosition(1246, int(pos_Y))



             elif int(nextprogram_width) == 515:
                 nextprograms_width = 507
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 507:
                     program_button_3.setPosition(1072, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 59:
                         program_button_4.setPosition(1138, int(pos_Y))



             elif int(nextprogram_width) >= 558 and int(nextprogram_width) <= 567:
                 nextprograms_width = 573
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 573:
                     program_button_3.setPosition(1138, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 59:
                         nextprograms1_width = 40
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 40:
                             program_button_4.setPosition(1184, int(pos_Y))



                     elif int(nextprogram1_width) == 117:
                         nextprograms1_width = 102
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 102:
                             program_button_4.setPosition(1246, int(pos_Y))



             elif int(nextprogram_width) == 626:
                 nextprograms_width = 620
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 620:
                     program_button_3.setPosition(1184, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 59:
                         nextprograms1_width = 56
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 56:
                             program_button_4.setPosition(1246, int(pos_Y))



                     elif int(nextprogram1_width) >= 342:
                         program_button_4.setPosition(1419, int(pos_Y))
                         program_button_5.setPosition(1762, int(pos_Y))




             elif int(nextprogram_width) == 691:
                 nextprograms_width = 681
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 681:
                     program_button_3.setPosition(1246, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 342:
                         program_button_4.setPosition(1527, int(pos_Y))



             elif int(nextprogram_width) >= 741:
                 program_button_3.setPosition(1419, int(pos_Y))
                 program_button_4.setPosition(1762, int(pos_Y))
                 program_button_5.setPosition(2104, int(pos_Y))
                 program_button_6.setPosition(2446, int(pos_Y))



     elif program_finished == '20' or program_finished == '50':
         programs_width = 229
         program_button_1.setWidth(int(programs_width))

         if int(programs_width) == 229:
             program_button_2.setPosition(610, int(pos_Y))
             nextprogram_width = program_button_2.getWidth()

             if int(nextprogram_width) >= 40 and int(nextprogram_width) <= 59:
                 nextprograms_width = 53
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 53:
                     program_button_3.setPosition(669, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 691:
                         program_button_4.setPosition(1419, int(pos_Y))




             elif int(nextprogram_width) >= 100 and int(nextprogram_width) <= 117:
                 nextprograms_width = 108
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 108:
                     program_button_3.setPosition(724, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 167:
                         program_button_4.setPosition(897, int(pos_Y))
                         nextprogram2_width = program_button_4.getWidth()

                         if int(nextprogram2_width) == 117:
                             nextprograms2_width = 106
                             program_button_4.setWidth(int(nextprograms2_width))

                             if int(nextprograms2_width) == 106:
                                 program_button_5.setPosition(1009, int(pos_Y))
                                 nextprogram3_width = program_button_5.getWidth()

                                 if int(nextprogram3_width) == 117:
                                     nextprograms3_width = 110
                                     program_button_5.setWidth(int(nextprograms3_width))

                                     if int(nextprograms3_width) == 110:
                                         program_button_6.setPosition(1125, int(pos_Y))
                                         nextprogram4_width = program_button_6.getWidth()

                                         if int(nextprogram4_width) == 117:
                                             nextprograms4_width = 114
                                             program_button_6.setWidth(int(nextprograms4_width))

                                             if int(nextprograms4_width) == 114:
                                                 program_button_7.setPosition(1246, int(pos_Y))



                     elif int(nextprogram1_width) == 515:
                         program_button_4.setPosition(1246, int(pos_Y))



                     elif int(nextprogram1_width) >= 567:
                         program_button_4.setPosition(1419, int(pos_Y))



             elif int(nextprogram_width) >= 160 and int(nextprogram_width) <= 172:
                 nextprograms_width = 173
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 173:
                     program_button_3.setPosition(790, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 515:
                         program_button_4.setPosition(1419, int(pos_Y))




             elif int(nextprogram_width) >= 219 and int(nextprogram_width) <= 230:
                 nextprograms_width = 222
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 222:
                     program_button_3.setPosition(838, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 515:
                         program_button_4.setPosition(1419, int(pos_Y))




             elif int(nextprogram_width) >= 280 and int(nextprogram_width) <= 290:
                 nextprograms_width = 283
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 283:
                     program_button_3.setPosition(897, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 101 and int(nextprogram1_width) <= 117:
                         nextprograms1_width = 114
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 114:
                             program_button_4.setPosition(1016, int(pos_Y))


                     elif int(nextprogram1_width) >= 161 and int(nextprogram1_width) <= 171:
                         nextprograms1_width = 169
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 169:
                             program_button_4.setPosition(1072, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 117:
                                 nextprograms2_width = 107
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 107:
                                     program_button_5.setPosition(1184, int(pos_Y))




                     elif int(nextprogram1_width) == 286:
                         nextprograms1_width = 281
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 281:
                             program_button_4.setPosition(1184, int(pos_Y))



             elif int(nextprogram_width) == 342:
                 nextprograms_width = 342
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 342:
                     program_button_3.setPosition(959, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 227:
                         nextprograms1_width = 230
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 230:
                             program_button_4.setPosition(1184, int(pos_Y))



                     elif int(nextprogram1_width) == 286:
                         nextprograms1_width = 282
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 282:
                             program_button_4.setPosition(1246, int(pos_Y))




             elif int(nextprogram_width) == 456:
                 nextprograms_width = 456
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 456:
                     program_button_3.setPosition(1072, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 59:
                         nextprograms1_width = 456
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 60:
                             program_button_4.setPosition(1138, int(pos_Y))




             elif int(nextprogram_width) == 515:
                 nextprograms_width = 522
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 522:
                     program_button_3.setPosition(1138, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 342:
                         program_button_4.setPosition(1762, int(pos_Y))




             elif int(nextprogram_width) == 567:
                 nextprograms_width = 569
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 569:
                     program_button_3.setPosition(1184, int(pos_Y))




             elif int(nextprogram_width) == 626:
                 nextprograms_width = 630
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 630:
                     program_button_3.setPosition(1246, int(pos_Y))
                     program_button_4.setPosition(1419, int(pos_Y))
                     program_button_5.setPosition(1762, int(pos_Y))



             elif int(nextprogram_width) >= 691:
                 program_button_3.setPosition(1419, int(pos_Y))
                 program_button_4.setPosition(1762, int(pos_Y))
                 program_button_5.setPosition(2104, int(pos_Y))




     elif program_finished == '25' or program_finished == '55':
         #ass1a
         programs_width = 288
         program_button_1.setWidth(int(programs_width))

         if int(programs_width) == 288:
             program_button_2.setPosition(669, int(pos_Y))
             nextprogram_width = program_button_2.getWidth()

             if int(nextprogram_width) >= 49 and int(nextprogram_width) <= 59:
                 nextprograms_width = 50
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 50:
                     program_button_3.setPosition(724, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 342:
                         program_button_4.setPosition(1072, int(pos_Y))



                     if int(nextprogram1_width) == 515:
                         program_button_4.setPosition(1246, int(pos_Y))


                     elif int(nextprogram1_width) >= 567:
                         program_button_4.setPosition(1419, int(pos_Y))
                         program_button_5.setPosition(1762, int(pos_Y))




             elif int(nextprogram_width) >= 106 and int(nextprogram_width) <= 122:
                 nextprograms_width = 114
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 114:
                     program_button_3.setPosition(790, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 102:
                         nextprograms1_width = 101
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 101:
                             program_button_4.setPosition(897, int(pos_Y))


                     if int(nextprogram1_width) >= 567:
                         program_button_4.setPosition(1364, int(pos_Y))
                         




             elif int(nextprogram_width) >= 160 and int(nextprogram_width) <= 170:
                 nextprograms_width = 163
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 163:
                     program_button_3.setPosition(838, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 342:
                         nextprograms1_width = 340
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 340:
                             program_button_4.setPosition(1184, int(pos_Y))



                     elif int(nextprogram1_width) >= 567:
                         program_button_4.setPosition(1364, int(pos_Y))




             elif int(nextprogram_width) >= 227 and int(nextprogram_width) <= 231:
                 nextprograms_width = 222
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 222:
                     program_button_3.setPosition(897, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 167:
                         nextprograms1_width = 169
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 169:
                             program_button_4.setPosition(1072, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 117:
                                 nextprograms2_width = 107
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 107:
                                     program_button_5.setPosition(1184, int(pos_Y))



                     elif int(nextprogram1_width) == 286:
                         nextprograms1_width = 282
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 282:
                             program_button_4.setPosition(1184, int(pos_Y))


                     elif int(nextprogram1_width) == 342:
                         program_button_4.setPosition(1246, int(pos_Y))




             elif int(nextprogram_width) >= 279 and int(nextprogram_width) <= 293:
                 nextprograms_width = 284
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 284:
                     program_button_3.setPosition(959, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 117:
                         nextprograms1_width = 106
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 106:
                             program_button_4.setPosition(1072, int(pos_Y))
                             nextprogram2_width = program_button_4.getWidth()

                             if int(nextprogram2_width) == 117:
                                 nextprograms2_width = 105
                                 program_button_4.setWidth(int(nextprograms2_width))

                                 if int(nextprograms2_width) == 105:
                                     program_button_5.setPosition(1184, int(pos_Y))



                     elif int(nextprogram1_width) == 286:
                         nextprograms1_width = 280
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 280:
                             program_button_4.setPosition(1246, int(pos_Y))


                         elif int(nextprogram1_width) >= 515:
                             program_button_4.setPosition(1419, int(pos_Y))




             #ass1a
             elif int(nextprogram_width) >= 330 and int(nextprogram_width) <= 344:
                 nextprograms_width = 335
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 335:
                     program_button_3.setPosition(1009, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 286:
                         program_button_4.setPosition(1419, int(pos_Y))




             elif int(nextprogram_width) >= 390 and int(nextprogram_width) <= 408:
                 nextprograms_width = 397
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 397:
                     program_button_3.setPosition(1072, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 342:
                         program_button_4.setPosition(1419, int(pos_Y))


                 elif int(nextprogram_width) >= 691:
                     program_button_3.setPosition(1419, int(pos_Y))




             elif int(nextprogram_width) == 456:
                 program_button_3.setPosition(1419, int(pos_Y))




             elif int(nextprogram_width) == 515:
                 nextprograms_width = 509
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 509:
                     program_button_3.setPosition(1184, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 59:
                         nextprograms1_width = 56
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 56:
                             program_button_4.setPosition(1246, int(pos_Y))




             elif int(nextprogram_width) == 567:
                 nextprograms_width = 562
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 562:
                     program_button_3.setPosition(1238, int(pos_Y))



             elif int(nextprogram_width) >= 626:
                 program_button_3.setPosition(1419, int(pos_Y))
                 program_button_4.setPosition(1762, int(pos_Y))





def EPG_time_2_and_EPG_time_3(self):
     program_finished = ''.join(str(x) for x in self.program_finished)
     program_id = ''.join(str(x) for x in self.program_id)
     nextprogram = int(program_id) + 1
     nextprogram1 = int(nextprogram) + 1
     nextprogram2 = int(nextprogram1) + 1
     nextprogram3 = int(nextprogram2) + 1
     nextprogram4 = int(nextprogram3) + 1
     nextprogram5 = int(nextprogram4) + 1
     nextprogram6 = int(nextprogram5) + 1
     nextprogram7 = int(nextprogram6) + 1
     nextprogram8 = int(nextprogram7) + 1
     program_button_1 = self.getControl(int(program_id))
     program_button_2 = self.getControl(int(nextprogram))
     program_button_3 = self.getControl(int(nextprogram1))
     program_button_4 = self.getControl(int(nextprogram2))
     program_button_5 = self.getControl(int(nextprogram3))
     program_button_6 = self.getControl(int(nextprogram4))
     program_button_7 = self.getControl(int(nextprogram5))
     program_button_8 = self.getControl(int(nextprogram6))
     program_button_9 = self.getControl(int(nextprogram7))
     program_button_10 = self.getControl(int(nextprogram8))
     pos_Y = program_button_1.getY()

     if program_finished == '05' or program_finished == '35':
         programs_width = 409
         program_button_1.setWidth(int(programs_width))

         if int(programs_width) == 409:
             program_button_2.setPosition(790, int(pos_Y))
             nextprogram_width = program_button_2.getWidth()

             if int(nextprogram_width) >= 40 and int(nextprogram_width) <= 59:
                 nextprograms_width = 42
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 42:
                     program_button_3.setPosition(838, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 117:
                         nextprograms1_width = 104
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 104:
                             program_button_4.setPosition(949, int(pos_Y))


                     elif int(nextprogram1_width) >= 691:
                         program_button_4.setPosition(1419, int(pos_Y))



             elif int(nextprogram_width) == 117:
                 nextprograms_width = 101
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 101:
                     program_button_3.setPosition(897, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 167:
                         nextprograms1_width = 168
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 168:
                             program_button_4.setPosition(1072, int(pos_Y))



                     elif int(nextprogram1_width) == 286:
                         nextprograms1_width = 282
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 282:
                             program_button_4.setPosition(1184, int(pos_Y))



                     elif int(nextprogram1_width) == 342:
                         nextprograms1_width = 342
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 342:
                             program_button_4.setPosition(1246, int(pos_Y))



                     elif int(nextprogram1_width) >= 396:
                         program_button_4.setPosition(1419, int(pos_Y))



             elif int(nextprogram_width) == 167:
                 nextprograms_width = 162
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 162:
                     program_button_3.setPosition(959, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 117:
                         nextprograms1_width = 107
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 107:
                             program_button_4.setPosition(1072, int(pos_Y))



             elif int(nextprogram_width) == 227:
                 nextprograms_width = 219
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 219:
                     program_button_3.setPosition(1016, int(pos_Y))




             elif int(nextprogram_width) >= 280 and int(nextprogram_width) <= 293:
                 nextprograms_width = 277
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 277:
                     program_button_3.setPosition(1072, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 167:
                         program_button_4.setPosition(1246, int(pos_Y))




             elif int(nextprogram_width) == 342:
                 nextprograms_width = 342
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 342:
                     program_button_3.setPosition(1138, int(pos_Y))



             elif int(nextprogram_width) == 456:
                 nextprograms_width = 451
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 451:
                     program_button_3.setPosition(1246, int(pos_Y))



             elif int(nextprogram_width) >= 515:
                 program_button_3.setPosition(1419, int(pos_Y))




     elif program_finished == '10' or program_finished == '40':
         programs_width = 457
         program_button_1.setWidth(int(programs_width))

         if int(programs_width) == 457:
             program_button_2.setPosition(838, int(pos_Y))
             nextprogram_width = program_button_2.getWidth()
             print nextprogram_width

             if int(nextprogram_width) >= 49 and int(nextprogram_width) <= 59:
                 nextprograms_width = 54
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 54:
                     program_button_3.setPosition(897, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 342:
                         program_button_4.setPosition(1419, int(pos_Y))



             elif int(nextprogram_width) == 117:
                 nextprograms_width = 114
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 114:
                     program_button_3.setPosition(959, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 117:
                         nextprogram1_width = 107
                         program_button_3.setWidth(int(nextprogram1_width))

                         if int(nextprogram1_width) == 107:
                             program_button_4.setPosition(1072, int(pos_Y))



             elif int(nextprogram_width) == 227:
                 nextprograms_width = 229
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 229:
                     program_button_3.setPosition(1072, int(pos_Y))



             elif int(nextprogram_width) == 286:
                 nextprograms_width = 282
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 282:
                     program_button_3.setPosition(1125, int(pos_Y))



             elif int(nextprogram_width) == 342:
                 nextprograms_width = 340
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 340:
                     program_button_3.setPosition(1184, int(pos_Y))



             elif int(nextprogram_width) == 396:
                 nextprograms_width = 402
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 402:
                     program_button_3.setPosition(1246, int(pos_Y))



             elif int(nextprogram_width) >= 456:
                 program_button_3.setPosition(1419, int(pos_Y))





     elif program_finished == '15' or program_finished == '45':
         programs_width = 517
         program_button_1.setWidth(int(programs_width))

         if int(programs_width) == 517:
             program_button_2.setPosition(897, int(pos_Y))
             nextprogram_width = program_button_2.getWidth()

             if int(nextprogram_width) == 59:
                 nextprograms_width = 56
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 56:
                     program_button_3.setPosition(959, int(pos_Y))



             elif int(nextprogram_width) == 117:
                 nextprograms_width = 107
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 107:
                     program_button_3.setPosition(1009, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 59:
                         nextprograms1_width = 58
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 58:
                             program_button_4.setPosition(1072, int(pos_Y))



             elif int(nextprogram_width) == 167:
                 nextprograms_width = 169
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 169:
                     program_button_3.setPosition(1072, int(pos_Y))




             elif int(nextprogram_width) == 227:
                 nextprograms_width = 234
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 234:
                     program_button_3.setPosition(1138, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 342:
                         program_button_4.setPosition(1419, int(pos_Y))



             elif int(nextprogram_width) == 286:
                 nextprograms_width = 282
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 282:
                     program_button_3.setPosition(1184, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) >= 286:
                         program_button_4.setPosition(1419, int(pos_Y))



             elif int(nextprogram_width) == 342:
                 nextprograms_width = 343
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 343:
                     program_button_3.setPosition(1246, int(pos_Y))



             elif int(nextprogram_width) >= 456:
                 program_button_3.setPosition(1419, int(pos_Y))
                 program_button_4.setPosition(1762, int(pos_Y))




     elif program_finished == '20' or program_finished == '50':
         programs_width = 577
         program_button_1.setWidth(int(programs_width))

         if int(programs_width) == 577:
             program_button_2.setPosition(959, int(pos_Y))
             nextprogram_width = program_button_2.getWidth()

             if int(nextprogram_width) >= 40 and int(nextprogram_width) <= 59:
                 nextprograms_width = 44
                 program_button_2.setWidth(int(nextprograms_width))
                 #IF THE OTHER PROGRAM IS IN THE SAME LINE AS THE 46, ADD THE CODE

                 if int(nextprograms_width) == 44:
                     program_button_3.setPosition(1009, int(pos_Y))
                     program_button_4.setPosition(1419, int(pos_Y))



             elif int(nextprogram_width) == 117:
                 nextprograms_width = 107
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 107:
                     program_button_3.setPosition(1072, int(pos_Y))
                     nextprogram1_width = program_button_3.getWidth()

                     if int(nextprogram1_width) == 117:
                         nextprograms1_width = 106
                         program_button_3.setWidth(int(nextprograms1_width))

                         if int(nextprograms1_width) == 106:
                             program_button_4.setPosition(1184, int(pos_Y))



             elif int(nextprogram_width) == 167:
                 nextprograms_width = 172
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 172:
                     program_button_3.setPosition(1138, int(pos_Y))



             elif int(nextprogram_width) == 227:
                 nextprograms_width = 219
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 219:
                     program_button_3.setPosition(1184, int(pos_Y))




             elif int(nextprogram_width) == 286:
                 nextprograms_width = 281
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 281:
                     program_button_3.setPosition(1246, int(pos_Y))



             elif int(nextprogram_width) >= 342:
                 program_button_3.setPosition(1419, int(pos_Y))
                 program_button_4.setPosition(1762, int(pos_Y))






     elif program_finished == '25' or program_finished == '55':
         programs_width = 629
         program_button_1.setWidth(int(programs_width))

         if int(programs_width) == 629:
             program_button_2.setPosition(1009, int(pos_Y))
             nextprogram_width = program_button_2.getWidth()

             if int(nextprogram_width) == 59:
                 nextprograms_width = 57
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 57:
                     program_button_3.setPosition(1072, int(pos_Y))



             elif int(nextprogram_width) == 117:
                 nextprograms_width = 110
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) >= 110:
                     program_button_3.setPosition(1125, int(pos_Y))



             elif int(nextprogram_width) == 227:
                 nextprograms_width = 230
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 230:
                     program_button_3.setPosition(1246, int(pos_Y))




             elif int(nextprogram_width) == 342:
                 nextprograms_width = 343
                 program_button_2.setWidth(int(nextprograms_width))

                 if int(nextprograms_width) == 343:
                     program_button_3.setPosition(1009, int(pos_Y))



             elif int(nextprogram_width) >= 515:
                 program_button_3.setPosition(1419, int(pos_Y))




def EPG_time_3(self):
     program_finished = ''.join(str(x) for x in self.program_finished)
     program_id = ''.join(str(x) for x in self.program_id)
     nextprogram = int(program_id) + 1
     nextprogram1 = int(nextprogram) + 1
     nextprogram2 = int(nextprogram1) + 1
     nextprogram3 = int(nextprogram2) + 1
     nextprogram4 = int(nextprogram3) + 1
     nextprogram5 = int(nextprogram4) + 1
     nextprogram6 = int(nextprogram5) + 1
     nextprogram7 = int(nextprogram6) + 1
     nextprogram8 = int(nextprogram7) + 1
     program_button_1 = self.getControl(int(program_id))
     program_button_2 = self.getControl(int(nextprogram))
     program_button_3 = self.getControl(int(nextprogram1))
     program_button_4 = self.getControl(int(nextprogram2))
     program_button_5 = self.getControl(int(nextprogram3))
     program_button_6 = self.getControl(int(nextprogram4))
     program_button_7 = self.getControl(int(nextprogram5))
     program_button_8 = self.getControl(int(nextprogram6))
     program_button_9 = self.getControl(int(nextprogram7))
     program_button_10 = self.getControl(int(nextprogram8))
     program_width = program_button_1.getWidth()
     program_stop_times = ''.join(str(x) for x in self.program_end_time)
     program_stop_time = time.strptime(program_stop_times, '%d/%m/%Y %I:%M%p')
     epg_time_3 = ''.join(str(x) for x in self.epg_time_3)
     epg_time_3 = time.strptime(epg_time_3, '%d/%m/%Y %I:%M%p')
     pos_Y = program_button_1.getY()
     print "you are calling EPG_time_3"
     print epg_time_3

     if program_stop_time == epg_time_3:
         print "you are calling EPG_time_3 =="
         if int(program_width) >= 670:
             programs_width = 691
             program_button_1.setWidth(int(programs_width))
             print "you are working on 691 epg_time_3"

             if int(programs_width) == 691:
                 program_button_2.setPosition(1072, int(pos_Y))
                 nextprogram_width = program_button_2.getWidth()
                 print "691 program width size for nextprogram"
                 print nextprogram_width

                 if int(nextprogram_width) == 59:
                     nextprograms_width = 60
                     program_button_2.setWidth(int(nextprograms_width))

                     if int(nextprograms_width) == 60:
                         program_button_3.setPosition(1138, int(pos_Y))
                         nextprogram1_width = program_button_3.getWidth()

                         if int(nextprogram1_width) == 117:
                             nextprograms1_width = 103
                             program_button_3.setWidth(int(nextprograms1_width))

                             if int(nextprograms1_width) == 103:
                                 program_button_4.setPosition(1246, int(pos_Y))



                 elif int(nextprogram_width) == 117:
                     nextprograms_width = 106
                     program_button_2.setWidth(int(nextprograms_width))

                     if int(nextprograms_width) == 106:
                         program_button_3.setPosition(1184, int(pos_Y))



                 elif int(nextprogram_width) == 167:
                     nextprograms_width = 168
                     program_button_2.setWidth(int(nextprograms_width))

                     if int(nextprograms_width) == 168:
                         program_button_3.setPosition(1246, int(pos_Y))



                 elif int(nextprogram_width) >= 342:
                     program_button_3.setPosition(1419, int(pos_Y))
                     program_button_4.setPosition(1762, int(pos_Y))
                     #program_button_5.setPosition(2106, int(pos_Y))
                     #program_button_6.setPosition(2405, int(pos_Y))



     elif program_stop_time > epg_time_3:
         #program_stop_times = ''.join(str(x) for x in self.program_end_time)
         #program_stop_time = time.strptime(program_stop_times, '%d/%m/%Y %I:%M%p')
         #program_stop_time = str(program_stop_time)
         epg_time_1 = ''.join(str(x) for x in self.epg_time_1)
         epg_time_2 = ''.join(str(x) for x in self.epg_time_2)
         epg_time_3 = ''.join(str(x) for x in self.epg_time_3)
         epg_time_1 = time.strptime(epg_time_1, '%d/%m/%Y %I:%M%p')
         epg_time_2 = time.strptime(epg_time_2, '%d/%m/%Y %I:%M%p')
         epg_time_3 = time.strptime(epg_time_3, '%d/%m/%Y %I:%M%p')
         print "epg_time_1"
         print epg_time_1
         print "you are calling EPG_time_3 >"
         print program_stop_time
         program_finished = ''.join(str(x) for x in self.program_finished)
         epg_time1 = str(self.getControl(344).getLabel())
         epg_time1 = epg_time1.split(':')[1].replace('PM', '').replace('AM', '')
         
         epg_time1_hour = epg_time_1.tm_hour
         epg_time2 = str(self.getControl(345).getLabel())
         epg_time2 = epg_time2.split(':')[1].replace('PM', '').replace('AM', '')
         epg_time2_hour = epg_time_2.tm_hour
         epg_time3 = str(self.getControl(346).getLabel())
         epg_time3 = epg_time3.split(':')[1].replace('PM', '').replace('AM', '')
         epg_time3_hour = epg_time_3.tm_hour
         program_stop_hour = program_stop_time.tm_hour
         program_width = program_button_1.getWidth()
         programX = program_button_1.getX()
         print "program_stop_hour"
         print program_stop_hour

         if program_stop_hour == epg_time3_hour:
             print "passed epg_time3 2 a"
             print program_finished

             if epg_time3 == '00':
                 if program_finished == '00':
                     print "you are in here6b 1"
                     if programX == 375 and int(program_width) >= 691:
                         programs_width = 691
                         program_button_1.setWidth(programs_width)
                         print "you are in here6b 2"

                         if int(programs_width) == 691:
                             program_button_2.setPosition(1072, int(pos_Y))
                             print "you are in here6b 3"



                 elif program_finished == '05' or program_finished == '35':
                     if programX == 375 and int(program_width) >= 691:
                         programs_width = 757
                         program_button_1.setWidth(programs_width)
                         print "you are in program finished 35................"

                         if int(programs_width) == 757:
                             program_button_2.setPosition(1138, int(pos_Y))
                             nextprogram_width = program_button_2.getWidth()

                             if int(nextprogram_width) == 59:
                                 nextprograms_width = 40
                                 program_button_2.setWidth(nextprograms_width)

                                 if int(nextprograms_width) == 40:
                                     program_button_3.setPosition(1184, int(pos_Y))



                             elif int(nextprogram_width) >= 227:
                                 program_button_3.setPosition(1419, int(pos_Y))



                 elif program_finished == '10' or program_finished == '40':
                     if programX == 375 and int(program_width) >= 691:
                         programs_width = 803
                         program_button_1.setWidth(programs_width)

                         if int(programs_width) == 803:
                             program_button_2.setPosition(1184, int(pos_Y))
                             nextprogram_width = program_button_2.getWidth()

                             if int(nextprogram_width) == 59:
                                 nextprograms_width = 57
                                 program_button_2.setWidth(nextprograms_width)

                                 if int(nextprograms_width) == 57:
                                     program_button_3.setPosition(1246, int(pos_Y))


                             elif int(nextprogram_width) >= 456:
                                 program_button_3.setPosition(1419, int(pos_Y))



                 elif program_finished == '15' or program_finished == '45':
                     if programX == 375 and int(program_width) >= 691:
                         programs_width = 865
                         program_button_1.setWidth(programs_width)

                         if int(programs_width) == 865:
                             program_button_2.setPosition(1246, int(pos_Y))



                 elif program_finished == '20' or program_finished == '50':
                     if programX == 375 and int(program_width) >= 691:
                         program_button_2.setPosition(1419, int(pos_Y))



                 elif program_finished == '25' or program_finished == '55':
                     if programX == 375 and int(program_width) >= 691:
                         program_button_2.setPosition(1419, int(pos_Y))



                 elif program_finished == '30' or program_finished == '00':
                     print "you are here in epg_time_3 in 30 mins"
                     print program_stop_time
                     print epg_time_3
                     
                     
                     if program_stop_time == epg_time_2:
                         if programX == 375 and int(program_width) >= 342:
                             programs_width = 344
                             program_button_1.setWidth(programs_width)

                             if int(programs_width) == 344:
                                 program_button_2.setPosition(724, int(pos_Y))

                                 if int(programs_width) == 344 and int(nextprogram_width) == 344:
                                     nextprograms_width = 342
                                     program_button_2.setWidth(nextprograms_width)

                                     if int(nextprograms_width) == 342:
                                         program_button_3.setPosition(1072, int(pos_Y))



                                 elif int(nextprogram_width) >= 342 and int(nextprogram_width) <= 344:
                                     nextprograms_width = 340
                                     program_button_2.setWidth(nextprograms_width)

                                     if int(nextprograms_width) == 340:
                                         program_button_3.setPosition(1072, int(pos_Y))




                     elif program_stop_time > epg_time_3:
                         print "passed 3"
                         if programX == 375 and int(program_width) >= 1026:
                             programs_width = 1035
                             program_button_1.setWidth(programs_width)

                             if int(programs_width) == 1035:
                                 program_button_2.setPosition(1414, int(pos_Y))





             elif epg_time3 == '30':
                 if program_finished == '00':
                     if programX == 375 and int(program_width) > 692:
                         programs_width = 1033
                         program_button_1.setWidth(programs_width)

                         if int(programs_width) == 1033:
                             program_button_2.setPosition(1412, int(pos_Y))



                 elif program_finished == '05':
                     if programX == 375 and int(program_width) > 692:
                         programs_width = 1093
                         program_button_1.setWidth(programs_width)



                 elif program_finished == '10':
                     if programX == 375 and int(program_width) >= 1037:
                         programs_width = 798
                         program_button_1.setWidth(programs_width)

                         if int(programs_width) == 798:
                             program_button_2.setPosition(1180, int(pos_Y))



                 elif program_finished == '25':
                     if programX == 375 and int(program_width) >= 691:
                         programs_width = 626
                         program_button_1.setWidth(programs_width)

                         if int(programs_width) == 626:
                             program_button_2.setPosition(1009, int(pos_Y))
                             nextprogram_width = program_button_2.getWidth()

                             if int(nextprogram_width) == 59:
                                 nextprograms_width = 56
                                 program_button_2.setWidth(nextprograms_width)

                                 if int(nextprograms_width) == 56:
                                     program_button_3.setPosition(1072, int(pos_Y))



                 elif program_finished == '30':
                     if programX == 375 and int(program_width) > 691:
                         programs_width = 691
                         program_button_1.setWidth(programs_width)

                         if int(programs_width) == 691:
                             program_button_2.setPosition(1072, int(pos_Y))



                 elif program_finished == '35':
                     if programX == 375 and int(program_width) > 691:
                         programs_width = 757
                         program_button_1.setWidth(programs_width)

                         if int(programs_width) == 757:
                             program_button_2.setPosition(1138, int(pos_Y))
                             nextprogram_width = program_button_2.getWidth()

                             if int(nextprogram_width) == 59:
                                 nextprograms_width = 40
                                 program_button_2.setWidth(nextprograms_width)

                                 if int(nextprograms_width) == 40:
                                     program_button_3.setPosition(1184, int(pos_Y))



                             elif int(nextprogram_width) >= 227:
                                 program_button_3.setPosition(1419, int(pos_Y))




                 elif program_finished == '40':
                     if programX == 375 and int(program_width) >= 691:
                         programs_width = 803
                         program_button_1.setWidth(programs_width)

                         if int(programs_width) == 803:
                             program_button_2.setPosition(1184, int(pos_Y))
                             nextprogram_width = program_button_2.getWidth()

                             if int(nextprogram_width) == 59:
                                 nextprograms_width = 56
                                 program_button_2.setWidth(nextprograms_width)

                                 if int(nextprograms_width) == 56:
                                     program_button_3.setPosition(1246, int(pos_Y))



                 elif program_finished == '45':
                     if programX == 375 and int(program_width) >= 691:
                         programs_width = 865
                         program_button_1.setWidth(programs_width)

                         if int(programs_width) == 865:
                             program_button_2.setPosition(1246, int(pos_Y))



                 elif program_finished == '50':
                     print "channel 5 here 3"
                     if programX == 375 and int(program_width) == 568:
                         programs_width = 228
                         program_button_1.setWidth(programs_width)
                         print "channel 5 here 4 a"

                         if int(programs_width) == 228:
                             program_button_2.setPosition(610, int(pos_Y))
                             nextprogram_width = program_button_2.getWidth()

                             if int(nextprogram_width) == 117:
                                 nextprograms_width = 109
                                 program_button_2.setWidth(nextprograms_width)

                                 if int(nextprograms_width) == 109:
                                     program_button_3.setPosition(724, int(pos_Y))
                                     nextprogram1_width = program_button_3.getWidth()
                                     print "nextprogram1_width"
                                     print nextprogram1_width

                                     if int(nextprogram1_width) == 106:
                                         nextprogram1s_width = 114
                                         program_button_3.setWidth(nextprogram1s_width)

                                         if int(nextprogram1s_width) == 114:
                                             program_button_4.setPosition(844, int(pos_Y))



                             elif int(nextprogram_width) == 230:
                                 nextprograms_width = 221
                                 program_button_2.setWidth(nextprograms_width)

                                 if int(nextprograms_width) == 221:
                                     program_button_3.setPosition(838, int(pos_Y))



                             elif int(nextprogram_width) == 290:
                                 nextprograms_width = 281
                                 program_button_2.setWidth(nextprograms_width)

                                 if int(nextprograms_width) == 281:
                                     program_button_3.setPosition(897, int(pos_Y))
                                     nextprogram1_width = program_button_3.getWidth()

                                     if int(nextprogram1_width) >= 515:
                                         program_button_4.setPosition(1419, int(pos_Y))



                     elif programX == 375 and int(program_width) >= 691:
                         programs_width = 918
                         program_button_1.setWidth(programs_width)
                         print "channel 5 here 4 b"

                         if int(programs_width) == 918:
                             program_button_2.setPosition(1297, int(pos_Y))



                 elif program_finished == '55':
                     if programX == 375 and int(program_width) >= 691:
                         programs_width = 978
                         program_button_1.setWidth(programs_width)

                         if int(programs_width) == 978:
                             program_button_2.setPosition(1357, int(pos_Y))



         else:
             program_button_2.setPosition(1419, int(pos_Y))
             program_button_3.setPosition(1762, int(pos_Y))
             print "you are in the else for channel 5"



     elif int(program_width) >= 1026:
         program_button_2.setPosition(1419, int(pos_Y))
         program_button_3.setPosition(1762, int(pos_Y))
         program_button_4.setPosition(2104, int(pos_Y))
         program_button_5.setPosition(2448, int(pos_Y))
         program_button_6.setPosition(2792, int(pos_Y))
         print "you are working on 1026"




def get_programming_times(self):
     #global self.program_stop_minutes, self.program_stop_time, self.epg_time_1, self.epg_time_2, self.epg_time_3
     #print "you are now calling the get_programming_times function now chrisssssssssssssssss"

     if self.select_db_flag == True:
         self.select_db_flag = False
         self.program_finished = list()

         if self.single_program == True:
             self.single_program = False
             self.program_end_time = list()
             program_id = ''.join(str(x) for x in self.program_id)
             print "self.program_id in get_programming_times"
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

                 if program_stop_minutes == "0":
                     program_stop_minutes = "00"
                 elif program_stop_minutes == "5":
                     program_stop_minutes = "05"


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
                 program_end_time = str(program_stop_days + "/" + program_stop_months + "/" + program_stop_year + " " + program_times)
                 self.program_end_time.append(program_end_time)
                 self.program_finished.append(program_stop_minutes)
                 print "self.program_end_time"
                 print self.program_end_time



         else:
             for program_id in self.prog_id_list:
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
                     program_end_time = str(program_stop_days + "/" + program_stop_months + "/" + program_stop_year + " " + program_times)
                     self.program_end_time.append(program_end_time)
                     self.program_finished.append(program_stop_minutes)
                     print "self.program_end_time"
                     print self.program_end_time


         #return self.program_stop_minutes, self.program_stop_time





         
def epg_times_stamp(self):
     self.epg_time_1 = list()
     self.epg_time_2 = list()
     self.epg_time_3 = list()
     epg_time1 = str(self.getControl(344).getLabel())
     epg_time2 = str(self.getControl(345).getLabel())
     epg_time3 = str(self.getControl(346).getLabel())
     day_date = self.program_day
     day = ''
     month = ''
     year = ''
     print "you are calling epg_times_stamp..................."
     print day_date

     if day_date >= 0 and day_date <= 6:
         if epg_time3 == '12:00AM':
             epg_time_1 = datetime.datetime.now() + datetime.timedelta(days = self.program_day - 1)
             epg_time_2 = datetime.datetime.now() + datetime.timedelta(days = self.program_day - 1)
             epg_time_3 = datetime.datetime.now() + datetime.timedelta(days = self.program_day)
             epg1_day = epg_time_1.strftime("%d")
             epg1_month = epg_time_1.strftime("%m")
             epg1_year = epg_time_1.strftime("%Y")
             epg2_day = epg_time_2.strftime("%d")
             epg2_month = epg_time_2.strftime("%m")
             epg2_year = epg_time_2.strftime("%Y")
             epg3_day = epg_time_2.strftime("%d")
             epg3_month = epg_time_2.strftime("%m")
             epg3_year = epg_time_2.strftime("%Y")
             half_hour = str(epg1_day + "/" + epg1_month + "/" + epg1_year + " " + epg_time1)
             one_hour = str(epg2_day + "/" + epg2_month + "/" + epg2_year + " " + epg_time2)
             one_hour_half = str(epg3_day + "/" + epg3_month + "/" + epg3_year + " " + epg_time3)
         else:
             if epg_time1 == '12:00AM':
                 epg_time_1 = datetime.datetime.now() + datetime.timedelta(days = self.program_day)
                 epg_time_2 = datetime.datetime.now() + datetime.timedelta(days = self.program_day)
                 epg_time_3 = datetime.datetime.now() + datetime.timedelta(days = self.program_day)

             elif epg_time2 == '12:00AM':
                 epg_time_1 = datetime.datetime.now() + datetime.timedelta(days = self.program_day - 1)
                 epg_time_2 = datetime.datetime.now() + datetime.timedelta(days = self.program_day)
                 epg_time_3 = datetime.datetime.now() + datetime.timedelta(days = self.program_day)
             else:
                 epg_time_1 = datetime.datetime.now() + datetime.timedelta(days = self.program_day)
                 epg_time_2 = datetime.datetime.now() + datetime.timedelta(days = self.program_day)
                 epg_time_3 = datetime.datetime.now() + datetime.timedelta(days = self.program_day)


             epg1_day = epg_time_1.strftime("%d")
             epg1_month = epg_time_1.strftime("%m")
             epg1_year = epg_time_1.strftime("%Y")
             epg2_day = epg_time_2.strftime("%d")
             epg2_month = epg_time_2.strftime("%m")
             epg2_year = epg_time_2.strftime("%Y")
             epg3_day = epg_time_2.strftime("%d")
             epg3_month = epg_time_2.strftime("%m")
             epg3_year = epg_time_2.strftime("%Y")
             half_hour = str(epg1_day + "/" + epg1_month + "/" + epg1_year + " " + epg_time1)
             one_hour = str(epg2_day + "/" + epg2_month + "/" + epg2_year + " " + epg_time2)
             one_hour_half = str(epg3_day + "/" + epg3_month + "/" + epg3_year + " " + epg_time3)


         self.epg_time_1.append(half_hour)
         self.epg_time_2.append(one_hour)
         self.epg_time_3.append(one_hour_half)
         print "half_hour for move right........................."
         print half_hour
         print "one_hour for move right........................."
         print one_hour
         print "one_hour_half for move right........................."
         print one_hour_half




def update_buttons(self):
     program_id = ''.join(str(x) for x in self.program_id)
     nextprogram = int(program_id) + 1
     nextprogram1 = int(nextprogram) + 1
     nextprogram2 = int(nextprogram1) + 1
     nextprogram3 = int(nextprogram2) + 1
     nextprogram4 = int(nextprogram3) + 1
     nextprogram5 = int(nextprogram4) + 1
     nextprogram6 = int(nextprogram5) + 1
     nextprogram7 = int(nextprogram6) + 1
     nextprogram8 = int(nextprogram7) + 1
     program_button_1 = self.getControl(int(program_id))
     program_button_2 = self.getControl(int(nextprogram))
     program_button_3 = self.getControl(int(nextprogram1))
     program_button_4 = self.getControl(int(nextprogram2))
     program_button_5 = self.getControl(int(nextprogram3))
     program_button_6 = self.getControl(int(nextprogram4))
     program_button_7 = self.getControl(int(nextprogram5))
     program_button_8 = self.getControl(int(nextprogram6))
     program_button_9 = self.getControl(int(nextprogram7))
     program_button_10 = self.getControl(int(nextprogram8))
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
     nextprogram8_width = program_button_10.getWidth()
     nextprogram8_label = program_button_10.getLabel()
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
     program_button_9.setLabel(nextprogram8_label)
     program_button_9.setWidth(nextprogram8_width)
     program_button_10.setLabel('')
     program_button_10.setWidth(0)
     update_in_database(self)
     program_id = int(nextprogram8)
     profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
     conn = database.connect(profilePath)
     cur = conn.cursor()
     cur.execute('SELECT title, start_date, stop_date FROM programs where program_id=?', [program_id])
     row = cur.fetchone()


     if row is not None:
         title = row[0]
         program_title = program_title = '[B]' + title.encode('utf-8', 'ignore') + '[/B]'
         program_start_date = str(row[1])
         program_end_date = str(row[2])

         #convert the date formats into minutes
         minutes_start = self.parseDateTimeToMinutesSinceEpoch(program_start_date)
         minutes_end = self.parseDateTimeToMinutesSinceEpoch(program_end_date)
         minutes_length = minutes_end - minutes_start
         program_minutes = minutes_length

         #work out on program per minute to multiply by 11.4 to get the width size
         program_width = program_minutes * 11.4
         program_width = eval(str(program_width).replace('.0', ''))

         #create width size for program buttons
         if program_width == 57:
             program_width = 59
         elif program_width == 79:
             program_width = 59
         elif program_width == 114:
             program_width = 117
         elif program_width == 148:
             program_width = 168
         elif program_width == 171:
             program_width = 167
         elif program_width == 228:
             program_width = 227
         elif program_width == 278:
             program_width = 276
         elif program_width == 285:
             program_width = 286
         elif program_width == 342:
             program_width = 342
         elif program_width == 399:
             program_width = 396
         elif program_width == 460:
             program_width = 456
         elif program_width == 453:
             program_width = 452
         elif program_width == 513:
             program_width = 515
         elif program_width == 570:
             program_width = 567
         elif program_width == 627:
             program_width = 626
         elif program_width == 677:
             program_width = 676
         elif program_width == 684:
             program_width = 691
         elif program_width == 3876:
             program_width = 3787

         #set the program button size and text
         program_button_10.setLabel(program_title)
         program_button_10.setWidth(program_width)
         conn.close()




def update_in_database(self):
     profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
     conn = database.connect(profilePath)
     cur = conn.cursor()
     program_id = ''.join(str(x) for x in self.program_id)
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
         try:
             cur.execute("UPDATE programs set program_id=? WHERE channel=? and start_date=? ",(value-1,data[0],data[1]))
         except:
             pass
         conn.commit()
         conn.close()




def GoRight(self):
     print "you are calling GoRight.............................."
     print "self.move_right_flag"
     print self.move_right_flag


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
                     self.program_id = list()
                     self.program_end_time = list()
                     self.select_db_flag = True
                     get_programming_times(self)
                     #epg_times_stamp(self)
                     
                     half_hour_date = ''.join(str(x) for x in self.epg_time_1)
                     one_hour_date = ''.join(str(x) for x in self.epg_time_2)
                     one_hour_half_date = ''.join(str(x) for x in self.epg_time_3)
                     epg_time_1 = time.strptime(half_hour_date, '%d/%m/%Y %I:%M%p')
                     epg_time_2 = time.strptime(one_hour_date, '%d/%m/%Y %I:%M%p')
                     epg_time_3 = time.strptime(one_hour_half_date, '%d/%m/%Y %I:%M%p')
                     
                     print "epg_time_1 for right move............."
                     print epg_time_1
                     print "epg_time_2 for right move............."
                     print epg_time_2
                     print "epg_time_3 for right move............."
                     print epg_time_3
                     
                     #half_hour_date = ''.join(str(x) for x in self.epg_time_1)
                     #one_hour_date = ''.join(str(x) for x in self.epg_time_2)
                     #one_hour_half_date = ''.join(str(x) for x in self.epg_time_3)
                     #epg_time_1 = time.strptime(half_hour_date, '%d/%m/%Y %I:%M%p')
                     #epg_time_2 = time.strptime(one_hour_date, '%d/%m/%Y %I:%M%p')
                     #epg_time_3 = time.strptime(one_hour_half_date, '%d/%m/%Y %I:%M%p')
                     #print "program_stop_times for go right................................"
                     #print self.program_day

                     for program_id, program_stop_times, program_finished in zip(self.prog_id_list, self.program_end_time, self.program_finished):
                         program_stop_time = time.strptime(program_stop_times, '%d/%m/%Y %I:%M%p')
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
                         self.program_id = list()
                         print "----------- Begin Data ----------"
                         print "program_stop_time"
                         print program_stop_time

                         if program_stop_time <= epg_time_1:
                             print "here 8b"

                             if program_stop_time <= epg_time_1:
                                 program_id = program_button_1.getId()
                                 nextprogram_width = program_button_2.getWidth()
                                 self.program_id = list()
                                 self.program_id.append(program_id)
                                 update_buttons(self)
                                 program_width = program_button_1.getWidth()
                                 print "you are working on 344 button"
                                 print self.program_id

                                 if int(program_width) >= 30:
                                     #use this code to call get_programming_times
                                     self.program_id = list()
                                     self.program_id.append(program_id)
                                     self.program_end_time = list()
                                     self.select_db_flag = True
                                     self.single_program = True
                                     get_programming_times(self)
                                     program_stop_times = ''.join(str(x) for x in self.program_end_time)
                                     program_stop_time = time.strptime(program_stop_times, '%d/%m/%Y %I:%M%p')
                                     print "now you are working on 59 area"
                                     print program_stop_time
                                     print "epg_time_2"
                                     #print epg_time_2

                                     if program_stop_time <= epg_time_1:
                                         update_buttons(self)
                                         program_width = program_button_1.getWidth()
                                         self.program_id = list()
                                         self.program_id.append(program_id)
                                         self.program_end_time = list()
                                         self.select_db_flag = True
                                         self.single_program = True
                                         get_programming_times(self)
                                         program_stop_times = ''.join(str(x) for x in self.program_end_time)
                                         program_stop_time = time.strptime(program_stop_times, '%d/%m/%Y %I:%M%p')
                                         program_finished = ''.join(str(x) for x in self.program_finished)
                                         print "you are under program_stop_time 1"

                                         if program_stop_time <= epg_time_1:
                                             update_buttons(self)
                                             program_width = program_button_1.getWidth()
                                             print "now you are working on 109 area c"
                                             self.program_id = list()
                                             self.program_id.append(program_id)
                                             self.program_end_time = list()
                                             self.select_db_flag = True
                                             self.single_program = True
                                             get_programming_times(self)
                                             program_stop_times = ''.join(str(x) for x in self.program_end_time)
                                             program_stop_time = time.strptime(program_stop_times, '%d/%m/%Y %I:%M%p')

                                             if program_stop_time <= epg_time_1:
                                                 update_buttons(self)
                                                 self.program_id = list()
                                                 self.program_id.append(program_id)
                                                 self.program_end_time = list()
                                                 self.select_db_flag = True
                                                 self.single_program = True
                                                 get_programming_times(self)
                                                 program_stop_times = ''.join(str(x) for x in self.program_end_time)
                                                 program_stop_time = time.strptime(program_stop_times, '%d/%m/%Y %I:%M%p')
                                                 program_finished = ''.join(str(x) for x in self.program_finished)

                                                 if program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                                                     EPG_time_1_and_EPG_time_2(self)


                                                 elif program_stop_time == epg_time_2:
                                                     EPG_time_2(self)


                                                 elif program_stop_time > epg_time_2 and program_stop_time < epg_time_3:
                                                     EPG_time_2_and_EPG_time_3(self)


                                                 elif program_stop_time == epg_time_3:
                                                     EPG_time_3(self)


                                             elif program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                                                 EPG_time_1_and_EPG_time_2(self)


                                             elif program_stop_time == epg_time_2:
                                                 EPG_time_2(self)


                                             elif program_stop_time > epg_time_2 and program_stop_time < epg_time_3:
                                                 EPG_time_2_and_EPG_time_3(self)


                                             elif program_stop_time == epg_time_3:
                                                 EPG_time_3(self)


                                         elif program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                                             EPG_time_1_and_EPG_time_2(self)


                                         elif program_stop_time == epg_time_2:
                                             EPG_time_2(self)


                                         elif program_stop_time > epg_time_2 and program_stop_time < epg_time_3:
                                             EPG_time_2_and_EPG_time_3(self)


                                         elif program_stop_time >= epg_time_3:
                                             EPG_time_3(self)



                                     elif program_stop_time == epg_time_2:
                                         print "you are calling Epg_time_2"
                                         EPG_time_2(self)


                                     elif program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                                         EPG_time_1_and_EPG_time_2(self)


                                     elif program_stop_time > epg_time_2 and program_stop_time < epg_time_3:
                                         EPG_time_2_and_EPG_time_3(self)


                                     elif program_stop_time >= epg_time_3:
                                         EPG_time_3(self)




                         elif program_stop_time == epg_time_2:
                             print "here 9b"
                             program_id = program_button_1.getId()
                             self.program_id = list()
                             self.program_id.append(program_id)
                             self.program_end_time = list()
                             self.select_db_flag = True
                             self.single_program = True
                             get_programming_times(self)
                             #epg_times_stamp(self)
                             EPG_time_2(self)




                         elif program_stop_time > epg_time_1 and program_stop_time < epg_time_2:
                             print "here 10b"
                             program_id = program_button_1.getId()
                             self.program_id = list()
                             self.program_id.append(program_id)
                             self.program_end_time = list()
                             self.select_db_flag = True
                             self.single_program = True
                             get_programming_times(self)
                             #epg_times_stamp(self)
                             EPG_time_1_and_EPG_time_2(self)




                         elif program_stop_time > epg_time_2 and program_stop_time < epg_time_3:
                             print "here 11b"
                             self.program_id = list()
                             self.program_id.append(program_id)
                             self.program_end_time = list()
                             self.select_db_flag = True
                             self.single_program = True
                             get_programming_times(self)
                             #epg_times_stamp(self)
                             EPG_time_2_and_EPG_time_3(self)




                         elif program_stop_time == epg_time_3:
                             print "here 12b"
                             self.program_id = list()
                             self.program_id.append(program_id)
                             self.program_end_time = list()
                             self.select_db_flag = True
                             self.single_program = True
                             get_programming_times(self)
                             #epg_times_stamp(self)
                             EPG_time_3(self)




                         elif program_stop_time > epg_time_3:
                             print "here 13b"
                             self.program_id = list()
                             self.program_id.append(program_id)
                             self.program_end_time = list()
                             self.select_db_flag = True
                             self.single_program = True
                             get_programming_times(self)
                             #epg_times_stamp(self)
                             programs_width = program_width - 344
                             print "program_stop_time"
                             print program_stop_time
                             EPG_time_3(self)


                             if program_stop_time > epg_time_2 and program_stop_time < epg_time_3:
                                 print "you are in program_stop_time > epg_time_2 and program_stop_time < epg_time_3"
                                 EPG_time_2_and_EPG_time_3(self)





                     self.program_end_time = list()