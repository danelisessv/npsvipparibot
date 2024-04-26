import telebot
import time
from telebot import types
from datetime import datetime
import requests
import gspread
from gspread import Client, Spreadsheet, Worksheet

vip_support_bot_token = '5340812840:AAFPM3KWZ-W_yNJmbmtPNBmTJpWRGMeSqds'

chat_id_vip_support = '-1001760406147'   #4194343492   1001760406147

TOKEN = '7060372730:AAGFZF-Soau4jYN04iQLQGvDGabvsJpy2Y4'

bot = telebot.TeleBot(TOKEN, parse_mode = 'html')

# Ссылка на схему MIRO - https://miro.com/app/board/uXjVKXQKWCc=/

# Ссылка на Google - Таблицу - https://docs.google.com/spreadsheets/d/1TXhvnMCXhtHaCSviSsrdgVrBAl_ZOKj_2W80klSdLzA/edit#gid=0

# Ссылка на Google - Таблицу СОКРАЩЕННАЯ - https://clck.ru/3AGtoK

""" Здесь инлайн клавиатура вступительная """

markup = types.InlineKeyboardMarkup(row_width = 3)

btn1 = types.InlineKeyboardButton('Да!', callback_data = 'Yes')
btn2 = types.InlineKeyboardButton('Перезвонить!', callback_data = 'Callback_me')
btn3 = types.InlineKeyboardButton('Нет!', callback_data = 'No')

markup.add(btn1, btn2, btn3)


""" Здесь инлайн клавиатура которая появляется в самом конце, ДОП вопрос Да или Нет """

markup_additional = types.InlineKeyboardMarkup(row_width = 2)

btn14 = types.InlineKeyboardButton('Да!', callback_data = 'additional_yes')
btn15 = types.InlineKeyboardButton('Нет!', callback_data = 'additional_no')

markup_additional.add(btn14, btn15)


""" Здесь Клавиатура, которая запрашивает номер телефона """

markup_phone = types.ReplyKeyboardMarkup(row_width = 1, one_time_keyboard = True, resize_keyboard = True)           

button_phone = types.KeyboardButton(text = "Поделиться номером", request_contact = True)

markup_phone.add(button_phone)

""" Переменые """

number_account = '' # В этой переменной хранится номер игрового счета, который указывает клиент!

question_one_vip = '' # Ответ на 1 вопрос!
question_two_vip = '' # Ответ на 2 вопрос!
question_three_vip = '' # Ответ на 3 вопрос!
question_four_vip = '' # Ответ на 4 вопрос!
question_five_vip = '' # Ответ на 5 вопрос!


additional_question_vip = '' # Доп ответ!

call_me_back_pls = '' # Здесь хранится номер телефона!


""" Рабочая ссылка """

SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1TXhvnMCXhtHaCSviSsrdgVrBAl_ZOKj_2W80klSdLzA/edit#gid=1011446080"

gc: Client = gspread.service_account(r"C:\Users\deliseev\Desktop\PYYYTHON\NPS-VIP-pariBOT\service_account.json")
sh: Spreadsheet = gc.open_by_url(SPREADSHEET_URL)
ws: Worksheet = gc.open('NPS исследование VIP').sheet1

def checkId(clientId):# Номер счета

    cellID = ws.find(clientId)
    if cellID:
        return True
    else:
        return False

def checkId_and_fioInput(clientId, telephone):# Номер счета + номер телефона

    cellID = ws.find(clientId)
    if cellID:
        ws.update_cell(cellID.row, cellID.col + 2, telephone)
        return True
    else:
        return False

def google_pull_q_one(clientId, q_one):# Номер счета + ответ на первый вопрос

    cellID = ws.find(clientId)
    if cellID:
        ws.update_cell(cellID.row, cellID.col + 3, q_one)
        return True
    else:
        return False
    
def google_pull_q_two(clientId, q_two):# Номер счета + ответ на второй вопрос

    cellID = ws.find(clientId)
    if cellID:
        ws.update_cell(cellID.row, cellID.col + 4, q_two)
        return True
    else:
        return False

