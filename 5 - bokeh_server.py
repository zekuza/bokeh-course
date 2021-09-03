from bokeh.io import curdoc
from bokeh.models.widgets import TextInput, Button, Paragraph
from bokeh.layouts import layout

# generate widgets
text_input = TextInput(value='Simon')
button = Button(label='Generate Text')
output = Paragraph()

def update():
    output.text = "Hello, " + text_input.value

button.on_click(update)

ui = layout([[button,text_input],[output]])

curdoc().add_root(ui)
