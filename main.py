import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import datetime

# Define data for the bar chart
x = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E', 'Product F', 'Product G']
y = [100, 200, 300, 400, 500, 600, 700]

pio.templates["draft"] = go.layout.Template(
    layout_annotations=[
        dict(
            name="draft watermark",
            text="DRAFT",
            textangle=-30,
            opacity=0.1,
            font=dict(color="black", size=100),
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
        )
    ]
)
pio.templates.default = "plotly+draft"

# Define a list of dates for the one-week date range
start_date = datetime.date.today()
end_date = start_date + datetime.timedelta(days=6)
dates = [start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]

# Create a list of colors for the bars based on the day of the week
colors = ['#0FD2D2' if date.weekday() < 5 else '#D08276' for date in dates]

# Create a list of weekday names
weekday_names = [date.strftime("%A") for date in dates]

# Create a bar chart using Plotly Express
fig = px.bar(x=weekday_names, y=y, color=colors, barmode='stack', title='Daily Total Sales',
             labels={'x': 'Weekday', 'y': 'Total Sales'},
             color_discrete_sequence=["#0FD2D2", "#D08276"],
             category_orders={'x': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']})

# Add separate legends for weekdays and weekends
fig.update_traces(name='Weekdays', selector=dict(name='#0FD2D2'))
fig.update_traces(name='Weekends', selector=dict(name='#D08276'))

# Customize the title text
fig.update_layout(title='Daily Total Sales',
                  # {'text': 'Daily Total Sales', 'font':
                  #     {'size': 30, 'family': 'Arial', 'color': 'white'}},
                  plot_bgcolor='#1F3333', paper_bgcolor='#1F3333', font_color='white')

# Display the bar chart
fig.show()
