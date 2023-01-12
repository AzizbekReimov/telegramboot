from aiogram import types

from loader import dp, bot
from aiogram.dispatcher import FSMContext
from states.server import Server
import time
from datetime import datetime as dt
from data.config import ADMINS
from keyboards.inline.creat_server import server_keyboard, server_callback
from data.config import servers, server_keys, server_namee

server_menu = {"local_server":"servers"}
message_list = []
f_message_list = []

@dp.message_handler(commands="creat_server")
async def creat_server(msg: types.Message):
    text0 = f"сервер яратиш жарайони<b>🔎 • • • • •</b>"
    text1 = f"сервер яратиш жарайони<b>• 🔎 • • • •</b>"
    text2 = f"сервер яратиш жарайони<b>• • 🔎 • • • </b>"
    text3 = f"сервер яратиш жарайони<b>• • • 🔎 • •</b>"
    text4 = f"сервер яратиш жарайони<b>• • • • 🔎 •</b>"
    text5 = f"сервер яратиш жарайони<b>• • • • • 🔎</b>"
    #n = await bot.send_message(chat_id=msg.from_user.id, text=text0)
    #time.sleep(0.4)
    #n1 = await bot.edit_message_text(chat_id=msg.from_user.id, text=text1, message_id=n.message_id)
    #time.sleep(0.4)
    #n2 = await bot.edit_message_text(chat_id=msg.from_user.id, text=text2, message_id=n1.message_id)
    #time.sleep(0.4)
    #n3 = await bot.edit_message_text(chat_id=msg.from_user.id, text=text3, message_id=n2.message_id)
    #time.sleep(0.4)
    #n4 = await bot.edit_message_text(chat_id=msg.from_user.id, text=text4, message_id=n3.message_id)
    #time.sleep(0.4)
    #n5 = await bot.edit_message_text(chat_id=msg.from_user.id, text=text5, message_id=n4.message_id)
    #time.sleep(0.4)
    #n6 = await bot.edit_message_text(chat_id=msg.from_user.id, text=text0, message_id=n5.message_id)
    #time.sleep(0.4)
    #n7 = await bot.edit_message_text(chat_id=msg.from_user.id, text=text1, message_id=n6.message_id)
    #time.sleep(0.4)
    #n8 = await bot.edit_message_text(chat_id=msg.from_user.id, text=text2, message_id=n7.message_id)
    #time.sleep(0.4)
    #n1 = await bot.edit_message_text(chat_id=msg.from_user.id, text=text3, message_id=n8.message_id)
    #time.sleep(0.4)
    #n2 = await bot.edit_message_text(chat_id=msg.from_user.id, text=text4, message_id=n1.message_id)
    #time.sleep(0.4)
    #n3 = await bot.edit_message_text(chat_id=msg.from_user.id, text=text5, message_id=n2.message_id)
    #time.sleep(0.4)
    #n4 = await bot.edit_message_text(chat_id=msg.from_user.id, text=text0, message_id=n3.message_id)
    #time.sleep(0.4)
    #n5 = await bot.edit_message_text(chat_id=msg.from_user.id, text=text1, message_id=n4.message_id)
    #time.sleep(0.4)
    #n6 = await bot.edit_message_text(chat_id=msg.from_user.id, text=text2, message_id=n5.message_id)
    #time.sleep(0.4)
    #n7 = await bot.edit_message_text(chat_id=msg.from_user.id, text=text3, message_id=n6.message_id)
    #time.sleep(0.4)
    #n8 = await bot.edit_message_text(chat_id=msg.from_user.id, text=text4, message_id=n7.message_id)
    #time.sleep(0.4)
    #await bot.delete_message(chat_id=msg.from_user.id, message_id=n8.message_id)
    m1 = await msg.answer(f"Серверга ном беринг.\n\n<b>Огохлантириш</b>\nсервер номи 15дан ошиб кетмаслиги керак❗️")
    message_list.append(msg.from_user.id)
    f_message_list.append(msg.from_user.id)
    f_message_list.append(msg.message_id)
    message_list.append(m1.message_id)
    await Server.server_name.set()

@dp.message_handler(state=Server.server_name)
async def server_name(msg: types.Message, state: FSMContext):
    f_message_list.append(msg.message_id)
    server_name = msg.text
    if len(server_name)>=15:
        m2 = await msg.answer(f"<b>Хатолик‼️</b>\nсервер номи 15дан ошиб кетти‼️\n\n<b>Яна уруниб коринг</b>")
        message_list.append(m2.message_id)
    else:
        await state.update_data(
            {"server_name":server_name}
        )
        m3 = await msg.answer(f"серверда нечта иштирокчи катнашади.\n\n<b>Огохлантириш</b>\nминимум --> 4\nмаксимум --> 10❗️")
        message_list.append(m3.message_id)
        await Server.next()

