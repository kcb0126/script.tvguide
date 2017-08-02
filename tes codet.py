 #DO NEED IT
                                                 if program_start_time < epg_time_2 

and program_stop_time > epg_time_3:
                                                     print 

"passed 1"

                                                     if program_stop_time < 

epg_time_2:
                                                         print "passed 4"
             

                                            program_finished = prog_stop_clock.split(':')

[1].replace('PM', '').replace('AM', '')

                                                         

if program_finished == '50':
                                                             print 

"you are working on this now chrissssssssssss 30"

                                                

             #OUTPUT THE PROGRAM REMAINING TIME HERE
                                             

                current_time = int(time.strftime("%M"))
                                          

                   prog_width = self.getControl(int(program_id)).getWidth()
                      

                                       prog_length = int(prog_width) / 11.4 - current_time
       

                                                      prog_length = str(prog_length)
             

                                                prog_length = prog_length.replace('.0', '')
      

                                                       prog_length = int(prog_length)
            

                                                 print "prog_length"
                             

                                print prog_length


                                                

             for program_time in program_remaining:
                                              

                   if int(program_time) <= 105:
                                                  

                   if int(prog_length) > 60 and int(prog_length) < 105:
                          

                                               if int(current_time) >= 30 and int(current_time) 

< 59:

                                                                             if prog_width 

== 1083:
                                                                                 print 

"let change the size in 90 mins program 1"
                                                       

                          prog_width = 741
                                                       

                          self.getControl(int(program_id)).setWidth(prog_width)
                  

                                                               getX = self.getControl(int

(program_id)).getX()
                                                                             

    getY = self.getControl(int(program_id)).getY()
                                               

                                  progId = list()
                                                

                                 posX = list()
                                                   

                              posY = list()


                                                      

                           for elem in programs_button:
                                          

                                           progId.append(elem.getId())
                           

                                                          posX.append(elem.getX())
               

                                                                      posY.append(elem.getY())
   

                                                                              progId = map(str, 

progId)
                                                                                 posX = 

map(str, posX)
                                                                                 

posY = map(str, posY)

                                                                            

     for pos_X, pos_Y, prog_id in zip(posX, posY, progId):
                                       

                                              if int(pos_X) >= 724 and int(pos_Y) == getY:
       

                                                                                  posX = int

(pos_X) - 348
                                                                                    

     posY = int(getY)
                                                                            

             self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                     

                                                        elif prog_width == 1368:
                 

                                                                print "let change the size in 90 

mins program 1"
                                                                                 

prog_width = 1026
                                                                                

 self.getControl(int(program_id)).setWidth(prog_width)
                                           

                                      getX = self.getControl(int(program_id)).getX()
             

                                                                    getY = self.getControl(int

(program_id)).getY()
                                                                             

    progId = list()
                                                                              

   posX = list()
                                                                                 

posY = list()


                                                                                 

for elem in programs_button:
                                                                     

                progId.append(elem.getId())
                                                      

                               posX.append(elem.getX())
                                          

                                           posY.append(elem.getY())
                              

                                                   progId = map(str, progId)
                     

                                                            posX = map(str, posX)
                

                                                                 posY = map(str, posY)

           

                                                                      for pos_X, pos_Y, prog_id 

in zip(posX, posY, progId):
                                                                      

               if int(pos_X) >= 724 and int(pos_Y) == getY:
                                      

                                                   posX = int(pos_X) - 348
                       

                                                                  posY = int(getY)
               

                                                                          self.getControl(int

(prog_id)).setPosition(int(posX), int(posY))


                                                     

elif program_stop_time > epg_time_2:
                                                         

program_finished = prog_stop_clock.split(':')[1].replace('PM', '').replace('AM', '')
             

                                            

                                                     

    if program_finished == '15':
                                                             if 

program_length == 691:
                                                                 print 

"bbc two"
                                                                 prog_width = 517
       

                                                          self.getControl(int

(program_id)).setWidth(prog_width)
                                                               

  next_program = int(program_id) + 1
                                                             

    next_program_width = self.getControl(int(next_program)).getWidth()
                           

                                      next_programs = int(next_program) + 1
                      

                                           next_programs_width = self.getControl(int

(next_programs)).getWidth()
                                                                 

previous_program = int(program_id) - 1
                                                           

      next_programs_width = self.getControl(int(previous_program)).getWidth()
                    

                                             getX = self.getControl(int(program_id)).getX()
      

                                                           getY = self.getControl(int

(program_id)).getY()
                                                                 progId = 

list()
                                                                 posX = list()
             

                                                    posY = list()

                                

                                 for elem in programs_button:
                                    

                                 progId.append(elem.getId())
                                     

                                posX.append(elem.getX())
                                         

                            posY.append(elem.getY())
                                             

                    progId = map(str, progId)
                                                    

             posX = map(str, posX)
                                                               

  posY = map(str, posY)

                                                                 for 

pos_X, pos_Y, prog_id in zip(posX, posY, progId):
                                                

                     if int(pos_X) >= 724 and int(pos_Y) == getY:
                                

                                         posX = int(pos_X) - 174
                                 

                                        posY = int(getY)
                                         

                                self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



  

                                               #DO NEED IT
                                       

          elif program_start_time > epg_time_1 and program_stop_time > epg_time_2:
               

                                      print "passed 2"



                                           

      #DO NEED IT
                                                 elif program_start_time == 

epg_time_1 and program_stop_time == epg_time_3:
                                                  

   print "passed 3"



                                                 #DO NEED IT
                  

                               if epg_time_1 < program_start_time and epg_time_2 == 

program_stop_time:
                                                     print "hello 

chrisssssssss 1"

                                                     if epg_time_1 < 

program_start_time:
                                                         program_finished = 

prog_stop_clock.split(':')[1].replace('PM', '').replace('AM', '')

                                

                         if program_finished == '00':
                                            

                 if program_length == 1197:
                                                      

           prog_width = 691
                                                                 

self.getControl(int(program_id)).setWidth(prog_width)


                                            

                 elif program_length == 691:
                                                     

            print "heloooooooooooooooooooo 1"
                                                    

             prog_width = 342
                                                                 

self.getControl(int(program_id)).setWidth(prog_width)
                                            

                     next_program = int(program_id) + 1
                                          

                       next_program_width = self.getControl(int(next_program)).getWidth()
        

                                                         next_programs = int(next_program) + 1
   

                                                              next_programs_width = 

self.getControl(int(next_programs)).getWidth()
                                                   

              previous_program = int(program_id) - 1
                                             

                    next_programs_width = self.getControl(int(previous_program)).getWidth()
      

                                                           getX = self.getControl(int

(program_id)).getX()
                                                                 getY = 

self.getControl(int(program_id)).getY()
                                                          

       progId = list()
                                                                 posX = 

list()
                                                                 posY = list()

             

                                                    for elem in programs_button:
                 

                                                    progId.append(elem.getId())
                  

                                                   posX.append(elem.getX())
                      

                                               posY.append(elem.getY())
                          

                                       progId = map(str, progId)
                                 

                                posX = map(str, posX)
                                            

                     posY = map(str, posY)

                                                       

          for pos_X, pos_Y, prog_id in zip(posX, posY, progId):
                                  

                                   if int(pos_X) >= 724 and int(pos_Y) == getY:
                  

                                                       posX = int(pos_X) - 348
                   

                                                      posY = int(getY)
                           

                                              self.getControl(int(prog_id)).setPosition(int

(posX), int(posY))


                                                                 if 

next_programs_width == 342:
                                                                     

if next_program_width == 285 and next_programs_width == 57:
                                      

                                   next_program_width = 278
                                      

                                   self.getControl(int(next_program)).setWidth

(next_program_width)
                                                                         

getY = self.getControl(int(next_program)).getY()
                                                 

                        progId = list()
                                                          

               posX = list()
                                                                     

    posY = list()

                                                                         for 

elem in programs_button:
                                                                         

    progId.append(elem.getId())
                                                                  

           posX.append(elem.getX())
                                                              

               posY.append(elem.getY())
                                                          

               progId = map(str, progId)
                                                         

                posX = map(str, posX)
                                                            

             posY = map(str, posY)


                                                               

          for pos_X, pos_Y, next_program in zip(posX, posY, progId):
                             

                                                if int(pos_X) > 952 and int(pos_Y) == getY:
      

                                                                           posX = int(pos_X) - 8
 

                                                                                posY = int(getY)
 

                                                                                self.getControl

