# --- 1. Определение ресурсов (заглушки) ---
# Фоны
image bg first_screen = "images/lvl1/main.png" 
image bg fake_site = "images/lvl1/bank.png"  
image bg final_screen = "images/lvl1/bg alise.png" 
image bg mail = "images/lvl1/mail.png"
image bg screen_for_dialogue = "images/lvl1/bg dialog.png"
image bg zvonok = "images/lvl1/zvonok.png"
image bg plachet = "images/lvl1/bg plachet.jpg"
image bg screen_kostya_govorit_po_telefonu = "images/lvl1/bg razgovor po tel.jpg"
image bg office_hall = "images/lvl2/bg_hall.png"        # Холл бизнес-центра
image bg wifi_menu = "images/lvl2/bg_wifi.png"          # Экран со списком сетей
image bg laptop_screen = "images/lvl2/bg_laptop.png"
image bg office = "images/lvl2/bg_office.png"
image bg office sad = "images/lvl2/bg_office_sad.png"
image bg time = "images/lvl2/bg_time.png"
image bg error = "images/lvl2/erorr.png"
image bg sertifikat = "images/lvl2/sertifikat.png"
image bg svoistva = "images/lvl2/svoistva.png"
image bg talk_with_woman = "images/lvl2/talk with woman.PNG"
image bg wifi otkl = "images/lvl2/wifi otkl.png"

# Персонажи
image screem = "images/lvl1/screem.png"
image volnenie = "images/lvl1/volnenie.png"
image volnenie2 = "images/lvl1/volnenie 2.png"
image zadumchivy = "images/lvl1/zadumchivy.png"

image moshenik = "images/lvl1/moshenik.png"
image zloy_moshennik = "images/lvl1/moshenik zloy.png"

image alaise = "images/lvl1/alaise_poz1.png"
image alaise2 = "images/lvl1/alaise_poz2.png"
image alaise3 = "images/lvl1/alaise_poz3.png"

image sotrudnik = "images/lvl1/sotrudnik.png"
image sotrudnik_laugh = "images/lvl1/sotrudnik_laugh.png"

image dima = "images/lvl2/dima.png"

# --- 2. Персонажи ---
define p = Character("Костя", color="ffff00")
define b = Character("Система", color="#21a038")
define m = Character("Голос в трубке", color="#ff4444")
define op = Character("Оператор банка", color="#21a038")
define g = Character("Элайза", color="#EE82EE")
define d = Character("Дима", color="#00BFFF")
define s = Character("Система", color="#21a038")
define st = Character("Сотрудник", color="#9ACD32")

# Определяем трансформацию в начале скрипта
transform kostya:
    zoom 0.8 # Уменьшить в 2 раза
    xalign 1.3 yalign 1.0

transform moshenik:
    zoom 0.85
    xalign -0.2 yalign 1.5

transform zloy_moshenik:
    zoom 0.85
    xalign -0.5 yalign 1.5

transform alaise:
    zoom 0.4

transform alaise1:
    zoom 0.37

transform sotrudnik_t:
    zoom 1.2
    xpos -100 ypos 175

# Трансформация для говорящего (стандартная яркость)
transform talk:
    matrixcolor BrightnessMatrix(0.0)
    ease 0.2 zoom 1.03

# Трансформация для слушающего (затемнение)
transform listen:
    matrixcolor BrightnessMatrix(-0.2)
    ease 0.2 zoom 1

# Проверки для условий
define ignore = False
define ignore_after_look_email = False
define good_ending = False

# --- 3. Начало игры ---

label start:
    play music "audio/In The Morning - The Grey Room _ Clark Sims.mp3"
    "Какую тему ты хочешь изучить?"

    menu:
        "Фишинг":
            jump fishing
        "Общедоступный Wi-Fi":
            jump wifi

