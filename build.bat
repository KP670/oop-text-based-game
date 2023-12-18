rm ./dist
pyinstaller --noconfirm --onefile --console --name "turn-based-attk" --add-data "./src/sfx;."  "./src/main.py"