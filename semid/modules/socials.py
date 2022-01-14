from bs4 import BeautifulSoup as bs
import requests, json, argparse
from semid.util.console import Console



def search(what):
    parser = argparse.ArgumentParser("SEMID")
    parser.add_argument("--username","-u", required=False)
    what = what.split()
    args = parser.parse_args(what)
    try:
        username = args.username
    except:
        raise TypeError()
    res = requests.get("https://linktr.ee/" + username)
    if res.status_code == 200:
        print("Linktree found!")
        soup = bs(res.text, "html.parser")
        socials = json.loads(soup.find("script", {"id": "__NEXT_DATA__"}).contents[0])["props"]["pageProps"]["account"]["socialLinks"]
        for s in socials:
            print(Console.color("Found: " + s["url"]))
    