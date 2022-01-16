from semid.util.search import Google
from semid.util.console import Console
import argparse

def search(args:str):
    parser = argparse.ArgumentParser("SEMID")
    parser.add_argument("--username", "-u", required=False)
    args = args.split()
    args = parser.parse_args(args)
    try:
        username = args.username
    except:
        raise TypeError
    search = Google.search(f'site:doxbin.com "{username}"', 0)
    if len(search) < 1:
        print("No search results")
    for url, title in search:
        print(f'{Console.red("|")} {url} - {title}')
def searchsyntax():
    text = """
--username | -u <name>  Searches name on doxbin and returns url

Example: use doxbin::search -u kt"""
    return text