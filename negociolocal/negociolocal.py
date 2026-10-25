import reflex as rx

# --- CONFIGURACIÓN DE COLORES Y ESTILOS (Beige & Dark Gold) ---
COLOR_BG = "#F4EBE1"
COLOR_CARD = "#EAE0D3"
COLOR_ACCENT_GRADIENT = "linear-gradient(135deg, #B8860B 0%, #996515 50%, #745100 100%)"
COLOR_TEXT_WHITE = "#2C221E"
COLOR_TEXT_MUTED = "#6B5B52"
COLOR_BORDER = "#D6C7B2"
COLOR_GOLD_DARK = "#8B5A2B"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Great+Vibes&family=Montserrat:wght@400;600;800&display=swap"
]

# --- ESTADO DEL MENÚ ---
class MenuState(rx.State):
    is_menu_open: bool = False

    def toggle_menu(self):
        self.is_menu_open = not self.is_menu_open

    def close_menu(self):
        self.is_menu_open = False


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Logo y marca
            rx.hstack(
                rx.image(src="logo.png", width="45px", height="45px", border_radius="full"),
                rx.vstack(
                    rx.text("slogan", font_family="'Great Vibes', cursive", size="6", color=COLOR_GOLD_DARK),
                    rx.text("NOMBRE DEL NEGOCIO", font_family="'Montserrat', sans-serif", font_weight="bold", size="1", letter_spacing="1.5px", color=COLOR_GOLD_DARK),
                    spacing="0",
                ),
                align="center",
                spacing="3",
            ),
            rx.spacer(),
            # Botón Pedir Cita (Topbar)
            rx.link(
                rx.button(
                    "Pide Cita",
                    background=COLOR_ACCENT_GRADIENT,
                    color="#FFFFFF",
                    radius="full",
                    size="2",
                    padding_x="22px",
                    font_weight="bold",
                    cursor="pointer",
                    _hover={"opacity": "0.9", "transform": "scale(1.03)"},
                    transition="all 0.2s ease",
                ),
                href="link a la agenda en línea",
                is_external=True,
            ),
            
            # Contenedor del menú hamburguesa
            rx.box(
                rx.icon(
                    tag="menu",
                    size=30,
                    color=COLOR_GOLD_DARK,
                    cursor="pointer",
                    padding="6px",
                    border_radius="8px",
                    on_click=MenuState.toggle_menu,
                    _hover={"background_color": "rgba(139, 90, 43, 0.12)"},
                ),
                # Panel desplegable lateral
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.text("MENÚ", font_weight="bold", size="3", color=COLOR_GOLD_DARK, letter_spacing="2px"),
                            rx.spacer(),
                            rx.icon(tag="x", size=24, color=COLOR_GOLD_DARK, cursor="pointer", on_click=MenuState.close_menu),
                            width="100%",
                            padding_bottom="20px",
                            border_bottom=f"1px solid {COLOR_BORDER}",
                        ),
                        rx.vstack(
                            rx.link(
                                rx.hstack(rx.icon(tag="home", size=20), rx.text("Inicio", size="4", font_weight="500"), spacing="3"),
                                href="#inicio",
                                on_click=MenuState.close_menu,
                                color=COLOR_TEXT_WHITE,
                                underline="none",
                                padding="14px",
                                width="100%",
                                border_radius="8px",
                                _hover={"background_color": COLOR_CARD, "color": COLOR_GOLD_DARK, "padding_left": "20px"},
                                transition="all 0.2s ease",
                            ),
                            rx.link(
                                rx.hstack(rx.icon(tag="user", size=20), rx.text("Sobre nosotros", size="4", font_weight="500"), spacing="3"),
                                href="#sobre-nosotros",
                                on_click=MenuState.close_menu,
                                color=COLOR_TEXT_WHITE,
                                underline="none",
                                padding="14px",
                                width="100%",
                                border_radius="8px",
                                _hover={"background_color": COLOR_CARD, "color": COLOR_GOLD_DARK, "padding_left": "20px"},
                                transition="all 0.2s ease",
                            ),
                            rx.link(
                                rx.hstack(rx.icon(tag="scissors", size=20), rx.text("Servicios", size="4", font_weight="500"), spacing="3"),
                                href="#servicios",
                                on_click=MenuState.close_menu,
                                color=COLOR_TEXT_WHITE,
                                underline="none",
                                padding="14px",
                                width="100%",
                                border_radius="8px",
                                _hover={"background_color": COLOR_CARD, "color": COLOR_GOLD_DARK, "padding_left": "20px"},
                                transition="all 0.2s ease",
                            ),
                            rx.link(
                                rx.hstack(rx.icon(tag="clock", size=20), rx.text("Horarios", size="4", font_weight="500"), spacing="3"),
                                href="#horarios",
                                on_click=MenuState.close_menu,
                                color=COLOR_TEXT_WHITE,
                                underline="none",
                                padding="14px",
                                width="100%",
                                border_radius="8px",
                                _hover={"background_color": COLOR_CARD, "color": COLOR_GOLD_DARK, "padding_left": "20px"},
                                transition="all 0.2s ease",
                            ),
                            spacing="2",
                            width="100%",
                            padding_top="20px",
                        ),
                        rx.spacer(),
                        rx.link(
                            rx.button(
                                "RESERVA TU CITA AHORA",
                                width="100%",
                                background=COLOR_ACCENT_GRADIENT,
                                color="#FFFFFF",
                                size="3",
                                font_weight="bold",
                                radius="medium",
                            ),
                            href="link a la agenda en línea",
                            is_external=True,
                            width="100%",
                        ),
                        height="100%",
                        padding="30px 24px",
                    ),
                    position="fixed",
                    top="0",
                    right="0",
                    width=["85vw", "350px"],
                    height="100vh",
                    background_color=COLOR_BG,
                    box_shadow="-10px 0px 30px rgba(0, 0, 0, 0.2)",
                    border_left=f"1px solid {COLOR_BORDER}",
                    opacity=rx.cond(MenuState.is_menu_open, "1", "0"),
                    pointer_events=rx.cond(MenuState.is_menu_open, "auto", "none"),
                    transform=rx.cond(MenuState.is_menu_open, "translateX(0)", "translateX(100%)"),
                    transition="all 0.35s cubic-bezier(0.16, 1, 0.3, 1)",
                    z_index="2000",
                ),
                position="relative",
            ),
            align="center",
            spacing="4",
            width="100%",
            max_width="1100px",
            margin="0 auto",
            padding_x="20px",
            padding_y="12px",
        ),
        position="fixed",
        top="0",
        left="0",
        width="100%",
        background_color="rgba(244, 235, 225, 0.94)",
        backdrop_filter="blur(12px)",
        border_bottom=f"1px solid {COLOR_BORDER}",
        z_index="1000",
    )

