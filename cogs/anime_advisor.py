from random import randint
import disnake
from disnake.ext import commands


# TODO добавить картинки для каждого аниме или картинки для рубрики
# TODO нормально организовать хранение данных

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
            'Mahoutsukai no Yome':
                ['https://animego.org/anime/nevesta-charodeya-s116',
                 'Hatori Chise is only 16, but she has lost far more than most. With neither family nor hope, it'
                 ' seems all doors are closed to her. But, a chance encounter began to turn the rusted wheels of fate.'
                 ' In her darkest hour, a mysterious magus appears before Chise, offering a chance she couldn\'t turn'
                 ' down. This magus who seems closer to demon than human, will he bring her the light she desperately'
                 ' seeks, or drown her in ever deeper shadows?'],
            'Tomo-chan wa Onnanoko!':
                ['https://animego.org/anime/tomo-devushka-s2236',
                 'Boyish high school girl Aizawa Tomo finally manages to tell her childhood friend Jun that she’s got'
                 ' a crush on him. Unfortunately, her confession goes right over his head—he didn’t even realize she '
                 'was a girl until junior high, and even now, Jun still thinks of her as a bro! How can Tomo-chan'
                 ' possibly convince him otherwise and win Jun’s heart?'],
            'Horimiya':
                ['https://animego.org/anime/horimiya-s1686',
                 'Although admired at school for her amiability and academic prowess, high school student Kyouko Hori'
                 ' has been hiding another side of her. With her parents often away from home due to work, Hori has to'
                 ' look after her younger brother and do the housework, leaving no chance to socialize away from'
                 ' school. Meanwhile, Izumi Miyamura is seen as a brooding, glasses-wearing otaku. However, in '
                 'reality, he is a gentle person inept at studying. Furthermore, he has nine piercings hidden behind '
                 'his long hair and a tattoo along his back and left shoulder. By sheer chance, Hori and Miyamura '
                 'cross paths outside of school—neither looking as the other expects. These seemingly polar opposites'
                 ' become friends, sharing with each other a side they have never shown to anyone else.'],
            'Akatsuki no Yona':
                ['https://animego.org/anime/rassvet-yony-s2028',
                 'Upon her sixteenth birthday, the cheerful Princess Yona intended to tell her doting father of her'
                 ' love for Soo-won, but her life was turned upside down after witnessing the man she loves cruelly'
                 ' assassinating her father. Heartbroken by this painful betrayal, Princess Yona fled the palace with '
                 'her loyal servant Hak. Now, she will take up the sword and the bow on a quest to gain new allies '
                 'and protect her beloved people.'],
            'Kaichou wa Maid-sama!':
                ['https://animego.org/anime/prezident-studsoveta-gornichnaya-s347',
                 'Misaki Ayuzawa is the first female student council president at a once-all-boys-turned-co-ed school.'
                 ' She rules the school with a strict discipline demeanor, but she has a secret: she works at a maid'
                 ' cafe due to her family\'s circumstances. One day, the popular A-student and notorious heart-breaker'
                 ' Takumi Usui finds out her secret and makes a deal with her to keep it hush from the school in'
                 ' exchange for spending some time with him.'],
            'Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen':
                ['https://animego.org/anime/gospozha-kaguya-v-lyubvi-kak-na-voyne-s821',
                 'Considered a genius due to having the highest grades in the country, Miyuki Shirogane leads the'
                 ' prestigious Shuchiin Academy\'s student council as its president, working alongside the beautiful'
                 ' and wealthy vice president Kaguya Shinomiya. The two are often regarded as the perfect couple by'
                 ' students despite them not being in any sort of romantic relationship. However, the truth is that '
                 'after spending so much time together, the two have developed feelings for one another; unfortunately,'
                 ' neither is willing to confess, as doing so would be a sign of weakness. With their pride as elite'
                 ' students on the line, Miyuki and Kaguya embark on a quest to do whatever is necessary to get a '
                 'confession out of the other. Through their daily antics, the battle of love begins!'],
            'Bakuman':
                ['https://animego.org/anime/bakuman-s128',
                 'As a child, Moritaka Mashiro dreamt of becoming a mangaka, just like his childhood hero and uncle,'
                 ' Tarou Kawaguchi, creator of a popular gag manga. But when tragedy strikes, he gives up on his dream'
                 ' and spends his middle school days studying, aiming to become a salaryman instead. One day, his'
                 ' classmate Akito Takagi, the school\'s top student and aspiring writer, notices the detailed'
                 ' drawings in Moritaka\'s notebook. Seeing the vast potential of his artistic talent, Akito'
                 ' approaches Moritaka, proposing that they become mangaka together. After much convincing, '
                 'Moritaka realizes that if he is able to create a popular manga series, he may be able to get the'
                 ' girl he has a crush on, Miho Azuki, to take part in the anime adaptation as a voice actor. Thus '
                 'the pair begins creating manga under the pen name Muto Ashirogi, hoping to become the greatest '
                 'mangaka in Japan, the likes of which no one has ever seen.'],
            'Gekkan Shoujo Nozaki-kun':
                ['https://animego.org/anime/ezhemesyachnoe-sedze-nodzaki-s2030',
                 'High school student Chiyo Sakura has a crush on schoolmate Umetarou Nozaki, but when she confesses'
                 ' her love to him, he mistakes her for a fan and gives her an autograph. When she says that she'
                 ' always wants to be with him, he invites her to his house and has her help on some drawings.'
                 ' Chiyo discovers that Nozaki is actually a renowned shoujo manga artist named Sakiko Yumeno.'
                 ' She then agrees to be his assistant in order to get closer to him. As they work on his manga,'
                 ' they encounter other schoolmates who assist them or serve as inspirations for characters in the'
                 ' stories.'],
            'Shokugeki no Souma: San no Sara':
                ['https://animego.org/anime/kulinarnye-poedinki-somy-trete-blyudo-s321',
                 'Ever since he was a child, fifteen-year-old Souma Yukihira has helped his father by working '
                 'as the sous chef in the restaurant his father runs and owns. Throughout the years, Souma developed'
                 ' a passion for entertaining his customers with his creative, skilled, and daring culinary '
                 'creations. His dream is to someday own his family\'s restaurant as its head chef. Yet when his'
                 ' father suddenly decides to close the restaurant to test his cooking abilities in restaurants '
                 'around the world, he sends Souma to Tootsuki Culinary Academy, an elite cooking school where '
                 'only 10 percent of the students graduate. The institution is famous for its "Shokugeki" or '
                 '"food wars," where students face off in intense, high-stakes cooking showdowns. As Souma and '
                 'his new schoolmates struggle to survive the extreme lifestyle of Tootsuki, more and greater'
                 ' challenges await him, putting his years of learning under his father to the test.'],
            'Bocchi the Rock!':
                ['https://animego.org/anime/odinokiy-roker-s2146',
                 'Yearning to make friends and perform live with a band, lonely and socially anxious Hitori "Bocchi"'
                 ' Gotou devotes her time to playing the guitar. On a fateful day, Bocchi meets the outgoing drummer'
                 ' Nijika Ijichi, who invites her to join Kessoku Band when their guitarist, Ikuyo Kita, flees before'
                 ' their first show. Soon after, Bocchi meets her final bandmate—the cool bassist Ryou Yamada. \n \n'
                 'Although their first performance together is subpar, the girls feel empowered by their shared love '
                 'for music, and they are soon rejoined by Kita. Finding happiness in performing, Bocchi and her'
                 ' bandmates put their hearts into improving as musicians while making the most of their fleeting'
                 ' high school days.'],
            'More than a married couple, but not lovers':
                ['https://animego.org/anime/bolshe-chem-para-menshe-chem-lyubovniki-s2147',
                 'Third-year high school student Jirou Yakuin hoped to partner with Shiori Sakurazaka of the same'
                 ' class in the mandatory "Couple Practical" course. In this practical, students must demonstrate '
                 'that they have the necessary skillset to live with a partner of the opposite sex while presenting '
                 'a certain level of harmony to the video surveillance that grades them. \n \n Unfortunately, random'
                 ' chance put his slightly subdued self into the practical with the person polar opposite to him, '
                 'the gyaru Akari Watanabe. Akari on the other hand hoped to be paired with her crush Minami Tenjin. '
                 '\n \n Their hopes are doubly dashed when they find out that Shiori and Minami are assigned together.'
                 ' Thus, they reluctantly decide to cooperate to reach the top ten, which would give them the right to'
                 ' exchange partners if both couples agree. To that end, Jirou steals Akari\'s first kiss without'
                 ' realizing what he\'d done, while giving a hurried good-bye kiss...'],
            'Bungou Stray Dogs':
                ['https://animego.org/anime/bungou-stray-dogs-s335',
                 'For weeks, Atsushi Nakajima\'s orphanage has been plagued by a mystical tiger that'
                 ' only he seems to be aware of. Suspected to be behind the strange incidents, the '
                 '18-year-old is abruptly kicked out of the orphanage and left hungry, homeless, and '
                 'wandering through the city. \n \n While starving on a riverbank, Atsushi saves a'
                 ' rather eccentric man named Osamu Dazai from drowning. Whimsical suicide enthusiast '
                 'and supernatural detective, Dazai has been investigating the same tiger that has'
                 ' been terrorizing the boy. Together with Dazai\'s partner Doppo Kunikida, they '
                 'solve the mystery, but its resolution leaves Atsushi in a tight spot. As various'
                 ' odd events take place, Atsushi is coerced into joining their firm of supernatural'
                 ' investigators, taking on unusual cases the police cannot handle, alongside his'
                 'numerous enigmatic co-workers.'],
            'Ghost in the Shell: Stand Alone Complex':
                ['https://animego.org/anime/prizrak-v-dospehah-sindrom-odinochki-s849',
                 'In the not so distant future, mankind has advanced to a state where complete body transplants from '
                 'flesh to machine is possible. This allows for great increases in both physical and cybernetic prowess'
                 ' and blurring the lines between the two worlds. However, criminals can also make full use of such '
                 'technology, leading to new and sometimes, very dangerous crimes. In response to such innovative new'
                 ' methods, the Japanese Government has established Section 9, an independently operating police unit'
                 ' which deals with such highly sensitive crimes. \n \n Led by Daisuke Aramaki and Motoko Kusanagi,'
                 ' Section 9 deals with such crimes over the entire social spectrum, usually with success. However, '
                 'when faced with a new A level hacker nicknamed “The Laughing Man”, the team is thrown into a '
                 'dangerous cat and mouse game, following the hacker’s trail as it leaves its mark on Japan.'],
            'Death Note':
                ['https://animego.org/anime/death-note-v2-s95',
                 'Yagami Light is a 17-year-old genius from Japan who is tired of his life, school, and the'
                 ' state of the world as he knows it. One day, on the way home from class, Light stumbles'
                 ' upon a dark notebook with "Death Note" written on the front. Intrigued by its appearance,'
                 ' Light reads the first few sentences, only to find out that it states that anyone whose'
                 ' name is written inside will die. Discarding it as a joke, Light continues his daily '
                 'activities. Soon after though, his human curiosity takes the better of him and prompts '
                 'Light to try the notebook, discovering the truth behind first sentence. Now, with power '
                 'in his hands, Yagami Light is on a quest to change the world and become God of the New '
                 'World. His path to holy status won\'t be easy however, as another genius, known as L, is '
                 'working against Light\'s beliefs and Light himself. Who will win this power'
                 ' of Gods between humans? '],
            'Durarara!!':
                ['https://animego.org/anime/durarara-s1-s1547',
                 'In Tokyo\'s downtown district of Ikebukuro, amidst many strange rumors and warnings of '
                 'anonymous gangs and dangerous occupants, one urban legend stands out above the rest – the'
                 ' existence of a headless “Black Rider” who is said to be seen driving a jet-black'
                 ' motorcycle through the city streets. \n \n Ryuugamine Mikado has always longed for the '
                 'excitement of the city life, and an invitation from a childhood friend convinces him to '
                 'move to Tokyo. Witnessing the Black Rider on his first day in the city, his wishes already '
                 'seem to have been granted. But as supernatural events begin to occur, ordinary citizens'
                 ' like himself, along with Ikebukuro\'s most colorful inhabitants, are mixed up in the'
                 ' commotion breaking out in their city.'],
            'Kimi no Suizou wo Tabetai':
                ['https://animego.org/anime/ya-hochu-sest-tvoyu-podzheludochnuyu-s771',
                 'Spring time in April and the last of the cherry blossoms are still in bloom.'
                 ' The usually aloof bookworm with no interest in others comes across a book '
                 'in a hospital waiting room. Handwritten on the cover are the words: "Living'
                 ' with Dying." He soon discovers that it is a diary kept by his very popular'
                 ' and genuinely cheerful classmate, Sakura Yamauchi, who reveals to him that'
                 ' she is secretly suffering from a pancreatic illness and only has a limited'
                 ' time left. It is at this moment that she gains just one more person to'
                 ' share her secret. Trying to maintain a normal life as much as possible,'
                 ' Sakura is determined to live her life to the fullest until the very last'
                 ' day. As her free spirit and unpredictable actions throw him for a loop, his'
                 ' heart begins to gradually change.'],
            'Dororo':
                ['https://animego.org/anime/dororo-s1-s791',
                 'A samurai lord has bartered away his newborn son\'s organs to forty-eight demons in exchange '
                 'for dominance on the battlefield. Yet, the abandoned infant survives thanks to a medicine man'
                 ' who equips him with primitive prosthetics—lethal ones with which the wronged son will use to'
                 ' hunt down the multitude of demons to reclaim his body one piece at a time, before confronting'
                 ' his father. On his journeys the young hero encounters an orphan who claims to be the greatest'
                 ' thief in Japan. '],
            'Grand Blue':
                ['https://animego.org/anime/neobyatnyy-okean-s645',
                 'Among the seaside town of Izu\'s ocean waves and rays of shining sun, Iori Kitahara is '
                 'just beginning his freshman year at Izu University. As he moves into his uncle\'s scuba'
                 ' diving shop, Grand Blue, he eagerly anticipates his dream college life, filled with'
                 ' beautiful girls and good friends. But things don\'t exactly go according to plan. Upon'
                 ' entering the shop, he encounters a group of rowdy, naked upperclassmen, who immediately '
                 'coerce him into participating in their alcoholic activities. Though unwilling at first, '
                 'Iori quickly gives in and becomes the heart and soul of the party. Unfortunately, this '
                 'earns him the scorn of his cousin, Chisa Kotegawa, who walks in at precisely the wrong '
                 'time. Undeterred, Iori still vows to realize his ideal college life, but will things go '
                 'according to plan this time, or will his situation take yet another dive?'],
            'Dr. Stone: Stone Wars':
                ['https://animego.org/anime/doktor-stoun-kamennye-voyny-s1698',
                 'Senkuu has made it his goal to bring back two million years of human '
                 ' achievement and revive the entirety of those turned to statues. However,'
                 ' one man stands in his way: Tsukasa Shishiou, who believes that only the fittest'
                 ' of those petrified should be revived. As the snow melts and spring approaches,'
                 ' Senkuu and his allies in Ishigami Village finish the preparations for their'
                 ' attack on the Tsukasa Empire. With a reinvented cell phone model now at their '
                 'disposal, the Kingdom of Science is ready to launch its newest scheme to recruit'
                 ' the sizable numbers of Tsukasa\'s army to their side. However, it is a race'
                 ' against time; for every day the Kingdom of Science spends perfecting their'
                 ' inventions, the empire rapidly grows in number. Reuniting with old friends and'
                 ' gaining new allies, Senkuu and the Kingdom of Science must stop Tsukasa\'s '
                 'forces in order to fulfill their goal of restoring humanity and all its '
                 'creations. With the two sides each in pursuit of their ideal world, the Stone'
                 ' Wars have now begun!'],
            'One Piece':
                ['https://animego.org/anime/van-pis-s65',
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
            'Naruto':
                ['https://animego.org/anime/naruto-s102',
                 'Naruto Uzumaki, a hyperactive and knuckle-headed ninja, lives in Konohagakure, the Hidden Leaf '
                 'village. Moments prior to his birth, a huge demon known as the Kyuubi, the Nine-tailed Fox,'
                 ' attacked Konohagakure and wreaked havoc. In order to put an end to the Kyuubi\'s rampage,'
                 ' the leader of the village, the 4th Hokage, sacrificed his life and sealed the monstrous beast '
                 'inside the newborn Naruto.   Shunned because of the presence of the Kyuubi inside him, Naruto'
                 ' struggles to find his place in the village. He strives to become the Hokage of Konohagakure,'
                 ' and he meets many friends and foes along the way.'],
            'Tengen Toppa Gurren Lagann':
                ['https://animego.org/anime/gurren-lagann1-s829',
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
            'Great Teacher Onizuka':
                ['https://animego.org/anime/krutoy-uchitel-onidzuka-s556',
                 'Onizuka is a reformed biker gang leader who has his sights set on an honorable '
                 'new ambition: to become the world\'s greatest teacher... for the purpose of '
                 'meeting sexy high school girls. Okay, so he\'s mostly reformed.\n'
                 'So get ready for math that doesn\'t add up, language you\'d be slapped for '
                 'using, and biology that would make a grown man blush... unless of course, '
                 'you\'re the Great Teacher Onizuka.'],
            'Log Horizon':
                ['https://animego.org/anime/log-gorizont-s300',
                 'By its eleventh expansion pack, the massively multiplayer online role-playing game Elder'
                 ' Tale has become a global success, having a following of millions of players. However,'
                 ' during the release of its twelfth expansion pack: Novasphere Pioneers, thirty thousand'
                 ' Japanese gamers who are all logged on at the time of the update, suddenly find themselves'
                 ' transported inside the game world and donning their in-game avatars. In the midst of the '
                 'event, a socially awkward gamer called Shiroe along with his friends Naotsugu and Akatsuki'
                 ' decide to team up so that they may face this world which has now become their reality'
                 ' along with the challenges which lie ahead.'],
            'No Game No Life':
                ['https://animego.org/anime/net-igry-net-zhizni-s171',
                 'The story of No Game, No Life centers around Sora and Shiro, a brother and sister '
                 'whose reputations as brilliant NEET hikikomori gamers have spawned urban legends all'
                 ' over the Internet. These two gamers even consider the real world as just another '
                 '"crappy game." One day, they are summoned by a boy named "God" to an alternate world.'
                 ' There, God has prohibited war and declared this to be a world where "everything is'
                 ' decided by games"—even national borders. Humanity has been driven back into one '
                 'remaining city by the other races. Will Sora and Shiro, the good-for-nothing brother'
                 ' and sister, become the "Saviors of Humanity" on this alternate world? "Well, let\'s'
                 ' start playing."'],
            'Kuroko no Basket':
                ['https://animego.org/anime/basketbol-kuroko-s531',
                 ' Kuroko no Basket follows the journey of Seirin\'s players as they attempt to become'
                 ' the best Japanese high school team by winning the Interhigh Championship. To reach '
                 'their goal, they have to cross pathways with several powerful teams, some of which '
                 'have one of the five players with godlike abilities, whom Kuroko and Taiga make a'
                 ' pact to defeat.'],
            'Haikyuu!!':
                ['https://animego.org/anime/voleybol-s256',
                 'A chance event triggered Shouyou Hinata\'s love for volleyball. His club had no members,'
                 ' but somehow persevered and finally made it into its very first and final regular match of'
                 ' middle school, where it was steamrolled by Tobio Kageyama, a superstar player known as '
                 '"King of the Court." Vowing revenge, Hinata applied to the Karasuno High School volleyball '
                 'club... only to come face-to-face with his hated rival, Kageyama! A tale of hot-blooded '
                 'youth and volleyball from the pen of Haruichi Furudate!!'],
            'Shigatsu wa Kimi no Uso':
                ['https://animego.org/anime/tvoya-aprelskaya-lozh-s793',
                 'Music accompanies the path of the human metronome, the prodigious pianist'
                 ' Kousei Arima. But after the passing of his mother, Saki Arima, Kousei falls'
                 ' into a downward spiral, rendering him unable to hear the sound of his own'
                 ' piano. \n Two years later, Kousei still avoids the piano, leaving behind his'
                 ' admirers and rivals, and lives a colorless life alongside his friends Tsubaki'
                 ' Sawabe and Ryouta Watari. However, everything changes when he meets a'
                 ' beautiful violinist, Kaori Miyazono, who stirs up his world and sets him on '
                 'a journey to face music again.'],
            'Yuri!!! on Ice':
                ['https://animego.org/anime/yuri-na-ldu-s165',
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
