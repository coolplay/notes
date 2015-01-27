fontattrs = range(0, 9)
fgcolors = range(30, 38)
bgcolors = range(40, 48)

graphics_mode = '\033[{}m'
text = '{}This source code is: '

def colored_texts():
    for fontattr in fontattrs:
        for fgcolor in fgcolors:
            for bgcolor in bgcolors:
                values = ';'.join(map(str, [fontattr, fgcolor, bgcolor]))
                mode = graphics_mode.format(values)
                colored_text = text.format(mode) + values
                yield colored_text
        yield ''


if __name__ == '__main__':
    for colored_text in colored_texts():
        print colored_text
