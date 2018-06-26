import pyautogui , PIL , time

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand','robocop': 4, 'comments': 'Tell Bob I said hi.'},
{'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,'comments': 'n/a'},
{'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball','robocop': 1, 'comments': 'Please take the puppets out of thebreak room.'},
{'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money','robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'}]

name = (554,329)    #coordinates
print("### Press CRTL + C to escape from the script ! ")        #to let the user exit from the script

try:
    for  i in formData:        
        time.sleep(8)
        pyautogui.click(name[0],name[1])
        pyautogui.typewrite(i['name'] + '\t')
        pyautogui.typewrite(i['fear'] + '\t')
        #for drop down selection
        if i['source'] == 'wand':
            pyautogui.typewrite(['down','\t'])
        elif i['source'] == 'amuler':
            pyautogui.typewrite(['down','down','\t'])
        elif i['source'] == 'crystal ball':
            pyautogui.typewrite(['down','down','down','\t'])
        elif i['source'] == 'money':
            pyautogui.typewrite(['down','down','down','down','\t'])
        #for button selection
        if i['robocop'] == 1 :
            pyautogui.typewrite(['down','up' ,'\t'])
        elif i['robocop'] == 2 :
            pyautogui.typewrite(['down','\t'])
        elif i['robocop'] == 3 :
            pyautogui.typewrite(['down','down','\t'])
        elif i['robocop'] == 4 :
            pyautogui.typewrite(['down','down','down','\t']) 
        #add commment
        pyautogui.typewrite(i['comments'] + '\t')
        print('Please check the information before submitting.....')
        time.sleep(8)
        print('submitting!')
        pyautogui.click(517,831)
        time.sleep(10)
        pyautogui.click(642,250)
                


except KeyboardInterrupt :
    print('######  The script has been terminated !  #######')   