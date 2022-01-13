from semid.util.search import Google
from semid.util.console import Console


def search(args:str):
    argsArr = args.split(" ")
    try:
        uind = argsArr.index("--username")
    except:
        try:
            uind = argsArr.index("-u")
        except:
            raise TypeError
    username = argsArr[uind + 1]
    search = Google.search(f'site:doxbin.com "{username}"')
    if len(search) < 1:
        print("No search results")
    for url, title in search:
        print(f'{Console.red("|")} {url} - {title}')
def searchsyntax():
    text = """
--username | -u <name>  Searches name on doxbin and returns url

Example: use doxbin::search -u kt"""
    return text