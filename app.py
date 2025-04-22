import streamlit as st
from pathlib import Path
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(
    page_title="Fichas de Jugadores",
    page_icon="⚽",
    layout="wide"
)

# Datos de ejemplo de fortalezas (1–10) para cada jugador
radar_data = {
    "Axel Rimoldi Ayas": {
        "Anticipación": 9,
        "Juego Aéreo": 8,
        "Salida de Balón": 8,
        "Inteligencia Táctica": 8,
        "Físico": 8
    },
    "Adam Segura Calderón": {
        "Visión de Juego": 9,
        "Finalización": 8,
        "Pase Corto": 8,
        "Desmarque": 6,
        "Resistencia": 8
    },
    "Manuel Serrano Díaz": {
        "Control y Visión": 9,
        "Recuperación": 6,
        "Versatilidad": 8,
        "Creatividad": 9,
        "Juego Aéreo": 5
    },
    "Ismael Ruesca Godino": {
        "Posicionamiento": 9,
        "Salida de Balón": 8,
        "Coraje Defensivo": 7,
        "Adaptabilidad": 8,
        "Visión de Juego": 7
    },
}

# Diccionario de datos de los jugadores
players = {
    "Axel Rimoldi Ayas": {
        "photo": "./img/axel-rimoldi.png",
        "crest": "./img/santafe.png",
        "video": "https://youtu.be/AFFAabY7BhQ",
        "description": (
            "**Axel Rimoldi Ayas**\n"
            "- **Edad:** 2007 (2.º año juvenil)\n"
            "- **Club:** SantaFe (Liga Nacional Gr. XIII)\n"
            "- **Posición principal:** Defensa central (diestro y zurdo), también lateral derecho e izquierdo.\n"
            "\n"
            "Axel ha emergido como un auténtico baluarte en la retaguardia de SantaFe. Con una combinación explosiva de anticipación y fortaleza física, se impone sin miedo en el uno contra uno y domina el juego aéreo tanto en tareas defensivas como en acciones a balón parado ofensivas. Su comprensión táctica le permite organizar la línea defensiva y leer las intenciones del rival antes de que se desarrollen.\n"
            "\n"
            "**Fortalezas:**\n"
            "- 🛡️ Anticipación milimétrica: corta trayectorias antes de que los atacantes reciban el balón.\n"
            "- ✈️ Juego aéreo contundente: neutraliza centros y se convierte en un recurso ofensivo en corners y faltas laterales.\n"
            "- 🎯 Salida jugada: fiabilidad con el pie para iniciar la construcción desde atrás.\n"
            "- 🧠 Inteligencia táctica: posicionamiento y liderazgo para coordinar el bloque defensivo.\n"
            "\n"
            "**Potencial de crecimiento:**\n"
            "Con un enfoque en entrenamiento de velocidad de reacción y fortalecimiento de la resistencia, Axel tiene la proyección para dar el salto a categorías superiores y convertirse en un pilar inamovible para cualquier equipo que apueste por una defensa sólida y bien construida."
        )
    },
    "Adam Segura Calderón": {
        "photo": "./img/adam.png",
        "crest": "./img/puerto.png",
        "video": "https://youtu.be/L-4XzcjZekI",
        "description": (
            "**Adam Segura Calderón**\n"
            "- **Edad:** 2007 (2.º año juvenil)\n"
            "- **Club:** Puerto Malagueño (Liga Nacional Gr. XIII)\n"
            "- **Posición principal:** Centrocampista ofensivo / mediapunta.\n"
            "\n"
            "Adam es la brújula creativa del mediocampo ofensivo. Con una visión de juego privilegiada, sabe cuándo pausar el ritmo para combinar cerca y cuándo acelerar para romper líneas con pases largos quirúrgicos. Sus diagonales desde la banda izquierda abren huecos en la defensa rival y generan oportunidades de disparo desde media distancia.\n"
            "\n"
            "**Fortalezas:**\n"
            "- 🎯 Juego visionario: identifica pases verticales y cambios de juego con precisión milimétrica.\n"
            "- 🔥 Capacidad de finalización: aporta gol y asistencias gracias a su golpeo seco y ajustado.\n"
            "- 🤝 Toque asociativo: domina el pase corto y las combinaciones rápidas en espacios reducidos.\n"
            "- ⚡ Desmarque en diagonal: se coloca inteligentemente para recibir entre líneas y filtrar balones.\n"
            "\n"
            "**Potencial de crecimiento:**\n"
            "Con un plan de mejora centrado en resistencia aeróbica y toma de decisiones bajo presión, Adam puede consolidarse como el ’10’ ideal para proyectos que exigen construcción combinativa y fluidez ofensiva."
        )
    },
    "Manuel Serrano Díaz": {
        "photo": "./img/manuel.png",
        "crest": "./img/santafe.png",
        "video": "https://youtu.be/Nk__6WPAt44",
        "description": (
            "**Manuel Serrano Díaz**\n"
            "- **Edad:** 2006 (3.er año juvenil)\n"
            "- **Club:** SantaFe (Liga Nacional Gr. XIII)\n"
            "- **Posición principal:** Mediocentro (defensivo y ofensivo).\n"
            "\n"
            "Manuel es el motor que enlaza defensa y ataque con elegancia. Su manejo de balón es excepcional: recibe en zonas de presión y distribuye con calma, habilitando a sus compañeros. Tiene la capacidad de asociarse junto a un pivote defensivo para iniciar la jugada o proyectarse hacia zonas de creación con libertad para filtrar el pase decisivo.\n"
            "\n"
            "**Fortalezas:**\n"
            "- 🎩 Control y visión: dicta el tempo del partido con toques precisos y cambios de orientación efectivos.\n"
            "- 🧲 Recuperación limpia: recupera balones en la medular sin perder compostura.\n"
            "- 🔄 Versatilidad posicional: se adapta al rol de distribuidor o generador de juego según el plan táctico.\n"
            "- 💡 Creatividad ofensiva: rompe esquemas con pases filtrados y arrastres de marca.\n"
            "\n"
            "**Potencial de crecimiento:**\n"
            "Con un programa de fortalecimiento físico y trabajo específico en juego aéreo defensivo, Manuel puede alcanzar un nivel diferencial, aportando tanto en fases de contención como en construcción de juego con maestría."
        )
    },
    "Ismael Ruesca Godino": {
        "photo": "./img/ismael.png",
        "crest": "./img/marbella.jpg",
        "video": "https://youtu.be/4298-i9oUz0",
        "description": (
            "**Ismael Ruesca Godino**\n"
            "- **Edad:** 2011 (2.º año infantil)\n"
            "- **Club:** Atlético Marbella Paraíso (División de Honor)\n"
            "- **Posición principal:** Mediocentro defensivo / pivote.\n"
            "\n"
            "Ismael es un diamante en bruto en la medular. Su lectura de juego y colocación le permiten interceptar pases y cortar la línea de presión rival antes de que se desarrolle el ataque. A pesar de su juventud, demuestra temple para sacar el balón jugado con criterio y aportar equilibrio al bloque.\n"
            "\n"
            "**Fortalezas:**\n"
            "- ⚙️ Posicionamiento perfecto: siempre en el sitio justo para desactivar la transición rival.\n"
            "- 🚀 Salida rápida: acelera la jugada tras recuperación con pases limpios.\n"
            "- 🛡️ Coraje defensivo: no rehúye el choque y contribuye en las tareas de cobertura.\n"
            "- 🔄 Adaptabilidad: puede retrasarse a central o acompañar la construcción según la necesidad del equipo.\n"
            "\n"
            "**Potencial de crecimiento:**\n"
            "Con un plan de mejora centrado en desarrollo de fuerza y coordinación, Ismael tiene todo el futuro por delante para convertirse en un pivote de élite, capaz de comandar la medular en niveles competitivos superiores."
        )
    }
}

