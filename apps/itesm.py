import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px

layout = html.Div([

    ####################################### COMIENZA ESPACIO DE EDICIÓN #######################################

    ## BANNER PRINCIPAL
    
    dbc.Row(
        dbc.Col([
            html.Img(src='../assets/imagen.png', style={'max-width':'100%', 'height':'auto'}),
            html.H2('Ejemplo título banner',
                style={'position': 'absolute', 'top': '50%', 'left': '50%',
                'transform': 'translate(-50%, -50%)'})
        ], style={'color': 'white', 'position': 'relative', 'text-align': 'center'})
    ),

    ## SECCIÓN 1
    dbc.Container([
        
        ## Títutlo
        dbc.Row(
            dbc.Col(
                html.H2('Ejemplo de título')
            ), className='px-1 pt-4'
        ),

        ## Texto
        dbc.Row(
            dbc.Col(
                html.H5('La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible.')  
            ), className='px-1 py-4'
        )

    ]),


    ## SECCION 2
    dbc.Container([
        # Título
        dbc.Row(
            dbc.Col(
                html.H2('Otro ejemplo de título')
                ),className='py-3', style={'background-color': 'black','color': 'white'}
            ),

        ## Texto
        dbc.Row([
            dbc.Col(
                html.H5('La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible.'), lg=3, md=9, sm=4
            ),
            dbc.Col(
                html.H5('La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible.'), lg=9, md=3, sm=8
            ), 
        ],className='py-3')

    ]),

    ######################################## TERMINA ESPACIO DE EDICIÓN ########################################

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