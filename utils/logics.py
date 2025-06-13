from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import datetime

def get_status(lang="ua"):
    return "✅ Система стабільна\nТемпература: 42°C\nВологість: 60%"

def get_back(lang="ua"):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
    ])

def generate_full_log():
    path = "daily_log.txt"
    with open(path, "w") as f:
        f.write("== Звіт за всі дільниці ==\n")
        f.write("Дата: " + str(datetime.datetime.now()) + "\n")
        for stage in ["rozkr", "arm", "zvar", "zach", "sklo", "kontrol"]:
            f.write(f"[{stage.upper()}]\nТемпература: 42°C\nЧас роботи: 7 год\n\n")
    return path

def get_settings_menu(lang="ua"):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🌐 Мова / Language", callback_data="lang")],
        [InlineKeyboardButton("⏱️ Частота оновлення", callback_data="update_freq")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
    ])

def get_lang_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🇺🇦 Українська", callback_data="ua")],
        [InlineKeyboardButton("🇬🇧 English", callback_data="en")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
    ])

def get_freq_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("15 хв", callback_data="15")],
        [InlineKeyboardButton("30 хв", callback_data="30")],
        [InlineKeyboardButton("1 год", callback_data="60")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
    ])

def get_admin_menu(lang="ua"):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Додати користувача", callback_data="add_user")],
        [InlineKeyboardButton("🗂️ Перегляд логів", callback_data="logs")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
    ])