(int(next_program)).setPosition(int(posX), int(posY))




                                            

                 elif program_length == 517:
                                                     

            prog_width = 342
                                                                 

self.getControl(int(program_id)).setWidth(prog_width)
                                            

                     getX = self.getControl(int(program_id)).getX()
                              

                                   getY = self.getControl(int(program_id)).getY()
                

                                                 progId = list()
                                 

                                posX = list()
                                                    

             posY = list()


                                                                 for 

elem in programs_button:
                                                                     

progId.append(elem.getId())
                                                                     

posX.append(elem.getX())
                                                                     

posY.append(elem.getY())
                                                                 progId 

= map(str, progId)
                                                                 posX = map

(str, posX)
                                                                 posY = map(str, 

posY)

                                                                 for pos_X, pos_Y, prog_id 

in zip(posX, posY, progId):
                                                                     

if int(pos_X) >= 724 and int(pos_Y) == getY:
                                                     

                    posX = int(pos_X) - 181
                                                      

                   posY = int(getY)
                                                              

           self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                       

                                      elif program_length == 798:
                                

                                 prog_width = 342
                                                

                 self.getControl(int(program_id)).setWidth(prog_width)



                           

                              elif program_finished >= '15' and program_finished <= '17':
        

                                                     if program_length == 691:
                   

                                              print "heloooooooooooooooooooo 2"
                  

                                               prog_width = 342
                                  

                               self.getControl(int(program_id)).setWidth(prog_width)
             

                                                    next_program = int(program_id) + 1
           

                                                      next_program_width = self.getControl(int

(next_program)).getWidth()
                                                                 

next_programs = int(next_program) + 1
                                                            

     next_programs_width = self.getControl(int(next_programs)).getWidth()
                        

                                         previous_program = int(program_id) - 1
                  

                                               next_programs_width = self.getControl(int

(previous_program)).getWidth()
                                                                 

getX = self.getControl(int(program_id)).getX()
                                                   

              getY = self.getControl(int(program_id)).getY()
                                     

                            progId = list()
                                                      

           posX = list()
                                                                 posY = 

list()

                                                                 for elem in 

programs_button:
                                                                     

progId.append(elem.getId())
                                                                     

posX.append(elem.getX())
                                                                     

posY.append(elem.getY())
                                                                 progId 

= map(str, progId)
                                                                 posX = map

(str, posX)
                                                                 posY = map(str, 

posY)

                                                                 for pos_X, pos_Y, prog_id 

in zip(posX, posY, progId):
                                                                     

if int(pos_X) >= 724 and int(pos_Y) == getY:
                                                     

                    posX = int(pos_X) - 348
                                                      

                   posY = int(getY)
                                                              

           self.getControl(int(prog_id)).setPosition(int(posX), int(posY))


                       

                                          if next_programs_width == 342:
                         

                                            if next_program_width == 285 and next_programs_width 

== 57:
                                                                         

next_program_width = 278
                                                                         

self.getControl(int(next_program)).setWidth(next_program_width)
                                  

                                       getY = self.getControl(int(next_program)).getY()
          

                                                               progId = list()
                   

                                                      posX = list()
                              

                                           posY = list()

                                         

                                for elem in programs_button:
                                     

                                        progId.append(elem.getId())
                              

                                               posX.append(elem.getX())
                          

                                                   posY.append(elem.getY())
                      

                                                   progId = map(str, progId)
                     

                                                    posX = map(str, posX)
                        

                                                 posY = map(str, posY)


                           

                                              for pos_X, pos_Y, next_program in zip(posX, posY, 

progId):
                                                                             if int

(pos_X) > 952 and int(pos_Y) == getY:
                                                            

                     posX = int(pos_X) - 8
                                                       

                          posY = int(getY)
                                                       

                          self.getControl(int(next_program)).setPosition(int(posX), int(posY))




   

                                                      elif program_finished == '30':
             

                                                if program_length == 517:
                        

                                         print "change size 2b"
                                  

                               prog_width = 342
                                                  

               self.getControl(int(program_id)).setWidth(prog_width)
                             

                                    getX = self.getControl(int(program_id)).getX()
               

                                                  getY = self.getControl(int(program_id)).getY()
 

                                                                progId = list()
                  

                                               posX = list()
                                     

                            posY = list()


                                                        

         for elem in programs_button:
                                                            

         progId.append(elem.getId())
                                                             

        posX.append(elem.getX())
                                                                 

    posY.append(elem.getY())
                                                                 

progId = map(str, progId)
                                                                 posX = 

map(str, posX)
                                                                 posY = map(str, 

posY)

                                                                 for pos_X, pos_Y, prog_id 

in zip(posX, posY, progId):
                                                                     

if int(pos_X) >= 724 and int(pos_Y) == getY:
                                                     

                    posX = int(pos_X) - 181
                                                      

                   posY = int(getY)
                                                              

           self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                       

                                      elif program_length == 691:
                                

                                 print "change size 2c"
                                          

                       prog_width = 342
                                                          

       self.getControl(int(program_id)).setWidth(prog_width)
                                     

                            next_program = int(program_id) + 1
                                   

                              next_program_width = self.getControl(int(next_program)).getWidth()
 

                                                                next_programs = int

(next_program) + 1
                                                                 

next_programs_width = self.getControl(int(next_programs)).getWidth()
                             

                                    previous_program = int(program_id) - 1
                       

                                          next_programs_width = self.getControl(int

(previous_program)).getWidth()
                                                                 

getX = self.getControl(int(program_id)).getX()
                                                   

              getY = self.getControl(int(program_id)).getY()
                                     

                            progId = list()
                                                      

           posX = list()
                                                                 posY = 

list()

                                                                 for elem in 

programs_button:
                                                                     

progId.append(elem.getId())
                                                                     

posX.append(elem.getX())
                                                                     

posY.append(elem.getY())
                                                                 progId 

= map(str, progId)
                                                                 posX = map

(str, posX)
                                                                 posY = map(str, 

posY)

                                                                 for pos_X, pos_Y, prog_id 

in zip(posX, posY, progId):
                                                                     

if int(pos_X) >= 724 and int(pos_Y) == getY:
                                                     

                    posX = int(pos_X) - 348
                                                      

                   posY = int(getY)
                                                              

           self.getControl(int(prog_id)).setPosition(int(posX), int(posY))

                       

                                          if next_programs_width == 342:
                         

                                            if next_program_width == 285 and next_programs_width 

== 57:
                                                                         

next_program_width = 278
                                                                         

self.getControl(int(next_program)).setWidth(next_program_width)
                                  

                                       getY = self.getControl(int(next_program)).getY()
          

                                                               progId = list()
                   

                                                      posX = list()
                              

                                           posY = list()

                                         

                                for elem in programs_button:
                                     

                                        progId.append(elem.getId())
                              

                                               posX.append(elem.getX())
                          

                                                   posY.append(elem.getY())
                      

                                                   progId = map(str, progId)
                     

                                                    posX = map(str, posX)
                        

                                                 posY = map(str, posY)


                           

                                              for pos_X, pos_Y, next_program in zip(posX, posY, 

progId):
                                                                             if int

(pos_X) > 952 and int(pos_Y) == getY:
                                                            

                     posX = int(pos_X) - 8
                                                       

                          posY = int(getY)
                                                       

                          self.getControl(int(next_program)).setPosition(int(posX), int(posY))




   

                                                  elif epg_time_3:
                               

                          program_finished = prog_stop_clock.split(':')[1].replace('PM', 

'').replace('AM', '')
                                                         print 

"helllllllllllllllllllllloooooooooooooooooooooooooooooooooooo"
                                   

                      self.getControl(int(program_id)).setVisible(False)


                         

                                if program_finished == '00':
                                     

                        if program_length == 798:
                                                

                 print "fuck you"
                                                                

 prog_width = 691
                                                                 

self.getControl(int(program_id)).setWidth(prog_width)
                                            

                     getX = self.getControl(int(program_id)).getX()
                              

                                   getY = self.getControl(int(program_id)).getY()
                

                                                 progId = list()
                                 

                                posX = list()
                                                    

             posY = list()


                                                                 for 

elem in programs_button:
                                                                     

progId.append(elem.getId())
                                                                     

posX.append(elem.getX())
                                                                     

posY.append(elem.getY())
                                                                 progId 

= map(str, progId)
                                                                 posX = map

(str, posX)
                                                                 posY = map(str, 

posY)

                                                                 for pos_X, pos_Y, prog_id 