@dp.message_handler(state=Server.server_player)
async def server_player(msg: types.Message, state: FSMContext):
    f_message_list.append(msg.message_id)
    try:
        int(msg.text)
    except ValueError:
        m4 = await msg.answer(f"<b>Хатолик‼️</b>\nбутун сон киритинг‼️\n\n<b>Яна уруниб коринг</b>")
        message_list.append(m4.message_id)
    else:
        if int(msg.text)>10 or int(msg.text)<4:
            m5 = await msg.answer(f"<b>Хатолик‼️</b>\nминимум --> 4\n максимум --> 10‼️\n\n<b>Яна уруниб коринг</b>")
            message_list.append(m5.message_id)
        else:
            await state.update_data(
                {"player_num":int(msg.text)}
            )
            m6 = await msg.answer(f"серверда кайсидир каманда канча балл йигса йутади.\n\n<b>Огохлантириш</b>\nминимум --> 15000\nмаксимум --> 25000❗️")
            message_list.append(m6.message_id)
            await Server.next()

kerakli_royxat = []
server_malumoti = []
juda_kerak = []
@dp.message_handler(state=Server.server_ball_over)
async def server_player(msg: types.Message, state: FSMContext):
    f_message_list.append(msg.message_id)
    try:
        float(msg.text)
    except ValueError:
        m10 = await msg.answer(f"<b>Хатолик‼️</b>\nбутун сон киритинг‼️\n\n<b>Яна уруниб коринг</b>")
        message_list.append(m10.message_id)
    else:
        if float(msg.text)>25000 or float(msg.text)<15000:
            m11 = await msg.answer(f"<b>Хатолик‼️</b>\nминимум --> 15000\n максимум --> 25000\n\n<b>Яна уруниб коринг</b>")
            message_list.append(m11.message_id)
        else:
            date = dt.now()
            time = date.strftime(f"/%m/%Y, %H:%M")
            day = date.strftime(f"%d")
            await state.update_data(
                {"ball":float(10000),
                "ball_over":float(msg.text),
                "date_creat_server":time,
                "day":int(day),
                "server_admin":[msg.from_user.full_name, msg.from_user.id, msg.from_user.username]}
            )
    
            data = await state.get_data()
            juda_kerak.append(data)
            server_name = data.get("server_name")
            player_num = data.get("player_num")
            ball = data.get("ball")
            ball_over = data.get("ball_over")
            date_creat_server = data.get("date_creat_server")
            server_admin = data.get("server_admin")
            day = data.get("day")
            server_malumoti.append(server_name)
            server_malumoti.append(player_num)
            server_malumoti.append(ball)
            server_malumoti.append(ball_over)
            server_malumoti.append(date_creat_server)
            server_malumoti.append(server_admin)
            server_malumoti.append(day)
            text = f"Сервернинг админи: ism = {server_admin[0]} telegram_id = {server_admin[1]} username = {server_admin[2]},\n"
            text += f"Сервер номи: {server_name},\n"
            text += f"Серверда канча одам катнашади: {player_num},\n"
            text += f"Серверга берилган балл: {ball},\n"
            text += f"Серверда якуний балл: {ball_over},\n"
            text += f"Сервер яратилган вакт: {day}{date_creat_server}\n"
            nn1 = await msg.answer(f"Админ жавобини кутинг")
            nn2 = await bot.send_message(chat_id=ADMINS[0], text=text, reply_markup=server_keyboard)
            kerakli_royxat.append(msg.from_user.id)
            kerakli_royxat.append(nn1.message_id)
            kerakli_royxat.append(nn2.message_id)
            kerakli_royxat.append(day)
            kerakli_royxat.append(date_creat_server)
            kerakli_royxat.append(text)
            await state.finish()