label fishing:
    play music "audio/In The Morning - The Grey Room _ Clark Sims.mp3"
    scene bg first_screen

    "Вечер. Костя проверяет почту."
    "Среди обычных писем — уведомление с логотипом Федбанка."
    voice "audio/voice_kostya/kostya1.mp3"
    p "Так, курсач сам себя не напишет, а шортсы сами себя не полайкают. О, письмо пришло. От Федбанка? Интересно, неужели мне пришли 15 рублей кэшбэка от покупки холодильника в Эльдавидео?"

    scene bg mail
    "Тема письма: Срочно!"
    "Ваш аккаунт будет заблокирован через 24 часа."
    "В письме написано, что с карты пытаются списать 18 450 рублей."
    
    scene bg first_screen
    voice "audio/voice_kostya/kostya2.mp3"
    p "18 косарей? Да у меня на счету столько денег было только в день рождения, когда бабушка подарила на конфетки! Что за суета на ровном месте?"

    menu:
        "Немедленно нажать на кнопку":
            jump branch_click_link
            
        "Внимательно проверить адрес отправителя":
            jump branch_check_address
            
        "Позвонить в банк":
            jump branch_call_bank
            
        "Игнорировать письмо":
            $ ignore = True
            jump branch_ignore

# --- ВЕТКА 1: Работа с ссылкой ---
label branch_click_link:
    play music "audio/Twin Lynches - Density & Time.mp3" fadein 2.0
    scene bg fake_site
    voice "audio/voice_kostya/kostya3.mp3"
    p "Сначала жми, потом думай — девиз моего поколения. Опа, сайт один в один как родной. Просят номер карты, CVV и код. Типичный вторник."

    menu:
        "Ввести все данные":
            voice "audio/voice_kostya/kostya4.mp3"
            p "Номер, срок, три цифры с оборота... Готово! О, СМСка прилетела. Ха! Ну, системе-то на сайте можно доверять, это же автоматика, а не человек."
            menu:
                "Ввести код":
                    voice "audio/voice_kostya/kostya5.mp3"
                    p "Финальный аккорд! Спасаем мои честно заработанные копейки!"
                    voice "audio/voice_kostya/kostya6.mp3"
                    p "Жму «Подтвердить»... Почему в приложении уведомление: «Списание 48 000 рублей. Покупка: Крипто-Биржа-Нарния»?  Пацаны, это не рофл, где мои деньги?!"
                    scene bg plachet
                    voice "audio/voice_kostya/kostya7.mp3"
                    p "Кажется, я только что оплатил кому-то отпуск в Геленджике."
                    "Плохая концовка номер 1 — Полный доступ передан мошенникам."
                    jump educational_summary
                
                "Прочитать внимательно текст SMS":
                    voice "audio/voice_kostya/kostya8.mp3"
                    p "«Сотрудники банка не запрашивают код... Отмена перевода на 48 000 руб».  Погодите-ка! У меня на карте было всего пять тысяч и стипендия! Откуда сорок восемь?! Это же дофига! Ах вы ж..."
                    menu:
                        "Заблокировать карту":
                            voice "audio/voice_kostya/kostya9.mp3"
                            p "Фух, успел. Сердце колотится, как после литра энергетика. Больше никаких ссылок, только официальное приложение, только хардкор."
                            "Хорошая концовка номер 1 — Спасение в последний момент."
                            $ good_ending = True
                            jump educational_summary
                        "Просто закрыть сайт":
                            voice "audio/voice_kostya/kostya10.mp3"
                            p "Почему в приложении уведомление: «Списание 48 000 рублей. Покупка: Крипто-Биржа-Нарния»?  Пацаны, это не рофл, где мои деньги?!"
                            scene bg plachet
                            voice "audio/voice_kostya/kostya7.mp3"
                            p "Кажется, я только что оплатил кому-то отпуск в Геленджике."
                            "Плохая концовка номер 2 — Слишком поздно."
                            jump educational_summary

        "Ввести только номер карты":
            voice "audio/voice_kostya/kostya11.mp3"
            p "Я им только номер дам, это же безопасно, да?"
            scene bg zvonok
            "Начинают поступать подозрительные звонки."
            voice "audio/voice_kostya/kostya12.mp3"
            p "О, звонок. Номер 900? А, нет, это +7 (900) ОO0-00-01. Вместо нулей — буквы «О». Креативно, ничего не скажешь."
            menu:
                "Ответить на звонок":
                    play music "audio/Radar - The Grey Room _ Density & Time.mp3"
                    scene bg screen_for_dialogue
                    # Показываем обоих, мошенник начинает первым
                    show moshenik at moshenik, talk zorder 2
                    show zadumchivy at kostya, listen zorder 1
                    
                    voice "audio/voice_vanya/vanya1.mp3"
                    m "Вечер в хату... то есть, здравствуйте! Служба безопасности, капитан Очевидность на связи. У вас там деньги улетают в Нарнию, срочно продиктуйте код из СМС!"
                    
                    # Переключаем фокус на Костю
                    show moshenik at moshenik, listen zorder 1
                    hide zadumchivy
                    show volnenie at kostya, talk zorder 2

                    voice "audio/voice_kostya/kostya13.mp3"
                    p "Слушайте, а голос у вас такой, будто вы Волк из «Крсной шапочки» после обеда бабушкой. «Вечер в хату» — это теперь новый корпоративный стандарт?"
                    
                    # Снова фокус на мошенника
                    
                    hide moshenik
                    show volnenie at kostya, listen zorder 1
                    show zloy_moshennik at zloy_moshenik, talk zorder 2

                    voice "audio/voice_vanya/vanya2.mp3"
                    m "Слышь, умник, ты код давай, а то карту заблочим так, что даже в метро по лицу не пустят."
                    
                    # Возвращаем фокус Косте для меню выбора
                    hide volnenie
                    show zloy_moshennik at zloy_moshenik, listen zorder 1
                    show screem at kostya, talk zorder 2
                    menu:
                        "Назвать код":
                            scene bg screen_kostya_govorit_po_telefonu
                            voice "audio/voice_kostya/kostya14.mp3"
                            p "Ну, он звучит очень уверенно, почти как мой батя."
                            scene bg plachet
                            "Деньги списаны."
                            "Плохая концовка номер 3 — Социальная инженерия."
                            jump educational_summary
                        "Сбросить звонок":
                            scene bg screen_kostya_govorit_po_telefonu
                            voice "audio/voice_kostya/kostya15.mp3"
                            p "Попахивает разводом, причем очень дешевым."
                            "Карта в безопасности."
                            "Хорошая концовка номер 2 — Не попался на давление."
                            $ good_ending = True
                            jump educational_summary
                "Игнорировать":
                    $ ignore_after_look_email = True
                    jump branch_ignore
        "Закрыть сайт":
            scene bg first_screen
            voice "audio/voice_kostya/kostya16.mp3"
            p "Что-то мне подсказывает, что я творю дичь. Уходим!"
            $ ignore_after_look_email = True
            jump branch_ignore