def hero() -> rx.Component:
    return rx.box(
        rx.html(
            """
            <video autoplay loop muted playsinline preload="auto" style="
                position: absolute; 
                top: 0; 
                left: 0; 
                width: 100%; 
                height: 100%; 
                object-fit: cover; 
                object-position: center top; 
                z-index: 0;
                will-change: transform;
            ">
                <source src="/hero_video.mp4" type="video/mp4" />
            </video>
            """
        ),
        rx.box(
            position="absolute",
            top="0",
            left="0",
            width="100%",
            height="100%",
            background="linear-gradient(to bottom, rgba(244, 235, 225, 0.75) 60%, rgba(244, 235, 225, 1) 100%)",
            z_index="1",
        ),
        rx.vstack(
            #rx.text("apdm", font_family="'Great Vibes', cursive", size="8", color=COLOR_GOLD_DARK),
            rx.heading(
                "NOMBRE DEL NEGOCIO",
                font_family="'Montserrat', sans-serif",
                size="9",
                weight="bold",
                align="center",
                color=COLOR_GOLD_DARK,
                letter_spacing="2px",
            ),
            rx.text(
                "SECTOR DE NEGOCIO",
                font_family="'Montserrat', sans-serif",
                size="4",
                color=COLOR_GOLD_DARK,
                letter_spacing="4px",
                text_transform="uppercase",
            ),
            rx.text(
                "Breve descripción \n del negocio.",
                size="3",
                color=COLOR_TEXT_MUTED,
                align="center",
                white_space="pre-line",
                max_width="550px",
            ),
            # Botón con ancho seguro en móvil para que no se corte
            rx.link(
                rx.button(
                    "Reserva Aquí tu Cita",
                    background=COLOR_ACCENT_GRADIENT,
                    color="white",
                    size="2",
                    radius="full",
                    padding_x=["20px", "32px"],
                    max_width="100%",
                    font_weight="bold",
                    cursor="pointer",
                    _hover={"transform": "translateY(-2px)"},
                    transition="all 0.2s ease",
                ),
                href="link a la agenda en línea",
                is_external=True,
                width=["100%", "auto"],
                display="flex",
                justify_content="center",
            ),
            align="center",
            justify="center",
            spacing="4",
            max_width="900px",
            width="100%",
            height="100%",
            margin="0 auto",
            padding_x="20px",
            padding_top="80px",
            position="relative",
            z_index="2",
        ),
        id="inicio",
        position="relative",
        width="100%",
        height="65vh",
        min_height="480px",
        overflow="hidden",
    )

