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
            'note':[''],
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
            'note':[''],
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
            'note':['Para una mejor interpretación la tasa de variación se da en términos absolutos al tratarse de una tasa'],
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
            'note':['Para una mejor interpretación la tasa de variación se da en términos absolutos al tratarse de una tasa'],
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
            'note':['Para una mejor interpretación la tasa de variación se da en términos absolutos al tratarse de una tasa'],
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
            'note':[''],
            'json': {
                'value': 'confianza-empresarial.json-stat',
                'trend': 'confianza-empresarial-tendencia.json-stat'
            }
        },
        'deudores_concursados': {
            'sheet': 'EPC_D',
            'label': 'Deudores concursados',
            'category': 'Empresas',
            'value_vars': [
                'Deudores concursados Cantabria',
                'Deudores concursados España'],
            'rate_vars': [
                'Deudores concursados Cantabria. Var interanual',
                'Deudores concursados España. Var interanual'],
            'trend_vars': [
                'Deudores concursados Cantabria. Tendencia',
                'Deudores concursados España. Tendencia'],
            'source': 'ICANE  a partir de Encuesta de Procedimiento Concursal del INE',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 1, 'label': 'Deudores (empresa y personas)'},
                    'Valor España': {
                        'decimals': 1, 'label': 'Deudores (empresa y personas)'},
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
            'note':['Los datos del T1 del año 2019 y posteriores son provisionales.'],
            'json': {
                'value': 'deudores-concursados.json-stat',
                'trend': 'deudores-concursados-tendencia.json-stat'
            }
        },
        'empresas_concursadas': {
            'sheet': 'EPC_E',
            'label': 'Empresas concursadas',
            'category': 'Empresas',
            'value_vars': [
                'Empresas concursadas Cantabria',
                'Empresas concursadas España'],
            'rate_vars': [
                'Empresas concursadas Cantabria. Var interanual',
                'Empresas concursadas España. Var interanual'],
            'trend_vars': [
                'Empresas concursadas Cantabria. Tendencia',
                'Empresas concursadas España. Tendencia'],
            'source': 'ICANE  a partir de Encuesta de Procedimiento Concursal del INE',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 1, 'label': 'Empresas'},
                    'Valor España': {
                        'decimals': 1, 'label': 'Empresas'},
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
            'note':['Los datos del T1 del año 2019 y posteriores son provisionales.'],
            'json': {
                'value': 'empresas-concursadas.json-stat',
                'trend': 'empresas-concursadas-tendencia.json-stat'
            }
        },
        'turistas_internacionales': {
            'sheet': 'FRONTUR',
            'label': 'Turistas internacionales',
            'category': 'Servicios',
            'value_vars': [
                'Turistas internacionalesCantabria',
                'Turistas internacionalesEspaña'],
            'rate_vars': [
                'Turistas internacionalesCantabria. Var interanual',
                'Turistas internacionalesEspaña. Var interanual'],
            'trend_vars': [
                'Turistas internacionalesCantabria. Tendencia',
                'Turistas internacionalesEspaña. Tendencia'],
            'source': 'ICANE a partir de Movimientos Turísticos en Frontera del INE e Instituto de Estudios Turísticos',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 1, 'label': 'Personas'},
                    'Valor España': {
                        'decimals': 1, 'label': 'Personas'},
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
            'note':['Los datos de abril del año 2019 y posteriores son provisionales'],
            'json': {
                'value': 'turistas-internacionales.json-stat',
                'trend': 'turistas-internacionales-tendencia.json-stat'
            }
        },
        'gasto_turistas_internacionales': {
            'sheet': 'EGATUR',
            'label': 'Gasto de turistas internacionales',
            'category': 'Servicios',
            'value_vars': [
                'Gasto de turistas internacionalesCantabria',
                'Gasto de turistas internacionalesEspaña'],
            'rate_vars': [
                'Gasto de turistas internacionalesCantabria. Var interanual',
                'Gasto de turistas internacionalesEspaña. Var interanual'],
            'trend_vars': [
                'Gasto de turistas internacionalesCantabria. Tendencia',
                'Gasto de turistas internacionalesEspaña. Tendencia'],
            'source': 'ICANE a partir de Encuesta de Gasto Turistico del INE e Instituto de Estudios Turísticos',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 1, 'label': 'Millones de euros'},
                    'Valor España': {
                        'decimals': 1, 'label': 'Millones de euros'},
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
            'note':['Los datos de abril del año 2019 y posteriores son provisionales'],
            'json': {
                'value': 'gasto-turistas-internacionales.json-stat',
                'trend': 'gasto-turistas-internacionales-tendencia.json-stat'
            }
        }
    },
    'globals': {
        'csv': 'vision-global-trimestrales.csv'
    }
}

quarterly_cfg = Baseconfig(params)
quarterly_cfg.add(common_cfg)