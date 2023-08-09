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

config(title='dd',css_style='''


.button-33 {
  background-color: #c2fbd7;
  border-radius: 100px;
  box-shadow: rgba(44, 187, 99, .2) 0 -25px 18px -14px inset,rgba(44, 187, 99, .15) 0 1px 2px,rgba(44, 187, 99, .15) 0 2px 4px,rgba(44, 187, 99, .15) 0 4px 8px,rgba(44, 187, 99, .15) 0 8px 16px,rgba(44, 187, 99, .15) 0 16px 32px;
  color: green;
  cursor: pointer;
  display: inline-block;
  font-family: CerebriSans-Regular,-apple-system,system-ui,Roboto,sans-serif;
  padding: 2px 9px;
  text-align: center;
  text-decoration: none;
  transition: all 250ms;
  border: 0;
  font-size: 13px;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.button-33:hover {
  box-shadow: rgba(44,187,99,.35) 0 -25px 18px -14px inset,rgba(44,187,99,.25) 0 1px 2px,rgba(44,187,99,.25) 0 2px 4px,rgba(44,187,99,.25) 0 4px 8px,rgba(44,187,99,.25) 0 8px 16px,rgba(44,187,99,.25) 0 16px 32px;
  transform: scale(1.05) rotate(-1deg);
}
''')
def t():
    put_html('''<img width="44" height="44" src="https://img.icons8.com/3d-fluency/94/module.png" alt="module"/>''')
    put_html('''<img width="44" height="44" src="https://img.icons8.com/3d-fluency/94/control-panel.png" alt="control-panel"/>''')
    put_html('''<img width="44" height="44" src="https://img.icons8.com/color/96/000000/artificial-intelligence.png" alt="artificial-intelligence"/>''')
    put_html('''<img width="44" height="44" src="https://img.icons8.com/3d-fluency/94/chatbot.png" alt="chatbot"/>''')
    put_html('''
<button class="button-33" role="button">Button 33</button>
''')

start_server(t,port=1231)