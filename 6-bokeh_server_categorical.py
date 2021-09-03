# Imports

from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models.annotations import Label,LabelSet
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Select, Slider
from bokeh.layouts import layout
from bokeh.models import Range1d

# Create column datasource

cds_original = ColumnDataSource(dict(average_grade = [7,9,10,5],
                            exam_grade=[9,9,7,4],
                            student_name = ['Simon','Jason','Peter','Aaron']))


cds = ColumnDataSource(dict(average_grade = [7,9,10,5],
                            exam_grade=[9,9,7,4],
                            student_name = ['Simon','Jason','Peter','Aaron']))

# generate figure
f = figure(x_range = Range1d(start=0,end=10),
          y_range = Range1d(start=0,end=10))

f.xaxis.axis_label = "average grade"
f.yaxis.axis_label = "exam grade"

# Plot glyph
f.circle(
    x = 'average_grade',
    y = 'exam_grade',
    source = cds,
    size = 8,
)

# Create filtering function

def filter_grades(attr, old, new):
    cds.data={
        key:[value for i,value in enumerate(cds_original.data[key]) if cds_original.data["exam_grade"][i] >= slider.value] for key in cds_original.data
    }

# UI widget functionality
def update_labels(attr, old, new):
    labels.text = select.value

# Add labels for bokeh glyphs
labels=LabelSet(
    x='average_grade',
    y='exam_grade',
    text='student_name',
    source=cds,
)
f.add_layout(labels)

# add description
description = Label(
    x=1,
    y=1,
    text="This graph shows average grades and exam grades for 3rd grade students",
    render_mode="css"
)
f.add_layout(description)

options = [('average_grade','average grade'),
            ('exam_grade','exam grade'),
            ('student_name','student name')]

select=Select(title = "Select title to view: ",
              options = options,
              )
slider=Slider(start=0,
              end=10,
              value=0,
              step=0.5,
              title="Above Exam Grade",
              )

select.on_change("value",update_labels)
slider.on_change("value",filter_grades)

ui = layout([[select,slider]])

curdoc().add_root(f)
curdoc().add_root(ui)

