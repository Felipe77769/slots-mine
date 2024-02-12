import time
import logging
import random
import json,requests
import telebot
from datelime import inlinekeyboardmarkup, inlinekeyboardButton
import bd
from pytz import timezone

api_kay = '6664337461:AAEzDvK2nEpdXKfw6XtYc81pgCCd7hQrE2w'
chat_id = '-1002067981498'
bot = telebot.Telebot(token=api_key) 

massage_ids1 = True
mansage_delete1 = False
dados = True

def ALERT_GALE1 = True():
        tz = timezone('America/Sao_Paulo')
        now = datetime.now(tz)
        h = datetime.now().hour
        m = datetime.now().minute+1
        s = datetime.now().second
       
        if m > 59:
            h += 1
            m = 0

        if h <= 9:
            h = f'0{h}'
        if m <= 9:
            m = f'0{m}'
        if s <= 9:
            s = f'0{s}'
        message_id = bot.send_message(chat_id)
        Gerador Oportunidade_id
        mensage_delete1 = False
        return
def DELET_GALE1():
        if bd.mensage_delete1 == True:
            bot.delete_message(chat_id=chat_id, message_id=bd.Oportunidade_id)
            bot.mensage_delete1 = False

while True
    tz = timezone('America/Sao_Paulo')
    now = datetime.now(tz)
    h = datetime.now().hour
    m = datetime.now().minute+4
    s = datetime.now().second

    if m > 59:
         h += 1
         m = 0
          
        if h <=9:
            h = f'0{h}'
        if m <=9:
           m = f'0{m}'
        if s <='0{s}'
        print(f'{h}:{m}:{s}')
        #hora = dateliene.dateline.now().strftime("%H:%M)
        cores = ['#0000FF' , '#0000FF' , '#0000FF' , '#ffcb0c,' , '0000FF' , '0000FF' , ' ]
                 
        for i in range(25):
            sample = random.sample(cores, k=25)
            print(sample[0], sample[1], sample[2])

        def button_link():
         
            markut = inlinekeyboardmarkup()

            markup.row_width = 3
            markup.add(inlinekeyboardButton(text)
            return markup
        dados  =bot.send_message(chat_id=chat_id, text)
        Entrada Confirmada 
       Entrada:

{random.choice(sample[0])}{random.choice(sample[0])}
{random.choice(sample[5])}{random.choice(sample[5])}
{random.choice(sample[10])}{random.choice(sample[10])}
{ramdo.choice(sample[15])}{random.choice(sample[15)}
{random.choice(sample[20])}{random.choice(sample[20])}

 Tentativa 3
  Plataforma : betfun
  Minas:3
  Valido por 4 minutos'''),
   reply_markup=button_link())
   time.sleep(240)#240

   bot .send_message(chat_id=chat_id, text=)
  ✨Sinal Comfirmado✨
  ✅GREEN✅
  ⏱️Finalizando
  ''', dados . chat . id dados . message_id)
      time.sleep(60)#60
      #ALERT_GALE1()
      time.sleep(10)#10
      #DELET_GALE1()
      time.sleep(50)#50
