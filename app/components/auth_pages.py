import reflex as rx
from app.state import AppState


def role_card(
    icon: str, title: str, subtitle: str, color: str, role: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(icon, size=28, class_name=color.replace("bg-", "text-")),
                class_name=f"p-4 {color} rounded-xl",
            ),
            rx.el.div(
                rx.el.p(title, class_name="font-semibold text-lg text-gray-800"),
                rx.el.p(subtitle, class_name="text-gray-500"),
                class_name="text-right",
            ),
            class_name="flex flex-row-reverse items-center justify-between w-full",
        ),
        rx.icon("chevron-left", size=24, class_name="text-gray-400"),
        on_click=lambda: AppState.select_role(role),
        class_name="bg-white p-5 rounded-2xl shadow-sm border border-gray-100 flex items-center justify-between cursor-pointer hover:shadow-lg hover:border-blue-500 transition-all duration-300",
    )


def role_selection_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "تسجيل الدخول", class_name="text-3xl font-bold text-gray-800 text-right"
            ),
            rx.el.p(
                "اختر نوع الحساب للدخول إلى النظام",
                class_name="text-gray-500 text-right mt-2",
            ),
            class_name="w-full mb-10",
        ),
        rx.el.div(
            role_card("users", "طالب", "الدخول بحساب الطالب", "bg-blue-100", "student"),
            role_card(
                "briefcase",
                "أستاذ",
                "الدخول بحساب الأستاذ",
                "bg-purple-100",
                "professor",
            ),
            role_card(
                "shield", "مشرف", "الدخول بحساب المشرف", "bg-green-100", "supervisor"
            ),
            class_name="w-full space-y-4",
        ),
        rx.el.p(
            "ليس لديك حساب؟ ",
            rx.el.span(
                "تواصل مع الإدارة",
                class_name="text-blue-600 font-semibold cursor-pointer",
            ),
            class_name="text-center text-gray-500 mt-12",
        ),
        class_name="min-h-screen bg-slate-50 flex flex-col items-center justify-center p-6 w-full max-w-md mx-auto",
    )


def login_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("users", size=40, class_name="text-blue-600"),
            class_name="p-5 bg-blue-100 rounded-full mb-6",
        ),
        rx.el.h1("مرحباً بك", class_name="text-3xl font-bold text-gray-800 mb-2"),
        rx.el.p(
            "سجل دخولك للوصول إلى ملفاتك الجامعية", class_name="text-gray-500 mb-10"
        ),
        rx.el.form(
            rx.el.div(
                rx.el.label(
                    "رقم الجامعي",
                    html_for="university_id",
                    class_name="text-right w-full block mb-2 font-medium text-gray-700",
                ),
                rx.el.div(
                    rx.el.input(
                        id="university_id",
                        name="university_id",
                        placeholder="1234567",
                        class_name="w-full bg-transparent text-right focus:outline-none placeholder-gray-400 pr-4",
                    ),
                    rx.icon("user", class_name="text-gray-400"),
                    class_name="flex items-center bg-white p-4 rounded-xl shadow-sm border border-gray-200 w-full",
                ),
                class_name="mb-6 w-full",
            ),
            rx.el.div(
                rx.el.label(
                    "كلمة المرور",
                    html_for="password",
                    class_name="text-right w-full block mb-2 font-medium text-gray-700",
                ),
                rx.el.div(
                    rx.el.input(
                        id="password",
                        name="password",
                        type="password",
                        placeholder="••••••••",
                        class_name="w-full bg-transparent text-right focus:outline-none placeholder-gray-400 pr-4",
                    ),
                    rx.icon("lock", class_name="text-gray-400"),
                    class_name="flex items-center bg-white p-4 rounded-xl shadow-sm border border-gray-200 w-full",
                ),
                class_name="mb-6 w-full",
            ),
            rx.el.div(
                rx.el.label(
                    rx.el.input(
                        type="checkbox",
                        name="remember",
                        class_name="ml-2 accent-blue-600",
                    ),
                    "تذكرني",
                    class_name="flex flex-row-reverse items-center text-gray-600 cursor-pointer",
                ),
                rx.el.a(
                    "نسيت كلمة المرور؟",
                    href="#",
                    class_name="text-blue-600 hover:underline",
                ),
                class_name="flex justify-between items-center mb-8 w-full",
            ),
            rx.el.button(
                "تسجيل الدخول",
                type="submit",
                class_name="w-full bg-blue-600 text-white p-4 rounded-xl font-semibold hover:bg-blue-700 transition-colors shadow-lg shadow-blue-500/30",
            ),
            on_submit=AppState.login,
            reset_on_submit=True,
            class_name="w-full flex flex-col items-center",
        ),
        class_name="min-h-screen bg-slate-50 flex flex-col items-center justify-center p-6 w-full max-w-md mx-auto",
    )