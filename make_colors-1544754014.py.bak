
class Win10Colors(object):
    """docstring for Win10Colors"""
    def __init__(self):
        super(Win10Colors, self).__init__()

    def colored(self, string, foreground, background, attrs=[]):
        '''win10color

        print out coloring for windows >= 10

        Keyword Arguments:
            foreground {str} -- string fore color (default: {''})
            background {str} -- background color  (default: {''})
            attrs {list} -- attribute support: reset, bold, underline, inverse
        '''
        # attrs_bank = {}
        # reset = ''
        # bold = ''
        # underline = ''
        # inverse = ''
        # if attrs:
        #     for i in attrs:
        #         if i == 'reset':
        #             reset = '0m'
        #         elif i == 'bold':
        #             bold = '1m'
        #         elif i == 'underline':
        #             underline = '4m'
        #         elif i == 'inverse':
        #             inverse = '7m'

        fore_color_bank = {
                'black': '30m',
                'red': '31m',
                'green': '32m',
                'yellow': '33m',
                'blue': '34m',
                'magenta': '35m',
                'cyan': '36m',
                'white': '37m',

                'lightblack': '90m',
                'lightgrey': '90m',
                'lightred': '91m',
                'lightgreen': '92m',
                'lightyellow': '93m',
                'lightblue': '94m',
                'lightmagenta': '95m',
                'lightcyan': '96m',
                'lightwhite': '97m',

            }

        back_color_bank = {
                'black': '40m',
                'red': '41m',
                'green': '42m',
                'yellow': '43m',
                'blue': '44m',
                'magenta': '45m',
                'cyan': '46m',
                'white': '47m',

                'on_black': '40m',
                'on_red': '41m',
                'on_green': '42m',
                'on_yellow': '43m',
                'on_blue': '44m',
                'on_magenta': '45m',
                'on_cyan': '46m',
                'on_white': '47m',

                'lightblack': '100m',
                'lightgrey': '100m',
                'lightred': '101m',
                'lightgreen': '102m',
                'lightyellow': '103m',
                'lightblue': '104m',
                'lightmagenta': '105m',
                'lightcyan': '106m',
                'lightwhite': '107m',

                'on_lightblack': '100m',
                'on_lightgrey': '100m',
                'on_lightred': '101m',
                'on_lightgreen': '102m',
                'on_lightyellow': '103m',
                'on_lightblue': '104m',
                'on_lightmagenta': '105m',
                'on_lightcyan': '106m',
                'on_lightwhite': '107m',

            }

        background = back_color_bank.get(background)
        foreground = fore_color_bank.get(foreground)
        if not background:
            background = '40m'
        if not foreground:
            foreground = '37m'

        return "[%s;%s%s[0m" % (background[:-1], foreground, string)

def make_colors(string, foreground = 'white', background=None, attrs=[]):
    win10color = Win10Colors()
    return win10color.colored(string, foreground, background, attrs)
