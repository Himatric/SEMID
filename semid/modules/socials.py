from bs4 import BeautifulSoup as bs
import requests, json, argparse
import semid
from semid.util.console import Console
from semid.util.search import Google, WeLeak
from fake_headers import Headers

def search(what):
    parser = argparse.ArgumentParser("SEMID")
    parser.add_argument("--username","-u", required=False)
    parser.add_argument("--weleak", "-w", action="store_true", required=False)
    what = what.split()
    args = parser.parse_args(what)
    try:
        username:str = args.username
    except:
        print("a")
        raise TypeError()
    res = requests.get("https://linktr.ee/" + username)
    if res.status_code == 200:
        print("Linktree found!")
        soup = bs(res.text, "html.parser")
        socials = json.loads(soup.find("script", {"id": "__NEXT_DATA__"}).contents[0])["props"]["pageProps"]["account"]["socialLinks"]
        for s in socials:
            print(Console.color("Found: " + s["url"]))
    socials:list = json.loads(open("./semid/socials.json", "r").read())
    for social in socials:
        headers = Headers("chrome").generate()
        res = requests.get(social["url"].replace("{name}", username), headers=headers)
        if social["type"] == "status" and res.status_code != social["status"]:
            print(Console.color("Found: " +social["url"].replace("{name}", username)))
        elif social["type"] == "message":
            msg = social["msg"]
            if msg not in res.text:
                print(Console.color("Found: " + social["url"].replace("{name}", username)))
    for url, title in Google.search(f'site:youtube.com "{username}"', 0):
        if "/channel/" in url and username.lower() in title.lower():
            print(Console.color("Found: " + url))
        elif "/channel/" in url:
            print(Console.green(f"Possible Connection: {url} - {title}"))
    for url, title in Google.search(f'site:twitter.com "{username}"', 0):
        if url.endswith(username.lower()):
            print(Console.color("Found: " + url))
    for url, title in Google.search(f'site:namemc.com "{username}"', 0):
        if username.lower() in url and "/profile/" in url:
            print(Console.color("Found: " + url))
    if args.weleak == True and semid.__app__.config["WeLeakInfo"] != "" and len(username) > 4:
        print(Console.color(WeLeak.search(username)))

def searchsyntax():
    text = """
--username | -u <username>

Example: use socials::search -u Xhemyd"""
    return text
    