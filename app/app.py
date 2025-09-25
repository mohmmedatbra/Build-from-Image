import reflex as rx
from app.state import AppState
from app.components.auth_pages import role_selection_page, login_page
from app.components.dashboards import (
    student_dashboard,
    professor_dashboard,
    admin_dashboard,
)


def index() -> rx.Component:
    return rx.el.main(
        rx.match(
            AppState.current_page,
            ("role_selection", role_selection_page()),
            ("login", login_page()),
            ("student_dashboard", student_dashboard()),
            ("professor_dashboard", professor_dashboard()),
            ("supervisor_dashboard", admin_dashboard()),
            role_selection_page(),
        ),
        class_name="font-['Lato'] bg-slate-50",
        dir="rtl",
    )


app = rx.App(
    theme=rx.theme(appearance="light", accent_color="blue"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700;900&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, title="Smart Cloud")