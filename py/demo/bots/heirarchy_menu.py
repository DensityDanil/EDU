from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters

# ����� �������
MENU, SUBMENU = range(2)

# ��������� ������� ����
def main_menu(update, context):
    user = update.effective_user
    update.message.reply_html(
        fr"�����, {user.mention_html()}!",
        reply_markup=main_menu_keyboard(),
    )
    return MENU

# ��������� �������� ����
def submenu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="������� ������� ������:",
        reply_markup=submenu_keyboard(),
    )
    return SUBMENU

# ������� ��� ������� ������ ������ ������
def submenu_choice(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text=f"�� ������: {query.data}",
        reply_markup=main_menu_keyboard(),
    )
    return MENU

# ��������� ��������� ��� ��������� ����
def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("������� 1", callback_data="item1"),
            InlineKeyboardButton("������� 2", callback_data="item2"),
        ],
        [InlineKeyboardButton("�������� ����", callback_data="submenu")],
    ]
    return InlineKeyboardMarkup(keyboard)

# ��������� ��������� ��� ������
def submenu_keyboard():
    keyboard = [
        [InlineKeyboardButton("����� 1", callback_data="subitem1")],
        [InlineKeyboardButton("����� 2", callback_data="subitem2")],
        [InlineKeyboardButton("����������� �����", callback_data="back")],
    ]
    return InlineKeyboardMarkup(keyboard)

# ������� ��� ������� ������� /start
def start(update, context):
    return main_menu(update, context)

# ������� ��� ������� ���������� ������
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

    # ������ �������� ������� /start
    dp.add_handler(CommandHandler("start", start))

    # ������ �������� ��� ���������� ������
    dp.add_handler(CallbackQueryHandler(button))

    # ��������� ����
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
