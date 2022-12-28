# связывает model.py и view.py

import model_mult as model
import view


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model.ad(value_a, value_b)
    result = model.do_it()
    view.view_data(result, 'result')

