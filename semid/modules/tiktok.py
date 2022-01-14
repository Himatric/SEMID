import requests, json, argparse, time
from bs4 import BeautifulSoup
from semid.util.console import Console
from semid.util.search import Regex, WeLeak
import semid
def search(args:str):
    parser = argparse.ArgumentParser(prog="SEMID")
    parser.add_argument("--username", "-u", required=False)
    parser.add_argument("--weleak", "-w", required=False, action="store_true")
    argsArr = args.split()
    try:
        arg = parser.parse_args(argsArr)
    except:
        raise TypeError
    # try:
    #     naInd = argsArr.index("--username")
    # except:
    #     try:
    #         naInd = argsArr.index("-u")
    #     except:
    #         raise TypeError
    username = arg.username
    base = "https://www.tiktok.com/@"
    res = requests.get(base + username)
    if res.status_code != 200:
        return print(Console.red("ERR! Invalid username!"))
    stringdata = ""
    soup = BeautifulSoup(res.text, "html.parser")
    soup2 = BeautifulSoup(res.text, "html.parser")
    bio = soup.find("h2", {'data-e2e': "user-bio"}).contents[0]
    stringdata += f'{bio};'
    alldata = json.loads(soup2.find("script", id="sigi-persisted-data").contents[0].split(";window['SIGI_RETRY'")[0].replace("window['SIGI_STATE']=", ""))
    del alldata["AppContext"]
    del alldata["SEO"]
    del alldata['SharingMeta']
    del alldata["ItemList"]
    del alldata["I18n"]
    stats = False
    for z in alldata["ItemModule"]:
        video = alldata["ItemModule"][z]
        stringdata += video["desc"] +";"
        stickers = video["stickersOnItem"]
        for sticker in stickers:
            stringdata += sticker["stickerText"][0]
    for z in alldata["UserModule"]["stats"]:
        stats = alldata["UserModule"]["stats"][z]
        nickname = alldata["UserModule"]["users"][z]["nickname"]
        bio = alldata["UserModule"]["users"][z]["signature"]
        link = alldata["UserModule"]["users"][z]["bioLink"]["link"]
    c = Console.red("|")
    text = f"""{c} Username: {username} , Nickname: {nickname}
{c} Bio:       {bio}
{c} Linked:    {link}
{c} Followers: {stats["followerCount"]}
{c} Following: {stats["followingCount"]}
{c} Likes:     {stats["heart"]}
{c} Videos:    {stats["videoCount"]}
""" 
    searched = Regex.search(stringdata.replace("\n", ""))
    text += searched[0]
    if arg.weleak == True and semid.__app__.config["WeLeakInfo"] != "":
        emails = searched[1]
        for email in emails:
            text += WeLeak.search(email)
            time.sleep(0.5)
    return print(text)

def searchsyntax():
    text = """
--username | -u <username>
--weleak   | -w  searches found emails on WeLeakInfo (requires WeLeakInfo api key)

Example: use tiktok::search -u tiktok"""
    return text