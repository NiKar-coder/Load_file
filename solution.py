from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    arr = [
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!"]
    return '</br></br>'.join(arr)


@app.route('/image_mars')
def image_mars():
    return render_template('mars.html')


@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image.html')


@app.route('/choice/<variant>')
def choice(variant):
    return render_template('choice.html', variant=variant)


img = None


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    global img
    if request.method == 'GET':
        return render_template('load_photo.html', img=img)
    elif request.method == 'POST':
        f = request.files['file']
        img = 'static/img/' + f.filename
        f.save(img)
        return render_template('load_photo.html', img=img)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
