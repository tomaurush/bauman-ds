import pickle


FEATURES_NAMES = [
    'Соотношение матрица-наполнитель',
    'Плотность, кг/м3',
    'модуль упругости, ГПа',
    'Количество отвердителя, м.%',
    'Содержание эпоксидных групп,%_2',
    'Температура вспышки, С_2',
    'Поверхностная плотность, г/м2',
    # 'Модуль упругости при растяжении, ГПа',
    # 'Прочность при растяжении, МПа',
    'Потребление смолы, г/м2',
    'Угол нашивки, град',
    'Шаг нашивки',
    'Плотность нашивки',
]


def validate_form_data(params):
    """Валидация и подготовка данных, полученных из формы."""
    error_message = ''

    input_data = dict(zip(FEATURES_NAMES, params.values()))
    clean_data = input_data.copy()

    for name, value in input_data.items():
        try:
            clean_data[name] = float(value)
            if clean_data[name] < 0:
                error_message += f'{name} - не должно быть отрицательным числом\n'
        except Exception as ex:
            error_message += f'{name} - {ex}\n'

        if name == 'Угол нашивки, град' and clean_data[name] not in (0, 90):
            error_message += f'{name} - должно быть 0 или 90\n'

    return clean_data, error_message


def load_model_from_file(filename):
    """Загрузка модели из файла."""

    with open('./models/' + filename, 'rb') as f:
        model = pickle.load(f)

    return model
