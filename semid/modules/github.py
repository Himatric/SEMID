import argparse, requests, json, semid
from semid.util.console import Console
from semid.util.search import WeLeak
def search(args:str):
    args = args.split()
    parser = argparse.ArgumentParser("SEMID")
    parser.add_argument("--username", "-u", required=False)
    parser.add_argument("--weleak", "-w", required=False, action="store_true")
    args = parser.parse_args(args)
    try:
        username = args.username
    except:
        raise TypeError
    res = requests.get(f'https://api.github.com/users/{username}')
    jso = json.loads(res.text)
    username = jso["login"]
    id = jso["id"]
    location = jso["location"] if jso["location"] else "None"
    email = jso["email"] if jso["email"] else "None"
    bio = jso["bio"]
    twitter = jso["twitter_username"] if jso["twitter_username"] else "None"
    name = jso["name"]
    a = Console.red("|")
    if email != "None" and args.weleak == True and semid.__app__.config["WeLeak"] != "":
        weleak = WeLeak.search(email)
    text = f"""
{a} Username: {username}
{a} Name:     {name}
{a} Bio:      {bio}
{a} Email:    {email}
{a} Twitter:  {twitter}
{a} Location: {location}
"""
    text += weleak
    print(text)

def searchsyntax():
    text = """a"""
    return text
