#!/usr/bin/env Python3
import PySimpleGUI as sg
import os
#from subprocess import *


# ----------- V2 -------------

# build exe
# pyinstaller -wF -F --uac-admin --uac-uiaccess SCTC.py


# some packages not working
#pip uninstall
#pip install --no-cache-dir --upgrade

sg.change_look_and_feel('Reddit')

# ------ Menu Definition ------ #
menu_def = [['File', ['Exit']],
            ['Help', 'go/wasd'], ]
# ------ Column Definition ------ #
counter = 1
column1 = [[sg.Button('MSRA', pad=((2,2),1)), sg.Button('Browse', pad=((2,2),1)), sg.Button('Ping', pad=((2,2),1))],
           [sg.Button('See Logged in Users', pad=((2,2),1))], #query user /server:
           [sg.Button('NsLookup', pad=((2,2),1)), sg.Button('Getmac', pad=((2,2),1))],
           [sg.Button('Send msg', pad=((2,2),1)), sg.InputText(size=(7,1))],
           [sg.Button('Run cmd', pad=((2,2),1)), sg.InputText(size=(8,1))],
           [sg.Button('Reboot', pad=((2,2),1)), sg.Button('Shutdown', pad=((2,2),1))],
           [sg.Button('Force Reboot', pad=((2,2),1)), sg.Button('Clicky',pad=((0,0),0), key='btnADHD')]]

layout = [[sg.Menu(menu_def, tearoff=True)],
          [sg.Text('Asset Number or IP address:')],
          [sg.InputText(size=(12, 3)), sg.Checkbox('Append ".corp.ads"', default=True)],
          [sg.Text('Remote Desktop Connection:')],
          [sg.Button('Standard', key='Standard', size=(10, 3)), sg.Button('Old Asset', size=(10, 3), disabled=True, key='btnOld'), sg.Button('New Asset', size=(10, 3), disabled=True, key='btnNew')],
          [sg.Checkbox('Faster Logon', default=True), sg.Checkbox('Automate PCmover Migration', default=False, enable_events=True, disabled=False)],
          [sg.Frame(layout=[
              [sg.Button('Computer Management', size=(18,1), pad=((0,0),0))],
              [sg.Button('Event Viewer', size=(18,1), pad=((0,0),0))],
              [sg.Button('Performance Monitor', size=(18,1), pad=((0,0),0))],
              [sg.Button('Services', size=(18,1), pad=((0,0),0))],
              [sg.Button('Registry Editor', size=(18,1), pad=((0,0),0))],
              [sg.Button('System Information', size=(18,1), pad=((0,0),0))],
              [sg.Button('Task Scheduler', size=(18,1), pad=((0,0),0))]], title='Administrative Tools', relief=sg.RELIEF_SUNKEN, tooltip=':)', background_color='#c8c8c8'), sg.Column(column1)],
          [sg.Text("Note: This tool must be ran with functional ID")]]

window = sg.Window('Service Center Technician Console', layout)

