import semid.modules
from semid.util.console import Console
import sys


class Modules:
    @staticmethod
    def get_module_by_name(name:str, func:str):
        try:
            funct = getattr(sys.modules[name.lower()], func.lower())
            return funct
        except:
            raise Exception()
    def get_function_syntax(module:str, function:str) -> str:
        function = function + "syntax"
        funct = getattr(sys.modules[module.lower()], function.lower())()
        return funct
    def list_modules():
        text = """
                                      SEMID ALL MODULES
        Module Name     Function Name               Description

        tiktok          search                      Searches through a users tiktok profile
                                                    and through all their videos for information
                                                    such as discord tag, email and phone number. 
        
        socials         search                      Searches for a users social media by the
                                                    username provided. Currently only looks
                                                    for linktree, but will be updated shortly

        playstation     searchusername              Sends a request to PS Resolver's api
                                                    which returns an IP Address if found

        playstation     searchip                    Sends a request to PS Resolver's api and
                                                    gets Username if one is found.
                    
        discord         tokeninfo                   Gets all information about the token by
                                                    sending requests to the discord api.

        discord         tokenonliner                Makes all the tokens from a provided file
                                                    online by connecting them directly to
                                                    Discord's websocket.

        discord         disabletoken                Disables the given token by sending invalid
                                                    requests to the discord api.

        doxbin          search                      Searches provided username on doxbin and
                                                    returns the urls if found.

        twitter         search                      Scrapes twitter forgot password page and
                                                    returns twitter account + email/phone if found
                                
        github          search                      Sends a requests to the github api with given
                                                    username, and returns all info about the account.
        """
        print(Console.color(text))


