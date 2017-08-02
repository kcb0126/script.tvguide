import datetime
import time
import xbmc
import xbmcgui
import os
from sqlite3 import dbapi2 as database

def update_database(self):
     profilePath = xbmc.translatePath(os.path.join('special://userdata/addon_data/script.tvguide', 'source.db'))
     conn1 = database.connect(profilePath)
     cur1 = conn1.cursor()

     for program_id in self.program_id:
         cur.execute('SELECT channel, program_id FROM programs WHERE program_id=?;', (program_id))
         data = cur.fetchone()

         if data is not None:
             cur.execute('UPDATE programs SET program_id=? WHERE program_id=?', ['', ['3001'])
             cur.execute('UPDATE programs SET program_id=? WHERE program_id=?', ['3001', '3002'])
             cur.execute('UPDATE programs SET program_id=? WHERE program_id=?', ['3002', '3003'])
             cur.execute('UPDATE programs SET program_id=? WHERE program_id=?', ['3003', '3004'])
             cur.execute('UPDATE programs SET program_id=? WHERE program_id=?', ['3004', '3005'])
             cur.execute('UPDATE programs SET program_id=? WHERE program_id=?', ['3005', '3006'])
             cur.execute('UPDATE programs SET program_id=? WHERE program_id=?', ['3006', '3007'])
             cur.execute('UPDATE programs SET program_id=? WHERE program_id=?', ['3007', '3008'])
             cur.execute('UPDATE programs SET program_id=? WHERE program_id=?', ['3008', '3009'])
             cur.execute('UPDATE programs SET program_id=? WHERE program_id=?', ['3009', '3010'])
             cur.execute('UPDATE programs SET program_id=? WHERE program_id=?', ['3010', ''])
             con.commit()