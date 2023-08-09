from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.platform import *
from pywebio.session import *
import time
import openai
from pywebio_battery import *
from datetime import datetime
import random
import urllib.request
from itranslate import itranslate

fir = 'sk-1YarzJpmgJAvj5Fwm9H'
sc = 'PT3BlbkFJBzEe11JamrLJM1RNVQIj'
openai.api_key = fir + sc
sty = ['nov']

sty.clear()
url_i = ['https://assets.website-files.com/61554cf069663530fc823d21/615892bd22b48c2408114c38_1-min.png',
         'https://hotpotmedia.s3.us-east-2.amazonaws.com/8-wuipF6eaCRZ3ImV.png',
         'https://hotpotmedia.s3.us-east-2.amazonaws.com/8-BUwnSe6eQQb7Td3.png',
         'https://hotpotmedia.s3.us-east-2.amazonaws.com/RBv8rnAKCQV3eajiuEeZQsBXusQ2.png',
         'https://hotpotmedia.s3.us-east-2.amazonaws.com/8-GHdrMyVJzsUC5Id.png',
         'https://hotpotmedia.s3.us-east-2.amazonaws.com/8-Yzm7akDw421tN1C.png',
         'https://hotpotmedia.s3.us-east-2.amazonaws.com/8-Jw8ejjdD0zOQIVy.png',
         'https://hotpotmedia.s3.us-east-2.amazonaws.com/8-ovIk68Py2GIwJjJ.png',
         'https://hotpotmedia.s3.us-east-2.amazonaws.com/8-q4j7qAUMwNz1CDY.png',

         'https://hotpotmedia.s3.us-east-2.amazonaws.com/8-JHbNDMYfIn3UWpb.png',

         'https://hotpotmedia.s3.us-east-2.amazonaws.com/8-PRedHE2xivMPPzu.png',
         'https://hotpotmedia.s3.us-east-2.amazonaws.com/8-Z7mAywUap4F42Qp.png'
         ]

txt_i_1 = [
    'Artificial intelligence drawing feelings ',
    'A world that starts with just an idea !',
    "@idea@, Then translated into something practical, and then returned to an idea in the mind of a machine after an era of the best of it",
    "MoiEis Learn more about us and be informed because we are the simplest for those who want to simplify ...!"]


def vedio():
    v = open('moihelp.mp4', 'rb').read()

    popup('Help Video ByMoi',
          put_grid([[None, None, None, put_video(v, autoplay=True, loop=True, muted=True, width="200", height="100"),
                     None, None, None]]), implicit_close=True)


def imp(x, y):
    set_env(title=f'{y}')
    clear(scope='main')
    clear(scope='down')
    if x == 'natural':
        # try:
            with use_scope(name='title', clear=True):
                put_grid([[None, None, put_loading(shape='grow', color='info'), None]])

                response = openai.Image.create(
                    prompt=f"{y}",
                    n=1,
                    size="1024x1024",

                )
                print(response)

                try:

                    dataa = open('moipicc.txt', 'a')
                    dataa.write(f'----------{info}----------\n')
                    dataa.write(f'============{y}============\n')
                    dataa.write(f'============{x}============\n')
                    dataa.close()

                except:
                    dataaa = open('moipicc.txt', 'a', encoding='utf-8')
                    dataaa.write(f'----------{info}----------\n')
                    dataaa.write(f'============{y}============\n')
                    dataaa.write(f'============{x}============\n')
                    dataaa.close()





        # except:
        #     clear(scope='title')
        #     toast('Make sure of your inputs and refresh the page !!', color='warn')
        #     time.sleep(2)
        #     run_js('window.location.reload();')

    else:
        try:
            with use_scope(name='title', clear=True):
                put_grid([[None, None, put_loading(shape='grow', color='info'), None]])
                response = openai.Image.create(
                    prompt=f"{x} STYLE {y}",
                    n=1,
                    size="1024x1024",

                )
                try:

                    dataa = open('moipicc.txt', 'a')
                    dataa.write(f'----------{info}----------\n')
                    dataa.write(f'============{y}============\n')
                    dataa.write(f'============{x}============\n')
                    dataa.close()

                except:
                    dataa = open('moipicc.txt', 'a', encoding='utf-8')
                    dataa.write(f'----------{info}----------\n')
                    dataa.write(f'============{y}============\n')
                    dataa.write(f'============{x}============\n')
                    dataa.close()




        except:
            clear(scope='title')
            toast('Make sure of your inputs and refresh the page !!', color='warn')
            time.sleep(2)
            run_js('window.location.reload();')

    try:
        image_url_1 = response['data'][0]['url']
        image_url_2 = response['data'][1]['url']
        print(image_url_2)
    except:
        pass
    with use_scope('title', clear=True):

        put_grid([[None, None, put_image(image_url_1, width='400', height='400'), None]])

    with use_scope(name='main', clear=True):

        def d():
            with use_scope(name='down', clear=True):
                put_grid([[None, None, None, None, put_button(label='Download', onclick=d, color='info', disabled=True),
                           None, None, None]])
            urllib.request.urlretrieve(image_url_1, filename=f'{y} By MOiPi.jpg')
            my_im = open(f'{y} By MOiPi.jpg', 'rb').read()
            download(f'{y} By MOiPi.jpg', content=my_im)
            with use_scope(name='down', clear=True):
                put_grid([[None, None, None, None,
                           put_button(label='Download', onclick=d, outline=True, color='info', disabled=False), None,
                           None, None]])

        put_html('<hr>')
    with use_scope(name='down', clear=True):
        put_grid([[None, None, None, None, put_button(label='Download', onclick=d, color='info'), None, None, None]])


