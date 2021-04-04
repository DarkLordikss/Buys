from flask import abort, Flask, render_template, request, redirect, url_for
app = Flask(__name__)


DB = {
    "Vasya": ["Молоко", "Хлеб"],
    "Masha": ["Сметана", "Картофель", "Яйца"],
}


@app.route('/', methods=['GET', 'POST'])
def handle_index():
    if request.method == "GET":
        return render_template('index.html')

    if request.method == "POST":
        # если метод POST, меняем args на form !!!
        name = request.form.get('name')
        products = DB.get(name)

        if not name:
            return render_template('index.html', error="Пустой пользователь!")

        if not products:
            return render_template('index.html', error="Продукты не найдены!")

        return render_template('index.html', name=name, products=products)


@app.route('/new', methods=['GET', 'POST'])
def handle_new():
    if request.method == "GET":
        return render_template('new.html')

    if request.method == "POST":
        name = request.form.get('name')
        products = request.form.get('products')

        if not name:
            return render_template('new.html', error="Введите имя!")

        if DB.get(name):
            return render_template('new.html', error="Пользователь уже существует!")

        if not products:
            return render_template('new.html', error="Введите продукты!")

        # сделали список, а-ля ['Хлеб', 'Молоко', ...]
        products = products.split('\n')
        DB[name] = products

        return redirect(url_for('handle_index'))


app.run('0.0.0.0', debug=True)