def google_pull_q_three(clientId, q_three):# Номер счета + ответ на третий вопрос

    cellID = ws.find(clientId)
    if cellID:
        ws.update_cell(cellID.row, cellID.col + 5, q_three)
        return True
    else:
        return False

def google_pull_q_four(clientId, q_four):# Номер счета + ответ на четвертый вопрос

    cellID = ws.find(clientId)
    if cellID:
        ws.update_cell(cellID.row, cellID.col + 6, q_four)
        return True
    else:
        return False
    
def google_pull_q_five(clientId, q_five):# Номер счета + ответ на четвертый вопрос

    cellID = ws.find(clientId)
    if cellID:
        ws.update_cell(cellID.row, cellID.col + 7, q_five)
        return True
    else:
        return False

def google_pull_q_additionalquestion(clientId, q_additionalquestion):# Номер счета + доп вопрос

    cellID = ws.find(clientId)
    if cellID:
        ws.update_cell(cellID.row, cellID.col + 8, q_additionalquestion)
        return True
    else:
        return False

def google_pull_q_grade_4(clientId, q_grade_4):# Номер счета + оценка четвертого вопроса
    cellID = ws.find(clientId)
    if cellID:
        ws.update_cell(cellID.row, cellID.col + 6, q_grade_4)
        return True
    else:
        return False

def google_pull_q_grade_5(clientId, q_grade_5):# Номер счета + оценка пятого вопроса
    cellID = ws.find(clientId)
    if cellID:
        ws.update_cell(cellID.row, cellID.col + 7, q_grade_5)
        return True
    else:
        return False

""" Начало - шапка """

@bot.message_handler(commands = ['start'])

def start(message):# Старт
    bot.send_message(message.chat.id,'Уточните ваш номер игрового счета, пожалуйста 😉'   
                     '\n\n🆔 Ваш номер игрового счета отображен в приложении во вкладке "Профиль" (нажмите на силуэт человека в верхнем правом углу), или по ссылке:'
                     '\n\n🔗 https://www.pari.ru/mobile/profile/')
    bot.register_next_step_handler(message, account)

def account(message):# Начало

    global number_account
    
    number_account = message.text # В этой переменной хранится номер игрового счета, который указывает клиент!

    try:

        if number_account.isdigit() and len(number_account) == 8:            

            if checkId(number_account):
                
                time.sleep(1)
                print(f'\n{'-' * 100} \nНомер игрового счета -> {number_account} \nКлиент -> {message.from_user.first_name} \n{'-' * 100}')
                bot.send_message(message.chat.id, 'Это команда контроля качества компании PARI. '
                                '\nМы хотим задать вам вопросы по работе нашего сайта/приложения - это займет несколько минут.'
                                '\nГотовы сейчас ответить? Или вам лучше позвонить?', reply_markup = markup)
                
            else:
                bot.send_message(message.chat.id, 'Данный опрос завершён. '
                                'Благодарим за уделенное время 🙌')

        elif number_account == '/start':
            bot.send_message(message.chat.id,'Уточните ваш номер игрового счета, пожалуйста 😉'  
                        '\n\n🆔 Ваш номер игрового счета отображен в приложении во вкладке "Профиль" (нажмите на силуэт человека в верхнем правом углу), или по ссылке:'
                        '\n\n🔗 https://www.pari.ru/mobile/profile/')
            bot.register_next_step_handler(message, account)

        else:
            bot.send_message(message.chat.id, '🚫Ошибка! Номер игрового счета должен состоять из 8 цифр. '
                            '\nПовторите ввод, пожалуйста. \n\n🆔Ваш номер игрового счета отображен в приложении во вкладке "Профиль" '
                            '(необходимо нажать на силуэт человека в верхнем правом углу), или перейти по ссылке: 🔗 https://www.pari.ru/mobile/profile/')
            bot.register_next_step_handler(message, account)

    except AttributeError:
        bot.send_message(message.chat.id, '🚫Ошибка! Номер игрового счета должен состоять из 8 цифр. '
                            '\nПовторите ввод, пожалуйста. \n\n🆔Ваш номер игрового счета отображен в приложении во вкладке "Профиль" '
                            '(необходимо нажать на силуэт человека в верхнем правом углу), или перейти по ссылке: 🔗 https://www.pari.ru/mobile/profile/')
        bot.register_next_step_handler(message, account)

