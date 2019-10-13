from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

# main markup

main_buttons = {
    'en': [
        ['🐱 Cat 🐱', '🐶 Dog 🐶'],
        ['Change Language', 'Help'],
        ['Send to a Friend']
    ],
    'ru': [
        ['🐱 Котик 🐱', '🐶 Собачка 🐶'],
        ['Сменить язык', 'Помощь'],
        ['Послать другу']
    ]
}

main_markup = {
    'en': ReplyKeyboardMarkup(main_buttons['en'], resize_keyboard=True),
    'ru': ReplyKeyboardMarkup(main_buttons['ru'], resize_keyboard=True)
}

# inline language keyboard

en_button = InlineKeyboardButton(text='English 🇬🇧', callback_data='change_lang_en')
ru_button = InlineKeyboardButton(text='Русский 🇷🇺', callback_data='change_lang_ru')
lang_markup = InlineKeyboardMarkup([[en_button, ru_button]])

# callbacks

reboot_callback = 'reboot'
mailing_callback = 'mailing'
statistics_callback = 'statistics'

# admin markup

admin_keyboard = {
    'en': [
        [InlineKeyboardButton(text='Check Statistics', callback_data=statistics_callback)],
        [InlineKeyboardButton(text='Send Mailing', callback_data=mailing_callback)],
        [InlineKeyboardButton(text='Restart the Bot', callback_data=reboot_callback)]
    ],
    'ru': [
        [InlineKeyboardButton(text='Посмотреть статистику', callback_data=statistics_callback)],
        [InlineKeyboardButton(text='Создать рассылку', callback_data=mailing_callback)],
        [InlineKeyboardButton(text='Перезагрузить бота', callback_data=reboot_callback)]
    ]
}

admin_markup = {
    'en': InlineKeyboardMarkup(admin_keyboard['en']),
    'ru': InlineKeyboardMarkup(admin_keyboard['ru'])
}

# mailing markup

mailing_keyboard = {
    'en': [
        ['Send Message', 'Preview'],
        ['Add Text', 'Add Photo'],
        ['Add Button', 'Cancel Mailing']
    ],
    'ru': [
        ['Разослать сообщение', 'Предпросмотр'],
        ['Добавить текст', 'Добавить фото'],
        ['Добавить кнопку', 'Отменить рассылку']
    ]
}

mailing_markup = {
    'en': ReplyKeyboardMarkup(mailing_keyboard['en']),
    'ru': ReplyKeyboardMarkup(mailing_keyboard['ru'])
}

# cancel markup

cancel_keyboard = {
    'en': [['Cancel']],
    'ru': [['Отмена']]
}

cancel_markup = {
    'en': ReplyKeyboardMarkup(cancel_keyboard['en']),
    'ru': ReplyKeyboardMarkup(cancel_keyboard['ru'])
}

# commands

admin_command = 'admin'
start_command = 'start'
help_command = 'help'
cat_command = 'cat'
dog_command = 'dog'

# buttons

cat_button = '({})|({})'.format(*(item[0][0] for item in main_buttons.values()))
dog_button = '({})|({})'.format(*(item[0][1] for item in main_buttons.values()))
lang_button = '({})|({})'.format(*(item[1][0] for item in main_buttons.values()))
help_button = '({})|({})'.format(*(item[1][1] for item in main_buttons.values()))
send_button = '({})|({})'.format(*(item[2][0] for item in main_buttons.values()))

send_mailing_button = '({})|({})'.format(*(item[0][0] for item in mailing_keyboard.values()))
preview_button = '({})|({})'.format(*(item[0][1] for item in mailing_keyboard.values()))
add_text_button = '({})|({})'.format(*(item[1][0] for item in mailing_keyboard.values()))
add_photo_button = '({})|({})'.format(*(item[1][1] for item in mailing_keyboard.values()))
add_button_button = '({})|({})'.format(*(item[2][0] for item in mailing_keyboard.values()))
cancel_mailing_button = '({})|({})'.format(*(item[2][1] for item in mailing_keyboard.values()))

add_content_button = '|'.join([add_text_button, add_photo_button, add_button_button])

cancel_adding_button = '({})|({})'.format(*(item[0][0] for item in cancel_keyboard.values()))

