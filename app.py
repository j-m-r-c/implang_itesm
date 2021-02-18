import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
from dash.dependencies import Input, Output


app = dash.Dash(__name__, title='Instituto Municipal de Planeación y Gestión Urbana - IMPLANG', external_stylesheets=[dbc.themes.BOOTSTRAP],
				meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])



server = app.server


# Connect to app pages

from apps import home, itesm


# App Layout

app.layout = dbc.Container([

	dbc.NavbarSimple(
		[

        	dbc.Button('ITESM', href='/apps/itesm', color='light'),

		],
		brand='IMPLANG',
		brand_href='/apps/home'
	),

	html.Div(id='page-content', children=[]),
	dcc.Location(id='url', refresh=False)

])


@app.callback(Output(component_id='page-content', component_property=
					'children'),
			[Input(component_id='url', component_property='pathname')])

def display_page(pathname):
	if pathname == '/apps/itesm':
		return itesm.layout
	else:
		return home.layout


if __name__ == '__main__':
	app.run_server(debug=True)


