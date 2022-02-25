from PIL import Image, ImageDraw
import pyautogui
import keyboard
import time
from time import perf_counter
import pydirectinput
IMAGE_FOLDER = "image/"

global k,yp,xp, xf, yf, xm, ym

k = 0
xf = 1170
yf = 450

xm = 1450
ym = 840
def region_analyze(image, x, y, width, height):
    white = 0
    for x_cord in range(x, x + width):
        for y_cord in range(y, y + height):
            pixel = image.getpixel((x_cord, y_cord))
            if pixel[0] > 240 and pixel[1] > 240 and pixel[2] > 240:
                white += 1

    return white


def analyze(image_ref, col=20, row=10):

    reference = Image.open(image_ref)
    width, height = reference.size
    block_width = width // col
    block_height = height // row
    for x in range(0, width, block_width):
        for y in range(0, height, block_height):
            dotx = 5
            doty = 1
            if x // block_width == dotx and y // block_height == doty:
                for xdraw in range(0, 1 * block_width, block_width):
                    for ydraw in range(0, 1 * block_height, block_height):
                        region_ref = region_analyze(reference, x + xdraw, y + ydraw, block_width * 13, 8 * block_height)
                        draw = ImageDraw.Draw(reference)
                        draw.rectangle(
                            (x + xdraw, y + ydraw, x + 13 * block_width + xdraw, y + 8 * block_height + ydraw),
                            outline="red")

    reference.save("diff.png")

    return region_ref


def run():

    STOP_COMBINATION = "0"
    keyboard.on_press(callback)
    keyboard.wait(STOP_COMBINATION)



def callback(event: keyboard._keyboard_event.KeyboardEvent):
    if event.name == "9":
        global yp, xp
        xp,yp = pyautogui.position()
        start1 = perf_counter()
        create_screenshot()
        #time.sleep()
        pyautogui.press('9')
        end1 = perf_counter()
        print(end1 - start1, "в отклике")

def create_screenshot():
    global yp, xp, k
    name = "icon20.png"
    pyautogui.screenshot(region=(800,20,200,800)).save("C:/Users/dimky/PycharmProjects/pythonProject1/image/icon20.png")
    IMAGE_20 = IMAGE_FOLDER + "icon20.png"
    wh = analyze(IMAGE_20)
    print(wh)

    if wh <= 30:
        pyautogui.mouseDown(button='left')
        time.sleep(1.9)
        pyautogui.mouseUp(button='left')
        time.sleep(1)
        k += 1
    elif wh >= 100 and wh <= 270:
        pyautogui.mouseDown(button='left')
        time.sleep(1.6)
        pyautogui.mouseUp(button='left')
        time.sleep(0.3)

    elif wh >= 290 and wh <= 750:
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.mouseUp(button='left')
        pyautogui.click(button='left', clicks=5, interval=0.04)
        time.sleep(0.4)
        pyautogui.click(button='left', clicks=5, interval=0.04)

    elif wh > 750 and wh <= 1000:
        for i in range(0, 4):
            pyautogui.mouseDown(button='left')
            time.sleep(0.4)
            pyautogui.mouseUp(button='left')
            pyautogui.click(button='left', clicks=4, interval=0.05)


    elif wh > 1000 and wh <= 1100:
        for i in range(0, 4):
            pyautogui.mouseDown(button='left')
            time.sleep(0.15)
            pyautogui.mouseUp(button='left')
            pyautogui.click(button='left', clicks=5, interval=0.05)


    elif wh > 1100:
        for i in range(0, 4):
            pyautogui.mouseDown(button='left')
            time.sleep(0.1)
            pyautogui.mouseUp(button='left')
            pyautogui.click(button='left', clicks=5, interval=0.05)

    print("k =", k)

    if k > 30:
        time.sleep(12)
        pyautogui.click(button='right')
        time.sleep(5)
        pyautogui.click(button='right')
        time.sleep(1)
        pydirectinput.keyDown('s')
        time.sleep(0.1)
        pydirectinput.keyUp('s')
        time.sleep(0.5)
        pydirectinput.keyDown('w')
        time.sleep(0.11)
        pydirectinput.keyUp('w')
        time.sleep(2)
        pydirectinput.keyDown('f3')
        time.sleep(0.5)
        pydirectinput.keyUp('f3')
        time.sleep(1)
        pydirectinput.press("r")
        time.sleep(1)
        pydirectinput.moveTo(xf, yf)
        time.sleep(0.5)
        pydirectinput.click()
        time.sleep(0.5)
        pydirectinput.moveTo(xm, ym)
        time.sleep(0.2)
        pydirectinput.click()
        time.sleep(2)
        k = 0



dir = 'image/icon'

run()
