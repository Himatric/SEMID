import requests, bs4, re, json
from semid.util.console import Console
import semid

class Google:
    @staticmethod
    def search(what:str, i:int) -> list:
        i += 1
        if i > 10: return [(None, None)]
        """ DuckDuckGo search """
        def req(what):
            res = requests.post("https://lite.duckduckgo.com/lite/", headers={
                    "accept": "*/*",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
                    "referer": "https://lite.duckduckgo.com/",
                    "origin": "https://lite.duckduckgo.com"
                }, data={
                    "q": what,
                    "dt": None,
                    "kl": None
                })
            return res

        res = req(what)
        if res.status_code == 403:
            req("nice cat")
            return Google.search(what, i)

        soup = bs4.BeautifulSoup(res.text, "html.parser")

        return [(found["href"], found.text) for found in soup.find_all("a", {"rel": "nofollow"})]
class Regex:
    @staticmethod
    def search(stringdata:str) -> str:
        c = Console.red("|")
        email = "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"
        discord = """[a-z_A-Z0-9_#!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]{1,32}#[0-9]{4}"""
        phone = "^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$"
        eml = re.compile(email)
        dcrd = re.compile(discord)
        phn = re.compile(phone)
        emails = eml.findall(stringdata)
        discords = dcrd.findall(stringdata)
        phones = phn.findall(stringdata)
        returnstring = ""
        for mail in emails:
            returnstring += f"""{c} Possible Email: {mail}\n"""
        for tag in discords:
            returnstring += f"""{c} Possible Discord: {tag}\n"""
        for nr in phones:
            returnstring += f"""{c} Possible Phone: {nr}\n"""
        return [returnstring, emails]
class WeLeak:
    @staticmethod
    def search(what):
        returnstring = ""
        res = requests.get(f"https://api.weleakinfo.to/api?value={what}&type=email&key={semid.__app__.config['WeLeakInfo']}")
        res = json.loads(res.text)
        if res["success"] != False:
            for result in res["result"]:
                if result != None:
                    returnstring += f"""Potential Leak: {result["line"]}\n"""
        return returnstring