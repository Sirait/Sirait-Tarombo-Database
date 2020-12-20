
import sys, re

#sys.stdout.reconfigure(encoding='utf-8')

#print('ダイスキ')
#print("Ûnicöde ダイスキ 日本語 الْأَبْجَدِيَّة الْعَرَبِيَّة")
#sys.stdout.write("Ûnicöde ダイスキ 日本語 الْأَبْجَدِيَّة الْعَرَبِيَّة\n")


import urllib.request, re, sqlite3, time

def urlopen_retry(hyperlink):
	for i in range(999):
		try:
			response = urllib.request.urlopen(hyperlink)
			return response.read().decode('utf-8')
		except:
			time.sleep(2)
			#print('except')




text_res = urlopen_retry('http://www.technocraft.org/sirait/tarombo.cgi?lyr=5;wfe=Y;dgh=L;clan=Sirait;man=100389;act=pick_man')




m2 = re.findall(r'(.*?)Istri:(.*?)Anak:(.*?)Boru:(.*)', text_res, re.MULTILINE | re.IGNORECASE | re.DOTALL)

suami_pick, istri_pick, anak_pick, boru_pick = m2[0]
alamat = re.findall(r'<td width="20%" align=left nowrap>&nbsp;(.*?)</td>', suami_pick, re.MULTILINE | re.IGNORECASE | re.DOTALL)[0]

#anak_no, anak_name, anak_alamat = re.findall(r'<td width="50%" align=left nowrap>&nbsp;(\d+?)&nbsp;&nbsp;(.*?)</td>\n<td width="20%" align=left nowrap>&nbsp;(.*?)</td>', anak_pick, re.MULTILINE | re.IGNORECASE | re.DOTALL)
istri = re.findall(r'<td width="50%" align=left nowrap>&nbsp;(\d*?)&nbsp;&nbsp;(.*?)</td>\n<td width="20%" align=left nowrap>&nbsp;(.*?)</td>', istri_pick, re.MULTILINE | re.IGNORECASE | re.DOTALL)
for k in istri:
	istri_no, istri_name, istri_alamat = k
	#suami_id = cw.lastrowid
	#print(k)

#print(boru_pick)
boru = re.findall(r'<td width="50%" align=left nowrap>&nbsp;(\d+?)&nbsp;&nbsp;(.*?)</td>\n<td width="20%" align=left nowrap>&nbsp;(.*?)</td>', boru_pick, re.MULTILINE | re.IGNORECASE | re.DOTALL)
for b in boru:
	boru_no, boru_name, boru_alamat = b
	#parent_id = cw.lastrowid
	#print(b)

	
#print(text_res)

