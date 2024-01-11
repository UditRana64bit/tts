import pyperclip # pip install pyperclip
import pyautogui # pip install pyautogui
import webbrowser # Inbuilt
from time import sleep # Inbuilt
import json # Inbuilt
import keyboard # pip install keyboard
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import warnings
import win32gui
import win32con


def maximize_active_window():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)


def CookieScrapper():
    print(".....")
    print(".....")
    webbrowser.open("https://bard.google.com/chat")
    sleep(2)
    maximize_active_window()
    pyautogui.click(x=1464, y=58)
    sleep(1)
    pyautogui.click(x=1431, y=56)
    sleep(7)
    pyautogui.click(x=1230, y=219)
    sleep(9)
    pyautogui.click(x=1200, y=94)
    sleep(1)
    keyboard.press_and_release('Ctrl + W')
    sleep(1)

CookieScrapper()