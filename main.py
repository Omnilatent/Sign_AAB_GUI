import PySimpleGUI as psg
import PySimpleGUI as sg

import os
import platform

sg.theme("Default1")

layout = [
    [sg.T("")],
    [sg.Text("Choose file to sign: "), sg.Input(), sg.FileBrowse(key="-AAB-")],
    [sg.Text("Choose keystore: "), sg.Input(), sg.FileBrowse(key="-KEYSTORE-")],
    [sg.Text("Keystore Password:"), sg.Input('', enable_events=False, key='-KEYSTOREPASSWORD-', password_char='*')],
    [sg.Text("Key Alias:"), sg.Input('', key='-KEYALIAS-')],
    [sg.Text("Alias Password:"), sg.Input('', key='-ALIASPASSWORD-', password_char='*')],
    [sg.Button("Submit")],
    [sg.Button("DeleteKey")],
    [sg.Text("", key="-RESULT-")]
]

print(platform.system())

###Building Window
window = sg.Window('My File Browser', layout, size=(600,250))
values = ""
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        window["-RESULT-"].update("Running... Please wait")
        window.refresh()
        print(values["-AAB-"])
        print(values["-KEYSTORE-"])
        print(values["-KEYSTOREPASSWORD-"])
        print(values["-KEYALIAS-"])
        print(values["-ALIASPASSWORD-"])
        if platform.system() == "Windows":
            command = "7z d \"{aab_path}\" META-INF".format(aab_path=values["-AAB-"])
        else:
            command = "zip -d \"{aab_path}\" META-INF/\\*".format(aab_path=values["-AAB-"])
        print(command)
        os.system(command)
        command = "jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 -keystore \"{key}\" \"{aab_path}\" {key_alias} -storepass {mystorepassword} -keypass {aliaspass}".format(
        	key=values["-KEYSTORE-"], 
        	aab_path=values["-AAB-"], 
        	key_alias=values["-KEYALIAS-"], 
        	mystorepassword=values["-KEYSTOREPASSWORD-"], 
        	aliaspass=values["-ALIASPASSWORD-"])
        print("jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 -keystore \"{key}\" \"{aab_path}\" {key_alias} -storepass {mystorepassword} -keypass {aliaspass}".format(
            key=values["-KEYSTORE-"], 
            aab_path=values["-AAB-"], 
            key_alias=values["-KEYALIAS-"], 
            mystorepassword="***", 
            aliaspass="***"))
        os.system(command)
        window["-RESULT-"].update("FINISHED")
    elif event == "DeleteKey":
        if platform.system() == "Windows":
            command = "7z d \"{aab_path}\" META-INF".format(aab_path=values["-AAB-"])
        else:
            command = "zip -d \"{aab_path}\" META-INF/\\*".format(aab_path=values["-AAB-"])
        print(command)
        os.system(command)
        window["-RESULT-"].update("FINISHED")
