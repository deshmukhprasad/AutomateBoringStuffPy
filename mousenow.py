import pyautogui , PIL
print('Press CRTL+ c to stop !')

try :
    while True :
        x ,y = pyautogui.position()
        im = pyautogui.screenshot()
        strp = 'X: ' + str(x).rjust(4) + '\t Y : ' + str(y).rjust(4) + '\t RGB: '+str(im.getpixel((x,y)))
        print( strp , end = '\r')
        print('\b'*len(strp) , end='', flush=True)
except KeyboardInterrupt :
    print('\nDone')

