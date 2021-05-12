import pyautogui
import sys
import time
import python_imagesearch.imagesearch as imgsearch
from pyclick import HumanClicker
from pynput import keyboard

exec_stop = False
mode = "autoclicker"
pos = 0
pyautogui.FAILSAFE = False

# mode = "pos_logger"

def run():
    hc = HumanClicker()
    # While there's no 'execution stop' command passed
    while exec_stop is False:
        # If the script is in autoclicker mode
        if mode == "autoclicker":
            try:                
                if imgsearch.imagesearch("img/mine.png")[0] != -1:
                    pos = imgsearch.imagesearch("img/mine.png")
                    posx = pos[0]
                    posy = pos[1]
                    hc.move((posx, posy), 1)
                    hc.click()
                    print(f"clicco mine")
                    
                if imgsearch.imagesearch("img/timed_out.png")[0] != -1:
                    pos = imgsearch.imagesearch("img/timed_out.png")
                    posx = pos[0]
                    posy = pos[1]
                    hc.move((posx, posy), 1)
                    hc.click()
                    print(f"clicco timed_out")

                if imgsearch.imagesearch("img/claim.png")[0] != -1:
                    pos = imgsearch.imagesearch("img/claim.png")
                    posx = pos[0]
                    posy = pos[1]
                    hc.move((posx, posy), 1)
                    hc.click()
                    print(f"clicco claim")
                    
                if imgsearch.imagesearch("img/recaptcha.png")[0] != -1:
                    pos = imgsearch.imagesearch("img/recaptcha.png")
                    posx = pos[0]
                    posy = pos[1]
                    hc.move((posx, posy), 1)
                    hc.click()
                    print(f"clicco recaptcha")
                    time.sleep(2)
                    if imgsearch.imagesearch("img/omino.png")[0] != -1:
                        pos = imgsearch.imagesearch("img/omino.png")
                        posx = pos[0]
                        posy = pos[1]
                        hc.move((posx, posy), 1)
                        hc.click()
                        print(f"clicco omino")
                        time.sleep(2)
                    while  imgsearch.imagesearch("img/riprova.png")[0] != -1:
                        pos = imgsearch.imagesearch("img/riprova.png")
                        posx = pos[0]
                        posy = pos[1]
                        hc.move((posx, posy), 1)
                        hc.click()
                        print(f"clicco riprova")
                        time.sleep(2)
                        if imgsearch.imagesearch("img/omino.png")[0] != -1:
                            pos = imgsearch.imagesearch("img/omino.png")
                            posx = pos[0]
                            posy = pos[1]
                            hc.move((posx, posy), 1)
                            hc.click()
                            print(f"clicco omino")
                            time.sleep(2)
                    if imgsearch.imagesearch("img/approve.png")[0] != -1:
                        pos = imgsearch.imagesearch("img/approve.png")
                        posx = pos[0]
                        posy = pos[1]
                        hc.move((posx, posy), 1)
                        hc.click()
                        print(f"clicco approve")

                if imgsearch.imagesearch("img/mine_main_menu.png")[0] != -1:
                    pos = imgsearch.imagesearch("img/mine_main_menu.png")
                    posx = pos[0]
                    posy = pos[1]
                    hc.move((posx, posy), 1)
                    hc.click()
                    print(f"clicco mine_main_menu")

                if imgsearch.imagesearch("img/go_to_hub.png")[0] != -1:
                    pos = imgsearch.imagesearch("img/go_to_hub.png")
                    posx = pos[0]
                    posy = pos[1]
                    hc.move((posx, posy), 1)
                    hc.click()
                    print(f"clicco go_to_hub")
                                       
                time.sleep(1)
            except:
                # If an error occurred
                print("An error occurred: ", sys.exc_info()[1])
                sys.exit(0)
        # If the script is in position logger mode
        else:
            try:
                # Print position to console every second
                print(pyautogui.position())
                time.sleep(1)
            except:
                # If an error occurred
                print("An error occurred: ", sys.exc_info()[2])


def on_press(key):
    # When F11 key is pressed, toggle modes between Autoclicker and Position Logger
    if key == keyboard.Key.f11:
        global mode
        mode = "pos_logger" if mode == "autoclicker" else "autoclicker"
        print(f"Changing mode to {mode}")
    # When F12 key is pressed, stop executing the script
    elif key == keyboard.Key.f12:
        global exec_stop
        exec_stop = True
        print("Shutting down...")
        sys.exit(0)


def main():
    # Listen for pressed keys
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    run()


if __name__ == '__main__':
    main()
