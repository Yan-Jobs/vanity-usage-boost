import requests
import httpx
import time
from user_agent import generate_user_agent
import socket
import urllib3
import os
import random

os.environ["PYTHONHTTPSVERIFY"] = "0"
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from urllib3.exceptions import InsecureRequestWarning
ssl=False
verify_ssl=False
ssl_context=False
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


print("""
 __      __  ______   __    __           _____   ______   _______    ______  
/  \    /  |/      \ /  \  /  |         /     | /      \ /       \  /      \ 
$$  \  /$$//$$$$$$  |$$  \ $$ |         $$$$$ |/$$$$$$  |$$$$$$$  |/$$$$$$  |
 $$  \/$$/ $$ |__$$ |$$$  \$$ |            $$ |$$ |  $$ |$$ |__$$ |$$ \__$$/ 
  $$  $$/  $$    $$ |$$$$  $$ |       __   $$ |$$ |  $$ |$$    $$< $$      \ 
   $$$$/   $$$$$$$$ |$$ $$ $$ |      /  |  $$ |$$ |  $$ |$$$$$$$  | $$$$$$  |
    $$ |   $$ |  $$ |$$ |$$$$ |      $$ \__$$ |$$ \__$$ |$$ |__$$ |/  \__$$ |
    $$ |   $$ |  $$ |$$ | $$$ |      $$    $$/ $$    $$/ $$    $$/ $$    $$/ 
    $$/    $$/   $$/ $$/   $$/        $$$$$$/   $$$$$$/  $$$$$$$/   $$$$$$/  
                                                                             
                                                                             
                                                                             
""")
code = input(f"Server vanity: ")
swid = input(f"Server ID: ")
stoken = input(f"Token:  ")
swurl = f"https://discord.com/api/v9/users/@me/guilds/{swid}"




def get_params():
  params = [ f"", f"?inputValue={code}&with_counts=true&with_expiration=true", "?with_counts=true&with_expiration=true"]
  return params
params = get_params()





def get_apiz():
  apiz = [ "v6", "v7"]
  return apiz
apiz = get_apiz()







def get_apis():
  apis = [ "v6", "v7", "v8", "v9"]
  return apis 
apis = get_apis()





def get_apis2():
  apis2 = [ "v6", "v7", "v8", "v9", "v10"]
  return apis2
apis2 = get_apis2()



def get_guids():
  guids = [
f"discord.com/api/{random.choice(apiz)}/invite/{code}{random.choice(params)}",f"ptb.discord.com/api/{random.choice(apiz)}/invite/{code}{random.choice(params)}",f"canary.discord.com/api/{random.choice(apiz)}/invite/{code}{random.choice(params)}",
f"discordapp.com/api/{random.choice(apiz)}/invite/{code}{random.choice(params)}",f"ptb.discordapp.com/api/{random.choice(apiz)}/invite/{code}{random.choice(params)}",f"canary.discordapp.com/api/{random.choice(apiz)}/invite/{code}{random.choice(params)}",





f"discord.com/api/{random.choice(apis2)}/invites/{code}{random.choice(params)}",f"ptb.discord.com/api/{random.choice(apis2)}/invites/{code}{random.choice(params)}",f"canary.discord.com/api/{random.choice(apis2)}/invites/{code}{random.choice(params)}",
f"discordapp.com/api/{random.choice(apis)}/invites/{code}{random.choice(params)}",f"ptb.discordapp.com/api/{random.choice(apis)}/invites/{code}{random.choice(params)}",f"canary.discordapp.com/api/{random.choice(apis)}/invites/{code}{random.choice(params)}",
]
  return guids   
guids = get_guids()





s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('discord.com', 443))



s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect(('ptb.discord.com', 443))



s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s3.connect(('canary.discord.com', 443))





payload = json.dumps({
  "session_id": f"https://{random.choice(guids)}"
})



payloads = json.dumps({
  "lurking": False
})





s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s4.connect(('discordapp.com', 443))



s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s5.connect(('canary.discordapp.com', 443))



s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s6.connect(('ptb.discordapp.com', 443))



while True:
    guids = get_guids()
    url = f"https://{random.choice(guids)}"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        'Content-Type': "application/json",
        'authority': "discord.com",
        'accept-language': "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        'authorization': f"{stoken}",
        'cache-control': "no-cache",
        'origin': "https://discord.com",
        'pragma': "no-cache",
        'referer': "https://discord.com/channels/@me/",
        'sec-ch-ua': "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"",
        'sec-ch-ua-mobile': "?1",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-fetch-dest': "empty",
        'sec-fetch-mode': "cors",
        'sec-fetch-site': "same-origin",
        'x-context-properties': "eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjEwODg4OTIyNjkxNzM2ODIyMzciLCJsb2NhdGlvbl9jaGFubmVsX2lkIjoiMTA5NDM2MjE4NzU0MTI2MjQ1NiIsImxvY2F0aW9uX2NoYW5uZWxfdHlwZSI6MH0=",
        'x-debug-options': "bugReporterEnabled",
        'x-discord-locale': "en-US",
        'x-discord-timezone': "America/New_York",
        'x-super-properties': "eyJvcyI6IkFuZHJvaWQiLCJicm93c2VyIjoiQW5kcm9pZCBDaHJvbWUiLCJkZXZpY2UiOiJBbmRyb2lkIiwic3lzdGVtX2xvY2FsZSI6InRyIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBLKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTIwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI2MTk3MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
    }

    response = requests.get(url, headers=headers, verify=False)
    cookies = dict(response.cookies)
    time.sleep(0.2)
    response2 = httpx.post(url, headers=headers, data=payload, verify=False, cookies=cookies)
    response3 = requests.delete(swurl, headers=headers, data=payloads, verify=False, cookies=cookies)

    try:
        response_data = response2.json()
        if response2.status_code == 200:
            print("[+] Success! Made  by: github.com/Yan-Jobs")
        else:
            error_message = response_data.get("message", "Unknown error")
            print(f"[-] Error: {error_message}")
    except json.JSONDecodeError:
        print("[-] Error: Response is not valid JSON")
    
    time.sleep(3)


