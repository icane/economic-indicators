from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_trimestral.xlsx',
    'series': {
        'epa_ocupados': {
            'sheet': 'EPA',
            'label': 'Ocupados EPA',
            'category': 'Mercado de Trabajo',
            'value_vars': [
                'Ocupados EPA Cantabria', 'Ocupados EPA España'],
            'rate_vars': [
                'Ocupados EPA Cantabria. Var interanual',
                'Ocupados EPA España. Var interanual'],
            'trend_vars': [
                'Ocupados EPA Cantabria. Tendencia',
                'Ocupados EPA España. Tendencia'],
            'source': 'ICANE a partir de Encuesta de Población Activa del INE',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 1, 'label': 'Miles de personas'},
                    'Valor España': {
                        'decimals': 1, 'label': 'Miles de personas'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
            'json': {
                'value': 'epa-ocupados.json-stat',
                'trend': 'epa-ocupados-tendencia.json-stat'
            }
        },
        'epa_parados': {
            'sheet': 'EPA_2',
            'label': 'Parados EPA',
            'category': 'Mercado de Trabajo',
            'value_vars': [
                'Parados EPA Cantabria', 'Parados EPA España'],
            'rate_vars': [
                'Parados EPA Cantabria. Var interanual',
                'Parados EPA España. Var interanual'],
            'trend_vars': [
                'Parados EPA Cantabria. Tendencia',
                'Parados EPA España. Tendencia'],
            'source': 'ICANE a partir de Encuesta de Población Activa del INE',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 1, 'label': 'Miles de personas'},
                    'Valor España': {
                        'decimals': 1, 'label': 'Miles de personas'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
            'json': {
                'value': 'epa-parados.json-stat',
                'trend': 'epa-parados-tendencia.json-stat'
            }
        },
        'epa_tasa_actividad': {
            'sheet': 'EPA_4',
            'label': 'Tasa de actividad EPA',
            'category': 'Mercado de Trabajo',
            'value_vars': [
                'Tasa de actividad EPA Cantabria', 'Tasa de actividad EPA España'],
            'rate_vars': [
                'Tasa de actividad EPA Cantabria. Var interanual',
                'Tasa de actividad EPA España. Var interanual'],
            'trend_vars': [
                'Tasa de actividad EPA Cantabria. Tendencia',
                'Tasa de actividad EPA España. Tendencia'],
            'source': 'ICANE a partir de Encuesta de Población Activa del INE',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 2, 'label': 'Tasas'},
                    'Valor España': {
                        'decimals': 2, 'label': 'Tasas'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":["Para una mejor interpretación la tasa de variación se da en términos absolutos al tratarse de una tasa"],
            'json': {
                'value': 'epa-tasa-actividad.json-stat',
                'trend': 'epa-tasa-actividad-tendencia.json-stat'
            }
        },
        'epa_tasa_empleo': {
            'sheet': 'EPA_5',
            'label': 'Tasa de empleo EPA',
            'category': 'Mercado de Trabajo',
            'value_vars': [
                'Tasa de empleo EPA Cantabria', 'Tasa de empleo EPA España'],
            'rate_vars': [
                'Tasa de empleo EPA Cantabria. Var interanual',
                'Tasa de empleo EPA España. Var interanual'],
            'trend_vars': [
                'Tasa de empleo EPA Cantabria. Tendencia',
                'Tasa de empleo EPA España. Tendencia'],
            'source': 'ICANE a partir de Encuesta de Población Activa del INE',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 2, 'label': 'Tasas'},
                    'Valor España': {
                        'decimals': 2, 'label': 'Tasas'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":["Para una mejor interpretación la tasa de variación se da en términos absolutos al tratarse de una tasa"],
            'json': {
                'value': 'epa-tasa-empleo.json-stat',
                'trend': 'epa-tasa-empleo-tendencia.json-stat'
            }
        },
        'epa_tasa_paro': {
            'sheet': 'EPA_3',
            'label': 'Tasa de paro EPA',
            'category': 'Mercado de Trabajo',
            'value_vars': [
                'Tasa de paro EPA Cantabria', 'Tasa de paro EPA España'],
            'rate_vars': [
                'Tasa de paro EPA Cantabria. Var interanual',
                'Tasa de paro EPA España. Var interanual'],
            'trend_vars': [
                'Tasa de paro EPA Cantabria. Tendencia',
                'Tasa de paro EPA España. Tendencia'],
            'source': 'ICANE a partir de Encuesta de Población Activa del INE',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 2, 'label': 'Tasas'},
                    'Valor España': {
                        'decimals': 2, 'label': 'Tasas'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":["Para una mejor interpretación la tasa de variación se da en términos absolutos al tratarse de una tasa"],
            'json': {
                'value': 'epa-tasa-paro.json-stat',
                'trend': 'epa-tasa-paro-tendencia.json-stat'
            }
        },
        'confianza': {
            'sheet': 'Indice confianza empresarial',
            'label': 'Índice de confianza empresarial',
            'category': 'Empresas',
            'value_vars': ['ICE Cantabria', 'ICE España'],
            'rate_vars': ['ICE Cantabria. Var interanual', 'ICE España. Var interanual'],
            'trend_vars': ['ICE Cantabria. Tendencia', 'ICE España. Tendencia'],
            'source': 'ICANE a partir de Índice de Confianza Empresarial del INE',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 1, 'label': 'Índice'},
                    'Valor España': {
                        'decimals': 1, 'label': 'Índice'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
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
        'csv': 'vision-global-trimestrales.csv'
    }
}

quarterly_cfg = Baseconfig(params)
quarterly_cfg.add(common_cfg)