in zip(posX, posY, progId):
                                                                     

if int(pos_X) >= 724 and int(pos_Y) == getY:
                                                     

                    posX = int(pos_X) - 113
                                                      

                   posY = int(getY)
                                                              

           self.getControl(int(prog_id)).setPosition(int(posX), int(posY))




                       

                                  elif program_finished == '30':
                                 

                            if program_length == 691:
                                            

                     print "hello chris 24"
                                                      

           prog_width = 342
                                                                 

self.getControl(int(program_id)).setWidth(prog_width)
                                            

                     next_program = int(program_id) + 1
                                          

                       next_program_width = self.getControl(int(next_program)).getWidth()
        

                                                         next_programs = int(next_program) + 1
   

                                                              next_programs_width = 

self.getControl(int(next_programs)).getWidth()
                                                   

              previous_program = int(program_id) - 1
                                             

                    next_programs_width = self.getControl(int(previous_program)).getWidth()
      

                                                           getX = self.getControl(int

(program_id)).getX()
                                                                 getY = 

self.getControl(int(program_id)).getY()
                                                          

       progId = list()
                                                                 posX = 

list()
                                                                 posY = list()

             

                                                    for elem in programs_button:
                 

                                                    progId.append(elem.getId())
                  

                                                   posX.append(elem.getX())
                      

                                               posY.append(elem.getY())
                          

                                       progId = map(str, progId)
                                 

                                posX = map(str, posX)
                                            

                     posY = map(str, posY)

                                                       

          for pos_X, pos_Y, prog_id in zip(posX, posY, progId):
                                  

                                   if int(pos_X) >= 724 and int(pos_Y) == getY:
                  

                                                       posX = int(pos_X) - 348
                   

                                                      posY = int(getY)
                           

                                              self.getControl(int(prog_id)).setPosition(int

(posX), int(posY))


                                                                         if 

next_programs_width == 342:
                                                                      

       if next_program_width == 285 and next_programs_width == 57:
                               

                                                  next_program_width = 278
                       

                                                          self.getControl(int

(next_program)).setWidth(next_program_width)
                                                     

                            getY = self.getControl(int(next_program)).getY()
                     

                                                            progId = list()
                      

                                                           posX = list()
                         

                                                        posY = list()

                            

                                                     for elem in programs_button:
                

                                                                     progId.append(elem.getId())
 

                                                                                    posX.append

(elem.getX())
                                                                                    

 posY.append(elem.getY())
                                                                        

         progId = map(str, progId)
                                                               

                  posX = map(str, posX)
                                                          

                       posY = map(str, posY)


                                                     

                            for pos_X, pos_Y, next_program in zip(posX, posY, progId):
           

                                                                          if int(pos_X) > 952 

and int(pos_Y) == getY:
                                                                          

               posX = int(pos_X) - 8
                                                             

                            posY = int(getY)
                                                     

                                    self.getControl(int(next_program)).setPosition(int(posX), 

int(posY))



                                                 #I DO NEED THIS
                       

                          elif program_start_time != epg_time_1 and program_stop_time < 

epg_time_3:
                                                     print "hello chris 2"


            

                                         if program_start_time < epg_time_1:
                     

                                    program_finished = prog_stop_clock.split(':')[1].replace

('PM', '').replace('AM', '')

                                                         if 

program_stop_time < epg_time_3:
                                                             if 

program_finished == '15':
                                                                 if 

program_length == 691:
                                                                     

prog_width = 517
                                                                     

self.getControl(int(program_id)).setWidth(prog_width)
                                            

                         getX = self.getControl(int(program_id)).getX()
                          

                                           getY = self.getControl(int(program_id)).getY()
        

                                                             progId = list()
                     

                                                posX = list()
                                    

                                 posY = list()


                                                   

                  for elem in programs_button:
                                                   

                      progId.append(elem.getId())
                                                

                         posX.append(elem.getX())
                                                

                         posY.append(elem.getY())
                                                

                     progId = map(str, progId)
                                                   

                  posX = map(str, posX)
                                                          

           posY = map(str, posY)

                                                                 

    for pos_X, pos_Y, prog_id in zip(posX, posY, progId):
                                        

                                 if int(pos_X) >= 724 and int(pos_Y) == getY:
                    

                                                         posX = int(pos_X) - 178
                 

                                                            posY = int(getY)
                     

                                                        self.getControl(int

(prog_id)).setPosition(int(posX), int(posY))



                                                     

        elif program_finished == '00':
                                                           

      if program_length == 517:
                                                                  

   prog_width = 342
                                                                     

self.getControl(int(program_id)).setWidth(prog_width)
                                            

                         getX = self.getControl(int(program_id)).getX()
                          

                                           getY = self.getControl(int(program_id)).getY()
        

                                                             progId = list()
                     

                                                posX = list()
                                    

                                 posY = list()


                                                   

                  for elem in programs_button:
                                                   

                      progId.append(elem.getId())
                                                

                         posX.append(elem.getX())
                                                

                         posY.append(elem.getY())
                                                

                     progId = map(str, progId)
                                                   

                  posX = map(str, posX)
                                                          

           posY = map(str, posY)

                                                                 

    for pos_X, pos_Y, prog_id in zip(posX, posY, progId):
                                        

                                 if int(pos_X) >= 724 and int(pos_Y) == getY:
                    

                                                         posX = int(pos_X) - 174
                 

                                                            posY = int(getY)
                     

                                                        self.getControl(int

(prog_id)).setPosition(int(posX), int(posY))



                                                     

            elif program_length == 691:
                                                          

           prog_width = 342
                                                                     

self.getControl(int(program_id)).setWidth(prog_width)
                                            

                         next_program = int(program_id) + 1
                                      

                               next_program_width = self.getControl(int(next_program)).getWidth

()
                                                                     next_programs = int

(next_program) + 1
                                                                     

next_programs_width = self.getControl(int(next_programs)).getWidth()
                             

                                        previous_program = int(program_id) - 1
                   

                                                  next_programs_width = self.getControl(int

(previous_program)).getWidth()
                                                                   

  getX = self.getControl(int(program_id)).getX()
                                                 

                    getY = self.getControl(int(program_id)).getY()
                               

                                      progId = list()
                                            

                         posX = list()
                                                           

          posY = list()

                                                                     for 

elem in programs_button:
                                                                         

progId.append(elem.getId())
                                                                      

   posX.append(elem.getX())
                                                                      

   posY.append(elem.getY())
                                                                     

progId = map(str, progId)
                                                                     

posX = map(str, posX)
                                                                     posY = 

map(str, posY)

                                                                     for pos_X, 

pos_Y, prog_id in zip(posX, posY, progId):
                                                       

                  if int(pos_X) >= 724 and int(pos_Y) == getY:
                                   

                                          posX = int(pos_X) - 348
                                

                                             posY = int(getY)
                                    

                                         self.getControl(int(prog_id)).setPosition(int(posX), 

int(posY))


                                                                     if 

next_programs_width == 342:
                                                                      

   if next_program_width == 285 and next_programs_width == 57:
                                   

                                          next_program_width = 278
                               

                                              self.getControl(int(next_program)).setWidth

(next_program_width)
                                                                             

getY = self.getControl(int(next_program)).getY()
                                                 

                            progId = list()
                                                      

                       posX = list()
                                                             

                posY = list()

                                                                    

         for elem in programs_button:
                                                            

                     progId.append(elem.getId())
                                                 

                                posX.append(elem.getX())
                                         

                                        posY.append(elem.getY())
                                 

                                            progId = map(str, progId)
                            

                                                 posX = map(str, posX)
                           

                                                  posY = map(str, posY)


                          

                                                   for pos_X, pos_Y, next_program in zip(posX, 

posY, progId):
                                                                                 

if int(pos_X) > 952 and int(pos_Y) == getY:
                                                      

                               posX = int(pos_X) - 8
                                             

                                        posY = int(getY)
                                         

                                            self.getControl(int(next_program)).setPosition(int

(posX), int(posY))



                                                             elif 

program_stop_time < epg_time_2:
                                                                 

if program_finished == '50':
                                                                     

if program_length == 627:
                                                                        

 prog_width = 228
                                                                         

self.getControl(int(program_id)).setWidth(prog_width)
                                            

                             getX = self.getControl(int(program_id)).getX()
                      

                                                   getY = self.getControl(int(program_id)).getY