# --- ВЕТКА 2: Проверка почты ---
label branch_check_address:
    scene bg mail
    voice "audio/voice_kostya/kostya17.mp3"
    p "Так-так-так, что тут у нас? «Срочно», «блокировка», «18 косарей»... Слишком много драмы для обычного вторника. Пора проверить «паспорт» этого спама."
    voice "audio/voice_kostya/kostya18.mp3"
    p "Смотрим на адрес... security@fedbank-support.xyz. Серьёзно? .xyz? Они бы ещё написали .narnia или ne-vzlom.com. Настоящий Федбанк скорее признает, что у них банкоматы иногда разговаривают, чем отправит письмо с такого домена."
    menu:
        "Пожаловаться на письмо как на фишинг":
            voice "audio/voice_kostya/kostya19.mp3"
            p "Отправляем этих клоунов в бан, пусть там флексят."
            voice "audio/voice_kostya/kostya20.mp3"
            p "Нажимаем кнопку «Спам», выбираем «Фишинг». Лети, голубь, в цифровой ад. Я сегодня не просто студент, я — санитар интернета. Чувствую себя как Гигачад, который спас чью-то бабушку от потери пенсии."
            "Секретная хорошая концовка — Осознанный пользователь."
            $ good_ending = True
            jump educational_summary
        "Всё равно перейти по ссылке":
            voice "audio/voice_kostya/kostya21.mp3"
            p "Ну, я же знаю, что это развод. Зайду чисто посмотреть на уровень графики. Главное — ничего не вводить, я же не мамонт..."
            jump branch_click_link
        "Удалить письмо":
            voice "audio/voice_kostya/kostya22.mp3"
            p "Ой, да идите вы в баню. Я только что открыл вкладку с прохождением Смуты, мне не до ваших драм."
            jump branch_ignore

