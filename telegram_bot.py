from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests 


token = "YOUR_TELEGRAM_BOT_TOKEN"
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f'/ip - ip address of the user \n ')
async def ip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if len(context.args) == 0:
            await update.message.reply_text(f'Please provide an IP address. Usage: /ip <IP_ADDRESS>')
            return
        else:
         ip_address = context.args[0]
         response = requests.get(f'http://ip-api.com/json/{ip_address}')
         if response.status_code == 200:
              data =response.json()
              if data['status'] == 'success':
                   country = data['country']
                   region = data['regionName']
                   city = data['city']
                   isp = data['isp']
                   await update.message.reply_text(f'IP Address: {ip_address}\nCountry: {country}\nRegion: {region}\nCity: {city}\nISP: {isp}')
              else:
                   await update.message.reply_text(f'Error: {data["message"]}')
async def dns(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if len(context.args) == 0:
            await update.message.reply_text(f'Please provide a domain name. Usage: /dns <DOMAIN_NAME>')
            return
        else:
                dns_name = context.args[0]
                response = requests.get(f'http://edns.ip-api.com/json/{dns_name}')
                if response.status_code == 200:
                    data = response.json()
                    await update.message.reply_text(f'IP: {data[0]["ip"]}\nGeo: {data[0]["geo"]}')


app = ApplicationBuilder().token(token).build()
app.add_handler(CommandHandler("ip", ip))
app.add_handler(CommandHandler("dns", dns))
app.add_handler(CommandHandler("help", help))

app.run_polling()

