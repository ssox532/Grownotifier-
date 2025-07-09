import discord
from discord.ext import commands
import datetime

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # necesario para enviar DMs

bot = commands.Bot(command_prefix="!", intents=intents)

ultimo_evento = {
    "bug egg": None,
    "master sprinkler": None,
    "hot air balloon": None,
    "paradise egg": None,
    "sugar apple": None,
    "burning bud": None
}

cooldown = 60  # segundos entre eventos repetidos

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    contenido = message.content.lower()
    ahora = datetime.datetime.now()

    def puede_responder(evento):
        anterior = ultimo_evento.get(evento)
        if not anterior or (ahora - anterior).total_seconds() > cooldown:
            ultimo_evento[evento] = ahora
            return True
        return False

    # 🐛 Bug Egg
    if "bug egg" in contenido and puede_responder("bug egg"):
        await message.channel.send("🔔 ¡BUG EGG DETECTADO!")
        await message.add_reaction("🐛")
        await enviar_dm(message.author, "🐛 ¡BUG EGG DETECTADO!")

    # 💧 Master Sprinkler
    elif ("master sprinkler" in contenido or "máster sprinkler" in contenido) and puede_responder("master sprinkler"):
        await message.channel.send("💧 ¡Sprinkler legendario detectado!")
        await message.add_reaction("💦")
        await enviar_dm(message.author, "💧 ¡MASTER SPRINKLER DETECTADO!")

    # 🎈 Hot Air Balloon
    elif ("hot air balloon" in contenido or "globo de aire caliente" in contenido) and puede_responder("hot air balloon"):
        await message.channel.send("🎈 ¡GLOBO DE AIRE CALIENTE DETECTADO!")
        await message.add_reaction("🎈")
        await enviar_dm(message.author, "🎈 ¡HOT AIR BALLOON DETECTADO!")

    # 🏝️ Paradise Garden Egg
    elif "paradise garden egg" in contenido and puede_responder("paradise egg"):
        await message.channel.send("🏝️ ¡Paradise Garden Egg detectado!")
        await message.add_reaction("🌴")
        await enviar_dm(message.author, "🏝️ ¡PARADISE GARDEN EGG DETECTADO!")

    # 🍭 Sugar Apple Seed
    elif "sugar apple seed" in contenido and puede_responder("sugar apple"):
        await message.channel.send("🍭 ¡Sugar Apple Seed detectada!")
        await message.add_reaction("🍎")
        await enviar_dm(message.author, "🍭 ¡SUGAR APPLE SEED DETECTADA!")

    # 🔥 Burning Bud Seed
    elif "burning bud seed" in contenido and puede_responder("burning bud"):
        await message.channel.send("🔥 ¡Burning Bud Seed detectada!")
        await message.add_reaction("🌶️")
        await enviar_dm(message.author, "🔥 ¡BURNING BUD SEED DETECTADA!")

    await bot.process_commands(message)

# ✉️ Función para enviar mensaje privado con @mención
async def enviar_dm(usuario, texto):
    try:
        await usuario.send(f"{usuario.mention} {texto}")
        print(f"📩 DM enviado a {usuario.name}: {texto}")
    except Exception as e:
        print(f"❌ No se pudo enviar DM a {usuario.name}: {e}")

# 👇 Token (tu mismo de antes)
bot.run("MTM5MjI1NDQxMjQ1MzMxNDc2MA.GrbGQP.RDxvwlVzrdR543baJo0JnCFUOA6wubexOWkdC4")
