from string import Template
import time

#https://docs.python.org/3/library/string.html#format-string-syntax
t=Template(""" 
 
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css">
<style>
body {
  background-color: #FFFFFF;
}
@keyframes tool {
  0%   {transform: translateX($x_beginn) translateY(0);}
  10%  {transform: translateX($x_beginn) translateY($nachlauf);}
  20%  {transform: translateX($x_beginn) translateY(0);}
  25%  {transform: translateX($x_beginn) translateY(0);}
  30%  {transform: translateX($x_beginn) translateY(-$tail_length);}
  40%  {transform: translateX(-10.0px) translateY(-$tear_height);}
  50%  {transform: translateX(5.0px) translateY(-$tear_height);}
  80%  {transform: translateX(5.0px) translateY(-$tear_height);}
  90%  {transform: translateX(5.0px) translateY(-100px);}
  95%  {transform: translateX(-100px) translateY(-100px);}
  100% {transform: translateX(-100px) translateY(0);}
}
@keyframes wirebond {
  0%   {transform: translateX($x_beginn) translateY(0);}
  20%  {transform: translateX($x_beginn) translateY(0);}
  90%  {transform: translateX($x_beginn) translateY(0);}
  91%  {transform: translateX($x_beginn) translateY(-100px);}
  95%  {transform: translateX($x_beginn) translateY(-100px);}
  100% {transform: translateX($x_beginn) translateY(0);
  }
}
@keyframes cutter {
  0%   {transform: translateX($x_beginn) translateY(0);}
  10%  {transform: translateX($x_beginn) translateY($nachlauf);}
  20%  {transform: translateX($x_beginn) translateY(0);}
  22%  {transform: translateX(-120px) translateY(180px);}
  25%  {transform: translateX($x_beginn) translateY(0);}
  30%  {transform: translateX($x_beginn) translateY(-$tail_length);}
  40%  {transform: translateX(-10.0px) translateY(-$tear_height);}
  50%  {transform: translateX(5.0px) translateY(-$tear_height);}
  80%  {transform: translateX(5.0px) translateY(-$tear_height);}
  90%  {transform: translateX(5.0px) translateY(-100px);}
  95%  {transform: translateX($x_beginn) translateY(-100px);}
  100% {transform: translateX($x_beginn) translateY(0);}
}
@keyframes feed {
  0%   {transform: translateX(250px) translateY(400px) rotate(-90deg) scaleX(0);}
  25%  {transform: translateX(250px) translateY(400px) rotate(-90deg) scaleX(0);}
  30%  {transform: translateX(250px) translateY(400px) rotate(-90deg) scaleX(0.6);}
  40%  {transform: translateX(250px) translateY(400px) rotate(0deg)   scaleX(0.3);}
  50%  {transform: translateX(265px) translateY(400px) rotate(0deg)   scaleX(0.3);}
  80%  {transform: translateX(265px) translateY(400px) rotate(0deg)   scaleX(0.3);}
  90%  {transform: translateX(265px) translateY(300px) rotate(0deg)   scaleX(0.3);}
  95%  {transform: translateX(200px) translateY(300px) rotate(0deg)   scaleX(0.3);}
  100% {transform: translateX(250px) translateY(400px) rotate(-90deg) scaleX(0);}
}
#tool,#toolinside,#wireguide,#wire {
  animation-name: tool;
  animation-duration: $duration;
  animation-iteration-count: infinite;
  animation-timing-function: linear;
}
#cutter {
  animation-name: cutter;
  animation-duration: $duration;
  animation-iteration-count: infinite;
  animation-timing-function: linear;
}
#feed {
  animation-name: feed;
  animation-duration: $duration;
  animation-iteration-count: infinite;
  animation-timing-function: linear;
}
#wirebond {
  animation-name: wirebond;
  animation-duration: $duration;
  animation-iteration-count: infinite;
  animation-timing-function: linear;
}
img{
width:100%;
padding:20px;
}
</style>

</head>
<body>
<main class="container">
<h1>Abstände DD-Bonden EL3</h1>
<h2>Draht abschneiden + abreißen</h2>

<svg height="600" width="1200">
    <g id="wire"><path transform="translate(-250,0) scale(0.8) translate(188 -25)" d="M458.79173265758635 509.2700348432055 L452.71000950269246 505.2155527399429 L443.58742477035156 501.1610706366803 L444.60104529616723 509.2700348432055 L444.60104529616723 514.3381374722837 L461.83259423503324 526.5015837820715 L483.1186252771618 
530.5560658853341 L504.4046563192904 527.5152043078872 L521.6362052581565 524.4743427304402 L540.8949952486537 517.3789990497307 L552.0448210326258 506.22917326575856 
L567.2491289198606 492.0384859043395 L578.3989547038327 476.83417801710476 L589.5487804878048 457.57538802660747 L597.65774469433 445.4119417168197 L681.7882483370286 
289.3143807412099 L722.3330693696546 227.4835286664554 L750.7144440924926 188.96594868546072 L789.2320240734873 141.32578397212535 L797.3409882800124 128.1487171365219 
L770.9868546088057 128.1487171365219 L670.6384225530564 272.0828318023439 L643.2706683560341 316.68213493823237 L621.9846373139055 357.2269559708583 L607.7939499524864 
374.4585049097243 L580.4261957554638 432.23487488121623 L567.2491289198606 457.57538802660747 L552.0448210326258 473.7933164396578 L542.922236300285 487.9840038010769 
L530.7587899904972 490.01124485270816 L511.49999999999994 502.17469116249595 L488.18672790624004 508.25641431738984 L471.9687994931897 507.2427937915742 L461.83259423503324 
505.2155527399429 Z"></g>
    <g id="tool"><path transform="translate(168,89) scale(1)" d="M100 300 L171.9 300 L 198.14 0 L 73.76 0 Z" fill="cyan"></g>
    <g id="toolinside"><path transform="translate(168,89) scale(1)" d="M95 246.4 C 95 263.65 117.25 280.9 134.5 280.9 L154.6 280.9 C 163.25 280.9 171.9 272.25 171.9 263.6 L198.14 0 L 73.76 0 Z" fill="blue"></g>
    <g id="cutter"><path transform="translate(-250,0) scale(0.8)  translate(188 -25)" d="M593.6032625910673 129.16233766233756 L572.3172315489387 302.49144757681336 L636.1753246753246 130.17595818815323 Z" fill="red"></g>
    <g id="wireguide"><path transform="translate(-250,0) scale(0.8) translate(188 -20)" d="M674.6929046563191 128.1487171365219 L587.5215394361735 412.97608489071894 L587.5215394361735 428.18039277795367 L587.5215394361735 437.3029775102945 L590.5624010136205 444.398321191004 L601.7122267975926 449.46642382008224 L618.9437757364585 
451.4936648717136 L633.1344630978776 453.52090592334486 L650.3660120367435 451.4936648717136 L662.5294583465313 434.26211593284756 L724.3603104212859 337.96816598036105 L828.7632245802974 174.7752613240417 L827.749604054482 132.20319923978445 Z" fill="gray"></g>
    <g id="gehaeuse"><path transform="translate(200,0) "d="M0 400 L 250 400 L 250 300 L340 300 L 340 600 L0 600Z" fill="green" fill-opacity="0.8"></g>
    <g id="pad"><path transform="translate(-200,0)" d="M400 400 L590 400 L590 450 L400 450 Z" fill="red"></g>
    <g id="lbl"><text transform="translate(-200,0) translate(-150 50) scale(0.8) translate(153,-23)" x="600" y="620" fill="white">1 mm</text></g>
    <g id="scale"><path transform="translate(-200,0)" d="M400 530 L500 530 L500 540 L400 540 Z" fill="gray"></g>
    <g id="feed"><path transform="translate(0,0)" d="M0 0 L300 0 L300 -25 L0 -25 Z" fill="black"></g>
    <g id="wirebond"><path transform="translate(260,400)" d="M0 0 L90 0 L90 -25 L0 -25 Z" fill="black"></g>
    
</svg>
<p>
Taillänge: $desc_tail µm <br>
Abreißweg: $desc_tear µm <br>
Abreißhöhe: $desc_tear_height µm <br>
Nachlauf: $desc_nachlauf µm <br>
</p>
</main> <footer> Michal Svoboda, $today</footer> </body> </html>

""")

x0=-100
tail=900
tear=150
xoff=-250
yoff=0
tear_height=250
nachl=250
today=time.ctime(time.time())


d=dict(product="__",
       date="22.07.2019",
       author="Michal Svoboda",
       duration="5s",
       nachlauf=str(nachl/10-15)+"px",
       tail_length=str(tail/10)+"px",
       tear_height=str(tear_height/10)+"px",
       x_beginn=str(x0)+"px",
       x_2=str(x0+tail/10)+"px",
       x_tear=str(x0+tail/10+tear/10)+"px",
       y_high=str(-100)+"px",
       gehaeuse="M0 400 L 250 400 L 250 300 L340 300 L 340 600 L0 600Z",
       xoffset=str(xoff),
       yoffset=str(yoff),
       desc_tail=str(tail),
       desc_tear=str(tear),
       desc_tear_height=str(tear_height),
       desc_nachlauf=str(nachl),
       today=today)

with(open("anim.html","w")) as fw:
    fw.write(t.substitute(d))



