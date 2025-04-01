# PyPong
Just a normal Pong game made in PyGame, nothing out of the ordinary...
# Instalation 
First install PyGame...
```sh 
pip install pygame
```
Then install pyinstaller...
```sh
pip install pyinstaller
```
Then use pyinstaller to build the game using : 
```sh 
pyinstaller --onefile --noconsole --icon=icon.ico --add-data "sounds/*;sounds" --add-data "fonts/*;fonts" main.py
```
This will create a dist dirrectory where the game files are located.
All done!