lang_inline_button = '(change_lang_en)|(change_lang_ru)'

# mailing states

states = {
    mailing_keyboard['en'][1][0]: 'add_text',
    mailing_keyboard['ru'][1][0]: 'add_text',
    mailing_keyboard['en'][1][1]: 'add_photo',
    mailing_keyboard['ru'][1][1]: 'add_photo',
    mailing_keyboard['en'][2][0]: 'add_button',
    mailing_keyboard['ru'][2][0]: 'add_button'
}

# messages

messages = {
    'menu': {
        'en': '🇬🇧 Welcome! Here you can get a random picture with a cat or a dog by pressing the buttons below.',
        'ru': '🇷🇺 Добро пожаловать! Здесь ты можешь получить случайную картинку с котиком или собачкой по нажатию '
              'кнопок снизу.'
    },

    'admin': {
        'en': 'Welcome back, Creator!',
        'ru': 'С возвращением, создатель!'
    },

    'reboot': {
        'en': 'The bot has been restarted',
        'ru': 'Бот успешно перезагружен'
    },

    'statistics': {
        'en': 'Here are some statistics about the bot:\n\n'
              'The number of users: <b>{}</b>\n'
              'Total requests amount: <b>{}</b>\n'
              'Requests for cats: <b>{}</b>\n'
              'Requests for dogs: <b>{}</b>\n',
        'ru': 'Вот немного статистики о боте:\n\n'
              'Количество пользователей: <b>{}</b>\n'
              'Суммарное число запросов: <b>{}</b>\n'
              'Запросы на котиков: <b>{}</b>\n'
              'Запросы на собачек: <b>{}</b>\n'
    },

    'mailing': {
        'en': '<i>The message for the mailing:</i>\n\n'
              '<b>Text:</b>\n\n{}\n\n'
              '<b>Photo:</b>\n\n<code>{}</code>\n\n'
              '<b>Button:</b>\n\n{}',
        'ru': '<i>Сообщение для массовой рассылки:</i>\n\n'
              '<b>Текст:</b>\n\n{}\n\n'
              '<b>Фото:</b>\n\n<code>{}</code>\n\n'
              '<b>Кнопка:</b>\n\n{}'
    },

    'cancel_mailing': {
        'en': 'The mailing has been canceled',
        'ru': 'Массовая рассылка отменена'
    },

    'no_mailing_data': {
        'en': 'Not enough data to send the message',
        'ru': 'Не хватает данных для отправки сообщения'
    },

    'mailing_completed': {
        'en': 'The message has been successfully sent:\n\n'
              'Users who received the message: <b>{}</b>\n'
              'Deleted users who blocked the bot: <b>{}</b>',
        'ru': 'Сообщение было успешно отправлено:\n\n'
              'Пользователи, получившие сообщение: <b>{}</b>\n'
              'Удаленные пользователи, которые заблокировали бота: <b>{}</b>'
    },

    'add_text': {
        'en': 'Enter the text which will be attached to the mailing list:',
        'ru': 'Введите текст, который будет прикреплен к сообщению для рассылки:'
    },

    'add_photo': {
        'en': 'Send a picture which will be attached to the message for the mailing:',
        'ru': 'Пришлите картинку, которая будет прикреплена к сообщению для рассылки:'
    },

    'add_button': {
        'en': 'Send a button which will be attached to the message for the newsletter in the format "text - full link":',
        'ru': 'Пришлите кнопку, которая будет прикреплена к сообщению для рассылки в формате "текст - полная ссылка":'
    },

    'broken_url': {
        'rn': 'This link does not work, please retry the request:',
        'ru': 'Данная ссылка не работает, повторите запрос:'
    },

    'incorrect_button': {
        'en': 'The input format does not match, retry the request:',
        'ru': 'Формат ввода не соответствует, повторите запрос:'
    },

    'invalid_tags': {
        'en': 'Make sure all your HTML-tags are valid',
        'ru': 'Убедитесь, что все ваши HTML-теги корректны'
    },

    'current_lang': {
        'en': 'Current language is English 🇬🇧',
        'ru': 'Текущий язык Русский 🇷🇺'
    },

    'changed': {
        'en': 'Language has been changed to English 🇬🇧',
        'ru': 'Язык был изменен на Русский 🇷🇺'
    }
}