while True:                             # The Event Loop
    event, values = window.read()
    #print(event, values)

    # values[]
    # 1 = asset number
    # 2 = append corp.ds
    # 3 = faster logon
    # 4 = automate


    if event is None or event == 'Exit':
        break

    # toggle automation
    if values[4] is True:
        window['btnOld'].update(disabled=False)
        window['btnNew'].update(disabled=False)
        window['Standard'].update(disabled=True)
    elif values[4] is False:
        window['btnOld'].update(disabled=True)
        window['btnNew'].update(disabled=True)
        window['Standard'].update(disabled=False)

    if event in (None, 'Quit'):
        break

    # adhd
    if event == "btnADHD":
        #print("test")
        counter = counter+counter
        window['btnADHD'].update(text=counter)


    # if no asset number
    if values[1] == '':
        #print("empty")
        # Please input asset number or IP address
        continue

    # append corp.ads
    if values[2] is True:
        values[1] = values[1] + '.corp.ads'


    # -------------- RDP --------------------

    # regular rdp
    if event == 'Standard' and values[3] is False:
        try:
            os.system('cmd /c start mstsc /w:900 /h:900 /v:' + values[1] + ' /admin')
        except:
            pass

    # regular rdp + fast
    elif event == 'Standard' and values[3] is True:
        try:
            os.system('cmd /c reg add "\\\\' + values[1] + '\\HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /f /v "DelayedDesktopSwitchTimeout" /t REG_DWORD /d 0 & reg add "\\\\' + values[1] + '\\HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /f /v "EnableFirstLogonAnimation" /t REG_DWORD /d 0 & reg add "\\\\' + values[1] + '\\HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\corp.ads" /f /v * /t REG_DWORD /d 1 & start cmd /c start mstsc /w:900 /h:900 /v:' + values[1] + ' /admin')
        except:
            pass


    # old
    if event == 'btnOld' and values[3] is False:
        try:
            os.system('cmd /c XCOPY /Y "\\\\D071101\\c$\\autostart\\old_autostart.bat" "\\\\' + values[1] + '\\c$\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\" & start cmd /c start mstsc /w:900 /h:900 /v:' + values[1] + ' /admin')
        except:
            pass

    # old + fast
    elif event == 'btnOld' and values[3] is True:
        try:
            os.system('cmd /c XCOPY /Y "\\\\D071101\\c$\\autostart\\old_autostart.bat" "\\\\' + values[1] + '\\c$\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\" & reg add "\\\\' + values[1] + '\\HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /f /v "DelayedDesktopSwitchTimeout" /t REG_DWORD /d 0 & reg add "\\\\' + values[1] + '\\HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /f /v "EnableFirstLogonAnimation" /t REG_DWORD /d 0 & reg add "\\\\' + values[1] + '\\HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\corp.ads" /f /v * /t REG_DWORD /d 1 & start cmd /c start mstsc /w:900 /h:900 /v:' + values[1] + ' /admin')
        except:
            pass


    # new
    if event == 'btnNew' and values[3] is False:
        try:
            os.system('cmd /c XCOPY /Y "\\\\D071101\\c$\\autostart\\new_autostart.bat" "\\\\' + values[1] + '\\c$\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\" & start cmd /c start mstsc /w:900 /h:900 /v:' + values[1] + ' /admin')
        except:
            pass

    # new + fast
    elif event == 'btnNew' and values[3] is True:
        try:
            os.system('cmd /c XCOPY /Y "\\\\D071101\\c$\\autostart\\new_autostart.bat" "\\\\' + values[1] + '\\c$\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\" & reg add "\\\\' + values[1] + '\\HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /f /v "DelayedDesktopSwitchTimeout" /t REG_DWORD /d 0 & reg add "\\\\' + values[1] + '\\HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /f /v "EnableFirstLogonAnimation" /t REG_DWORD /d 0 & reg add "\\\\' + values[1] + '\\HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\corp.ads" /f /v * /t REG_DWORD /d 1 & start cmd /c start mstsc /w:900 /h:900 /v:' + values[1] + ' /admin')
        except:
            pass


    # values[]
    # 1 = asset number

    # ------------- Administrative Tools ---------------

    if event == "Computer Management":
        try:
            os.system('start cmd /c start compmgmt.msc /computer=\\\\' + values[1])
        except:
            pass

    if event == "Event Viewer":
        try:
            os.system('start cmd /c start EventVwr \\\\' + values[1])
        except:
            pass


    if event == "Performance Monitor":
        try:
            os.system('start cmd /c start perfmon')
        except:
            pass

    if event == "Services":
        try:
            os.system('start cmd /c start services.msc /computer=' + values[1])
        except:
            pass

    if event == "Registry Editor":
        try:
            os.system('start cmd /c start regedit')
        except:
            pass

    if event == "System Information":
        try:
            os.system('start cmd /c start msinfo32 /computer \\\\' + values[1])
        except:
            pass

    if event == "Task Scheduler":
        try:
            os.system('start cmd /c start taskschd.msc')
        except:
            pass


    #----------- more tools -----------------

    if event == "MSRA":
        try:
            os.system('start cmd /c start msra /offerra ' + values[1])
        except:
            pass

    if event == "See Logged in Users":
        try:
            os.system('start cmd /k query user /server:' + values[1])
        except:
            pass

    if event == "Browse":
        try:
            os.system('start cmd /c start \\\\' + values[1] + '\\c$')
        except:
            pass

    if event == "Ping":
        try:
            os.system('start cmd /k ping ' + values[1] + ' -t')
        except:
            pass

    if event == "NsLookup":
        try:
            os.system('start cmd /k nslookup ' + values[1])
        except:
            pass

    if event == "Getmac":
        try:
            os.system('start cmd /k getmac /s ' + values[1])
        except:
            pass

    if event == "Send msg":
        try:
            os.system('start cmd /k msg * /server:' + values[1] + ' /v ' + values[5])
        except:
            pass

    if event == "Run cmd":
        # \\d071101\c$\Tools\PSTools\psexec.exe \\hostname
        psexec = r'\\d071101\c$\Tools\PSTools\psexec.exe ' + r'\\'
        # https://ss64.com/nt/psexec.html
        try:
            os.system('start cmd /k ' + psexec + values[1] + ' ' + values[6])
        except:
            pass

    if event == "Reboot":
        try:
            os.system('start cmd /c shutdown /r /m \\\\' + values[1] + ' /t 01')
        except:
            pass

    if event == "Shutdown":
        try:
            os.system('start cmd /c shutdown /s /m \\\\' + values[1] + ' /t 01')
        except:
            pass

    if event == "Force Reboot":
        try:
            os.system('start cmd /c shutdown /r /f /m \\\\' + values[1] + ' /t 01')
        except:
            pass


window.close()

