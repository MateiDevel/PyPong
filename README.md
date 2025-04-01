# PyPong
Just a normal Pong game made in PyGame, nothing out of the ordinary...
# Instalation 
First install PyGame...
```pip install pygame```
Then install pyinstaller...
```pip install pyinstaller```
Then use pyinstaller to build the game using : 
```pyinstaller --onefile --noconsole --icon=src/icon.ico --add-data "sounds/*;sounds" --add-data "fonts/*;fonts" main.py```
All done!
