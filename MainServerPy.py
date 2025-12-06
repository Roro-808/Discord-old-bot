from datetime import datetime, timedelta
import discord
from typing import List
# from discord import Embed
from discord.ext import commands
import random
import asyncio
#points
import json
import os
from dotenv import load_dotenv

SCORES_FILE = 'scores.json'
ToolsFile = 'tools.json'
waiter_FILE = "wait_data.json"
SettingsFILE = 'settings.json'
InventoryFILE = 'inventory.json'


import pytz

timezone = pytz.timezone("Europe/Moscow")
start_date = datetime(1970, 1, 1, 3, 0, 0, tzinfo=pytz.UTC)

"""
now = datetime.now(timezone)                                            
timer_secsafter1970 = int((now - start_date).total_seconds()) + (3600*3)
f"<t:{timer_secsafter1970}:R>"


снизу старый
NOW_time_Day_HMS = now.strftime("%d.%m,%H:%M:%S")
"""

def inventory_load():
    if os.path.exists(InventoryFILE):
        with open(InventoryFILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def inventory_save(invent):
    with open(InventoryFILE, 'w', encoding='utf-8') as f:
        json.dump(invent, f, ensure_ascii=False, indent=4)



def settings_load():
    if os.path.exists(SettingsFILE):
        with open(SettingsFILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def settings_save(setts):
    with open(SettingsFILE, 'w', encoding='utf-8') as f:
        json.dump(setts, f, ensure_ascii=False, indent=4)



# Загрузка данных очков
def load_scores():
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}
# Сохранение данных очков
def save_scores(scores):
    with open(SCORES_FILE, 'w', encoding='utf-8') as f:
        json.dump(scores, f, ensure_ascii=False, indent=4)
# Загрузка данных предметов
def load_data():
    if os.path.exists(ToolsFile):
        with open(ToolsFile, 'r', encoding='utf+8') as f:
            return json.load(f)
    return {}

def save_data(qut):
    with open(ToolsFile, 'w', encoding='utf-8') as f:
        json.dump(qut, f, ensure_ascii=False, indent=4)

def load_timedata():
    if os.path.exists(waiter_FILE):
        with open(waiter_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

# Сохраняем данные в файл
def save_timedata(data):
    with open(waiter_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)










intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents, case_insensitive=True)



ALLOWED_CHANNEL_ID1 = [1209537208667738122, 1208840643737157633, 1206603858176905237, 1205941408742121472] #Нон-РП
ALLOWED_CHANNEL_ID2 = [1208338093648904282, 1207962871326187520] # тикеты + модерация (команды)
ALLOWED_CHANEL_ID3 = [1205941408742121472, 1338526927924756560, 1338527100604256257, 1207962871326187520] #Команды
MOD_COMMANDS = 1207962871326187520 #команды-модерации -- канал
ROLE_REGISTERED = 1337758563086368779 #Зарегестрирован
Registration_Items_CHANNEL_ID = 1342805713906434178
C_INFO = 1207966485243498507 #общие-процессы
C_I_INFO = 1207966738520743976 #особо-важные-процессы
C_MON_INFO = 1205928689590603826 #денежные-процессы
ROLE_MODERATOR = 1208838193919688714 # ?
ROLE_TICKETS_PERMISSION = 1210291933658746921 # тикет-хелпер
ROLE_HELPER_OR_HIGHER = 1208713089650921482 # хелпер+
ROLE_MODERATOR_OR_HIGHER = 1208783844967317624 # Модер+
VIP_user = 1210246875660296233 # Вип
ALLOWED_CHANGE_SETTINGS_ROLES = [1337710547751141407, 1210250378629746749, 1338533687305834518, 1210246417755672698] #создатель, разработчик, главный админ, владелец (ПОРЯДОК НЕВЕРНЫЙ)
Role_TESTER = 1342534294538686544 # Tester
Role_high_administr = 1213160833572409396 # старшая модерация
Role_Unregistered = 1207965677705629716 # Незарегестрирован
Country_Role_RP = 1353374447134052487 # Страна



# experiment



Err001 = "Эта команда недоступна в этом канале!"
Err020 = 'У вас недостаточно прав, чтобы пользоваться данной командой'
Err100 = "Время ожидания истекло. Попробуйте снова."
Err200 = 'Ошибка при заполнении данных! Попробуйте снова.'
Err300_1 = 'Вы ещё не зарегестрированы!'
Err301 = 'У вас нет показателя очков'
Err301_1 = 'Ни у кого нет показателей очков!'
Err301_2 = 'У пользователя нет показателя очков!'
Err302 = 'У вас не хватает очков!'
Err303 = 'У вас уже есть показатель очков'
Err304 = 'У вас нет роли для получения денег'
Err304_modification1 = 'У вас есть роль заработка, но нет ролей экономики!' # unused
Err305 = 'У вас присутствует 2 или более ролей экономики одновременно!'

Err404_1 = 'Роль не найдена!'
Err404_2 = 'Канал не найден!'
Err404_3 = "Пользователь не найден!"
Err404_4 = 'Предмет не найден!'

Err500 = 'Вайп ещё не начался!'
Err501 = 'Вы не являетесь страной!'

Err600 = 'Сетевая ошибка (HTTPException)'

ErrNONacess = 'У бота нет привелегий на данное действие!'

# Pages experimental
class Paginator(discord.ui.View):
    def __init__(self, embeds: List[discord.Embed]):
        super().__init__(timeout=60)
        self.embeds = embeds
        self.current_page = 0
        self.message = None

        self.update_buttons()

    def update_buttons(self):

        self.prev_page.disabled = self.current_page == 0
        self.next_page.disabled = self.current_page == len(self.embeds) - 1

    @discord.ui.button(label="◀", style=discord.ButtonStyle.blurple)
    async def prev_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_page -= 1
        self.update_buttons()
        await interaction.response.edit_message(
            embed=self.embeds[self.current_page],
            view=self
        )

    @discord.ui.button(label="▶", style=discord.ButtonStyle.blurple)
    async def next_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_page += 1
        self.update_buttons()
        await interaction.response.edit_message(
            embed=self.embeds[self.current_page],
            view=self
        )

    @discord.ui.button(label="❌", style=discord.ButtonStyle.red)
    async def stop_pages(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await interaction.delete_original_response()
        self.stop()

    async def on_timeout(self):
        for item in self.children:
            item.disabled = True
        if self.message:
            try:
                await self.message.edit(view=self)
            except discord.NotFound:
                pass



#Обработчик ошибок, проверка данных и т.д.
'''
@bot.event
async def on_command_error(ctx, error):
    # Игнорируем команды без ошибок
    if hasattr(ctx.command, 'on_error'):
        return

    # Пропускаем ошибки от других обработчиков
    if isinstance(error, (commands.CommandNotFound, commands.UserInputError)):
        return

    # Основные типы ошибок
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Не хватает аргумента: `{ctx.prefix}{ctx.command.name} <{error.param.name}>`")

    elif isinstance(error, commands.BadArgument):
        await ctx.send("Неверный формат аргумента")

    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(Err404_3)

    elif isinstance(error, commands.CheckFailure):
        await ctx.send(Err020)
    else:
        print(f"\nОшибка в {ctx.command.name}: v {type(error)} - {error}\n")
        await ctx.send(f"{Err000} {type(error)} - {error}")
'''

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Выключаюсь...")
    print(f'END, reason: shutdown command at {datetime.now(timezone).strftime("%d.%m,%H:%M:%S")}')
    await bot.get_channel(C_INFO).send(f'END, reason: shutdown command at {datetime.now(timezone).strftime("%d.%m,%H:%M:%S")}')
    await bot.close()

@bot.command(name='settings', help="Изменяет настройки бота")
async def Settings(ctx, settname:str=False, value:str=False):
    if not settname:
        await ctx.send("Не указан параметр!", delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    # settings
    datya = load_data()
    settings = settings_load()
    audit = bot.get_channel(C_I_INFO)
    now = datetime.now(timezone)
    timer_secsafter1970 = int((now - start_date).total_seconds()) + (3600 * 3)
    points = load_scores()
    time_data = load_timedata()
    # settings

    if not [role.id == ALLOWED_CHANGE_SETTINGS_ROLES for role in ctx.author.roles]:
        await ctx.send(Err020, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    if ctx.channel.id != MOD_COMMANDS:
        await ctx.send(Err001, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return

    '''
    settname 0 - доход за сбои в системе
    settname 1 - 
    
    '''

    try:
        if int(settname) == 0:
            if not value:
                await ctx.send("Не указано значение!", delete_after=5)
                await asyncio.sleep(5)
                await ctx.message.delete()
                return
            try:
                float(value)
            except ValueError:
                if value.upper() == 'FALSE':
                    value = False
                else:
                    await ctx.send(Err200, delete_after=5)
                    await asyncio.sleep(5)
                    await ctx.message.delete()
                    return
            if settings["errOcr"] == 0 and value:
                settings["errOcr"] = float(value)
                settings["errOcr"] = float(value)
                await ctx.send(f'На сервере установлен увеличенный доход за сбой в системе. Доход увеличен на {round((float(value)-1)*100)}%')
                await audit.send(f'На сервере установлен увеличенный доход за сбой в системе. Доход увеличен на {round((float(value)-1)*100)}% пользователем {ctx.author.mention}.\n`{ctx.message.content}`\n{ctx.channel.mention}\n<t:{timer_secsafter1970}:R>')
            elif not value:
                settings["errOcr"] = 0
                await ctx.send('Доход за сбой отменён.')
                await audit.send(f'Доход за сбой в программе отменён пользователем {ctx.author.mention}.\n`{ctx.message.content}`\n{ctx.channel.mention}\n<t:{timer_secsafter1970}:R>')
        elif int(settname) == 1:
            ifcancel = False
            administr = ctx.guild.get_role(Role_high_administr)
            if settings['vp'] == 1:
                await ctx.send("Вы уверены что хотите сбросить игру?\nДля подтверждения подождите 1 минуту.")
                await audit.send(f'{ctx.author.mention} собирается окончить сезон в канале {ctx.channel.mention}.\nЧтобы предотвратить процесс, напишите "ОТМЕНА" в этом канале.')

                def check1(message):
                    return message.content.upper() == "FALSE" or message.content.upper() == 'ОТМЕНА' and administr in message.author.roles and audit
                try:
                    await bot.wait_for("message", check=check1, timeout=5)
                    ifcancel = True
                    await ctx.send('Отмена в канале аудита.')

                except asyncio.TimeoutError:
                    pass

                if not ifcancel:
                    await ctx.send('Ожидание 60 секунд прошло. Напишите "начать", если готовы начать вайп.')
                    asafafas = bot.get_channel(MOD_COMMANDS)
                    def check2(message):
                        return message.content.upper() == "TRUE" or message.content.upper() == 'НАЧАТЬ' and message.author == ctx.author and asafafas
                    try:
                        await bot.wait_for("message", check=check2, timeout=20)
                        await audit.send(f'{ctx.author.mention} начал процесс вайпа.')
                        settings['vp'] = 0
                        time_data={}
                        points={}

                        # removing roles

                        unregistered = ctx.guild.get_role(Role_Unregistered)
                        test_role = ctx.guild.get_role(Role_TESTER)
                        all_roles = [1210487981408780389, 1210488156718374932, 1352530035072041040, 1213896862575108126, 1213571689653342338, 1213571528961298532, 1213571025430909038, 1213570823130980362, 1206105082135838720, 1206104847947010078, 1213563532512067704, 1210486220505743381, 1213563532512067704, 1210486220505743381, 1337758563086368779]
                        reg = ctx.guild.get_role(ROLE_REGISTERED)

                        remove_roles = [reg] + [ctx.guild.get_role(i) for i in all_roles]
                        for member in ctx.guild.members:
                            if reg in member.roles and test_role not in member.roles:
                                try:
                                    await member.remove_roles(*remove_roles, reason="Сезон окончен.")
                                    await member.add_roles(unregistered, reason="Сезон окончен.")
                                except discord.Forbidden:
                                    await ctx.send(f"{ErrNONacess}. Нет прав для снятия ролей у {member.name}")
                                    print(f"{ErrNONacess}. Нет прав для снятия ролей у {member.name}")
                                except discord.HTTPException as e:
                                    await ctx.send(f"{Err600}. Ошибка при снятии ролей у {member.name}: {e}")
                                    print(f"{Err600}. Ошибка при снятии ролей у {member.name}: {e}")
                        for d in datya:
                            if d[10]:
                                try:
                                    del datya[d]
                                except KeyError:
                                    await ctx.send(f'Не удалось сбросить {d} в предметах.')
                        await ctx.send("Успешно сброшен!")
                        await audit.send('Успешно сброшен!')
                    except asyncio.TimeoutError:
                        await ctx.send(Err100, delete_after=5)
                        await asyncio.sleep(5)
                        await ctx.message.delete()
                        return
                else:
                    return

            elif settings['vp'] == 0:
                await ctx.send('На доработке!')
                await ctx.send('Начать новый сезон? Для подтверждени подождите 1 минуту.')
                await audit.send(f'{ctx.author.mention} собирается начать сезон в канале {ctx.channel.mention}.\nЧтобы предотвратить процесс, напишите "отмена" в этом канале.')

            else:
                await ctx.send(f'Неизвестная ошибка! Vp = {settings['vp']}', delete_after=5)
                await asyncio.sleep(5)
                await ctx.message.delete()
                return


        else: # Остальные с elif
            await ctx.send('Такое значение не существует', delete_after=5)
            await asyncio.sleep(5)
            await ctx.message.delete()
            return
    except ValueError:
        await ctx.send(Err200, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    save_timedata(time_data)
    save_scores(points)
    settings_save(settings)
    save_data(datya)







# EXPERIMENTAL
@bot.command(name='добавить', help="Добавляет предмет")
async def добавить(ctx, имя: str = False):
    if not имя:
        await ctx.send("Не указано имя предмета!!", delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return

    sts = settings_load()

    rtest = ctx.guild.get_role(Role_TESTER)
    if ctx.guild.get_role(1210999471937429554) not in ctx.author.roles:
        await ctx.send(Err020, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    if ctx.channel.id != MOD_COMMANDS:
        await ctx.send(Err001, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    if sts["vp"] == 0 and rtest not in ctx.author.roles:
        await ctx.send(Err500, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    data = load_data()
    if data.get(имя) is not None:
        await ctx.send('Такое значение уже существует', delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    print(data)
    await ctx.send("Теперь добавьте описание.")
    def check(mess_used0):
        return mess_used0.author == ctx.author and mess_used0.channel == ctx.channel
    try:
        mess_used = await bot.wait_for("message", timeout=150.0, check=check)
        message1 = mess_used.content
    except TimeoutError:
        await ctx.send(Err100, delete_after=5)
        return
    await ctx.send("Какая должна быть цена? Укажите 'skip' или 'none', если товар бесплатный.")
    try:
        mess_used = await bot.wait_for("message", timeout=30.0, check=check)
        message2 = mess_used.content
        if message2.upper() == 'FALSE' or message2.upper() == 'NONE' or message2.upper() == 'SKIP':
            message2 = False
        else:
            try:
                message2 = int(message2)
            except ValueError:
                await ctx.send(Err200, delete_after=5)
                return
    except TimeoutError:
        await ctx.send(Err100, delete_after=5)
        return
    await ctx.send("Какая роль необходима для получения предмета? Укажите 'skip' или 'none', если некакая.")
    try:
        mess_used = await bot.wait_for("message", timeout=30.0, check=check)
        message3 = mess_used.content
        if message3.upper() == 'FALSE' or message3.upper() == 'NONE' or message3.upper() == 'SKIP':
            message3 = False
        else:
            message3 = mess_used.role_mentions
            if not message3:
                await ctx.send(Err200, delete_after=5)
                return
            message3 = [role.id for role in message3]
    except TimeoutError:
        await ctx.send(Err100, delete_after=5)
        return
    await ctx.send("Сколько раз один пользователь сможет приобрести предмет? Укажите 'skip' или 'none', если неогранниченное кол-во")
    try:
        mess_used = await bot.wait_for("message", timeout=30.0, check=check)
        message4 = mess_used.content
        if message4.upper() == 'FALSE' or message4.upper() == 'NONE' or message4.upper() == 'SKIP':
            message4 = False
        else:
            try:
                message2 = int(message2)
            except ValueError:
                await ctx.send(Err200, delete_after=5)
                return
    except TimeoutError:
        await ctx.send(Err100, delete_after=5)
        return
    await ctx.send("Какая роль будет выдана после приобретения предмета? Укажите 'skip' или 'none', если никакая.")
    try:
        mess_used = await bot.wait_for("message", timeout=30.0, check=check)
        message5 = mess_used.content
        if message5.upper() == 'FALSE' or message5.upper() == 'NONE' or message5.upper() == 'SKIP':
            message5 = False
        else:
            message5 = mess_used.role_mentions
            if not message5:
                await ctx.send(Err200, delete_after=5)
                return
            message5 = [i.id for i in message5]
    except TimeoutError:
        await ctx.send(Err100, delete_after=5)
        return
    await ctx.send("Какую роль необходимо будет удалить после получения предмета? Укажите 'skip' или 'none', если никакую.")
    try:
        mess_used = await bot.wait_for("message", timeout=30.0, check=check)
        message6 = mess_used.content
        if message6.upper() == 'FALSE' or message6.upper() == 'NONE' or message6.upper() == 'SKIP':
            message6 = False
        else:
            message6 = mess_used.role_mentions
            if not message6:
                await ctx.send(Err200, delete_after=5)
                return
            message6 = [i.id for i in message6]
    except TimeoutError:
        await ctx.send(Err100, delete_after=5)
        return
    await ctx.send("Будет ли предмет показываться при использовании команды !shop? Укажите 'skip' или 'none', если не будет, укажите 'true', если будет.")
    try:
        mess_used = await bot.wait_for("message", timeout=30.0, check=check)
        message7 = mess_used.content
        if message7.upper() == 'FALSE' or message7.upper() == 'NONE' or message7.upper() == 'SKIP':
            message7 = False
        elif message7.upper() == 'TRUE':
            message7 = True
        else:
            await ctx.send(Err200, delete_after=5)
            return
    except TimeoutError:
        await ctx.send(Err100, delete_after=5)
        return
    await ctx.send("Будет ли предмет уничтожен сразу после покупки? Укажите 'skip' или 'none', если не будет.")
    try:
        mess_used = await bot.wait_for("message", timeout=30.0, check=check)
        message8 = mess_used.content
        if message8.upper() == 'FALSE' or message8.upper() == 'NONE' or message8.upper() == 'SKIP':
            message8 = False
        elif message8.upper() == 'TRUE':
            message8 = True
        else:
            await ctx.send(Err200, delete_after=3)
            return
    except TimeoutError:
        await ctx.send(Err100, delete_after=3)
        return
    await ctx.send("Можно ли будет использовать предмет командой !use? Укажите 'skip' или 'none', если нельзя. Укажите 'true', если можно")
    try:
        mess_used = await bot.wait_for("message", timeout=30.0, check=check)
        message9 = mess_used.content
        if message9.upper() == 'FALSE' or message9.upper() == 'NONE' or message9.upper() == 'SKIP':
            message9 = False
        elif message9.upper() == 'TRUE':
            message9 = True
        else:
            await ctx.send(Err200, delete_after=3)
            return
    except TimeoutError:
        await ctx.send(Err100, delete_after=5)
        return
    moder_or_higher = ctx.guild.get_role(ROLE_MODERATOR_OR_HIGHER)
    if moder_or_higher in ctx.author.roles:
        try:
            await ctx.send("Будет ли предмет удалён после вайпа?")
            mess_used = await bot.wait_for("message", timeout=30.0, check=check)
            message10 = mess_used.content
            if message10.upper() == 'FALSE' or message10.upper() == 'NONE' or message10.upper() == 'SKIP':
                message10 = False
            elif message10.upper() == 'TRUE':
                message10 = True
            else:
                await ctx.send(Err200, delete_after=3)
                return
        except TimeoutError:
            await ctx.send(Err100, delete_after=5)
            return
    else:
        message10 = True
    spisochek = [ctx.author.id, message1, message2, message3, message4, message5, message6, message7, message8, message9, message10]
    await ctx.send(spisochek)
    data[имя] = spisochek
    await ctx.send(f"Данные для '{имя}' успешно добавлены.")
    save_data(data)


@bot.command(name="shop", aliases=["Магазин", "Магаз"])
async def shop(ctx):
    sts = settings_load()
    rtest = ctx.guild.get_role(Role_TESTER)
    if sts["vp"] == 0 and rtest not in ctx.author.roles:
        await ctx.send(Err500, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return

    embed1 = discord.Embed(
        title="МАГАЗИН",  # Заголовок
        description="Магазин товаров.",  # Описание
        color=0x32cd32
    )


    Fill = []
    data = load_data()
    for i in data:
        """                     data[i]  --  [num]
        id автора                              0
        Описание                               1
        Цена | false - бесплатно               2
        Роль для покупки                       3
        Сколько раз можно использовать         4
        Получить роль после покупки            5
        Удалить роль после покупки             6
        Показать командой !shop                7
        Будет ли уничтожен после покупки       8
        Использование командой !use            9
        Будет ли уничтожен после вайпа         10
        Тип                                    11
        """
        if data[i][7]:
            Fill.append(i)
            if not data[i][2]:
                m_txt = 'Бесплатно'
            else:
                m_txt = f"{str(data[i][2])}:money_with_wings:"
            if data[i][11] == 'basic':
                type_txt = ''
            elif data[i][11] == 'common':
                type_txt = '\n-# Товар'
            elif data[i][11] == 'army':
                type_txt = f'\n-# Военный товар - {data[i][12][1]}'
            elif data[i][11] == 'agreement':
                type_txt = '\n-# Договор'
            embed1.add_field(name=f'{i} - {m_txt}', value=f"{data[i][1]}{type_txt}", inline=False)

    if not Fill:
        await ctx.send('Магазин пуст!')
    else:
        await ctx.send(embed=embed1)


@bot.command(name="buy", aliases=["купить", "приобрести"])
async def buy(ctx, item:str = False, val:str = False):
    if not item:
        await ctx.send("Не указан предмет!", delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    if not val:
        await ctx.send("Не указано кол-во!", delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    tools = load_data()
    invent = inventory_load()
    mon = load_scores()
    try:
        val = int(val)
        if val < 1:
            await ctx.send(Err200, delete_after=5)
            await asyncio.sleep(5)
            await ctx.message.delete()
            return
    except ValueError:
        await ctx.send(Err200, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    if item.upper() not in [i.upper() for i in tools]:
        await ctx.send(Err404_4, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    else:
        for i in tools:
            if item.upper() == i.upper():
                item = i
    if ctx.author.id in invent.keys():
        if item.upper() in [i.upper() for i in invent[ctx.author.id]]:
            returningVal = invent[ctx.author.id][item]
        else:
            returningVal = 0
    else: returningVal = 0
    if (returningVal + val) > tools[item][4]:
        del returningVal
        await ctx.send(f'Этот предмет можно приобрести только {tools[item][4]} раз!', delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    if tools[item][3]:
        missing_roles = [role.name for role in [ctx.guild.get_role(i) for i in tools[item][3]] if role not in ctx.author.roles]
        if missing_roles:
            await ctx.send(f'Необходима роль(-и): {', '.join(missing_roles)}', delete_after=5)
            await asyncio.sleep(5)
            await ctx.message.delete()
            return
    am_mon = val * tools[item][2]

    if str(ctx.author.id) not in mon.keys():
        await ctx.send(Err301, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    def check(mess_used0):
        return mess_used0.author == ctx.author and mess_used0.channel == ctx.channel
    try:
        await ctx.send(f"Вы уверены, что хотите купить {item} в кол-ве {val} за {am_mon}? Укажите да, если хотите.")
        mess_used = await bot.wait_for("message", timeout=15.0, check=check)
        if mess_used.content.upper() == "ДА" or mess_used.content.upper() == "TRUE":
            mon[str(ctx.author.id)] -= am_mon
            if str(ctx.author.id) not in invent.keys():
                invent[str(ctx.author.id)] = {item: val}
                await ctx.send("Создан инвентарь с предметами.")
            elif item not in invent[str(ctx.author.id)].keys():
                invent[str(ctx.author.id)][item] = val
            else:
                invent[str(ctx.author.id)][item] += val
            await ctx.send("Покупка успешно совершена!")
    except TimeoutError:
        await ctx.send(Err100, delete_after=5)
        return
    inventory_save(invent)
    save_scores(mon)
    save_data(tools)











# points part
@bot.command(name="баланс", aliases=["кошелёк", 'банк', "казна"], help="Проверяет баланс")
async def баланс(ctx):
    scores = load_scores()
    user_id = str(ctx.author.id)
    sts = settings_load()
    rtest = ctx.guild.get_role(Role_TESTER)
    if sts["vp"] == 0 and rtest not in ctx.author.roles:
        await ctx.send(Err500, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    if ctx.channel.id not in ALLOWED_CHANEL_ID3:
        await ctx.send(Err001, delete_after=5)
        await asyncio.sleep(3)
        await ctx.message.delete()
        return
    if user_id in scores:
        await ctx.send(f"У вас {scores[user_id]} очков.")
    else:
        await ctx.send(Err301, delete_after=5)
        await asyncio.sleep(3)
        await ctx.message.delete()

@bot.command()
async def сброситьочки(ctx, user: discord.Member = False):
    if not user:
        await ctx.send("Не указан пользователь!", delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    scores = load_scores()
    ROLE_MODER_OR_HIGHER1 = ctx.guild.get_role(ROLE_HELPER_OR_HIGHER)
    Moneyinfo = bot.get_channel(C_MON_INFO)
    try:
        user_id = str(user.id)
    except Exception as e:
        await ctx.send(f"Ошибка! {e}", delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    sts = settings_load()
    rtest = ctx.guild.get_role(Role_TESTER)
    if sts["vp"] == 0 and rtest not in ctx.author.roles:
        await ctx.send(Err500, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    if ctx.channel.id not in ALLOWED_CHANEL_ID3:
        await ctx.send(Err001, delete_after=3)
        await asyncio.sleep(3)
        await ctx.message.delete()
        return
    elif ROLE_MODER_OR_HIGHER1 not in ctx.author.roles:
        await ctx.send(Err020, delete_after=3)
        await asyncio.sleep(3)
        await ctx.message.delete()
    if user_id in scores:
        del scores[user_id]
        save_scores(scores)
        await ctx.send(f"Очки пользователя {user.mention} сброшены.")
        await Moneyinfo.send(f"Очки пользователя {user.mention} сброшены.")
    else:
        await ctx.send(Err301_2, delete_after=3)
        await asyncio.sleep(3)
        await ctx.message.delete()





@bot.command(name="collect", aliases=["сбор", 'налог', "получить_деньги", "получитьденьги", "прибыль"])
async def collect(ctx):
    # РОЛИ ДОБЫЧИ

    Disabled_economyRProle = ctx.guild.get_role(1206104847947010078)
    TerribleEconomyRProle = ctx.guild.get_role(1206105082135838720)
    GrowingEconomyRProle = ctx.guild.get_role(1213570823130980362)
    BasicEconomyRProle = ctx.guild.get_role(1213571025430909038)
    GoodEconomyRProle = ctx.guild.get_role(1213571528961298532)
    AmazingEconomyRProle = ctx.guild.get_role(1213571689653342338)
    PerfectEconomyRProle = ctx.guild.get_role(1213896862575108126)
    VIProle = ctx.guild.get_role(VIP_user)
    # РОЛИ ДОБЫЧИ

    # ДРУГОЕ
    settings = settings_load()
    data = load_timedata()
    save_timedata(data)
    rtest = ctx.guild.get_role(Role_TESTER)
    if settings["vp"] == 0 and rtest not in ctx.author.roles:
        await ctx.send(Err500, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return

    if str(ctx.author.id) in data:
        end_time = datetime.fromisoformat(data[str(ctx.author.id)])
        if datetime.now() < end_time:
            remaining_time = end_time - datetime.now()
            remaining_time_str = str(remaining_time).split(".")[0]
            await ctx.send(f"Ожидание ещё не прошло. Осталось: {remaining_time_str}")
            return


    scores = load_scores()
    RR = ctx.guild.get_role(ROLE_REGISTERED)
    user_id = str(ctx.author.id)
    CMI = bot.get_channel(C_MON_INFO)
    CI = bot.get_channel(C_INFO)
    CR = ctx.guild.get_role(Country_Role_RP)

    # ДРУГОЕ

    if CR not in ctx.author.roles:
        await ctx.send(Err501, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return

    if RR not in ctx.author.roles:
        await ctx.send(Err300_1, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    if ctx.channel.id not in ALLOWED_CHANEL_ID3:
        await ctx.send(Err001, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    if user_id in scores:
        """
        Далее подходит вычислительная часть.
        Вычисление производится по формуле:
        Минимальное значение - a - при определённой экономики
        Максимальное значение - b - при определённой экономики
        Особая ситуация - c - произведение событий (к примеру: VIP-роль (1.15) * недовольство населения (0.9) = 1.035)
        mon = round(round(random.randint(a,b)) * c)
        
        В реальности они умножаются постепенно.
        Особые ситуации ( ЕСЛИ != 1 ):
        
        RP:
        Счастливое население = 1.1
        Поддержка государств/альянса/ООН = 1.05 или 1.1 или 1.15
        Идеология = 1.1
        Несчастное население = 0.9
        
        
        NonRP:
        
        VIP-роль = 1.15
        Сотрудник (роль) = 1.15
        Поощрение из-за ошибки 
        
        """
        tph_type = ''
        tpgp = 0
        nickname = ctx.author.name
        if Disabled_economyRProle in ctx.author.roles:
            tpgp += 1
            tph_type = Disabled_economyRProle
            mon = round(random.randint(1000, 5000), -1)
        if TerribleEconomyRProle in ctx.author.roles:
            tpgp += 1
            tph_type = TerribleEconomyRProle
            mon = round(random.randint(7000, 13000), -1)
        if GrowingEconomyRProle in ctx.author.roles:
            tpgp += 1
            tph_type = GrowingEconomyRProle
            mon = round(random.randint(15000, 26000), -1)
        if BasicEconomyRProle in ctx.author.roles:
            tpgp += 1
            tph_type = BasicEconomyRProle
            mon = round(random.randint(25000, 50000), -1)
        if GoodEconomyRProle in ctx.author.roles:
            tpgp += 1
            tph_type = GoodEconomyRProle
            mon = round(random.randint(45000, 100000), -1)
        if AmazingEconomyRProle in ctx.author.roles:
            tpgp += 1
            tph_type = AmazingEconomyRProle
            mon = round(random.randint(99000, 222000), -1)
        if PerfectEconomyRProle in ctx.author.roles:
            tpgp += 1
            tph_type = PerfectEconomyRProle
            mon = round(random.randint(222000, 555000), -1)
        if VIProle in ctx.author.roles and tpgp == 1:
            mon = int(round(mon * 1.15, -1))
            embed1 = discord.Embed(
                title=None,  # Заголовок
                description="**+15% заработка за роль**",  # Описание
                color=0x32cd32
            )
            embed1.add_field(name="", value=f"{VIProle.mention}", inline=False)
            # embed.set_footer(text="text")
            # embed.set_thumbnail(url="url_picture")
            # embed.set_image(url="url_picture")
            await CMI.send(embed=embed1)
            await ctx.send(embed=embed1)
        if tpgp == 0:
            await ctx.send(Err304, delete_after=10)
            await asyncio.sleep(5)
            await ctx.message.delete()
            return
        if tpgp > 1:
            await ctx.send(Err305 + " Удалите лишнюю роль", delete_after=15)
            await CI.send(f"У {ctx.author.mention} обнаружено {tpgp} ролей экономики.")
            await asyncio.sleep(15)
            await ctx.message.delete()
            return
        if settings["errOcr"] != 0:
            embed1 = discord.Embed(
                title=None,  # Заголовок
                description=f"**+{round(settings["errOcr"]*100)-100}% заработка**",  # Описание
                color=0x32cd32
            )
            embed1.add_field(name="", value=f"Из-за сбоя в системе", inline=False)
            await ctx.send(embed=embed1)
            await CMI.send(embed=embed1)
        embed = discord.Embed(
            title=None,  # Заголовок
            description="**Роль заработка**",  # Описание
            color=0x32cd32
        )

        now1 = datetime.now(timezone)
        secs_after19701jan3hours1 = int((now1 - start_date).total_seconds())


        embed.add_field(name="", value=f"{tph_type.mention}**|** **{mon}:money_with_wings:**", inline=False)
        embed.add_field(name="", value=f"<t:{secs_after19701jan3hours1 + (3600*3)}:R>", inline=False)
        embed.set_author(name=f"{nickname}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
        await CMI.send(embed=embed)

        end_time = datetime.now() + timedelta(hours=4)
        end_time_str = end_time.isoformat()
        data[user_id] = end_time_str
        save_timedata(data)


        scores[user_id] += mon
        save_scores(scores)
        settings_save(settings)

        await asyncio.sleep(4 * 60 * 60)

        current_data = load_timedata()
        if user_id in current_data and current_data[user_id] == end_time_str:
            del current_data[user_id]
            save_timedata(current_data)


    else:
        await ctx.send(f'{Err301_2} Попробуйте использовать команду _`"!обновить"`_, возможно ваши очки были сброшены.', delete_after=10)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return



@bot.command(name="чек_баланс", aliases=["чек_кошелёк", 'чек_банк', "чек_казна"])
async def чек_баланс(ctx, user: discord.Member = False):
    if not user:
        await ctx.send("Не указана роль.", delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    settings = settings_load()
    scores = load_scores()
    try:
        user_id = str(user.id)
    except Exception as e:
        await ctx.send(f"Ошибка! {e}", delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    ROLE_MODER_OR_HIGHER1 = ctx.guild.get_role(ROLE_HELPER_OR_HIGHER)
    rtest = ctx.guild.get_role(Role_TESTER)
    if settings["vp"] == 0 and rtest not in ctx.author.roles:
        await ctx.send(Err500, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    if ctx.channel.id not in ALLOWED_CHANEL_ID3:
        await ctx.send(Err001, delete_after=3)
        await asyncio.sleep(3)
        await ctx.message.delete()
        return
    if user_id in scores and ROLE_MODER_OR_HIGHER1 in ctx.autor.roles:
        await ctx.send(f"У пользователя {user.mention} {scores[user_id]} очков.")
    elif ROLE_MODER_OR_HIGHER1 not in ctx.autor.roles:
        await ctx.send(Err020, delete_after=3)
        await asyncio.sleep(3)
        await ctx.message.delete()
    else:
        await ctx.send(Err301_2, delete_after=3)
        await asyncio.sleep(3)
        await ctx.message.delete()

@bot.command(name='датьочки', aliases=["дать_очки", "отдатьочки", 'отдать_очки'])
async def датьочки(ctx, recipient: discord.Member, points: int):
    C_INFO1 = bot.get_channel(C_INFO)
    scores = load_scores()
    sender_id = str(ctx.author.id)
    recipient_id = str(recipient.id)
    sts = settings_load()
    rtest = ctx.guild.get_role(Role_TESTER)
    if sts["vp"] == 0 and rtest not in ctx.author.roles:
        await ctx.send(Err500, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    if ctx.channel.id not in ALLOWED_CHANEL_ID3:
        await ctx.send(Err001, delete_after=5)
        await asyncio.sleep(3)
        await ctx.message.delete()
        return
    if sender_id not in scores or scores[sender_id] < points:
        await ctx.send(Err302, delete_after=5)
        await asyncio.sleep(3)
        await ctx.message.delete()
        return
    scores[sender_id] -= points
    if recipient_id in scores:
        scores[recipient_id] += points
    else:
        scores[recipient_id] = points
    save_scores(scores)
    await ctx.send(f"Вы передали {points} очков пользователю {recipient.mention}. У вас осталось {scores[sender_id]} очков.")
    await C_INFO1.send(f"{ctx.author.mention} передал {points} очков пользователю {recipient.mention}.")




@bot.command()
async def топ(ctx):
    scores = load_scores()
    sts = settings_load()
    rtest = ctx.guild.get_role(Role_TESTER)
    if sts["vp"] == 0 and rtest not in ctx.author.roles:
        await ctx.send(Err500, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    if ctx.channel.id not in ALLOWED_CHANEL_ID3:
        await ctx.send(Err001, delete_after=3)
        await asyncio.sleep(3)
        await ctx.message.delete()
        return
    if not scores:
        await ctx.send(Err301_1, delete_after=3)
        await asyncio.sleep(3)
        await ctx.message.delete()
        return
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:10]
    top_list = "\n".join([f"<@{user_id}>: {score} очков" for user_id, score in sorted_scores])
    await ctx.send(f"Топ пользователей:\n{top_list}")

@bot.command(name='обновить', aliases=["update", "обновитьочки"])
async def обновить(ctx):

    scores = load_scores()
    user_id = str(ctx.author.id)
    CMI = bot.get_channel(C_MON_INFO)
    RR = ctx.guild.get_role(ROLE_REGISTERED)
    sts = settings_load()
    rtest = ctx.guild.get_role(Role_TESTER)
    if sts["vp"] == 0 and rtest not in ctx.author.roles:
        await ctx.send(Err500, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    if RR not in ctx.author.roles:
        await ctx.send(Err300_1, delete_after=3)
        await asyncio.sleep(3)
        await ctx.message.delete()
        return
    if ctx.channel.id not in ALLOWED_CHANEL_ID3:
        await ctx.send(Err001, delete_after=3)
        await asyncio.sleep(3)
        await ctx.message.delete()
        return
    if user_id not in scores:
        scores[user_id] = 0
        save_scores(scores)

        nickname = ctx.author.name

        now = datetime.now(timezone)
        timer_secsafter1970 = int((now - start_date).total_seconds()) + (3600 * 3)

        embed = discord.Embed(
            title='**Очки успешно обновлены**',  # Заголовок
            description=f"-# <t:{timer_secsafter1970}:R>",  # Описание
            color=0x32cd32
        )
        embed.set_author(name=f"{nickname}", icon_url=ctx.author.avatar.url)



        await ctx.send(embed=embed)
        await CMI.send(embed=embed)
    else:
        await ctx.send(Err303, delete_after=3)
        await asyncio.sleep(3)
        await ctx.message.delete()
        return

@bot.command()
async def добавитьочки(ctx, user: discord.Member, points: int):
    scores = load_scores()
    user_id = str(user.id)
    sts = settings_load()
    rtest = ctx.guild.get_role(Role_TESTER)
    if sts["vp"] == 0 and rtest not in ctx.author.roles:
        await ctx.send(Err500, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    if user_id in scores:
        scores[user_id] += points
    else:
        scores[user_id] = points

    save_scores(scores)
    await ctx.send(f"Пользователю {user.mention} добавлено {points} очков. Текущий счёт: {scores[user_id]}.")

@bot.command()
async def удалитьочки(ctx, user: discord.Member, points: int):
    scores = load_scores()
    user_id = str(user.id)
    sts = settings_load()
    rtest = ctx.guild.get_role(Role_TESTER)
    if sts["vp"] == 0 and rtest not in ctx.author.roles:
        await ctx.send(Err500, delete_after=5)
        await asyncio.sleep(5)
        await ctx.message.delete()
        return
    if user_id in scores:
        scores[user_id] = max(scores[user_id] - points, 0)  # Не даём счёту уйти в минус
        save_scores(scores)
        if scores[user_id] == 0:
            del scores[user_id]
            save_scores(scores)
            await ctx.send(f"Очки пользователя {user.mention} сброшены, так как они ушли в минус.")
        await ctx.send(f"У пользователя {user.mention} удалено {points} очков. Текущий счёт: {scores[user_id]}.")
    else:
        await ctx.send(Err301, delete_after=3)












@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен и готов к работе!')
    data = load_timedata()
    for user_id, end_time_str in data.items():
        end_time = datetime.fromisoformat(end_time_str)
        now = datetime.now()
        if now < end_time:
            remaining_time = (end_time - now).total_seconds()
            await asyncio.sleep(remaining_time)
            current_data = load_timedata()
            if user_id in current_data and current_data[user_id] == end_time_str:
                del current_data[user_id]
                save_timedata(current_data)



@bot.command(name="привет", aliases=["Добрый_день", "hello", 'даров', 'дарова', 'скажи_привет', 'guten_tag', 'hallo', 'здравствуйте', 'hi'])
async def привет(ctx):
    if ctx.channel.id in ALLOWED_CHANEL_ID3:
        await ctx.send("Привет!")
    else:
        await ctx.send(Err001, delete_after=3)
        await asyncio.sleep(3)
        await ctx.message.delete()
Gde_bot_words = ['Я здесь!', 'Тут!', 'Уже здесь!', 'Где-то тут', 'Недалеко', 'Вроде здесь', "На этом сервере", "Пока только тут", 'Скоро будет!', 'Точно не в космосе', '👋', 'У тебя на экране']
@bot.command(name="гдебот", aliases=['где_бот',])
async def гдебот(ctx):
    if ctx.channel.id in ALLOWED_CHANEL_ID3:
        await ctx.send(random.choice(Gde_bot_words))
    else:
        await ctx.send(Err001, delete_after=3)
        await asyncio.sleep(3)
        await ctx.message.delete()
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot.run(token)