()
                                                                         progId = list()
       

                                                                  posX = list()
                  

                                                       posY = list()


                             

                                            for elem in programs_button:
                         

                                                    progId.append(elem.getId())
                  

                                                           posX.append(elem.getX())
              

                                                               posY.append(elem.getY())
          

                                                               progId = map(str, progId)
         

                                                                posX = map(str, posX)
            

                                                             posY = map(str, posY)

               

                                                          for pos_X, pos_Y, prog_id in zip(posX, 

posY, progId):
                                                                             if 

int(pos_X) >= 724 and int(pos_Y) == getY:
                                                        

                         posX = int(pos_X) - 400
                                                 

                                posY = int(getY)
                                                 

                                self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



  

                                                       elif program_stop_time == epg_time_2:
     

                                                        program_finished = 

prog_stop_clock.split(':')[1].replace('PM', '').replace('AM', '')
                                

                             print "program_id"
                                                  

           print (program_id)

                                                             #error 

ValueError: invalid literal for int() with base 10: on line 2274
                                 

                            if program_finished == '00':
                                         

                        current_time = int(time.strftime("%M"))
                                  

                               prog_widths = self.getControl(int(program_id)).getWidth()
         

                                                        print prog_widths
                        

                                         prog_length = int(prog_widths) / 11.4 - current_time
    

                                                             prog_length = str(prog_length)
      

                                                           prog_length = prog_length.replace

('.0', '')
                                                                 prog_length = int

(prog_length)


                                                                 for program_time 

in program_remaining:
                                                                     if 

int(program_time) <= 30:
                                                                         

if int(current_time) >= 30 and int(current_time) < 59:

                                           

                                  if prog_widths == 1026:
                                        

                                         prog_widths = 342
                                       

                                          self.getControl(int(program_id)).setWidth(prog_widths)
 

                                                                                getX = 

self.getControl(int(program_id)).getX()
                                                          

                       getY = self.getControl(int(program_id)).getY()
                            

                                                     progId = list()
                             

                                                    posX = list()
                                

                                                 posY = list()


                                   

                                              for elem in programs_button:
                       

                                                              progId.append(elem.getId())
        

                                                                             posX.append

(elem.getX())
                                                                                    

 posY.append(elem.getY())
                                                                        

         progId = map(str, progId)
                                                               

                  posX = map(str, posX)
                                                          

                       posY = map(str, posY)

                                                     

                            for pos_X, pos_Y, prog_id in zip(posX, posY, progId):
                

                                                                     if int(pos_X) >= 724 and 

int(pos_Y) == getY:
                                                                              

           posX = int(pos_X) - 684
                                                               

                          posY = int(getY)
                                                       

                                  self.getControl(int(prog_id)).setPosition(int(posX), int

(posY))



                                                                             elif 

prog_width == 1368:
                                                                              

   print "let change the size in 90 mins program 1"
                                              

                                   prog_width = 342
                                              

                                   self.getControl(int(program_id)).setWidth(prog_width)
         

                                                                        getX = self.getControl

(int(program_id)).getX()
                                                                         

        getY = self.getControl(int(program_id)).getY()
                                           

                                      progId = list()
                                            

                                     posX = list()
                                               

                                  posY = list()


                                                  

                               for elem in programs_button:
                                      

                                               progId.append(elem.getId())
                       

                                                              posX.append(elem.getX())
           

                                                                          posY.append(elem.getY

())
                                                                                 progId = 

map(str, progId)
                                                                                 

posX = map(str, posX)
                                                                            

     posY = map(str, posY)

                                                                       

          for pos_X, pos_Y, prog_id in zip(posX, posY, progId):
                                  

                                                   if int(pos_X) >= 1024 and int(pos_Y) == getY:
 

                                                                                        posX = 

int(pos_X) - 1026
                                                                                

         posY = int(getY)
                                                                        

                 self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                 

                                                        elif int(current_time) >= 30 and int

(current_time) < 59:

                                                                             

if prog_width == 1026:
                                                                           

      prog_width = 342
                                                                           

      self.getControl(int(program_id)).setWidth(prog_width)
                                      

                                           getX = self.getControl(int(program_id)).getX()
        

                                                                         getY = self.getControl

(int(program_id)).getY()
                                                                         

        progId = list()
                                                                          

       posX = list()
                                                                             

    posY = list()


                                                                                

 for elem in programs_button:
                                                                    

                 progId.append(elem.getId())
                                                     

                                posX.append(elem.getX())
                                         

                                            posY.append(elem.getY())
                             

                                                    progId = map(str, progId)
                    

                                                             posX = map(str, posX)
               

                                                                  posY = map(str, posY)

          

                                                                       for pos_X, pos_Y, prog_id 

in zip(posX, posY, progId):
                                                                      

               if int(pos_X) >= 724 and int(pos_Y) == getY:
                                      

                                                   posX = int(pos_X) - 684
                       

                                                                  posY = int(getY)
               

                                                                          self.getControl(int

(prog_id)).setPosition(int(posX), int(posY))



                                                     

                        elif prog_width == 1368:
                                                 

                                print "let change the size in 90 mins program 1"
                 

                                                                prog_width = 342
                 

                                                                self.getControl(int

(program_id)).setWidth(prog_width)
                                                               

                  getX = self.getControl(int(program_id)).getX()
                                 

                                                getY = self.getControl(int(program_id)).getY()
   

                                                                              progId = list()
    

                                                                             posX = list()
       

                                                                          posY = list()


          

                                                                       for elem in 

programs_button:
                                                                                 

    progId.append(elem.getId())
                                                                  

                   posX.append(elem.getX())
                                                      

                               posY.append(elem.getY())
                                          

                                       progId = map(str, progId)
                                 

                                                posX = map(str, posX)
                            

                                                     posY = map(str, posY)

                       

                                                          for pos_X, pos_Y, prog_id in zip(posX, 

posY, progId):
                                                                                   

  if int(pos_X) >= 1024 and int(pos_Y) == getY:
                                                  

                                       posX = int(pos_X) - 1026
                                  

                                                       posY = int(getY)
                          

                                                               self.getControl(int

(prog_id)).setPosition(int(posX), int(posY))



                                                     

    elif program_stop_time < epg_time_2:
                                                         

    print "epg pass 1"
                                                             if 

program_start_time < epg_time_1:
                                                                 

program_finished = prog_stop_clock.split(':')[1].replace('PM', '').replace('AM', '')
             

                                                    print "epg pass 2"

                           

                                      if program_stop_time < epg_time_2:
                         

                                            print "epg pass 3"
                                   

                                  if program_finished == '50':
                                   

                                      print "epg pass 4"
                                         

                                if program_length == 691:
                                        

                                     print "epg pass 5"
                                          

                                   prog_width = 228
                                              

                               self.getControl(int(program_id)).setWidth(prog_width)
             

                                                                getX = self.getControl(int

(program_id)).getX()
                                                                             

getY = self.getControl(int(program_id)).getY()
                                                   

                          progId = list()
                                                        

                     posX = list()
                                                               

              posY = list()


                                                                      

       for elem in programs_button:
                                                              

                   progId.append(elem.getId())
                                                   

                              posX.append(elem.getX())
                                           

                                      posY.append(elem.getY())
                                   

                                          progId = map(str, progId)
                              

                                               posX = map(str, posX)
                             

                                                posY = map(str, posY)

                            

                                                 for pos_X, pos_Y, prog_id in zip(posX, posY, 

progId):
                                                                                 if int

(pos_X) >= 724 and int(pos_Y) == getY:
                                                           

                          posX = int(pos_X) - 463
                                                

                                     posY = int(getY)
                                            

                                         self.getControl(int(prog_id)).setPosition(int(posX), 

int(posY))



                                                                         elif 

program_length == 342:
                                                                           

  print "epg pass 6"
                                                                             

prog_width = 228
                                                                             

self.getControl(int(program_id)).setWidth(prog_width)
                                            

                                 getX = self.getControl(int(program_id)).getX()
                  

                                                           getY = self.getControl(int

(program_id)).getY()
                                                                             

progId = list()
                                                                             posX 

= list()
                                                                             posY = 

list()


                                                                             for elem in 

programs_button:
                                                                                 

progId.append(elem.getId())
                                                                      

           posX.append(elem.getX())
                                                              

                   posY.append(elem.getY())
                                                      

                       progId = map(str, progId)
                                                 

                            posX = map(str, posX)
                                                

                             posY = map(str, posY)

                                               

                              for pos_X, pos_Y, prog_id in zip(posX, posY, progId):
              

                                                                   if int(pos_X) >= 724 and int

