import PySimpleGUI as psg
import PySimpleGUI as sg

import os


sg.theme("DarkTeal2")
layout = [
    [sg.T("")],
    [sg.Text("Choose file to sign: "), sg.Input(), sg.FileBrowse(key="-IN-")],
    [sg.Button("Submit")]
]

###Building Window
window = sg.Window('My File Browser', layout, size=(600,150))
aabpath = ""
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        print(values["-IN-"])
        print(type(values["-IN-"]))
        aabpath = values["-IN-"]
        #command = "zip -d \"" + values["-IN-"] + "\" META-INF/\\*"
        #os.system(command)
        break


layout = [
    [sg.T("")],
    [sg.Text("Choose keystore: "), sg.Input(), sg.FileBrowse(key="-IN-")],
    [sg.Text("Keystore Password:"), sg.Input('', enable_events=False, key='-KEYSTOREPASSWORD-')],
    [sg.Text("Key Alias:"), sg.Input('', key='-KEYALIAS-')],
    [sg.Text("Alias Password:"), sg.Input('', key='-ALIASPASSWORD-')],
    [sg.Button("Submit")]
]

###Building Window
window = sg.Window('My File Browser', layout, size=(600,150))
keystore = ""
while True:
    event, keystore = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        print(keystore["-IN-"])
        print(values["-IN-"])
        print(values["-KEYSTOREPASSWORD-"])
        print(values["-KEYALIAS-"])
        print(values["-ALIASPASSWORD-"])
        command = "zip -d \"" + aabpath + "\" META-INF/\\*"
        os.system(command)
        command = "jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 -keystore {key} {aab_path} {key_alias} -storepass {mystorepassword} -keypass {aliaspass}".format(key=keystore, aab_path=aabpath, key_alias="", mystorepassword="", aliaspass="")


l1 = psg.Text('AAB name', key='-OUT-', font=('Arial Bold', 20), expand_x=True, justification='center')
t1 = psg.Input('', enable_events=True, key='-INPUT-', font=('Arial Bold', 20), expand_x=True, justification='left')
b1 = psg.Button('Ok', key='-OK-', font=('Arial Bold', 20))
b2 = psg.Button('Exit', font=('Arial Bold', 20))
layout = [[l1], [t1], [b1, b2]]
window = psg.Window('Input Demo', layout, size=(750, 150))
while True:
   event, values = window.read()
   print(event, values)
   if event == '-INPUT-':
      if values['-INPUT-'][-1] not in ('0123456789'):
         psg.popup("Only digits allowed")
         window['-INPUT-'].update(values['-INPUT-'][:-1])
   if event == psg.WIN_CLOSED or event == 'Exit':
      break
window.close()