from django.shortcuts import render
from django.conf import settings
from aiogram import Bot, Dispatcher, types, executor
from asgiref.sync import sync_to_async
from logging import basicConfig, INFO

from apps.products.models import Product
from apps.users.models import User

# Create your views here.
bot = Bot(settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
basicConfig(level=INFO)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здравствуйте {message.from_user.full_name}.\nВаш ID чата: {message.chat.id}")

async def send_billing_notification(manager_id:int, shop:str, user:int, products:str, billing_receipt_type:str, payment_code:int, created:str):
    await bot.send_message(manager_id, f"Billing shop: {shop}\nПользователь: {user}\nТовары: {products}\nТип доставки: {billing_receipt_type}\nКод оплаты{payment_code}\nДата создания: {created}")
    # print("NOTIFICATION SEND")