--[[
local http=require'socket.http'
--body,c,l,h = http.request('http://www.technocraft.org/sirait/tarombo.cgi?lyr=5;wfe=Y;dgh=L;man=100273;act=tree')
body,c,l,h = http.request('https://www.bing.com/search?q=DAOKO%E3%80%8E%E3%83%80%E3%82%A4%E3%82%B9%E3%82%AD+with+TeddyLoid%E3%80%8F&pc=MOZI&form=MOZSBR')

print(c,l,h)


print(body)
]]





print('ダ from lua')

