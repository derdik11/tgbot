import asyncio
from aiogram import F, Router, Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.types import Message, FSInputFile, InputMediaPhoto

from aiogram.types import ChatPermissions
import hand.key as k


r = Router()

async def send_video_with_text(callback: CallbackQuery, video_path: str, start: int, end: int, markup):
    await callback.answer('Идет загрузка')

    video = FSInputFile(video_path, chunk_size=1024 * 1024)

    video_file =await callback.bot.send_video(chat_id=callback.message.chat.id, video=video, height=2000, width=4000)
    with open('hand/text.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    text_to_send = ''.join(lines[start:end])

    text = await callback.message.answer(text_to_send, reply_markup=markup)

    await asyncio.sleep(72000)

    await text.delete()

    await video_file.delete()

async def send_text(callback: CallbackQuery, start: int, end: int, markup):
    await callback.answer('Идет загрузка')
    
    with open('hand/text.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    text_to_send = ''.join(lines[start:end])

    text = await callback.message.answer(text_to_send, reply_markup=markup)

    await asyncio.sleep(72000)

    await text.delete()


async def clear(text):
    await asyncio.sleep(72000)

    await text.delete()

async def clear_media(bot, chat_id, message_ids):
    await asyncio.sleep(64800)  
    for message_id in message_ids:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        


@r.message(CommandStart())
async def cmd_start(message: Message):
    answer = await message.answer('Привет, я бот, который поможет тебе узнать необходимую информацию!', reply_markup=k.main)


    await asyncio.sleep(72000) 
    await message.delete()

    await clear(text= answer)



@r.callback_query(F.data == 'Back')
async def catalog(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Привет, я бот, который поможет тебе узнать необходимую информацию!',reply_markup=k.main)

    await clear(text= callback.message)

@r.message(lambda message: message.text == 'Вернуться назад')
async def go_back(message: types.Message):
    answer = await message.answer('Привет, я бот, который поможет тебе узнать необходимую информацию!', reply_markup=k.main)

    await asyncio.sleep(72000) 
    await message.delete()

    await clear(text= answer)
    

@r.callback_query(F.data == 'Открытие/закрытие')
async def catalog(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Открытие/закрытие',reply_markup=k.key1)

    await clear(text= callback.message)

@r.callback_query(F.data == 'Работа с чеками в КЭШ')
async def catalog(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Работа с чеками в КЭШ',reply_markup=k.key2)

    await clear(text= callback.message)

@r.callback_query(F.data == 'Движение товара')
async def catalog(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Движение товара',reply_markup=k.key3)

    await clear(text= callback.message)

@r.callback_query(F.data == 'Послепродажка')
async def catalog(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Послепродажка',reply_markup=k.key4)

    await clear(text= callback.message)

@r.callback_query(F.data == 'Расрочка/кредит/Лизинг')
async def catalog(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Расрочка/кредит/Лизинг',reply_markup=k.key5)

    await clear(text= callback.message)

@r.callback_query(F.data == 'Безнал')
async def handle_cashless(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/выдача безнала.mp4', 251, 266, k.replykey)

@r.callback_query(F.data == 'Прием на комиссию')
async def handle_commission(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/договор комиссии.mp4', 266, 284, k.replykey)

@r.callback_query(F.data == 'Инкассация')
async def handle_collection(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/инкассация.mp4', 0, 16, k.replykey)

@r.callback_query(F.data == 'Выдача из ремонта')
async def handle_repair_issue(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/выдача ТА из ремонта.mp4', 17, 36, k.replykey)

@r.callback_query(F.data == 'Заказ товара на ТО')
async def handle_order(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/заказ товара на ТО.mp4', 37, 51, k.replykey)

@r.callback_query(F.data == 'Закрытие смены')
async def handle_shift_close(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/закрытие смены_.mp4', 52, 72, k.replykey)

@r.callback_query(F.data == 'Продажа сим')
async def handle_sim_sale(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/Оплата подключения сим-карты.mp4', 73, 87, k.replykey)

@r.callback_query(F.data == 'Открытие смены')
async def handle_shift_open(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/открытие смены.mp4', 88, 103, k.replykey)

@r.callback_query(F.data == 'Отправка перемещение')
async def handle_transfer(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/перемещение.mp4', 103, 124, k.replykey)

@r.callback_query(F.data == 'Прием платежей КИВИ')
async def handle_qiwi(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/платеж киви.mp4', 124, 141, k.replykey)

@r.callback_query(F.data == 'Прием в ремонт')
async def handle_repair_accept(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/прием_товара.mp4', 404, 434, k.replykey)

@r.callback_query(F.data == 'Приемка перемещение')
async def handle_transfer_accept(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/приемка товара из перемещения.mp4', 141, 155, k.replykey)

@r.callback_query(F.data == 'Инвентаризация')
async def handle_inventory(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/инвента группы товаров.mp4', 155, 169, k.replykey)

@r.callback_query(F.data == 'Выдача лизинг')
async def handle_lease_issue(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/договор лизинга.mp4', 169, 186, k.replykey)

@r.callback_query(F.data == 'Возврат товара')
async def handle_return_goods(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/возврат товара_.mp4', 434, 468, k.replykey)

@r.callback_query(F.data == 'Побдор товара, оплата')
async def handle_select_goods_payment(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/сложная оплата.mp4', 359, 372, k.replykey)

@r.callback_query(F.data == 'Добавление СП, формирование чека')
async def handle_adding_sp(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/формирование_чека_сервис_и_сп_через_подбор.mp4', 372, 392, k.replykey)

@r.callback_query(F.data == 'Оплата собственной рассрочки (СР)')
async def handle_payment_sr(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/оплата ср.mp4', 284, 301, k.replykey)

@r.callback_query(F.data == 'Заполнение заявки')
async def handle_form_application(callback: CallbackQuery):
    await send_video_with_text(callback, 'hand/video/формирование фин.mp4', 232, 251, k.replykey)

@r.callback_query(F.data == 'Документы ФакторЛизинг')
async def handle_documents_factor_leasing(callback: CallbackQuery):
    file_paths = [
        'hand/pict/фактор/photo_1.jpg',
        'hand/pict/фактор/photo_2.jpg',
        'hand/pict/фактор/photo_3.jpg',
        'hand/pict/фактор/photo_4.jpg',
        'hand/pict/фактор/photo_5.jpg',
        'hand/pict/фактор/photo_6.jpg',
        'hand/pict/фактор/photo_7.jpg'
    ]


    media = []
    for file in file_paths:
        fs_input_file = FSInputFile(file) 
        media_photo = InputMediaPhoto(media=fs_input_file) 
        media.append(media_photo)

 
    media_messages = await callback.bot.send_media_group(chat_id=callback.message.chat.id, media=media)


    message_ids = [message.message_id for message in media_messages]


    await send_text(callback, 186, 198, k.replykey)

    await clear_media(callback.bot, callback.message.chat.id, message_ids)

@r.callback_query(F.data == 'Документы ЛайтЛизинг')
async def handle_documents_light_leasing(callback: CallbackQuery):
    file_paths1 = [
        'hand/pict/лайт/photo_1.jpg',
        'hand/pict/лайт/photo_2.jpg',
        'hand/pict/лайт/photo_3.jpg',
        'hand/pict/лайт/photo_4.jpg',
        'hand/pict/лайт/photo_5.jpg',
        'hand/pict/лайт/photo_6.jpg',
        'hand/pict/лайт/photo_7.jpg',
        'hand/pict/лайт/photo_8.jpg',
        'hand/pict/лайт/photo_9.jpg',
        'hand/pict/лайт/photo_10.jpg'
    ]
    media1 = [InputMediaPhoto(media=FSInputFile(file)) for file in file_paths1]
    media_messages1 = await callback.bot.send_media_group(chat_id=callback.message.chat.id, media=media1)

    file_paths2 = [
        'hand/pict/лайт/photo_11.jpg',
        'hand/pict/лайт/photo_12.jpg',
        'hand/pict/лайт/photo_13.jpg'
    ]
    media2 = [InputMediaPhoto(media=FSInputFile(file)) for file in file_paths2]
    media_messages2 = await callback.bot.send_media_group(chat_id=callback.message.chat.id, media=media2)

    message_ids = [message.message_id for message in media_messages1] + [message.message_id for message in media_messages2]

    await send_text(callback, 198, 214, k.replykey)

    await clear_media(callback.bot, callback.message.chat.id, message_ids)

@r.callback_query(F.data == 'Документы ИЗИ')
async def handle_documents_easy(callback: CallbackQuery):
    file_paths1 = [
        'hand/pict/изи/photo_1_2024-08-19_17-23-25.jpg',
        'hand/pict/изи/photo_2_2024-08-19_17-23-25.jpg',
        'hand/pict/изи/photo_3_2024-08-19_17-23-25.jpg',
        'hand/pict/изи/photo_4_2024-08-19_17-23-25.jpg',
        'hand/pict/изи/photo_5_2024-08-19_17-23-25.jpg',
        'hand/pict/изи/photo_6_2024-08-19_17-23-25.jpg',
        'hand/pict/изи/photo_7_2024-08-19_17-23-25.jpg',
        'hand/pict/изи/photo_8_2024-08-19_17-23-25.jpg',
        'hand/pict/изи/photo_9_2024-08-19_17-23-25.jpg',
        'hand/pict/изи/photo_10_2024-08-19_17-23-25.jpg'
    ]
    media1 = [InputMediaPhoto(media=FSInputFile(file)) for file in file_paths1]
    media_messages1 = await callback.bot.send_media_group(chat_id=callback.message.chat.id, media=media1)

    file_paths2 = [
        'hand/pict/изи/photo_2024-08-19_07-15-10.jpg',
        'hand/pict/изи/photo_2024-08-19_07-15-10_2.jpg'
    ]
    media2 = [InputMediaPhoto(media=FSInputFile(file)) for file in file_paths2]
    media_messages2 = await callback.bot.send_media_group(chat_id=callback.message.chat.id, media=media2)

    message_ids = [message.message_id for message in media_messages1] + [message.message_id for message in media_messages2]

    await send_text(callback, 214, 232, k.replykey)

    await clear_media(callback.bot, callback.message.chat.id, message_ids)

@r.callback_query(F.data == 'Выдача БИБ + документ')
async def catalog(callback: CallbackQuery):
    file_paths = [
        'hand/pict/БИБ/photo_1_2024-08-19_17-21-19.jpg',
        'hand/pict/БИБ/photo_2_2024-08-19_17-21-19.jpg',
        'hand/pict/БИБ/photo_3_2024-08-19_17-21-19.jpg',
        'hand/pict/БИБ/photo_4_2024-08-19_17-21-19.jpg',
        'hand/pict/БИБ/photo_5_2024-08-19_17-21-19.jpg',
        'hand/pict/БИБ/photo_6_2024-08-19_17-21-19.jpg',
        'hand/pict/БИБ/photo_7_2024-08-19_17-21-19.jpg',
        'hand/pict/БИБ/photo_8_2024-08-19_17-21-19.jpg',
        'hand/pict/БИБ/photo_9_2024-08-19_17-21-19.jpg',
        'hand/pict/БИБ/photo_10_2024-08-19_17-21-19.jpg'
    ]
    
    media = [InputMediaPhoto(media=FSInputFile(file)) for file in file_paths]
    media_messages = await callback.bot.send_media_group(chat_id=callback.message.chat.id, media=media)

    message_ids = [message.message_id for message in media_messages]

    await send_text(callback, 392, 404, k.replykey)

    await clear_media(callback.bot, callback.message.chat.id, message_ids)

@r.callback_query(F.data == 'Выдача альфа + документ')
async def handle_issue_alpha(callback: CallbackQuery):
    file_paths = [
        'hand/pict/альфа/photo_1.jpg',
        'hand/pict/альфа/photo_2.jpg',
        'hand/pict/альфа/photo_3.jpg',
        'hand/pict/альфа/photo_4.jpg',
        'hand/pict/альфа/photo_5.jpg',
        'hand/pict/альфа/photo_6.jpg',
        'hand/pict/альфа/photo_7.jpg',
        'hand/pict/альфа/photo_8.jpg',
        'hand/pict/альфа/photo_9.jpg',
        'hand/pict/альфа/photo_10.jpg'
    ]
    
    media = [InputMediaPhoto(media=FSInputFile(file)) for file in file_paths]
    media_messages = await callback.bot.send_media_group(chat_id=callback.message.chat.id, media=media)

    file_paths2 = [
        'hand/pict/альфа/photo_11.jpg',
        'hand/pict/альфа/photo_12.jpg',
        'hand/pict/альфа/photo_13.jpg'
    ]

    media2 = [InputMediaPhoto(media=FSInputFile(file)) for file in file_paths2]
    media_messages2 = await callback.bot.send_media_group(chat_id=callback.message.chat.id, media=media2)

    message_ids = [message.message_id for message in media_messages] + [message.message_id for message in media_messages2]

    await send_video_with_text(callback, 'hand/video/печать доков альфы.mp4', 331, 359, k.replykey)

    await clear_media(callback.bot, callback.message.chat.id, message_ids)

@r.callback_query(F.data == 'Выдача СР + документы')
async def handle_issue_sr(callback: CallbackQuery):
    file_paths = [
        'hand/pict/ср/photo1.jpg',
        'hand/pict/ср/photo2.jpg',
        'hand/pict/ср/photo3.jpg',
        'hand/pict/ср/photo4.jpg',
        'hand/pict/ср/photo5.jpg',
        'hand/pict/ср/photo6.jpg',
        'hand/pict/ср/photo7.jpg',
        'hand/pict/ср/photo8.jpg',
        'hand/pict/ср/photo9.jpg',
        'hand/pict/ср/photo10.jpg'
    ]

    media = [InputMediaPhoto(media=FSInputFile(file)) for file in file_paths]
    media_messages = await callback.bot.send_media_group(chat_id=callback.message.chat.id, media=media)

    message_ids = [message.message_id for message in media_messages]

    await send_video_with_text(callback, 'hand/video/печать договора СР.mp4', 301, 331, k.replykey)

    await clear_media(callback.bot, callback.message.chat.id, message_ids)