(pos_Y) == getY:
                                                                                 

    posX = int(pos_X) - 114
                                                                      

               posY = int(getY)
                                                                  

                   self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



               

                                      elif program_start_time >= epg_time_2:
                     

                                    program_finished = prog_stop_clock.split(':')[1].replace

('PM', '').replace('AM', '')

                                                         if 

program_finished == '00':
                                                             if 

program_length == 1197:
                                                                 print 

"you are working on this now chrissssssssssss 1"
                                                 

                #prog_width = 691
                                                                

 #self.getControl(int(program_id)).setWidth(prog_width)


                                          

                   elif program_length == 570:
                                                   

              print "you are working on this now chrissssssssssss 2"
                             

                                    prog_width = 342
                                             

                    self.getControl(int(program_id)).setWidth(prog_width)
                        

                                         


                                                        

     elif program_length == 691:
                                                                 

print "you are working on this now chrissssssssssss 3"
                                           

                      prog_width = 342
                                                           

      self.getControl(int(program_id)).setWidth(prog_width)
                                      

                           self.getControl(int(program_id)).setVisible(False)



                    

                                     elif program_finished == '10':
                              

                               if program_length == 691:
                                         

                        print "you are working on this now chrissssssssssss 4"
                   

                                              prog_width = 456
                                   

                              self.getControl(int(program_id)).setWidth(prog_width)



              

                                           elif program_finished == '15':
                        

                                     print "you are working on this now chrissssssssssss 5"


      

                                                       if program_length == 691:
                 

                                                print "you are working on this now 

chrissssssssssss 6"
                                                                 prog_width = 

517
                                                                 self.getControl(int

(program_id)).setWidth(prog_width)
                                                               

  getX = self.getControl(int(program_id)).getX()
                                                 

                getY = self.getControl(int(program_id)).getY()
                                   

                              progId = list()
                                                    

             posX = list()
                                                                 posY 

= list()


                                                                 for elem in 

programs_button:
                                                                     

progId.append(elem.getId())
                                                                     

posX.append(elem.getX())
                                                                     

posY.append(elem.getY())
                                                                 progId 

= map(str, progId)
                                                                 posX = map

(str, posX)
                                                                 posY = map(str, 

posY)

                                                                 for pos_X, pos_Y, prog_id 

in zip(posX, posY, progId):
                                                                     

if int(pos_X) >= 724 and int(pos_Y) == getY:
                                                     

                    posX = int(pos_X) - 174
                                                      

                   posY = int(getY)
                                                              

           self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                       

                                      elif program_length == 517:
                                

                                 prog_width = 171
                                                

                 print "you are working on this now chrissssssssssss 7"
                          

                                       #self.getControl(int(program_id)).setWidth(prog_width)
    

                                                             self.getControl(int

(program_id)).setVisible(False)



                                                         elif 

program_finished == '20':
                                                             if 

program_length == 691:
                                                                 

prog_width = 570
                                                                 print "you are 

working on this now chrissssssssssss 8"
                                                          

       self.getControl(int(program_id)).setWidth(prog_width)



                                     

                    elif program_finished == '30':
                                               

              if program_length == 517:
                                                          

       prog_width = 342
                                                                 print 

"you are working on this now chrissssssssssss 9"
                                                 

                self.getControl(int(program_id)).setWidth(prog_width)



                            

                             elif program_finished == '50':
                                      

                       if program_length == 627:
                                                 

                prog_width = 285
                                                                 

print "you are working on this now chrissssssssssss 10"
                                          

                       self.getControl(int(program_id)).setWidth(prog_width)



                     

                                        elif program_length == 342:
                              

                                   prog_width = 228
                                              

                   print "you are working on this now chrissssssssssss 11"
                       

                                          self.getControl(int(program_id)).setWidth(prog_width)



  

                                                       elif program_finished == '55':
            

                                                 if program_length == 691:
                       

                                          prog_width = 634
                                       

                          print "you are working on this now chrissssssssssss 12"
                

                                                 self.getControl(int(program_id)).setWidth

(prog_width)





                                                 #I DO NEED THIS
                     

                            elif program_start_time > epg_time_2 and program_stop_time < 

epg_time_3:
                                                     print "hello chris 3"
            

                                         if program_length == 517:
                               

                          print "you are working on this now chrissssssssssss 14"


                

                                     elif program_length == 691:
                                 

                        print "you are working on this now chrissssssssssss 15"
                  

                                       #prog_width = 342
                                         

                #self.getControl(int(program_id)).setWidth(prog_width)
                           

                              #next_program_id = int(program_id) + 1
                             

                            #getX = self.getControl(int(next_program_id)).getX()
                 

                                        #getY = self.getControl(int(next_program_id)).getY()
     

                                                    #print "getX"
                                

                         #print getX
                                                         

#print "getY"
                                                         #print getY


                

                                     elif program_length == 1197:
                                

                         prog_width = 513
                                                        

 print "you are working on this now chrissssssssssss 16"
                                         

                #self.getControl(int(program_id)).setWidth(prog_width)



                           

                      elif program_start_time < epg_time_2 and program_stop_time < epg_time_3:
   

                                                  if program_start_time < epg_time_3:
            

                                             program_finished = prog_stop_clock.split(':')

[1].replace('PM', '').replace('AM', '')
                                                         

print "you are working on this now chrissssssssssss 18as"


                                        

                 if program_start_time < epg_time_1:
                                             

                program_finished = prog_stop_clock.split(':')[1].replace('PM', '').replace('AM', 

'')
                                                             print "disable the button 2"
     

                                                        self.getControl(int

(program_id)).setVisible(False)


                                                             if 

program_stop_time == epg_time_2:
                                                                 

if program_finished == '30':
                                                                     

if program_length == 517:
                                                                        

 prog_width = 342
                                                                         

self.getControl(int(program_id)).setWidth(prog_width)
                                            

                             getX = self.getControl(int(program_id)).getX()
                      

                                                   getY = self.getControl(int(program_id)).getY

()
                                                                         progId = list()
       

                                                                  posX = list()
                  

                                                       posY = list()


                             

                                            for elem in programs_button:
                         

                                                    progId.append(elem.getId())
                  

                                                           posX.append(elem.getX())
              

                                                               posY.append(elem.getY())
          

                                                               progId = map(str, progId)
         

                                                                posX = map(str, posX)
            

                                                             posY = map(str, posY)

               

                                                          for pos_X, pos_Y, prog_id in zip(posX, 

posY, progId):
                                                                             if 

int(pos_X) >= 724 and int(pos_Y) == getY:
                                                        

                         posX = int(pos_X) - 175
                                                 

                                posY = int(getY)
                                                 

                                self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



  

                                                                   elif program_length == 691:
   

                                                                      prog_width = 342
           

                                                              self.getControl(int

(program_id)).setWidth(prog_width)
                                                               

          getX = self.getControl(int(program_id)).getX()
                                         

                                getY = self.getControl(int(program_id)).getY()
                   

                                                      progId = list()
                            

                                             posX = list()
                                       

                                  posY = list()


                                                  

                       for elem in programs_button:
                                              

                               progId.append(elem.getId())
                                       

                                      posX.append(elem.getX())
                                   

                                          posY.append(elem.getY())
                               

                                          progId = map(str, progId)
                              

                                           posX = map(str, posX)
                                 

                                        posY = map(str, posY)

                                    

                                     for pos_X, pos_Y, prog_id in zip(posX, posY, progId):
       

                                                                      if int(pos_X) >= 724 and 

int(pos_Y) == getY:
                                                                              

   posX = int(pos_X) - 342
                                                                       

          posY = int(getY)
                                                                       

          self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                        

                                     elif program_stop_time > epg_time_1:
                        

                                         print "test it"
                                         

                        
                                                                 



        

                                         #DO NEED IT
                                             

    elif epg_time_1 > program_start_time and program_stop_time > epg_time_2:
                     

                                print "you are working on this now chrissssssssssss 26"

          

                                           if program_start_time < epg_time_1:

                   

                                      if program_stop_time > epg_time_3:
                         

                                    program_finished = prog_stop_clock.split(':')[1].replace

('PM', '').replace('AM', '')

                                                             if 

program_finished == '00':
                                                                 print 

"you are working on this now chrissssssssssss 30"
                                                

                 #OUTPUT THE PROGRAM REMAINING TIME HERE
                                         

                        current_time = int(time.strftime("%M"))
                                  

                               prog_width = self.getControl(int(program_id)).getWidth()
          

                                                       prog_length = int(prog_width) / 11.4 - 