def question_one(message):# Первый вопрос

    global number_account

    question_one_vip = message.text # В этой переменной хранится ответ клиента 1 вопрос!

    try:
        if len(question_one_vip) > 4000:
            bot.send_message(message.chat.id,f'Пожалуйста, сократите ваш ответ до <b>4000</b> символов.'
                                            f'\n\nКол-во ваших символов ➡️ <b>{len(question_one_vip)}</b>')
            bot.register_next_step_handler(message, question_one)
            
        elif len(question_two_vip) <= 4000:

            if google_pull_q_one (number_account, question_one_vip):   
                print(f'\n{'-' * 100} \n\nОтвет на 1 вопрос -> {question_one_vip} \n{'-' * 100}')
                bot.send_message(message.chat.id, '<b>Вопрос №2</b> \n\nЕсть ли что-то, что вас '
                                'разочаровало или затруднило использование нашего приложения/сайта?')
                bot.register_next_step_handler(message, question_two)

    except TypeError or AttributeError:
        bot.send_message(message.chat.id,f'Укажите ответ текстом, пожалуйста!')
        bot.register_next_step_handler(message, question_one)

def question_two(message):# Второй вопрос

    global number_account

    question_two_vip = message.text # В этой переменной хранится ответ клиента 2 вопрос!

    try:
        if len(question_two_vip) > 4000:
            bot.send_message(message.chat.id,f'Пожалуйста, сократите ваш ответ до <b>4000</b> символов.'
                                            f'\n\nКол-во ваших символов ➡️ <b>{len(question_two_vip)}</b>')
            bot.register_next_step_handler(message, question_two)
            
        elif len(question_two_vip) <= 4000:

            if google_pull_q_two(number_account, question_two_vip):
                    print(f'\n{'-' * 100} \n\nОтвет на 2 вопрос -> {question_two_vip} \n{'-' * 100}')
                    bot.send_message(message.chat.id, '<b>Вопрос №3</b> \n\nЧто бы вы хотели добавить '
                                    'или изменить в нашем продукте/сервисе?')
                    bot.register_next_step_handler(message, question_three)
        
    except TypeError:
        bot.send_message(message.chat.id,f'Укажите ответ текстом, пожалуйста!')
        bot.register_next_step_handler(message, question_two)

def question_three(message):# Третий вопрос

    global number_account

    question_three_vip = message.text

    try:
        if len(question_three_vip) > 4000:
            bot.send_message(message.chat.id,f'Пожалуйста, сократите ваш ответ до <b>4000</b> символов.'
                                            f'\n\nКол-во ваших символов ➡️ <b>{len(question_three_vip)}</b>')
            bot.register_next_step_handler(message, question_three)

        elif len(question_three_vip) <= 4000:

            if google_pull_q_three(number_account, question_three_vip):
                    print(f'\n{'-' * 100} \n\nОтвет на 3 вопрос -> {question_three_vip} \n{'-' * 100}')
                    bot.send_message(message.chat.id, '<b>Вопрос №4</b> \n\nУдовлетворены ли вы качеством работы менеджеров службы поддержки PARI? \n\n<b>Поставьте оценку от 1 до 10: </b>'
                                    '\n• <i>1 - полностью не удовлетворен.</i> '
                                    '\n• <i>10 - удовлетворен полностью.</i>')
                    bot.register_next_step_handler(message, question_four)

    except TypeError:
        bot.send_message(message.chat.id,'Укажите ответ текстом, пожалуйста!')
        bot.register_next_step_handler(message, question_three)                  

