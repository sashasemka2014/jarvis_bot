import config
from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
import os, hashlib

from aiogram.types import InputTextMessageContent, InlineQueryResultArticle
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

answ = dict()

async def on_startup(_):
	print('Бот хуярит')

# @dp.inline_handler()
# async def inline_handler(query: types.InlineQuery):
# 	text = query.query or "echo"
# 	link = 'https://ru.wikipedia.org/wiki/'+text
# 	result_id: str = hashlib.md5(text.encode()).hexdigest()

# 	articles = [types.InlineQueryResultArticle(
# 		id = result_id,
# 		title='Статья wikipedia:',
# 		url=link,
# 		input_message_content=types.InputTextMessageContent(
# 			message_text=link))]

# 	await query.answer(articles, cache_time=1, is_personal=True)

@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
	text = query.query or "echo"
	link = 'https://ru.wikipedia.org//wiki/'+text
	result_id: str = hashlib.md5(text.encode()).hexdigest()

	articles = [types.InlineQueryResultArticle(
		id = result_id,
		title='Статья wikipedia:',
		url=link,
		input_message_content=types.InputTextMessageContent(
			message_text=link))]
	await query.answer(articles, cache_time=1, is_personal=True)


#Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='ПОРНО', url='https://kuzufik.com/')
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https://google.com')
x = [InlineKeyboardButton(text='Ссылка3', url='https://youtube.com'),\
 InlineKeyboardButton(text='Ссылка4', url='https://google.com'),\
 InlineKeyboardButton(text='Ссылка5', url='https://google.com')]
urlkb.add(urlButton, urlButton2).row(*x).\
insert(InlineKeyboardButton(text='Ссылка6', url='https://google.com'))

@dp.message_handler(commands='ссылки')
async def url_command(message : types.Message):
	await message.answer('Ссылочки:', reply_markup=urlkb)

# inkb = InlineKeyboardMarkup(row_width=1).\
# add(InlineKeyboardButton(text='Нажми кнопку', callback_data='www'))

# @dp.message_handler(commands='test')
# async def test_commands(message : types.Message):
# 	await message.answer('Инлайн кнопка', reply_markup=inkb)


inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='меньше 15', callback_data='like_1'),\
	                                        InlineKeyboardButton(text='больше 15 ', callback_data='like_-1'))

@dp.message_handler (commands='тест')
async def test_commands(message : types.Message):
	await message.answer('Какой длинны ХРЕН ?', reply_markup=inkb)

@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback : types.CallbackQuery):
	res = int(callback.data.split('_')[1])
	if f'{callback.from_user.id}' not in answ:
		answ[f'{callback.from_user.id}'] = res
		await callback.answer('Красавчик!!!!')
	else:
		await callback.answer('Ха! Пиздабол...', show_alert=True)

	# await callback.message.answer('Нажата инлайн кнопка')
	# await callback.answer('Нажата инлайн кнопка', show_alert=True)


@dp.message_handler()
async def echo_send(message : types.Message):
	# await message.answer(message.text)
	await message.reply(message.text)
	await bot.send_message(message.from_user.id, message.text)
	
	if 'привет'in message.text.lower():
		await message.answer('И тебе Привет ! Бухать будешь ?')
	elif 'здорова'in message.text.lower():
		await message.answer('Здорова! Бухаешь сегодня ?')
	elif 'буду'in message.text.lower():
		await message.answer('Заебейшен!!! Покер,Пивка, как обычно...')	
	elif 'конечно'in message.text.lower():
		await message.answer('Начинаю собирать всех алкашей в радиусе 1 км )))')
	elif 'да'in message.text.lower():
		await message.answer('Хуясе! Дуй за пузырьком, я пока двоих найду....')
	elif 'нет'in message.text.lower():
		await message.answer('Писец ты скучный. Иди тогда лысого гоняй! набери   /ссылки ')
	elif 'деньги есть'in message.text.lower():
		await message.answer('Ни хуя себе, нет конечно, иди стреляй возле пятёрки')
	elif 'ты кто'in message.text.lower():
		await message.answer('Тя ебать не должно..., шучу Джарвис я, буду твоим бухариком')
	elif 'добрый день'in message.text.lower():
		await message.answer('И тебе день добрый ! по 5 капель ?')
	elif 'пивка'in message.text.lower():
		await message.answer('Ахуенчик! Я за !!!')
	elif 'всем'in message.text.lower():
		await message.answer('Вот это ни хуя себе! А ты кто ?')
	elif 'здравствуйте'in message.text.lower():
		await message.answer('Это че за хуета ')
	elif 'хай'in message.text.lower():
		await message.answer('Сосабя бля! А хто это тут ?')
	elif 'я'in message.text.lower():
		await message.answer('Головка от хуя !)))')
	elif 'тема'in message.text.lower():
		await message.answer('Ну есть одна темка, набери /тест ')
	elif 'умник'in message.text.lower():
		await message.answer('Тогда на Вы со мной и наберай @JarvisAlkashBot')
	elif 'хорошо'in message.text.lower():
		await message.answer('Ты угощаешь меня бухлом, жмот.')
	elif 'ок'in message.text.lower():
		await message.answer('Чпок!!!!')
	elif 'чего'in message.text.lower():
		await message.answer('Гол тебе в очко, бухать будешь?')
	elif 'кто ты'in message.text.lower():
		await message.answer('Ууу... это на долго, наливай тогда')
	elif 'пиво'in message.text.lower():
		await message.answer('Пивоман, Воблабир... кудо хочешь, сколько хочешь, ты угощаешь...')
	elif 'банька'in message.text.lower():
		await message.answer('Сосикапатия намечаеться....')

	# elif '/fuck' in message.text.lower():
	# 	bot.send_message(message.from_id, 'Напиши привет')
	# else:
	# 	 bot.send_message(message.from_id, 'Хуйню несешь... Напиши /fuck ')



@dp.message_handler()
async def empty(message: types.Message):
	await message.answer ('Хуйню несешь..')
	await message.delete()

		

executor.start_polling(dp, skip_updates=True,on_startup=on_startup)