current_time
                                                                 prog_length = str

(prog_length)
                                                                 prog_length = 

prog_length.replace('.0', '')
                                                                 

prog_length = int(prog_length)
                                                                 

print "prog_length"
                                                                 print type

(prog_length)


                                                                 if int

(prog_length) > 60 and int(prog_length) < 120:
                                                   

                  print "the program has passed on if statement 1"


                               

                                      if int(current_time) >= 30 and int(current_time) < 59:

     

                                                                    if prog_width == 1026:
       

                                                                      print "let change the size 

in 90 mins program 1"
                                                                            

 prog_width = 691
                                                                             

self.getControl(int(program_id)).setWidth(prog_width)
                                            

                                 getX = self.getControl(int(program_id)).getX()
                  

                                                           getY = self.getControl(int

(program_id)).getY()
                                                                             

progId = list()
                                                                             posX 

= list()
                                                                             posY = 

list()


                                                                             for elem in 

programs_button:
                                                                                 

progId.append(elem.getId())
                                                                      

           posX.append(elem.getX())
                                                              

                   posY.append(elem.getY())
                                                      

                       progId = map(str, progId)
                                                 

                            posX = map(str, posX)
                                                

                             posY = map(str, posY)

                                               

                              for pos_X, pos_Y, prog_id in zip(posX, posY, progId):
              

                                                                   if int(pos_X) >= 724 and int

(pos_Y) == getY:
                                                                                 

    posX = int(pos_X) - 348
                                                                      

               posY = int(getY)
                                                                  

                   self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



               

                                                          elif prog_width == 1368:
               

                                                              print "let change the size in 90 

mins program 1"
                                                                             

prog_width = 1026
                                                                             

self.getControl(int(program_id)).setWidth(prog_width)
                                            

                                 getX = self.getControl(int(program_id)).getX()
                  

                                                           getY = self.getControl(int

(program_id)).getY()
                                                                             

progId = list()
                                                                             posX 

= list()
                                                                             posY = 

list()


                                                                             for elem in 

programs_button:
                                                                                 

progId.append(elem.getId())
                                                                      

           posX.append(elem.getX())
                                                              

                   posY.append(elem.getY())
                                                      

                       progId = map(str, progId)
                                                 

                            posX = map(str, posX)
                                                

                             posY = map(str, posY)

                                               

                              for pos_X, pos_Y, prog_id in zip(posX, posY, progId):
              

                                                                   if int(pos_X) >= 724 and int

(pos_Y) == getY:
                                                                                 

    posX = int(pos_X) - 348
                                                                      

               posY = int(getY)
                                                                  

                   self.getControl(int(prog_id)).setPosition(int(posX), int(posY))




               

                                                  #CALCULATE THE CURRENT TIME FROM 12AM TO 6AM
   

                                                              if program_length == 570:
          

                                                           prog_width = 228
                      

                                               self.getControl(int(program_id)).setWidth

(prog_width)


                                                                 elif program_length 

== 912:
                                                                     prog_width = 570
     

                                                                self.getControl(int

(program_id)).setWidth(prog_width)


                                                               

  elif program_length == 1254:
                                                                   

  prog_width = 912
                                                                     

self.getControl(int(program_id)).setWidth(prog_width)


                                            

                     elif program_length == 1596:
                                                

                     prog_width = 1254
                                                           

          self.getControl(int(program_id)).setWidth(prog_width)


                                  

                               elif program_length == 1938:
                                      

                               prog_width = 1596
                                                 

                    self.getControl(int(program_id)).setWidth(prog_width)



                        

                                     elif program_finished == '05':
                              

                                   if program_length == 741:
                                     

                                prog_width = 399
                                                 

                    self.getControl(int(program_id)).setWidth(prog_width)
                        

                                             getX = self.getControl(int(program_id)).getX()
      

                                                               getY = self.getControl(int

(program_id)).getY()
                                                                     progId 

= list()
                                                                     posX = list()
       

                                                              posY = list()


                      

                                               for elem in programs_button:
                      

                                                   progId.append(elem.getId())
                   

                                                      posX.append(elem.getX())
                   

                                                      posY.append(elem.getY())
                   

                                                  progId = map(str, progId)
                      

                                               posX = map(str, posX)
                             

                                        posY = map(str, posY)

                                    

                                 for pos_X, pos_Y, prog_id in zip(posX, posY, progId):
           

                                                              if int(pos_X) >= 724 and int

(pos_Y) == getY:
                                                                             

posX = int(pos_X) - 348
                                                                          

   posY = int(getY)
                                                                             

self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                                  

                       elif program_stop_time > epg_time_2:
                                      

                       print "you are working on here now 1"
                                     

                        program_finished = prog_stop_clock.split(':')[1].replace('PM', 

'').replace('AM', '')

                                                             if 

program_finished == '15':
                                                                 if 

program_length == 691:
                                                                     

prog_width = 517
                                                                     

self.getControl(int(program_id)).setWidth(prog_width)
                                            

                         next_program = int(program_id) + 1
                                      

                               next_program_width = self.getControl(int(next_program)).getWidth

()
                                                                     next_programs = int

(next_program) + 1
                                                                     

next_programs_width = self.getControl(int(next_programs)).getWidth()
                             

                                        previous_program = int(program_id) - 1
                   

                                                  next_programs_width = self.getControl(int

(previous_program)).getWidth()
                                                                   

  getX = self.getControl(int(program_id)).getX()
                                                 

                    getY = self.getControl(int(program_id)).getY()
                               

                                      progId = list()
                                            

                         posX = list()
                                                           

          posY = list()

                                                                     for 

elem in programs_button:
                                                                         

progId.append(elem.getId())
                                                                      

   posX.append(elem.getX())
                                                                      

   posY.append(elem.getY())
                                                                     

progId = map(str, progId)
                                                                     

posX = map(str, posX)
                                                                     posY = 

map(str, posY)

                                                                     for pos_X, 

pos_Y, prog_id in zip(posX, posY, progId):
                                                       

                  if int(pos_X) >= 724 and int(pos_Y) == getY:
                                   

                                          posX = int(pos_X) - 178
                                

                                             posY = int(getY)
                                    

                                         self.getControl(int(prog_id)).setPosition(int(posX), 

int(posY))



                                                         elif program_stop_time == 

epg_time_3:
                                                             program_finished = 

prog_stop_clock.split(':')[1].replace('PM', '').replace('AM', '')
                                

                             print "you are working on here now 2"

                               

                              if program_finished == '00':
                                       

                          #OUTPUT THE PROGRAM REMAINING TIME HERE
                                

                                 current_time = int(time.strftime("%M"))
                         

                                        prog_width = self.getControl(int(program_id)).getWidth()
 

                                                                prog_length = int(prog_width) / 

11.4 - current_time
                                                                 prog_length 

= str(prog_length)
                                                                 prog_length = 

prog_length.replace('.0', '')
                                                                 

prog_length = int(prog_length)
                                                                 

print "current_time"
                                                                 print 

current_time


                                                                 for program_time in 

program_remaining:


                                                                     if int

(program_time) <= 60:
                                                                         if 

int(current_time) >= 0 and int(current_time) < 30:

                                               

                              if prog_width == 1026:
                                             

                                    prog_width = 691
                                             

                                    self.getControl(int(program_id)).setWidth(prog_width)
        

                                                                         getX = self.getControl

(int(program_id)).getX()
                                                                         

        getY = self.getControl(int(program_id)).getY()
                                           

                                      progId = list()
                                            

                                     posX = list()
                                               

                                  posY = list()


                                                  

                               for elem in programs_button:
                                      

                                               progId.append(elem.getId())
                       

                                                              posX.append(elem.getX())
           

                                                                          posY.append(elem.getY

())
                                                                                 progId = 

map(str, progId)
                                                                                 

posX = map(str, posX)
                                                                            

     posY = map(str, posY)

                                                                       

          for pos_X, pos_Y, prog_id in zip(posX, posY, progId):
                                  

                                                   if int(pos_X) >= 724 and int(pos_Y) == getY:
  

                                                                                       posX = 

int(pos_X) - 335
                                                                                 

        posY = int(getY)
                                                                         

                self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                  

                                                           elif prog_width == 1368:
              

                                                                   print "let change the size in 

90 mins program 1"
                                                                               

  prog_width = 691
                                                                               

  self.getControl(int(program_id)).setWidth(prog_width)
                                          

                                       getX = self.getControl(int(program_id)).getX()
            

                                                                     getY = self.getControl(int

(program_id)).getY()
                                                                             

    progId = list()
                                                                              

   posX = list()
                                                                                 

