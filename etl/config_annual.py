from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_anual.xlsx',
    'series': {
        'pib_precios_corrientes': {
            'sheet': 'PIB_corr',
            'label': 'PIB. Precios corrientes',
            'category': 'Economía',
            'value_vars': [
                'PIB. Precios corrientes Cantabria',
                'PIB. Precios corrientes España'],
            'rate_vars': [
                'PIB. Precios corrientes Cantabria. Var interanual',
                'PIB. Precios corrientes España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Contabilidad Regional de España Base 2020 del INE',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Miles de euros'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Miles de euros'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': ['2023 provisional y 2024 avance'],
            'json': {
                'value': 'pib-precios-corrientes.json-stat',
                'trend': 'pib-precios-corrientes-tendencia.json-stat'
            }
        },
        'pib_indice_volumen': {
            'sheet': 'PIB_in',
            'label': 'PIB. Índices de volumen',
            'category': 'Economía',
            'value_vars': [
                'PIB. Índice de volumen Cantabria',
                'PIB. Índice de volumen España'],
            'rate_vars': [
                'PIB. Índice de volumen Cantabria. Var interanual',
                'PIB. Índice de volumen España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Contabilidad Regional de España Base 2020 del INE',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 2, 'label': 'Índice'},
                    'Valor España': {
                        'decimals': 2, 'label': 'Índice'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': ['2023 provisional y 2024 avance'],
            'json': {
                'value': 'pib-indice-volumen.json-stat',
                'trend': 'pib-indice-volumen-tendencia.json-stat'
            }
        },
        'pib_per_capita': {
            'sheet': 'PIB_perc',
            'label': 'PIB per cápita',
            'category': 'Economía',
            'value_vars': [
                'PIB per cápita Cantabria','PIB per cápita España'],
            'rate_vars': [
                'PIB per cápita Cantabria. Var interanual',
                'PIB per cápita España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Contabilidad Regional de España Base 2020 del INE',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Euros'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Euros'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': ['2023 provisional y 2024 avance'],
            'json': {
                'value': 'pib-per-capita.json-stat',
                'trend': 'pib-per-capita-tendencia.json-stat'
            }
        },
        'gasto_publico_educacion': {
            'sheet': 'Gasto_educa',
            'label': 'Gasto público en educación',
            'category': 'Economía',
            'value_vars': [
                'Gasto público en educación Cantabria',
                'Gasto público en educación España'],
            'rate_vars': [
                'Gasto público en educación Cantabria. Var interanual',
                'Gasto público en educación España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Estadística de Gasto Público en Educación del Ministerio de Educación y Formación Profesional',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Miles de euros'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Miles de euros'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': [''],
            'json': {
                'value': 'gasto-publico-educacion.json-stat',
                'trend': 'gasto-publico-educacion-tendencia.json-stat'
            }
        },
        'gasto_publico_educacion_pib': {
            'sheet': 'Gasto_educa_pib',
            'label': 'Gasto público en educación sobre el PIB',
            'category': 'Economía',
            'value_vars': [
                'Gasto público en educación sobre el PIB. Cantabria',
                'Gasto público en educación sobre el PIB. España'],
            'rate_vars': [
                'Gasto público en educación sobre el PIB. Cantabria. Var interanual',
                'Gasto público en educación sobre el PIB.  España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Estadística de Gasto Público en Educación del Ministerio de Educación y Formación Profesional',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': '%'},
                    'Valor España': {
                        'decimals': 0, 'label': '%'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': [''],
            'json': {
                'value': 'gasto-publico-educacion-pib.json-stat',
                'trend': 'gasto-publico-educacion-pib-tendencia.json-stat'
            }
        },
        'gasto_id_sobre_pib': {
            'sheet': 'Gasto I+D_pib',
            'label': 'Gasto I+D sobre el PIB',
            'category': 'Economía',
            'value_vars': [
                'Gasto I+D sobre el PIB. Cantabria',
                'Gasto I+D sobre el PIB. España'],
            'rate_vars': [
                'Gasto I+D sobre el PIB. Cantabria. Var interanual',
                'Gasto I+D sobre el PIB. España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Estadística de I+D y Contabilidad Regional de España del INE',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': '%'},
                    'Valor España': {
                        'decimals': 0, 'label': '%'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': ['A partir del año 2021 los datos están basados en Empresa Estadística en lugar de Unidades Legales'],
            'json': {
                'value': 'gasto-id-sobre-pib.json-stat',
                'trend': 'gasto-id-sobre-pib-tendencia.json-stat'
            }
        },
        'personal_iD_ocupada': {
            'sheet': 'Per I+D sobre p ocupada',
            'label': 'Personal en I+D sobre la población ocupada',
            'category': 'Economía',
            'value_vars': [
                'Personal en I+D sobre población ocupada en tanto por mil Cantabria',
                'Personal en I+D sobre población ocupada en tanto por mil  España'],
            'rate_vars': [
                'Personal en I+D sobre población ocupada en tanto por mil Cantabria. Var interanual',
                'Personal en I+D sobre población ocupada en tanto por mil  España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Estadística de I+D y Encuesta de Población Activa del INE',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 1, 'label': 'Tanto por mil'},
                    'Valor España': {
                        'decimals': 1, 'label': 'Tanto por mil'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': ['A partir del año 2021 los datos están basados en Empresa Estadística en lugar de Unidades Legales'],
            'json': {
                'value': 'personal-id-poblacion.json-stat',
                'trend': 'personal-id-poblacion-tendencia.json-stat'
            }
        },
        'gasto_id': {
            'sheet': 'Gasto I+D',
            'label': 'Gasto I+D',
            'category': 'Economía',
            'value_vars': [
                'Gasto I+D.  Cantabria',
                'Gasto I+D.  España'],
            'rate_vars': [
                'Gasto I+D.  Cantabria. Var interanual',
                'Gasto I+D. España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Estadística de I+D del INE',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 1, 'label': 'Miles de euros'},
                    'Valor España': {
                        'decimals': 1, 'label': 'Miles de euros'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': ['A partir del año 2021 los datos están basados en Empresa Estadística en lugar de Unidades Legales'],
            'json': {
                'value': 'gasto-id.json-stat',
                'trend': 'gasto-id-tendencia.json-stat'
            }
        },
        'gasto_sanitario_consolidado': {
            'sheet': 'Gasto_sani',
            'label': 'Gasto sanitario público consolidado. Sector CC.AA',
            'category': 'Sanidad',
            'value_vars': [
                'Gasto sanitario público consolidado. Sector CC.AA Cantabria',
                'Gasto sanitario público consolidado. Sector CC.AA España'],
            'rate_vars': [
                'Gasto sanitario público consolidado. Sector CC.AA Cantabria. Var interanual',
                'Gasto sanitario público consolidado. Sector CC.AA España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Estadística de Gasto sanitario público del Ministerio de Sanidad',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Miles de euros'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Miles de euros'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': ['Los dos últimos años son provisionales'],
            'json': {
                'value': 'gasto-sanitario-consolidado.json-stat',
                'trend': 'gasto-sanitario-consolidado-tendencia.json-stat'
            }
        },
        'gasto_sanitario_consolidado_pib': {
            'sheet': 'Gasto_sanpib',
            'label': 'Gasto sanitario público consolidado sobre el PIB. Sector CC.AA',
            'category': 'Sanidad',
            'value_vars': [
                'Gasto sanitario público consolidado sobre PIB. Sector CC.AA Cantabria',
                'Gasto sanitario público consolidado sobre PIB. Sector CC.AA España'],
            'rate_vars': [
                'Gasto sanitario público consolidado sobre PIB. Sector CC.AA Cantabria. Var interanual',
                'Gasto sanitario público consolidado sobre PIB. Sector CC.AA España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Estadística de Gasto Sanitario Público del Ministerio de Sanidad',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Valor España': {
                        'decimals': 2, 'label': '%'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': ['Los dos últimos años son provisionales. Para una mejor interpretación es el dato del indicador y no su tasa de variación anual.'],
            'json': {
                'value': 'gasto-sanitario-consolidado-pib.json-stat',
                'trend': 'gasto-sanitario-consolidado-pib-tendencia.json-stat'
            }
        },
        'gasto_sanitario_consolidado_per_capita': {
            'sheet': 'Gasto_sanPC',
            'label': 'Gasto sanitario público consolidado per cápita. Sector CC.AA',
            'category': 'Sanidad',
            'value_vars': [
                'Gasto sanitario público consolidado per cápita. Sector CC.AA Cantabria',
                'Gasto sanitario público consolidado per cápita. Sector CC.AA España'],
            'rate_vars': [
                'Gasto sanitario público consolidado per cápita. Sector CC.AA Cantabria. Var interanual',
                'Gasto sanitario público consolidado per cápita. Sector CC.AA España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Estadística de Gasto sanitario público del Ministerio de Sanidad',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Euros'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Euros'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': ['Los dos últimos años son provisionales'],
            'json': {
                'value': 'gasto-sanitario-consolidado-per-capita.json-stat',
                'trend': 'gasto-sanitario-consolidado-per-capita-tendencia.json-stat'
            }
        },
    }
}

annual_cfg = Baseconfig(params)
annual_cfg.add(common_cfg)