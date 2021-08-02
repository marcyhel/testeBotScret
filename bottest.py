import telebot
import os
import random
import requests as req
from bs4 import BeautifulSoup as bs

BOT_KEY = ''
BOT_CHAVE = ''

#os.environ["BOT_CHAVE"] = "16"

if os.environ.get('BOT_KEY', '') != '':
	BOT_KEY = os.environ['BOT_KEY']
if os.environ.get('BOT_CHAVE', '') != '':
	BOT_CHAVE = os.environ['BOT_CHAVE']

chaves=BOT_KEY.split(";")


os.environ['BOT_CHAVE'] = str((int(BOT_CHAVE)+1))

url='https://www.tecmundo.com.br/noticias'
bss=req.get(url)
bss=bs(bss.text,'html.parser')
print(bss.main.find_all("a",href=True)[0]["href"])

novaURL=bss.main.find_all("a",href=True)[0]["href"]
bss=req.get(novaURL)
bss=bs(bss.text,'html.parser')

categorias=["Segurança","Inteligência artificial","PS4","Xbox One","Ciência","Google","Steam","PC","Astronomia","Software","Internet","Android","Apple","Windows"]
verificado=False

for i in range(len(categorias)):
	for j in bss.find_all("a"):
		if(j.text.strip()==categorias[i]):
			verificado=True
			
if(verificado):
	print(bss.find_all("h1")[0].text.strip())
	titulo="``` "+bss.find_all("h1")[0].text.strip()+" ``` "
	conteudo=''
	for i in range(2,5):
		print(bss.find_all("p")[i].text.strip())
		conteudo+=" _ "+bss.find_all("p")[i].text.strip()+" _ "+'\n'
	conteudo+='\n\n'
	conteudo+=" ``` "+bss.find_all("p")[0].text.strip()+" - "
	conteudo+=bss.find_all("p")[1].text.strip()+'\n' 
	conteudo+="Via TecMundo"+" ``` "






	#enviar=frases[random.randint(0,len(frases)-1)]
bot = telebot.TeleBot(chaves[0])
for i in chaves[1:]:
	bot.send_message(i, text=str(BOT_CHAVE)+" - "+str((int(BOT_CHAVE)+1)), parse_mode= 'Markdown')
	
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
