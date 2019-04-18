import sys

def make_colors(string, foreground = '', background = '', attrs = '', color_type = '', **kwargs):
    string = str(string)
    if not foreground:
        return string
    if not background:
        background = ''           

    try:
        import click
        colors = {
            "white": "white",
            "black": "black",
            "blue": "blue",
            "cyan": "cyan",
            "green": "green",
            "red": "red",
            "magenta": "magenta",
            "yellow": "yellow",
            "lightwhite": "white",
            "lightblack": "black",
            "lightblue": "blue",
            "lightcyan": "cyan",
            "lightgreen": "green",
            "lightred": "red",
            "lightmagenta": "magenta",
            "lightyellow": "yellow",
            "on_white": "white",
            "on_black": "black",
            "on_blue": "blue",
            "on_cyan": "cyan",
            "on_green": "green",
            "on_red": "red",
            "on_magenta": "magenta",            
        }
        fg = colors.get(foreground)
        bg = colors.get(background)
        args = {}
        for i in attrs:
            args.update({i: True,})
        
        click.secho(string, fg = fg, bg = bg, **args)
        return ''

    except:
        return string
    
        
    
    
