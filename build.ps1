rm ./dist/* -a
rm ./build -a
pyinstaller --noconfirm --console --name "turn-based-attk" --add-data "./src/sfx;."  "./src/main.py"