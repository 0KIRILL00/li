import random
import discord
import os

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.command()
async def mem(ctx):
    lst = os.listdir('image')
    rand_img = random.choice(lst)
    with open('image/' + rand_img, 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
@bot.command()
async def proof(ctx):
    await ctx.send(f'''На нашей планете все живые существа обитают в тесной взаимосвязи друг с другом и окружающим миром.
В природе все гармонично и взаимосвязано: растения получают питательные вещества из почвы, животным необходима растительная пища, а человеку нужны и пища, и ресурсы.
И если это равновесие в природе нарушается, то сразу же возникает экологический кризис.
Вот всеми этими проблемами и занимается экология.
Экология – это такая наука, которая изучает живые организмы и среду их обитания. 
В современном мире люди не всегда живут в гармонии с природой, и это может стать толчком к нарушению равновесия живых организмов и природы. 
Поэтому очень важно, чтобы школьники понимали взаимосвязь человека и природы, и предвидели, какие могут произойти изменения под воздействием человека. 
И если экология пострадала, то человек должен знать, что можно предпринять для устранения экологической катастрофы. 
Вот поэтому экология является нужной и важной наукой, которую необходимо изучать с ранних лет.''')
@bot.command()
async def prooff(ctx):
    await ctx.send('https://greentruth.ru/ecology/ob-ekologii/dlya-chego-nuzhna-ekologiya/?ysclid=lnhbffkwll508719532')
    
bot.run("")

bot.run('')
