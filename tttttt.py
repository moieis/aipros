from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.platform import *
from pywebio.session import *
from pywebio_battery import *
import pandas as pd
import time
import openai
from datetime import datetime







def supmoi():

    run_js('''window.open("https://bizb.io/3c0e14b5_4447_4ca3_85c6_32c2c1493260", '_blank');''')
    popup('''If your browser doesn't support auto move  ''',
          put_grid([[None,None,put_html('<h3><span> just press this link with : </span></h3>'),None,None],
                    [None,None,None ,put_link('! All opportunities and support !',url='https://bizb.io/3c0e14b5_4447_4ca3_85c6_32c2c1493260',new_window=True),None,None,None]]))

def moidata():
    with use_scope(name='name', clear=True):
        put_html(f'<h4><span> Coming Soon {pin.d}</span>'
                 f'         <span> We are working hard and it is with great pleasure and motivation that you support us in the button below  </span>'
                 f'   <span> 🤗 </span></h4>'
                 f''
                 f'         ')

def retret():
    print(pin.d)
    if pin.d == "" or len(pin.d) == 1 or pin.d == ' ' or pin.d == '  ':
        with use_scope(name='name', clear=True):
            put_html(f'<h2 color:#231557;><span>🙄 Nop, Write your name</span></h2>')
    else:
        set_localstorage(key='moiiforutest', value='GoForMoiAuto')
        set_localstorage(key='moiusename', value=f'{pin.d}')
        dataa = get_localstorage(key='moiusename')
        celint_nae=open('namec.txt','a',encoding='utf8').write(f'{str(dataa)}\n')
        clear(scope='allw')
        with use_scope(name='allw',clear=True):
            put_html(f'''
        
     
       
         <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
          <h3>⠀⠀⠀⠀⠀⠀</h3>
           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
                
                    <h3><span>{dataa}</span></h3>
                    <h3><span>Keep in touch with Moi updates</span></h3>
                    
        
        
        ''')
        time.sleep(3)
        with use_scope(name='allw', clear=True):
            put_html('''



         <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
          <h3>⠀⠀⠀⠀⠀⠀</h3>
           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
           <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>

                    <h3><span>let's</span>
                    <span>go</span>
                    </h3>



        ''')



        time.sleep(3)
        # clear(scope='name')
        clear(scope='allw')
        from app import index
        go_app('index', new_window=False)
        index()



def helpp():
    popup('DOFMoiAi',put_html('''<iframe src="https://show.zoho.eu/show/publish/akrkj124274af90af412e80f0cf5134517b64/params?toolbar=true&menu=false&loop=true&viewtype=3&preload=false" width="960" height="569" style="border:1px solid #aabbcc;max-width: 100%;" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>'''))