posY = list()


                                                                                 

for elem in programs_button:
                                                                     

                progId.append(elem.getId())
                                                      

                               posX.append(elem.getX())
                                          

                                           posY.append(elem.getY())
                              

                                                   progId = map(str, progId)
                     

                                                            posX = map(str, posX)
                

                                                                 posY = map(str, posY)

           

                                                                      for pos_X, pos_Y, prog_id 

in zip(posX, posY, progId):
                                                                      

               if int(pos_X) >= 1024 and int(pos_Y) == getY:
                                     

                                                    posX = int(pos_X) - 677
                      

                                                                   posY = int(getY)
              

                                                                           self.getControl(int

(prog_id)).setPosition(int(posX), int(posY))
                                                     

            
                                                                 
                    

                                             
                                                    

                     elif int(current_time) >= 30 and int(current_time) < 59:

                    

                                                         if prog_width == 1026:
                  

                                                               prog_width = 691
                  

                                                               self.getControl(int

(program_id)).setWidth(prog_width)
                                                               

                  getX = self.getControl(int(program_id)).getX()
                                 

                                                getY = self.getControl(int(program_id)).getY()
   

                                                                              progId = list()
    

                                                                             posX = list()
       

                                                                          posY = list()


          

                                                                       for elem in 

programs_button:
                                                                                 

    progId.append(elem.getId())
                                                                  

                   posX.append(elem.getX())
                                                      

                               posY.append(elem.getY())
                                          

                                       progId = map(str, progId)
                                 

                                                posX = map(str, posX)
                            

                                                     posY = map(str, posY)

                       

                                                          for pos_X, pos_Y, prog_id in zip(posX, 

posY, progId):
                                                                                   

  if int(pos_X) >= 724 and int(pos_Y) == getY:
                                                   

                                      posX = int(pos_X) - 335
                                    

                                                     posY = int(getY)
                            

                                                             self.getControl(int

(prog_id)).setPosition(int(posX), int(posY))



                                                     

                        elif prog_width == 1368:
                                                 

                                print "let change the size in 90 mins program 1"
                 

                                                                prog_width = 691
                 

                                                                self.getControl(int

(program_id)).setWidth(prog_width)
                                                               

                  getX = self.getControl(int(program_id)).getX()
                                 

                                                getY = self.getControl(int(program_id)).getY()
   

                                                                              progId = list()
    

                                                                             posX = list()
       

                                                                          posY = list()


          

                                                                       for elem in 

programs_button:
                                                                                 

    progId.append(elem.getId())
                                                                  

                   posX.append(elem.getX())
                                                      

                               posY.append(elem.getY())
                                          

                                       progId = map(str, progId)
                                 

                                                posX = map(str, posX)
                            

                                                     posY = map(str, posY)

                       

                                                          for pos_X, pos_Y, prog_id in zip(posX, 

posY, progId):
                                                                                   

  if int(pos_X) >= 1024 and int(pos_Y) == getY:
                                                  

                                       posX = int(pos_X) - 677
                                   

                                                      posY = int(getY)
                           

                                                              self.getControl(int

(prog_id)).setPosition(int(posX), int(posY))
                                                     

            
                                                                 
                    

                                             
                                                    

             
                                                                 
                   

                                              
                                                   

              
                                                                 if program_length 

== 798:
                                                                     prog_width = 691
     

                                                                self.getControl(int

(program_id)).setWidth(prog_width)
                                                               

      getX = self.getControl(int(program_id)).getX()
                                             

                        getY = self.getControl(int(program_id)).getY()
                           

                                          progId = list()
                                        

                             posX = list()
                                                       

              posY = list()


                                                                     

for elem in programs_button:
                                                                     

    progId.append(elem.getId())
                                                                  

       posX.append(elem.getX())
                                                                  

       posY.append(elem.getY())
                                                                  

   progId = map(str, progId)
                                                                     

posX = map(str, posX)
                                                                     posY = 

map(str, posY)

                                                                     for pos_X, 

pos_Y, prog_id in zip(posX, posY, progId):
                                                       

                  if int(pos_X) >= 724 and int(pos_Y) == getY:
                                   

                                          posX = int(pos_X) - 107
                                

                                             posY = int(getY)
                                    

                                         self.getControl(int(prog_id)).setPosition(int(posX), 

int(posY))



                                                     elif program_stop_time > 

epg_time_1:
                                                         print "hey arsehole"
         

                                            
                                                     
                                                     
                                            

         
                                                     
                                   

                  elif program_stop_time > epg_time_3:
                                           

              program_finished = prog_stop_clock.split(':')[1].replace('PM', '').replace('AM', 

'')

                                                         if program_finished == '00':
         

                                                    print "you are working on this now 

chrissssssssssss 30"

                                                             #OUTPUT THE 

PROGRAM REMAINING TIME HERE
                                                             
         

                                                    
                                             

                current_time = int(time.strftime("%M"))
                                          

                   print current_time
                                                            

 prog_width = self.getControl(int(program_id)).getWidth()
                                        

                     prog_length = int(prog_width) / 11.4 - current_time
                         

                                    prog_length = str(prog_length)
                               

                              prog_length = prog_length.replace('.0', '')
                        

                                     prog_length = int(prog_length)
                              

                               print "prog_length"
                                               

              print prog_length


                                                             if 

int(prog_length) == '90':
                                                                 if 

prog_width == 1368:
                                                                     print 

"let change the size in 90 mins program 1"



                                                 elif 

program_start_time < epg_time_1 and program_stop_time == epg_time_3:
                             

                        if program_stop_time == epg_time_3:
                                      

                   program_finished = prog_stop_clock.split(':')[1].replace('PM', '').replace

('AM', '')
                                                         print "you are working on 

here now 2"

                                                         if program_finished == '00':
 

                                                            if program_length == 1197:
           

                                                      prog_width = 691
                           

                                      self.getControl(int(program_id)).setWidth(prog_width)
      

                                                           getX = self.getControl(int

(program_id)).getX()
                                                                 getY = 

self.getControl(int(program_id)).getY()
                                                          

       progId = list()
                                                                 posX = 

list()
                                                                 posY = list()


             

                                                    for elem in programs_button:
                 

                                                    progId.append(elem.getId())
                  

                                                   posX.append(elem.getX())
                      

                                               posY.append(elem.getY())
                          

                                       progId = map(str, progId)
                                 

                                posX = map(str, posX)
                                            

                     posY = map(str, posY)

                                                       

          for pos_X, pos_Y, prog_id in zip(posX, posY, progId):
                                  

                                   if int(pos_X) >= 724 and int(pos_Y) == getY:
                  

                                                       posX = int(pos_X) - 506
                   

                                                      posY = int(getY)
                           

                                              self.getControl(int(prog_id)).setPosition(int

(posX), int(posY))



                                                 if program_start_time > 

epg_time_1 and program_stop_time < epg_time_2:
                                                   

  print "hello chris 4"
                                                     if program_length == 

342:
                                                         print "you are working on this now 

chrissssssssssss 17"
                                                         #self.getControl

(int(program_id)).setVisible(False)


                                                     #DO NOT 

ADD 45 MINS (PROGRAM_LENGTH = 517) AS IT IS NO NEEDED 
                                           

          elif program_length == 691:
                                                         

print "you are working on this now chrissssssssssss 19"
                                          

               #prog_width = 342
                                                         

#self.getControl(int(program_id)).setWidth(prog_width)
                                           

              #next_program_id = int(program_id) + 1
                                             

            #getX = self.getControl(int(next_program_id)).getX()
                                 

                        #getY = self.getControl(int(next_program_id)).getY()
                     

                                    #print "getX"
                                                

         #print getX
                                                         #print "getY"
       

                                                  #print getY


                                    

                 elif program_length == 517:
                                                     

    print "you are working on this now chrissssssssssss 20"
                                      

                   #prog_width = 171
                                                         

#self.getControl(int(program_id)).setWidth(prog_width)
                                           

              self.getControl(int(program_id)).setVisible(False)




                                 

                elif program_start_time < epg_time_1 and program_stop_time < epg_time_2:
         

                                            print "epg time 7"


                                   

                  if program_stop_time < epg_time_2:
                                             

            program_finished = prog_stop_clock.split(':')[1].replace('PM', '').replace('AM', '')

 

                                                        if program_finished == '20':
             

                                                print "epg pass 8"

                               

                              if program_length == 691:
                                          

                       print "epg pass 9"
                                                        

         prog_width = 228
                                                                 