@dp.callback_query_handler(server_callback.filter(action="creat"))
async def creat(call: types.CallbackQuery):
    await bot.delete_message(chat_id=kerakli_royxat[0], message_id=kerakli_royxat[1])
    await bot.delete_message(chat_id=ADMINS[0], message_id=kerakli_royxat[2])
    son = 1
    son1 = 0
    while True:
        if son!=len(message_list):
            await bot.delete_message(chat_id=message_list[0], message_id=message_list[son])
            son += 1
        else:
            while True:
                if son1!=len(message_list):
                    del message_list[-1]
                else:
                    break
            break
    son = 1
    son1 = 0
    while True:
        if son!=len(f_message_list):
            await bot.delete_message(chat_id=f_message_list[0], message_id=f_message_list[son])
            son += 1
        else:
            while True:
                if son1!=len(f_message_list):
                    del f_message_list[-1]
                else:
                    break
            break 

    await call.answer("Сервер яратишга рухсат бердингиз", show_alert=True)
    text1 = f"Сизнинг серверингиз кабул килинди✅\nСервер муддати: {int(kerakli_royxat[3])+2}{kerakli_royxat[4]}\
        \n                          5"
    text2 = f"Сизнинг серверингиз кабул килинди✅\nСервер муддати: {int(kerakli_royxat[3])+2}{kerakli_royxat[4]}\
        \n                          4"
    text3 = f"Сизнинг серверингиз кабул килинди✅\nСервер муддати: {int(kerakli_royxat[3])+2}{kerakli_royxat[4]}\
        \n                          3"
    text4 = f"Сизнинг серверингиз кабул килинди✅\nСервер муддати: {int(kerakli_royxat[3])+2}{kerakli_royxat[4]}\
        \n                          2"
    text5 = f"Сизнинг серверингиз кабул килинди✅\nСервер муддати: {int(kerakli_royxat[3])+2}{kerakli_royxat[4]}\
        \n                          1"
    text6 = f"Сизнинг серверингиз кабул килинди✅\nСервер муддати: {int(kerakli_royxat[3])+2}{kerakli_royxat[4]}\
        \n                          0"
    msg1 = await bot.send_message(chat_id=kerakli_royxat[0], text=text1)
    #time.sleep(1)
    msg2 = await bot.edit_message_text(chat_id=kerakli_royxat[0], text=text2, message_id=msg1.message_id)
    #time.sleep(1)
    msg3 = await bot.edit_message_text(chat_id=kerakli_royxat[0], text=text3, message_id=msg2.message_id)
    #time.sleep(1)
    msg4 = await bot.edit_message_text(chat_id=kerakli_royxat[0], text=text4, message_id=msg3.message_id)
    #time.sleep(1)
    msg5 = await bot.edit_message_text(chat_id=kerakli_royxat[0], text=text5, message_id=msg4.message_id)
    #time.sleep(1)
    msg6 = await bot.edit_message_text(chat_id=kerakli_royxat[0], text=msg5.message_id, message_id=msg5.message_id)
    await bot.edit_message_text(chat_id=kerakli_royxat[0], text=kerakli_royxat[5], message_id=msg6.message_id)
    
    servers[server_malumoti[0]]={}
    servers[server_malumoti[0]]['max_player_num']=server_malumoti[1]
    servers[server_malumoti[0]]['ball']=server_malumoti[2]
    servers[server_malumoti[0]]['ball_over']=server_malumoti[3]
    servers[server_malumoti[0]]['creat_date_server']=f"{server_malumoti[6]}{server_malumoti[4]}"
    servers[server_malumoti[0]]['srok_server']=f"{int(server_malumoti[6])+2}{server_malumoti[4]}"
    servers[server_malumoti[0]]['day']=server_malumoti[6]
    servers[server_malumoti[0]]['admin_server']=server_malumoti[5]
    servers[server_malumoti[0]]['players']=[]

    server_keys[server_malumoti[0]]=servers[server_malumoti[0]]['players']
    server_namee.append(server_malumoti[0])

    del server_malumoti[-1]
    del server_malumoti[-1]
    del server_malumoti[-1]
    del server_malumoti[-1]
    del server_malumoti[-1]
    del server_malumoti[-1]
    del server_malumoti[-1]


    del kerakli_royxat[-1]
    del kerakli_royxat[-1]
    del kerakli_royxat[-1]
    del kerakli_royxat[-1]
    del kerakli_royxat[-1]
    del kerakli_royxat[-1]

@dp.callback_query_handler(server_callback.filter(action="cancel"))
async def cancel(call: types.CallbackQuery):
    await bot.delete_message(chat_id=kerakli_royxat[0], message_id=kerakli_royxat[1])
    await bot.delete_message(chat_id=ADMINS[0], message_id=kerakli_royxat[2])

    son = 1
    son1 = 0
    while True:
        if son!=len(message_list):
            await bot.delete_message(chat_id=message_list[0], message_id=message_list[son])
            son += 1
        else:
            while True:
                if son1!=len(message_list):
                    del message_list[-1]
                else:
                    break
            break

    await call.answer("Сервер рад килинди", show_alert=True)
    await bot.send_message(chat_id=kerakli_royxat[0], text=f"Сизнинг серверингиз кабул килинмади❌")

    del kerakli_royxat[-1]
    del kerakli_royxat[-1]
    del kerakli_royxat[-1]