# --- ВЕТКА 3: Официальный канал ---
label branch_call_bank:
    scene bg first_screen
    "Костя находит номер на обратной стороне карты и звоните в банк."

    scene bg dialog
    show sotrudnik at sotrudnik_t, talk zorder 2
    show zadumchivy at kostya, listen zorder 1

    voice "audio/voice_ilya/ilya1.mp3"
    op "Здравствуйте, Константин! Служба поддержки банка на связи. Чем могу, Вам, помочь?"

    show sotrudnik at sotrudnik_t, listen zorder 1
    show zadumchivy at kostya, talk zorder 2

    voice "audio/voice_kostya/kostya23.mp3"
    p "Добрый вечер! Тут мне письмо пришло, мол, я внезапно решил задонатить 18 450 рублей какому-то таинственному незнакомцу.  Скажите честно: я во сне занимаюсь благотворительностью или это кто-то хочет мои пельмени на ужин отобрать?"
    
    hide sotrudnik
    show sotrudnik_laugh at sotrudnik_t, talk zorder 2
    show zadumchivy at kostya, listen zorder 1

    voice "audio/voice_ilya/ilya2.mp3"
    op "*Смеётся* Константин, расслабьтесь. Мы проверили систему — никаких писем с требованием перейти по ссылке мы вам не отправляли.  Ваша карта в безопасности, а 18 тысяч всё ещё на месте."

    show sotrudnik_laugh at sotrudnik_t, listen zorder 1
    show zadumchivy at kostya, talk zorder 2

    voice "audio/voice_kostya/kostya24.mp3"
    p "Фух! А я уже думал, что мой аккаунт реально превратится в тыкву через 24 часа.  Вы — мой личный герой дня. Ставлю вам 10 баллов из 10 и виртуальное «спасибо»!"

    hide sotrudnik_laugh
    show sotrudnik at sotrudnik_t, talk zorder 2
    show zadumchivy at kostya, listen zorder 1

    voice "audio/voice_ilya/ilya3.mp3"
    op "Рад, Вам, помочь! Хорошего вечера!"
    "Отличная концовка — Проверил источник."
    $ good_ending = True
    jump educational_summary

# --- ВЕТКА 4: Игнорирование ---
label branch_ignore:
    scene bg first_screen
    if ignore:
        voice "audio/voice_kostya/kostya22.mp3"
        p "Ой, да идите вы в баню. Я только что открыл вкладку с прохождением Смуты, мне не до ваших драм."
    if ignore_after_look_email:
        play music "audio/In The Morning - The Grey Room _ Clark Sims.mp3" fadein 2.0
    "Через сутки приходит второе письмо: Ваш аккаунт заблокирован."
    voice "audio/voice_kostya/kostya25.mp3"
    p "Ого, ставки растут! Теперь я официально заблокирован. Это что, получается, я теперь цифровой изгой? А как же мой заказ на маркетплейсе? Как же подписка на музыку? Паника — мой компас земной, кажется, пора что-то делать!"
    menu:
        "Теперь перейти по ссылке":
            voice "audio/voice_kostya/kostya26.mp3"
            p "Всё, я сломался! Жму! Лишь бы карточка работала, а то как я буду за шаурму платить?"
            jump branch_click_link
        "Зайти в официальное приложение банка":
            voice "audio/voice_kostya/kostya27.mp3"
            p "Так, глубокий вдох. Открываем официальное приложение Федбанка. Палец на сканер... И-и-и... Барабанная дробь! В приложении всё в порядке."
            "Хорошая концовка номер 3 — Спокойствие спасает."
            $ good_ending = True
            jump educational_summary

