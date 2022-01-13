import requests, os
def searchusername(args:str):
    arrArgs = args.split(" ")
    try:
        nameindex = arrArgs.index("--username")
    except:
        try:
            nameindex = arrArgs.index("-u")
        except:
            raise TypeError
    name = arrArgs[nameindex + 1]
    url = f"https://api.playstationresolver.xyz/?ACTION=GAMERTAG_TO_IP&GAMERTAG={name}&JSON=True"
    res = requests.get(url)
    res.raise_for_status()
    os.system('echo {} | python -m json.tool | pygmentize -l javascript --json'.format(res.text.replace("\n", "").replace(" ", "")))

def searchusernamesyntax():
    text= """
--username | -u <username>

Example: use playstation::searchusername -u SEMID"""
    return text

def searchip(args:str):
    arrArgs = args.split(" ")
    try:
        nameindex = arrArgs.index("--ip")
    except:
        try:
            nameindex = arrArgs.index("-h")
        except:
            raise TypeError
    ip = arrArgs[nameindex + 1]
    url = f"https://api.playstationresolver.xyz?ACTION=IP_TO_GAMERTAG&IP_ADDRESS={ip}&JSON=true"
    res = requests.get(url)
    res.raise_for_status()
    os.system('echo {} | python -m json.tool | pygmentize -l javascript --json'.format(res.text.replace("\n", "").replace(" ", "")))
def searchipsyntax():
    text= """
--ip | -h <username>

Example: use playstation::searchip -h 127.0.0.1"""
    return text