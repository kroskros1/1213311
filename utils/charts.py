from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import matplotlib.pyplot as plt
import pandas as pd

def get_stage_menu(lang="ua"):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔪 Розкрій", callback_data="chart_rozkr")],
        [InlineKeyboardButton("🧱 Армування", callback_data="chart_arm")],
        [InlineKeyboardButton("🔥 Зварювання", callback_data="chart_zvar")],
        [InlineKeyboardButton("🧼 Зачистка", callback_data="chart_zach")],
        [InlineKeyboardButton("🪟 Скління", callback_data="chart_sklo")],
        [InlineKeyboardButton("✅ Контроль", callback_data="chart_kontrol")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
    ])

def generate_chart(stage):
    hours = list(range(8))
    values = [40 + i + (hash(stage) % 5) for i in range(8)]
    df = pd.DataFrame({"hour": hours, "temp": values})
    plt.figure()
    plt.plot(df["hour"], df["temp"], marker='o')
    plt.title(f"Температура ({stage})")
    plt.xlabel("Година")
    plt.ylabel("Температура °C")
    path = f"{stage}_chart.png"
    plt.savefig(path)
    plt.close()
    return path