# --- ОБРАЗОВАТЕЛЬНЫЙ БЛОК ---
label educational_summary:
    play music "audio/Ghibli Station - The Mini Vandals.mp3"
    scene bg final_screen
    show alaise at talk, center, alaise
    if good_ending:
        g "Ну что, дорогуша, как прошли твои цифровые приключения? Надеюсь, ты еще при деньгах и с целыми нервами!"
    else:
        g "Ну что, дорогуша, как прошли твои цифровые приключения? Тебе стоило бы действовать осторожнее!"
    hide alaise
    show alaise2 at talk, center, alaise1
    g "Позволь мне, твоей верной наставнице, разобрать этот хаос по полочкам. Мошенники — те еще драматические актеры, но мы-то с тобой зрители искушенные, верно?  Чтобы в следующий раз они ушли со сцены под свист, запомни эти золотые правила:"
    hide alaise2
    show alaise3 at talk, center, alaise1
    g "1. Тише едешь — деньги будут! Заметил, как они кричали: «СРОЧНО!»? Это их любимый трюк, чтобы ты отключил мозг и включил панику."
    hide alaise3
    show alaise at talk, center, alaise
    g "2. Смотри в «паспорт» письма. Если адрес отправителя похож на винегрет из букв вроде .xyz или fed-security-verify.com — это фальшивка. Настоящий банк не прячется за странными доменами."
    hide alaise
    show alaise2 at talk, center, alaise1
    g "3. Твои секреты — только твои. Запомни как мантру: сотрудники банка никогда, слышишь, никогда не спросят твой CVV или код из SMS. Если просят — смело жми «отбой»."
    hide alaise2
    show alaise3 at talk, center, alaise1
    g "4. Официальный путь — самый короткий. Сомневаешься? Не тыкай в подозрительные кнопки. Просто зайди в официальное приложение или набери номер с оборота своей карты. Это всегда работает безотказно!"
    hide alaise3
    show alaise at talk, center, alaise
    g "Ну что, теперь ты чувствуешь себя чуть-чуть кибер-гением?  Не расслабляйся, впереди еще много интересного!"
    return

default wifi_score = 0 # 0 - плохо, 1 - средне, 2 - отлично

# --- 4. Общедоступный wifi ---
label wifi:
    play music "audio/In The Morning - The Grey Room _ Clark Sims.mp3" fadein 2.0
    scene bg office_hall
    
    d "Так… спокойно. Сегодня я либо получаю работу… либо получаю новый опыт под названием «как не надо ходить на собеседования»."
    
    scene bg time
    "Дима смотрит на часы."
    d "20 минут. Времени вроде много… но если я сейчас сяду в TikTok — всё, можно сразу идти домой."
    
    scene bg office
    "Садится, достаёт ноутбук."
    d "Так, презентация… где ты…"
    
    d "…а где интернет?"
    
    scene bg wifi_menu
    d "О, три сети. Классика жанра."
    
    menu:
        "BusinessCenter_Free":
            jump branch_open_wifi
            
        "BC_Guest_WPA2":
            jump branch_secure_wifi
            
        "BusinessCenter_5G_Free":
            jump branch_fake_wifi

# --- ВЕТКА 2А: Открытая сеть ---
label branch_open_wifi:
    d "Ого. Ни пароля, ни вопросов… даже мама так быстро не пускает домой."
    d "Ладно, времени мало. Погнали."
    
    scene bg laptop_screen
    "Дима открывает облако."
    s "Введите логин и пароль..."
    
    menu:
        "Ввести данные":
            d "Ну а что тут может пойти не так? Я же просто зайду…"
            "Через пару секунд на телефон падает уведомление."
            s "Вход выполнен с нового устройства."
            d "…подождите. Это что за второе я? Я вроде один пришёл…"
            
            menu:
                "Игнорировать":
                    d "Да ну, баг какой-то. Сейчас всё само пройдёт."
                    "..."
                    d "Если игнорировать проблемы — они же исчезают, да? Да?.."
                    s "Внимание: Подозрительная активность."
                    d "Ну вот. Проблема не исчезла. Она прокачалась."
                    $ wifi_score = 0
                    jump educational_summary2
                
                "Сменить пароль":
                    d "Так, без паники. Я взрослый человек… сейчас что-нибудь нажму правильно."
                    "Лихорадочно меняет пароль через мобильный интернет."
                    d "Фух. Сердце бьётся как будто я не пароль меняю, а экзамен сдаю."
                    $ wifi_score = 1
                    jump educational_summary2
                    
                "Отключить Wi-Fi":
                    d "Нет, стоп. Мне это не нравится."
                    "Выключает Wi-Fi."
                    d "Так… а если уже поздно?.."
                    $ wifi_score = 1
                    jump educational_summary2

        "Проверить сайт":
            d "Так, секунду. Я вообще куда захожу?"
            d "Так… это что за домен? Это не выглядит как нормальный сайт."
            d "Это больше похоже на 'my-real-bank-no-scam.ru'"
            
            menu:
                "Всё равно войти":
                    d "Ладно, может я просто параноик…"
                    $ wifi_score = 0
                    jump educational_summary2
                
                "Не вводить данные":
                    d "Не, спасибо. Я ещё пожить хочу спокойно."
                    jump branch_secure_wifi # Возвращаем к выбору безопасной сети

