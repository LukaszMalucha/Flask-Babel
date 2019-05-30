from flask import Flask, render_template, request
from babel import numbers, dates
from datetime import date, datetime, time
from flask_babel import Babel, format_date, gettext

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

@babel.localeselector
def get_local():
    return 'pl'
    # return request.accept_languages.best_match(['en', 'es', 'pl'])


@app.route('/')
def index():

    lukasz = gettext('Lukasz')


    us_num = numbers.format_decimal(12345, locale='en_US')
    se_num = numbers.format_decimal(12345, locale='sv_SE')
    pl_num = numbers.format_decimal(12345, locale='pl_PL')

    d = date(2018, 12, 10)

    us_date = dates.format_date(d, locale='en_US')
    local_date = format_date(d)
    pl_date = dates.format_date(d, locale='pl_PL')

    dt = datetime.now()
    us_dt = dates.format_datetime(dt, locale='en_US')
    se_dt = dates.format_datetime(dt, locale='sv_SE')
    pl_dt = dates.format_datetime(dt, locale='pl_PL')

    results = {'us_num': us_num, 'se_num': se_num, 'pl_num': pl_num, 'us_date': us_date, 'local_date': local_date,
               'pl_date': pl_date, 'us_dt': us_dt, 'se_dt': se_dt, 'pl_dt': pl_dt, 'lukasz' : lukasz}
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
