from flask import Flask, render_template, request
import myconnutils

app = Flask(__name__)


def list_select():
    """Запрашиваем у бд зарегистрированных пользователей для формирования выпадающего меню в форме"""

    connection = myconnutils.getConnection()
    cursor = connection.cursor()
    sql_select = "SELECT user_id FROM users ORDER BY user_id"
    cursor.execute(sql_select)
    select = cursor.fetchall()
    connection.close()
    return select


@app.route('/', methods=['POST', 'GET'])
def search_username():
    username = ''
    category = ''
    if request.method == 'POST':
        connection = myconnutils.getConnection()
        try:
            cursor = connection.cursor()
            sql = "SELECT username, user_id FROM users WHERE user_id = %s "

            user_id = int(request.form['select'])
            cursor.execute(sql, user_id)
            data = cursor.fetchone()
            if data is not None:
                username = data['username']
                category = 'success'
            else:
                username = 'Пользователь с таким id не найден!'
                category = 'danger'

        except ValueError:
            username = 'Error: ошибка ввода или пустой запрос!'
            category = 'danger'
        finally:
            connection.close()
    return render_template('index.html', username=username, category=category, select=list_select())


if __name__ == '__main__':
    app.run()
