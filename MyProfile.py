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



def picai():
    with use_scope('hide',clear=True):
        pass
    toast('Lets Get Into It')
    time.sleep(2)
    toast('Lets Get Into It Please Wait..',color='warn')
    response = openai.Image.create(
        prompt=f"create profile photo for men human not art ",
        n=1,
        size="1024x1024",

    )
    toast('Almost Done Wait...', color='warn')
    time.sleep(1)
    print(response)
    set_localstorage(key='piclink',value=f'{response["data"][0]["url"]}')
    toast('Done')
    time.sleep(1)
    run_js('window.location.reload();')


def start():
    set_env(output_max_width='100%')

    To_Know_The_Celint = get_localstorage(key='moiiforutest')
    To_Know_user = get_localstorage(key='moiusename')

    if To_Know_The_Celint == None or To_Know_The_Celint == 'None':
        go_app('firstrunmoi', new_window=False)

    set_env(title='MoiAi')
    logo(2)
    with use_scope(name='appsbt', clear=True):
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
        profile_pic=get_localstorage('piclink')
        print(profile_pic)
        put_grid([[None,None,put_html('<h4>Change My Profile Pic Using Ai :</h4>'),None]
                     ,[None,None,None,None,put_scope('hide',[put_html('''<button class="bubbly-button">Click me!</button>

<style>
.bubbly-button {
  font-family: "Helvetica", "Arial", sans-serif;
  display: inline-block;
  font-size: 0.9em;
 
 

  -webkit-appearance: none;
  appearance: none;
  background-color: #ff0081;
  color: #fff;
  border-radius: 100px;
  border: none;
  cursor: pointer;
  position: relative;
  transition: transform ease-in 0.1s, box-shadow ease-in 0.25s;
  box-shadow: 0 2px 25px rgba(255, 0, 130, 0.5);
}
.bubbly-button:focus {
  outline: 0;
}
.bubbly-button:before, .bubbly-button:after {
  position: absolute;
  content: "";
  display: block;
  width: 140%;
  height: 100%;
  left: -20%;
  z-index: -1000;
  transition: all ease-in-out 0.5s;
  background-repeat: no-repeat;
}
.bubbly-button:before {
  display: none;
  top: -75%;
  background-image: radial-gradient(circle, #ff0081 20%, transparent 20%), radial-gradient(circle, transparent 20%, #ff0081 20%, transparent 30%), radial-gradient(circle, #ff0081 20%, transparent 20%), radial-gradient(circle, #ff0081 20%, transparent 20%), radial-gradient(circle, transparent 10%, #ff0081 15%, transparent 20%), radial-gradient(circle, #ff0081 20%, transparent 20%), radial-gradient(circle, #ff0081 20%, transparent 20%), radial-gradient(circle, #ff0081 20%, transparent 20%), radial-gradient(circle, #ff0081 20%, transparent 20%);
  background-size: 10% 10%, 20% 20%, 15% 15%, 20% 20%, 18% 18%, 10% 10%, 15% 15%, 10% 10%, 18% 18%;
}
.bubbly-button:after {
  display: none;
  bottom: -75%;
  background-image: radial-gradient(circle, #ff0081 20%, transparent 20%), radial-gradient(circle, #ff0081 20%, transparent 20%), radial-gradient(circle, transparent 10%, #ff0081 15%, transparent 20%), radial-gradient(circle, #ff0081 20%, transparent 20%), radial-gradient(circle, #ff0081 20%, transparent 20%), radial-gradient(circle, #ff0081 20%, transparent 20%), radial-gradient(circle, #ff0081 20%, transparent 20%);
  background-size: 15% 15%, 20% 20%, 18% 18%, 20% 20%, 15% 15%, 10% 10%, 20% 20%;
}
.bubbly-button:active {
  transform: scale(0.9);
  background-color: #e60074;
  box-shadow: 0 2px 25px rgba(255, 0, 130, 0.2);
}
.bubbly-button.animate:before {
  display: block;
  animation: topBubbles ease-in-out 0.75s forwards;
}
.bubbly-button.animate:after {
  display: block;
  animation: bottomBubbles ease-in-out 0.75s forwards;
}

@keyframes topBubbles {
  0% {
    background-position: 5% 90%, 10% 90%, 10% 90%, 15% 90%, 25% 90%, 25% 90%, 40% 90%, 55% 90%, 70% 90%;
  }
  50% {
    background-position: 0% 80%, 0% 20%, 10% 40%, 20% 0%, 30% 30%, 22% 50%, 50% 50%, 65% 20%, 90% 30%;
  }
  100% {
    background-position: 0% 70%, 0% 10%, 10% 30%, 20% -10%, 30% 20%, 22% 40%, 50% 40%, 65% 10%, 90% 20%;
    background-size: 0% 0%, 0% 0%, 0% 0%, 0% 0%, 0% 0%, 0% 0%;
  }
}
@keyframes bottomBubbles {
  0% {
    background-position: 10% -10%, 30% 10%, 55% -10%, 70% -10%, 85% -10%, 70% -10%, 70% 0%;
  }
  50% {
    background-position: 0% 80%, 20% 80%, 45% 60%, 60% 100%, 75% 70%, 95% 60%, 105% 0%;
  }
  100% {
    background-position: 0% 90%, 20% 90%, 45% 70%, 60% 110%, 75% 80%, 95% 70%, 110% 10%;
    background-size: 0% 0%, 0% 0%, 0% 0%, 0% 0%, 0% 0%, 0% 0%;
  }
}</style>

<script>var animateButton = function (e) {
  e.preventDefault;
  //reset animation
  e.target.classList.remove("animate");

  e.target.classList.add("animate");
  setTimeout(function () {
    e.target.classList.remove("animate");
  }, 700);
};

var bubblyButtons = document.getElementsByClassName("bubbly-button");

for (var i = 0; i < bubblyButtons.length; i++) {
  bubblyButtons[i].addEventListener("click", animateButton, false);
}

</script>''').onclick(picai)]),None,None]])
        put_html('‎ ')
        put_html('‎ ')
        put_grid([[None,None,None,put_html(f'''<div class="wrapper">
  <div class="profile-card js-profile-card">
    <div class="profile-card__img">
      <img src="{profile_pic}" alt="profile card">
    </div>

    <div class="profile-card__cnt js-profile-cnt">
      <div class="profile-card__name">{To_Know_user}</div>
      <div class="profile-card__txt">MoiClient <strong>Human Control Ai</strong></div>
      <div class="profile-card-loc">
        <span class="profile-card-loc__icon">
          <svg class="icon">
            <use xlink:href="#icon-location"></use>
          </svg>
        </span>

       
      </div>

      


      
     

    <div class="profile-card-message js-message">
      <form class="profile-card-form">
        <div class="profile-card-form__container">
          <textarea placeholder="Say something..."></textarea>
        </div>

        <div class="profile-card-form__bottom">
          <button class="profile-card__button button--blue js-message-close">
            Send
          </button>

          <button class="profile-card__button button--gray js-message-close">
            Cancel
          </button>
        </div>
      </form>

      <div class="profile-card__overlay js-message-close"></div>
    </div>

  </div>

</div>
'''),None,None,None]])

    with use_scope(name='main', clear=True):
        pass
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
                                       <li><a href="https://lookingforsponsor.com/app/opportunities/8327974312_KQlvZ9fyetduyl4Wb70v">Place of sponsor</a></li>
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



class MoiProfile_New_Page:
    def rettur(self):


        start()