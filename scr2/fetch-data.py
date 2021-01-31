import http_post_get as crawler



#def urlopen_retry(hyperlink):
#	for i in range(999):
#		try:
#			response = urllib.request.urlopen(hyperlink)
#			return response.read().decode('utf-8')
#		except:
#			time.sleep(2)
			

def data_miner(gen):
	for row in cr.execute("SELECT id, name, parent_id, anak_no, generation, link FROM anak WHERE generation = %d ORDER BY id ASC;" % gen):
		tid, tname, tparent_id, tanak_no, tgeneration, tlink = row
		
		#text_tree = urlopen_retry(tlink + '=tree')
		text_tree = crawler.http_get(tlink + '=tree')
		
		m1 = re.findall(r'<tr><td width="7%">&nbsp;</td><td colspan=5><a href="(.+?)">(.+?)</a>', text_tree, re.MULTILINE | re.IGNORECASE | re.DOTALL)
		if not m1:
			continue
		
		#text_pick = urlopen_retry(tlink + '=pick_man')
		text_pick = crawler.http_get(tlink + '=pick_man')
		m2 = re.findall(r'(.*?)Istri:(.*?)Anak:(.*?)Boru:(.*)', text_pick, re.MULTILINE | re.IGNORECASE | re.DOTALL)
		
		suami_pick, istri_pick, anak_pick, boru_pick = m2[0]
		alamat = re.findall(r'<td width="20%" align=left nowrap>&nbsp;(.*?)</td>', suami_pick, re.MULTILINE | re.IGNORECASE | re.DOTALL)[0]
		
		# istri INSERT
		istri = re.findall(r'<td width="50%" align=left nowrap>&nbsp;(\d+?)&nbsp;&nbsp;(.+?)</td>\n<td width="20%" align=left nowrap>&nbsp;(.*?)</td>', istri_pick, re.MULTILINE | re.IGNORECASE | re.DOTALL)
		if istri:
			for k in istri:
				istri_no, istri_name, istri_alamat = k
				istri_no = int(istri_no)
				suami_id = tid
				print('istri:', istri_name, suami_id, istri_no)
				cw.execute("INSERT INTO istri (name, suami_id, istri_no) VALUES (?, ?, ?);",
					 (istri_name, suami_id, istri_no) )
				
		
		# boru INSERT
		boru = re.findall(r'<td width="50%" align=left nowrap>&nbsp;(\d+?)&nbsp;&nbsp;(.*?)</td>\n<td width="20%" align=left nowrap>&nbsp;(.*?)</td>', boru_pick, re.MULTILINE | re.IGNORECASE | re.DOTALL)
		if boru:
			for b in boru:
				boru_no, boru_name, boru_alamat = b
				boru_no = int(boru_no)
				parent_id = tid
				print('boru: ', boru_name, parent_id, boru_no, tgeneration+1, boru_alamat)
				cw.execute("INSERT INTO boru (name, parent_id, boru_no, generation, alamat) VALUES (?, ?, ?, ?, ?);",
					(boru_name, parent_id, boru_no, tgeneration+1, boru_alamat) )
				
		
		# anak INSERT
		anak_no = 1
		for i in m1:
			name = i[1]
			#link = re.sub(r'=pick_man', r'=tree', i[0], 0, re.MULTILINE | re.IGNORECASE | re.DOTALL)
			link = re.sub('=pick_man', '', i[0], 0, re.MULTILINE | re.IGNORECASE | re.DOTALL)
			
			# anak INSERT
			print('suami:', name, tid, anak_no, tgeneration+1, alamat)
			cw.execute("INSERT INTO anak (name, parent_id, anak_no, generation, alamat, link) VALUES (?, ?, ?, ?, ?, ?);",
				(name, tid, anak_no, tgeneration+1, alamat, link) )
			anak_no += 1
			

##########################
# main program

db = '..\\Database\\sirait-link.sqlite'

conn = sqlite3.connect(db)
cr = conn.cursor()	# read cursor
cw = conn.cursor()	# write cursor

for gen in range(1, 50):
	data_miner(gen)
	conn.commit()

conn.close()

#################


text_res = crawler.http_get('http://bing.com')
print(text_res)