def question_four(message):# Четвертый вопрос

    global number_account

    question_four_vip = message.text

    try:

        if question_four_vip in ('1','2','3','4','5','6','7','8','9','10'):

            if google_pull_q_four(number_account, question_four_vip):

                print(f'\n{'-' * 100} \n\nОтвет на 4 вопрос -> {question_four_vip} \n{'-' * 100}')
                bot.send_message(message.chat.id, '<b>Вопрос №5</b> \n\nПорекомендовали бы вы сайт/приложение PARI своим знакомым и друзьям, которых интересуют ставки на спорт? '
                                '\n\n<b>Поставьте оценку от 1 до 10:</b> '
                                '\n• <i>1 - точно не порекомендую.</i>'
                                '\n• <i>10 - точно порекомендую.</i>')
                bot.register_next_step_handler(message, question_five)

        else:
            bot.send_message(message.chat.id, 'Необходимо выбрать оценку в числовом формате: '
                             '\n<b>• 1</b> - полностью не удовлетворен.'
                             '\n<b>• 10</b> - полностью удовлетворен.')
            bot.register_next_step_handler(message, question_four)

    except AttributeError:
        bot.send_message(message.chat.id, 'Необходимо выбрать оценку в числовом формате: '
                             '\n<b>• 1</b> - полностью не удовлетворен.'
                             '\n<b>• 10</b> - полностью удовлетворен.')
        bot.register_next_step_handler(message, question_four)

def question_five(message):# Пятый вопрос  

    global number_account

    question_five_vip = message.text  

    try:

        if question_five_vip in ('1','2','3','4','5','6','7','8','9','10'): 

            if google_pull_q_five(number_account, question_five_vip):
                print(f'\n{'-' * 100} \n\nОтвет на 5 вопрос -> {question_five_vip} \n{'-' * 100}')
                bot.send_message(message.chat.id, 'Имеются ли у вас рекомендации по нашему сайту?', reply_markup = markup_additional)

        else:
            bot.send_message(message.chat.id, 'Необходимо выбрать оценку в числовом формате: '
                             '\n<b>• 1</b> - точно не порекомендую.'
                             '\n<b>• 10</b> - точно порекомендую.')
            bot.register_next_step_handler(message, question_five)

    except AttributeError:
        bot.send_message(message.chat.id, 'Необходимо выбрать оценку в числовом формате: '
                             '\n<b>• 1</b> - точно не порекомендую.'
                             '\n<b>• 10</b> - точно порекомендую.')
        bot.register_next_step_handler(message, question_five)

def call_me_back(message): # Функция которая выводит номер телефона клиента 

    global number_account   

    try:
        call_me_back_pls = message.contact.phone_number
        call_me_back_pls is not None

        text_vip_support = (f'<b>Хьюстон, у нас звоночек!</b> \n\nКлиент: {number_account}'
                            '\nПросит перезвонить с 10:00 до 20:00'
                            f'\nПо этому номеру ➡️ {call_me_back_pls}\n\nСсылка на таблицу - https://clck.ru/3AGtoK')

        markup_phone = types.ReplyKeyboardRemove(selective = False)

        if not checkId_and_fioInput(number_account, call_me_back_pls):
            pass

        else:
            print(f'\n{'-' * 100} \nНомер счета -> {number_account} '
                                f'\nНомер телефона -> {call_me_back_pls}\n{'-' * 100}')
            
            bot.send_message(chat_id = chat_id_vip_support , text = text_vip_support, disable_web_page_preview = True)

            bot.send_message(message.chat.id,'С вами свяжется наш сотрудник в период с 10:00 до 20:00 по МСК. '
                                'Пожалуйста, ожидайте звонок специалиста.🤗', reply_markup = markup_phone)
            time.sleep(1)
            bot.send_message(message.chat.id, 'При возникновении вопросов, свяжитесь с нами. Мы работаем 24/7 🤝'
                            '\n\nКонтакты ВИП-отдела PARI:'
                            '\n\nEmail 📩: vip@pari.ru'
                            '\nЧат-бот Telegram 📱: http://t.me/VipPARI_bot'
                            '\nТел 📞: 8-800-600-11-55')
            bot.register_next_step_handler(message, theend)
         
    except AttributeError:           
            bot.send_message(message.chat.id, 'Нужно нажать на кнопку "Поделиться номером". '
                             '\nКнопка отображается снизу, если она у вас исчезла, найти ее можно справа внизу, квадрат с четырьмя точками. '
                             '\nНажмите на него и у вас появится кнопка поделиться номером телефона!')
            bot.register_next_step_handler(message, call_me_back)       