# Función para dibujar radar
def plot_radar(player_name: str):
    metrics = radar_data.get(player_name)
    if not metrics:
        st.info("No hay datos de métricas para este jugador.")
        return
    categories = list(metrics.keys())
    values = list(metrics.values())
    # cerrar el polígono
    categories += categories[:1]
    values += values[:1]

    fig = go.Figure(
        data=go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name=player_name
        )
    )
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,10]
            )
        ),
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20)
    )
    st.subheader("📊 Radar de Fortalezas y Debilidades")
    st.plotly_chart(fig, use_container_width=True)


# Sidebar de selección
st.sidebar.image("./img/logo.png", width=400)
selected = st.sidebar.radio("Jugadores:", list(players.keys()))

# Ficha principal
player = players[selected]
st.markdown(f"# {selected}")
clubs = Path(player['crest'])
photos = Path(player['photo'])

col1, col2 = st.columns([1, 2], gap="large")
with col1:
    # Creamos dos sub-columnas: una para la foto y otra para el escudo
    img_col, crest_col = st.columns([2, 1], gap="small")
    with img_col:
        if photos.exists():
            st.image(
                str(photos),
                caption=selected,
                use_container_width=True
            )
        else:
            st.warning("Imagen de jugador no encontrada.")
    with crest_col:
        if clubs.exists():
            st.image(
                str(clubs),
                width=150,
                caption="Escudo del club"
            )
        else:
            st.warning("Escudo del club no encontrado.")

with col2:
    st.markdown(player['description'])
    plot_radar(selected)


# Video
st.divider()
st.subheader("🎥 Video Destacado")
st.video(player.get('video'), start_time=0)