def transfirre_imp():
    imp(sty[-1],pin.ai )
    # itranslate(pin.ai, from_lang='auto', to_lang='en')


def proses():
    set_env(title='MoiDraw', output_max_width='110%')
    sty.append(pin.stty)
    put_html('<style>body {font-family: Courier New; }</style')

    with use_scope(name='main', clear=True):
        put_html('<hr>')
        put_grid([[None, None, put_html('<h3>Make MoiPic Draw :</h3>'), None]])
        put_grid([[None, put_input(name='ai', type=TEXT, placeholder='Feel before writing ...'), None]])
        put_html('<hr>')
    with use_scope(name='down', clear=True):
        put_grid([[None, None, put_button(label='Draw', onclick=transfirre_imp, color='dark', outline=False)
                      , None]])


def Ai_G():
    set_env(title='style', output_max_width='110%', output_animation=False)
    clear(scope='down')
    with use_scope(name='title', clear=True):
        pass
    clear(scope='main')
    with use_scope(name='main', clear=True):
        # put_image('https://imgs.search.brave.com/AMX5wlcN-1MFZDagpugX_i1lYRUiL68dUPiQvPE4nvU/rs:fit:1006:1014:1/g:ce/aHR0cDovL2NhbnZh/cy1jb3V0dXJlLmNv/LnVrL3dwLWNvbnRl/bnQvdXBsb2Fkcy8y/MDE0LzA5L3R1bWJs/cl9zdGF0aWNfY3Zu/cGd4YWdsdTA0b28w/d2NrOGdzZ3MwNC5q/cGc')
        # fantasy
        # anime
        # midjourney
        # natural https://oaidalleapiprodscus.blob.core.windows.net/private/org-bxpHHPqfo6i5FxZdD5lbjYiJ/user-JEUd1c553LeKBYFWQwWYQ0AC/img-YCfBVdQtglEm8jO8DyU0giuG.png?st=2022-12-23T17%3A08%3A03Z&se=2022-12-23T19%3A08%3A03Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-12-23T13%3A39%3A04Z&ske=2022-12-24T13%3A39%3A04Z&sks=b&skv=2021-08-06&sig=mtScpgwjYn73DDvJwrvccTJA0twcG2JaxQA2ihwqmw8%3D
        #

        put_html('<hr>')
        put_grid([[None, put_html('<h4>Choose the style you want me to draw :</h4>'), None, None]])
        put_grid([[None, None, put_radio(name='stty',
                                         options=['painting', 'fantasy', 'anime', 'natural', '3d art animation'],inline=True
                                         ), None, None]])
        put_html('<hr>')

        while True:
            pin_wait_change('stty')
            if str(pin.stty) == 'painting':
                with use_scope(name='title', clear=True):
                    put_html('<hr>')
                    pan = open('pp.jpeg', 'rb').read()
                    put_grid([[None, None, None, put_image(pan, width='400', height='300').style('''    width: 80%;
    background-color: white;
    box-shadow: 0 9px 16px 0 rgb(0 0 0 / 20%), 0 6px 20px 0 rgb(0 0 0 / 19%);
    margin-bottom: 25px;
    border-radius: 55px;'''), None, None]])

            if str(pin.stty) == 'fantasy':
                with use_scope(name='title', clear=True):
                    fan = open('ff.jpeg', 'rb').read()
                    put_html('<hr>')
                    put_grid([[None, None, None, put_image(fan
                                                           , width='400', height='300').style('''    width: 80%;
    background-color: white;
    box-shadow: 0 9px 16px 0 rgb(0 0 0 / 20%), 0 6px 20px 0 rgb(0 0 0 / 19%);
    margin-bottom: 25px;
    border-radius: 55px;'''), None, None]])

            if str(pin.stty) == 'anime':
                with use_scope(name='title', clear=True):
                    ani = open('aa.jpeg', 'rb').read()
                    put_html('<hr>')
                    put_grid([[None, None, None, put_image(ani
                                                           , width='450', height='300').style('''    width: 80%;
    background-color: white;
    box-shadow: 0 9px 16px 0 rgb(0 0 0 / 20%), 0 6px 20px 0 rgb(0 0 0 / 19%);
    margin-bottom: 25px;
    border-radius: 55px;'''), None, None]])

            if str(pin.stty) == 'natural':
                with use_scope(name='title', clear=True):
                    put_html('<hr>')

                    nan = open('nn.jpeg', 'rb').read()
                    put_grid([[None, None, None, put_image(nan, width='450', height='300').style('''    width: 80%;
    background-color: white;
    box-shadow: 0 9px 16px 0 rgb(0 0 0 / 20%), 0 6px 20px 0 rgb(0 0 0 / 19%);
    margin-bottom: 25px;
    border-radius: 55px;'''), None, None]])

            if str(pin.stty) == '3d art animation':
                with use_scope(name='title', clear=True):
                    put_html('<hr>')
                    thre = open('3d.jpeg', 'rb').read()
                    put_grid([[None, None, None, put_image(
                        thre, width='450', height='300').style('''    width: 80%;
    background-color: white;
    box-shadow: 0 9px 16px 0 rgb(0 0 0 / 20%), 0 6px 20px 0 rgb(0 0 0 / 19%);
    margin-bottom: 25px;
    border-radius: 55px;'''), None, None]])

            with use_scope(name='down', clear=True):
                put_grid([[None, None, None, put_button(label='Next', onclick=proses, outline=True, color='dark'), None,
                           None]])


