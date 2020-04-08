from beautifuldict.baseconfig import Baseconfig

from decouple import config

from pkg_resources import resource_filename


params = {
    'input': {
        'path': resource_filename(__name__, 'data/input/'),
        'file': {
            'mensual': 'Mensual.xlsx',
            'trimestral': 'Trimestral.xlsx'
        }
    },
    'output': {
        'path': resource_filename(__name__, 'data/output/')
    },
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
    }
}

etl_cfg = Baseconfig(params)
