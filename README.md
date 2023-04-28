# Dependencies

- PySimpleGUI
- Java JDK 20 for jarsigner.
- 7z for modifying AAB file: deleting exist key files in AAB file.


# Installation

- Register Java JDK's binaries and 7z's binary in system's PATH. Required commands: jarsigner and 7z.

- If you encounter error relating to missing PySimpleGUI: `ImportError: No module named PySimpleGUI`, install PySimpleGUI through CLI:

```pip install PySimpleGUI```

- Run these commands to initialize virtual environment and install dependencies

```
python -m venv venv

pip install -r requirements.txt
```

# Run

On Window, you can click on the 'RUN_window.bat' and run saved batch command to launch the GUI.

Otherwise, run these commands:

Window:
```
venv\Scripts\activate
python main.py
```

Mac:
```
source venv/bin/activate
python main.py
```