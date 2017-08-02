                             elif int(pos_X) == 375 and int(prog_width) == 1368:
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
                                     one_hour_half = str(self.getControl(346).getLabel())
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
                                     programs_width = 0


                                     if program_stop_time > epg_time_3:
                                         if program_stop_minutes == '05':
                                             programs_width = 677
                                             self.getControl(int(prog_id)).setWidth(int(programs_width))
                                             nextprogram = int(prog_id) + 1
                                             pos_X = self.getControl(int(nextprogram)).getX()

                                             if int(pos_X) != 1093:
                                                 pos_Y = self.getControl(int(nextprogram)).getY()
                                                 self.getControl(int(nextprogram)).setPosition(1124, int(pos_Y))
                                                 self.getControl(int(nextprogram)).setVisible(True)