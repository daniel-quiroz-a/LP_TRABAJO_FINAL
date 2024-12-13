import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.graph_objects as go
import reveal_slides as rs
import folium
from streamlit_folium import st_folium
from scipy.stats import linregress
import streamlit_toggle as tog
import random
import numpy as np

# Configuración inicial de la página
st.set_page_config(page_title="Análisis Global de la Anemia", layout="wide")

# Colocar el logo de la universidad en la parte superior
st.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 65%;
        }
    </style>
    """, unsafe_allow_html=True
)

st.sidebar.image("imagenes/escudo-unalm.png", use_container_width=True)
# Agregar texto en markdown con un estilo de fuente distintivo
st.sidebar.markdown(
    """
    <div style="text-align: center; font-size: 24px; font-family: 'Georgia'; font-weight: bold; color: #2C3E50; margin-top: 15px;">
        Análisis de la anemia infantil en el mundo
    </div>
    """,
    unsafe_allow_html=True,  # Permitir HTML para personalización avanzada
)

with st.sidebar:
    # Menú principal (vertical) en el sidebar
    menu = option_menu(
        menu_title="Menú Principal",  # Título del menú
        options=["Introducción", "Fuentes de datos", "Visualización de datos", "Conclusiones", "Equipo"],  # Opciones
        icons=["info-circle", "database", "bar-chart", "clipboard", "people"],  # Íconos si quieres
        menu_icon="cast",  # Ícono principal del menú
        default_index=0,  # Primera opción seleccionada por defecto
        orientation="vertical",
    )



# Contenido dinámico según opción seleccionada
if menu == "Introducción":
    st.title("Introducción")
    # Queda pendiente

elif menu == "Fuentes de datos":
    st.title("Fuentes de Datos")
    # Queda pendiente

elif menu == "Visualización de datos":
    st.title("Visualización de Datos")

    # Submenú Horizontal para visualizaciones
    viz_menu = option_menu(
        menu_title="",
        options=["Situación Global", "Análisis geográfico", "Proyecciones", "Factores Relacionados"],
        icons=["globe", "bar-chart-steps", "graph-up-arrow", "table"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

    if viz_menu == "Situación Global":
        # Queda pendiente. Tener cuidado con la identacion


    elif viz_menu == "Análisis geográfico":
        # Queda pendiente. Tener cuidado con la identacion

    elif viz_menu == "Proyecciones":
            st.markdown("""
            # 🌍 Estimaciones Futuras: Mirando hacia el 2030
    
            El análisis de datos históricos no solo nos permite comprender lo que ha sucedido, sino que también nos da las herramientas necesarias para **proyectar escenarios futuros**. Al observar cómo han evolucionado los niveles globales de anemia infantil en el pasado, es posible extrapolar esas tendencias para anticipar qué rumbo podrían tomar las próximas décadas.
    
            La capacidad de realizar estas estimaciones no es trivial. La posibilidad de **predecir escenarios futuros**, por simplificados que sean, ofrece una base importante para:
            - **Planificación preventiva:** Si entendemos cómo podría comportarse la prevalencia según las tendencias actuales, es más fácil priorizar estrategias a largo plazo.
            - **Asignación de recursos:** Países con falta de progreso podrían recibir atención focalizada para cambiar su trayectoria.
            - **Creación de políticas públicas:** Las proyecciones generan argumentos sólidos para justificar acciones inmediatas en salud pública.
    
            El siguiente gráfico, presenta datos a comparar que muestra:
            1. Los datos históricos disponibles desde el año 2000 hasta el 2019.
            2. Una extrapolación proyectada de esos patrones basada en tendencias observadas, extendiendo el análisis hasta el 2030.
            """)

            # Cargar los datos históricos
            data_historico_est = pd.read_csv("data/world_bank_anemia_mundial_listo.csv")

            # Ordenamos los datos por año de forma ascendente (aseguramos que estén en orden cronológico)
            data_historico_est = data_historico_est.sort_values(by='year', ascending=True)

            # Calcular el factor de crecimiento promedio (promedio de las variaciones porcentuales año tras año)
            factor_crecimiento = (data_historico_est[
                                      'prevalencia (%)'].pct_change().mean() + 1)  # Para que sea un factor de multiplicación

            # Lista para almacenar los datos con las estimaciones proyectadas
            datos_con_estimaciones = []

            # Agregar los datos originales al conjunto de datos de estimaciones
            for _, row in data_historico_est.iterrows():
                datos_con_estimaciones.append({
                    'year': row['year'],
                    'nivel geográfico': row['nivel geográfico'],  # Usar nivel_geografico
                    'prevalencia (%)': row['prevalencia (%)']
                })
            # Proyectar valores desde 2020 hasta 2030 usando el factor de crecimiento
            ultima_prevalencia = data_historico_est['prevalencia (%)'].iloc[-1]  # Último valor conocido (2019)

            # El último valor de 'nivel_geografico' será el mismo en las proyecciones
            nivel_geografico = data_historico_est['nivel geográfico'].iloc[0]

            for year in range(2020, 2031):
                ultima_prevalencia *= factor_crecimiento  # Aplicar el factor de crecimiento
                datos_con_estimaciones.append({
                    'year': year,
                    'nivel geográfico': 'Mundial',  # Mantener el mismo nivel_geografico
                    'prevalencia (%)': ultima_prevalencia
                })

            # Convertir los datos con estimaciones a un DataFrame
            data_historico_est = pd.DataFrame(datos_con_estimaciones)

            # Reordenar las columnas para que aparezcan como 'year', 'prevalencia (%)' y 'nivel_geografico'
            data_historico_est = data_historico_est[['year', 'prevalencia (%)', 'nivel geográfico']]
            # Crear el gráfico de líneas interactivo con Plotly
            fig = go.Figure()

            # Agregar la línea de datos históricos al gráfico
            fig.add_trace(go.Scatter(
                x=data_historico_est[data_historico_est['year'] < 2020]['year'],
                y=data_historico_est[data_historico_est['year'] < 2020]['prevalencia (%)'],
                mode='lines+markers',
                name='Datos Históricos',
                line=dict(color='#636efa', width=3, shape='spline'),  # Agregamos 'spline' para suavizar la línea
                marker=dict(size=7, color='#636efa', symbol='circle', line=dict(color='white', width=2)),
                hovertemplate="<b>Año:</b> %{x}<br><b>Prevalencia:</b> %{y:.2f}%<extra></extra>"
            ))
            # Agregar la interseccion
            fig.add_trace(go.Scatter(
                x=data_historico_est[(data_historico_est['year'] >= 2019) & (data_historico_est['year'] <= 2020)]['year'],
                y=data_historico_est[(data_historico_est['year'] >= 2019) & (data_historico_est['year'] <= 2020)]['prevalencia (%)'],
                mode='lines+markers',
                name='Proyección',
                line=dict(color='#EF553B', width=3, dash='dot'),  # Línea punteada para diferenciar los proyectados
                marker=dict(size=7, color='#EF553B', symbol='diamond', line=dict(color='white', width=2)),
                hoverinfo="skip",
                showlegend=False
            ))

            # Agregar la línea de datos proyectados al gráfico
            fig.add_trace(go.Scatter(
                x=data_historico_est[data_historico_est['year'] >= 2020]['year'],
                y=data_historico_est[data_historico_est['year'] >= 2020]['prevalencia (%)'],
                mode='lines+markers',
                name='Proyección',
                line=dict(color='#EF553B', width=3, dash='dot'),  # Línea punteada para diferenciar los proyectados
                marker=dict(size=7, color='#EF553B', symbol='diamond', line=dict(color='white', width=2)),
                hovertemplate="<b>Año:</b> %{x}<br><b>Proyección:</b> %{y:.2f}%<extra></extra>"
            ))

            # Personalización del diseño general
            fig.update_layout(
                title=dict(
                    text="<span style='font-size:24px; color:#1f77b4; font-family:Arial;'><b>📉 Estimación Futura de Anemia Infantil (2000-2030)</b></span>",
                    x=0.2),
                xaxis=dict(
                    title="Año",
                    title_font=dict(size=16, color='black'),
                    tickfont=dict(size=14, color='black'),
                    tickmode="linear",
                    tickangle=45,  # Rotar los ticks para mayor claridad
                    range=[1999.5, 2030.5],  # Desde justo antes del 2000 hasta 2030
                    showline=True,
                    linewidth=2,
                    linecolor='gray',
                    gridcolor='lightgray'
                ),
                yaxis=dict(
                    title="Prevalencia (%)",
                    title_font=dict(size=16, color='black'),
                    tickfont=dict(size=14, color='black'),
                    range=[25, 50],  # Ajustar el rango según los datos observados
                    showline=True,
                    linewidth=2,
                    linecolor='gray',
                    gridcolor='lightgray'
                ),
                plot_bgcolor='rgba(240,240,240,0.95)',  # Fondo claro para el gráfico
                paper_bgcolor='white',
                margin=dict(t=100, b=100, l=80, r=80),
                legend=dict(
                    orientation="h",  # Leyenda en formato horizontal
                    yanchor="bottom",
                    y=-0.2,
                    xanchor="center",
                    x=0.5,
                    title=None  # Ocultar encabezado "Legend"
                )
            )

            # Mejorar interactividad
            fig.update_traces(marker_line_width=1.5)
            fig.update_layout(
                hovermode="x",  # Mostrar tooltip alineado a los valores en X
                template="simple_white"
            )
            # Leyenda
            fig.update_layout(
                legend=dict(
                    orientation="v",  # Leyenda en formato vertical
                    yanchor="top",  # Alinear la parte superior con el margen
                    y=1,  # Mantener la posición de la leyenda en la parte superior
                    xanchor="left",  # Anclar al lado izquierdo
                    x=1.02,  # Empujar la leyenda fuera de la gráfica (a la derecha)
                    font=dict(
                        size=12,  # Ajustar tamaño de la fuente
                        color="black"  # Establecer el color de la fuente como negro
                    ),
                    bordercolor="gray",  # (opcional) Borde alrededor de la leyenda para resaltarla
                    borderwidth=1  # Ancho del borde de la leyenda (opcional)
                )
            )
            # Mostrar el gráfico en Streamlit
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("""
                ## 🌎 Comparador de Países: Análisis Futuro

                En esta sección, hemos adaptado el gráfico interactivo presentado en el capítulo anterior, que permitía comparar la prevalencia de anemia infantil entre diferentes países hasta el año 2019.
                Ahora, este gráfico no solo sigue permitiendo la selección y comparación de múltiples países, sino que también **incorpora las proyecciones calculadas para cada uno**, basándonos en las tendencias estimadas. Esta extensión resulta esencial para evaluar cómo podrían afectar los patrones globales y locales a cada región, permitiéndonos identificar posibles diferencias entre naciones en el futuro cercano.
                """)

            st.subheader("Comparador futuro de anemia infantil para cada país")
            # Cargar datos del CSV original
            data = pd.read_csv("data/world_bank_anemia_paises_listo.csv")

            # Limpiar nombres de columnas (por si tienen espacios adicionales)
            data.columns = data.columns.str.strip()

            # Lista para almacenar los datos originales y las estimaciones
            datos_con_estimaciones = []

            # Obtener la lista de países únicos
            paises_unicos = data['pais'].unique()

            for pais in paises_unicos:
                # Filtrar los datos para el país actual
                datos_pais = data[data['pais'] == pais].sort_values(by='year')

                # Calcular las variaciones anuales porcentuales
                datos_pais['variacion'] = datos_pais['prevalencia (%)'].pct_change()

                # Calcular el promedio de la variación porcentual (ignorando valores nulos)
                factor_crecimiento = datos_pais[
                                         'variacion'].mean() + 1  # Agregar 1 para obtener el factor multiplicativo

                # Agregar los datos originales del país al conjunto de datos
                for _, row in datos_pais.iterrows():
                    datos_con_estimaciones.append({
                        'year': row['year'],
                        'pais': row['pais'],
                        'prevalencia (%)': row['prevalencia (%)']
                    })

                # Proyectar valores desde 2020 hasta 2030 usando el factor de crecimiento
                ultima_prevalencia = datos_pais['prevalencia (%)'].iloc[-1]  # Último valor conocido (2019)
                for year in range(2020, 2031):
                    ultima_prevalencia *= factor_crecimiento  # Aplicar el factor de crecimiento
                    datos_con_estimaciones.append({
                        'year': year,
                        'pais': pais,
                        'prevalencia (%)': ultima_prevalencia
                    })

            # Convertir los resultados a un DataFrame
            data_historico_pais_est = pd.DataFrame(datos_con_estimaciones)  # Data con estimación hasta el 2030

            # Transformar la variable 'year' a entero
            data_historico_pais_est['year'] = pd.to_numeric(data_historico_pais_est['year'], errors='coerce')
            data_historico_pais_est['year'] = data_historico_pais_est['year'].astype(int)

            # Obtener la lista de países únicos
            country_data = sorted(data_historico_pais_est['pais'].unique())

            # Generar colores aleatorios para cada país
            colors = {country: f"#{random.randint(0, 0xFFFFFF):06x}" for country in country_data}


            # Función para completar los años faltantes
            def completar_anios(df, country):
                country_data = df[df['pais'] == country]
                all_years = pd.DataFrame({'year': range(df['year'].min(), df['year'].max() + 1)})
                completed_data = pd.merge(all_years, country_data, on='year', how='left')
                completed_data['prevalencia (%)'] = completed_data['prevalencia (%)'].interpolate()
                completed_data['pais'] = completed_data['pais'].fillna(country)
                return completed_data


            # Función para obtener estadísticas y generar mensajes
            def obtener_estadisticas_mensaje(country_df):
                # Calcular el promedio histórico entre 2000 y 2019
                historical_data = country_df[(country_df['year'] >= 2000) & (country_df['year'] <= 2019)]
                avg_prevalence_2000_2019 = historical_data['prevalencia (%)'].mean()

                # Calcular la tasa de disminución promedio anual hasta 2030
                future_data = country_df[(country_df['year'] > 2019) & (country_df['year'] <= 2030)]
                if len(future_data) > 1:
                    slope, _, _, _, _ = linregress(future_data['year'], future_data['prevalencia (%)'])
                    annual_decrease_rate = -slope
                else:
                    annual_decrease_rate = 0

                # Determinar si la prevalencia sube o baja
                if annual_decrease_rate < 0:
                    tendencia = "disminuirá"  # Caso mayoritario: la prevalencia disminuye
                elif annual_decrease_rate > 0:
                    tendencia = "aumentará"
                else:
                    tendencia = "se mantendrá estable"
                rate_abs = abs(annual_decrease_rate)
                mensaje = (
                    f"Para {country_df['pais'].iloc[0]}, la prevalencia de anemia tuvo un promedio de "
                    f"{avg_prevalence_2000_2019:.2f}% entre 2000 y 2019. "
                    f"Con base en las proyecciones, se estima que la prevalencia {tendencia} a una tasa promedio anual de "
                    f"{rate_abs:.2f}% hacia el año 2030."
                )
                return mensaje

            # Función para graficar prevalencias en base a países seleccionados
            def plot_selected_countries_plotly(countries_selected):
                if not countries_selected:
                    st.warning("Por favor selecciona al menos un país.")
                    return

                fig = go.Figure()
                mensajes = []

                for country in countries_selected:
                    country_data = completar_anios(data_historico_pais_est, country)
                    # Generar el mensaje estadístico
                    mensaje = obtener_estadisticas_mensaje(country_data)
                    mensajes.append(mensaje)

                    # Dividir datos por período (histórico y proyecciones por separado)
                    before_2020 = country_data[country_data['year'] < 2020]
                    from_2020_onwards = country_data[country_data['year'] >= 2020]

                    # Obtener el color del país
                    country_color = colors[country]

                    # Gráfico histórico antes de 2020 (línea sólida)
                    fig.add_trace(go.Scatter(
                        x=before_2020['year'],
                        y=before_2020['prevalencia (%)'],
                        mode='lines+markers',
                        name=f"{country} (Histórico)",
                        hovertemplate="Prevalencia: %{y:.2f}<extra></extra>",
                        line=dict(color=country_color)
                    ))

                    # Gráfico proyectado desde 2020 en adelante (línea punteada)
                    fig.add_trace(go.Scatter(
                        x=from_2020_onwards['year'],
                        y=from_2020_onwards['prevalencia (%)'],
                        mode='lines+markers',
                        name=f"{country} (Proyectado)",
                        hovertemplate="Prevalencia: %{y:.2f}<extra></extra>",
                        line=dict(color=country_color, dash='dot')
                    ))

                    #Interseccion
                    fig.add_trace(go.Scatter(
                        x=country_data[(country_data['year'] >= 2019) & (country_data['year'] <= 2020)]['year'],
                        y=country_data[(country_data['year'] >= 2019) & (country_data['year'] <= 2020)]['prevalencia (%)'],
                        mode='lines+markers',
                        line=dict(color=country_color, dash='dot'),
                        hoverinfo="skip",
                        showlegend=False
                    ))

                    # Etiqueta desplazada hacia la derecha de 2030
                    year_2030_data = from_2020_onwards[from_2020_onwards['year'] == 2030]
                    if not year_2030_data.empty:
                        prev_2030 = year_2030_data['prevalencia (%)'].values[0]
                        fig.add_annotation(
                            x=2030.6,  # Etiqueta fuera de los límites de 2030
                            y=prev_2030,
                            text=country,
                            showarrow=False,
                            font=dict(size=10, color=country_color),
                            xanchor='left',
                            align='left'
                        )

                # Diseño del gráfico
                fig.update_layout(
                    title={
                        'text': 'Prevalencia histórica y futura de anemia',
                        'x': 0.5,
                        'xanchor': 'center',
                    },
                    xaxis=dict(
                        title=None,
                        showline=True,
                        linecolor='black',
                        ticks='outside',
                        tickwidth=1,
                        tickangle=45,
                        tickvals=list(range(2000, 2031))
                    ),
                    yaxis=dict(
                        title="Prevalencia (%)",
                        showline=True,
                        linewidth=1,
                        linecolor='black',
                    ),
                    showlegend=True,
                    legend_title='Países',
                    template="plotly_white"
                )

                # Mostrar el gráfico en Streamlit
                st.plotly_chart(fig)

                # Mostrar los mensajes estadísticos
                for mensaje in mensajes:
                    st.text(mensaje)


            # Crear un multiselect para seleccionar países
            selected_countries = st.multiselect('Selecciona los países', country_data, placeholder="Elija un país")

            # Actualizar el gráfico según selección de países
            if selected_countries:
                plot_selected_countries_plotly(selected_countries)
            else:
                st.warning("Por favor selecciona al menos un país.")

            st.markdown("""
            ## 📊 Reflexiones sobre los Datos y Proyecciones
    
            El análisis de los datos históricos revela un comportamiento importante: si bien la prevalencia global de la anemia infantil ha mostrado una **tendencia decreciente desde los años 2000**, esta mejora ha ocurrido a un ritmo **moderado a lento**. Este hecho es significativo porque refleja que, aunque existen avances globales en nutrición y desarrollo infantil, estos no han sido lo suficientemente acelerados como para lograr una reducción más sustancial.
    
            #### Puntos Clave:
            1. **Tendencia General:** La prevalencia promedio a nivel mundial ha disminuido desde niveles cercanos al 45% en el año 2000 hasta valores alrededor del 40% al cierre del 2019 (según los datos históricos). Sin embargo, esta reducción representa menos del 1% anual en promedio.
            
            2. **Proyección Futura:** El modelo predictivo sugiere que, si las condiciones observadas en las últimas dos décadas permanecen constantes, el porcentaje global podría alcanzar valores cercanos al 35% para el año 2030. Aunque esto indica una mejora progresiva en términos absolutos, podría argumentarse que el ritmo no es lo suficientemente acelerado para cumplir objetivos globales más ambiciosos.
            
            3. **Limitaciones del Análisis:** Es crucial tener presente que las proyecciones aquí expuestas asumen que las tendencias pasadas continuarán inalteradas. Factores disruptivos —por ejemplo, pandemias globales o intervenciones masivas— podrían cambiar radicalmente las trayectorias proyectadas.

            """)




    elif viz_menu == "Factores Relacionados":
        st.markdown("""
        # 🛠️ Factores relacionados con la anemia infantil

        En los análisis anteriores, hemos explorado una serie de visualizaciones descriptivas enfocándonos en el panorama general de la anemia infantil. Hasta este punto, hemos identificado que **el nivel de ingresos es un factor con potencial impacto** en la prevalencia de esta enfermedad. Sin embargo, para profundizar más allá de este primer enfoque, es crucial preguntarnos: ¿qué otros factores socioeconómicos podrían estar conectados con la anemia infantil?

        En esta sección, vamos a centrar nuestra atención en **Nigeria**, un caso relevante dado el contexto socioeconómico del país y los datos disponibles. Para este caso, contamos con valores específicos de **niveles de anemia** y una amplia variedad de indicadores socioeconómicos que pueden ayudarnos a entender mejor este fenómeno.

        El objetivo principal no es solo observar una relación entre variables, sino también empezar a explorar patrones y posibles correlaciones que nos permitan **enriquecer el análisis**. Esto no solo nos lleva a interpretar con mayor profundidad la situación de Nigeria, sino también a generar insights aplicables para otros contextos.   
        """)

        st.markdown("""
                ## 1. Factor Riqueza

                La riqueza, como indicador socioeconómico, siempre ha estado bajo el reflector cuando hablamos de salud pública y bienestar infantil. Aunque previamente hemos explorado el nivel de ingresos a nivel nacional utilizando datos de World Bank, esta perspectiva es más **macroeconómica** y se centra en recibir información respecto a los grupos económicos generales de un país. Sin embargo, el panorama se vuelve más interesante cuando comenzamos a analizar cómo los niveles específicos de riqueza en las familias y comunidades afectan directamente la prevalencia de anemia en niños.

                En este punto, el objetivo será analizar un gráfico de barras apiladas que nos permita visualizar las diferencias en los niveles de anemia infantil dentro de **varios niveles específicos de riqueza interna en Nigeria**.

                Ahora bien, pasemos al gráfico para explorar estas diferencias.
                """)
        data = pd.read_csv("data/datos_limpios_transformados.csv", sep=';')

        # Tratar la variable 'Smokes' como categórica
        data['Smokes'] = data['Smokes'].map({0: 'No', 1: 'Sí'})

        # Tratar la variable 'Anemia_Level' como categórica
        anemia_mapping = {0: 'Medio', 1: 'Moderado', 2: 'No anémico', 3: 'Severo'}
        data['Anemia_Level'] = data['Anemia_Level'].map(anemia_mapping)

        # Tratar la variable 'Wealth_Index' como categórica con las nuevas categorías
        wealth_mapping = {
            0: 'Medio',
            1: 'Pobre',
            2: 'Pobreza extrema',
            3: 'Rico',
            4: 'Riqueza alta'
        }
        data['Wealth_Index'] = data['Wealth_Index'].map(wealth_mapping)

        # Tratar la variable 'Iron_Supplements' como categórica
        data['Iron_Supplements'] = data['Iron_Supplements'].map({0: 'No sabe', 1: 'No', 2: 'Si'})

        # Tratar la variable 'Iron_Supplements' como categórica
        data['Residence_Type'] = data['Residence_Type'].map({0: 'Rural', 1: 'Urbana'})

        # **PASOS PREVIOS DE TRANSFORMACIÓN DE LOS DATOS**

        # Contar las observaciones para cada combinación de Anemia y Riqueza
        contado = data.groupby(['Anemia_Level', 'Wealth_Index']).size().reset_index(name='Count')

        # Calcular el total por cada categoría de Wealth_Index
        contado['Total_Wealth_Index'] = contado.groupby('Wealth_Index')['Count'].transform('sum')

        # Calcular el porcentaje dentro de cada Wealth_Index
        contado['Percentage'] = (contado['Count'] / contado['Total_Wealth_Index']) * 100

        # Redondear los porcentajes a un solo decimal
        contado['Percentage'] = contado['Percentage'].round(1)

        # Definir el orden específico para Wealth_Index y Anemia_Level
        orden_wealth = ['Pobreza extrema', 'Pobre', 'Medio', 'Rico', 'Riqueza alta']
        orden_anemia = ['No anémico', 'Moderado', 'Medio', 'Severo']

        # Convertir Wealth_Index y Anemia_Level en variables categóricas con orden específico
        contado['Wealth_Index'] = pd.Categorical(contado['Wealth_Index'], categories=orden_wealth, ordered=True)
        contado['Anemia_Level'] = pd.Categorical(contado['Anemia_Level'], categories=orden_anemia, ordered=True)

        # Ordenar los datos de acuerdo al orden categórico definido
        contado = contado.sort_values(by=['Wealth_Index', 'Anemia_Level'])

        # **CREAR GRÁFICO DE BARRAS APILADAS HORIZONTALES EN PLOTLY GO**

        # Definir colores para los niveles de anemia
        colores_anemia = {
            'No anémico': '#626efa',
            'Moderado': '#ee543b',
            'Medio': '#01cc95',
            'Severo': '#aa62fb'
        }

        fig = go.Figure()

        # Añadir trazas individuales por nivel de anemia
        for anemia_level in orden_anemia:
            nivel_data = contado[contado['Anemia_Level'] == anemia_level]
            fig.add_trace(go.Bar(
                x=nivel_data['Percentage'],
                y=nivel_data['Wealth_Index'],
                orientation='h',
                name=anemia_level,
                marker=dict(color=colores_anemia[anemia_level]),
                text=nivel_data['Percentage'],  # Inserta porcentajes dentro de las barras
                textposition='inside',  # Mostrar texto en el interior de las barras
                insidetextanchor='middle',
                hovertemplate=(f"<b>Anemia:</b> {anemia_level}<br>"
                               "<b>Riqueza:</b> %{y}<br>"
                               "<b>Porcentaje:</b> %{x:.1f}%<extra></extra>")
            ))

        # Configurar el diseño del gráfico
        fig.update_layout(
            title={
                'text': 'Nivel de anemia infantil según nivel de riqueza',
                'x': 0.5,  # Centrar título horizontalmente
                'xanchor': 'center',
                'font': dict(size=20)
            },
            barmode='stack',  # Apilar las barras
            xaxis=dict(
                title='Porcentaje (%)',
                tickformat='.1f',
                showgrid=False,
                gridcolor='lightgray',
                zeroline=False,
                linecolor='black',
                showline=True,
            ),
            yaxis=dict(
                title=None,
                categoryorder='array',
                categoryarray=orden_wealth,  # Asegurar orden lógico en eje Y
                showline=True,
                linecolor='black',
                showgrid=False
            ),
            plot_bgcolor='white',
            legend=dict(
                title='Niveles de anemia',
                orientation="h",  # Leyenda horizontal debajo del gráfico
                yanchor="top",
                y=-0.2,
                xanchor="center",
                x=0.5,
            ),
            margin=dict(l=40, r=20, t=50, b=80),  # Ajuste de márgenes interno

        )

        # Mostrar gráfico en Streamlit
        st.plotly_chart(fig)

        st.markdown("""
        ## 2. Factor Consumo de Hierro

        El consumo de suplementos de hierro es un tema clave en la discusión sobre la anemia infantil, no solo en Nigeria, sino a nivel global. En el caso de Nigeria, contamos con datos específicos que nos permiten explorar cuántos niños han recibido **suplementos de hierro**, un elemento esencial en la prevención y tratamiento de la anemia. Este dato es valioso porque nos brinda una perspectiva práctica: **¿realmente el acceso a suplementos mejora los niveles de anemia infantil?**

        La anemia infantil en países como Nigeria, aunque asociada a múltiples factores socioeconómicos, también está profundamente influenciada por **deficiencias en micronutrientes esenciales como el hierro**. La suplementación adecuada podría ser una herramienta efectiva para reducir los niveles de anemia, especialmente en poblaciones vulnerables. Sin embargo, para validar esta hipótesis, es necesario analizar los datos directamente.

        En este apartado, presentaremos dos gráficos de pie con el propósito de abordar desde dos ángulos diferentes la relación entre el consumo de suplementos de hierro y los niveles de anemia infantil:
        1. El primero mostrará la distribución de niveles de anemia en niños que **sí consumen suplementos de hierro**
        2. El segundo mostrará la distribución de niveles de anemia en niños que **no consumen suplementos de hierro**
                        """)

        # Filtrar datos según el valor de Iron_Supplements
        data_yes = data[data['Iron_Supplements'] == 'Si']
        data_no = data[data['Iron_Supplements'] == 'No']

        # Contar la frecuencia de cada categoría de Anemia_Level
        counts_yes = data_yes['Anemia_Level'].value_counts().reset_index()
        counts_yes.columns = ['Anemia_Level', 'Count']

        counts_no = data_no['Anemia_Level'].value_counts().reset_index()
        counts_no.columns = ['Anemia_Level', 'Count']


        # Crear gráfico de pie para Iron_Supplements = "Sí"
        fig_yes = go.Figure(data=[
            go.Pie(
                labels=counts_yes['Anemia_Level'],
                values=counts_yes['Count'],
                marker=dict(colors=[colores_anemia[level] for level in counts_yes['Anemia_Level']]),
                hole=0.4,  # Hacerlo tipo dona
                textinfo='label+percent',  # Mostrar etiquetas y porcentaje
                hoverinfo='label+value',  # Mostrar etiquetas y valores en el hover
                pull=[0.05] * len(counts_yes)  # Separar ligeramente cada segmento
            )
        ])
        fig_yes.update_layout(
            title=dict(text='Anemia en consumidores de hierro', x=0.32, font=dict(size=16)),
            showlegend=False
        )

        # Crear gráfico de pie para Iron_Supplements = "No"
        fig_no = go.Figure(data=[
            go.Pie(
                labels=counts_no['Anemia_Level'],
                values=counts_no['Count'],
                marker=dict(colors=[colores_anemia[level] for level in counts_no['Anemia_Level']]),
                hole=0.4,  # Hacerlo tipo dona
                textinfo='label+percent',
                hoverinfo='label+value',
                pull=[0.05] * len(counts_no)
            )
        ])
        fig_no.update_layout(
            title=dict(text='Anemia en no consumidores de hierro', x=0.32, font=dict(size=16)),
            showlegend=False
        )

        # Combinar los gráficos lado a lado con subplots usando Streamlit
        col1, col2 = st.columns(2)

        with col1:
            st.plotly_chart(fig_yes, use_container_width=True)

        with col2:
            st.plotly_chart(fig_no, use_container_width=True)

        st.markdown("""
        ## 3. Factor Tipo de Residencia

        El lugar en el que viven los niños, ya sea en áreas **rurales** o **urbanas**, juega un papel crucial en su desarrollo y bienestar, incluyendo su estado de salud. En el caso de la anemia infantil en Nigeria, este aspecto no es una excepción. El **tipo de residencia** puede influir en factores como el acceso a alimentos nutritivos, servicios básicos de salud, agua potable, saneamiento y, por supuesto, a suplementos de hierro.
        Históricamente, se ha observado que las áreas rurales tienden a estar en desventaja respecto a las urbanas por múltiples razones: recursos más limitados, falta de infraestructura y menores ingresos promedio. Esto podría traducirse en **mayores niveles de anemia infantil** en estas regiones. Por otro lado, las zonas urbanas, aunque cuentan con más recursos, también tienen desafíos propios: densidad poblacional elevada, contraste en la distribución de recursos entre barrios y, en algunos casos, dependencia de dietas menos naturales.
        
        Para profundizar en este análisis, se presenta un gráfico de barras horizontales que compara las distribuciones absolutas de los diferentes niveles de anemia según el tipo de residencia: urbana y rural. Este enfoque nos permite observar, por ejemplo, cuántos niños identificados con anemia severa pertenecen a cada contexto residencial, para así poder comparar ambos escenarios.        
                                """)

        # Contar las observaciones por combinación de 'Anemia_Level' y 'Residence_Type', especificando 'observed=False'
        # Contar las observaciones por combinación de 'Anemia_Level' y 'Residence_Type', especificando 'observed=False'
        data_count_res = data.groupby(['Anemia_Level', 'Residence_Type'], observed=False).size().reset_index(
            name='count')

        # Modificar los valores de 'count' a negativos cuando 'Residence_Type' sea 'Rural'
        data_count_res['count'] = data_count_res.apply(
            lambda row: -row['count'] if row['Residence_Type'] == 'Rural' else row['count'], axis=1)

        # Calcular el porcentaje tomando el valor absoluto de 'count'
        total_per_anemia = data_count_res.groupby('Anemia_Level', observed=False)['count'].transform(
            lambda x: x.abs().sum())
        data_count_res['percentage'] = (data_count_res['count'].abs() / total_per_anemia) * 100

        # Invertir los porcentajes cuando 'Residence_Type' sea 'Rural'
        data_count_res['percentage'] = data_count_res.apply(
            lambda row: -row['percentage'] if row['Residence_Type'] == 'Rural' else row['percentage'], axis=1)

        # Cambiar el orden de los niveles de anemia: "Severo" arriba y "No anémico" abajo
        orden_anemia = ["No anémico", "Moderado", "Medio", "Severo"]
        data_count_res['Anemia_Level'] = pd.Categorical(
            data_count_res['Anemia_Level'], categories=orden_anemia, ordered=True
        )
        data_count_res = data_count_res.sort_values(by='Anemia_Level')
        # Crear el gráfico con Plotly Go
        fig = go.Figure()

        color_map = {"Rural": "#1f77b4", "Urbana": "#ff7f0e"}

        # Añadir trazas para cada tipo de residencia
        for residence in ['Rural', 'Urbana']:
            residencia_data = data_count_res[data_count_res['Residence_Type'] == residence]
            fig.add_trace(go.Bar(
                x=residencia_data['count'],
                y=residencia_data['Anemia_Level'],
                name=residence,
                orientation='h',
                marker_color=color_map[residence],
                customdata=residencia_data[['percentage', 'count']].abs(),  # Para el hover personalizado
                hovertemplate=(
                    "<b>Tipo de Residencia:</b> " + residence + "<br>"
                    "<b>Nivel de Anemia:</b> %{y}<br>"
                    "<b>Número de Observaciones:</b> %{customdata[1]}<br>"
                    "<b>Porcentaje:</b> %{customdata[0]:.1f}%<extra></extra>"
                )
            ))

        # Configurar diseño del gráfico con ejes claros
        fig.update_layout(
            title={
                'text': 'Nivel de anemia según el tipo de residencia',
                'x': 0.5,
                'xanchor': 'center',
                'font': dict(size=18, color='black'),
            },
            barmode='relative',  # Permitir valores positivos y negativos apilados horizontalmente
            xaxis=dict(
                title="Niños contabilizados",
                titlefont=dict(size=14, color='black'),
                tickfont=dict(size=12, color='black'),
                showgrid=False,
                gridcolor='lightgray',
                zeroline=True,
                zerolinecolor="white",
                linecolor='white',
                linewidth=1,
                range=[-3000, 3000],
                tickvals=[-3000, -2000, -1000, 0, 1000, 2000, 3000],  # Personalizar valores del eje X
                ticktext=["3000", "2000", "1000", "0", "1000", "2000","3000"],  # Mostrar los valores sin signos negativos
            ),
            yaxis=dict(
                title="Nivel de Anemia",
                titlefont=dict(size=14, color='black'),
                tickfont=dict(size=12, color='black'),
                showgrid=False,
                linecolor='white',
                linewidth=1,
            ),
            legend=dict(
                title="Tipo de Residencia",
                orientation="h",
                yanchor="bottom",
                y=-0.3,
                xanchor="center",
                x=0.05,
            ),
            plot_bgcolor='white',
            template="simple_white",
            margin=dict(t=50, b=80)
        )

        # Mostrar gráfico en Streamlit
        st.plotly_chart(fig)



elif menu == "Conclusiones":
    st.title("Conclusiones")
    # Queda pendiente

elif menu == "Equipo":
    st.title("El equipo detrás del proyecto")
    # Queda pendiente



