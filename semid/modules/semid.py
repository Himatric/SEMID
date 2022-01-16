import requests, argparse

def search(args:str):
    args = args.split()
    parser = argparse.ArgumentParser("SEMID")
    parser.add_argument("--id", "-q", required=False)
    args = parser.parse_args(args)
    try:
        id:str = args.id 
    except:
        raise TypeError()
    if not id or id == "":
        raise TypeError()
    if not id.isdigit() or len(id) < 14:
        raise TypeError()
    host = "https://himas.wrld.is-best.net/discord"
    res = requests.post(host, data={
        'query': id
    })
    if res.status_code == 200:
        print("Found a match: \n" + res.json()["data"])
    elif res.status_code == 404:
        print("Invalid UserID")
    elif res.status_code == 401:
        print("No result found")

    """DM ME IF U HAVE ANY DISCORD DB LEAKS (CAN BE FROM GAMES BUT MUST INCLUDE DISCORD IDS)"""


def searchsyntax():
    text = """
--id | -q <discord ID>

Example: use tiktok::search --id 423544947686244362"""
    return text
    
