from beautifuldict.baseconfig import Baseconfig

from decouple import config

from pkg_resources import resource_filename

params = {
    'path': {
        'input': resource_filename(__name__, 'data/input/'),
        'output': resource_filename(__name__, 'data/output/')
    },
    'value_labels': {
        'month': {
            '1': 'Enero',
            '2': 'Febrero',
            '3': 'Marzo',
            '4': 'Abril',
            '5': 'Mayo',
            '6': 'Junio',
            '7': 'Julio',
            '8': 'Agosto',
            '9': 'Septiembre',
            '10': 'Octubre',
            '11': 'Noviembre',
            '12': 'Diciembre'
        },
        'quarter': {
            '1': '1T',
            '2': '2T',
            '3': '3T',
            '4': '4T'
        }
    },
    'periods': {
        'global_annual': 6,
        'annual': 10,
        'global_monthly': 5,
        'monthly': 61,
        'global_quarterly': 5,
        'quarterly': 15
    }
}

common_cfg = Baseconfig(params)
