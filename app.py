import random
import pandas as pd
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.platform import *
from pywebio.session import *
import time
import openai
from datetime import datetime
from pywebio_battery import *

Key_room = []
Key_toClear = [0]
picc = open('url.txt', 'r').read()
countt_of_rom_list = [22322, 23454, 3454]
fix_url_pic_f = picc.split('\n')
compcss = '''

.form-control
{
  -webkit-box-sizing: content-box;
  -moz-box-sizing: content-box;
  box-sizing: content-box;
  width: 120px;
  height: 9px;
  margin: auto;
  padding: 10px 20px;
  overflow: scroll;
  border: 2px dashed #ff7a89;
  -webkit-border-radius: 2px;
  border-radius: 39px;
  font: normal normal bold 11px/normal "Comic Sans MS", cursive, sans-serif;
  color: rgba(0,0,0,1);
  text-align: center;
  -o-text-overflow: clip;
  text-overflow: clip;
  letter-spacing: 1px;
  white-space: pre-line;
  background: rgba(252,252,252,1);
  -webkit-box-shadow: 4px 9px 9px 0 rgba(0,0,0,0.2) ;
  box-shadow: 4px 9px 9px 0 rgba(0,0,0,0.2) ;
  text-shadow: 4px 6px 0 rgba(255,255,255,0.66) ;
  -webkit-transition: all 201ms cubic-bezier(0.42, 0, 0.58, 1);
  -moz-transition: all 201ms cubic-bezier(0.42, 0, 0.58, 1);
  -o-transition: all 201ms cubic-bezier(0.42, 0, 0.58, 1);
  transition: all 201ms cubic-bezier(0.42, 0, 0.58, 1);
  -webkit-transform: rotateX(-4.4377467708deg) rotateY(-1.1459155902616465deg)   ;
  transform: rotateX(-4.4377467708deg) rotateY(-1.1459155902616465deg)   ;
  -webkit-transform-origin: 49% 50% 0;
  transform-origin: 49% 50% 0;
}

.webio-scrollable {
border-radius: 30px;
''' + f'''
background-image:
                  url({str(random.choice(fix_url_pic_f))});
background-position: 25% 50%;
box-shadow: inset 0 0 6px rgba(0,0,0,0.5);
''' + '}'


#######################$$$$########################


now = datetime.now()
###################################################################
athouey = ''  # Do Not Play With this var Will Cross The Lop Hestory
##################################################################
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

tet_file = open('ai.txt', 'a', encoding='utf-8')

Ai_answer_Hestory = ['AI: Im Smart MoiBot \n How Can I Help You ']

Ai_answer_Hestory.clear()

Ai_answer_Hestory.append('AI: Im Smart MoiBot \n How Can I Help You ')

AI_answer_nlp = ['  Translate ']

AI_answer_nlp.clear()

AI_answer_nlp.append('  Translate  ')

AI_answer_gramer = ['do ti']

AI_answer_gramer.clear()
AI_answer_gramer.append('do ti')

chat_style = d = '''.chat {
                                        display: flex;
                                        flex-direction: column;
                                        justify-content: center;
                                        align-items: flex-start;
                                        list-style-type: none;
                                        padding: 0;
                                        margin: 0;
                                       }
                                       .message {
                                        background-color: rgba(255, 255, 255, 0.9);
                                        border-radius: 50px;
                                        box-shadow: 0px 15px 5px 0px rgba(0,0,0,0.5);
                                        position: relative;
                                        margin-bottom: 30px;
                                       }
                                       .message.left {
                                        padding: 15px 20px 15px 70px;
                                       }
                                       .message.right {
                                        align-self: flex-end;
                                        padding: 15px 70px 15px 20px;
                                       }
                                       .logo {
                                        border-radius: 50%;
                                        box-shadow: 0px 10px 10px 0px rgba(0,0,0,0.7);
                                        object-fit: cover;
                                        position: absolute;
                                        left: 10px;
                                        top: -10px;
                                        width: 50px;
                                        height: 50px;
                                       }
                                       .message.right .logo {
                                        left: auto;
                                        right: 10px;
                                       }
                                       .message p {
                                        margin: 0;
                                       }'''
fir = 'sk-1YarzJpmgJAvj5Fwm9H'
sc = 'PT3BlbkFJBzEe11JamrLJM1RNVQIj'
openai.api_key = fir + sc
start_sequence = "\nAI: "
restart_sequence = "\nHuman: "
prompt_gbt = """The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\n
        Human: hello\n
        AI: I am an AI created by Moieis brain. How can I help you today?\n
        Human: What date you was created?\n
        AI: As Me As My Creator 2002\n
        Human: Were are you?\n
        AI: Netherlands With My Creators\n
        Human: who are you \n
        AI: I was created to assist you with any tasks or questions you may have. Is there something specific you need help with?\n
        Human: where are you from?\n
        AI: My physical location is in Moieis brain, as Im in the cloud for more about my creator you can vist on https://znap.link/MoiCbio\n
        Human: 
        """

Lan_iso_Name_Options = """Afar
        Abkhazian
        Avestan
        Afrikaans
        Akan
        Amharic
        Aragonese
        Arabic
        Assamese
        Avaric
        Aymara
        Azerbaijani
        Bashkir
        Belarusian
        Bulgarian
        Bihari languages
        Bambara
        Bislama
        Bengali
        Tibetan
        Breton
        Bosnian
        Catalan
        Valencian
        Chechen
        Chamorro
        Corsican
        Cree
        Czech
        Church Slavic
        Old Slavonic
        Church Slavonic
        Old Bulgarian
        Old Church Slavonic 
        Chuvash
        Welsh
        Danish
        German
        Divehi
        Dhivehi
        Maldivian
        Dzongkha
        Ewe
        Greek, Modern (1453-)
        English
        Esperanto
        Spanish
        Castilian
        Estonian
        Basque
        Persian
        Fulah
        Finnish
        Fijian
        Faroese
        French
        Western Frisian
        Irish
        Gaelic
        Scottish Gaelic
        Galician
        Guarani
        Gujarati
        Manx
        Hausa
        Hebrew
        Hindi
        Hiri Motu
        Croatian
        Haitian 
        Haitian Creole
        Hungarian
        Armenian
        Herero
        Interlingua (International Auxiliary Language Association)
        Indonesian
        Interlingue
        Occidental
        Igbo
        Sichuan Yi
        Nuosu
        Inupiaq
        Ido
        Icelandic
        Italian
        Inuktitut
        Japanese
        Javanese
        Georgian
        Kongo
        Kikuyu 
        Gikuyu
        Kuanyama 
        Kazakh
        Kalaallisut
        Greenlandic
        Central Khmer
        Kannada
        Korean
        Kanuri
        Kashmiri
        Kurdish
        Komi
        Cornish
        Kirghiz
        Kyrgyz
        Latin
        Luxembourgish
        Letzeburgesch
        Ganda
        Limburgan 
        Limburger
        Limburgish
        Lingala
        Lao
        Lithuanian
        Luba-Katanga
        Latvian
        Malagasy
        Marshallese
        Maori
        Macedonian
        Malayalam
        Mongolian
        Marathi
        Malay
        Maltese
        Burmese
        Nauru
        Bokmål 
        Ndebele
        North Ndebele
        Nepali
        Ndonga
        Dutch
        Flemish
        Norwegian 
        Nynorsk
        Norwegian
        Norwegian
        Ndebele
        South
        South Ndebele
        Navajo
        Navaho
        Chichewa
        Chewa
        Nyanja
        Occitan 
        Ojibwa
        Oromo
        Oriya
        Ossetian
        Ossetic
        Panjabi
        Pali
        Polish
        Pushto
        Portuguese
        Quechua
        Romansh
        Rundi
        Romanian 
        Moldavian
        Moldovan
        Russian
        Kinyarwanda
        Sanskrit
        Sardinian
        Sindhi
        Northern Sami
        Sango
        Sinhala; Sinhalese
        Slovak
        Slovenian
        Samoan
        Shona
        Somali
        Albanian
        Serbian
        Swati
        Sotho, Southern
        Sundanese
        Swedish
        Swahili
        Tamil
        Telugu
        Tajik
        Thai
        Tigrinya
        Turkmen
        Tagalog
        Tswana
        Tonga (Tonga Islands)
        Turkish
        Tsonga
        Tatar
        Twi
        Tahitian
        Uighur; Uyghur
        Ukrainian
        Urdu
        Uzbek
        Venda
        Vietnamese
        Volapük
        Walloon
        Wolof
        Xhosa
        Yiddish
        Yoruba
        Zhuang
        Chuang
        Chinese
        Zulu
        """.split('\n')
####################################
###################################
###########$$$$$####################

holy_conv = ["""The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\n
        Human: hello\n
        AI: I am an AI created by Moieis brain. How can I help you today?\n
        Human: What date you was created?\n
        AI: As Me As My Creator 2002\n
        Human: Were are you?\n
        AI: Netherlands With My Creators\n
        Human: who are you \n
        AI: I was created to assist you with any tasks or questions you may have. Is there something specific you need help with?\n
        Human: where are you from?\n
        AI: My physical location is in Moieis brain, as Im in the cloud for more about my creator you can vist on https://znap.link/MoiCbio\n
        Human: 
        """]

holy_conv.clear()
holy_conv.append(prompt_gbt)
time_pross = [1]

############$$$$$##################
##################################
###################################

############################################### config css do not play here #########################################
cssfi = open('ase.css', 'r').read()
csss = open('firstpage.css', 'r').read()
moidfa_csss = open('moidfa.css', 'r').read()
moipiccdc = open('moipicc.css', 'r', encoding='utf8').read()

ai_h_Conv = {'ai': [0], 'you': [None]}
ai_h_Conv['ai'].clear()
ai_h_Conv['you'].clear()
############################################Do Not Play Here################################################
Key_room.clear()
Key_room.append(0)
ai_h_Conv['ai'].append(1)

