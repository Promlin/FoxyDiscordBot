from random import randint
import disnake
from disnake.ext import commands

# TODO add stickers and description to dropdown menu

class AnimeAdvisor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Аниме советчик")
    async def anime_advisor(self, inter: disnake.ApplicationCommandInteraction):
        view = DropdownViewAnime()

        await inter.send("Pick the genre:", view=view)


class DropdownAnime(disnake.ui.StringSelect):
    def __init__(self):
        self.genre_dict = {
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

        self.anime_dict = {
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

        self.emoji_dict = {
            'romance': ["💗"],
            'everyday life': ["🏄‍♀️"],
            'detective': ["🔎"],
            'drama': ["🤧"],
            'comedy': ["🤪"],
            'shonen': ["⚔"],
            'fantasy': ["🏹"],
            'sport': ["🥇"]
        }

        self.description_dict = {
            'romance': ["Very cute stories"],
            'everyday life': ["To relax after hard work"],
            'detective': ["Exciting stories"],
            'drama': ["Smth make you cry"],
            'comedy': ["For loud laughter"],
            'shonen': ["Epic battles"],
            'fantasy': ["To change your reality"],
            'sport': ["For strong motivation"]
        }

        options = []

        genres = list(self.genre_dict)
        for genre in genres:
            options.append(disnake.SelectOption(
                label=genre, description=str(self.description_dict[genre][0]),
                emoji=self.emoji_dict[genre][0]))

        super().__init__(
            placeholder="Choose the genre",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, inter: disnake.MessageInteraction):
        genre = self.values[0]
        to_advise = self.genre_dict[genre][randint(0, len(self.genre_dict[genre]) - 1)]
        link = self.anime_dict[to_advise][0]

        await inter.response.send_message(f"I can advise you {to_advise}. \n "
                                          f"You can follow the link {link}")


class DropdownViewAnime(disnake.ui.View):
    def __init__(self):
        super().__init__()

        # Add the dropdown to our view object.
        self.add_item(DropdownAnime())


bot = commands.Bot(command_prefix=commands.when_mentioned)


def setup(bot):
    bot.add_cog(AnimeAdvisor(bot))