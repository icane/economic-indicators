from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_anual.xlsx',
    'series': {
        'pib_precios_corrientes': {
            'sheet': 'Hoja2',
            'label': 'PIB. Precios corrientes',
            'category': 'Economía',
            'value_vars': [
                'PIB. Precios corrientes Cantabria',
                'PIB. Precios corrientes España'],
            'rate_vars': [
                'PIB. Precios corrientes Cantabria. Var interanual',
                'PIB. Precios corrientes España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Contabilidad Regional de España Base 2015 del INE',
            'unit':{
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
            'note':['Para Cantabria, los datos de 2017 son provisionales, 2018 son avance y 2019 primera estimación. Para España los datos de 2018 son provisionales y 2019 son avance'],
            'json': {
                'value': 'pib-precios-corrientes.json-stat',
                'trend': 'pib-precios-corrientes-tendencia.json-stat'
            }
        },
        'pib_indice_volumen': {
            'sheet': 'Hoja1',
            'label': 'PIB. Índices de volumen',
            'category': 'Economía',
            'value_vars': [
                'PIB. Índice de volumen Cantabria',
                'PIB. Índice de volumen España'],
            'rate_vars': [
                'PIB. Índice de volumen Cantabria. Var interanual',
                'PIB. Índice de volumen España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Contabilidad Regional de España Base 2015 del INE',
            'unit':{
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
            'note':['Para Cantabria, los datos de 2017 son provisionales, 2018 son avance y 2019 primera estimación. Para España los datos de 2018 son provisionales y 2019 son avance'],
            'json': {
                'value': 'pib-indice-volumen.json-stat',
                'trend': 'pib-indice-volumen-tendencia.json-stat'
            }
        },
        'pib_per_capita': {
            'sheet': 'Hoja3',
            'label': 'PIB per cápita',
            'category': 'Economía',
            'value_vars': [
                'PIB per cápita Cantabria','PIB per cápita España'],
            'rate_vars': [
                'PIB per cápita Cantabria. Var interanual',
                'PIB per cápita España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Contabilidad Regional de España Base 2015 del INE',
            'unit':{
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
            'note':['Para Cantabria, los datos de 2017 son provisionales, 2018 son avance y 2019 primera estimación. Para España los datos de 2018 son provisionales y 2019 son avance'],
            'json': {
                'value': 'pib-per-capita.json-stat',
                'trend': 'pib-per-capita-tendencia.json-stat'
            }
        },
        'ingresos_tributarios_netos': {
            'sheet': 'Hoja7',
            'label': 'Ingresos tributarios netos',
            'category': 'Economía',
            'value_vars': [
                'Ingresos tributarios netos Delegación Cantabria',
                'Ingresos tributarios netos España'],
            'rate_vars': [
                'Ingresos tributarios netos Delegación Cantabria. Var interanual',
                'Ingresos tributarios netos España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Informes Anuales de Recaudación Tributaria de la AEAT',
            'unit':{
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
            'note':[''],
            'json': {
                'value': 'ingresos-tributarios-netos.json-stat',
                'trend': 'ingresos-tributarios-netos-tendencia.json-stat'
            }
        },
        'deuda_publica': {
            'sheet': 'Hoja8',
            'label': 'Deuda pública CC.AA',
            'category': 'Economía',
            'value_vars': [
                'Deuda pública CC.AA Cantabria',
                'Deuda pública CC.AA España'],
            'rate_vars': [
                'Deuda pública CC.AA Cantabria. Var interanual',
                'Deuda pública CC.AA España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Deuda según PDE del Banco de España',
            'unit':{
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
            'note':[''],
            'json': {
                'value': 'deuda-publica.json-stat',
                'trend': 'deuda-publica-tendencia.json-stat'
            }
        },
        'deficit_publico': {
            'sheet': 'Hoja10',
            'label': 'Deficit público CC.AA',
            'category': 'Economía',
            'value_vars': [
                'Déficit público CC.AA Cantabria',
                'Déficit público CC.AA España'],
            'rate_vars': [
                'Déficit público CC.AA Cantabria. Var interanual',
                'Déficit público CC.AA España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Presupuestos de la Comunidad Autónoma en términos de Contabilidad Nacional de la IGAE',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Millones de euros'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Millones de euros'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note':['Los datos de 2018 son provisionales y los de 2019 avance'],
            'json': {
                'value': 'deficit-publico.json-stat',
                'trend': 'deficit-publico-tendencia.json-stat'
            }
        },
        'deficit_publico_pib': {
            'sheet': 'Hoja11',
            'label': 'Deficit público CC.AA sobre el PIB',
            'category': 'Economía',
            'value_vars': [
                'Déficit público CC.AA sobre el PIB Cantabria',
                'Déficit público CC.AA sobre el PIB España'],
            'rate_vars': [
                'Déficit público CC.AA sobre el PIB Cantabria. Var interanual',
                'Déficit público CC.AA sobre el PIB España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Presupuestos de la Comunidad Autónoma en términos de Contabilidad Nacional de la IGAE',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 1, 'label': '%'},
                    'Valor España': {
                        'decimals': 1, 'label': '%'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note':['Los datos de 2017 son provisionales y los de 2018 y 2019 son un avance. Para una mejor interpretación es el dato del indicador y no su tasa de variación anual.'],
            'json': {
                'value': 'deficit-publico-pib.json-stat',
                'trend': 'deficit-publico-pib-tendencia.json-stat'
            }
        },
        'deuda_publica_pib': {
            'sheet': 'Hoja9',
            'label': 'Deuda pública CC.AA sobre el PIB',
            'category': 'Economía',
            'value_vars': [
                'Deuda pública CC.AA sobre el PIB Cantabria',
                'Deuda pública CC.AA sobre el PIB España'],
            'rate_vars': [
                'Deuda pública CC.AA sobre el PIB Cantabria. Var interanual',
                'Deuda pública CC.AA sobre el PIB España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Deuda según PDE del Banco de España',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 1, 'label': '%'},
                    'Valor España': {
                        'decimals': 1, 'label': '%'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note':['Los datos de 2017 son provisionales y los de 2018 y 2019 son un avance. Para una mejor interpretación es el dato del indicador y no su tasa de variación anual.'],
            'json': {
                'value': 'deuda-publica-pib.json-stat',
                'trend': 'deuda-publica-pib-tendencia.json-stat'
            }
        },
        'gasto_sanitario_consolidado': {
            'sheet': 'Hoja4',
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
            'unit':{
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
            'note':['Los datos de 2017 y 2018 son provisionales'],
            'json': {
                'value': 'gasto-sanitario-consolidado.json-stat',
                'trend': 'gasto-sanitario-consolidado-tendencia.json-stat'
            }
        },
        'gasto_sanitario_consolidado_pib': {
            'sheet': 'Hoja6',
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
            'unit':{
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
            'note':['Los datos de 2017 y 2018 son provisionales. Para una mejor interpretación es el dato del indicador y no su tasa de variación anual.'],
            'json': {
                'value': 'gasto-sanitario-consolidado-pib.json-stat',
                'trend': 'gasto-sanitario-consolidado-pib-tendencia.json-stat'
            }
        },
        'gasto_sanitario_consolidado_per_capita': {
            'sheet': 'Hoja5',
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
            'unit':{
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
            'note':['Los datos de 2017 y 2018 son provisionales'],
            'json': {
                'value': 'gasto-sanitario-consolidado-per-capita.json-stat',
                'trend': 'gasto-sanitario-consolidado-per-capita-tendencia.json-stat'
            }
        },
    },
    'globals': {
        'csv': 'vision-global-anuales.csv'
    }
}

annual_cfg = Baseconfig(params)
annual_cfg.add(common_cfg)