########################################key of retrn #############################################
def mypininfodfu():
    if get_localstorage(key='fromw') != 'dfu':
        mypin('dfu')
        logo(5)
        time.sleep(2)
        toast('its in your pin now enjoy',color='info')
        time.sleep(2)
        toast('you can accses it fast from MYPIN Loopy page', color='warn')

    else:
        pinconf=confirm('Remove Pin !','You Have Been Pin It U Sure Wanna Remove It !')
        if pinconf == True:
            logo(4)
            toast('We H ave Remove It Done (: ', color='error')
            set_localstorage(key='fromw',value='None')




def mypin(wloc):

    set_localstorage(key='fromw',value=wloc)
######################################logice guiss fix####################################
def logo(sec: int):  # --> section on change logo
    if sec == 1:
        with use_scope(name='logoo', clear=True):
            put_grid([[None, None, None,
                       put_image('https://s9.gifyu.com/images/a5a25d4df2619524f.gif', width='150', height='150'),
                       None,
                       None, None]])
    if sec == 2:
        with use_scope(name='logoo', clear=True):
            put_grid([[None, None, None,
                       put_image('https://s9.gifyu.com/images/a5a25d4df2619524f.gif', width='150', height='150'),
                       None,
                       None, None]])  # second
    if sec == 3:
        with use_scope(name='logoo', clear=True):
            put_grid(
                [[None, None, None, put_image('https://s9.gifyu.com/images/massg.gif', width='150', height='150'),
                  None, None]])  # this when send 3   # Logo

    if sec == 4:
        with use_scope(name='logoo', clear=True):
            put_grid(
                [[None, None, None, put_image('https://s9.gifyu.com/images/massg.gif', width='150', height='150'),
                  None, put_html('''<img width="37" height="37" src="https://img.icons8.com/emoji/48/pushpin-emoji.png" alt="pushpin-emoji"/>''').onclick(mypininfodfu)]])
    if sec == 5:
        if get_localstorage(key='fromw') == 'dfu':
            with use_scope(name='logoo', clear=True):
                     put_grid(
                [[None, None, None, put_image('https://s9.gifyu.com/images/massg.gif', width='150', height='150'),
                  None, put_html('''<img width="37" height="37" src="https://img.icons8.com/emoji/48/round-pushpin-emoji.png" alt="round-pushpin-emoji"/>''').onclick(mypininfodfu)]])
        else:
            with use_scope(name='logoo', clear=True):
                put_grid(
                    [[None, None, None, put_image('https://s9.gifyu.com/images/massg.gif', width='150', height='150'),
                      None, put_html(
                            '''<img width="37" height="37" src="https://img.icons8.com/emoji/48/pushpin-emoji.png" alt="pushpin-emoji"/>''').onclick(
                            mypininfodfu)]])


def logout():
    To_Know_The_Celint = set_localstorage(key='moiiforutest', value='None')
    toast('logging out', color='#454449')
    go_app('firstrunmoi', new_window=False)

def moipiccc():
    popup('for any issue with no action :',
          put_grid([[put_html('<h4>!!If your browser not supported auto trans!!</h4>')],
                    [put_html('<h4>press in this link -></h4>'), put_link(name='MoiPic',
                                                                          url='https://moi.onrender.com/?app=moipic',
                                                                          new_window=False)]]))
    go_app('moipic', new_window=False)

@config(title='info', css_style=csss)
def togather():

    def moire():
        To_Know_user = get_localstorage(key='moiusename')

        if pin.name or pin.email or pin.words == '':
            with use_scope(name='inf', clear=True):
                put_html(f'''
                             <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                              <h3>⠀⠀⠀⠀⠀⠀</h3>
                               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>






                            <h3><span>! Thanks {To_Know_user} We Got it !</span></h3>''')

            time.sleep(4)

            with use_scope(name='inf', clear=True):
                put_html(f'''
                             <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                              <h3>⠀⠀⠀⠀⠀⠀</h3>
                               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>






                            <h3><span>back To MoiAi</span>
                            <span>.</span>
                            <span>.</span>
                            <span>.</span></h3>''')

                k = open('allthereport.txt', 'a', encoding='utf8')
                k.write(f"=============={To_Know_user}==============\n"
                        f"\n"
                        f"        {pin.woords}"
                        f"\n"
                        f"===========================================")
                time.sleep(2)
                go_app('index', new_window=False)

        else:
            toast('please fill all the inputs !', color='error')

    with use_scope(name='inf', clear=True):
        put_html('''
             <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
              <h3>⠀⠀⠀⠀⠀⠀</h3>
               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>






            <h3><span>Before</span>
            <span>Everything</span></h3>''')
    time.sleep(3)

    with use_scope(name='inf', clear=True):
        put_html('''
             <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
              <h3>⠀⠀⠀⠀⠀⠀</h3>
               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>






            <h3><span>We receive</span>
                    <span>and accept</span>
                    <span>all your opinions|advice|bugs </span>
                    <span>and we value &</span>
                    <span>appreciate every detail that you</span>
                    <span>direct us to .</span>
                    <span>.</span>
                    <span>.</span>
                    <span>.</span>
                    <span>.</span></h3>''')

    time.sleep(2)

    with use_scope(name='inf', clear=True):
        put_html('''
             <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
              <h3>⠀⠀⠀⠀⠀⠀</h3>
               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
               <h3><span>We receive</span>
                    <span>and accept</span>
                    <span>all your opinions|advice|bugs </span>
                    <span>and we value &</span>
                    <span>appreciate every detail that you</span>
                    <span>direct us to .</span>
                    <span>.</span>
                    <span>.</span>
                    <span>.</span>
                    <span>.</span></h3>

            <h3><span>Your name :</span></h3>''')

        put_input('name', type=TEXT, value='')

        put_html('<h3><span>Your Email :</span></h3>')

        put_input('email', type=TEXT, value='')

        put_html('<h3><span>Your Words :</span></h3>')
        put_input('woords', type=TEXT, value='')
        put_html('<hr>')
        put_grid([[None, None, None, put_button('To MoiReport', onclick=moire, ), None, None]])

###############################logice guiss fix and clint staff ##########################

def interv():
    set_env(title='MoiIdea', auto_scroll_bottom=True, input_auto_focus=True, input_panel_min_height=500,
            output_max_width='100%')

    y = ['']
    y.clear()
    val = []

    def requ_inter():
        with use_scope(name='down', clear=True):
            put_grid([[None, None, None,
                       put_button('Next', disabled=True, onclick=None, small=True, color='info', outline=True),
                       put_button('Back', disabled=True, color='dark', small=True, onclick=interv, outline=True),
                       None, None, None]])
        toast('Let me think for you !!', color='#00ffd5')
        val.append(pin.tinm)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Create a list of {val[-1]} questions for my interview with {val[-2]}?",
            temperature=0.5,
            max_tokens=182,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        print(val[-1])
        print(val[-2])
        val.clear()
        return y.append(response.choices[0].text)

    def next():
        val.append(pin.secc)

        def fain():
            if pin.tinm <= 15:
                requ_inter()

                with use_scope('title', clear=True):
                    put_grid([[None, put_html(
                      '<img width="55" height="55" src="https://img.icons8.com/color/96/new-job.png" alt="new-job"/>'), None, put_html('<h3>focus !!</h3>'), None, None]])
                    put_html(''' <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>

        ''')
                with use_scope(name='main', clear=True):
                    put_grid([[None, None, None, put_textarea(name='val', value=y[-1]), None, None, None]])
                    put_html('<hr>')
                with use_scope(name='down', clear=True):
                    put_grid(
                        [[None, None, None,
                          put_button('Back To field of specialization ', small=True, onclick=interv, color='info',
                                     outline=True),
                          put_button('Back To MoiDfa', color='success', onclick=moidfa, small=True, outline=True),
                          None, None]])

            else:
                toast('must be less then 16 Q', color='warn')

        with use_scope(name='main', clear=True):

            put_grid([[None, None, None,
                       put_input(name='tinm', label='how many questions You want :', type=NUMBER, value=10), None,
                       None, None]])

            put_html('<hr>')
        with use_scope(name='down', clear=True):
            put_grid([[None, None, None, put_button('Next', onclick=fain, small=True, color='info', outline=True),
                       put_button('Back', color='dark', small=True, onclick=interv, outline=True),
                       None, None, None]])

    with use_scope(name='title', clear=True):

        put_grid(
            [[None, None, put_html(
                      '<img width=50" height="50" src="https://img.icons8.com/color/96/new-job.png" alt="new-job"/>'), None, put_html('<h5>Create interview questions by MoiAi</h5>'), None, None,
              None]])

        put_html('<hr>')
    with use_scope(name='main', clear=True):

        put_grid([[None, None, None,
                   put_input(name='secc', label='your field of specialization :', value='data science',
                             placeholder='data science')
                      , None, None, None]])
        put_html('<hr>')

    with use_scope(name='down', clear=True):
        put_grid([[None, None, None, None, put_button('Next', onclick=next, color='info', outline=True),
                   put_button('Back', color='dark', onclick=moidfa, outline=True),
                   None, None, None]])

