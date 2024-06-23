import discord
from discord.ext import commands

permissao = discord.Intents.default()
permissao.message_content = True  # permite que o bot ler as mensagens
permissao.members = True

bot = commands.Bot(command_prefix="!", intents=permissao)

@bot.command()  # comandos para o discord
async def ola(ctx: commands.Context):
    usuario = ctx.author
    servidor = ctx.guild
    await ctx.reply(f"Olá!, {usuario.display_name}\n Você está no canal: {servidor.name}")

@bot.command()
async def falar(ctx: commands.Context, *, frase):  # *, ler a frase completa
    await ctx.send(frase)

@bot.command()
async def enviar_embed(ctx: commands.Context):
    meu_embed = discord.Embed(title='Olá, Mundo!', description='Descrição :D')
    await ctx.reply(embed=meu_embed)

@bot.event
async def on_ready():
    print("Estou pronto!")

@bot.event
async def on_guild_channel_create(canal: discord.abc.GuildChannel):  # aciona quando um canal é criado
    await canal.send(f"Novo canal criado: {canal.name}")

@bot.event
async def on_member_join(membro: discord.Member):  # dispara mensagem de boas vindas
    canal = bot.get_channel(1254233450073030707)  # id especifico do canal de boas vindas
    await canal.send(f"{membro.display_name} Entrou no servidor!\nSeja bem vindos(as)!")

@bot.event
async def on_member_remove(menbro: discord.Member):  # dispara ao sair do servidor
    canal = bot.get_channel(1254233450073030707)
    await canal.send(f"{menbro.display_name} Saiu do servidor...\n Até breve!")

bot.run('SEU TOKEN')