def additionalquestion(message):# ДОП вопрос

    global number_account

    additional_question_vip = message.text

    try:
        if len(additional_question_vip) > 4000:
            bot.send_message(message.chat.id,f'Пожалуйста, сократите ваш ответ до <b>4000</b> символов.'
                                            f'\n\nКол-во ваших символов ➡️ <b>{len(additional_question_vip)}</b>')
            bot.register_next_step_handler(message, additionalquestion)

        elif len(additional_question_vip) <= 4000:
        
            if google_pull_q_additionalquestion(number_account, additional_question_vip):
                print(f'\n{'-' * 100} \n\nОтвет ДОП вопрос -> {additional_question_vip} \n{'-' * 100}')
                bot.send_message(message.chat.id,'Благодарим, что проявили интерес и дополнили свои ответы!')
                time.sleep(1)
                bot.send_message(message.chat.id, 'При возникновении вопросов, свяжитесь с нами. Мы работаем 24/7 🤝'
                                '\n\nКонтакты ВИП-отдела PARI:'
                                '\n\nEmail 📩: vip@pari.ru'
                                '\nЧат-бот Telegram 📱: http://t.me/VipPARI_bot'
                                '\nТел 📞: 8-800-600-11-55')

                bot.register_next_step_handler(message, theend)

    except TypeError:
        bot.send_message(message.chat.id,f'Укажите ответ текстом, пожалуйста!')
        bot.register_next_step_handler(message, additionalquestion)
    
def theend(message):# Конец

    bot.send_message(message.chat.id,'При возникновении вопросов, свяжитесь с нами. Мы работаем 24/7 🤝'
                            '\n\nКонтакты ВИП-отдела PARI:'
                            '\nEmail 📩: vip@pari.ru'
                            '\nЧат-бот Telegram 📱: http://t.me/VipPARI_bot'
                            '\nТел 📞: 8-800-600-11-55')
    bot.register_next_step_handler(message, theend)

@bot.callback_query_handler(func = lambda call: True)

def callback(call):# Выбор кнопок

    global number_account
    
    if call.data == 'Yes':
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = '<b>Вопрос №1</b> \n\nЧто вам больше '
                                'всего нравится в нашем приложении/сайте?')
        bot.register_next_step_handler(call.message, question_one)

    elif call.data == 'Callback_me':
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = 'Это команда контроля качества компании PARI. '
                        '\nМы хотим задать вам вопросы по работе нашего сайта/приложения - это займет несколько минут.'
                        '\nГотовы сейчас ответить? Или вам лучше позвонить?')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Чтобы мы смогли связаться с вами, пожалуйста, выберите "Поделиться номером".'
                        '\n\nПри нажатии клавиши "Поделиться номером", вы предоставите ваш номер телефона для консультации с менеджером 📞', reply_markup = markup_phone)       
        bot.register_next_step_handler(call.message, call_me_back)

    elif call.data == 'No':
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = 'Как будет удобно, напишите или нажмите ➡️ /start')


        """Здесь выбор ДОП вопроса """

    elif call.data == 'additional_yes':
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = 'Имеются ли у вас рекомендации по нашему сайту?')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Напишите, пожалуйста, рекомендации одним сообщением 🙏')
        bot.register_next_step_handler(call.message, additionalquestion)

    elif call.data == 'additional_no':
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = 'Имеются ли у вас рекомендации по нашему сайту?')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'Благодарим за прохождение опроса! \nСтановимся лучше для вас 😇')
        time.sleep(1)
        bot.send_message(call.message.chat.id, 'При возникновении вопросов, свяжитесь с нами. Мы работаем 24/7 🤝'
                        '\n\nКонтакты ВИП-отдела PARI:'
                        '\n\nEmail 📩: vip@pari.ru'
                        '\nЧат-бот Telegram 📱: http://t.me/VipPARI_bot'
                        '\nТел 📞: 8-800-600-11-55')
        bot.register_next_step_handler(call.message, theend)


bot.polling(none_stop = True)



# """ Здесь инлайн клавиатура которая отменяет запрос на звонок """
# markup_call_not_back = types.InlineKeyboardMarkup(row_width = 1)

