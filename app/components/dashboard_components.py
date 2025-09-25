import reflex as rx
from app.state import AppState, StatCard, ScheduleItem, RecentFile, RecentActivity


def dashboard_header(title: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("bell", size=24, class_name="text-gray-500 cursor-pointer"),
            rx.icon("search", size=24, class_name="text-gray-500 cursor-pointer"),
            on_click=AppState.go_to_role_selection,
        ),
        rx.el.div(
            rx.el.p(title, class_name="font-bold text-lg"),
            rx.icon("user", size=20, class_name="text-gray-500"),
            class_name="flex items-center gap-2",
        ),
        class_name="flex items-center justify-between p-4 bg-white",
    )


def welcome_card(user: str, message: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                f"صباح الخير، {user}!", class_name="font-bold text-lg text-purple-800"
            ),
            rx.el.p(message, class_name="text-sm text-purple-600"),
            class_name="text-right",
        ),
        rx.el.div(
            rx.icon("sun", size=24, class_name="text-yellow-500"),
            class_name="p-3 bg-white rounded-full",
        ),
        class_name="flex flex-row-reverse items-center justify-between w-full bg-purple-100 rounded-2xl p-5",
    )


def system_status_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p("حالة النظام: نشط", class_name="font-bold text-lg text-green-800"),
            rx.el.p("كل الخدمات تعمل بشكل طبيعي", class_name="text-sm text-green-600"),
            class_name="text-right",
        ),
        rx.el.div(
            rx.icon("check_check", size=24, class_name="text-green-500"),
            class_name="p-3 bg-white rounded-full",
        ),
        class_name="flex flex-row-reverse items-center justify-between w-full bg-green-100 rounded-2xl p-5",
    )


def section_header(title: str, link_text: str = "عرض الكل") -> rx.Component:
    return rx.el.div(
        rx.el.a(link_text, href="#", class_name="text-sm text-blue-600 font-medium"),
        rx.el.h2(title, class_name="font-bold text-xl text-gray-800"),
        class_name="flex justify-between items-center w-full",
    )


def stat_card_component(card: StatCard) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                card["icon"], size=24, class_name=card["color"].replace("bg-", "text-")
            ),
            class_name=f"p-3 {card['color']} rounded-lg",
        ),
        rx.el.div(
            rx.el.p(
                card["value"], class_name="font-bold text-2xl text-gray-800 text-right"
            ),
            rx.el.p(card["title"], class_name="text-sm text-gray-500 text-right"),
        ),
        class_name="bg-white p-4 rounded-xl shadow-sm border border-gray-100 flex flex-col items-end gap-2",
    )


def quick_access_card(card: StatCard) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                card["icon"], size=24, class_name=card["color"].replace("bg-", "text-")
            ),
            class_name=f"p-4 {card['color']} rounded-xl mb-3",
        ),
        rx.el.p(card["title"], class_name="text-sm text-gray-600 font-semibold"),
        class_name="bg-white p-4 rounded-xl shadow-sm border border-gray-100 flex flex-col items-center justify-center cursor-pointer hover:shadow-md transition-shadow",
    )


def schedule_item_component(item: ScheduleItem) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(item["title"], class_name="font-semibold text-gray-800"),
            rx.el.p(
                f"{item['time']} | {item['location']}",
                class_name="text-sm text-gray-500",
            ),
            class_name="text-right",
        ),
        rx.el.div(
            rx.icon(item["icon"], size=20, class_name=item["color"]),
            class_name="p-3 bg-gray-100 rounded-full ml-4",
        ),
        class_name="flex flex-row-reverse items-center bg-white p-4 rounded-xl shadow-sm border border-gray-100 w-full",
    )


def recent_file_component(item: RecentFile) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(item["title"], class_name="font-semibold text-gray-800"),
            rx.el.p(item["subtitle"], class_name="text-sm text-gray-500"),
            class_name="text-right",
        ),
        rx.el.div(
            rx.icon(item["icon"], size=20, class_name=item["color"]),
            class_name="p-3 bg-gray-100 rounded-full ml-4",
        ),
        class_name="flex flex-row-reverse items-center justify-between bg-white p-4 rounded-xl shadow-sm border border-gray-100 w-full",
    )


def student_file_component(item: RecentFile) -> rx.Component:
    return rx.el.div(
        rx.el.p(item["size"], class_name="text-sm font-medium text-gray-500"),
        rx.el.div(
            rx.el.div(
                rx.el.p(item["title"], class_name="font-semibold text-gray-800"),
                rx.el.p(item["subtitle"], class_name="text-sm text-gray-500"),
                class_name="text-right",
            ),
            rx.el.div(
                rx.icon(item["icon"], size=20, class_name=item["color"]),
                class_name="p-3 bg-gray-100 rounded-full ml-4",
            ),
            class_name="flex flex-row-reverse items-center",
        ),
        class_name="flex items-center justify-between bg-white p-4 rounded-xl shadow-sm border border-gray-100 w-full",
    )


def announcement_component(item: ScheduleItem) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(item["title"], class_name="font-semibold text-gray-800"),
            rx.el.p(item["time"], class_name="text-sm text-gray-500 leading-relaxed"),
            rx.el.p(item["location"], class_name="text-xs text-gray-400 mt-2"),
            class_name="text-right",
        ),
        rx.el.div(
            rx.icon(item["icon"], size=20, class_name=item["color"]),
            class_name="p-3 bg-white rounded-full ml-4",
        ),
        class_name="flex flex-row-reverse items-start bg-yellow-50 p-4 rounded-xl border border-yellow-200 w-full",
    )


def activity_item_component(item: RecentActivity) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(item["title"], class_name="font-semibold text-gray-800"),
            rx.el.p(item["subtitle"], class_name="text-sm text-gray-500"),
            class_name="text-right",
        ),
        rx.el.div(
            rx.icon(item["icon"], size=20, class_name=item["color"]),
            class_name="p-3 bg-gray-100 rounded-full ml-4",
        ),
        class_name="flex flex-row-reverse items-center justify-between bg-white p-4 rounded-xl shadow-sm border border-gray-100 w-full",
    )