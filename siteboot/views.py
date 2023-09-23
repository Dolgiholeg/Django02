from django.shortcuts import render

# Create your views here.
def index(req):
    return  render(req,'index.html')
def chockolate(req,id):
    id=int(id)
    name = ''
    img = ''
    text = ''
    if id==0:
        name = 'Snickers'
        img = 'img/0.jpg'
        text = 'Не тормози - сникерсни!'
    elif id==1:
        name = 'Mars'
        img = 'img/1.png'
        text = 'Марс - всё будет в шоколаде!'
    elif id == 2:
        name = 'Nats'
        img = 'img/2.png'
        text = 'Натс - заряжай мозги!'
    elif id == 3:
        name = 'РОССИЯ'
        img = 'img/3.png'
        text = 'РОССИЯ - Щедрая душа!'
    data = {'id': id, 'k1': name, 'k2': img, 'k3': text}
    return render(req, 'prochokolad.html', context=data)