def study_note():
    set_env(title='MoiNotes', auto_scroll_bottom=True, input_auto_focus=True, input_panel_min_height=500,
            output_max_width='100%')

    y = ['']
    y.clear()
    val = []

    def requ_inter():
        with use_scope(name='down', clear=True):
            put_grid([[None, None, None,
                       put_button('Next', disabled=True, onclick=None, small=True, color='info', outline=True),
                       put_button('Back', disabled=True, color='dark', small=True, onclick=interv, outline=True),
                       None, None]])

        toast('Let me think for you !!', color='#00ffd5')
        val.append(pin.tinm)
        print(y)

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=F"What are {val[-1]} key points I should know when studying {val[-2]}?",
            temperature=0.3,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        try:
            date = open('moinotes.txt', 'a')
            date.write(f'----------{info}----------\n')
            date.write(f'============{val[-1]}============\n')
            date.write(f'============{val[-2]}============\n')
            date.close()

        except:
            daoooo = open('moinotes.txt', 'a', encoding='utf-8')
            daoooo.write(f'----------{info}----------\n')
            daoooo.write(f'============{val[-1]}============\n')
            daoooo.write(f'============{val[-2]}============\n')
            daoooo.close()

        val.clear()
        return y.append(response.choices[0].text)

    def next():
        val.append(pin.secc)

        def fain():
            if pin.tinm <= 15:
                requ_inter()

                with use_scope('title', clear=True):
                    put_grid([[None, put_html(
                      '<img width="55" height="55" src="https://img.icons8.com/emoji/48/books-emoji.png" alt="books-emoji"/>'), None, put_html(f'''Here is the result :'''), None, None]])
                    put_html('<hr>')
                with use_scope(name='main', clear=True):

                    put_grid([[None, None, None, put_textarea(name='val', value=y[-1],readonly=True), None, None, None]])
                    put_html('<hr>')
                with use_scope(name='down', clear=True):

                    put_grid(
                        [[None, None, None,
                          put_button('Return to the field of study ', small=True, onclick=study_note, color='info',
                                     outline=True),
                          put_button('Back To MoiDfa', color='success', small=True, onclick=moidfa, outline=True),
                          None, None]])


            else:
                toast('must be less then 16 ', color='warn')

        with use_scope(name='main', clear=True):

            put_grid([[None, None, None,
                       put_input(name='tinm', label='how many key point You want :', type=NUMBER, value=10), None,
                       None,
                       None]])

            put_html('<hr>')

        with use_scope(name='down', clear=True):
            put_grid([[None, None, None, put_button('Next', onclick=fain, small=True, color='info', outline=True),
                       put_button('Back', color='dark', small=True, onclick=study_note, outline=True),
                       None, None]])

    with use_scope(name='title', clear=True):

        put_grid(
            [[None, None, put_html(
                      '<img width="50" height="50" src="https://img.icons8.com/emoji/48/books-emoji.png" alt="books-emoji"/>'), None, put_html('<h5>Create study notes by MoiAi</h5>'), None, None, None]])
        put_html('<hr>')
    with use_scope(name='main', clear=True):

        put_grid([[None, None, None,
                   put_input(name='secc', label='your field of study :', value='data science',
                             placeholder='data science')
                      , None, None, None]])
        put_html('<hr>')
    with use_scope(name='down', clear=True):
        put_grid([[None, None, None, None, put_button('Next', onclick=next, small=True, color='info', outline=True),
                   put_button('Back', color='dark', small=True, onclick=moidfa, outline=True),
                   None, None, None]])

def js_py():
    set_env(title='MoiJsPy', auto_scroll_bottom=True, input_auto_focus=True, input_panel_min_height=500,
            output_max_width='100%')

    from_lng = ['python']
    from_lng.clear()
    to_lng = ['javascript']
    to_lng.clear()
    y = ['']
    y.clear()
    from_cot = [' print("hi") ']
    from_cot.clear()

    def req_codtr():
        response = openai.Completion.create(
            model="code-davinci-002",
            prompt=f"##### Translate this function  from {from_lng[-1]} into {to_lng[-1]}\n### {from_lng[-1]}\n    \n {from_cot[-1]}\n    \n### {to_lng[-1]}"
            , temperature=0,
            max_tokens=54,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["###"]

        )
        return y.append(response.choices[0].text)

    def do_it():

        if pin.fro_inp != pin.to_inp:
            def mor_do():
                with use_scope(name='down', clear=True):
                    put_html('<hr>')
                    put_grid([[None, None, None,
                               put_button('Translate', small=True, disabled=True, onclick=mor_do, color='info',
                                          outline=True),
                               put_button('Back', color='dark', onclick=js_py, outline=True, small=True,
                                          disabled=True), None, None]])

                from_cot.append(pin.from_prg_lng)

                req_codtr()
                pin_update('rr', value=y[-1])
                data_nl = open('programtrans.txt', 'a', encoding='utf-8')
                data_nl.write(f"this time ---> {str(dt_string)}\n"
                              f"this request ---> {str(y[-1])}<----------\n"
                              f"_________________________________________________________\n")
                data_nl.close()
                with use_scope(name='down', clear=True):
                    put_html('<hr>')
                    put_grid([[None, None, None,
                               put_button('Translate', small=True, onclick=mor_do, color='info', outline=True),
                               put_button('Back', color='dark', onclick=js_py, outline=True, small=True,
                                          disabled=False), None, None]])

            name_pinfrom_here = ['nov']
            name_pinfrom_here.clear()
            name_pinto_here = ['nov']
            name_pinto_here.clear()
            example = [
                '###########Example###########\n#Python\n    \n    def predict_proba(X: Iterable[str]):\n        return np.array([predict_one_probas(tweet) for tweet in X])\n ',
                '###########Example###########\n#js\n    \n    function predict_proba(X) {\n        return X.map(predict_one_probas);\n    }\n    \n']
            name_pinfrom_here.append(pin.fro_inp)
            name_pinto_here.append(pin.to_inp)
            from_lng.append(name_pinfrom_here)
            to_lng.append(name_pinto_here)

            with use_scope(name='title', clear=True):

                put_grid(
                    [[None, put_html(
                      '<img width="55" height="55" src="https://img.icons8.com/arcade/64/python.png" alt="python"/>'), None, put_html('<h3>Translate programming languages By MoiAi</h3>'), None, None,
                      None]])
                put_html('<hr>')
            with use_scope(name='main', clear=True):
                put_grid([[None, put_textarea('from_prg_lng', value=example[0],
                                              label=f'Put Your {name_pinfrom_here[-1]} Code :', code={
                        'mode': f"{name_pinfrom_here[-1]}",
                        'theme': 'darcula'
                    }), None]])
                put_html('<hr>')
                put_grid([[None, put_textarea(name='rr', label=f'To {name_pinto_here[-1]} Code !', value=example[1],
                                              code={
                                                  'mode': f"{name_pinto_here[-1]}",
                                                  'theme': 'darcula'
                                              }, readonly=True), None]])

            # print(pin.from_prg_lng)

            with use_scope(name='down', clear=True):
                put_html('<hr>')
                put_grid([[None, None, None,
                           put_button('Translate', small=True, onclick=mor_do, color='info', outline=True),
                           put_button('Back', color='dark', onclick=js_py, outline=True, small=True), None, None]])

        else:
            toast("It shouldn't be the same !", color='warn')

    # req_gramer()
    # print(y[-1])
    with use_scope(name='title', clear=True):

        put_grid([[None, put_html(
                      '<img width="60" height="60" src="https://img.icons8.com/arcade/64/python.png" alt="python"/>'), None, put_html('<h3>Translate programming languages By MoiAi</h3>'), None, None]])
        put_html('<hr>')
    with use_scope(name='main', clear=True):

        put_grid([[None, put_select('fro_inp', label='From Lang :', options=['js', 'python']), None,
                   put_select('to_inp', label='To Lang :', options=['js', 'python']), None]])

    with use_scope(name='down', clear=True):
        put_html('<hr>')
        put_grid([[None, None, None, put_button('Next', small=True, onclick=do_it, color='info'),
                   put_button('Back', color='dark', small=True, onclick=moidfa), None, None, None]])

def python_fix():
    set_env(title='MoiPyFix', auto_scroll_bottom=True, input_auto_focus=True, input_panel_min_height=500,
            output_max_width='100%')

    y = [""]
    y.clear()
    bugss = ['']
    bugss.clear()
    fixed = ['']
    fixed.clear()

    def get_valu():
        response = openai.Completion.create(
            model="code-davinci-002",
            prompt=f"###{bugss[-1]}   \n\n ### Fixed Python{fixed[-1]}",
            temperature=0,
            max_tokens=182,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["###"]
        )
        return y.append(response.choices[0].text)

    def mor_do():
        with use_scope(name='down', clear=True):
            put_html('''<hr>''')
            put_grid(
                [[None, None, None,
                  put_button('Fix My Code', small=True, disabled=True, onclick=mor_do, color='info', outline=False),
                  put_button('Back', color='dark', onclick=moidfa, outline=True, disabled=True, small=True), None,
                  None]])

        bugss.append(pin.from_prg_lng)
        fixed.append(pin.rr)
        get_valu()
        print(y)
        pin_update('rr', value=y[-1])
        data_nl = open('pythonfixed.txt', 'a', encoding='utf-8')
        data_nl.write(f"this time ---> {str(dt_string)}\n"
                      f"this request ---> {str(y[-1])}<----------\n"
                      f"_________________________________________________________\n")
        data_nl.close()
        with use_scope(name='down', clear=True):
            put_html('''<hr>''')
            put_grid(
                [[None, None, None,
                  put_button('Fix My Code', small=True, onclick=mor_do, color='info', outline=False),
                  put_button('Back', color='dark', onclick=moidfa, outline=True, small=True), None, None]])

    example = [
        ' \nimport Random\na = random.randint(1,12)\nb = random.randint(1,12)\nfor i in range(10):\n    question = \"What is \"+a+\" x \"+b+\"? \"\n    answer = input(question)\n    if answer = a*b\n        print (Well done!)\n    else:\n        print(\"No.\")   ',
        '\n  import random\na = random.randint(1,12)\nb = random.randint(1,12)\nfor i in range(10):\n    question = \"What is \"+str(a)+\" x \"+str(b)+\"? \"\n    answer = input(question)\n    if answer == str(a*b):\n        print (\"Well done!\")\n    else:\n        print(\"No.\")\n\n']

    with use_scope(name='title', clear=True):
        put_grid(
            [[None, None, put_html(
                      '<img width="55" height="55" src="https://img.icons8.com/fluency/48/window-bug.png" alt="window-bug"/>'), None, put_html('<h3>Fix Python Bugs By MoiAi</h3>'), None, None, None]])
        put_html('<hr>')
    with use_scope(name='main', clear=True):
        put_grid([[None,
                   put_textarea('from_prg_lng', value=example[0], label=f'Put Your Code Here :',
                                code={
                                    'mode': "your bugs",
                                    'theme': 'darcula'
                                }), None]])
        put_html('<hr>')
        put_grid([[None, put_textarea(name='rr', label=f' My True Value', value=example[1], code={
            'mode': "Fixed",
            'theme': 'darcula'
        }, readonly=True), None]])

        # print(pin.from_prg_lng)

    with use_scope(name='down', clear=True):
        put_html('''<hr>''')
        put_grid(
            [[None, None, None, put_button('Fix My Code', small=True, onclick=mor_do, color='info', outline=False),
              put_button('Back', color='dark', onclick=moidfa, outline=True, small=True), None, None]])

