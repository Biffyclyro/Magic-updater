import urllib.request as req
from pathlib import Path
import json
import os

url = 'https://mtgarena.downloads.wizards.com/Live/Windows64/version'

home = str(Path.home())

resp = req.urlopen(url)

game_infos = json.loads(resp.read())

game_file = req.urlopen(game_infos['CurrentInstallerURL'])

os.system(f"rm -rf {home}/Downloads/installer")
os.system(f"mkdir {home}/Downloads/installer")
os.system(f"touch {home}/Downloads/installer/magic.msi")

with open(f'{home}/Downloads/installer/magic.msi', 'wb') as magic:
    magic.write(game_file.read())

os.system(f"wine {home}/Downloads/installer/magic.msi")