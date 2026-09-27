import discord
from claves import CLAVE_IA, TOKEN 
from ollama import chat 
from discord.ext import commands
from google import genai

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def saludo (ctx):
    await ctx.send("Hola, bienvenido a mi servidor de discord!")

@bot.command()
async def suma(ctx, num1:float, num2:float):
    resultado = num1 + num2
    await ctx.send(f"el resultado de la suma es: {resultado}")

@bot.command()
async def resta(ctx, num1:float, num2:float):
    resultado = num1 - num2
    await ctx.send(f"el resultado de la resta es: {resultado}")

@bot.command()
async def división(ctx, num1:float, num2:float):
    if num2 == 0:
        await ctx.send("No podemos dividir por cero")
    else:
        resultado = num1 / num2
        await ctx.send(f"el resultado de la división es: {resultado}")


@bot.command()
async def multiplicación(ctx, num1:float, num2:float):
    resultado = num1 * num2
    await ctx.send(f"el resultado de la multiplicación es: {resultado}")

@bot.command()
async def ia(ctx,*,pregunta):
    client = genai.Client(api_key=CLAVE_IA)

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=pregunta
    )
    await ctx.send(interaction.output_text)

@bot.command()
async def guardar(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{file_name}")
            await ctx.send(f"Guarde el archivo {file_name} en {file_url}")
    else:
        await ctx.send("No me enviaste un archivo para guardar!")

@bot.command()
async def analizar(ctx, nombre):
    if nombre == "arana_prueba.jpg":
        await ctx.send("la imagen que me enviaste es la de una araña!")


bot.run(TOKEN)
