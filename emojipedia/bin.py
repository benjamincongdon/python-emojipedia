from emojipedia import Emojipedia
import sys


def run():
    if len(sys.argv) < 2:
        print('Usage: emojipedia <emoji-name>')
        return

    try:
        emoji = Emojipedia.search(sys.argv[1])

        print(emoji.character)
    except (RuntimeError, ValueError):
        print('Emoji not found')
