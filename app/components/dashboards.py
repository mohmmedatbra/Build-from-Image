import reflex as rx
from app.state import AppState
from app.components.dashboard_components import (
    dashboard_header,
    welcome_card,
    system_status_card,
    section_header,
    stat_card_component,
    quick_access_card,
    schedule_item_component,
    recent_file_component,
    student_file_component,
    announcement_component,
    activity_item_component,
)


def professor_dashboard() -> rx.Component:
    return rx.el.div(
        dashboard_header(AppState.greeting_user),
        rx.el.div(
            welcome_card(AppState.greeting_user, "لديك 3 واجبات جديدة للتقييم"),
            rx.el.div(
                section_header("إحصائيات سريعة", ""),
                rx.el.div(
                    rx.foreach(AppState.professor_stats, stat_card_component),
                    class_name="grid grid-cols-2 gap-4 mt-4",
                ),
                class_name="mt-6",
            ),
            rx.el.div(
                section_header("جدول اليوم", "عرض الكل"),
                rx.el.div(
                    rx.foreach(AppState.professor_schedule, schedule_item_component),
                    class_name="space-y-3 mt-4",
                ),
                class_name="mt-6",
            ),
            rx.el.div(
                section_header("آخر المرفوعات", "عرض الكل"),
                rx.el.div(
                    rx.foreach(AppState.professor_uploads, recent_file_component),
                    class_name="space-y-3 mt-4",
                ),
                class_name="mt-6",
            ),
            class_name="p-4",
        ),
        class_name="bg-slate-50 min-h-screen",
    )


def student_dashboard() -> rx.Component:
    return rx.el.div(
        dashboard_header(AppState.greeting_user),
        rx.el.div(
            welcome_card(AppState.greeting_user, "لديك 3 ملفات جديدة اليوم!"),
            rx.el.div(
                section_header("الوصول السريع", ""),
                rx.el.div(
                    rx.foreach(AppState.student_quick_access, quick_access_card),
                    class_name="grid grid-cols-4 gap-3 mt-4",
                ),
                class_name="mt-6",
            ),
            rx.el.div(
                section_header("أحدث الملفات", "عرض الكل"),
                rx.el.div(
                    rx.foreach(AppState.student_files, student_file_component),
                    class_name="space-y-3 mt-4",
                ),
                class_name="mt-6",
            ),
            rx.el.div(
                section_header("الإعلانات", "عرض الكل"),
                rx.el.div(
                    rx.foreach(AppState.student_announcements, announcement_component),
                    class_name="space-y-3 mt-4",
                ),
                class_name="mt-6",
            ),
            class_name="p-4",
        ),
        class_name="bg-slate-50 min-h-screen",
    )


def admin_dashboard() -> rx.Component:
    return rx.el.div(
        dashboard_header(AppState.greeting_user),
        rx.el.div(
            system_status_card(),
            rx.el.div(
                section_header("إجراءات سريعة", ""),
                rx.el.div(
                    rx.foreach(AppState.admin_quick_actions, stat_card_component),
                    class_name="grid grid-cols-3 gap-4 mt-4",
                ),
                class_name="mt-6",
            ),
            rx.el.div(
                section_header("إحصائيات النظام", ""),
                rx.el.div(
                    rx.foreach(AppState.admin_stats, stat_card_component),
                    class_name="grid grid-cols-2 gap-4 mt-4",
                ),
                class_name="mt-6",
            ),
            rx.el.div(
                section_header("النشاطات الأخيرة", "عرض الكل"),
                rx.el.div(
                    rx.foreach(AppState.admin_activities, activity_item_component),
                    class_name="space-y-3 mt-4",
                ),
                class_name="mt-6",
            ),
            class_name="p-4",
        ),
        class_name="bg-slate-50 min-h-screen",
    )