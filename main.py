from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters,
    ContextTypes
)
from config import BOT_TOKEN
from utils import logics, charts, thresholds, users, states, i18n

user_states = {}

def get_main_menu(lang="ua"):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(i18n.t("status", lang), callback_data="status")],
        [InlineKeyboardButton(i18n.t("charts", lang), callback_data="charts")],
        [InlineKeyboardButton(i18n.t("thresholds", lang), callback_data="thresholds")],
        [InlineKeyboardButton(i18n.t("logs", lang), callback_data="logs")],
        [InlineKeyboardButton(i18n.t("settings", lang), callback_data="settings")],
        [InlineKeyboardButton(i18n.t("admin", lang), callback_data="admin")],
        [InlineKeyboardButton(i18n.t("feedback", lang), callback_data="feedback")]
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not users.is_authorized(user_id):
        await update.message.reply_text("⛔ Доступ заборонено.")
        return
    lang = users.get_lang(user_id)
    await update.message.reply_text(i18n.t("welcome", lang), reply_markup=get_main_menu(lang))

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    lang = users.get_lang(user_id)
elif action == "feedback":
    await query.edit_message_text(
        "📬 Ви можете написати нам ваші пропозиції чи проблеми сюди:\n\n"
        "📧 Email: support@example.com\n"
        "📞 Телефон: +380 99 123 4567\n"
        "📨 Або просто надішліть повідомлення у чат.",
        reply_markup=logics.get_back(lang)
    )


    if not users.is_authorized(user_id):
        await query.edit_message_text("⛔ Доступ заборонено.")
        return

    action = query.data

    if action == "status":
        await query.edit_message_text(logics.get_status(lang), reply_markup=logics.get_back(lang))
    elif action == "charts":
        await query.edit_message_text(i18n.t("choose_stage", lang), reply_markup=charts.get_stage_menu(lang))
    elif action.startswith("chart_"):
        stage = action.split("_")[1]
        path = charts.generate_chart(stage)
        await query.message.reply_photo(photo=open(path, "rb"))
    elif action == "thresholds":
        await query.edit_message_text(i18n.t("choose_stage", lang), reply_markup=thresholds.get_stage_menu(lang))
    elif action.startswith("thresh_"):
        stage = action.split("_")[1]
        user_states[user_id] = states.awaiting_threshold(stage)
        await query.message.reply_text(i18n.t("enter_threshold", lang))
    elif action == "logs":
        path = logics.generate_full_log()
        await query.message.reply_document(InputFile(path, filename="daily_log.txt"))
    elif action == "settings":
        await query.edit_message_text(i18n.t("settings_text", lang), reply_markup=logics.get_settings_menu(lang))
    elif action == "lang":
        await query.edit_message_text(i18n.t("choose_lang", lang), reply_markup=logics.get_lang_menu())
    elif action in ["ua", "en"]:
        users.set_lang(user_id, action)
        await query.edit_message_text(i18n.t("lang_changed", action), reply_markup=get_main_menu(action))
    elif action == "update_freq":
        await query.edit_message_text(i18n.t("choose_freq", lang), reply_markup=logics.get_freq_menu())
    elif action in ["15", "30", "60"]:
        users.set_freq(user_id, int(action))
        await query.edit_message_text(i18n.t("freq_set", lang).format(action), reply_markup=get_main_menu(lang))
    elif action == "admin":
        await query.edit_message_text(i18n.t("admin_panel", lang), reply_markup=logics.get_admin_menu(lang))
    elif action == "add_user":
        user_states[user_id] = states.awaiting_user_id()
        await query.message.reply_text(i18n.t("enter_user_id", lang))
    elif action == "back":
        await query.edit_message_text(i18n.t("welcome", lang), reply_markup=get_main_menu(lang))

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = users.get_lang(user_id)
    if user_id in user_states:
        state = user_states[user_id]
        if state["type"] == "threshold":
            thresholds.set_threshold(state["stage"], update.message.text)
            await update.message.reply_text(i18n.t("threshold_saved", lang))
        elif state["type"] == "add_user":
            new_id = int(update.message.text.strip())
            users.add_user(new_id)
            await update.message.reply_text(i18n.t("user_added", lang).format(new_id))
        del user_states[user_id]

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.run_polling()

if __name__ == "__main__":
    main()
