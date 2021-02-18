import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px


# App Layout

layout = html.Div([

    # Banner Principal

    dbc.Row(
        dbc.Col([
            html.Img(src='../assets/home.jpg', style={'max-width':'100%', 'height':'auto'}),
             html.H2('Una ciudad más inclusiva se está construyendo',
                style={'position': 'absolute', 'top': '50%', 'left': '50%',
                'transform': 'translate(-50%, -50%)','color': 'white','text-align':'center'})
        ])
    ),

    # GIF
    
    dbc.Row(
        dbc.Col([
            html.Img(src='../assets/home_2.gif', style={'max-width':'100%', 'height':'auto'})
        ])
    ),

    #VIDEO

    dbc.Container(
        dbc.Row(
            dbc.Col([
                html.Iframe(src='https://www.youtube.com/embed/FIL5--AeKK4', width='100%', height='550')
            ],className='py-3')
        )
    ),


    # Footer 

    dbc.Container([
    
        dbc.Row(
            dbc.Col(
              html.H6('Envíanos un correo a implang@sanpedro.gob.mx')  
            ), className='px-1 pt-4'
        ),

        dbc.Row(
            dbc.Col([
                html.A(
                    html.Img(src='../assets/instagram.png', style={'max-width':'85px', 'height':'34px'}),
                    href='https://www.instagram.com/implang_spgg/', target='blank'
                ),

                html.A(
                    html.Img(src='../assets/facebook.png', style={'max-width':'85px', 'height':'34px'}),
                    href='https://www.facebook.com/implangspgg', target='blank', className='pl-3'
                ),

                html.A(
                    html.Img(src='../assets/twitter.png', style={'max-width':'85px', 'height':'34px'}),
                    href='https://twitter.com/implang_spgg', target='blank', className='pl-3'
                ),

                html.A(
                    html.Img(src='../assets/youtube.png',style={'max-width':'85px', 'height':'34px'}),
                    href='https://www.youtube.com/channel/UCZwYFPh0dHnKhXqzaxlaqNg', target='blank',
                    className='pl-3'
                )
            ]), className='px-1 py-4'
        )
        
    ]),

    dbc.Container([

       dbc.Row(
            dbc.Col(
                html.H6('Instituto Municipal de Planeación y Gestión Urbana')
            ), className='px-1 pt-3'
        ),

        dbc.Row(
            dbc.Col(
                html.H6('San Pedro Garza García, Nuevo León, México')
            ), className='px-1 py-3'
        )
        
    ], style={'background-color': 'black','color': 'white'}
    )




])