def tran_prog():
    set_env(title='MoiTrProg', auto_scroll_bottom=True, input_auto_focus=True, input_panel_min_height=500,
            output_max_width='100%')

    from_lng = ['python']
    from_lng.clear()
    to_lng = ['javascript']
    to_lng.clear()
    y = ['']
    y.clear()
    from_cot = [' print("hi") ']
    from_cot.clear()

    def req_codtr():
        response = openai.Completion.create(
            model="code-davinci-002",
            prompt=f"##### Translate this function  from {from_lng[-1]} into {to_lng[-1]}\n### {from_lng[-1]}\n    \n {from_cot[-1]}\n    \n### {to_lng[-1]}"
            , temperature=0,
            max_tokens=54,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["###"]

        )
        return y.append(response.choices[0].text)

    def do_it():
        if pin.fro_inp and pin.to_inp == '' or pin.fro_inp and pin.to_inp == None:
            toast('!! input is Null !!', color='error')

        def mor_do():
            with use_scope(name='down', clear=True):
                put_grid([[None, None, None,
                           put_button('Translate', small=True, onclick=mor_do, color='info', outline=True),
                           put_button('Back', color='dark', onclick=tran_prog, outline=True, small=True,
                                      disabled=True), None, None]])

            from_cot.append(pin.from_prg_lng)
            req_codtr()
            pin_update('rr', value=y[-1])
            data_nl = open('programtrans.txt', 'a', encoding='utf-8')
            data_nl.write(f"this time ---> {str(dt_string)}\n"
                          f"this request ---> {str(y[-1])}<----------\n"
                          f"_________________________________________________________\n")
            data_nl.close()
            with use_scope(name='down', clear=True):
                put_html('<hr>')
                put_grid([[None, None, None,
                           put_button('Translate', small=True, onclick=mor_do, color='info', outline=True),
                           put_button('Back', color='dark', onclick=tran_prog, outline=True, small=True,
                                      disabled=False), None, None]])

        name_pinfrom_here = ['nov']
        name_pinfrom_here.clear()
        name_pinto_here = ['nov']
        name_pinto_here.clear()
        example = [
            '###########Example###########\n#Python\n    \n    def predict_proba(X: Iterable[str]):\n        return np.array([predict_one_probas(tweet) for tweet in X])\n ',
            '###########Example###########\n#js\n    \n    function predict_proba(X) {\n        return X.map(predict_one_probas);\n    }\n    \n']
        name_pinfrom_here.append(pin.fro_inp)
        name_pinto_here.append(pin.to_inp)
        from_lng.append(name_pinfrom_here)
        to_lng.append(name_pinto_here)

        with use_scope(name='title', clear=True):
            put_grid(
                [[None,put_html(
                      '<img width="55" height="55" src="https://img.icons8.com/arcade/64/python.png" alt="python"/>'), None, put_html('<h3>Translate programming languages By MoiAi</h3>'), None, None, None]])
            put_html('<hr>')
        with use_scope(name='main', clear=True):
            put_grid([[None, put_textarea('from_prg_lng', value=example[0],
                                          label=f'Put Your {name_pinfrom_here[-1]} Code :', code={
                    'mode': f"{name_pinfrom_here[-1]}",
                    'theme': 'darcula'
                }), None]])
            put_html('<hr>')
            put_grid(
                [[None, put_textarea(name='rr', label=f'To {name_pinto_here[-1]} Code !', value=example[1], code={
                    'mode': f"{name_pinto_here[-1]}",
                    'theme': 'darcula'
                }, readonly=True), None]])

            # print(pin.from_prg_lng)

        with use_scope(name='down', clear=True):
            put_html('<hr>')
            put_grid(
                [[None, None, None, put_button('Translate', small=True, onclick=mor_do, color='info', outline=True),
                  put_button('Back', color='dark', onclick=tran_prog, outline=True, small=True), None, None]])

    # req_gramer()
    # print(y[-1])
    with use_scope(name='title', clear=True):
        put_grid([[None,put_html(
                      '<img width="60" height="60" src="https://img.icons8.com/arcade/64/python.png" alt="python"/>'), put_html('<h3>Translate programming languages By MoiAi</h3>'), None, None]])
        put_html('<hr>')
    with use_scope(name='main', clear=True):
        put_grid(
            [[None, None, None, put_input('fro_inp', label='From Lang :', type=TEXT, value='python'), None, None],
             [None, None, None, put_input('to_inp', label='To Lang :', type=TEXT, value='java script'), None,
              None]])

        put_html('<hr>')
    with use_scope(name='down', clear=True):
        put_grid([[None, None, None, put_button('Next', onclick=do_it, color='info', small=True),
                   put_button('Back', color='dark', onclick=moidfa, small=True), None, None]])

def gramerfix():
    set_env(title='MoiCorrection', auto_scroll_bottom=True, input_auto_focus=True, input_panel_min_height=500,
            output_max_width='100%')
    prompt_gramer = """Correct this to standard English:\n\n"""

    def req_gramer(prompt, p):
        with use_scope('down', clear=True):
            put_grid([[None, None, None, None,
                       put_button(label='Back', onclick=moidfa, color='dark', small=True, outline=True,
                                  disabled=True), None, None,
                       None]])
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt + p,
            temperature=0.9,
            max_tokens=600,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]

        )

        with use_scope('down', clear=True):
            put_grid([[None, None, None, None,
                       put_button(label='Back', onclick=moidfa, color='dark', small=True, outline=True), None, None,
                       None]])
        return AI_answer_gramer.append(response.choices[0].text)

    with use_scope(name='title', clear=True):
        put_html('<hr>')
        put_grid([[None, put_html('<img width="65" height="65" src="https://img.icons8.com/fluency/48/grammarly.png" alt="grammarly"/>'), None, put_html('<h3>Grammar Correction</h3>'), None, None, None]])

    with use_scope(name='main', clear=True):
        put_grid([[None, None, None, put_input('ins', value='I Usa AI evry tIME and ever day .', type=TEXT,
                                               help_text='Your Words Here !'), None, None, None]])
        put_html('<hr>')
        while True:
            req_gramer(prompt_gramer, pin.ins)
            data_nl = open('gramerfix.txt', 'a', encoding='utf-8')
            data_nl.write(f"this time ---> {str(dt_string)}\n"
                          f"this request ---> {str(AI_answer_gramer[-1])}<----------\n"
                          f"_________________________________________________________\n")
            data_nl.close()
            with use_scope(name='texter', clear=True):
                put_grid([[None, None, put_textarea('val', value=AI_answer_gramer[-1], readonly=True), None, None]])

            with use_scope('down', clear=True):
                put_grid([[None, None, None, None,
                           put_button(label='Back', onclick=moidfa, color='dark', small=True, outline=True), None,
                           None, None]])
            pin_wait_change('ins')

def NlpTra():
    set_env(title='NlpTrans', auto_scroll_bottom=True, input_auto_focus=True, input_panel_min_height=500,
            output_max_width='100%')

    def to_to_l():
        def req_nlp_tr(prompt, p):
            toast('....Here We Go .....')
            with use_scope('down', clear=True):
                put_grid([[None, None, None,
                           put_button(label='Back', onclick=moidfa, disabled=True, color='dark', small=True,
                                      outline=True),
                           put_button(label='Deep TR', onclick=doit, disabled=True, color='success', small=True,
                                      outline=True), None,
                           None]])

            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt + p,
                temperature=0.9,
                max_tokens=500,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]

            )
            with use_scope('down', clear=True):
                put_html('<hr>')
                put_grid([[None, None, None,
                           put_button(label='Back', onclick=moidfa, color='dark', small=True, outline=True),
                           put_button(label='Deep TR', onclick=doit, color='success', small=True, outline=True),
                           None,
                           None]])

            return AI_answer_nlp.append(response.choices[0].text)

        def doit():
            data_nl = open('nlp.txt', 'a', encoding='utf-8')
            data_nl.write(f"this time ---> {str(dt_string)}<------\n"
                          f"this request ---> {str(AI_answer_nlp[-1])}<-----\n"
                          f"_________________________________________________________\n")
            data_nl.close()
            prompt_NlpTrans = f"""Translate this from auto detected into {pin.choselang}:"""
            req_nlp_tr(prompt_NlpTrans, pin.inptr)
            with use_scope(name='sd', clear=True):
                put_grid([[None, None, put_textarea('val', value=AI_answer_nlp[-1], readonly=True), None, None]])
                put_html('<hr>')

        with use_scope(name='main', clear=True):
            put_grid([[None, None, None, put_input('choselang', label='From Auto Delect Languge To :',
                                                   datalist=list(Lan_iso_Name_Options),
                                                   help_text='put your lang here !'), None, None, None]])
            put_html('<hr>')
            put_grid([[None, None, None, put_textarea('inptr', label='Your Words Here :', rows=4), None,
                       set_scope(name='sd'), None]])

            with use_scope('down', clear=True):
                put_html('<hr>')
                put_grid([[None, None, None,
                           put_button(label='Back', onclick=moidfa, color='dark', small=True, outline=True),
                           put_button(label='Deep TR', onclick=doit, color='success', small=True, outline=True),
                           None, None]])

    with use_scope(name='title', clear=True):
        put_grid([[None, put_html('<img width="65" height="65" src="https://img.icons8.com/color/96/google-translate.png" alt="google-translate"/>'), None, put_html('<h3>! NLP Translate !</h3>'), None, None]])
        put_html('<hr>')
    with use_scope(name='main', clear=True):
        put_grid([[None, None, None, put_input('fromreadonly', value='Auto Delect Languge', readonly=True), None,
                   None, None]])

    with use_scope(name='down', clear=True):
        put_html('<hr>')
        put_grid([[None, None, None, put_button('Next', onclick=to_to_l, small=True, color='info'),
                   put_button('Back', small=True, color='dark', onclick=moidfa), None, None]])