def sobre_nosotros() -> rx.Component:
    return rx.box(
        rx.grid(
            rx.vstack(
                rx.text("CONÓCENOS", size="1", weight="bold", color=COLOR_GOLD_DARK, letter_spacing="2px"),
                rx.heading("Sobre Nosotros", size="7", weight="bold", color=COLOR_GOLD_DARK, font_family="'Montserrat', sans-serif"),
                rx.text(
                    "Breve descripción \n del negocio.",
                    size="3",
                    color=COLOR_TEXT_MUTED,
                    align="left",
                    white_space="pre-line",
                    line_height="1.6",
                ),
                align_items="start",
                spacing="3",
                justify="center",
            ),
            rx.box(
                rx.image(
                    src="/marta_studio.jpg",
                    width="100%",
                    height="380px",
                    object_fit="cover",
                    border_radius="16px",
                    border=f"1px solid {COLOR_BORDER}",
                ),
                width="100%",
            ),
            columns=rx.breakpoints(initial="1", md="2"),
            spacing="6",
            align_items="center",
            max_width="1000px",
            margin="0 auto",
            padding_x="20px",
        ),
        padding_y="80px",
        id="sobre-nosotros",
        width="100%",
    )

def servicio_card(titulo: str, descripcion: str, img_src: str) -> rx.Component:
    return rx.vstack(
        rx.image(
            src=img_src,
            width="100%",
            height="140px",
            object_fit="cover",
            border_radius="12px",
        ),
        rx.hstack(
            rx.heading(titulo, size="4", weight="bold", color=COLOR_GOLD_DARK, font_family="'Montserrat', sans-serif"),
            rx.spacer(),
            width="100%",
            align="center",
        ),
        rx.text(descripcion, size="2", color=COLOR_TEXT_MUTED, line_height="1.5"),
        padding="20px",
        background_color=COLOR_CARD,
        border=f"1px solid {COLOR_BORDER}",
        radius="large",
        width="100%",
        spacing="3",
        _hover={"border_color": COLOR_GOLD_DARK, "transform": "translateY(-3px)"},
        transition="all 0.2s ease",
    )

