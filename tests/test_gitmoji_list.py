import subprocess
from unittest import TestCase

from gitmoji import GITMOJI_LIST_STR
from gitmoji.constants import split_gitmoji_list


class TestGitmojiList(TestCase):
    def setUp(self):
        subprocess.run(["npm", "install", "-g", "gitmoji-cli@latest"])
        self.maxDiff = None

    def test_gitmoji_list(self):
        output = subprocess.getoutput("gitmoji --list")
        if output.startswith("- Fetching the emoji list"):
            output = "\n".join(output.splitlines()[2:])
        for a, b in zip(
            split_gitmoji_list(GITMOJI_LIST_STR), split_gitmoji_list(output)
        ):
            assert a["description"] == b["description"]
            assert a["command"] == b["command"]