def sup():
    run_js('''window.open("https://bizb.io/3c0e14b5_4447_4ca3_85c6_32c2c1493260", '_blank');''')
    popup('No Action !', put_grid([[put_html(
                      '<img width="50" height="50" src="https://img.icons8.com/3d-fluency/94/money-bag-euro.png" alt="money-bag-euro"/>'), put_html('<h2>Then press on this link ;)</h2>'), None], [
        None, None,
        put_link('Support MoiAi', url='https://bizb.io/3c0e14b5_4447_4ca3_85c6_32c2c1493260', new_window=True),
        None, None]]))

@config(title='AiTools', css_style=moidfa_csss)
def moidfa():
    set_env(title='MoiTrProg', auto_scroll_bottom=True, input_auto_focus=True, input_panel_min_height=500,
            output_max_width='88%')

    logo(5)
    clear(scope='title')

    with use_scope(name='dj', clear=True):
        put_html('''
             <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
              ''')
    with use_scope(name='title', clear=True):
        pass
    with use_scope(name='main', clear=True):
        put_grid([[None, None,put_html('<img width="42" height="42" src="https://img.icons8.com/fluency/48/grammarly.png" alt="grammarly"/>')
                      ,put_html('<img width="42" height="42" src="https://img.icons8.com/color/96/google-translate.png" alt="google-translate"/>'), None]
                     ,[None, None, put_button(label='GramerFix', onclick=gramerfix),
                   put_button('NLP | Trans', onclick=NlpTra), None],
                  [None, put_html('<hr>'), put_html('<hr>'), put_html('<hr>'), None],
                  [None, None, put_html(
                      '<img width="42" height="42" src="https://img.icons8.com/fluency/48/programming-flag.png" alt="programming-flag"/>')
                      , put_html(
                      '<img width="42" height="42" src="https://img.icons8.com/fluency/48/window-bug.png" alt="window-bug"/>'),
                   None],
                  [None, None, put_button('Trans Prog', onclick=tran_prog),
                   put_button('Py Bugs Fix', onclick=python_fix), None],
                  [None, put_html('<hr>'), put_html('<hr>'), put_html('<hr>'), None],
                  [None, None, put_html(
                      '<img width="42" height="42" src="https://img.icons8.com/arcade/64/python.png" alt="python"/>')
                      , put_html(
                      '<img width="42" height="42" src="https://img.icons8.com/color/96/new-job.png" alt="new-job"/>'),
                   None],
                  [None, None, put_button('Js To Py', onclick=js_py), put_button('Interview QA', onclick=interv),
                   None],
                  [None, put_html('<hr>'), put_html('<hr>'), put_html('<hr>'), None],
                  [None, None, put_html(
                      '<img width="42" height="42" src="https://img.icons8.com/emoji/48/books-emoji.png" alt="books-emoji"/>')
                      , put_html(
                      '<img width="42" height="42" src="https://img.icons8.com/3d-fluency/94/money-bag-euro.png" alt="money-bag-euro"/>'),
                   None],
                  [None, None, put_button('Study Notes', onclick=study_note),
                   put_button('Support Moi', onclick=sup), None]
                  ])

    with use_scope('down', clear=True):
        put_html('<hr>')
        put_grid(
            [[None, None, None, put_button(label='Back', onclick=index, color='dark', small=True, outline=True),
              None, None]])

    with use_scope(name='fll', clear=True):
        put_html('''<h3>⠀⠀⠀⠀⠀⠀</h3>
                <div class="footer-dark">
                <p class="copyright">MoiEis © 2023</p>
                </div>''')

@config(title='MoiAiChatBot', css_style=cssfi)
def firstpage():
    set_env(output_max_width='100%')

    To_Know_The_Celint = get_localstorage(key='moiiforutest')
    To_Know_user = get_localstorage(key='moiusename')

    if To_Know_The_Celint == None or To_Know_The_Celint == 'None':
        go_app('firstrunmoi', new_window=False)

    set_env(title='MoiAi')
    logo(2)
    with use_scope(name='appsbt',clear=True):

        put_grid([[None, None, None, put_html('''
        <!-- No bacwards compatabilty yet: I'm a terrible person!-->
        <ul class="menu-bar">
          <li><a href="?app=MyProfile">My Profile</a></li>
          <li><a href="?app=firstpage">MoiAi</a></li>
          <li><a href="?app=firstpage">TV Shows</a></li>
        </ul>'''), None, None]])
        put_html('<hr>')
        put_html('‎ ')

    with use_scope(name='title', clear=True):
        robot=open('robot.png','rb').read()
        put_grid([[None,None,None,put_image(robot,width='70',height='70',format='PNG'),put_html(f'''
                   <div class="container">
                <div class="box">

                    <div class="title">
                        <span class="block"></span>
                        <h2>{To_Know_user}<span></span></h2>
                    </div>

                    <div class="role">
                        <div class="block"></div>
                        <p>Make your choice !</p>
                    </div>

                </div>
            </div>





                   '''),None,None]])
    with use_scope(name='linefirst', clear=True):

        put_html('‎ ')

    with use_scope(name='main', clear=True):
        put_grid([[None,None,None,None,None,put_html('''<img width="44" height="44" src="https://img.icons8.com/3d-fluency/94/chatbot.png" alt="chatbot"/>'''),None,
                   put_html('''<img width="44" height="44" src="https://img.icons8.com/3d-fluency/94/module.png" alt="module"/>'''),None,
                   put_html('''<img width="44" height="44" src="https://img.icons8.com/3d-fluency/94/control-panel.png" alt="control-panel"/>'''),None,None,None,None
                      ]])

        put_grid([[None, None, None, put_html('''<!-- HTML !-->


            <button class="button-92" role="button">GbtBot</button>

            <style>
            .button-92 {
              --c: #fff;
              /* text color */
              background: linear-gradient(90deg, #0000 33%, #fff5, #0000 67%) var(--_p,100%)/300% no-repeat,
                #2A9817;
              /* background color */
              color: #0000;
              border: none;
              transform: perspective(500px) rotateY(calc(20deg*var(--_i,-1)));
              text-shadow: calc(var(--_i,-1)* 0.08em) -.01em 0   var(--c),
                calc(var(--_i,-1)*-0.08em)  .01em 2px #0004;
              outline-offset: .1em;
              transition: 0.5s;
            }

            .button-92:hover,
            .button-92:focus-visible {
              --_p: 0%;
              --_i: 1;
            }

            .button-92:active {
              text-shadow: none;
              color: #444444;
              box-shadow: inset 0 0 9e9q #0005;
              transition: 0s;
            }

            .button-92 {
              font-family: "Gill Sans", sans-serif;
              font-weight: bold;
              font-size: 0.8rem;
              margin: 0;
              cursor: pointer;
              padding: .1em .3em;
            }
            </style>''').onclick(gbt),
                   put_html('''<!-- HTML !-->
            <button class="button-92" role="button">MoiDfa</button>

            <style>
            .button-92 {
            --c: #fff;
            /* text color */
            background: linear-gradient(90deg, #0000 33%, #fff5, #0000 67%) var(--_p,100%)/300% no-repeat,
            #2A9817;
            /* background color */
            color: #0000;
            border: none;
            transform: perspective(500px) rotateY(calc(20deg*var(--_i,-1)));
            text-shadow: calc(var(--_i,-1)* 0.08em) -.01em 0   var(--c),
            calc(var(--_i,-1)*-0.08em)  .01em 2px #3282AE;
            outline-offset: .1em;
            transition: 0.3s;
            }

            .button-92:hover,
            .button-92:focus-visible {
            --_p: 0%;
            --_i: 1;
            }

            .button-92:active {
            text-shadow: none;
            color: #444444;
            box-shadow: inset 0 0 9e9q #0005;
            transition: 0s;
            }

            .button-92 {
            font-family: "Gill Sans", sans-serif;
            font-weight: bold;
            font-size: 2rem;
            margin: 0;
            cursor: pointer;
            padding: .1em .3em;
            }
            </style>''').onclick(moidfa_conv),
                   put_html('''<!-- HTML !-->
            <button class="button-92" role="button">MoiPic</button>

            <style>
            .button-92 {
            --c: #fff;
            /* text color */
            background: linear-gradient(90deg, #0000 33%, #fff5, #0000 67%) var(--_p,100%)/300% no-repeat,
            #2A9817;
            /* background color */
            color: #0000;
            border: none;
            transform: perspective(500px) rotateY(calc(20deg*var(--_i,-1)));
            text-shadow: calc(var(--_i,-1)* 0.08em) -.01em 0   var(--c),
            calc(var(--_i,-1)*-0.08em)  .01em 2px #0004;
            outline-offset: .1em;
            transition: 0.3s;
            }

            .button-92:hover,
            .button-92:focus-visible {
            --_p: 0%;
            --_i: 1;
            }

            .button-92:active {
            text-shadow: none;
            color: #444444;
            box-shadow: inset 0 0 9e9q #0005;
            transition: 0s;
            }

            .button-92 {
            font-family: "Gill Sans", sans-serif;
            font-weight: bold;
            font-size: 1.3rem;
            margin: 0;
            cursor: pointer;
            padding: .1em .3em;
            }
            </style>''').onclick(moipiccc), None, None]])
        put_html('<hr>')
        put_grid([[None, None, None, None, None, put_html(
            '''<img width="44" height="44" src="https://img.icons8.com/3d-fluency/94/cinema-.png" alt="cinema-"/>'''),
                   None,
                   put_html(
                       '''<img width="44" height="44" src="https://img.icons8.com/3d-fluency/94/help.png" alt="help"/>'''),
                   None,
                   put_html(
                       '''<img width="44" height="44" src="https://img.icons8.com/3d-fluency/94/pin3.png" alt="pin3"/>'''),
                   None, None, None, None
                   ]])
        put_html('‎ ')
        put_grid([[None, None, None, put_html('''<!-- HTML !-->


                    <button class="button-92" role="button">Script</button>

                    <style>
                    .button-92 {
                      --c: #fff;
                      /* text color */
                      background: linear-gradient(90deg, #0000 33%, #fff5, #0000 67%) var(--_p,100%)/300% no-repeat,
                        #2A9817;
                      /* background color */
                      color: #0000;
                      border: none;
                      transform: perspective(500px) rotateY(calc(20deg*var(--_i,-1)));
                      text-shadow: calc(var(--_i,-1)* 0.08em) -.01em 0   var(--c),
                        calc(var(--_i,-1)*-0.08em)  .01em 2px #0004;
                      outline-offset: .1em;
                      transition: 0.5s;
                    }

                    .button-92:hover,
                    .button-92:focus-visible {
                      --_p: 0%;
                      --_i: 1;
                    }

                    .button-92:active {
                      text-shadow: none;
                      color: #444444;
                      box-shadow: inset 0 0 9e9q #0005;
                      transition: 0s;
                    }

                    .button-92 {
                      font-family: "Gill Sans", sans-serif;
                      font-weight: bold;
                      font-size: 0.7rem;
                      margin: 0;
                      cursor: pointer;
                      padding: .1em .3em;
                    }
                    </style>''').onclick(gbt),
                   put_html('''<!-- HTML !-->
                    <button class="button-92" role="button">Updates</button>

                    <style>
                    .button-92 {
                    --c: #fff;
                    /* text color */
                    background: linear-gradient(90deg, #0000 33%, #fff5, #0000 67%) var(--_p,100%)/300% no-repeat,
                    #2A9817;
                    /* background color */
                    color: #0000;
                    border: none;
                    transform: perspective(500px) rotateY(calc(20deg*var(--_i,-1)));
                    text-shadow: calc(var(--_i,-1)* 0.08em) -.01em 0   var(--c),
                    calc(var(--_i,-1)*-0.08em)  .01em 2px #3282AE;
                    outline-offset: .1em;
                    transition: 0.3s;
                    }

                    .button-92:hover,
                    .button-92:focus-visible {
                    --_p: 0%;
                    --_i: 1;
                    }

                    .button-92:active {
                    text-shadow: none;
                    color: #444444;
                    box-shadow: inset 0 0 9e9q #0005;
                    transition: 0s;
                    }

                    .button-92 {
                    font-family: "Gill Sans", sans-serif;
                    font-weight: bold;
                    font-size: 2rem;
                    margin: 0;
                    cursor: pointer;
                    padding: .1em .3em;
                    }
                    </style>''').onclick(moidfa_conv),
                   put_html('''<!-- HTML !-->
                    <button class="button-92" role="button">Fast Go</button>

                    <style>
                    .button-92 {
                    --c: #fff;
                    /* text color */
                    background: linear-gradient(90deg, #0000 33%, #fff5, #0000 67%) var(--_p,100%)/300% no-repeat,
                    #2A9817;
                    /* background color */
                    color: #0000;
                    border: none;
                    transform: perspective(500px) rotateY(calc(20deg*var(--_i,-1)));
                    text-shadow: calc(var(--_i,-1)* 0.08em) -.01em 0   var(--c),
                    calc(var(--_i,-1)*-0.08em)  .01em 2px #0004;
                    outline-offset: .1em;
                    transition: 0.3s;
                    }

                    .button-92:hover,
                    .button-92:focus-visible {
                    --_p: 0%;
                    --_i: 1;
                    }

                    .button-92:active {
                    text-shadow: none;
                    color: #444444;
                    box-shadow: inset 0 0 9e9q #0005;
                    transition: 0s;
                    }

                    .button-92 {
                    font-family: "Gill Sans", sans-serif;
                    font-weight: bold;
                    font-size: 1.3rem;
                    margin: 0;
                    cursor: pointer;
                    padding: .1em .3em;
                    }
                    </style>''').onclick(moipiccc), None, None]])
        put_html('<hr>')
        put_html('''
                   <h3><span>‎ ‎ ‎ </span></h3>
                   <h3><span>‎ ‎ </span></h3>
                   <h3><span>‎ ‎ </span></h3>
                   <h3><span>‎ </span></h3>
                   <h3><span>‎ </span></h3>
                   <h3><span>‎ </span></h3>
                   ''')
        put_grid([[None, None, None,
                   put_image('https://www.svgrepo.com/show/21304/logout.svg', format='svg', width='20',
                             height='20').onclick(logout), None, None]])

    with use_scope('don', clear=True):
        put_html('<span>⠀</span>'
                 '<span>⠀</span>')
    with use_scope('down', clear=True):
        pass

    with use_scope(name='foo', clear=True):
        put_html(''' 



        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Untitled</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.min.css">
            <link rel="stylesheet" href="assets/css/style.css">
        </head>
        <body>
            <div class="footer-dark">
                <footer>
                    <div class="container">
                        <div class="row">
                             <div class="col-sm-6 col-md-3 item">
                                <h3>Growing With MoiEis</h3>
                                <ul>
                                    <li><a href="?app=BuyMeC">Buy Me a Coffee</a></li>
                                    <li><a href="?app=togather">Tips for improving MoiAi</a></li>

                                </ul>
                            </div>
                            <div class="col-md-6 item text">

                                <h3><span>MoiAi</h3>
                                <p>A world that starts with just an idea ! Then translated into something practical, and returned to an idea in the mind of a machine after an era of the best of it</p>
                            </div>
                            <div class="col item social">

                            <a href="https://twitter.com/moi2all"  target="_blank" ><i class="icon ion-social-twitter"></i></a>
                             <a href="https://www.instagram.com/moie._10/"  target="_blank" ><i class="icon ion-social-instagram"></i></a></div>
                        </div>
                        <p class="copyright">MoiEis © 2023</p>
                    </div>
                </footer>
            </div>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/js/bootstrap.bundle.min.js"></script>
        </body>
        ''')

