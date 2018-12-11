from libqtile import bar, widget
from settings.theme import colors

bottom = bar.Bar(
    [
        widget.GroupBox(
            active=colors['green'],
            this_current_screen_border=colors['yellow'],
            urgent_color=colors['magenta'],
            urgent_border=colors['magenta'],
            borderwidth=2),
        widget.CurrentLayoutIcon(),
        widget.Prompt(),
        widget.TaskList(border=colors['blue']),
        widget.Mpd(),
        widget.Volume(update_interval=2),
        widget.Systray(),
        widget.CPUGraph(
            graph_color=colors['green'],
            border_color=colors['black']),
        widget.MemoryGraph(graph_color=colors['blue'],
                           border_color=colors['black']),
        widget.NetGraph(
            graph_color=colors['yellow'],
            border_color=colors['black']),
        widget.ThermalSensor(),
        widget.Battery(),
        widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
    ],
    24,
    background=colors['background'],
)
