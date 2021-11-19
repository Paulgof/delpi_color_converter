import argparse
from typing import Tuple


def main(rgb_color: Tuple[int] = None, hex_color: int = None, reverse: int = None):
    if reverse:
        print('Converting Pascal Color to HEX')
        bgr_hex = '{:0>6X}'.format(reverse)
        rgb_hex = ''.join((bgr_hex[4:], bgr_hex[2:4], bgr_hex[:2]))
        print('HEX: #{}'.format(rgb_hex))
        return

    if not hex_color:
        hex_color = ''.join(map(lambda component: '{:0>2X}'.format(component), rgb_color))

    if hex_color[0] == '#':
        hex_color = hex_color[1:]

    if len(hex_color) != 6:
        raise ValueError('Wrong hex')

    converted_hex = ''.join((hex_color[4:], hex_color[2:4], hex_color[:2]))
    pascal_color = int(converted_hex, base=16)
    print('Pascal Color: {}'.format(pascal_color))


if __name__ == '__main__':
    command_line_parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Консольная программа для конвертации цвета RGB или HEX в Pascal Color (TColor) для Инфоклиники',
        epilog='''
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
        '''
    )
    color_format_group = command_line_parser.add_mutually_exclusive_group()
    color_format_group.add_argument(
        '--rgb',
        type=int,
        nargs=3,
        metavar=('R', 'G', 'B'),
        help='Цвет в формате RGB (3 числа от 0 до 255)',
    )
    color_format_group.add_argument('-#', '--hex', type=str, help='Цвет в формате HEX')
    color_format_group.add_argument(
        '-r',
        '--reverse',
        type=int,
        metavar='PASCAL_COLOR_INT',
        help='Обратная конвертация Pascal Color в HEX',
    )
    arguments = command_line_parser.parse_args()
    main(
        arguments.rgb,
        arguments.hex,
        arguments.reverse,
    )