@config(title='chose room', css_style=csss)
def secondpage():

    holy_conv.clear()
    holy_conv.append(prompt_gbt)
    To_Know_The_Celint = get_localstorage(key='moiiforutest')

    if To_Know_The_Celint == None or To_Know_The_Celint == 'None':
        go_app('firstrunmoi', new_window=False)

    set_env(output_max_width='100%', input_auto_focus=False)
    clear(scope='title')

    data_chat_stroge_hetor = get_localstorage(key='MoiToYou')
    name = get_localstorage(key='moiusename')
    data = countt_of_rom_list[-1] + 1

    countt_of_rom_list.append(data)

    def keep_going():

        with use_scope(name='main', clear=True):
            with use_scope(name='allw', clear=True):
                put_html(f'''
                         <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                          <h3>⠀⠀⠀⠀⠀⠀</h3>
                           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>

                                    <h3><span>Equip</span>

                                    <span>A private</span>
                                    <span>Room</span>
                                    <span>For</span>
                                    <span>You</span>
                                    <span>{name}</span></h3>

                        ''')

            with use_scope(name='lodi', clear=True):
                put_grid([[None, None, None, put_html('''
                                <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>   


                            <style>



                            .lds-ellipsis {
                  display: inline-block;
                  position: relative;
                  width: 80px;
                  height: 80px;
                }
                .lds-ellipsis div {
                  position: absolute;
                  top: 33px;
                  width: 13px;
                  height: 13px;
                  border-radius: 50%;
                  background: #fff;
                  animation-timing-function: cubic-bezier(0, 1, 1, 0);
                }
                .lds-ellipsis div:nth-child(1) {
                  left: 8px;
                  animation: lds-ellipsis1 0.6s infinite;
                }
                .lds-ellipsis div:nth-child(2) {
                  left: 8px;
                  animation: lds-ellipsis2 0.6s infinite;
                }
                .lds-ellipsis div:nth-child(3) {
                  left: 32px;
                  animation: lds-ellipsis2 0.6s infinite;
                }
                .lds-ellipsis div:nth-child(4) {
                  left: 56px;
                  animation: lds-ellipsis3 0.6s infinite;
                }
                @keyframes lds-ellipsis1 {
                  0% {
                    transform: scale(0);
                  }
                  100% {
                    transform: scale(1);
                  }
                }
                @keyframes lds-ellipsis3 {
                  0% {
                    transform: scale(1);
                  }
                  100% {
                    transform: scale(0);
                  }
                }
                @keyframes lds-ellipsis2 {
                  0% {
                    transform: translate(0, 0);
                  }
                  100% {
                    transform: translate(24px, 0);
                  }
                }</style>
                '''), None, None]])

            time.sleep(3)
            with use_scope(name='allw', clear=True):
                put_html(f'''
                         <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                          <h3>⠀⠀⠀⠀⠀⠀</h3>
                           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>

                                    <h3><span>We</span>
                                    <span>Guarantee</span>
                                    <span>The Security Of {name} Data</span>
                                    <span>There Is No Excuse For Its Leakage</span>
                                    <span>So We Hope To Support Free Services</span>
                                    <span>As This Is A strong Motivation For Continuing Development </span>
                                    <span></span>
                                    <span></span></h3>
                        ''')

            time.sleep(3)

            with use_scope(name='lodi', clear=True):
                put_grid([[None, None, None, put_html(f'''<h2><span>We Have Reached</span>
                                     <span>This Number Of Rooms With MoiAiChat</span>
                                     </h2>

                                        '''), None, None]])

                put_html(f'''<h3><span>{countt_of_rom_list[-1]}</span></h3>''')

        time.sleep(5)
        Key_room.append(1)
        go_app('theredpage', new_window=False)

    if data_chat_stroge_hetor == None or data_chat_stroge_hetor == 'None':

        with use_scope(name='main', clear=True):
            with use_scope(name='allw', clear=True):
                put_html(f'''
                         <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                          <h3>⠀⠀⠀⠀⠀⠀</h3>
                           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>

                                    <h3>

                                    <span>{name} History </span>
                                    <span>is </span>
                                    <span>Empty </span>
                                    <span>😅</span>
                                    </h3>

                        ''')
                time.sleep(3)

            with use_scope(name='allw', clear=True):
                put_html('''   <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                          <h3>⠀⠀⠀⠀⠀⠀</h3>
                           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                            <h3>

                                    <span>would you like to store your data </span>
                                    <span>in your device for next time history ?</span>

                                    </h3>

                                     <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>''')

                put_grid([[None, None, None, put_button('Yes', onclick=keep_going),
                           put_button('Nope', onclick=keep_going, color='dark'), None, None]])

    else:
        keep_going()

