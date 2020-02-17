from pylab import *
import plotly
plotly.plotly.sign_in('LeeYunHow', 'WgfWHEVjL60p3OVaWLWx')
py = plotly.plotly


def to_plotly(ax=None):
    if ax is None:
        ax = gca()
    lines = []
    for line in ax.get_lines():
        lines.append({'x': line.get_xdata(),
                      'y': line.get_ydata(),
                      'name': line.get_label()})

    layout = {
        'title': ax.get_title(),
        'xaxis': {'title': ax.get_xlabel()},
        'yaxis': {'title': ax.get_ylabel()}
    }
    filename = ax.get_title() if ax.get_title() != '' else 'Untitled'
    print(filename)
    close('all')
    # return lines, layout
    return py.iplot(lines, layout=layout, filename=filename)


plot(rand(100), label='trace1')
plot(rand(100)+1, label='trace2')
title('title')
xlabel('X label')
ylabel('Y label')

response = to_plotly()
print(response)