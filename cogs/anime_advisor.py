from random import randint
import disnake
from disnake.ext import commands

# TODO добавить картинки для каждого аниме или картинки для рубрики

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
            'Mahoutsukai no Yome': ['https://animego.org/anime/nevesta-charodeya-s116',
                                    'annotation'],
            'Tomo-chan wa Onnanoko!': ['https://animego.org/anime/tomo-devushka-s2236',
                                       'annotation'],
            'Horimiya': ['https://animego.org/anime/horimiya-s1686',
                         'annotation'],
            'Akatsuki no Yona': ['https://animego.org/anime/rassvet-yony-s2028',
                                 'annotation'],
            'Kaichou wa Maid-sama!': ['https://animego.org/anime/prezident-studsoveta-gornichnaya-s347',
                                      'annotation'],
            'Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen':
                ['https://animego.org/anime/gospozha-kaguya-v-lyubvi-kak-na-voyne-s821',
                 'annotation'],
            'Bakuman': ['https://animego.org/anime/bakuman-s128',
                        'annotation'],
            'Gekkan Shoujo Nozaki-kun': ['https://animego.org/anime/ezhemesyachnoe-sedze-nodzaki-s2030',
                                         'annotation'],
            'Shokugeki no Souma: San no Sara': ['https://animego.org/anime/kulinarnye-poedinki-somy-trete-blyudo-s321',
                                                'annotation'],
            'Bocchi the Rock!': ['https://animego.org/anime/odinokiy-roker-s2146',
                                 'annotation'],
            'More than a married couple, but not lovers':
                ['https://animego.org/anime/bolshe-chem-para-menshe-chem-lyubovniki-s2147',
                 'annotation'],
            'Bungou Stray Dogs': ['https://animego.org/anime/bungou-stray-dogs-s335',
                                  'annotation'],
            'Ghost in the Shell: Stand Alone Complex':
                ['https://animego.org/anime/prizrak-v-dospehah-sindrom-odinochki-s849',
                 'annotation'],
            'Death Note': ['https://animego.org/anime/death-note-v2-s95',
                           'annotation'],
            'Durarara!!': ['https://animego.org/anime/durarara-s1-s1547',
                           'annotation'],
            'Kimi no Suizou wo Tabetai': ['https://animego.org/anime/ya-hochu-sest-tvoyu-podzheludochnuyu-s771',
                                          'annotation'],
            'Dororo': ['https://animego.org/anime/dororo-s1-s791',
                       'annotation'],
            'Grand Blue': ['https://animego.org/anime/neobyatnyy-okean-s645',
                           'annotation'],
            'Dr. Stone: Stone Wars': ['https://animego.org/anime/doktor-stoun-kamennye-voyny-s1698',
                                      'annotation'],
            'One Piece': ['https://animego.org/anime/van-pis-s65',
                          'Gol D. Roger was known as the Pirate King, the strongest and most infamous being to have'
                          ' sailed the Grand Line. The capture and death of Roger by the World Government brought a '
                          'change throughout the world. His last words before his death revealed the location of the'
                          'greatest treasure in the world, One Piece. It was this revelation that brought about the '
                          'Grand Age of Pirates, men who dreamed of finding One Piece (which promises an unlimited '
                          'amount of riches and fame), and quite possibly the most coveted of titles for the person '
                          'who found it, the title of the Pirate King.Enter Monkey D. Luffy, a 17-year-old boy that '
                          'defies your standard definition of a pirate. Rather than the popular persona of a wicked,'
                          ' hardened, toothless pirate who ransacks villages for fun, Luffy’s reason for being a pirate'
                          ' is one of pure wonder; the thought of an exciting adventure and meeting new and intriguing '
                          'people, along with finding One Piece, are his reasons of becoming a pirate. Following in'
                          ' the footsteps of his childhood hero, Luffy and his crew travel across the Grand Line,'
                          ' experiencing crazy adventures, unveiling dark mysteries and battling strong enemies, all '
                          'in order to reach One Piece.'],
            'Naruto': ['https://animego.org/anime/naruto-s102',
                       'Naruto Uzumaki, a hyperactive and knuckle-headed ninja, lives in Konohagakure, the Hidden Leaf '
                       'village. Moments prior to his birth, a huge demon known as the Kyuubi, the Nine-tailed Fox,'
                       ' attacked Konohagakure and wreaked havoc. In order to put an end to the Kyuubi\'s rampage,'
                       ' the leader of the village, the 4th Hokage, sacrificed his life and sealed the monstrous beast '
                       'inside the newborn Naruto.   Shunned because of the presence of the Kyuubi inside him, Naruto'
                       ' struggles to find his place in the village. He strives to become the Hokage of Konohagakure,'
                       ' and he meets many friends and foes along the way.'],
            'Tengen Toppa Gurren Lagann': ['https://animego.org/anime/gurren-lagann1-s829',
                                           'In a far away future, mankind lives underground in huge caves, unknowing '
                                           'of a world above with a sky and stars.In the small village of Jiha, Simon,'
                                           ' a shy boy who works as a digger discovers a strange glowing object '
                                           'during excavation. The enterprising Kamina, a young man with a pair of '
                                           'rakish sunglasses and the passion of a firey sun, befriends Simon and '
                                           'forms a small band of brothers, the Gurren Brigade, to escape the village '
                                           'and break through the ceiling of the cave to reach the surface, which few'
                                           ' believe exist.The village elder won\'t hear of such foolishness and'
                                           ' punishes the Brigade. However, when disaster strikes from the world above '
                                           'and the entire village is in jeopardy, it\'s up to Simon, Kamina, a girl '
                                           'with a big gun named Yoko, and the small yet sturdy robot, Lagann, to save'
                                           ' the day.The new friends journey to the world above and find that the '
                                           'surface is a harsh battlefield, and it\'s up to them to fight back against'
                                           ' the rampaging Beastmen to turn the tide in the humans\' favor! Pierce'
                                           ' the heavens, Gurren Lagann!'],
            'Great Teacher Onizuka': ['https://animego.org/anime/krutoy-uchitel-onidzuka-s556',
                                      'Onizuka is a reformed biker gang leader who has his sights set on an honorable '
                                      'new ambition: to become the world\'s greatest teacher... for the purpose of '
                                      'meeting sexy high school girls. Okay, so he\'s mostly reformed.\n'
                                      'So get ready for math that doesn\'t add up, language you\'d be slapped for '
                                      'using, and biology that would make a grown man blush... unless of course, '
                                      'you\'re the Great Teacher Onizuka.'],
            'Log Horizon': ['https://animego.org/anime/log-gorizont-s300',
                            'By its eleventh expansion pack, the massively multiplayer online role-playing game Elder'
                            ' Tale has become a global success, having a following of millions of players. However,'
                            ' during the release of its twelfth expansion pack: Novasphere Pioneers, thirty thousand'
                            ' Japanese gamers who are all logged on at the time of the update, suddenly find themselves'
                            ' transported inside the game world and donning their in-game avatars. In the midst of the '
                            'event, a socially awkward gamer called Shiroe along with his friends Naotsugu and Akatsuki'
                            ' decide to team up so that they may face this world which has now become their reality'
                            ' along with the challenges which lie ahead.'],
            'No Game No Life': ['https://animego.org/anime/net-igry-net-zhizni-s171',
                                'The story of No Game, No Life centers around Sora and Shiro, a brother and sister '
                                'whose reputations as brilliant NEET hikikomori gamers have spawned urban legends all'
                                ' over the Internet. These two gamers even consider the real world as just another '
                                '"crappy game." One day, they are summoned by a boy named "God" to an alternate world.'
                                ' There, God has prohibited war and declared this to be a world where "everything is'
                                ' decided by games"—even national borders. Humanity has been driven back into one '
                                'remaining city by the other races. Will Sora and Shiro, the good-for-nothing brother'
                                ' and sister, become the "Saviors of Humanity" on this alternate world? "Well, let\'s'
                                ' start playing."'],
            'Kuroko no Basket': ['https://animego.org/anime/basketbol-kuroko-s531',
                                 ' Kuroko no Basket follows the journey of Seirin\'s players as they attempt to become'
                                 ' the best Japanese high school team by winning the Interhigh Championship. To reach '
                                 'their goal, they have to cross pathways with several powerful teams, some of which '
                                 'have one of the five players with godlike abilities, whom Kuroko and Taiga make a'
                                 ' pact to defeat.'],
            'Haikyuu!!': ['https://animego.org/anime/voleybol-s256',
                          'A chance event triggered Shouyou Hinata\'s love for volleyball. His club had no members,'
                          ' but somehow persevered and finally made it into its very first and final regular match of'
                          ' middle school, where it was steamrolled by Tobio Kageyama, a superstar player known as '
                          '"King of the Court." Vowing revenge, Hinata applied to the Karasuno High School volleyball '
                          'club... only to come face-to-face with his hated rival, Kageyama! A tale of hot-blooded '
                          'youth and volleyball from the pen of Haruichi Furudate!!'],
            'Shigatsu wa Kimi no Uso': ['https://animego.org/anime/tvoya-aprelskaya-lozh-s793',
                                        'Music accompanies the path of the human metronome, the prodigious pianist'
                                        ' Kousei Arima. But after the passing of his mother, Saki Arima, Kousei falls'
                                        ' into a downward spiral, rendering him unable to hear the sound of his own'
                                        ' piano. \n Two years later, Kousei still avoids the piano, leaving behind his'
                                        ' admirers and rivals, and lives a colorless life alongside his friends Tsubaki'
                                        ' Sawabe and Ryouta Watari. However, everything changes when he meets a'
                                        ' beautiful violinist, Kaori Miyazono, who stirs up his world and sets him on '
                                        'a journey to face music again.'],
            'Yuri!!! on Ice': ['https://animego.org/anime/yuri-na-ldu-s165',
                               'The show\'s story revolves around Yuuri Katsuki, who carried all of Japan\'s'
                               ' hopes on his shoulders to win at the Gran Prix Finale ice skating competition,'
                               ' but suffered a crushing defeat. He returns home to Kyushu and half feels like he wants'
                               ' to retire, and half feels like he wants to continue ice skating. With those mixed'
                               ' feelings swirling inside him, he confines himself inside his parents house. '
                               'Suddenly the five-time consecutive world championship ice skater Viktor Nikiforov '
                               'appears before him, and along with him is Yuri Plisetsky, a young Russian figure skater'
                               ' who is already defeating his seniors. Viktor and both Yuris take up the challenge on'
                               ' an unprecedented Gran Prix series.']
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
        annotation = self.anime_dict[to_advise][1]

        embed = disnake.Embed(
            title=to_advise,
            description=link,
            color=disnake.Colour.green()
        )

        embed.add_field(name="Annotation", value=annotation, inline=False)
        embed.set_image(file=disnake.File("welcome_image.png"))

        await inter.response.send_message(embed=embed)


class DropdownViewAnime(disnake.ui.View):
    def __init__(self):
        super().__init__()

        # Add the dropdown to our view object.
        self.add_item(DropdownAnime())


bot = commands.Bot(command_prefix=commands.when_mentioned)


def setup(bot):
    bot.add_cog(AnimeAdvisor(bot))
