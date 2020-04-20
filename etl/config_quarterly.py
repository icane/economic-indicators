from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_trimestral.xlsx',
    'series': {
        'confianza': {
            'sheet': 'Indice confianza empresarial',
            'label': 'Índice de confianza empresarial',
            'value_vars': ['ICE Cantabria', 'ICE España'],
            'rate_vars': ['ICE Cantabria. Var interanual', 'ICE España. Var interanual'],
            'trend_vars': ['ICE Cantabria. Tendencia', 'ICE España. Tendencia'],
            'source': 'Fuente: ICANE a partir de Índice de Confianza Empresarial del INE',
            'unit':{
                'value': 'Índice',
                'trend': '%'
            },
            'json': {
                'value': 'confianza-empresarial.json-stat',
                'trend': 'confianza-empresarial-tendencia.json-stat'
            }
        }
    }
}

quarterly_cfg = Baseconfig(params)
quarterly_cfg.add(common_cfg)