def servicios() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("SERVICIOS & TRATAMIENTOS", size="5", weight="bold", color=COLOR_GOLD_DARK, letter_spacing="2px"),
            rx.grid(
                servicio_card("Servicio 1", "Descripción", "/imagen.jpg"),
                servicio_card("Servicio 2", "Descripción", "/imagen.jpg"),
                servicio_card("Servicio 3", "Descripción", "/imagen.jpg"),
                servicio_card("Servicio 4", "Descripción", "/imagen.jpg"),
                columns=rx.breakpoints(initial="1", sm="2"),
                spacing="4",
                width="100%",
                padding_top="20px",
            ),
            rx.text(
                "Si te interesa alguno de nuestros servicios, infórmate más detalladamente sobre su tiempo y precio ",
                rx.link(
                    "aquí",
                    href="link a la agenda en línea",
                    is_external=True,
                    color=COLOR_GOLD_DARK,
                    font_weight="bold",
                    text_decoration="underline",
                    _hover={"opacity": "0.8"},
                ),
                ".",
                size="3",
                color=COLOR_TEXT_MUTED,
                align="center",
                padding_top="20px",
            ),
            align="center",
            spacing="3",
            max_width="900px",
            margin="0 auto",
            padding_x="20px",
        ),
        padding_y="80px",
        id="servicios",
        width="100%",
    )

def horarios_y_ubicacion() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.grid(
                rx.vstack(
                    rx.text("HORARIOS", size="1", weight="bold", color=COLOR_GOLD_DARK, letter_spacing="2px"),
                    rx.heading("Cuándo visitarnos", size="5", weight="bold", color=COLOR_GOLD_DARK),
                    rx.vstack(
                        rx.hstack(rx.text("Lunes y Martes", weight="bold", color=COLOR_TEXT_WHITE, size="2"), rx.spacer(), rx.text("Horario", color=COLOR_TEXT_MUTED, size="2"), width="100%"),
                        rx.hstack(rx.text("Miércoles", weight="bold", color=COLOR_TEXT_WHITE, size="2"), rx.spacer(), rx.text("Horario", color=COLOR_GOLD_DARK, size="2"), width="100%"),
                        rx.hstack(rx.text("Jueves y Viernes", weight="bold", color=COLOR_TEXT_WHITE, size="2"), rx.spacer(), rx.text("Horario", color=COLOR_TEXT_MUTED, size="2"), width="100%"),
                        rx.hstack(rx.text("Sábados", weight="bold", color=COLOR_TEXT_WHITE, size="2"), rx.spacer(), rx.text("Horario", color=COLOR_TEXT_MUTED, size="2"), width="100%"),
                        rx.hstack(rx.text("Domingos", weight="bold", color=COLOR_TEXT_WHITE, size="2"), rx.spacer(), rx.text("Horario", color=COLOR_GOLD_DARK, size="2"), width="100%"),
                        spacing="3",
                        width="100%",
                        padding_top="10px",
                    ),
                    padding="30px",
                    background_color=COLOR_CARD,
                    border=f"1px solid {COLOR_BORDER}",
                    radius="large",
                    width="100%",
                    spacing="3",
                ),
                rx.vstack(
                    rx.text("UBICACIÓN", size="1", weight="bold", color=COLOR_GOLD_DARK, letter_spacing="2px"),
                    rx.heading("Dónde estamos", size="5", weight="bold", color=COLOR_GOLD_DARK),
                    rx.vstack(
                        rx.text("Nombre del Negocio", weight="bold", color=COLOR_TEXT_WHITE, size="2"),
                        rx.text("Dirección", color=COLOR_TEXT_MUTED, size="2"),
                        rx.text("Ciudad", color=COLOR_TEXT_MUTED, size="2"),
                        spacing="1",
                        width="100%",
                        padding_top="10px",
                    ),
                    rx.spacer(),
                    rx.link(
                        rx.button(
                            "Cómo llegar",
                            background="transparent",
                            color=COLOR_GOLD_DARK,
                            border=f"1px solid {COLOR_GOLD_DARK}",
                            radius="full",
                            width="100%",
                            size="2",
                            font_weight="bold",
                            cursor="pointer",
                            _hover={"background_color": COLOR_BG},
                        ),
                        href="link de la ubicación",
                        is_external=True,
                        width="100%",
                    ),
                    padding="30px",
                    background_color=COLOR_CARD,
                    border=f"1px solid {COLOR_BORDER}",
                    radius="large",
                    width="100%",
                    spacing="3",
                ),
                rx.vstack(
                    rx.text("RESERVAS", size="1", weight="bold", color=COLOR_GOLD_DARK, letter_spacing="2px"),
                    rx.heading("Cita Previa Online", size="5", weight="bold", color=COLOR_GOLD_DARK),
                    rx.text("Elige el día y la hora que mejor te vengan a través de nuestra agenda.", size="2", color=COLOR_TEXT_MUTED),
                    rx.spacer(),
                    rx.link(
                        rx.button(
                            "Ver Disponibilidad Aquí",
                            background=COLOR_ACCENT_GRADIENT,
                            color="white",
                            radius="full",
                            width="100%",
                            size="3",
                            font_weight="bold",
                            cursor="pointer",
                        ),
                        href="link a la agenda en línea",
                        is_external=True,
                        width="100%",
                    ),
                    padding="30px",
                    background_color=COLOR_CARD,
                    border=f"1px solid {COLOR_BORDER}",
                    radius="large",
                    width="100%",
                    spacing="3",
                ),
                columns=rx.breakpoints(initial="1", md="3"),
                spacing="5",
                width="100%",
            ),
            max_width="1100px",
            margin="0 auto",
            padding_x="20px",
        ),
        padding_y="80px",
        id="horarios",
        width="100%",
    )

