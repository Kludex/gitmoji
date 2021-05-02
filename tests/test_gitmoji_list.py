import subprocess

from gitmoji import GITMOJI_LIST_STR
from gitmoji.constants import split_gitmoji_list


def test_gitmoji_list():
    subprocess.run(["npm", "install", "-g", "gitmoji-cli@latest"])
    output = subprocess.getoutput("gitmoji --list")
    print(output)
    assert split_gitmoji_list(GITMOJI_LIST_STR) == split_gitmoji_list(output)
