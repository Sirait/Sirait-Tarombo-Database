import sqlite3, os

db = '..\\Database\\sirait-link.sqlite'

if os.path.isfile(db):
	os.remove(db)

conn = sqlite3.connect(db)
c = conn.cursor()

# Create table
c.execute("CREATE TABLE anak (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, parent_id INTEGER, anak_no INTEGER, generation INTEGER, alamat TEXT, link TEXT);")
c.execute("INSERT INTO anak (name, parent_id, anak_no, generation, alamat, link) VALUES ('Raja Toga Sirait alias Sirait', 0, 2, 1, '', 'http://www.technocraft.org/sirait/tarombo.cgi?lyr=5;wfe=Y;dgh=L;clan=Sirait;man=100273;act');")

c.execute("CREATE TABLE boru (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, parent_id INTEGER, boru_no INTEGER, generation INTEGER, alamat TEXT);")

c.execute("CREATE TABLE istri (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, suami_id INTEGER, istri_no INTEGER);")


conn.commit()
conn.close()



