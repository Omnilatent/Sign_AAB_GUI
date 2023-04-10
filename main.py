import PySimpleGUI as psg
import PySimpleGUI as sg

import os


sg.theme("Default1")

layout = [
    [sg.T("")],
    [sg.Text("Choose file to sign: "), sg.Input(), sg.FileBrowse(key="-AAB-")],
    [sg.Text("Choose keystore: "), sg.Input(), sg.FileBrowse(key="-KEYSTORE-")],
    [sg.Text("Keystore Password:"), sg.Input('', enable_events=False, key='-KEYSTOREPASSWORD-', password_char='*')],
    [sg.Text("Key Alias:"), sg.Input('', key='-KEYALIAS-')],
    [sg.Text("Alias Password:"), sg.Input('', key='-ALIASPASSWORD-', password_char='*')],
    [sg.Button("Submit")]
]

###Building Window
window = sg.Window('My File Browser', layout, size=(600,250))
values = ""
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        print(values["-AAB-"])
        print(values["-KEYSTORE-"])
        print(values["-KEYSTOREPASSWORD-"])
        print(values["-KEYALIAS-"])
        print(values["-ALIASPASSWORD-"])
        command = "zip -d \"" + values["-AAB-"] + "\" META-INF/\\*"
        print(command)
        #os.system(command)
        command = "jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 -keystore \"{key}\" \"{aab_path}\" {key_alias} -storepass {mystorepassword} -keypass {aliaspass}".format(
        	key=values["-KEYSTORE-"], 
        	aab_path=values["-AAB-"], 
        	key_alias=values["-KEYALIAS-"], 
        	mystorepassword=values["-KEYSTOREPASSWORD-"], 
        	aliaspass=values["-ALIASPASSWORD-"])
        print(command)
        os.system(command)