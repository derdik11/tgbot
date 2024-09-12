from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

replykey = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вернуться назад')]

],
    resize_keyboard= True
)

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Открытие/закрытие', callback_data='Открытие/закрытие')],
    [InlineKeyboardButton(text='Работа с чеками в КЭШ', callback_data='Работа с чеками в КЭШ')],
    [InlineKeyboardButton(text='Движение товара', callback_data='Движение товара')],
    [InlineKeyboardButton(text='Послепродажка', callback_data='Послепродажка')],
    [InlineKeyboardButton(text='Расрочка/кредит/Лизинг', callback_data='Расрочка/кредит/Лизинг')],
    [InlineKeyboardButton(text='Безнал', callback_data='Безнал')],
    [InlineKeyboardButton(text='Прием на комиссию', callback_data='Прием на комиссию')],
    [InlineKeyboardButton(text='Инкассация', callback_data='Инкассация')],

])

key1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Открытие смены', callback_data='Открытие смены')],
    [InlineKeyboardButton(text='Закрытие смены', callback_data='Закрытие смены')],
    [InlineKeyboardButton(text='Назад', callback_data='Back')]

])

key2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Побдор товара, оплата', callback_data='Побдор товара, оплата')],
    [InlineKeyboardButton(text='Добавление СП, формирование чека', callback_data='Добавление СП, формирование чека')],
    [InlineKeyboardButton(text='Продажа сим', callback_data='Продажа сим')],
    [InlineKeyboardButton(text='Прием платежей КИВИ', callback_data='Прием платежей КИВИ')],
    [InlineKeyboardButton(text='Оплата собственной рассрочки (СР)', callback_data='Оплата собственной рассрочки (СР)')],
    #[InlineKeyboardButton(text='Дисплей ОК ', callback_data='Дисплей ОК')],
    [InlineKeyboardButton(text='Назад', callback_data='Back')]

])

key3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Приемка перемещение', callback_data='Приемка перемещение')],
    [InlineKeyboardButton(text='Отправка перемещение', callback_data='Отправка перемещение')],
    [InlineKeyboardButton(text='Заказ товара на ТО', callback_data='Заказ товара на ТО')],
    #[InlineKeyboardButton(text='Заказ не полки', callback_data='Заказ не полки')],
    [InlineKeyboardButton(text='Инвентаризация', callback_data='Инвентаризация')],
    #[InlineKeyboardButton(text='печать ценников', callback_data='печать ценников')],
    [InlineKeyboardButton(text='Назад', callback_data='Back')]

])

key4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Возврат товара', callback_data='Возврат товара')],
    [InlineKeyboardButton(text='Прием в ремонт', callback_data='Прием в ремонт')],
    #[InlineKeyboardButton(text='Прием на ПК', callback_data='Прием на ПК')],
    #[InlineKeyboardButton(text='Выдача подменки', callback_data='Выдача подменки')],
    [InlineKeyboardButton(text='Выдача из ремонта', callback_data='Выдача из ремонта')],
    [InlineKeyboardButton(text='Назад', callback_data='Back')]

])

key5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Заполнение заявки', callback_data='Заполнение заявки')],
    [InlineKeyboardButton(text='Выдача СР + документы', callback_data='Выдача СР + документы')],
    [InlineKeyboardButton(text='Выдача альфа + документ', callback_data='Выдача альфа + документ')],
    [InlineKeyboardButton(text='Выдача БИБ + документ', callback_data='Выдача БИБ + документ')],
    [InlineKeyboardButton(text='Выдача лизинг', callback_data='Выдача лизинг')],
    [InlineKeyboardButton(text='Документы ИЗИ', callback_data='Документы ИЗИ')],
    [InlineKeyboardButton(text='Документы ЛайтЛизинг', callback_data='Документы ЛайтЛизинг')],
    [InlineKeyboardButton(text='Документы ФакторЛизинг', callback_data='Документы ФакторЛизинг')],
    [InlineKeyboardButton(text='Назад', callback_data='Back')]

])


