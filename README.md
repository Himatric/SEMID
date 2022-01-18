# SEMID Framework #

## About ## 

Semid is a framework with different Discord functions and OSINT modules.\
Currently this is still a work in development, but modules are still being added

## Installation ##

```bash
git clone https://github.com/Himatric/Semid

cd Semid

pip install -r requirements.txt
```
## Usage ##

```
python -m semid

$ help

                                      SEMID HELP MENU
    CommandName             Args                Kwargs              Description

    use                     Module::Function    Function Arguments  Use a built in function

    modules                                                         Lists all availabe modules
    
    cls                                                             Clears the console.

    help                                                            Shows this menu.

$  use github::search -u Himatric

| Username: Himatric
| Name:     Hima
| Bio:      i code or something
| Email:    None
| Twitter:  None
| Location: None

```

## Modules ##

```
=>  modules

                                    SEMID ALL MODULES
        Module Name     Function Name               Description

        tiktok          search                      Searches through a users tiktok profile
                                                    and through all their videos for information
                                                    such as discord tag, email and phone number.

        socials         search                      Searches for a users social media by the
                                                    username provided. Currently only looks
                                                    for linktree, but will be updated shortly
        
        semid           search                      Sends a request to our api, which includes an
                                                    ip address if found. Currently only working
                                                    with discord ID

        playstation     searchusername              Sends a request to PS Resolver's api
                                                    which returns an IP Address if found

        playstation     searchip                    Sends a request to PS Resolver's api and
                                                    gets Username if one is found.

        discord         tokeninfo                   Gets all information about the token by
                                                    sending requests to the discord api.

        discord         tokenonliner                Makes all the tokens from a provided file
                                                    online by connecting them directly to
                                                    Discord's websocket.

        discord         scrapechannel               Scrapes messages from a discord channel
                                                    and outputs them in a file/console

        discord         disabletoken                Disables the given token by sending invalid
                                                    requests to the discord api.

        doxbin          search                      Searches provided username on doxbin and
                                                    returns the urls if found.
                                                    
        twitter         search                      Scrapes twitter forgot password page and
                                                    returns twitter account + email/phone if found.
                                
        github          search                      Sends a requests to the github api with given
                                                    username, and returns all info about the account.
```

## Needed ##

DM me if you have any leaks with discord ids.


## Notes ##


#### Currently only tested with python 3.8.9 ####