# btn16 = types.InlineKeyboardButton('Отмена звонка!', callback_data = 'not_call')

# markup_call_not_back.add(btn16)



""" Здесь инлайн клавиатура в 4 вопросе """
# markup_4_question = types.InlineKeyboardMarkup(row_width = 1)

# btn4 = types.InlineKeyboardButton('1 – точно нет', callback_data = '4_question:1')
# btn5 = types.InlineKeyboardButton('2 – скорее нет', callback_data = '4_question:2')
# btn6 = types.InlineKeyboardButton('3 – ни да, ни нет', callback_data = '4_question:3')
# btn7 = types.InlineKeyboardButton('4 – скорее да', callback_data = '4_question:4')
# btn8 = types.InlineKeyboardButton('5 – точно да', callback_data = '4_question:5')

# markup_4_question.add(btn4, btn5, btn6, btn7, btn8)



""" Здесь инлайн клавиатура в 5 вопросе """
# markup_5_question = types.InlineKeyboardMarkup(row_width = 1)

# btn9 = types.InlineKeyboardButton('1 – точно нет', callback_data = '5_question:1')
# btn10 = types.InlineKeyboardButton('2 – скорее нет', callback_data = '5_question:2')
# btn11 = types.InlineKeyboardButton('3 – ни да, ни нет', callback_data = '5_question:3')
# btn12 = types.InlineKeyboardButton('4 – скорее да', callback_data = '5_question:4')
# btn13 = types.InlineKeyboardButton('5 – точно да', callback_data = '5_question:5')

# markup_5_question.add(btn9, btn10, btn11, btn12, btn13)



"""Здесь выбор оценки на 4 вопрос """

# elif call.data == '4_question:1':
    
#     btn_4_question = '1'

#     if google_pull_q_grade_4(number_account, btn_4_question):
#         print(f'\n{'-' * 100} \n\nОценка 4 вопроса -> {btn_4_question}  \n{'-' * 100}')
#         bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = '<b>Вопрос №4</b> \n\nУдовлетворены ли '
#                 'вы качеством работы менеджеров службы поддержки PARI?')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, 'Благодарим за оценку!')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, '<b>Вопрос №5</b> \n\nПорекомендовали бы Вы сайт/приложение PARI '
#                 'своим знакомым и друзьям, которых интересуют ставки на спорт?', reply_markup = markup_5_question) 
                
# elif call.data == '4_question:2':

#     btn_4_question = '2'

#     if google_pull_q_grade_4(number_account, btn_4_question):
#         print(f'\n{'-' * 100} \n\nОценка 4 вопроса -> {btn_4_question}  \n{'-' * 100}')
#         bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = '<b>Вопрос №4</b> \n\nУдовлетворены ли '
#                 'вы качеством работы менеджеров службы поддержки PARI?')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, 'Благодарим за оценку!')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, '<b>Вопрос №5</b> \n\nПорекомендовали бы Вы сайт/приложение PARI '
#                 'своим знакомым и друзьям, которых интересуют ставки на спорт?', reply_markup = markup_5_question)

# elif call.data == '4_question:3':

#     btn_4_question = '3'

#     if google_pull_q_grade_4(number_account, btn_4_question):
#         print(f'\n{'-' * 100} \n\nОценка 4 вопроса -> {btn_4_question}  \n{'-' * 100}')
#         bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = '<b>Вопрос №4</b> \n\nУдовлетворены ли '
#                 'вы качеством работы менеджеров службы поддержки PARI?')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, 'Благодарим за оценку!')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, '<b>Вопрос №5</b> \n\nПорекомендовали бы Вы сайт/приложение PARI '
#                 'своим знакомым и друзьям, которых интересуют ставки на спорт?', reply_markup = markup_5_question)
    
# elif call.data == '4_question:4':

#     btn_4_question = '4'

