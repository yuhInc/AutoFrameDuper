from ctypes.wintypes import SIZE
import keyboard
import webbrowser
import win32api, win32con
import threading
import pyautogui
import time
import PySimpleGUI as sg
delayLeft = 2
delayRight = 0.1
script_running = False

def main():
    def dupingClicker():

        def rightClicker():
            print("rightClicker activated")
            time.sleep(10)
            while keyboard.is_pressed('alt') == False and script_running == True:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                time.sleep(0.1)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
                time.sleep(delayRight)

        def leftClicker():
            print("leftClicker activated")
            time.sleep(12)
            while keyboard.is_pressed('fn') == False and script_running == True:
                pyautogui.click()
                time.sleep(delayLeft)
        t1 = threading.Thread(target=rightClicker)
        t2 = threading.Thread(target=leftClicker)
        t1.start()
        t2.start()

        t1.join() 
        t2.join()
        print("Script Finished Clicking")
        sg.popup_ok('Script Stopped', title=('Script Stopped'))
    menu = ['&Discord', ['yuh#0004',]],['&Github', ['My Profile',]],
    layout = [  
                [sg.Menu(menu)],
                [sg.Text('Left click delay: '), sg.Slider(range=(2, 10), default_value=2, orientation='h', size=(30, 30)), sg.Text('Ticks')],
                [sg.Text('Right click delay: '), sg.Spin(initial_value=0, values=(0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0),size=(5, 5)), sg.Text('Ticks')],
                [sg.Text('Default delay (2) is recommended')],
                [sg.Button('Start Script'),sg.Button("Info"),sg.Text('', size=(32, 0)), sg.Button('Leave')],
                [sg.StatusBar('Script is not running', key='-STATUS-')]]
    window = sg.Window('Auto Frame Duper by yuh#0004', layout, size=(550, 190), font='standart', icon=r"item_frame.ico")
   
    while True:
        event, values = window.read()
        if event == 'Info':
            sg.popup('Instructions','You have 10 seconds to switch your window to Minecraft. If you need help contact me on Discord yuh#0004')
        if event == 'Start Script':
            window['Start Script'].update(disabled=True)
            print('pressed button - activate script')
            window['-STATUS-'].update('Script is now running...')
            delayLeft = int(values[1])
            delayRight = float(values[2])
            script_running = True
            sg.popup_notify('Hold ALT to stop Script') 
            dupingClicker() 
            script_running = False 
            window['-STATUS-'].update('Script is not running')
            window['Start Script'].update(disabled=False)
        if event == 'My Profile':
            webbrowser.open('https://github.com/yuhInc')
        if event == sg.WIN_CLOSED or event == 'Leave':
            script_running = False
            break
        

    window.close()   


if __name__ ==  '__main__':
    main()
