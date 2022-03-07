import base64
import colorama
import random
import halo
import os
import time
try:
    import config
except ImportError:
    class Dummy():
        pass
    config = Dummy()
    config.hard = False
    config.additional_words = []
    config.clean = False
exec(
    "words = " + base64.b64decode(
        base64.b64decode(
            open("words.txt", "rb").read()
        )
    ).decode(
        "utf-8"
    ) if not config.clean else "words = []"
)
if config.additional_words:
    words += config.additional_words

if not isinstance(words, (list, tuple)):
    raise ValueError(
        "Verification failed!"
    )


def clear():
    os.system("clear") if os.name == 'posix' else os.system("cls")


def play():
    with halo.Halo("Loading", color="cyan", spinner="simpleDotsScrolling") as h:
        word = random.choice(words)
        sliced = list(word)
        time.sleep(2)
    count = 1
    emoji = "Pordle! Tries: []"
    clear()
    while count < 6:
        text = f"""
{colorama.Fore.CYAN}P O R D L E{colorama.Fore.RESET}
CHANCE: {count}\n
        """
        a = input(
            f"{colorama.Fore.BLUE}Word> {colorama.Fore.RESET}"
        )
        success = 0
        if not len(a) == 5:
            print("Invalid word!")
            continue
        elif a not in words:
            print("Not exists!")
            continue

        else:
            for char in sliced:
                for char_ in list(a):
                    if char_ in sliced:
                        if char_ == char:
                            a = a.replace(
                                char_, f"{colorama.Fore.GREEN}{char_}{colorama.Fore.RESET}")
                            success += 1
                            emoji += "🟩"
                        else:
                            a = a.replace(
                                char_, f"{colorama.Fore.YELLOW}{char_}{colorama.Fore.RESET}")
                            emoji += "🟨"
                    else:
                        emoji += "⬛"
                        continue
        if isinstance(len(emoji)/5, int):
            print('newline')
            emoji += "\n"
        if success == 5:
            print(
                "Congratulations! You won!"
            )
            break
        text += f"""
{a}
        """
        print(text, end="\r")
        count += 1
    with open('result.txt', 'w', encoding='utf-8') as fp:
        fp.write(emoji.replace("[]", f"{count - 1}"))
    return emoji.replace("[]", f"{count - 1}")


def check(word: str):
    if not word in words:
        return False
    return True


colorama.init()

print(
    f"""
{colorama.Fore.CYAN}Pordle!{colorama.Fore.RESET}
{colorama.Back.WHITE}{colorama.Fore.BLACK}A wordle but in python!{colorama.Back.RESET}{colorama.Fore.RESET}
How to play?
If wordle returns you some characters that has no color then it isn't in the pordle select word.

However if wordle returns you some characters yellow that mean it does exists in the selected word BUT it isn't placed in correct place yet!

ELSE if wordles returns you some characters green that mean you placed a correct alphabet in correct positions!

btw hard mode exists just make {colorama.Fore.LIGHTBLUE_EX}config.py{colorama.Fore.RESET} and do
{colorama.Fore.LIGHTGREEN_EX}{colorama.Back.BLACK}
hard = True
{colorama.Fore.RESET}{colorama.Back.RESET}
If you want to add your own dictionary then do
{colorama.Fore.LIGHTGREEN_EX}{colorama.Back.BLACK}
additional_words = [
    "balls"
]
{colorama.Fore.RESET}{colorama.Back.RESET}
OR if you want to use the dictionary NOT OURS then do
{colorama.Fore.LIGHTGREEN_EX}{colorama.Back.BLACK}
clean = True
{colorama.Fore.RESET}{colorama.Back.RESET}
    """
)

while True:
    a = input(
        "Selection> "
    )
    if a.lower() in ('h', 'help'):
        print(
            f"""
    {colorama.Fore.CYAN}Pordle!{colorama.Fore.RESET}
    {colorama.Back.WHITE}{colorama.Fore.BLACK}A wordle but in python!{colorama.Back.RESET}{colorama.Fore.RESET}
    How to play?
    If wordle returns you some characters that has no color then it isn't in the pordle select word.

    However if wordle returns you some characters yellow that mean it does exists in the selected word BUT it isn't placed in correct place yet!

    ELSE if wordles returns you some characters green that mean you placed a correct alphabet in correct positions!

    btw hard mode exists just make {colorama.Fore.LIGHTBLUE_EX}config.py{colorama.Fore.RESET} and do
    {colorama.Fore.LIGHTGREEN_EX}{colorama.Back.BLACK}
    hard = True
    {colorama.Fore.RESET}{colorama.Back.RESET}
    If you want to add your own dictionary then do
    {colorama.Fore.LIGHTGREEN_EX}{colorama.Back.BLACK}
    additional_words = [
        "balls"
    ]
    {colorama.Fore.RESET}{colorama.Back.RESET}
    OR if you want to use the dictionary NOT OURS then do
    {colorama.Fore.LIGHTGREEN_EX}{colorama.Back.BLACK}
    clean = True
    {colorama.Fore.RESET}{colorama.Back.RESET}
        """
        )
    elif a.lower() in ('play', 'p'):
        print(play())
    elif a.lower() in ('q', 'quit'):
        print("Exiting")
        exit(0)
    else:
        print(
            f"{colorama.Fore.RED}No command found!"
        )
