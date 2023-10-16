from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters

# Стани розмови
MENU, SUBMENU = range(2)

# Створюємо головне меню
def main_menu(update, context):
    user = update.effective_user
    update.message.reply_html(
        fr"Привіт, {user.mention_html()}!",
        reply_markup=main_menu_keyboard(),
    )
    return MENU

# Створюємо вкладене меню
def submenu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Виберіть елемент підменю:",
        reply_markup=submenu_keyboard(),
    )
    return SUBMENU

# Функція для обробки вибору пункту підменю
def submenu_choice(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text=f"Ви обрали: {query.data}",
        reply_markup=main_menu_keyboard(),
    )
    return MENU

# Створюємо клавіатуру для головного меню
def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Елемент 1", callback_data="item1"),
            InlineKeyboardButton("Елемент 2", callback_data="item2"),
        ],
        [InlineKeyboardButton("Вкладене меню", callback_data="submenu")],
    ]
    return InlineKeyboardMarkup(keyboard)

# Створюємо клавіатуру для підменю
def submenu_keyboard():
    keyboard = [
        [InlineKeyboardButton("Пункт 1", callback_data="subitem1")],
        [InlineKeyboardButton("Пункт 2", callback_data="subitem2")],
        [InlineKeyboardButton("Повернутися назад", callback_data="back")],
    ]
    return InlineKeyboardMarkup(keyboard)

# Функція для обробки команди /start
def start(update, context):
    return main_menu(update, context)

# Функція для обробки натискання кнопок
def button(update, context):
    query = update.callback_query
    query.answer()
    
    if query.data == "submenu":
        return submenu(update, context)
    elif query.data == "back":
        return main_menu(update, context)
    else:
        return submenu_choice(update, context)

def main():
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)

    dp = updater.dispatcher

    # Додаємо обробник команди /start
    dp.add_handler(CommandHandler("start", start))

    # Додаємо обробник для натискання кнопок
    dp.add_handler(CallbackQueryHandler(button))

    # Запускаємо бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
