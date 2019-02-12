import dash
import dash_html_components as html
import dash_core_components as dcc
import requests

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    # html.Div(dcc.Input(id='input-box', type='text')),
    html.Button('Get Artist', id='artist_btn'),


    html.Div(id='output-container',
             children='Enter a value and press submit')
])


@app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('artist_btn', 'n_clicks')],
    # [dash.dependencies.State('input-box', 'value')]
    )
def update_output(n_clicks, value=20503):
	# print(requests.get(f'https://rap-stats.com/Markov?artist_id=20503').text)
	return requests.get(f'https://rap-stats.com/Markov?artist_id={value}').json()['data']



if __name__ == '__main__':
    app.run_server(debug=True)