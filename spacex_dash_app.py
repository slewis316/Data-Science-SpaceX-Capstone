import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# dash application
app = dash.Dash(__name__)

# dropdown options
dropdown_options = [
                    {'label': 'All Sites', 'value': 'ALL'},
                    {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                    {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                    {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                    {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}
                    ]

# app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                
                                dcc.Dropdown(id='site-dropdown',
                                             options=dropdown_options,
                                             value='ALL',
                                             placeholder="Select a Launch Site Here",
                                             searchable=True
                                            ),
                                html.Br(),

                                # pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # slider to select payload range
                                dcc.RangeSlider(
                                    id='payload-slider',
                                    min=0,
                                    max=10000,
                                    step=1000,
                                    marks={0:'0', 10000:'10000'},
                                    value=[min_payload,max_payload]
                                ),


                                # scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# callback function for `site-dropdown` as input, `success-pie-chart` as output
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))

def get_pie_chart(entered_site):
    
    if entered_site == 'ALL':
        df  = spacex_df[spacex_df['class'] == 1]
        fig = px.pie(df, names='Launch Site', title='Success Rate of All Sites')
        return fig
    else:
        # return the outcomes piechart for a selected site
        df = spacex_df.loc[spacex_df['Launch Site'] == entered_site]
        fig = px.pie(df, names = 'class',title = 'Total Success Launches for site '+entered_site)
        return fig


# callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),Input(component_id='payload-slider', component_property='value')])

def get_scatter_chart(entered_site,slider_range):
    low, high = slider_range

    if entered_site=='ALL':
        mask = (spacex_df['Payload Mass (kg)'] > low) & (spacex_df['Payload Mass (kg)'] < high)
        fig = px.scatter(spacex_df[mask], x="Payload Mass (kg)", y="class", color="Booster Version Category",
                        title="Correlation Between Payload Mass And Success For All Sites")
        return fig
    else :
        filtered_df = spacex_df.loc[spacex_df['Launch Site'] == entered_site]
        mask = (filtered_df['Payload Mass (kg)'] > low) & (filtered_df['Payload Mass (kg)'] < high)
        fig = px.scatter(filtered_df[mask], x="Payload Mass (kg)", y="class", color="Booster Version Category",
                        title="Correlation Between Payload Mass and Success for site " +entered_site)
        return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
