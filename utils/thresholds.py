from telegram import InlineKeyboardMarkup, InlineKeyboardButton

threshold_data = {}

def get_stage_menu(lang="ua"):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔪 Розкрій", callback_data="thresh_rozkr")],
        [InlineKeyboardButton("🧱 Армування", callback_data="thresh_arm")],
        [InlineKeyboardButton("🔥 Зварювання", callback_data="thresh_zvar")],
        [InlineKeyboardButton("🧼 Зачистка", callback_data="thresh_zach")],
        [InlineKeyboardButton("🪟 Скління", callback_data="thresh_sklo")],
        [InlineKeyboardButton("✅ Контроль", callback_data="thresh_kontrol")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
    ])

def set_threshold(stage, value):
    threshold_data[stage] = value