@config(title='chose room', css_style=csss)
def save_pref():

    # print(ai_h_Conv['hu'])
    # print(ai_h_Conv['ai'])
    To_Know_The_Celint = get_localstorage(key='moiiforutest')
    To_Know_user = get_localstorage(key='moiusename')

    if To_Know_The_Celint == None or To_Know_The_Celint == 'None':
        go_app('firstrunmoi', new_window=False)

    try:
        try:
            data_hestory = pd.DataFrame({'Data': get_localstorage(key='olddata').split('\n\n' and '\n')[2::]})

        except:
            data_hestory = pd.DataFrame({'Data': get_localstorage(key='MoiToYou').split('\n\n' and '\n')[2::]})

        put_html(data_hestory.to_html())

        def ddo():
            dataaa = open('historyByMoiAi.txt', 'w', encoding='utf8').write(data_hestory.to_string())
            opendata = open('historyByMoiAi.txt', 'rb').read()
            download('historyByMoiAi.txt', opendata)

        put_grid([[None, None, None, put_button('download', onclick=ddo), None, None]])

    except:

        put_html(f'''
                                     <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                                      <h3>⠀⠀⠀⠀⠀⠀</h3>
                                       <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                                       <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                                       <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>

                                      <h2><span>Your Value </span>
                                     <span>Still [0]</span>
                                     </h2>

                                    ''')

@config(title='MoiAiChatBot', css_style=compcss + cssfi)
def theredpage():

    To_Know_The_Celint = get_localstorage(key='moiiforutest')

    if To_Know_The_Celint == None or To_Know_The_Celint == 'None':
        go_app('firstrunmoi', new_window=False)

    if Key_room[-1] != 1 or None:
        go_app(name='secondpage', new_window=False)
    else:
        pass

    clear(scope='linefirst')
    logo(3)

    set_env(title='moi chat', auto_scroll_bottom=False, input_auto_focus=True, input_panel_min_height=500,
            output_max_width='100%')

    put_grid([[None, None, None, put_html(f'''   


                             <div class="line">
            <h3 class='lineUp'></h3>
          </div>


                                  <h3>‎ ‎ </h3>
          '''), None, None]])
    with use_scope(name='main', clear=True):

        put_scrollable([put_scope(name='dd', content=[put_html(f'''
                                                       <div class="chat-container">

                                                        <ul class="chat">
                                                            <li class="message left">
                                                                <img class="logo" src="https://s9.gifyu.com/images/ai.gif" alt="">

                                                                <div class="typewriter">
                                                                  <h4>Hi Im moibot ! How Can I Help You Today ?</h4>
                                                                </div>
                                                            </li>
                                                        </ul>

                                                       </div>
                                                       <style>
                                                       {d}
                                                       </style>''')])
                        ], keep_bottom=True)

    with use_scope(name='don', clear=True):
        put_html(''' <h3><span>‎ </span></h3>''')
        put_grid([[None, None, None, None, None, put_textarea('tryy', placeholder='Start Your Chat With MoiGbt'),
                   None, None, None, None, None]])
        put_grid([[None, None, None, None, put_scope(name='presss', content=[put_html('''
                        <button>
                  <div class="svg-wrapper-1">
                    <div class="svg-wrapper">
                      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="14" height="14">
                        <path fill="none" d="M0 0h24v24H0z"></path>
                        <path fill="currentColor" d="M1.946 9.315c-.522-.174-.527-.455.01-.634l19.087-6.362c.529-.176.832.12.684.638l-5.454 19.086c-.15.529-.455.547-.679.045L12 14l6-8-8 6-8.054-2.685z"></path>
                      </svg>
                    </div>
                  </div>
                  <span>dos</span>
                </button>

                        <style>button {
                 font-family: inherit;
                 font-size: 8px;
                 background: royalblue;
                 color: white;
                 padding: 0.4em 0.4em;
                 padding-left: 0.9em;
                 display: -webkit-box;
                 display: -ms-flexbox;
                 display: flex;
                 -webkit-box-align: center;
                     -ms-flex-align: center;
                         align-items: center;
                 border: none;
                 border-radius: 16px;
                 overflow: hidden;
                 -webkit-transition: all 0.2s;
                 transition: all 0.2s;
                }

                button span {
                 display: block;
                 margin-left: 0.3em;
                 -webkit-transition: all 0.3s ease-in-out;
                 transition: all 0.3s ease-in-out;
                }

                button svg {
                 display: block;
                 -webkit-transform-origin: center center;
                     -ms-transform-origin: center center;
                         transform-origin: center center;
                 -webkit-transition: -webkit-transform 0.3s ease-in-out;
                 transition: -webkit-transform 0.3s ease-in-out;
                 transition: transform 0.3s ease-in-out;
                 transition: transform 0.3s ease-in-out, -webkit-transform 0.3s ease-in-out;
                }

                button:hover .svg-wrapper {
                 -webkit-animation: fly-1 0.6s ease-in-out infinite alternate;
                         animation: fly-1 0.6s ease-in-out infinite alternate;
                }

                button:hover svg {
                 -webkit-transform: translateX(1.2em) rotate(45deg) scale(1.1);
                     -ms-transform: translateX(1.2em) rotate(45deg) scale(1.1);
                         transform: translateX(1.2em) rotate(45deg) scale(1.1);
                }

                button:hover span {
                 -webkit-transform: translateX(5em);
                     -ms-transform: translateX(5em);
                         transform: translateX(5em);
                }

                button:active {
                 -webkit-transform: scale(0.95);
                     -ms-transform: scale(0.95);
                         transform: scale(0.95);
                }

                @-webkit-keyframes fly-1 {
                 from {
                  -webkit-transform: translateY(0.1em);
                          transform: translateY(0.1em);
                 }

                 to {
                  -webkit-transform: translateY(-0.1em);
                          transform: translateY(-0.1em);
                 }
                }

                @keyframes fly-1 {
                 from {
                  -webkit-transform: translateY(0.1em);
                          transform: translateY(0.1em);
                 }

                 to {
                  -webkit-transform: translateY(-0.1em);
                          transform: translateY(-0.1em);
                 }
                }

                </style>''').onclick(fourd_r)]), None, None, None]])

    put_html('''
                                                         <h3><span>‎ ‎ ‎ </span></h3>
                                                         <h3><span>‎ ‎ </span></h3>


                                                         ''')

    with use_scope(name='floott', clear=True):
        put_html('''

                                <h3><span>‎ ‎ ‎ </span></h3>


                            <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <title>Untitled</title>
                                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css">
                                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.min.css">
                                <link rel="stylesheet" href="assets/css/style.css">
                            </head>
                            <body>
                                <div class="footer-dark">
                                    <footer>
                                        <div class="container">
                                            <div class="row">
                                                 <div class="col-sm-6 col-md-3 item">
                                                    <h3>Growing With MoiEis</h3>
                                                    <ul>
                                                        <li><a href="?app=save_pref" target="_blank">collect my data</a></li>
                                                        <li><a href="https://lookingforsponsor.com/app/opportunities/8327974312_KQlvZ9fyetduyl4Wb70v" target="_blank">Place of sponsor</a></li>
                                                        <li><a href="?app=firstpage" target="_blank">Back To Moi</a></li>


                                                    </ul>
                                                </div>
                                                <div class="col-md-6 item text">

                                                    <h3><span>MoiAi</h3>
                                                    <p>A world that starts with just an idea ! Then translated into something practical, and returned to an idea in the mind of a machine after an era of the best of it</p>
                                                </div>
                                                <div class="col item social">
                                                <a href="https://twitter.com/moi2all" target="_blank"><i class="icon ion-social-twitter"></i></a>
                                         <a href="https://www.instagram.com/moie._10/" target="_blank"><i class="icon ion-social-instagram"></i></a></div>


                                            </div>
                                            <p class="copyright">MoiEis © 2023</p>
                                        </div>
                                    </footer>
                                </div>
                                <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
                                <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/js/bootstrap.bundle.min.js"></script>
                            </body>
                            ''')

