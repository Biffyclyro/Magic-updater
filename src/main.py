import urllib.request as req
import json
import os

url = 'https://mtgarena.downloads.wizards.com/Live/Windows64/version'

resp = req.urlopen(url)

game_infos = json.loads(resp.read())

game_file = req.urlopen(game_infos['CurrentInstallerURL'])

os.system("rm -rf ./installer")
os.system("mkdir ./installer")

with open('./installer/magic.msi', 'wb') as magic:
    magic.write(game_file.read())

os.system("wine ./installer/magic.msi")