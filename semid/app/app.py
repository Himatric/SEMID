import os, sys, json
from requests import get

from semid.util.console import Console
from semid.util.modules import Modules
class Semid:
    def __init__(self) -> None:
        self.response = Console.green("\n$  ")
        self.version = "BETA"
        if os.name == "nt":
            os.system("cls")
        else: 
            os.system("clear")
        self.show_banner()
        Console.set_title("""SEMID Framework | Made by Hima""")
        self.config = json.loads(open("config.json").read())
        self.checkversion()
    def start(self):
        sys.stdout.write(self.response)
        sys.stdout.flush()
        what = input()
        self.handle(what)
    def handle(self, what:str):
        function = what.split(" ")[0]
        # self.check_function(function)
        if function == "use":
            try:
                module = what.split(" ")[1]
                function = module.split("::")[1]
                module = "semid.modules." + module.split("::")[0].replace("/", ".")
            except:
                self.wrong_module()
                self.start()
            try:
                args = " ".join(what.split(" ")[2:])
                try:
                    Modules.get_module_by_name(module, function)(args)
                    return self.start()
                except Exception or TypeError or ValueError or KeyError:
                    try:
                        print(Modules.get_function_syntax(module, function))
                        return self.start()
                    except:
                        self.wrong_module()
                        self.start()
            except IndexError:
                try:
                    Modules.get_module_by_name(module, function)()
                    return self.start()
                except Exception or TypeError or ValueError or KeyError:
                    try:
                        print(Modules.get_function_syntax(module, function))
                    except:
                        self.wrong_module()
                    return self.start()
        if function == "help":
            self.show_help()
            self.start()
        if function == "modules":
            Modules.list_modules()
            self.start()
        if function == "cls":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            self.start()
        else:
            self.wrong_module()
            self.start()
    def show_banner(self):
        banner = """Welcome to SEMID!
SEMID is yet another OSINT framework. 
Although it does have a lot of functions for Discord.
Currently SEMID is still under heavy development.
Try typing help to see what you can do.

"""
        sys.stdout.write(Console.color(Console.center(banner)))
    def checkversion(self):
        res = json.loads(get("https://raw.githubusercontent.com/Himatric/SEMID/master/config.json").text)
        if res["version"] != self.version:
            print("\n" + Console.red("You are not using the latest version of SEMID."))
    def show_help(self):
        text = """
                                    SEMID HELP MENU
    CommandName             Args                Kwargs              Description

    use                     Module::Function    Function Arguments  Use a built in module.

    modules                                                         Lists all availabe modules.

    cls                                                             Clears the console.

    help                                                            Shows this menu.


"""
        print(Console.color(text))
    def wrong_module(self):
        text = """ERR: Invalid module"""
        return print(Console.red(Console.center(text)))
    def check_function(self, functio:str):
        found = False
        functions = ["search", "searchusername", "searchip", "tokeninfo", "tokenonliner", "search"]
        
    
        