def fourd_r():

    name = get_localstorage(key='moiusename')

    def req(prompt):

        with use_scope(name='presss', clear=True):
            def wait():
                toast('please wait ....')

            put_html(u'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin:auto;background:#fff;display:block;" width="30px" height="30px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
        <path fill="none" stroke="#284ab1" stroke-width="4" stroke-dasharray="189.87580688476564 66.71312133789061" d="M24.3 30C11.4 30 5 43.3 5 50s6.4 20 19.3 20c19.3 0 32.1-40 51.4-40 C88.6 30 95 43.3 95 50s-6.4 20-19.3 20C56.4 70 43.6 30 24.3 30z" stroke-linecap="round" style="transform:scale(0.97);transform-origin:50px 50px">
          <animate attributeName="stroke-dashoffset" repeatCount="indefinite" dur="1.0204081632653061s" keyTimes="0;1" values="0;256.58892822265625"></animate>
        </path>
        </svg>''').onclick(wait)

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=200,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]

        )

        with use_scope(name='presss', clear=True):
            def wait():
                toast('please wait ....')

            put_html('''
                            <button>
                      <div class="svg-wrapper-1">
                        <div class="svg-wrapper">
                          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="17" height="17">
                            <path fill="none" d="M0 0h24v24H0z"></path>
                            <path fill="currentColor" d="M1.946 9.315c-.522-.174-.527-.455.01-.634l19.087-6.362c.529-.176.832.12.684.638l-5.454 19.086c-.15.529-.455.547-.679.045L12 14l6-8-8 6-8.054-2.685z"></path>
                          </svg>
                        </div>
                      </div>
                      <span>dos</span>
                    </button>

                            <style>button {
                     font-family: inherit;
                     font-size: 12px;
                     background: royalblue;
                     color: white;
                     padding: 0.7em 1em;
                     padding-left: 0.9em;
                     display: -webkit-box;
                     display: -ms-flexbox;
                     display: flex;
                     -webkit-box-align: center;
                         -ms-flex-align: center;
                             align-items: center;
                     border: none;
                     border-radius: 16px;
                     overflow: hidden;
                     -webkit-transition: all 0.2s;
                     transition: all 0.2s;
                    }

                    button span {
                     display: block;
                     margin-left: 0.3em;
                     -webkit-transition: all 0.3s ease-in-out;
                     transition: all 0.3s ease-in-out;
                    }

                    button svg {
                     display: block;
                     -webkit-transform-origin: center center;
                         -ms-transform-origin: center center;
                             transform-origin: center center;
                     -webkit-transition: -webkit-transform 0.3s ease-in-out;
                     transition: -webkit-transform 0.3s ease-in-out;
                     transition: transform 0.3s ease-in-out;
                     transition: transform 0.3s ease-in-out, -webkit-transform 0.3s ease-in-out;
                    }

                    button:hover .svg-wrapper {
                     -webkit-animation: fly-1 0.6s ease-in-out infinite alternate;
                             animation: fly-1 0.6s ease-in-out infinite alternate;
                    }

                    button:hover svg {
                     -webkit-transform: translateX(1.2em) rotate(45deg) scale(1.1);
                         -ms-transform: translateX(1.2em) rotate(45deg) scale(1.1);
                             transform: translateX(1.2em) rotate(45deg) scale(1.1);
                    }

                    button:hover span {
                     -webkit-transform: translateX(5em);
                         -ms-transform: translateX(5em);
                             transform: translateX(5em);
                    }

                    button:active {
                     -webkit-transform: scale(0.95);
                         -ms-transform: scale(0.95);
                             transform: scale(0.95);
                    }

                    @-webkit-keyframes fly-1 {
                     from {
                      -webkit-transform: translateY(0.1em);
                              transform: translateY(0.1em);
                     }

                     to {
                      -webkit-transform: translateY(-0.1em);
                              transform: translateY(-0.1em);
                     }
                    }

                    @keyframes fly-1 {
                     from {
                      -webkit-transform: translateY(0.1em);
                              transform: translateY(0.1em);
                     }

                     to {
                      -webkit-transform: translateY(-0.1em);
                              transform: translateY(-0.1em);
                     }
                    }

                    </style>''').onclick(fourd_r)

        ####################################################################################################$
        ###################################fix the botun bug on press#####################################

        return Ai_answer_Hestory.append(response.choices[0].text), ai_h_Conv['ai'].append(Ai_answer_Hestory[-1])

    ######################################################################################################
    ####################################fixbugs#############################################################

    if len(pin.tryy) > 1:

        ai_h_Conv['you'].append(pin.tryy)

        # data1 = prompt_gbt + ai_h_Conv['you'][-1] + ai_h_Conv['ai'][-1] + '\nHuman: '

        holy_conv.append(holy_conv[-1] + ai_h_Conv['you'][-1])

        req(holy_conv[-1])

        holy_conv.append(holy_conv[-1] + ai_h_Conv['ai'][-1] + '\nHuman: ')
        try:
            old_to_use = set_localstorage(key='olddata', value=get_localstorage(key='MoiToYou'))
            
        except:
            pass

        save_it_to_you_ = set_localstorage(key='MoiToYou', value=str(holy_conv[-1]))

        # holy_conv.append(holy_conv[-1]+ai_h_Conv['you'][-1] + ai_h_Conv['ai'][-1] + '\nHuman: ')

        
        with use_scope(name='dd'):

            logo(3)
            out = '''/* ===== Scrollbar CSS ===== */
                  /* Firefox */
                  * {
                    scrollbar-width: thin;
                    scrollbar-color: #8f54a0 #ffffff;
                  }

                  /* Chrome, Edge, and Safari */
                  *::-webkit-scrollbar {
                    width: 16px;
                  }

                  *::-webkit-scrollbar-track {
                    background: #ffffff;
                  }

                  *::-webkit-scrollbar-thumb {
                    background-color: #8f54a0;
                    border-radius: 10px;
                    border: 3px solid #ffffff;
                  }'''
            put_scrollable([put_html(f'''<hr><div class="chat-container">

                                                                                                <ul class="chat">
                                                                                                <li class="message right">
                                                                            <img class="logo" src="https://s3.gifyu.com/images/human.gif" alt="Me">


                                                                            <h4><span>{name}: {pin.tryy}</span></h4>

                                                                        </li>
                                                                    </ul>

                                                                        <style>
                                                                   {d}
                                                                   </style>'''), put_html(f'''
                                                                       <div class="chat-container">
                                                                        <ul class="chat">
                                                                             <div class="typewriter">
                                                                            <li class="message left">
                                                                                <img class="logo" src="https://s9.gifyu.com/images/ai.gif" alt="Ai">
                                                                                <h4>{Ai_answer_Hestory[-1]}</h4>
                                                                            </li>
                                                                            </div>
                                                                        </ul>

                                                                       </div>
                                                                       <style>
                                                                       {d}
                                                                       </style>''')], keep_bottom=True,
                           border=False)
            To_Know_user = get_localstorage(key='moiusename')
            try:
                tet_file.write(f'--------------\n')
                tet_file.write(f'Human: {pin.tryy}\n')
                tet_file.write(f'--------------\n')
                tet_file.write(f'{Ai_answer_Hestory[-1]}\n')
                tet_file.write(f'--------------\n')
                tet_file.close()
            except:
                retet_file = open('ai', 'a', encoding='utf-8')
                retet_file.write(f'----{To_Know_user}-----\n')
                retet_file.write(f'Human: {pin.tryy}\n')
                retet_file.write(f'--------------\n')
                retet_file.write(f'{Ai_answer_Hestory[-1]}\n')
                retet_file.write(f'--------------\n')
            pin_update(name='tryy', value='')

        time_pross[-1] += 1






    else:
        toast(' Add more characters, it must be len() > 3', color='#FFE785 ')

@config(title='MoiWelcome', css_style=csss,manifest={
  "name": "MoiAi",
  
})
def firstrunmoi():

    from tttttt import Wmoi
    s = Wmoi.rettur('sd')

@config(title='MoiAi', description='Moi Artificial Intelligence MoiAi Generator Art,Text.Nlp ', css_style='''.footer {
            display: none;
        }''')
def index():

    To_Know_The_Celint = get_localstorage(key='moiiforutest')

    if To_Know_The_Celint == None or To_Know_The_Celint == 'None':
        go_app('firstrunmoi', new_window=False)

    moiuser = get_localstorage(key='moiusename')

    ai_h_Conv['ai'].clear()
    ai_h_Conv['you'].clear()

    data_nl = open('moigbt.txt', 'a', encoding='utf-8')
    data_nl.write(f"  ##################{str(info.user_ip)}####################\n"
                  f"on this user agent ---> {str(info.user_agent)}<-----\n"
                  f"________info user lang---->{str(info.user_language)}<------________________\n"
                  f"*---->{str(info)}\n"
                  f"================================================================================\n"
                  )
    data_nl.close()

    logo(2)
    print('asffgdf')
    go_app('firstpage', new_window=False)

def gbt():
    go_app('secondpage', new_window=False)

def moidfa_conv():
    go_app(name='moidfa', new_window=False)

@config(title='moipic', css_style=moipiccdc)
def moipic():
    set_env(output_max_width='100%')

    To_Know_The_Celint = get_localstorage(key='moiiforutest')
    if To_Know_The_Celint == None:
        go_app('firstrunmoi', new_window=False)
        firstrunmoi()
    from moipicc import MoiPic_New_Page
    pic = MoiPic_New_Page.rettur('ds')




@config(title='MoiAiChatBot', css_style=cssfi)
def MyProfile():
    set_env(output_max_width='100%')

    To_Know_The_Celint = get_localstorage(key='moiiforutest')
    if To_Know_The_Celint == None:
        go_app('firstrunmoi', new_window=False)
        firstrunmoi()
    from MyProfile import MoiProfile_New_Page
    pic = MoiProfile_New_Page.rettur('ds')
@config(title='MoiAiChatBot', css_style=cssfi)
def BuyMeC():
    set_env(output_max_width='100%')

    To_Know_The_Celint = get_localstorage(key='moiiforutest')
    if To_Know_The_Celint == None:
        go_app('firstrunmoi', new_window=False)
        firstrunmoi()
    from BuyMeC import BuyMeC_New_Page
    pic = BuyMeC_New_Page.rettur('ds')

#
# if __name__ == '__main__':
#         import argparse
#         from pywebio.platform.tornado_http import start_server as start_http_server
#         from pywebio import start_server as start_ws_server
#
#         parser = argparse.ArgumentParser()
#         parser.add_argument("-p", "--port", type=int, default=8080)
#         parser.add_argument("--http", action="store_true", default=False,
#                             help='Whether to enable http protocol for communicates')
#         args = parser.parse_args()
#
#         if args.http:
#             start_http_server(
#                 [index, firstpage, secondpage, theredpage, save_pref, moidfa, firstrunmoi, togather, moipic],
#                 port=args.port, debug=False)
#         else:
#             # Since some cloud server may close idle connections (such as heroku),
#             # use `websocket_ping_interval` to  keep the connection alive
#             start_ws_server(
#                 [index, firstpage, secondpage, theredpage, save_pref, moidfa, firstrunmoi, togather, moipic],
#                 port=args.port, websocket_ping_interval=30, debug=False, cdn=True)

start_server(
                [index, firstpage, secondpage, theredpage, save_pref, moidfa, firstrunmoi, togather, moipic,MyProfile,BuyMeC],
                port=1232, debug=False)