import dash
from dash import dcc
from dash import html
import plotly.express as px
import plotly.graph_objects as go
import datetime

app = dash.Dash(__name__)

# Define data for the bar chart
x = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E', 'Product F', 'Product G']
y = [100, 200, 300, 400, 500, 600, 700]

# Define a list of dates for the one-week date range
start_date = datetime.date.today()
end_date = start_date + datetime.timedelta(days=6)
dates = [start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]

# Create a list of colors for the bars based on the day of the week
colors = ['#0FD2D2' if date.weekday() < 5 else '#D08276' for date in dates]

# Create a list of weekday names
weekday_names = [date.strftime("%A") for date in dates]

# Create a bar chart using Plotly
fig = px.bar(x=weekday_names, y=y, color=colors, barmode='stack')

# Add separate legends for weekdays and weekends
fig.update_traces(name='Weekdays', selector=dict(name='#0FD2D2'))
fig.update_traces(name='Weekends', selector=dict(name='#D08276'))

# Customize the bar chart
fig.update_layout(
    title='Figure title',
    # title={
    #     'text': 'Figure title',
    #     # 'x': 0.1,  # Set the x position of the title to be centered
    #     # 'y': 0.95,  # Set the y position of the title to be near the top of the plot
    #     'font': {
    #         'size': 18,
    #         'color': 'white',
    #         'family': 'Arial, sans-serif'
    #     },
    #     # 'xanchor': 'left',
    #     'yanchor': 'top',
    #     'pad': {'l': 500}
    # },
    legend=dict(
        title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="right",
    ),
    xaxis_title='Weekday',
    yaxis_title='Total Sales',
    plot_bgcolor='#1F3333',
    paper_bgcolor='#1F3333',
    font=dict(color='white'))

draft_template = go.layout.Template()

draft_template.layout.title = {
    'x': 0.1,
    'font': {
        'size': 30,
        'color': 'red',
        'family': 'Arial, sans-serif'
    }}

fig.update_layout(
    template=draft_template,
    annotations=[
        dict(
            templateitemname="draft watermark",
            text="CONFIDENTIAL",
        )
    ]
)

app.layout = html.Div(children=[
    html.H1(children='Daily Total Sales', className='fig-title'),
    dcc.Graph(
        id='sales-bar-chart',
        figure=fig
    ),

])

if __name__ == '__main__':
    app.run_server(debug=True)
