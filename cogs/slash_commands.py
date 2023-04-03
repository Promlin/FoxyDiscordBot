import disnake
from disnake.ext import commands
from typing import Optional
from cogs.commands import CMDUsers

"""
I'm going to create such functions:
- I need to come up with some ideas 
-
-
"""


# slash - command
@commands.slash_command(description="Калькулятор")
async def calc(inter, a: int, oper: str, b: int):
    if oper == "+":
        result = a + b
    elif oper == "-":
        result = a - b
    else:
        result = "Неверный оператор"

    await inter.send(str(result))


@commands.slash_command(description="Аниме советчик")
async def anime(inter, genre: str):
    genre_dict = {
        'romance': ['Mahoutsukai no Yome', 'Tomo-chan wa Onnanoko!', 'Horimiya',
                    'Akatsuki no Yona', 'Kaichou wa Maid-sama!',
                    'Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen'],
        'everyday life': ['Bakuman', 'Gekkan Shoujo Nozaki-kun', 'Shokugeki no Souma: San no Sara',
                          'Bocchi the Rock!', 'More than a married couple, but not lovers'],
        'detective': ['Bungou Stray Dogs', 'Ghost in the Shell: Stand Alone Complex', 'Death Note',
                      'Durarara!!'],
        'drama': ['Shigatsu wa Kimi no Uso', 'Kimi no Suizou wo Tabetai', 'Dororo'],
        'comedy': ['Grand Blue', 'Dr. Stone: Stone Wars', 'Great Teacher Onizuka'],
        'shonen': ['One Piece', 'Naruto', 'Tengen Toppa Gurren Lagann'],
        'fantasy': ['Log Horizon', 'No Game No Life'],
        'sport': ['Yuri!!! on Ice', 'Kuroko no Basket', 'Haikyuu!!']
    }

    anime_dict = {
        'Mahoutsukai no Yome': ['https://animego.org/anime/nevesta-charodeya-s116'],
        'Tomo-chan wa Onnanoko!': ['https://animego.org/anime/tomo-devushka-s2236'],
        'Horimiya': ['https://animego.org/anime/horimiya-s1686'],
        'Akatsuki no Yona': ['https://animego.org/anime/rassvet-yony-s2028'],
        'Kaichou wa Maid-sama!': ['https://animego.org/anime/prezident-studsoveta-gornichnaya-s347'],
        'Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen':
            ['https://animego.org/anime/gospozha-kaguya-v-lyubvi-kak-na-voyne-s821'],
        'Bakuman': ['https://animego.org/anime/bakuman-s128'],
        'Gekkan Shoujo Nozaki-kun': ['https://animego.org/anime/ezhemesyachnoe-sedze-nodzaki-s2030'],
        'Shokugeki no Souma: San no Sara': ['https://animego.org/anime/kulinarnye-poedinki-somy-trete-blyudo-s321'],
        'Bocchi the Rock!': ['https://animego.org/anime/odinokiy-roker-s2146'],
        'More than a married couple, but not lovers':
            ['https://animego.org/anime/bolshe-chem-para-menshe-chem-lyubovniki-s2147'],
        'Bungou Stray Dogs': ['https://animego.org/anime/bungou-stray-dogs-s335'],
        'Ghost in the Shell: Stand Alone Complex':
            ['https://animego.org/anime/prizrak-v-dospehah-sindrom-odinochki-s849'],
        'Death Note': ['https://animego.org/anime/death-note-v2-s95'],
        'Durarara!!': ['https://animego.org/anime/durarara-s1-s1547'],
        'Kimi no Suizou wo Tabetai': ['https://animego.org/anime/ya-hochu-sest-tvoyu-podzheludochnuyu-s771'],
        'Dororo': ['https://animego.org/anime/dororo-s1-s791'],
        'Grand Blue': ['https://animego.org/anime/neobyatnyy-okean-s645'],
        'Dr. Stone: Stone Wars': ['https://animego.org/anime/doktor-stoun-kamennye-voyny-s1698'],
        'One Piece': ['https://animego.org/anime/van-pis-s65'],
        'Naruto': ['https://animego.org/anime/naruto-s102'],
        'Tengen Toppa Gurren Lagann': ['https://animego.org/anime/gurren-lagann1-s829'],
        'Great Teacher Onizuka': ['https://animego.org/anime/krutoy-uchitel-onidzuka-s556'],
        'Log Horizon': ['https://animego.org/anime/log-gorizont-s300'],
        'No Game No Life': ['https://animego.org/anime/net-igry-net-zhizni-s171'],
        'Kuroko no Basket': ['https://animego.org/anime/basketbol-kuroko-s531'],
        'Haikyuu!!': ['https://animego.org/anime/voleybol-s256'],
        'Shigatsu wa Kimi no Uso': ['https://animego.org/anime/tvoya-aprelskaya-lozh-s793'],
        'Yuri!!! on Ice': 'https://animego.org/anime/yuri-na-ldu-s165'
    }

    for key in genre_dict:
        print(key)


def setup():
    bot = commands.Bot(command_prefix=commands.when_mentioned, help_command=None, intents=disnake.Intents.all(),
                       test_guilds=[1067903829040955432])

    bot.add_cog(CMDUsers(bot))
