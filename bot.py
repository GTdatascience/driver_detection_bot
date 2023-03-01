# TOKEN FOR SLEEPING JIMMY= '5626289703:AAGe5g4Kzi0cChUbfiSFvxf9mF6K07f5frE'

from aiogram import Bot, Dispatcher, executor, types
from driver_class import driver_detection

# logging.basicConfig(level=logging.INFO,filename="logs.log") 

bot = Bot(token='5626289703:AAGe5g4Kzi0cChUbfiSFvxf9mF6K07f5frE')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start']) 
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Пришлите мне фотографию водителя, и я попробую определить спит он или нет.'
    # logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await message.reply(text)

@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    await message.photo[-1].download('test.jpg')
    
@dp.message_handler() 
async def send_response(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = driver_detection('test.jpg')
    print(text)
    # logging.info(f'{user_name=} {user_id=} sent message: {text}')
    await bot.send_message(user_id, text)    

if __name__ == '__main__':
    executor.start_polling(dp)