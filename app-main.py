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

    # Concepto 1: ¿Qué es la Anemia?
    col1, col2 = st.columns([3, 2])  # Relación 3:2 para que el texto esté a la izquierda y la imagen a la derecha

    with col1:
        st.markdown(
            """
            <style>
            .concepto-container {
                background-color: rgba(0, 0, 0, 0.7);  /* Fondo semi-transparente */
                padding: 40px;
                border-radius: 15px;
                color: white;
                margin-bottom: 30px;
                height: auto;
            }
            .concepto-container h3 {
                text-align: center;
                font-size: 1.8em;
            }
            .concepto-container p {
                text-align: justify;
                font-size: 1.2em;
            }
            </style>
            <div class="concepto-container">
                <h3>¿Qué es la Anemia?</h3>
                <p>La <strong>anemia</strong> es una condición médica caracterizada por una insuficiencia de glóbulos rojos o hemoglobina en la sangre.
                Esta carencia provoca que los tejidos del cuerpo no reciban suficiente oxígeno, lo cual puede generar síntomas como fatiga,
                debilidad, mareos y palidez. En los niños, la anemia puede afectar seriamente su desarrollo físico y cognitivo, ya que durante
                sus primeros años de vida, el crecimiento y el desarrollo cerebral necesitan niveles adecuados de oxígeno.</p>
                <p>
                Existen diferentes tipos de anemia, siendo la más común la <strong>anemia ferropénica</strong>, causada por una deficiencia de hierro.
                El hierro es un componente crucial de la hemoglobina, la proteína que permite a los glóbulos rojos transportar oxígeno. Sin
                suficiente hierro, el cuerpo produce menos hemoglobina y, por ende, menos glóbulos rojos saludables.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.image("https://elmen.pe/wp-content/uploads/2023/03/Anemia-scaled.jpg", use_container_width=True)

    # Concepto 2: Efectos y poblacion vulnerable
    col1, col2 = st.columns([2, 3])  # Relación 3:2 para que el texto esté a la izquierda y la imagen a la derecha

    with col2:
        st.markdown(
            """
            <style>
            .effect-container {
                background-color: rgba(0, 0, 0, 0.7);  /* Fondo semi-transparente */
                padding: 30px;
                border-radius: 15px;
                color: white;
                margin-bottom: 30px;
                height: auto;
            }
            .effect-container h3 {
                text-align: center;
                font-size: 1.8em;
            }
            .effect-container p {
                text-align: justify;
                font-size: 1.2em;
            }
            </style>
            <div class="effect-container">
                <h3>Efectos y condiciones de vulnerabilidad</h3>
                <p>La <strong>anemia</strong> se asocia con una variedad de efectos adversos en la salud y puede incrementar la vulnerabilidad a otras condiciones médicas. Entre los efectos más destacados se encuentran la <strong>disminución de la capacidad física y la función cognitiva</strong>, que puede impactar en el rendimiento laboral y académico.</p>
                <p>A nivel celular, la falta de oxígeno afecta el <strong>metabolismo energético</strong>, lo que puede provocar una disminución en la capacidad de regeneración celular y una mayor susceptibilidad a infecciones. Esto se debe a que las células inmunitarias también requieren oxígeno para funcionar eficazmente.</p>
                <p>En general, las poblaciones vulnerables, como los niños, mujeres gestantes y las personas mayores, son especialmente susceptibles a los efectos de la anemia debido a necesidades fisiológicas particulares o disminución de la capacidad de absorción de nutrientes esenciales.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col1:
        st.image("https://elcomercio.pe/resizer/xTR28Ck_-oiLTyn23B7uMPCtrHM=/1200x0/smart/filters:format(jpeg):quality(75)/arc-anglerfish-arc2-prod-elcomercio.s3.amazonaws.com/public/ZQWV7YV4N5GFPGQDX2PS7DNYXI.jpg", use_container_width=True)

    # Concepto 3: Anemia infantil
    col1, col2 = st.columns([3, 2])  # Relación 3:2 para que el texto esté a la izquierda y la imagen a la derecha

    with col1:
        st.markdown(
            """
            <style>
            .infantil-container {
                background-color: rgba(0, 0, 0, 0.7);  /* Fondo semi-transparente */
                padding: 30px;
                border-radius: 15px;
                color: white;
                margin-bottom: 30px;
                height: auto;
            }
            .infantil-container h3 {
                text-align: center;
                font-size: 1.8em;
            }
            .infantil-container p {
                text-align: justify;
                font-size: 1.2em;
            }
            </style>
            <div class="infantil-container">
                <h3>Anemia Infantil</h3>
                <p>La <strong>anemia infantil</strong> es una condición particularmente preocupante debido a los efectos graves que puede tener en el desarrollo físico y mental de los niños. Durante los primeros años de vida, el crecimiento rápido y el desarrollo cerebral demandan una cantidad adecuada de oxígeno, y la anemia compromete este suministro crítico.</p>
                <p>Los niños con anemia severa pueden sufrir retrasos en el crecimiento, dificultades en el aprendizaje, y una baja capacidad de respuesta inmunológica, haciéndolos más vulnerables a infecciones. Además, la anemia infantil puede presentar síntomas menos evidentes como irritabilidad, falta de concentración y apatía, que muchas veces pasan inadvertidos pero afectan significativamente la calidad de vida y aprovechamiento escolar del niño.</p>
                <p>La causa principal de anemia infantil es la <strong>deficiencia de hierro</strong>, pero también hay que considerar que factores socioeconómicos juegan un rol crítico, ya que los niños en hogares con limitados recursos tienen mayor riesgo de sufrir esta condición debido a una dieta inadecuada y acceso limitado a servicios de salud.</p>
                <p>En este informe, se presentará información detallada sobre la prevalencia de la anemia infantil en diferentes regiones del mundo, los esfuerzos gubernamentales y comunitarios realizados para abordar este problema, así como algunos estudios que nos proporcionen un panorama más completo de este problema.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown("<br><br><br><br>", unsafe_allow_html=True)
        st.image("imagenes/anemia.jpg", use_container_width=True)


    st.subheader("¿Cómo se ha vivido la anemia alrededor del mundo?")

    st.write("La anemia infantil es un problema que afecta a millones de niños en todo el mundo, con impactos duraderos en su salud, "
             "desarrollo y calidad de vida. Sin embargo, diferentes gobiernos han emprendido iniciativas específicas para abordar "
             "este desafío, implementando políticas públicas, programas de suplementación y campañas educativas contra esta condición. "
             "En esta sección, exploraremos un conjunto de noticias que destacan las acciones gubernamentales más relevantes y "
             "algunos momentos históricos clave en la lucha contra la anemia infantil, permitiéndonos reflexionar sobre los "
             "esfuerzos globales realizados y los aprendizajes obtenidos en diversos contextos.")

    # Configuración del contenido en Markdown para los slides
    content_markdown = """
    # Noticias de la anemia en el mundo
    ---
    ## Perú
    ![](https://resources.sbcnoticias.com/sbcnoticias/2020/11/shutterstock_1780081652-696x350.jpg)
    --
    
    <!-- .slide: data-background-color="#283747" -->
    **"Tan Fuertes como el Hierro": Iniciativa ha ayudado en la recuperación de niños diagnosticados con anemia**
    
    <u>20 de mayo de 2022</u>
    
    La campaña “Tan Fuertes como el Hierro” ya está cosechando resultados impresionantes. Más de 1,000 familias han sido educadas en alimentación nutritiva y más de 1,200 frascos de suplemento nutricional de hierro han sido entregados gratuitamente para el tratamiento de la anemia infantil. Además, las proyecciones apuntan a la recuperación de, por lo menos, el 70% de los niños diagnosticados con anemia después del tratamiento y la implementación de las estrategias educativas.
    https://rpp.pe/campanas/valor-compartido/tan-fuertes-como-el-hierro-iniciativa-ha-ayudado-en-la-recuperacion-de-ninos-diagnosticados-con-anemia-noticia-1504586?ref=rpp
    --
    
    <!-- .slide: data-background-color="#283747" -->
    **Minsa proyecta mejores resultados en lucha contra la anemia para el 2022**
    
    <u>20 de mayo de 2022</u>
    
    Pese al contexto de la pandemia por la COVID-19, los resultados alcanzados durante el 2021 en la reducción de la prevalencia de anemia de 40.1 % a 38.8 % en menores de 6 a 35 meses a nivel nacional (Encuesta Endes 2021), el Ministerio de Salud (Minsa) viene proyectando, para fines del 2022, mejores resultados en la lucha contra la anemia, debido a la reactivación de acciones multisectoriales para reforzar la estrategia de prevención y control de la enfermedad en el país.
    https://www.gob.pe/institucion/minsa/noticias/608484-minsa-proyecta-mejores-resultados-en-lucha-contra-la-anemia-para-el-2022

    ---
    ## Argentina
    <div style="text-align: center;">
        <img src="https://i.pinimg.com/736x/2b/1b/96/2b1b961dffad584769549a42eb0fc943.jpg" width="500" height="600">
    </div>
    --
    
    <!-- .slide: data-background-color="#283747" -->
    **El presidente presentó el programa Fierritas para prevenir la anemia infantil mediante un complemento producido en laboratorio público**
    
    <u>07 de septiembre de 2022</u>
    
    Fierritas es un complemento nutricional de hierro, zinc y vitamina A para niñas y niños entre los 6 y 24 meses de vida con falta de adherencia al tratamiento con Sulfato Ferroso. Se presenta en sobres individuales de 1 gramo y contiene micronutrientes en polvo que se pueden mezclar fácilmente con los alimentos de los lactantes cuando comienzan con la alimentación sólida.
    Para esta primera etapa, el ministerio de Salud definió la producción de sobres de Fierritas por una inversión de casi $250.000.000 que serán distribuidos dentro de la canasta de los 1.000 días del Remediar, comenzando en las regiones de mayor prevalencia de anemia: NOA y NEA.
    https://www.argentina.gob.ar/noticias/el-presidente-presento-el-programa-fierritas-para-prevenir-la-anemia-infantil-mediante-un
    ---
    ## Colombia
    ![](https://i0.wp.com/viajerosporcolombia.com/wp-content/uploads/Cartagena-de-Indias.jpg?w=1200&ssl=1)
    --
    
    <!-- .slide: data-background-color="#283747" -->
    **Minsalud cuenta con estrategia para prevenir anemia en primera infancia**
    
    <u>04 de noviembre de 2020</u>
    
    La Estrategia Nacional para la prevención y control de las deficiencias de Micronutrientes en Colombia 2014-2021, que tiene como principal objetivo "Prevenir y reducir las deficiencias de micronutrientes en la población colombiana, con énfasis en niños y niñas hasta 12 años, gestantes y mujeres en edad fértil", propone 5 líneas de acción:
    1.   Diversificación de la alimentación
    2.   Fortalecimiento de acciones prioritarias
    3.   Fortificación
    4.   Biofortificación o fortificación biológica de los alimentos
    5.   Suplementación con Micronutrientes
    
https://www.minsalud.gov.co/Paginas/Minsalud-cuenta-con-estrategia-para-prevenir-anemia-en-primera-infancia-.aspx
    ---
    ## Guatemala
    ![](https://i.pinimg.com/736x/6c/45/cb/6c45cba616d0aca213f9d91db522bfed.jpg)
    --
    
    <!-- .slide: data-background-color="#283747" -->
    **Campamentos Nutrimóviles: exitoso proyecto impulsado en Guatemala para erradicar la desnutrición infantil**
    
    <u>21 de marzo de 2024</u>
    
    La iniciativa de Guatemaltecos por la Nutrición pasó por instalar lo que sus promotores han bautizado como “Campamentos Nutrimóviles”, que son unas clínicas equipadas con la última tecnología para facilitar atención médica y nutricional a las comunidades guatemaltecas.
    Según datos de la organización, el 79 % de los niños vencieron la desnutrición aguda después de implantar este proyecto en algunas zonas del país en su fase inicial. Ahora, la organización ha anunciado un segundo campamento que beneficiará a más de 19.000 residentes de San Pedro Soloma y Santa Eulalia, en Huehuetanango.
    https://www.vozdeamerica.com/a/campamentos-nutrimoviles-exitoso-proyecto-guatemala-erradicar-desnutricion-infantil/7536588.html

    ---
    ## México
    ![](https://www.landuum.com/wp-content/uploads/2023/09/pexels-luis-ariza-13808918landuum-scaled.jpg)
    --
    
    <!-- .slide: data-background-color="#283747" -->
    **IMSS desarrolla campañas para prevenir anemia entre menores**
    
    <u>18 de mayo de 2012</u>
    
    El IMSS desarrolla diversas campañas para prevenir la anemia entre los grupos más vulnerables, a través de suplementos de hierro y de pláticas sobre nutrición en las Unidades de Medicina Familiar (UMF).
    La anemia crónica en menores puede generar consecuencias severas para su desarrollo físico, intelectual y emocional, advirtió Miguel Ángel Andrade Padilla, médico pediatra y profesor del Centro de Investigación Educativa y Formación Docente de la Delegación Norte del Distrito Federal del IMSS.
    https://www.sinembargo.mx/238279/imss-desarrolla-campanas-para-prevenir-anemia-entre-menores/

    ---
    ## Bolivia
    ![](https://as1.ftcdn.net/jpg/01/40/10/50/1000_F_140105071_ia43Nfs23jz1O2eezuDdFYRvfL6dudpS.jpg)
    --
    
    <!-- .slide: data-background-color="#283747" -->
    **La anemia en niños disminuyó en 7,6 puntos porcentuales**
    
    <u>07 de abril de 2018</u>
    
    En el Día Mundial de la Salud, El Instituto Nacional de Estadística (INE), informó que la anemia en niños de 6 a 59 meses disminuyo en 7,6 puntos porcentuales, de acuerdo a la Encuesta de Demografía y Salud (EDSA) 2016, el porcentaje de anemia es de 53,7% mientras que para la ENDSA 2008 fue de 61,3%.
    Según el nivel de hemoglobina, los tipos de anemia se miden en leve 26,0 %, moderada 25,6% y severa 2,1%. Según la EDSA 2016, se registra una disminución de 7,6 puntos porcentuales en la anemia moderada y 1,1 puntos en la severa, así como un incremento de 1,1 puntos porcentuales en la anemia leve, en relación a la ENDSA 2008.
    https://www.ine.gob.bo/index.php/la-anemia-en-ninos-disminuyo-en-76-puntos-porcentuales/



    """

    # Creación del layout con columnas
    col1, col2, col3 = st.columns([1, 2, 1])  # Relación: 1:2:1 para centrar

    with col2:  # Contenido en la columna central
        response_dict = rs.slides(content_markdown, height=700, markdown_props={"data-separator-vertical":"^--$"}, config={"height": 1200})

elif menu == "Fuentes de datos":
    st.title("Fuentes de Datos")

    # Submenú Horizontal
    sub_menu = option_menu(
        menu_title="",  # Sin título en el menú horizontal
        options=["Fuente 1", "Fuente 2", "Fuente 3", "Fuente 4"],
        icons=["link-45deg", "link-45deg", "link-45deg", "link-45deg"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

    if sub_menu == "Fuente 1":
        st.subheader("World Bank")
        st.markdown("""
        La plataforma World Bank (Banco Mundial) es una fuente global y confiable de datos socioeconómicos y de desarrollo. Proporciona una amplia variedad de indicadores que permiten comprender los desafíos y avances en áreas cruciales como salud, educación, economía y medio ambiente.
        En el estudio de la anemia infantil, el World Bank ofrece información valiosa para evaluar la magnitud de esta condición y los factores asociados en distintos países y regiones. Estos datos están disponibles a través de su API de Datos Abiertos, una herramienta eficaz para acceder automáticamente a indicadores recopilados por gobiernos, organizaciones de salud y estudios científicos a nivel global.
        Esta es una breve descripción de la plataforma World Bank (Banco Mundial) y cómo se ha usado para la extracción de información sobre la anemia infantil mediante su API:
        
        **Características de la API del World Bank**
        1. Acceso a Indicadores de Salud: La API ofrece información detallada sobre indicadores específicos relacionados con la anemia infantil, como:
            - Prevalencia de anemia en niños menores de 5 años (%).
            - Desglose por país, ingresos, zona geográfica, etc.
            - Relación con otros determinantes sociales y económicos.

        2.	Datos Históricos y Comparativos: Es posible acceder a datos históricos, lo que permite analizar tendencias a lo largo del tiempo y realizar comparaciones entre distintos países o regiones.
        3.	Formato Estándar: La API entrega la información en formatos como JSON y XML, facilitando la integración con herramientas de análisis y visualización como Python, R, o plataformas de business intelligence.
        4.	Actualizaciones Frecuentes: Los datos se actualizan periódicamente, garantizando información actualizada y relevante para estudios e investigaciones sobre salud pública.

        API utilizada: http://api.worldbank.org/v2/country/ALL/indicator/SH.ANM.CHLD.ZS
        
        ![](https://gustavo-godoy.com/wp-content/uploads/Banco-mundial-1536x864.jpeg)

        
        
        """)

    elif sub_menu == "Fuente 2":
        st.subheader("Global Health Observatory (GHO)")
        st.markdown("""
        El Global Health Observatory (GHO) es una plataforma de la Organización Mundial de la Salud (OMS) dedicada a recopilar, analizar y difundir datos sobre temas de salud a nivel mundial. Proporciona acceso a una extensiva colección de indicadores, reportes y análisis que permiten tener una visión holística de las condiciones de salud a nivel global, regional y nacional.
        Para el análisis de la anemia infantil, el GHO ofrece datos detallados y actualizados que ayudan a comprender la prevalencia de esta afección y sus implicaciones en la salud pública. Esta información es crucial para investigadores, formuladores de políticas y profesionales de la salud que buscan implementar intervenciones eficaces y monitorear avances hacia metas globales como los Objetivos de Desarrollo Sostenible (ODS).
        
        **Características del Global Health Observatory**
        1.	Amplia Cobertura de Indicadores de Salud: El GHO ofrece indicadores específicos relacionados con la anemia infantil, como:
            - Prevalencia de anemia en niños menores de 5 años (%).
            - Desglose por país, ingresos, zona geográfica, etc.
        2.	Acceso a Datos en Tiempo Real: A través de su API y su portal de datos, el GHO permite acceder a información actualizada, lo que facilita el seguimiento de tendencias emergentes en la salud infantil.
        3.	Formatos de Datos Flexibles: Los datos del GHO se pueden descargar en formatos como CSV, JSON y XML, facilitando su integración con herramientas de análisis de datos como Python, R y Excel.
        4.	Datos Comparativos y Desglosados: Permite realizar comparaciones entre países, regiones y grupos demográficos, ayudando a identificar brechas en la atención de la salud y desigualdades en la prevalencia de anemia.

        API utilizada: https://ghoapi.azureedge.net/api/NUTRITION_ANAEMIA_CHILDREN_NUM
        
        ![](https://static.euronews.com/articles/stories/06/44/64/20/1920x1080_cmsv2_62a1dfd1-f77f-5f69-83e7-f6bc7f6d2cb9-6446420.jpg)

                """)

    elif sub_menu == "Fuente 3":
        st.subheader("Demographic and Health Surveys (DHS)")
        st.markdown("""
            La plataforma Demographic and Health Surveys (DHS) es una iniciativa respaldada por la Agencia de los Estados Unidos para el Desarrollo Internacional (USAID) y gestionada por ICF International. Desde 1984, se especializa en recopilar datos detallados y precisos sobre salud, población y nutrición en más de 90 países en desarrollo.
            En investigaciones relacionadas con la anemia infantil, los datos de DHS son invaluables gracias a sus encuestas exhaustivas y su rigor metodológico. Estas encuestas proporcionan información desglosada por edad, sexo y factores socioeconómicos, lo que permite identificar patrones de prevalencia y los determinantes de esta condición. La información de DHS es ampliamente utilizada por científicos, responsables de políticas y organismos de salud para diseñar e implementar estrategias de intervención efectivas.

            **Datos detallados y desglosados:**
            - DHS ofrece datos sobre la prevalencia de anemia en niños, medidos a través de pruebas de hemoglobina realizadas durante las encuestas.
            - Los datos están desglosados por edad, sexo, país, y número de encuestas realizadas como el nivel educativo de los padres y el acceso a servicios de salud.
            
            **Acceso a microdatos:**
            - DHS permite descargar microdatos (datos a nivel individual) para realizar análisis personalizados.
            - La API permite extraer datos en formatos como JSON y CSV para su análisis con lenguajes como Python o R.
            
            **Cobertura geográfica amplia:**
            - Los datos de DHS abarcan más de 90 países, especialmente en regiones de África, Asia, América Latina y el Caribe, permitiendo comparaciones internacionales y análisis regionales.
            
            **Actualizaciones periódicas:**
            - Las encuestas se realizan aproximadamente cada 5 años en los países participantes, lo que facilita el seguimiento de tendencias a lo largo del tiempo.
            
            
            APIs utilizadas: 
            - https://api.dhsprogram.com/rest/dhs/data/CN_ANMC_C_ANY
            - https://api.dhsprogram.com/rest/dhs/data/CN_ANMC_C_MLD
            - https://api.dhsprogram.com/rest/dhs/data/CN_ANMC_C_MOD
            - https://api.dhsprogram.com/rest/dhs/data/CN_ANMC_C_SEV

            ![](https://data.humdata.org/image/2022-01-08-033748.794232Screen-Shot-2022-01-08-at-10.37.03.png)
        """)
    elif sub_menu == "Fuente 4":
        st.subheader("Kaggle")
        st.markdown("""
            Kaggle es una plataforma en línea perteneciente a Google que se destaca por su enfoque en el análisis de datos, aprendizaje automático (machine learning) y competencias de ciencia de datos. Es reconocida por su activa comunidad de científicos de datos y su extenso repositorio de datasets de alta calidad y fácil acceso.
            En el análisis de la anemia infantil, Kaggle facilita la adquisición de datasets compartidos tanto por instituciones oficiales como por la comunidad de usuarios. Gracias a su API, los usuarios pueden descargar estos datasets directamente a sus entornos de trabajo, como Python o Jupyter Notebooks, agilizando el proceso de extracción y análisis de datos. Además, la plataforma ofrece notebooks y scripts de referencia que ayudan a desarrollar modelos predictivos y visualizaciones informativas.

            **Características clave de Kaggle:**
            1. Acceso a datasets diversos:
                - Datasets sobre salud infantil, anemia, nutrición y otros factores relevantes.
                - Datos aportados por investigadores, organizaciones de salud y proyectos académicos.

            2. API de Kaggle:
                - Facilita la descarga automatizada de datasets mediante comandos simples.
                - Integración sencilla con entornos de ciencia de datos como Python y bibliotecas como pandas y scikit-learn.

            3. Comunidad y recursos:
                - Acceso a notebooks, scripts y discusiones de otros usuarios para inspiración y colaboración en proyectos relacionados con la anemia infantil.

            Data utilizada: 
            https://www.kaggle.com/datasets/adeolaadesina/factors-affecting-children-anemia-level

            ![](https://opendatascience.com/wp-content/uploads/2018/12/kaggle-640x300.png)
        """)

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

        # Dashboard Principal
        st.write("### Análisis visual más detallado de la situación global e histórica de la anemia infantil")
        st.write("### Indicadores de resumen en 2019")

        # Indicadores (Méritos)
        col1, col2, col3 = st.columns([0.95, 0.7, 1.35])

        with col1:
            st.metric(label="Prevalencia Global (%)", value="39.8%", delta="-0.5% respecto al año 2015")

        with col2:
            st.metric(label="Continente más afectado", value="Africa (60.2 %)")

        with col3:
            st.subheader("Prevalencia histórica de anemia por niveles de ingresos")
            st.markdown("Los datos muestran una diferencia en los niveles de anemia infantil según el nivel de ingresos promedio de los países")

        col1, col2 = st.columns([1.55, 1.45])

        with col1:
            # Cargar los datos desde el archivo CSV
            data_historico = pd.read_csv("data/world_bank_anemia_mundial_listo.csv")

            # Crear el gráfico de líneas interactivo con Plotly
            fig = go.Figure()

            # Agregar la línea principal al gráfico
            fig.add_trace(go.Scatter(
                x=data_historico["year"],
                y=data_historico["prevalencia (%)"],
                mode='lines+markers',
                name='Prevalencia',
                line=dict(color='#636efa', width=3),
                marker=dict(size=7, color='#636efa', symbol='circle', line=dict(color='white', width=2)),
                hovertemplate="<b>Año:</b> %{x}<br><b>Prevalencia:</b> %{y:.2f}%<extra></extra>"
            ))

            fig.update_traces(line_shape='spline')

            # Personalización del diseño del gráfico
            fig.update_layout(
                title=dict(
                    text="<span style='font-size:24px; color:#1f77b4; font-family:Roboto;'><b>🌎 Prevalencia Histórica de Anemia infantil (2000-2019) 🩸</b></span>",
                    x=0.07 # Centrar el título
                ),
                xaxis=dict(
                    title="Año",
                    title_font=dict(size=16, color='black'),
                    tickfont=dict(size=14, color='black'),
                    tickmode="linear",
                    tickangle=45,  # Rotar los ticks para que no se apilen
                    range=[1999.5, 2019.5],
                    showline=True,
                    linewidth=2,
                    linecolor='gray',
                    gridcolor='lightgray'
                ),
                yaxis=dict(
                    title="Prevalencia (%)",
                    title_font=dict(size=16, color='black'),
                    tickfont=dict(size=14, color='black'),
                    range=[25, 50],  # Ajustar el rango según los datos
                    showline=True,
                    linewidth=2,
                    linecolor='gray',
                    gridcolor='lightgray'
                ),
                plot_bgcolor='rgba(240,240,240,0.95)',  # Fondo claro para el gráfico
                paper_bgcolor='white',
                margin=dict(t=100, b=100, l=80, r=80)
            )

            # Mejorar interactividad (opcional)
            fig.update_traces(marker_line_width=1.5)
            fig.update_layout(
                hovermode="x",  # Mostrar valores al pasar sobre la línea
                template="simple_white"
            )

            # Mostrar el gráfico en Streamlit (si lo necesitas)
            st.plotly_chart(fig)

        with col2:

            # Cargar datos del CSV
            data_nivelingresos = pd.read_csv("data/world_bank_anemia_ingresos_listo.csv")

            # Asegurarse de que los datos de 'year' sean numéricos
            data_nivelingresos['year'] = pd.to_numeric(data_nivelingresos['year'], errors='coerce')
            data_nivelingresos = data_nivelingresos.dropna(subset=['year', 'prevalencia (%)'])  # Eliminar filas con NaN
            data_nivelingresos['year'] = data_nivelingresos['year'].astype(int)

            # Obtener los niveles de ingresos únicos
            income_levels = sorted(data_nivelingresos['nivel de ingresos'].unique())

            # Asignar colores personalizados a cada nivel de ingresos
            colors = {
                "Bajos ingresos": "#FF5733",  # Rojo ladrillo
                "Ingresos bajos y medios": "#FFBD33",  # Amarillo cálido
                "Ingreso medio": "#5b8f68",  # Verde vibrante
                "Ingreso medio alto": "#3380FF",  # Azul moderno
                "Ingresos altos": "#9B33FF"  # Morado sofisticado
            }

            # Crear la figura Plotly
            fig = go.Figure()

            # Añadir las trazas de datos
            for i, level in enumerate(income_levels):
                # Filtrar datos por nivel de ingresos
                level_data = data_nivelingresos[data_nivelingresos['nivel de ingresos'] == level]

                # Añadir la línea al gráfico
                fig.add_trace(
                    go.Scatter(
                        x=level_data['year'],
                        y=level_data['prevalencia (%)'],
                        mode="lines+markers",
                        line=dict(color=colors.get(level, "gray"), width=2),  # Usar colores predefinidos si existen
                        marker=dict(size=6),  # Tamaño de los marcadores
                        name=level,  # Nombre del nivel de ingresos
                        hovertemplate="<b>%{name}</b><br>Año: %{x}<br>Prevalencia: %{y:.2f}%<extra></extra>",
                    )
                )

            # Añadir anotaciones cerca del último punto para cada nivel de ingresos
            y_offset = 0.5  # Ajuste vertical entre las anotaciones (evitar superposición)
            for i, level in enumerate(income_levels):
                level_data = data_nivelingresos[data_nivelingresos['nivel de ingresos'] == level]
                last_row = level_data[level_data['year'] == level_data['year'].max()]

                if not last_row.empty:
                    last_year = last_row['year'].values[0]
                    last_value = last_row['prevalencia (%)'].values[0]

                    # Añadir la anotación
                    fig.add_annotation(
                        x=last_year - 3,  # Un poco a la derecha del último año
                        y=last_value + 1.5,  # Ajuste vertical por nivel
                        text=f"<b>{level}</b>",  # Texto del nivel de ingresos
                        font=dict(size=10, color=colors.get(level, "gray")),  # Personalización de la fuente
                        showarrow=False,
                        xanchor="left",
                        align="left",
                    )

            # Configurar diseño del gráfico
            fig.update_layout(
                title= "",
                xaxis=dict(
                    title='Año',
                    tickmode='array',
                    tickvals=sorted(data_nivelingresos['year'].unique()),
                    showline=True,
                    linecolor='black',
                    ticks='outside',  # Marcas fuera del eje
                    tickwidth=1,
                    tickangle=45
                ),
                yaxis=dict(
                    title='Prevalencia (%)',
                    showline=True,
                    linewidth=1,
                    linecolor='black',
                ),
                plot_bgcolor='rgba(240,240,240,0.95)',  # Fondo blanco para mayor legibilidad
                showlegend=False,  # Eliminamos la leyenda; usamos anotaciones dinámicas
                width=900,
                height=600,  # Ajustar el tamaño del gráfico en Streamlit
                margin=dict(t=10)
            )

            # Mostrar gráfico en Streamlit
            st.plotly_chart(fig)

        col1, col2 = st.columns([1.2, 0.8])
        with col1:
            # Cargar los datos
            st.subheader("Comparador histórico de anemia infantil para cada país")
            data_historico_pais_est = pd.read_csv("data/world_bank_anemia_paises_listo.csv")
            data_historico_pais_est['year'] = pd.to_numeric(data_historico_pais_est['year'], errors='coerce')
            data_historico_pais_est['year'] = data_historico_pais_est['year'].astype(int)

            # Obtener la lista de países únicos
            countries = sorted(data_historico_pais_est['pais'].unique())


            # Asignar un color único a cada país
            def assign_colors(countries):
                colors = {}
                for country in countries:
                    # Asignamos un color aleatorio a cada país
                    colors[
                        country] = f'rgba({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)}, 0.8)'
                return colors


            colors = assign_colors(countries)


            # Función para completar los años faltantes y hacer líneas continuas
            def completar_anios(data, country):
                # Filtrar datos del país
                country_data = data[data['pais'] == country].copy()

                # Generar el rango completo de años
                all_years = pd.DataFrame({'year': range(country_data['year'].min(), country_data['year'].max() + 1)})

                # Unir con los datos originales y llenar los valores faltantes mediante interpolación
                completed_data = pd.merge(all_years, country_data, on='year', how='left')
                completed_data['prevalencia (%)'] = completed_data['prevalencia (%)'].interpolate()

                # Añadir el nombre del país
                completed_data['pais'] = country
                return completed_data


            # Función para graficar prevalencias históricas basadas en los países seleccionados
            def plot_selected_countries_plotly(countries_selected):
                if not countries_selected:
                    st.warning("Por favor selecciona al menos un país.")
                    return

                # Crear una figura
                fig = go.Figure()

                for country in countries_selected:
                    # Completar los años faltantes
                    country_data = completar_anios(data_historico_pais_est, country)

                    # Obtener el color para el país
                    country_color = colors[country]

                    # Añadir el segmento antes de 2020 (línea continua)
                    fig.add_trace(
                        go.Scatter(
                            x=country_data['year'],
                            y=country_data['prevalencia (%)'],
                            mode='lines+markers',
                            name=country,
                            hovertemplate="Prevalencia: %{y:.2f}<extra></extra>",
                            # Personalizar el tooltip sin el símbolo '%'
                            line=dict(color=country_color)  # Usamos el color del país
                        )
                    )

                    # Colocar el nombre del país ligeramente desplazado a la derecha
                    year_2019_data = country_data[country_data['year'] == 2019]
                    if not year_2019_data.empty:
                        # Obtenemos el valor de prevalencia para 2019
                        prev_2019 = year_2019_data['prevalencia (%)'].values[0]
                        fig.add_annotation(
                            x=2019 + 0.5,  # Desplazamos un poco a la derecha de 2030
                            y=prev_2019,
                            text=country,
                            showarrow=False,
                            font=dict(size=10, color=country_color),
                            xanchor='left',  # Alineación del texto a la izquierda
                            align='left'  # Alineación del texto a la izquierda
                        )

                # Ajustar el diseño del gráfico
                fig.update_layout(
                    title={
                        'text': 'Prevalencia histórica de anemia',
                        'x': 0.5,  # Centrar el título
                        'xanchor': 'center',  # Asegurar que el anclaje sea en el centro
                    },
                    xaxis=dict(
                        title=None,  # Quitar el título del eje X
                        tickangle=45,
                        showline=True,
                        linecolor='black',
                        ticks='outside',  # Mostrar marcas de graduación principales hacia el exterior
                        tickwidth=1,  # Grosor de las marcas de graduación
                        tickvals=list(
                            range(
                                data_historico_pais_est['year'].min(),
                                data_historico_pais_est['year'].max() + 1
                            )
                        )  # Asegurar que todos los años estén en el eje X
                    ),
                    yaxis=dict(
                        showline=True,  # Mostrar la línea del eje Y
                        linewidth=1,  # Definir el grosor de la línea
                        linecolor='black'  # Definir el color de la línea
                    ),
                    showlegend=True,
                    legend_title='Países',
                    yaxis_title='Prevalencia (%)',
                    template='plotly_white',
                    width=850  # Ampliar el ancho del gráfico,
                )

                # Mostrar el gráfico en Streamlit
                st.plotly_chart(fig)


            # Crear checkbox para seleccionar países
            selected_countries = st.multiselect('Selecciona los países', countries, placeholder="Elija un país")

            # Actualizar y mostrar gráfico dinámicamente según selección de países
            if selected_countries:
                plot_selected_countries_plotly(selected_countries)
            else:
                st.warning("Por favor selecciona al menos un país.")

        with col2:
            # Cargar los datos
            data_ind_anemia = pd.read_csv("data/dhs_anemia_final.csv")

            # Limpiar y renombrar columnas
            data_ind_anemia.drop(data_ind_anemia.columns[[3, 4, 6, 7, 9, 10, 12, 13]], axis=1, inplace=True)
            data_ind_anemia.rename(
                columns={
                    'Valor Cualquier': 'Valor General',
                    'Year': 'Año'
                },
                inplace=True
            )


            # Crear la Gauge con Plotly
            def create_gauge(value, country):
                """
                Crear un velocímetro circular estilizado con Plotly y una flecha personalizada.
                """
                if value < 20:
                    estado = "Anemia leve"
                elif 20 <= value < 40:
                    estado = "Anemia moderada"
                else:
                    estado = "Anemia alta"
                # Crear la figura base del gauge
                fig = go.Figure(
                    go.Indicator(
                        mode="gauge",
                        value=value,
                        gauge={
                            'axis': {'range': [0, 100], 'tickwidth': 2, 'tickcolor': "#000"},
                            'bar': {'color': "#295491"},  # Barra roja
                            'steps': [
                                {'range': [0, 20], 'color': "#32CD32"},  # Verde
                                {'range': [20, 40], 'color': "#FFD700"},  # Amarillo
                                {'range': [40, 100], 'color': "#FF4D4D"},  # Rojo
                            ],
                            'threshold': {
                                'line': {'color': "black", 'width': 4},
                                'thickness': 0.85,
                                'value': value  # Dónde apunta la aguja
                            }
                        }
                    )
                )

                # Calcular la posición de la flecha en coordenadas polares
                angle = (value / 100) * 180  # Convertir el valor a un ángulo en grados
                angle_rad = np.radians(angle)  # Convertir a radianes
                unit = np.array([np.cos(np.pi-angle_rad), np.sin(np.pi-angle_rad)])
                ro = 0.9
                ri = 0
                ax, ay = ri * unit
                x, y = ro * unit

                # Agregar la flecha al gráfico
                fig.add_annotation(
                    ax=ax,
                    ay=ay,
                    axref='x',
                    ayref='y',
                    x=x,
                    y=y,
                    xref='x',
                    yref='y',
                    showarrow=True,
                    arrowhead=3,
                    arrowsize=1,
                    arrowwidth=4,
                    arrowcolor="#e3e7e8"
                )

                fig.add_annotation(
                    ax=ax,
                    ay=ay,
                    axref='x',
                    ayref='y',
                    x=x,
                    y=y,
                    xref='x',
                    yref='y',
                    showarrow=True,
                    arrowhead=3,
                    arrowsize=1,
                    arrowwidth=4,
                    arrowcolor="black"
                )

                fig.add_trace(
                    go.Scatter(
                        x=[x], y=[y],  # Coordenadas ficticias para hover centralizado
                        mode="markers",
                        marker=dict(size=1, opacity=0),
                        hoverinfo="text",  # Muestra solo texto definido en hovertext
                        hovertext=f"<b>{estado}</b><br>Prevalencia: {value}%"
                    )
                )


                # Configuración del diseño
                fig.update_layout(
                    height=300,  # Altura del gráfico
                    margin=dict(t=70, b=10, l=70, r=70),  # Márgenes compactos
                    font=dict(color="black", family="Arial"),  # Estilo tipográfico (limpio)
                    xaxis={'showgrid': False, 'showticklabels': False, 'range': [-1, 1]},
                    yaxis={'showgrid': False, 'showticklabels': False, 'range': [0, 1]},

                )
                # Mostrar cuadrícula para facilitar el debug
                fig.update_yaxes(
                    scaleanchor="x",
                    scaleratio=1,
                )
                return fig


            # Sidebar interactivo para seleccionar el país
            st.subheader("Reportes de la gravedad de anemia infantil")
            pais_seleccionado = st.selectbox("Selecciona un país:", data_ind_anemia["Pais"].unique())

            # Datos del país seleccionado
            if pais_seleccionado:
                st.subheader(f"Prevalencia de anemia general en {pais_seleccionado} según el reporte más reciente")

                # Filtrar datos del país
                data_paises = data_ind_anemia[data_ind_anemia["Pais"] == pais_seleccionado].reset_index(drop=True)

                # Obtener el valor más reciente de "Valor Real"
                latest_year = data_paises["Año"].max()
                valor_real = data_paises[data_paises["Año"] == latest_year]["Valor General"].values[0]

                # Gauge para el valor actual
                st.plotly_chart(create_gauge(valor_real, pais_seleccionado), use_container_width=True)
                st.markdown(f"""
                    <div style="text-align: center; margin-left: 35px; margin-top: -30px; margin-bottom: -20px;">
                        <h2 style='color: black; display: inline-block;'>{valor_real}%</h2>
                    </div>
                """, unsafe_allow_html=True)
                st.markdown(f"""
                            <div style="text-align: center; margin-left: 35px; margin-top: -20px; margin-bottom: -20px;">
                                <h3 style='color: black; display: inline-block;'>{pais_seleccionado}</h3>
                            </div>
                                """, unsafe_allow_html=True)

                # Tabla bonita con Streamlit
                st.subheader("Reportes de gravedad por año")
                st.dataframe(data_paises.style.format({
                    "Año": "{:.0f}",
                    "Valor General": "{:.2f}%",
                    "Valor Leve": "{:.2f}%",
                    "Valor Moderado": "{:.2f}%",
                    "Valor Severo": "{:.2f}%"
                }).background_gradient(cmap="YlOrRd", vmin=0, vmax=60,
                                       subset=["Valor Leve", "Valor Moderado", "Valor Severo"])
                             .set_properties(**{"text-align": "center"}))  # Centrar contenido de la tabla


    elif viz_menu == "Análisis geográfico":
        # Lectura del archivo csv de prevalencia de anemia para país y continente
        data_country = pd.read_csv("data/world_bank_continentes.csv")

        col1, col2, col3 = st.columns([1.15, 0.1, 1.75])

        with col1:
            st.subheader("Veamos la situación de la anemia infantil en cada año 🌍👀")
            anio = st.slider("Seleccione un año para visualizar", 2000, 2019, 2019)
            # Filtrar los datos para el año seleccionado
            data_filtrada = data_country[data_country['date'] == anio]

            # Ordenar por el valor de anemia y seleccionar los 10 primeros
            top_10 = data_filtrada.nlargest(10, 'value')

            # Crear el gráfico con Plotly Go
            fig = go.Figure()

            # Agregar barras al gráfico
            fig.add_trace(
                go.Bar(
                    x=top_10['country.value'],
                    y=top_10['value'],
                    marker=dict(color='indianred'),
                    text=top_10['Continente'],  # Mostrar el continente al pasar el mouse
                    textposition="outside",
                    hovertemplate="<b>País:</b> %{x}<br>" +
                                  "<b>Porcentaje de Anemia:</b> %{y}%<br>" +
                                  "<b>Continente:</b> %{text}<extra></extra>"
                )
            )

            # Configurar el diseño del gráfico
            fig.update_layout(
                title=f"Top 10 países con mayor anemia infantil en {anio}",
                xaxis=dict(title="País", tickangle=-45),
                yaxis=dict(title="Porcentaje de Anemia", range=(0, 101)),
                template="plotly_white",
                title_font=dict(size=20),
                margin=dict(l=40, r=40, t=60, b=40),
                height=600
            )

            # Mostrar el gráfico
            st.plotly_chart(fig)

        with col3:
            st.subheader(f"¿Cómo la anemia infantil ha afectado a cada contintente en {anio}?")
            with st.form(key='myform', border=False):
                # Mapa 1: Anemia por Continentes
                # Crear diccionario sobre continentes

                data_recent = data_country.loc[data_country.groupby("Continente")["date"].idxmax()]
                continent_stats = (
                    data_country[data_country["date"] == anio]
                    .groupby("Continente")[["country.value", "value", "date"]]
                    .apply(lambda group: pd.Series({
                        "max_prevalence_country": group.loc[group["value"].idxmax()]["country.value"],
                        "max_prevalence_value": group["value"].max(),
                        "min_prevalence_country": group.loc[group["value"].idxmin()]["country.value"],
                        "min_prevalence_value": group["value"].min()
                    }))
                    .reset_index()
                )

                # Coordenadas aproximadas de los continentes
                locations = {
                    "Africa": [9.1, 23.7],
                    "Asia": [34.0, 100.0],
                    "Europe": [54.0, 15.0],
                    "North America": [37.0, -98.0],
                    "South America": [-15.0, -60.0],
                    "Oceania": [-20.0, 130.0]
                }

                # Crear el mapa
                m1 = folium.Map(location=[0, 0], zoom_start=2)

                for _, row in continent_stats.iterrows():
                    continent = row["Continente"]
                    tooltip_text = f"""
                                        <b>{continent}</b><br>
                                        <i>País con mayor prevalencia:</i> {row['max_prevalence_country']} ({row['max_prevalence_value']}%)<br>
                                        <i>País con menor prevalencia:</i> {row['min_prevalence_country']} ({row['min_prevalence_value']}%)
                                        """
                    folium.CircleMarker(
                        location=locations[continent],
                        radius=10,
                        color="blue",
                        fill=True,
                        fill_color="blue",
                        fill_opacity=0.6,
                        tooltip=tooltip_text,
                    ).add_to(m1)


                # Mostrar el mapa en Streamlit
                # Mapa 1: Continentes
                mapa1 = m1
                st_folium(mapa1, width=900)
                # Esconder el boton
                hide_button_style = """
                    <style>
                    button[data-testid="stBaseButton-secondaryFormSubmit"] {
                        visibility: hidden;
                    }
                    </style>
                """
                st.markdown(hide_button_style, unsafe_allow_html=True)
                submit_button = st.form_submit_button(label="",
                                                      disabled=True)
                if submit_button: pass

        st.subheader("Ahora un vistazo más completo en cada país")
        # Mapa 2: Países
        # Se mostrará como HTML debido a que Streamlit-folium no tiene compatibilidad con MarkerCluster
        # Además no es necesario la interacción dinámica con el usuario por lo que el HTML es suficiente
        tog = tog.st_toggle_switch(label="Mostrar datos totales",
                             key="Key1",
                             default_value=False,
                             label_after=False,
                             inactive_color='#D3D3D3',
                             active_color="#D3D3D3",
                             track_color="#29B5E8"
                             )
        if tog:
            with open("data/mapa_pais.html", 'r') as f:
                html_data = f.read()
                st.components.v1.html(html_data, width=1200, height=700)
        else:
            with open("data/mapa_prevalencia_max_min.html", 'r') as f:
                html_data = f.read()
                st.components.v1.html(html_data, width=1200, height=700)

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
    st.markdown(
        """
        Tras realizar un análisis exhaustivo de los datos relacionados con la anemia infantil, hemos obtenido varios hallazgos significativos que arrojan luz sobre este problema de salud pública desde diferentes perspectivas.

        **1. Resultados Generales y Tendencias Históricas:**
        - Observamos una tendencia decreciente en la prevalencia global de anemia infantil a lo largo de las últimas dos décadas, aunque esta disminución ha sido suave.
        - Se identificaron ciertas regiones donde las tasas de anemia han disminuido de manera más pronunciada, mientras que en otras, el cambio ha sido mínimo o inexistente.

        **2. Análisis Geográficos:**
        - A nivel mundial, África y el sur de Asia presentan las tasas más altas de anemia infantil, reflejando disparidades significativas en comparación con regiones como América del Norte y Europa.
        - Las diferencias intrarregionales también son notables, donde ciertos países en vías de desarrollo muestran tasas alarmantes debido a factores socioeconómicos y disponibilidad de recursos.

        **3. Análisis Predictivo:**
        - Las proyecciones hacia el año 2030 indican una leve mejora en la reducción de los casos de anemia infantil globalmente, sin embargo, el ritmo proyectado de mejora no es suficiente para erradicar la condición por completo en varios países vulnerables.
        - Factores emergentes, como cambios climáticos y económicos, podrían impactar nuestras proyecciones actuales y merecen atención para futuras evaluaciones.

        **4. Factores Relacionados con la Anemia Infantil:**
        - Aunque la muestra de análisis es aproximadamente homogénea al tratarse del país de Nigeria, los datos han mostrado diferencias lo suficientemente significativas como para definir factores relacionados con la anemia.
        - El nivel de riqueza mostró una correlación con los niveles de anemia, destacando que los niños en los sectores más pobres son los más afectados.
        - El consumo de suplementos de hierro se correlaciona con una disminución en los niveles de anemia, lo cual destaca la importancia de programas nutricionales y suplementarios.
        - Los análisis residenciales indicaron que los casos de anemia existentes, corresponden a niños que residen en áreas rurales por sobre los que viven en zonas urbanas, reflejando desigualdades en el acceso a recursos como la educación y servicios de salud.

        """
    )

elif menu == "Equipo":
    st.title("El equipo detrás del proyecto")
    # Datos del equipo
    equipo = [
        {"nombre": "Segio Santillan Tsejem", "Código": "20191314", "github": "https://github.com/SergioSantillan"},
        {"nombre": "Brisa Cielo Paredes Ballenas", "Código": "20221411", "github": "https://github.com/BrisaParedes"},
        {"nombre": "Marcell Enrique Rojas Molina", "Código": "20230411", "github": "https://github.com/marcellRojas91"},
        {"nombre": "Nagiely Sandoval Hurtado", "Código": "20220780", "github": "https://github.com/Brigiely"},
        {"nombre": "Leonardo Joaquín Frías Gómez ", "Código": "20230394", "github": "https://github.com/leonardo3010f"},
        {"nombre": "Andrea Vanesa Mamani Taipe", "Código": "20211819", "github": "https://github.com/Andrea-Mamani"},
        {"nombre": "Marcial Homero Reyes Robles", "Código": "20240731", "github": "https://github.com/Marcial03reyes"},
        {"nombre": "Giannella Teresa Galvez-Durand Bravo ", "Código": "20210945",
         "github": "https://github.com/GiaBravo"},
        {"nombre": "Catherine Antonia Ramirez Gutierrez", "Código": "20220742",
         "github": "https://github.com/CatherineandHachi"},
        {"nombre": "Justin Wess Sam Vasquez Vega", "Código": "20230416", "github": "https://github.com/JustinWessSam"},
        {"nombre": "José Ignacio Gamarra Rivas", "Código": "20180319", "github": "https://github.com/eljose1998"},
        {"nombre": "Jorge Abel Sencara Maldonado", "Código": "20231508", "github": "https://github.com/Jorge-Abel"},
        {"nombre": "Omar Zenon Sanchez Perez", "Código": "20211938", "github": "https://github.com/OmarSanchez-UNALM"},
        {"nombre": "Leonardo Jesús Ccorahua Madera", "Código": "20240701", "github": "https://github.com/leojkuz"},
        {"nombre": "Daniel Mauricio Quiroz Acho", "Código": "20220776", "github": "https://github.com/daniel-quiroz-a"}
    ]

    # Personalizar los nombres de los grupos
    group_titles = ["Módulo de Extracción de datos", "Módulo de Análisis de Datos", "Módulo de Visualización",
                    "Módulo de Documentación", "Integradores de código"]

    # Añadir CSS para mejorar el estilo de los subtítulos y miembros del equipo
    st.markdown(
        """
        <style>
        .team-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        .group-title {
            background-color: rgba(0, 0, 0, 0.8);  /* Fondo semi-transparente */
            color: white;
            border-radius: 15px;
            padding: 15px;
            width: 100%;
            text-align: center;
            margin-bottom: 20px;
            font-size: 1.5em;
        }
        .team-column {
            width: 48%;  /* Aproximadamente la mitad del ancho con espacio */
        }
        .team-member {
            background-color: rgba(0, 0, 0, 0.8);  /* Fondo semi-transparente */
            color: white;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin-bottom: 15px;
            text-align: center;  /* Centrar el texto */
        }
        .team-member h3 {
            margin: 0;
            border-bottom: 2px solid white;
            padding-bottom: 5px;
            font-size: 1.2em;
        }
        .team-member p {
            margin: 0;
            font-size: 1em;
        }
        </style>
        """, unsafe_allow_html=True
    )


    # Función para mostrar cada miembro del equipo
    def mostrar_miembro(nombre, codigo, github):
        return f"""
            <div class="team-member">
                <h3>{nombre}</h3>
                <p>Código: {codigo}</p>
                <p>GitHub: <a href="{github}" target="_blank">{github}</a></p>
            </div>
            """


    # Organizar miembros en cinco grupos específicos
    team_groups = [
        equipo[0:3],  # Primer grupo con 3 integrantes
        equipo[3:6],  # Segundo grupo con 3 integrantes
        equipo[6:9],  # Tercer grupo con 3 integrantes
        equipo[9:12],  # Cuarto grupo con 3 integrantes
        equipo[12:15]  # Quinto grupo con 3 integrantes
    ]

    st.markdown('<div class="team-container">', unsafe_allow_html=True)
    for i, group in enumerate(team_groups):
        st.markdown(f'<div class="group-title">{group_titles[i]}</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            for miembro in group[:2]:  # Primeros 2 miembros en la primera columna
                st.markdown(mostrar_miembro(miembro["nombre"], miembro["Código"], miembro["github"]),
                            unsafe_allow_html=True)
        with col2:
            for miembro in group[2:]:  # Últimos miembros en la segunda columna (puede ser 1 o 2 miembros)
                st.markdown(mostrar_miembro(miembro["nombre"], miembro["Código"], miembro["github"]),
                            unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)