def wopen():
    set_env(output_max_width='100%', input_auto_focus=False)
    with use_scope('allw', clear=True):
        set_env(output_max_width='100%')

        with use_scope(name='logo', clear=True):
            put_html('''


                                <div class="container">
                      <div class="row">
                        <div class="col-md-12 text-center">
                          <h3 class="animate-charcter"> MoiApps</h3>
                        </div>
                      </div>
                    </div>
                    <div>




                        


                     

                    
                    ''')
            put_html(f'<h5><span> </span>'
                     f'<span> </span>'
                     f'<span> </span>'
                     f'<span> </span></h5>')
            # put_grid([[None,None,None,put_html('''
            #
            #
            #
            #   <a class="button"  style="--color:#1e9bff;">
            #     <span></span>
            #     <span></span>
            #     <span></span>
            #     <span></span>
            #     description
            #   </a>
            # </div>
            # ''').onclick(helpp),None,None]])
            put_html(f'<h5><span> </span>'
                     f'<span> </span>'
                     f'<span> </span>'
                     f'<span> </span></h5>')
            with  use_scope('1st',clear=True):

                put_grid([[None,None,put_html('''<svg fill="#ffffff" height="60px" width="60px" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 463 463" xml:space="preserve" stroke="#ffffff"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g> <path d="M223,47.5c0-12.958-10.542-23.5-23.5-23.5S176,34.542,176,47.5S186.542,71,199.5,71S223,60.458,223,47.5z M191,47.5 c0-4.687,3.813-8.5,8.5-8.5s8.5,3.813,8.5,8.5s-3.813,8.5-8.5,8.5S191,52.187,191,47.5z"></path> <path d="M263.5,71c12.958,0,23.5-10.542,23.5-23.5S276.458,24,263.5,24S240,34.542,240,47.5S250.542,71,263.5,71z M263.5,39 c4.687,0,8.5,3.813,8.5,8.5s-3.813,8.5-8.5,8.5s-8.5-3.813-8.5-8.5S258.813,39,263.5,39z"></path> <path d="M367,297.234v-27.469c9.29-3.138,16-11.93,16-22.266c0-12.958-10.542-23.5-23.5-23.5c-1.103,0-2.187,0.082-3.25,0.23 l-12.088-24.176c4.224-4.251,6.838-10.102,6.838-16.554c0-12.958-10.542-23.5-23.5-23.5c-0.167,0-0.333,0.013-0.5,0.016V151.5 c0-4.142-3.358-7.5-7.5-7.5H255v-17h8.5c12.958,0,23.5-10.542,23.5-23.5V95h16.5c4.142,0,7.5-3.358,7.5-7.5v-56 C311,14.131,296.869,0,279.5,0h-96C166.131,0,152,14.131,152,31.5v56c0,4.142,3.358,7.5,7.5,7.5H176v8.5 c0,12.958,10.542,23.5,23.5,23.5h8.5v17h-64.5c-4.142,0-7.5,3.358-7.5,7.5v8.516c-0.167-0.004-0.333-0.016-0.5-0.016 c-12.958,0-23.5,10.542-23.5,23.5c0,6.452,2.614,12.303,6.838,16.554L106.75,224.23c-1.063-0.148-2.147-0.23-3.25-0.23 C90.542,224,80,234.542,80,247.5c0,10.336,6.71,19.128,16,22.266v27.469c-9.29,3.138-16,11.93-16,22.266v16 c0,12.958,10.542,23.5,23.5,23.5s23.5-10.542,23.5-23.5c0-4.142-3.358-7.5-7.5-7.5s-7.5,3.358-7.5,7.5c0,4.687-3.813,8.5-8.5,8.5 s-8.5-3.813-8.5-8.5v-16c0-4.687,3.813-8.5,8.5-8.5c4.142,0,7.5-3.358,7.5-7.5v-33.734c9.29-3.138,16-11.93,16-22.266 c0-6.452-2.614-12.303-6.838-16.554l12.088-24.176c1.063,0.148,2.147,0.23,3.25,0.23c1.841,0,3.666-0.228,5.442-0.65 c6.848,15.092,20.246,26.602,36.555,30.858l13.774,41.322c-2.947,2.819-5.161,6.393-6.332,10.41 C175.165,291.786,168,300.819,168,311.5v48c0,10.336,6.71,19.128,16,22.266V416h-0.5c-17.369,0-31.5,14.131-31.5,31.5v8 c0,4.142,3.358,7.5,7.5,7.5h48c4.142,0,7.5-3.358,7.5-7.5v-32c0-4.142-3.358-7.5-7.5-7.5H199v-34.234 c9.29-3.138,16-11.93,16-22.266V319h33v40.5c0,10.336,6.71,19.128,16,22.266V416h-8.5c-4.142,0-7.5,3.358-7.5,7.5v32 c0,4.142,3.358,7.5,7.5,7.5h48c4.142,0,7.5-3.358,7.5-7.5v-8c0-17.369-14.131-31.5-31.5-31.5H279v-34.234 c9.29-3.138,16-11.93,16-22.266v-48c0-10.681-7.165-19.714-16.939-22.561c-1.17-4.018-3.385-7.591-6.332-10.41l13.774-41.322 c16.309-4.255,29.707-15.766,36.555-30.858c1.776,0.422,3.601,0.65,5.442,0.65c1.103,0,2.187-0.082,3.25-0.23l12.088,24.176 C338.614,235.197,336,241.048,336,247.5c0,10.336,6.71,19.128,16,22.266V303.5c0,4.142,3.358,7.5,7.5,7.5 c4.687,0,8.5,3.813,8.5,8.5v16c0,4.687-3.813,8.5-8.5,8.5s-8.5-3.813-8.5-8.5c0-4.142-3.358-7.5-7.5-7.5s-7.5,3.358-7.5,7.5 c0,12.958,10.542,23.5,23.5,23.5s23.5-10.542,23.5-23.5v-16C383,309.164,376.29,300.372,367,297.234z M200,448h-33v-0.5 c0-9.098,7.402-16.5,16.5-16.5H200V448z M296,447.5v0.5h-33v-17h16.5C288.598,431,296,438.402,296,447.5z M199,159h65v8.5 c0,13.509-10.991,24.5-24.5,24.5h-16c-13.509,0-24.5-10.991-24.5-24.5V159z M167,31.5c0-9.098,7.402-16.5,16.5-16.5h96 c9.098,0,16.5,7.402,16.5,16.5V80H167V31.5z M191,103.5V95h81v8.5c0,4.687-3.813,8.5-8.5,8.5h-64 C194.813,112,191,108.187,191,103.5z M223,127h17v17h-17V127z M103.5,256c-4.687,0-8.5-3.813-8.5-8.5s3.813-8.5,8.5-8.5 s8.5,3.813,8.5,8.5S108.187,256,103.5,256z M135.5,192c-4.687,0-8.5-3.813-8.5-8.5s3.813-8.5,8.5-8.5 c0.169,0,0.333,0.022,0.5,0.032v8.468c0,2.863,0.218,5.675,0.638,8.422C136.262,191.973,135.882,192,135.5,192z M266.094,248 h-69.188l-3-9h75.188L266.094,248z M264,295.5c0,4.687-3.813,8.5-8.5,8.5h-48c-4.687,0-8.5-3.813-8.5-8.5s3.813-8.5,8.5-8.5h48 C260.187,287,264,290.813,264,295.5z M191.5,368c-4.687,0-8.5-3.813-8.5-8.5v-48c0-2.599,1.175-4.926,3.019-6.487 c2.657,5.976,7.733,10.642,13.981,12.752V359.5C200,364.187,196.187,368,191.5,368z M280,359.5c0,4.687-3.813,8.5-8.5,8.5 s-8.5-3.813-8.5-8.5v-41.734c6.247-2.11,11.324-6.777,13.981-12.752c1.844,1.561,3.019,3.888,3.019,6.487V359.5z M255.5,272h-48 c-0.861,0-1.71,0.05-2.547,0.14l-3.047-9.14h59.188l-3.047,9.14C257.21,272.05,256.361,272,255.5,272z M312,183.5 c0,22.332-18.168,40.5-40.5,40.5h-80c-22.332,0-40.5-18.168-40.5-40.5V159h33v8.5c0,21.78,17.72,39.5,39.5,39.5h16 c21.78,0,39.5-17.72,39.5-39.5V159h33V183.5z M326.362,191.922c0.42-2.747,0.638-5.56,0.638-8.422v-8.468 c0.167-0.01,0.331-0.032,0.5-0.032c4.687,0,8.5,3.813,8.5,8.5s-3.813,8.5-8.5,8.5C327.118,192,326.738,191.973,326.362,191.922z M359.5,239c4.687,0,8.5,3.813,8.5,8.5s-3.813,8.5-8.5,8.5s-8.5-3.813-8.5-8.5S354.813,239,359.5,239z"></path> </g> </g></svg>'''),put_html('''

                    <h3 > What Do You Want Moi To call You ?</h3>


                    '''),None,None]])
            with use_scope(name='name', clear=True):
                put_html(f'<h5><span> </span>'
                         f'<span> </span>'
                         f'<span> </span></h5>')

            put_input('d', type=TEXT,placeholder='...NAME..')

        while True:
            pin_wait_change('d')

            with use_scope(name='1st', clear=True):

                put_grid([[None,None,None,put_html('''<svg fill="#ffffff" height="80px" width="80px" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 463 463" xml:space="preserve"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g> <path d="M207.5,95c10.336,0,19.128-6.71,22.266-16H271.5c4.142,0,7.5-3.358,7.5-7.5s-3.358-7.5-7.5-7.5h-41.734 c-3.138-9.29-11.93-16-22.266-16C194.542,48,184,58.542,184,71.5S194.542,95,207.5,95z M207.5,63c4.687,0,8.5,3.813,8.5,8.5 s-3.813,8.5-8.5,8.5s-8.5-3.813-8.5-8.5S202.813,63,207.5,63z"></path> <path d="M199.5,144h-16c-4.142,0-7.5,3.358-7.5,7.5s3.358,7.5,7.5,7.5h16c4.142,0,7.5-3.358,7.5-7.5S203.642,144,199.5,144z"></path> <path d="M239.5,144h-16c-4.142,0-7.5,3.358-7.5,7.5s3.358,7.5,7.5,7.5h16c4.142,0,7.5-3.358,7.5-7.5S243.642,144,239.5,144z"></path> <path d="M279.5,144h-16c-4.142,0-7.5,3.358-7.5,7.5s3.358,7.5,7.5,7.5h16c4.142,0,7.5-3.358,7.5-7.5S283.642,144,279.5,144z"></path> <path d="M351,272.913V143h0.5c12.958,0,23.5-10.542,23.5-23.5S364.458,96,351.5,96H319v-8.5C319,39.252,279.748,0,231.5,0 S144,39.252,144,87.5V96h-32.5C98.542,96,88,106.542,88,119.5S98.542,143,111.5,143h0.5v129.913 c-5.418,1.319-10.551,4.09-14.774,8.313c-12.282,12.282-12.282,32.266,0,44.548c2.929,2.929,7.678,2.929,10.606,0 c2.929-2.929,2.929-7.678,0-10.606c-6.433-6.434-6.433-16.901,0-23.335c3.117-3.116,7.26-4.833,11.667-4.833 s8.551,1.716,11.667,4.833c6.433,6.434,6.433,16.901,0,23.335c-2.929,2.929-2.929,7.678,0,10.606 c1.464,1.464,3.384,2.197,5.303,2.197s3.839-0.732,5.303-2.197c12.282-12.282,12.282-32.266,0-44.548 c-4.223-4.223-9.356-6.994-14.774-8.313V143h17v88.5c0,12.958,10.542,23.5,23.5,23.5H184v8.5c0,11.686,8.575,21.404,19.763,23.2 l3.675,22.049C184.323,318.25,168,341,168,367.5v32c0,4.142,3.358,7.5,7.5,7.5H200v24.5c0,17.369,14.131,31.5,31.5,31.5 s31.5-14.131,31.5-31.5V407h24.5c4.142,0,7.5-3.358,7.5-7.5v-32c0-26.5-16.323-49.25-39.438-58.751l3.675-22.049 C270.425,284.904,279,275.186,279,263.5V255h16.5c12.958,0,23.5-10.542,23.5-23.5V143h17v129.913 c-5.418,1.319-10.551,4.09-14.774,8.313c-12.282,12.282-12.282,32.266,0,44.548c2.929,2.929,7.678,2.929,10.606,0 c2.929-2.929,2.929-7.678,0-10.606c-6.433-6.434-6.433-16.901,0-23.335c3.117-3.116,7.26-4.833,11.667-4.833 s8.551,1.716,11.667,4.833c6.433,6.434,6.433,16.901,0,23.335c-2.929,2.929-2.929,7.678,0,10.606 c1.464,1.464,3.384,2.197,5.303,2.197s3.839-0.732,5.303-2.197c12.282-12.282,12.282-32.266,0-44.548 C361.551,277.003,356.418,274.232,351,272.913z M159,127h145v81H159V127z M159,87.5c0-39.977,32.523-72.5,72.5-72.5 S304,47.523,304,87.5V112H159V87.5z M111.5,128c-4.687,0-8.5-3.813-8.5-8.5s3.813-8.5,8.5-8.5H144v17H111.5z M248,431.5 c0,9.098-7.402,16.5-16.5,16.5s-16.5-7.402-16.5-16.5v-64c0-9.098,7.402-16.5,16.5-16.5s16.5,7.402,16.5,16.5V431.5z M280,367.5 V392h-17v-24.5c0-17.369-14.131-31.5-31.5-31.5S200,350.131,200,367.5V392h-17v-24.5c0-26.743,21.757-48.5,48.5-48.5 S280,340.757,280,367.5z M231.5,304c-3.238,0-6.419,0.247-9.527,0.716L219.02,287h24.96l-2.953,17.716 C237.919,304.247,234.738,304,231.5,304z M264,263.5c0,4.687-3.813,8.5-8.5,8.5h-48c-4.687,0-8.5-3.813-8.5-8.5V255h65V263.5z M295.5,240h-24h-80h-24c-4.687,0-8.5-3.813-8.5-8.5V223h145v8.5C304,236.187,300.187,240,295.5,240z M319,111h32.5 c4.687,0,8.5,3.813,8.5,8.5s-3.813,8.5-8.5,8.5H319V111z"></path> </g> </g></svg>'''),put_html(f'''<h1><span> Hoi,</span>
                                            <span>{pin.d}</span></h1>

                                           <span> </span>
                                                                                           <span> </span>
                                                                                           

            '''),None,None,None]])
            with use_scope(name='name', clear=True):

                put_html(f'''<h3><span>↶ Press to</span>
                                                            <span>the service </span> <span>  you want ↷</span></h3>

                                                            <span> </span>
                                                                                                           <span> </span>


                            ''')

                put_grid([[None, None, None,
                           put_button(label='Support Moi', outline=True, onclick=supmoi, color='success', small=True),
                           put_button(label='MoiAi', outline=True, onclick=retret, color='light', small=True),
                            None,
                           None]])
                put_html('<hr>')
                put_html('''<h5>
                                           <span> </span>
                                                                                           <span> </span>''')

            with use_scope(name='down', clear=True):
                put_html(''' <h5><span> </span>
                                                                                           <span> </span>
                                                                                           <span> </span>
                                                                                            <span> </span>

                                                                                                </h5>
                                                                                      ''')

                put_grid([[None, None, None, None, None]])
                put_html(''' <h5><span> </span>


                                                                        </h5>
                                                              ''')

                with use_scope(name='insta', clear=True):
                    put_grid([[None, None, None, put_html(''' 

                                      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"> 
                               <a href="https://www.instagram.com/savirax._33/" target="_blank" class="fa fa-instagram"></a>  
              '''), None, None]])

                put_grid([[None, None, put_html('''


                                           <h5><span> </span>
                                           <span> </span>

                                            <span>Learn more about us and be informed because we are the simplest for those who want to simplify ...!</span>

                                               </h5>

                            '''), None]])