# --- ВЕТКА 2Б: Безопасная сеть ---
label branch_secure_wifi:
    "Дима подошел спросить пароль от Wi-Fi"
    scene bg talk_with_woman
    d "Пароль есть — уже плюс. Значит, не совсем дикий запад."
    
    menu:
        "Сразу зайти в облако":
            d "Да всё нормально, не первый день в интернете."
            "Работает. Значит всё ок… наверное."
            $ wifi_score = 1
            jump educational_summary2
            
        "Проверить наличие HTTPS":
            d "Так, замочек есть… https на месте…"
            d "Вот теперь я спокоен. Даже немного горжусь собой."
            $ wifi_score = 2
            jump educational_summary2
            
        "Использовать мобильный интернет":
            d "Знаешь что… я не настолько доверяю этому месту."
            d "Медленно, зато спокойно. Как бабушка в очереди — но надёжно."
            $ wifi_score = 2
            $ good_ending = True
            jump educational_summary2

# --- ВЕТКА 2В: Фальшивая сеть ---
label branch_fake_wifi:
    d "Сигнал идеальный… слишком идеальный."
    scene bg laptop_screen
    s "Для доступа к интернету скачайте и установите сертификат безопасности."
    
    menu:
        "Скачать сертификат":
            scene bg sertifikat
            d "Ну ладно… попробую."
            scene bg error
            "Устройство начинает тормозить. Появляются странные окна."
            scene bg_office_sad
            d "Так… это было плохое решение. Очень плохое. Прямо как мои решения в 3 ночи."
            $ wifi_score = 0
            jump educational_summary2
            
        "Спросить сотрудника":
            scene bg talk_with_woman
            st "Такой сети у нас нет. Рекомендую использовать BC_Guest_WPA2."
            d "Ну всё ясно. Бесплатный сыр найден."
            jump branch_secure_wifi

# --- ФИНАЛ — ОБУЧЕНИЕ ---
label educational_summary2:
    play music "audio/Ghibli Station - The Mini Vandals.mp3"
    scene bg final_screen
    
    if wifi_score == 0:
        show alaise at talk, center, alaise
        g "Ну что, Дима… ты сейчас прошёл экспресс-курс «Как потерять данные за 10 минут»."
        g "Но не переживай. Все через это проходят… один раз. Ну максимум два."
    
    elif wifi_score == 1:
        show alaise at talk, center, alaise
        g "Ну… было пару опасных моментов, Дима. Но ты хотя бы вовремя остановился. Это уже половина успеха."
        
    else:
        show alaise at talk, center, alaise
        g "О, да ты осторожный! Мне нравится. Таких пользователей мошенники обычно обходят стороной."

    hide alaise
    show alaise2 at talk, center, alaise1
    g "Запомни правила выживания в открытых сетях:"
    hide alaise2
    show alaise3 at talk, center, alaise
    g "1. Открытый Wi-Fi — это проходной двор. Любой в этой сети может попытаться «подсмотреть» твой трафик."
    hide alaise3
    show alaise at talk, center, alaise
    g "2. Никогда не скачивай «сертификаты» или «обновления» для подключения к Wi-Fi. Это прямой путь для вируса."
    hide alaise
    show alaise2 at talk, center, alaise1
    g "3. Если нужно зайти в банк или почту — лучше раздай интернет с телефона. Это в сто раз безопаснее."
    hide alaise2
    show alaise3 at talk, center, alaise
    g "И главное — если что-то кажется подозрительным…"
    
    d "…то это не паранойя?"
    
    hide alaise3
    show alaise at talk, center, alaise
    g "Нет. Это здравый смысл!"
    
    return