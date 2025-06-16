from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import unicodedata

def limpiar_texto(texto):
    # Convierte a minúsculas, elimina tildes y normaliza
    texto = texto.lower().strip()
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    return texto

TOKEN = '7939012209:AAHIrmg-GmzsyrrLwubATqolEXJckbJsC6Y'
    # Ejecutar el archivo en consola bash: nohup python3 bot.py > salida_bot.out 2>&1 &

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌟Holaaaa exploradora de mi corazón! 🌟\n\nContinúa la búsqueda del tesoro que diseñé para ti... Esta pista es secreta, pero sé que podrás encontrarla, eres mi detective favorita...\n\n🔍 \n\nCuando estés lista, dime la palabra secreta..."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = limpiar_texto(update.message.text)

    if "estoy buscando mi tesoro" in text:
        await update.message.reply_text("Perfecto mi reina linda🕺, ahora tu tarea 🕵️‍♀️, es averiguar las palabras correctas 🔍que te llevarán a la siguiente aventura.🧗‍♀️.. Tu peux y arriver, mon amour. Ne lâche pas ma main  🫱et continuons à marcher dans cette grande aventure d’amour ! 💖")

    elif "je serai la" in text:
        await update.message.reply_text("Je savais que tu y arriverais, mon amour… Comme toujours, je suis tellement fier de toi 💝.\nMaintenant, je veux que tu prennes ta rame et que tu vogues 🚣 jusqu’à trouver l’île perdue du trésor qui t’appartient.\nJe te laisse la rame pour que tu puisses avancer 🛶.") 

    else:
        await update.message.reply_text("Amorcito 😘 \nUn esfuerzo más 💪podría ser clave para descubrir lo que hay más allá de Orión,👀 en donde estaremos juntos. \nTe espero allí,✨ Solo faltas tú")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot iniciado...")
    app.run_polling()