def wepage():
    set_env(output_max_width='100%',output_animation =False,)
    with use_scope(name='allw', clear=True):
        put_html('''
     <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
      <h3>⠀⠀⠀⠀⠀⠀</h3>
       <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
       <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
       <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>

                <h3><span>WELCOME</span></h3>
    ''')

    time.sleep(2)
    with use_scope(name='allw', clear=True):
        put_html('''
     <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
      <h3>⠀⠀⠀⠀⠀⠀</h3>
       <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
       <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
       <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>

                <h3><span>TO</span></h3>
    ''')

    time.sleep(2)
    with use_scope(name='allw',clear=True):
        put_html('''
             <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
              <h3>⠀⠀⠀⠀⠀⠀</h3>
               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>

                        <h3><span>Another</span>
                        <span>Level</span>
                        </h3>
            ''')
    time.sleep(2)

    with use_scope(name='allw',clear=True):
        put_html('''
             <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
              <h3>⠀⠀⠀⠀⠀⠀</h3>
               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>

                        <h3><span>O</span>
                        <span>F</span>
                        </h3>
            ''')
    time.sleep(2)


    with use_scope(name='allw',clear=True):
        time.sleep(0.5)
        put_html('''
        
         <h3>⠀⠀⠀⠀⠀⠀⠀⠀</h3>
              <h3>⠀⠀⠀⠀⠀⠀</h3>
               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>
               <h3>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h3>

        
        
        <div class="container">
                      <div class="row">
                        <div class="col-md-12 text-center">
                          <h3 class="animate-charcter"> MoiApps </h3>
                          
                        </div>
                      </div>
                    </div>
                    <div>
        ''')
        time.sleep(2)
        wopen()

















class Wmoi:
    def rettur(self):


        To_Know_The_Celint = get_localstorage(key='moiiforutest')





        if To_Know_The_Celint == None or To_Know_The_Celint == 'None':
                 wepage()

        else:

                    from app import firstpage
                    go_app('firstpage', new_window=False)
                    firstpage()







