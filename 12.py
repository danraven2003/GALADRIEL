import discord
import requests
import os
import asyncio
from discord.ext import commands
def s():
    global m
    m.clear()
    f = open(r'baza.txt', encoding='utf-8')
    n = f.readlines()
    f.close()
    n = [i.rstrip() for i in n]
    m = [i.split('/') for i in n]
    for i in m:
        i[1], i[2] = int(i[1]), int(i[2])
def so():
    global m
    s()
    m = sorted(m, key = lambda i: i[2], reverse = False)

def fur(user_message):
    global ni
    ni.clear()
    ni.append(user_message)
    ni = ni[0].split()
    for i in ni:
        if '/' in i:
            ni = []
            break
m = []
ni = []
h = [['Сейчас будет список команд и что они означают'],
     ['/vyvod Данной командой можно вывести список товаров'],
     ['/nygno Данной командой можно занести в список товар, который необходимо купить'],
     ['/kyplu Данной командой можно выбрать товар из списка, который вы купите, тем самым удалите товар из списка'],
     ['/titry Над ботом работали:']]
k = ['Товарищ, введите следующим образом, что вы приобритаете: сначала укажите <наименование товара>, который вы собираетесь купить, далее укажите <количество> приобритаемого товара']
n = ['Товарищ, введите следующим образом, что вам необходимо купить: сначала укажите <наименование товара>, затем - <нужное количество>, далее - критерий срочности <от 1 до 3>, где 1 это срочно']
tit = [['Програмист и разработчик:'],
       ['Равенский Даниил Денисович'],
       ['Идея:'],
       ['Леонтьева Елена Андреевна'],
       ['Автор и редакторы текста:'],
       ['Равенский Даниил Денисович'],
       ['Равенская Оксана Алексеевна'],
       ['Тестировщики:'],
       ['Равенский Даниил Денисович'],
       ['Равенская Оксана Алексеевна']]
TOKEN = "MTExNzE0MDY0MjUyNzcxMTM5Mw.G0EJrA.HgvE4zD9zZ5LC9UcAXUpNjv9Q9Lv_52-T_VEBo"
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents = intents)
@bot.command()
async def load(ctx, extension):
    extension =extension.lower()
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} загружен')
@bot.command()
async def unload(ctx, extension):
    extension =extension.lower()
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} выгружен')
@bot.event
async def on_ready():
    for guild in bot.guilds:
        category = guild.categories[0]
        channel = category.channels[0]
        await channel.send('Добро пожаловать, друзья, хотите узнать больше - пишите (/pomogi)')
@bot.command(name='pomogi')
async def pomogi(ctx):
    global h
    for i in h:
        await ctx.send(*i)
@bot.command(name='vyvod')
async def vyvod(ctx):
    global m
    await ctx.send('Товарищ, благодарим, что вы интересуетесь нуждами общества')
    so()
    for i in m:
        if i[2] == 1:
            i[2] = 'СРОЧНО'
        elif i[2] == 2:
            i[2] = 'средне'
        elif i[2] == 3:
            i[2] = 'в планах'
    m = [[str(i[2]) + ' ' + str(i[0]) + ' ' + str (i[1])] for i in m]
    for i in m:
        await ctx.send(*i)
@bot.command(name='nygno')
async def nygno(ctx):
    s()
    global ni, m
    flag = False
    await ctx.send(*n)
    try:
        message = await bot.wait_for('message', timeout=100.0, check=lambda x: x.author == ctx.author and x.channel == ctx.channel)
        fur(message.content)
        if len(ni) == 3:
            a = ni[0].lower()
            b = ni[1]
            c = ni[2]
            if (b.isdigit() == False) or (c.isdigit() == False):
                await ctx.send('Товарищ, введено неверное значение')
            else:
                if ((int(b) > 0) and ((int(c) == 1) or (int(c) == 2) or (int(c) == 3))):
                    await ctx.send('Товарищ, благодарим, что вы сообщили, в чём вы нуждаетесь')
                    for i in range(len(m)):
                        if m[i][0] == a:
                            flag = True
                            t = i
                            break
                        else:
                            flag = False
                    if flag == False:
                        f = open(r'baza.txt', 'a+', encoding='utf-8')
                        f.write(a + '/' +
                            b + '/' +
                            c + '\n')
                        f.close()
                    else:
                        m[t][1] += int(b)
                        m = [str(i[0])+'/'+str(i[1])+'/'+str(i[2])+'\n' for i in m]
                        f = open(r'baza.txt', 'w', encoding='utf-8')
                        for i in m:
                            f.write(i)
                        f.close()
                else:
                    await ctx.send('Товарищ, введено неверное значение')
        else:
            await ctx.send('Товарищ, введено неверное значение')
    except asyncio.TimeoutError:
        await ctx.send("Товарищ, ваше время истекло")
@bot.command(name='kyplu')
async def kyplu(ctx):
    s()
    global ni, m
    flag = False
    await ctx.send(*k)
    try:
        message = await bot.wait_for('message', timeout=100.0, check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
        fur(message.content)
        if len(ni) == 2:
            a = ni[0].lower()
            b = ni[1]
            if (b.isdigit() == False):
                await ctx.send('Товарищ, введено не верное значение')
            elif (int(b) <= 0):
                await ctx.send('Товарищ, вы очень хитрый, за вами выехал наряд')
            else:
                b = int(b)
                for i in range(len(m)):
                    if m[i][0] == a:
                        flag = True
                        t = i
                        break
                    else:
                        flag = False
                if flag == True:
                    m[t][1] -= b
                    if m[t][1] <= 0:
                        del m[t]
                        m = [str(i[0])+'/'+str(i[1])+'/'+str(i[2])+'\n' for i in m]
                        f = open(r'baza.txt', 'w', encoding='utf-8')
                        for i in m:
                            f.write(i)
                        f.close()
                    else:
                        m = [str(i[0])+'/'+str(i[1])+'/'+str(i[2])+'\n' for i in m]
                        f = open(r'baza.txt', 'w', encoding='utf-8')
                        for i in m:
                            f.write(i)
                        f.close()
                    await ctx.send('Товарищ, верной дорогой идете, вы, достойны назывваться СТРОИТЕЛЕМ КОММУНИЗМА')
                else:
                    await ctx.send('Товарищ, выбранного наименования не существует')
    except asyncio.TimeoutError:
        await ctx.send("Товарищ, ваше время истекло")
@bot.command(name='titry')
async def titry(ctx):
    global tit
    for i in tit:
        await ctx.send(*i)
bot.run(TOKEN)