#     if google_pull_q_grade_4(number_account, btn_4_question):
#         print(f'\n{'-' * 100} \n\nОценка 4 вопроса -> {btn_4_question}  \n{'-' * 100}')
#         bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = '<b>Вопрос №4</b> \n\nУдовлетворены ли '
#                 'вы качеством работы менеджеров службы поддержки PARI?')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, 'Благодарим за оценку!')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, '<b>Вопрос №5</b> \n\nПорекомендовали бы Вы сайт/приложение PARI '
#                 'своим знакомым и друзьям, которых интересуют ставки на спорт?', reply_markup = markup_5_question)
    
# elif call.data == '4_question:5':

#     btn_4_question = '5'

#     if google_pull_q_grade_4(number_account, btn_4_question):
#         print(f'\n{'-' * 100} \n\nОценка 4 вопроса -> {btn_4_question}  \n{'-' * 100}')
#         bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = '<b>Вопрос №4</b> \n\nУдовлетворены ли '
#                 'вы качеством работы менеджеров службы поддержки PARI?')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, 'Благодарим за оценку!')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, '<b>Вопрос №5</b> \n\nПорекомендовали бы Вы сайт/приложение PARI '
#                 'своим знакомым и друзьям, которых интересуют ставки на спорт?', reply_markup = markup_5_question)
    


"""Здесь выбор оценки на 5 вопрос """

# elif call.data == '5_question:1':

#     btn_5_question = '1'

#     if google_pull_q_grade_5(number_account, btn_5_question):
#         print(f'\n{'-' * 100} \n\nОценка 5 вопроса -> {btn_5_question}  \n{'-' * 100}')
#         bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = '<b>Вопрос №5</b> \n\nПорекомендовали бы Вы сайт/приложение PARI '
#                 'своим знакомым и друзьям, которых интересуют ставки на спорт?')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, 'Благодарим вас за оценку!')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, 'У вас есть что дополнить?', reply_markup = markup_additional)

# elif call.data == '5_question:2':

#     btn_5_question = '2'

#     if google_pull_q_grade_5(number_account, btn_5_question):
#         print(f'\n{'-' * 100} \n\nОценка 5 вопроса -> {btn_5_question}  \n{'-' * 100}')
#         bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = '<b>Вопрос №5</b> \n\nПорекомендовали бы Вы сайт/приложение PARI '
#                 'своим знакомым и друзьям, которых интересуют ставки на спорт?')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, 'Благодарим вас за оценку!')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, 'У вас есть что дополнить?', reply_markup = markup_additional)

# elif call.data == '5_question:3':

#     btn_5_question = '3'

#     if google_pull_q_grade_5(number_account, btn_5_question):
#         print(f'\n{'-' * 100} \n\nОценка 5 вопроса -> {btn_5_question}  \n{'-' * 100}')
#         bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = '<b>Вопрос №5</b> \n\nПорекомендовали бы Вы сайт/приложение PARI '
#                 'своим знакомым и друзьям, которых интересуют ставки на спорт?')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, 'Благодарим вас за оценку!')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, 'У вас есть что дополнить?', reply_markup = markup_additional)

# elif call.data == '5_question:4':

#     btn_5_question = '4'

#     if google_pull_q_grade_5(number_account, btn_5_question):
#         print(f'\n{'-' * 100} \n\nОценка 5 вопроса -> {btn_5_question}  \n{'-' * 100}')
#         bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = '<b>Вопрос №5</b> \n\nПорекомендовали бы Вы сайт/приложение PARI '
#                 'своим знакомым и друзьям, которых интересуют ставки на спорт?')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, 'Благодарим вас за оценку!')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, 'У вас есть что дополнить?', reply_markup = markup_additional)

# elif call.data == '5_question:5':

#     btn_5_question = '5'

#     if google_pull_q_grade_5(number_account, btn_5_question):
#         print(f'\n{'-' * 100} \n\nОценка 5 вопроса -> {btn_5_question}  \n{'-' * 100}')
#         bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = '<b>Вопрос №5</b> \n\nПорекомендовали бы Вы сайт/приложение PARI '
#                 'своим знакомым и друзьям, которых интересуют ставки на спорт?')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, 'Благодарим вас за оценку!')
#         time.sleep(1)
#         bot.send_message(call.message.chat.id, 'У вас есть что дополнить?', reply_markup = markup_additional)



