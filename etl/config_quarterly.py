from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_trimestral.xlsx',
    'series': {
        'confianza': {
            'sheet': 'Indice confianza empresarial',
            'label': 'Índice de confianza empresarial',
            'category': 'Empresas',
            'value_vars': ['ICE Cantabria', 'ICE España'],
            'rate_vars': ['ICE Cantabria. Var interanual', 'ICE España. Var interanual'],
            'trend_vars': ['ICE Cantabria. Tendencia', 'ICE España. Tendencia'],
            'source': 'Fuente: ICANE a partir de Índice de Confianza Empresarial del INE',
            'unit':{
                'value': {
                    'ICE Cantabria': {
                        'decimals': 2, 'label': 'Índice'},
                    'ICE España': {
                        'decimals': 2, 'label': 'Índice'},
                },
                'trend': {
                    'ICE Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'ICE España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'ICE Cantabria. Tendencia': {
                        'decimals': 2, 'label': '%'},
                    'ICE España. Tendencia': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
            'json': {
                'value': 'confianza-empresarial.json-stat',
                'trend': 'confianza-empresarial-tendencia.json-stat'
            }
        }
    },
    'globals': {
        'source': 'Fuente: ICANE a partir de Índice de Confianza Empresarial del INE',
        'note': [""],
        'json': 'globales-trimestral.json-stat',
        'csv': 'globales-trimestral-tabla.csv'
    }
}

quarterly_cfg = Baseconfig(params)
quarterly_cfg.add(common_cfg)