def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            #rx.text("apdm", font_family="'Great Vibes', cursive", size="7", color=COLOR_GOLD_DARK),
            rx.heading("NOMBRE DEL NEGOCIO", size="2", weight="bold", color=COLOR_GOLD_DARK, letter_spacing="2px"),
            rx.hstack(
                rx.link(
                    rx.html(
                        f"""
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="{COLOR_GOLD_DARK}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <rect width="20" height="20" x="2" y="2" rx="5" ry="5"/>
                            <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/>
                            <line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/>
                        </svg>
                        """
                    ),
                    href="link a Instagram/Redes sociales del negocio",
                    is_external=True,
                    _hover={"transform": "scale(1.15)", "opacity": "0.8"},
                    transition="all 0.2s ease",
                ),
                rx.link(
                    rx.hstack(
                        rx.icon(tag="phone", size=20, color=COLOR_GOLD_DARK),
                        rx.text("123 45 67 89", size="2", weight="medium", color=COLOR_GOLD_DARK),
                        align="center",
                        spacing="2",
                    ),
                    href="tel:123456789",
                    is_external=True,
                    _hover={"transform": "scale(1.05)", "opacity": "0.8"},
                    transition="all 0.2s ease",
                ),
                align="center",
                spacing="5",
            ),
            rx.text("© 2026 Nombre del Negocio. Todos los derechos reservados.", size="1", color=COLOR_TEXT_MUTED),
            align="center",
            spacing="3",
            padding_y="40px",
        ),
        background_color=COLOR_BG,
        border_top=f"1px solid {COLOR_BORDER}",
        width="100%",
    )

smooth_scroll_style = rx.html(
    """
    <style>
        html {
            scroll-behavior: smooth;
        }
    </style>
    """
)

def index() -> rx.Component:
    return rx.theme(
        smooth_scroll_style,
        rx.box(
            navbar(),
            hero(),
            sobre_nosotros(),
            servicios(),
            horarios_y_ubicacion(),
            footer(),
            background_color=COLOR_BG,
            min_height="100vh",
            width="100%",
        ),
        accent_color="amber",
        gray_color="sand",
        radius="large",
    )

app = rx.App(
    stylesheets=STYLESHEETS,
    style={
        "html": {"scroll_behavior": "smooth"},  
        "h1": {"color": COLOR_GOLD_DARK},
        "h2": {"color": COLOR_GOLD_DARK},
        "h3": {"color": COLOR_GOLD_DARK},
        "h4": {"color": COLOR_GOLD_DARK},
        "h5": {"color": COLOR_GOLD_DARK},
        "h6": {"color": COLOR_GOLD_DARK},
        ".rt-Heading": {"color": COLOR_GOLD_DARK},
        "a": {"color": COLOR_GOLD_DARK},
    },
)

app.add_page(index, title="Nombre del Negocio", route="/")