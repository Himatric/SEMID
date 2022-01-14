import os, argparse
from semid.util.modules import Modules
from semid.util.console import Console
class SemidArgs:
    def __init__(self):
        self.version = 1.0
    def start(self, args:list):
        parser = argparse.ArgumentParser("SEMID")
        parser.add_argument("--module", "-m")
        parser.add_argument("--args", "-a")
        # parser.add_argument("--help", "-h", action="store_true", required=False)
        args = parser.parse_args(args=args)
        funcargs = args.args
        module = args.module
        # if args.help == True:
        #     return self.show_help()
        if not module or module == "":
            return print(self.wrong_module())
        else:
            try:
                mod = "semid.modules."+module.split("::")[0]
                func = module.split("::")[1]
                try:
                    return Modules.get_module_by_name(mod, func)(funcargs)
                except:
                    try:
                        return Modules.get_function_syntax(mod, func)
                    except:
                        return print(self.wrong_module())
            except:
                return print(self.wrong_module())
                

    def wrong_module():
        print(Console.red("Not a valid module"))
    def show_help():
        text = """
                                    SEMID HELP MENU
    CommandName             Args                Kwargs              Description

    use                     Module::Function    Function Arguments  Use a built in module.

    modules                 /                   /                   Lists all availabe modules.

    cls                     /                   /                   Clears the console.

    help                    /                   /                   Shows this menu.


"""
        print(Console.color(text))

