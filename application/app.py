from flask import Flask, render_template, request
import pandas as pd

from utils import validate_form_data, load_model_from_file

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/predictions/', methods=['GET', 'POST'])
def predictions_page():
    if request.method == 'GET':
        return render_template('predictions.html')

    if request.method == 'POST':
        params = request.form.to_dict()
        data, error_message = validate_form_data(params)
        if error_message:
            return render_template('predictions.html', error_message=error_message)

        x = pd.DataFrame(data, index=[0])

        model1 = load_model_from_file('best_model_1')
        y1 = model1.predict(x)
        result = {'Модуль упругости при растяжении, ГПа': y1[0]}

        model2 = load_model_from_file('best_model_2')
        y2 = model2.predict(x)
        result['Прочность при растяжении, МПа'] = y2[0]

        return render_template('predictions.html', params=data, inputs=x.to_html(), result=result)


if __name__ == '__main__':
    app.run()
