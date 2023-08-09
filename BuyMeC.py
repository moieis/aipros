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






def backk():
    go_app(name='firstpage', new_window=False)
def start():
    put_grid([[None,None,None,put_text('😊'),None,None]])

    put_grid([[None,None,None,put_html('''<script async
  src="https://js.stripe.com/v3/buy-button.js">
</script>

<stripe-buy-button
  buy-button-id="buy_btn_1NcICTIsYdq0egIJaf5eS81g"
  publishable-key="pk_live_51NYLWpIsYdq0egIJD1clHa5ziHfQ91WHyTS7TIXpXfhujOC9WgQme90Gdnx5XWKPIIRA9IMiUDzPIrVOpH5kWauY00k6xgTKNI"
>
</stripe-buy-button>'''),None,None]])
    put_grid([[None,None,None,put_button(label='Back To Ai',onclick=backk),None,None]])



class BuyMeC_New_Page:
    def rettur(self):


        start()