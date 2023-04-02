import random
import time
from colorama import Style
from config import Config
import speak
cfg = Config()


def print_to_console(
        title,
        title_color,
        content,
        speak_text=False,
        min_typing_speed=0.05,
        max_typing_speed=0.01):
    global cfg
    if speak_text and cfg.speak_mode:
        speak.say_text(f"{title}. {content}")
    print(title_color + title + " " + Style.RESET_ALL, end="")
    if content:
        words = content.split()
        for i, word in enumerate(words):
            print(word, end="", flush=True)
            if i < len(words) - 1:
                print(" ", end="", flush=True)
            typing_speed = random.uniform(min_typing_speed, max_typing_speed)
            time.sleep(typing_speed)
            # type faster after each word
            min_typing_speed = min_typing_speed * 0.95
            max_typing_speed = max_typing_speed * 0.95
    print()
