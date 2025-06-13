translations = {
    "welcome": {"ua": "👋 Вітаємо! Оберіть опцію:", "en": "👋 Welcome! Choose an option:"},
    "status": {"ua": "🖥️ Стан системи", "en": "🖥️ System Status"},
    "charts": {"ua": "📉 Графіки", "en": "📉 Charts"},
    "thresholds": {"ua": "🎚️ Пороги", "en": "🎚️ Thresholds"},
    "logs": {"ua": "🗂️ Вивантаження логів", "en": "🗂️ Export Logs"},
    "settings": {"ua": "🔧 Налаштування", "en": "🔧 Settings"},
    "admin": {"ua": "👤 Адмін панель", "en": "👤 Admin Panel"},
    "choose_stage": {"ua": "Оберіть дільницю:", "en": "Choose a stage:"},
    "enter_threshold": {"ua": "Введіть новий поріг:", "en": "Enter new threshold:"},
    "threshold_saved": {"ua": "✅ Поріг збережено!", "en": "✅ Threshold saved!"},
    "settings_text": {"ua": "🔧 Налаштування:", "en": "🔧 Settings:"},
    "choose_lang": {"ua": "Оберіть мову:", "en": "Choose language:"},
    "choose_freq": {"ua": "Оберіть частоту оновлення:", "en": "Choose update frequency:"},
    "lang_changed": {"ua": "✅ Мову змінено!", "en": "✅ Language changed!"},
    "freq_set": {"ua": "✅ Частоту встановлено на {} хвилин.", "en": "✅ Frequency set to {} minutes."},
    "admin_panel": {"ua": "👤 Адмін панель:", "en": "👤 Admin panel:"},
    "enter_user_id": {"ua": "Введіть Telegram ID нового користувача:", "en": "Enter the new user's Telegram ID:"},
    "user_added": {"ua": "✅ Користувач {} доданий!", "en": "✅ User {} added!"}
"feedback": {
    "ua": "📬 Зворотній зв'язок",
    "en": "📬 Feedback"
}

}

def t(key, lang="ua"):
    return translations.get(key, {}).get(lang, key)