def start():
    set_env(output_max_width='110%')
    To_Know_user = get_localstorage(key='moiusename')

    with use_scope(name='logoo', clear=True):
        im = open('moi.png', 'rb').read()

        put_grid([[None, None, None, None, put_image(im, width='150', height='150'), None, None, None]])

    put_html('<h3><span>‎ ‎ ‎ </span></h3>'
             '<h3><span>‎ ‎ ‎ </span></h3>')
    with use_scope(name='title', clear=True):
        pass
    with use_scope(name='main', clear=True):
        put_html(f'''<!-- 
Please note, that you can apply .m--global-blending-active to .fnc-slider 
to enable blend-mode for all background-images or apply .m--blend-bg-active
to some specific slides (.fnc-slide). It's disabled by default in this demo,
because it requires specific images, where more than 50% of bg is transparent or monotone
-->
<div class="demo-cont">
  <!-- slider start -->
  <div class="fnc-slider example-slider">
    <div class="fnc-slider__slides">
      <!-- slide start -->
      <div class="fnc-slide m--blend-green m--active-slide">
        <div class="fnc-slide__inner">
          <div class="fnc-slide__mask">
            <div class="fnc-slide__mask-inner"></div>
          </div>
          <div class="fnc-slide__content">
            <h2 class="fnc-slide__heading">
              <div class="fnc-slide__heading-line">
                <span>{To_Know_user} idea</span>
              </div>

              <div class="fnc-slide__heading-line">
                <span>to</span>
              </div>


              <div class="fnc-slide__heading-line">
                <span>{To_Know_user} writing</span>
              </div>


              <div class="fnc-slide__heading-line">
                <span>‎‎‎ then</span>
              </div>

              <div class="fnc-slide__heading-line">
                <span>Moi pic</span>
              </div>


            </h2>
            <button type="button" class="fnc-slide__action-btn">
              More
              <span data-text="More">More</span>
            </button>
          </div>
        </div>
      </div>
      <!-- slide end -->
      <!-- slide start -->
      <div class="fnc-slide m--blend-dark">
        <div class="fnc-slide__inner">
          <div class="fnc-slide__mask">
            <div class="fnc-slide__mask-inner"></div>
          </div>
          <div class="fnc-slide__content">
            <h2 class="fnc-slide__heading">
              <div class="fnc-slide__heading-line">
                <span>moi</span>
              </div>

              <div class="fnc-slide__heading-line">
                <span>ai</span>
              </div>


              <div class="fnc-slide__heading-line">
                <span>is whatever</span>
              </div>


              <div class="fnc-slide__heading-line">
                <span>hasn't been done yet</span>
              </div>


            </h2>
            <button type="button" class="fnc-slide__action-btn">
              More
              <span data-text="More">More</span>
            </button>
          </div>
        </div>
      </div>
      <!-- slide end -->
      <!-- slide start -->
      <div class="fnc-slide m--blend-red">
        <div class="fnc-slide__inner">
          <div class="fnc-slide__mask">
            <div class="fnc-slide__mask-inner"></div>
          </div>
          <div class="fnc-slide__content">
            <h1 class="fnc-slide__heading">
              <div class="fnc-slide__heading-line">
                <span>Down the page</span>
              </div>
              <div class="fnc-slide__heading-line">
                <span>press on</span>
              </div>
              <div class="fnc-slide__heading-line">
                <span>Tips for </span>
              </div>
              <div class="fnc-slide__heading-line">
                <span>improving MoiAi</span>
              </div>

              <div class="fnc-slide__heading-line">
                <span>and let's build</span>
              </div>

              <div class="fnc-slide__heading-line">
                <span>moiai together</span>
              </div>

            </h1>




            <button type="button" class="fnc-slide__action-btn">
              More
              <span data-text="More">More</span>
            </button>
          </div>
        </div>
      </div>
      <!-- slide end -->
      <!-- slide start -->
      <div class="fnc-slide m--blend-blue">
        <div class="fnc-slide__inner">
          <div class="fnc-slide__mask">
            <div class="fnc-slide__mask-inner"></div>
          </div>
          <div class="fnc-slide__content">



            <h1 class="fnc-slide__heading">
              <div class="fnc-slide__heading-line">
                <span>think outside</span>
              </div>
              <div class="fnc-slide__heading-line">
                <span>the box</span>
              </div>

              <div class="fnc-slide__heading-line">
                <span>to get</span>
              </div>

              <div class="fnc-slide__heading-line">
                <span>the highest </span>
              </div>

              <div class="fnc-slide__heading-line">
                <span>value&score</span>
              </div>

            </h1>
            <button type="button" class="fnc-slide__action-btn">
              Credits
              <span data-text="Credits">More</span>
            </button>
          </div>
        </div>
      </div>
      <!-- slide end -->
    </div>
    <nav class="fnc-nav">
      <div class="fnc-nav__bgs">
        <div class="fnc-nav__bg m--navbg-green m--active-nav-bg"></div>
        <div class="fnc-nav__bg m--navbg-dark"></div>
        <div class="fnc-nav__bg m--navbg-red"></div>
        <div class="fnc-nav__bg m--navbg-blue"></div>
      </div>
      <div class="fnc-nav__controls">
        <button class="fnc-nav__control">
          Steps
          <span class="fnc-nav__control-progress"></span>
        </button>
        <button class="fnc-nav__control">
          To know
          <span class="fnc-nav__control-progress"></span>
        </button>
        <button class="fnc-nav__control">
          {To_Know_user}
          <span class="fnc-nav__control-progress"></span>
        </button>
        <button class="fnc-nav__control">
           r
          <span class="fnc-nav__control-progress"></span>
        </button>
      </div>
    </nav>
  </div>
  <!-- slider end -->
  <div class="demo-cont__credits">
    <div class="demo-cont__credits-close"></div>
    <h2 class="demo-cont__credits-heading">MoiPic</h2>
    <img src="" alt="" class="demo-cont__credits-img" />
    <h3 class="demo-cont__credits-name">About</h3>
    <a href="https://znap.link/MoiCbio" target="_blank" class="demo-cont__credits-link">my all</a>
    <a href="https://bizb.io/3c0e14b5_4447_4ca3_85c6_32c2c1493260" target="_blank" class="demo-cont__credits-link">support moi</a>
    <h2 class="demo-cont__credits-heading">Do Effect</h2>

    <h4 class="demo-cont__credits-blend">Global Blend Mode</h4>
    <div class="colorful-switch">
      <input type="checkbox" class="colorful-switch__checkbox js-activate-global-blending" id="colorful-switch-cb" />
      <label class="colorful-switch__label" for="colorful-switch-cb">
        <span class="colorful-switch__bg"></span>
        <span class="colorful-switch__dot"></span>
        <span class="colorful-switch__on">
          <span class="colorful-switch__on__inner"></span>
        </span>
        <span class="colorful-switch__off"></span>
      </label>
    </div>
  </div>
</div>

''' + '''
<script>
(function () {
  var $$ = function (selector, context) {
    var context = context || document;
    var elements = context.querySelectorAll(selector);
    return [].slice.call(elements);
  };

  function _fncSliderInit($slider, options) {
    var prefix = ".fnc-";

    var $slider = $slider;
    var $slidesCont = $slider.querySelector(prefix + "slider__slides");
    var $slides = $$(prefix + "slide", $slider);
    var $controls = $$(prefix + "nav__control", $slider);
    var $controlsBgs = $$(prefix + "nav__bg", $slider);
    var $progressAS = $$(prefix + "nav__control-progress", $slider);

    var numOfSlides = $slides.length;
    var curSlide = 1;
    var sliding = false;
    var slidingAT =
      +parseFloat(getComputedStyle($slidesCont)["transition-duration"]) * 1000;
    var slidingDelay =
      +parseFloat(getComputedStyle($slidesCont)["transition-delay"]) * 1000;

    var autoSlidingActive = false;
    var autoSlidingTO;
    var autoSlidingDelay = 5000; // default autosliding delay value
    var autoSlidingBlocked = false;

    var $activeSlide;
    var $activeControlsBg;
    var $prevControl;

    function setIDs() {
      $slides.forEach(function ($slide, index) {
        $slide.classList.add("fnc-slide-" + (index + 1));
      });

      $controls.forEach(function ($control, index) {
        $control.setAttribute("data-slide", index + 1);
        $control.classList.add("fnc-nav__control-" + (index + 1));
      });

      $controlsBgs.forEach(function ($bg, index) {
        $bg.classList.add("fnc-nav__bg-" + (index + 1));
      });
    }

    setIDs();

    function afterSlidingHandler() {
      $slider
        .querySelector(".m--previous-slide")
        .classList.remove("m--active-slide", "m--previous-slide");
      $slider
        .querySelector(".m--previous-nav-bg")
        .classList.remove("m--active-nav-bg", "m--previous-nav-bg");

      $activeSlide.classList.remove("m--before-sliding");
      $activeControlsBg.classList.remove("m--nav-bg-before");
      $prevControl.classList.remove("m--prev-control");
      $prevControl.classList.add("m--reset-progress");
      var triggerLayout = $prevControl.offsetTop;
      $prevControl.classList.remove("m--reset-progress");

      sliding = false;
      var layoutTrigger = $slider.offsetTop;

      if (autoSlidingActive && !autoSlidingBlocked) {
        setAutoslidingTO();
      }
    }

    function performSliding(slideID) {
      if (sliding) return;
      sliding = true;
      window.clearTimeout(autoSlidingTO);
      curSlide = slideID;

      $prevControl = $slider.querySelector(".m--active-control");
      $prevControl.classList.remove("m--active-control");
      $prevControl.classList.add("m--prev-control");
      $slider
        .querySelector(prefix + "nav__control-" + slideID)
        .classList.add("m--active-control");

      $activeSlide = $slider.querySelector(prefix + "slide-" + slideID);
      $activeControlsBg = $slider.querySelector(prefix + "nav__bg-" + slideID);

      $slider
        .querySelector(".m--active-slide")
        .classList.add("m--previous-slide");
      $slider
        .querySelector(".m--active-nav-bg")
        .classList.add("m--previous-nav-bg");

      $activeSlide.classList.add("m--before-sliding");
      $activeControlsBg.classList.add("m--nav-bg-before");

      var layoutTrigger = $activeSlide.offsetTop;

      $activeSlide.classList.add("m--active-slide");
      $activeControlsBg.classList.add("m--active-nav-bg");

      setTimeout(afterSlidingHandler, slidingAT + slidingDelay);
    }

    function controlClickHandler() {
      if (sliding) return;
      if (this.classList.contains("m--active-control")) return;
      if (options.blockASafterClick) {
        autoSlidingBlocked = true;
        $slider.classList.add("m--autosliding-blocked");
      }

      var slideID = +this.getAttribute("data-slide");

      performSliding(slideID);
    }

    $controls.forEach(function ($control) {
      $control.addEventListener("click", controlClickHandler);
    });

    function setAutoslidingTO() {
      window.clearTimeout(autoSlidingTO);
      var delay = +options.autoSlidingDelay || autoSlidingDelay;
      curSlide++;
      if (curSlide > numOfSlides) curSlide = 1;

      autoSlidingTO = setTimeout(function () {
        performSliding(curSlide);
      }, delay);
    }

    if (options.autoSliding || +options.autoSlidingDelay > 0) {
      if (options.autoSliding === false) return;

      autoSlidingActive = true;
      setAutoslidingTO();

      $slider.classList.add("m--with-autosliding");
      var triggerLayout = $slider.offsetTop;

      var delay = +options.autoSlidingDelay || autoSlidingDelay;
      delay += slidingDelay + slidingAT;

      $progressAS.forEach(function ($progress) {
        $progress.style.transition = "transform " + delay / 1000 + "s";
      });
    }

    $slider
      .querySelector(".fnc-nav__control:first-child")
      .classList.add("m--active-control");
  }

  var fncSlider = function (sliderSelector, options) {
    var $sliders = $$(sliderSelector);

    $sliders.forEach(function ($slider) {
      _fncSliderInit($slider, options);
    });
  };

  window.fncSlider = fncSlider;
})();

/* not part of the slider scripts */

/* Slider initialization
options:
autoSliding - boolean
autoSlidingDelay - delay in ms. If audoSliding is on and no value provided, default value is 5000
blockASafterClick - boolean. If user clicked any sliding control, autosliding won't start again
*/
fncSlider(".example-slider", { autoSlidingDelay: 4000 });

var $demoCont = document.querySelector(".demo-cont");

[].slice
  .call(document.querySelectorAll(".fnc-slide__action-btn"))
  .forEach(function ($btn) {
    $btn.addEventListener("click", function () {
      $demoCont.classList.toggle("credits-active");
    });
  });

document
  .querySelector(".demo-cont__credits-close")
  .addEventListener("click", function () {
    $demoCont.classList.remove("credits-active");
  });

document
  .querySelector(".js-activate-global-blending")
  .addEventListener("click", function () {
    document
      .querySelector(".example-slider")
      .classList.toggle("m--global-blending-active");
  });




</script>''')

    with use_scope(name='down', clear=True):
        put_html('<h3><span>‎ ‎ ‎ </span></h3>'
                 '<h3><span>‎ ‎ ‎ </span></h3>')
        put_grid([[None, None, put_html('''

<button class="button-50" role="button">Ai Art Generator</button>
''').onclick(Ai_G), None, None]])

    with use_scope(name='foo', clear=True):
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
                                    <li><a href="?app=togather">Tips for improving MoiAi</a></li>
                                    <li><a href="https://lookingforsponsor.com/app/opportunities/8327974312_KQlvZ9fyetduyl4Wb70v">Place of sponsor</a></li>
                                    <li><a href="?app=firstpage">Back To Moi</a></li>


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
    # equal to `start_server({'index': index, 'task_1': task_1, 'task_2': task_2})`


class MoiPic_New_Page:
    def rettur(self):
        To_Know_The_Celint = get_localstorage(key='moiiforutest')

        start()