self.getControl(int(program_id)).setWidth(prog_width)
                                            

                     getX = self.getControl(int(program_id)).getX()
                              

                                   getY = self.getControl(int(program_id)).getY()
                

                                                 progId = list()
                                 

                                posX = list()
                                                    

             posY = list()


                                                                 for 

elem in programs_button:
                                                                     

progId.append(elem.getId())
                                                                     

posX.append(elem.getX())
                                                                     

posY.append(elem.getY())
                                                                 progId 

= map(str, progId)
                                                                 posX = map

(str, posX)
                                                                 posY = map(str, 

posY)

                                                                 for pos_X, pos_Y, prog_id 

in zip(posX, posY, progId):
                                                                     

if int(pos_X) >= 724 and int(pos_Y) == getY:
                                                     

                    posX = int(pos_X) - 463
                                                      

                   posY = int(getY)
                                                              

           self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                       

                                      elif program_length == 342:
                                

                                 print "epg pass 10"
                                             

                    prog_width = 228
                                                             

    self.getControl(int(program_id)).setWidth(prog_width)
                                        

                         getX = self.getControl(int(program_id)).getX()
                          

                                       getY = self.getControl(int(program_id)).getY()
            

                                                     progId = list()
                             

                                    posX = list()
                                                

                 posY = list()


                                                                 

for elem in programs_button:
                                                                     

progId.append(elem.getId())
                                                                     

posX.append(elem.getX())
                                                                     

posY.append(elem.getY())
                                                                 progId 

= map(str, progId)
                                                                 posX = map

(str, posX)
                                                                 posY = map(str, 

posY)

                                                                 for pos_X, pos_Y, prog_id 

in zip(posX, posY, progId):
                                                                     

if int(pos_X) >= 724 and int(pos_Y) == getY:
                                                     

                    posX = int(pos_X) - 114
                                                      

                   posY = int(getY)
                                                              

           self.getControl(int(prog_id)).setPosition(int(posX), int(posY))




                       

                          elif program_start_time < epg_time_1 and program_stop_time > 

epg_time_2:

                                                     if program_stop_time > 

epg_time_2:
                                                         program_finished = 

prog_stop_clock.split(':')[1].replace('PM', '').replace('AM', '')

                                

                         if program_finished == '50':
                                            

                 if program_length == 691:
                                                       

          print "helooooooooooooooooooooooooooooo chris"
                                         

                        prog_width = 577
                                                         

        self.getControl(int(program_id)).setWidth(prog_width)
                                    

                             getX = self.getControl(int(program_id)).getX()
                      

                                           getY = self.getControl(int(program_id)).getY()
        

                                                         progId = list()
                         

                                        posX = list()
                                            

                     posY = list()


                                                               

  for elem in programs_button:
                                                                   

  progId.append(elem.getId())
                                                                    

 posX.append(elem.getX())
                                                                     

posY.append(elem.getY())
                                                                 progId 

= map(str, progId)
                                                                 posX = map

(str, posX)
                                                                 posY = map(str, 

posY)

                                                                 for pos_X, pos_Y, prog_id 

in zip(posX, posY, progId):
                                                                     

if int(pos_X) >= 724 and int(pos_Y) == getY:
                                                     

                    posX = int(pos_X) - 114
                                                      

                   posY = int(getY)
                                                              

           self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                       

                          #DO NEED IT
                                                 if 

program_start_time > epg_time_1 and program_stop_time > epg_time_3:
                              

                       if program_start_time < epg_time_2:
                                       

                  program_finished = prog_stop_clock.split(':')[1].replace('PM', '').replace

('AM', '')

                                                         #NEED TO FIND OUT WHAT TIME 

if program_finished == '??':
                                                         if 

program_length == 1368:
                                                             prog_width = 

1026
                                                             self.getControl(int

(program_id)).setWidth(prog_width)
                                                             

getX = self.getControl(int(program_id)).getX()
                                                   

          getY = self.getControl(int(program_id)).getY()
                                         

                    progId = list()
                                                             

posX = list()
                                                             posY = list()


          

                                                   for elem in programs_button:
                  

                                               progId.append(elem.getId())
                       

                                          posX.append(elem.getX())
                               

                                  posY.append(elem.getY())
                                       

                      progId = map(str, progId)
                                                  

           posX = map(str, posX)
                                                             

posY = map(str, posY)

                                                             for pos_X, 

pos_Y, prog_id in zip(posX, posY, progId):
                                                       

          if int(pos_X) >= 724 and int(pos_Y) == getY:
                                           

                          posX = int(pos_X) - 348
                                                

                     posY = int(getY)
                                                            

         self.getControl(int(prog_id)).setPosition(int(posX), int(posY))
                         

                                            self.getControl(int(prog_id)).setPosition(int(posX), 

int(posY))




                                                 #DO NEED IT
                           

                      if epg_time_1 == program_start_time and program_stop_time > epg_time_3:
    

                                                 print "you are working on this now a!"
          

                                           
                                                     

if program_stop_time > epg_time_3:
                                                         

program_finished = prog_stop_clock.split(':')[1].replace('PM', '').replace('AM', '')
             

                                            print "you are working on this now b!"

               

                                          if program_finished == '00':
                           

                                  print "you are working on this now chrissssssssssss 30"

        

                                                     #OUTPUT THE PROGRAM REMAINING TIME HERE
     

                                                        current_time = int(time.strftime("%M"))
  

                                                           prog_width = self.getControl(int

(program_id)).getWidth()
                                                             prog_length 

= int(prog_width) / 11.4 - current_time
                                                          

   prog_length = str(prog_length)
                                                             

prog_length = prog_length.replace('.0', '')
                                                      

       prog_length = int(prog_length)
                                                            

 print "prog_length"
                                                             print 

prog_length


                                                             for program_time in 

program_remaining:
                                                                     if int

(program_time) <= 60:
                                                                         if 

int(prog_length) > 60 and int(prog_length) < 120:
                                                

                             if int(current_time) >= 30 and int(current_time) < 59:

              

                                                                   if prog_width == 1026:
        

                                                                             print "let change 

the size in 90 mins program 1"
                                                                   

                  prog_width = 691
                                                               

                      self.getControl(int(program_id)).setWidth(prog_width)
                      

                                                               getX = self.getControl(int

(program_id)).getX()
                                                                             

        getY = self.getControl(int(program_id)).getY()
                                           

                                          progId = list()
                                        

                                             posX = list()
                                       

                                              posY = list()


                                      

                                               for elem in programs_button:
                      

                                                                   progId.append(elem.getId())
   

                                                                                      

posX.append(elem.getX())
                                                                         

                posY.append(elem.getY())
                                                         

                            progId = map(str, progId)
                                            

                                         posX = map(str, posX)
                                   

                                                  posY = map(str, posY)

                          

                                                           for pos_X, pos_Y, prog_id in zip

(posX, posY, progId):
                                                                            

             if int(pos_X) >= 724 and int(pos_Y) == getY:
                                        

                                                     posX = int(pos_X) - 348
                     

                                                                        posY = int(getY)
         

                                                                                    

self.getControl(int(prog_id)).setPosition(int(posX), int(posY))



                                  

                                               elif prog_width == 1368:
                          

                                                           print "let change the size in 90 mins 

program 1"
                                                                                     

prog_width = 1026
                                                                                

     self.getControl(int(program_id)).setWidth(prog_width)
                                       

                                              getX = self.getControl(int(program_id)).getX()
     

                                                                                getY = 

self.getControl(int(program_id)).getY()
                                                          

                           progId = list()
                                                       

                              posX = list()
                                                      

                               posY = list()


                                                     

                                for elem in programs_button:
                                     

                                                    progId.append(elem.getId())
                  

                                                                       posX.append(elem.getX())
  

                                                                                       

posY.append(elem.getY())
                                                                         

            progId = map(str, progId)
                                                            

                         posX = map(str, posX)
                                                   

                                  posY = map(str, posY)

                                          

                                           for pos_X, pos_Y, prog_id in zip(posX, posY, progId):
 

                                                                                        if int

(pos_X) >= 724 and int(pos_Y) == getY:
                                                           

                                  posX = int(pos_X) - 348
                                        

                                                     posY = int(getY)
                            

                                                                 self.getControl(int

(prog_id)).setPosition(int(posX), int(posY))