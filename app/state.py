import reflex as rx
from typing import Literal, TypedDict

Role = Literal["student", "professor", "supervisor"]


class StatCard(TypedDict):
    title: str
    value: str
    icon: str
    color: str


class ScheduleItem(TypedDict):
    title: str
    time: str
    location: str
    icon: str
    color: str


class RecentFile(TypedDict):
    title: str
    subtitle: str
    icon: str
    color: str
    size: str | None = None


class RecentActivity(TypedDict):
    title: str
    subtitle: str
    icon: str
    color: str


class AppState(rx.State):
    current_page: str = "role_selection"
    selected_role: Role = "student"
    username: str = ""
    professor_stats: list[StatCard] = [
        {
            "title": "الطلاب",
            "value": "87",
            "icon": "users",
            "color": "bg-blue-100 text-blue-600",
        },
        {
            "title": "المواد",
            "value": "3",
            "icon": "book-open",
            "color": "bg-purple-100 text-purple-600",
        },
        {
            "title": "الملفات",
            "value": "24",
            "icon": "folder",
            "color": "bg-red-100 text-red-600",
        },
        {
            "title": "الواجبات",
            "value": "12",
            "icon": "edit-3",
            "color": "bg-yellow-100 text-yellow-600",
        },
    ]
    professor_schedule: list[ScheduleItem] = [
        {
            "title": "نظم التشغيل",
            "time": "10:00 ص - 11:30 ص",
            "location": "القاعة 203",
            "icon": "clock",
            "color": "text-blue-500",
        },
        {
            "title": "هياكل البيانات",
            "time": "12:00 م - 1:30 م",
            "location": "القاعة 105",
            "icon": "clock",
            "color": "text-purple-500",
        },
    ]
    professor_uploads: list[RecentFile] = [
        {
            "title": "ملف المحاضرة 5",
            "subtitle": "نظم التشغيل | منذ يومين",
            "icon": "arrow-up-circle",
            "color": "text-green-500",
        },
        {
            "title": "تمارين الوحدة 4",
            "subtitle": "هياكل البيانات | منذ 3 أيام",
            "icon": "arrow-up-circle",
            "color": "text-green-500",
        },
    ]
    student_quick_access: list[StatCard] = [
        {
            "title": "الجدول الدراسي",
            "value": "",
            "icon": "calendar",
            "color": "bg-purple-100 text-purple-600",
        },
        {
            "title": "الملفات الدراسية",
            "value": "",
            "icon": "file-text",
            "color": "bg-blue-100 text-blue-600",
        },
        {
            "title": "المواد",
            "value": "",
            "icon": "book-open",
            "color": "bg-green-100 text-green-600",
        },
        {
            "title": "الواجبات",
            "value": "",
            "icon": "edit-3",
            "color": "bg-yellow-100 text-yellow-600",
        },
    ]
    student_files: list[RecentFile] = [
        {
            "title": "ملف المحاضرة الأولى",
            "subtitle": "نظم التشغيل - د.خالد",
            "size": "2MB",
            "icon": "file-text",
            "color": "text-blue-500",
        },
        {
            "title": "تمارين الوحدة 3",
            "subtitle": "هياكل البيانات - د.نورا",
            "size": "1.5MB",
            "icon": "file-text",
            "color": "text-purple-500",
        },
        {
            "title": "ملخص القواعد",
            "subtitle": "لغة إنجليزية - د.سارة",
            "size": "3MB",
            "icon": "file-text",
            "color": "text-green-500",
        },
    ]
    student_announcements: list[ScheduleItem] = [
        {
            "title": "تغيير موعد المحاضرة",
            "time": "تم تغيير محاضرة نظم التشغيل إلى يوم الأحد الساعة 10 صباحًا",
            "location": "منذ ساعتين",
            "icon": "alert-circle",
            "color": "text-yellow-500",
        }
    ]
    admin_quick_actions: list[StatCard] = [
        {
            "title": "المستخدمون",
            "value": "",
            "icon": "users",
            "color": "bg-blue-100 text-blue-600",
        },
        {
            "title": "المواد",
            "value": "",
            "icon": "book-open",
            "color": "bg-purple-100 text-purple-600",
        },
        {
            "title": "التخزين",
            "value": "",
            "icon": "database",
            "color": "bg-green-100 text-green-600",
        },
        {
            "title": "التقارير",
            "value": "",
            "icon": "bar-chart-2",
            "color": "bg-yellow-100 text-yellow-600",
        },
        {
            "title": "الإعدادات",
            "value": "",
            "icon": "settings",
            "color": "bg-red-100 text-red-600",
        },
        {
            "title": "النسخ الإحتياطي",
            "value": "",
            "icon": "archive",
            "color": "bg-indigo-100 text-indigo-600",
        },
    ]
    admin_stats: list[StatCard] = [
        {
            "title": "المستخدمون",
            "value": "1,245",
            "icon": "users",
            "color": "bg-blue-100 text-blue-600",
        },
        {
            "title": "الملفات",
            "value": "8,742",
            "icon": "folder",
            "color": "bg-red-100 text-red-600",
        },
        {
            "title": "المساحة المستخدمة",
            "value": "45.2GB",
            "icon": "hard-drive",
            "color": "bg-green-100 text-green-600",
        },
        {
            "title": "المواد",
            "value": "87",
            "icon": "book-open",
            "color": "bg-yellow-100 text-yellow-600",
        },
    ]
    admin_activities: list[RecentActivity] = [
        {
            "title": "تمت إضافة مستخدم جديد",
            "subtitle": "أحمد محمد - طالب | منذ 15 دقيقة",
            "icon": "user-plus",
            "color": "text-blue-500",
        },
        {
            "title": "تم رفع ملف جديد",
            "subtitle": "ملف المحاضرة 5 - د.خالد | منذ ساعة",
            "icon": "upload-cloud",
            "color": "text-green-500",
        },
    ]

    @rx.var
    def dashboard_title(self) -> str:
        if self.selected_role == "student":
            return "لوحة الطالب"
        if self.selected_role == "professor":
            return "لوحة الأستاذ"
        return "لوحة المشرف"

    @rx.var
    def greeting_user(self) -> str:
        if self.selected_role == "student":
            return "أحمد"
        if self.selected_role == "professor":
            return "د. خالد"
        return "إدارة النظام"

    @rx.event
    def select_role(self, role: Role):
        self.selected_role = role
        self.current_page = "login"

    @rx.event
    def login(self, form_data: dict):
        self.username = form_data["university_id"]
        self.current_page = f"{self.selected_role}_dashboard"
        return rx.toast(f"مرحباً بك {self.username}")

    @rx.event
    def go_to_role_selection(self):
        self.current_page = "role_selection"