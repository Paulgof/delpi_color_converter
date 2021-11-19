# delpi_color_converter
Python console program that converts RGB or HEX to Pascal Color (TColor) and back
```
Консольная программа для конвертации цвета RGB или HEX в Pascal Color (TColor)

optional arguments:
  -h, --help            show this help message and exit
  --rgb R G B           Цвет в формате RGB (3 числа от 0 до 255)
  -# HEX, --hex HEX     Цвет в формате HEX
  -r PASCAL_COLOR_INT, --reverse PASCAL_COLOR_INT
                        Обратная конвертация Pascal Color в HEX

Пример получения Pascal Color из RGB (красный цвет):
    python3 pascal_color.py --rgb 255 0 0
    >> Pascal Color: 255

Пример получения Pascal Color из HEX (зелёный цвет):
    python3 pascal_color.py -# '#00FF00' (или python3 pascal_color.py -# 00FF00)
    >> Pascal Color: 65280

Пример получения HEX из Pascal Color (синий цвет):
    python3 pascal_color.py -r 16711680
    >> Converting Pascal Color to HEX
    >> HEX: #0000FF
        
```
