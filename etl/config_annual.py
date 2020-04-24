from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_anual.xlsx',
    'series': {
        'pib_precios_corrientes': {
            'sheet': 'Hoja2',
            'label': 'PIB. Precios corrientes',
            'value_vars': [
                'PIB. Precios corrientes Cantabria',
                'PIB. Precios corrientes España'],
            'rate_vars': [
                'PIB. Precios corrientes Cantabria. Var interanual',
                'PIB. Precios corrientes España. Var interanual'],
            'trend_vars': [],
            'source': 'Fuente: ICANE a partir de Contabilidad Regional de España Base 2015 del INE',
            'unit':{
                'value': {
                    'PIB. Precios corrientes Cantabria': {
                        'decimals': 0, 'label': 'Miles de euros'},
                    'PIB. Precios corrientes España': {
                        'decimals': 0, 'label': 'Miles de euros'},
                },
                'trend': {
                    'PIB. Precios corrientes Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'PIB. Precios corrientes España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":["Los datos de 2017 son provisionales, 2018 son avance"],
            'json': {
                'value': 'pib-precios-corrientes.json-stat',
                'trend': 'pib-precios-corrientes-tendencia.json-stat'
            }
        },
        'pib_indice_volumen': {
            'sheet': 'Hoja1',
            'label': 'PIB. Índices de volumen',
            'value_vars': [
                'PIB. Índice de volumen Cantabria',
                'PIB. Índice de volumen España'],
            'rate_vars': [
                'PIB. Índice de volumen Cantabria. Var interanual',
                'PIB. Índice de volumen España. Var interanual'],
            'trend_vars': [],
            'source': 'Fuente: ICANE a partir de Contabilidad Regional de España Base 2015 del INE',
            'unit':{
                'value': {
                    'PIB. Índice de volumen Cantabria': {
                        'decimals': 0, 'label': 'Miles de euros'},
                    'PIB. Índice de volumen España': {
                        'decimals': 0, 'label': 'Miles de euros'},
                },
                'trend': {
                    'PIB. Índice de volumen Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'PIB. Índice de volumen España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":["Los datos de 2017 son provisionales, 2018 son avance"],
            'json': {
                'value': 'pib-indice-volumen.json-stat',
                'trend': 'pib-indice-volumen-tendencia.json-stat'
            }
        },
        'pib_per_capita': {
            'sheet': 'Hoja3',
            'label': 'PIB per cápita',
            'value_vars': [
                'PIB per cápita Cantabria','PIB per cápita España'],
            'rate_vars': [
                'PIB per cápita Cantabria. Var interanual',
                'PIB per cápita España. Var interanual'],
            'trend_vars': [],
            'source': 'Fuente: ICANE a partir de Contabilidad Regional de España Base 2015 del INE',
            'unit':{
                'value': {
                    'PIB per cápita Cantabria': {
                        'decimals': 0, 'label': 'Miles de euros'},
                    'PIB per cápita España': {
                        'decimals': 0, 'label': 'Miles de euros'},
                },
                'trend': {
                    'PIB per cápita Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'PIB per cápita España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":["Los datos de 2017 son provisionales, 2018 son avance"],
            'json': {
                'value': 'pib-per-capita.json-stat',
                'trend': 'pib-per-capita-tendencia.json-stat'
            }
        },
        'gasto_sanitario_consolidado': {
            'sheet': 'Hoja4',
            'label': 'Gasto sanitario público consolidado. Sector CC.AA',
            'value_vars': [
                'Gasto sanitario público consolidado. Sector CC.AA Cantabria',
                'Gasto sanitario público consolidado. Sector CC.AA España'],
            'rate_vars': [
                'Gasto sanitario público consolidado. Sector CC.AA Cantabria. Var interanual',
                'Gasto sanitario público consolidado. Sector CC.AA España. Var interanual'],
            'trend_vars': [],
            'source': 'Fuente: ICANE a partir de Estadística de Gasto sanitario público del Ministerio de Sanidad',
            'unit':{
                'value': {
                    'Gasto sanitario público consolidado. Sector CC.AA Cantabria': {
                        'decimals': 0, 'label': 'Miles de euros'},
                    'Gasto sanitario público consolidado. Sector CC.AA España': {
                        'decimals': 0, 'label': 'Miles de euros'},
                },
                'trend': {
                    'Gasto sanitario público consolidado. Sector CC.AA Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Gasto sanitario público consolidado. Sector CC.AA España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
            'json': {
                'value': 'gasto-sanitario-consolidado.json-stat',
                'trend': 'gasto-sanitario-consolidado-tendencia.json-stat'
            }
        },
        'gasto_sanitario_consolidado_per_capita': {
            'sheet': 'Hoja5',
            'label': 'Gasto sanitario público consolidado per cápita. Sector CC.AA',
            'value_vars': [
                'Gasto sanitario público consolidado per cápita. Sector CC.AA Cantabria',
                'Gasto sanitario público consolidado per cápita. Sector CC.AA España'],
            'rate_vars': [
                'Gasto sanitario público consolidado per cápita. Sector CC.AA Cantabria. Var interanual',
                'Gasto sanitario público consolidado per cápita. Sector CC.AA España. Var interanual'],
            'trend_vars': [],
            'source': 'Fuente: ICANE a partir de Estadística de Gasto sanitario público del Ministerio de Sanidad',
            'unit':{
                'value': {
                    'Gasto sanitario público consolidado per cápita. Sector CC.AA Cantabria': {
                        'decimals': 0, 'label': 'Euros'},
                    'Gasto sanitario público consolidado per cápita. Sector CC.AA España': {
                        'decimals': 0, 'label': 'Euros'},
                },
                'trend': {
                    'Gasto sanitario público consolidado per cápita. Sector CC.AA Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Gasto sanitario público consolidado per cápita. Sector CC.AA España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
            'json': {
                'value': 'gasto-sanitario-consolidado-per-capita.json-stat',
                'trend': 'gasto-sanitario-consolidado-per-capita-tendencia.json-stat'
            }
        },
        'gasto_sanitario_consolidado_pib': {
            'sheet': 'Hoja6',
            'label': 'Gasto sanitario público consolidado sobre el PIB. Sector CC.AA',
            'value_vars': [
                'Gasto sanitario público consolidado sobre PIB. Sector CC.AA Cantabria',
                'Gasto sanitario público consolidado sobre PIB. Sector CC.AA España'],
            'rate_vars': [
                'Gasto sanitario público consolidado sobre PIB. Sector CC.AA Cantabria. Var interanual',
                'Gasto sanitario público consolidado sobre PIB. Sector CC.AA España. Var interanual'],
            'trend_vars': [],
            'source': 'Fuente: ICANE a partir de Estadística de Gasto sanitario público del Ministerio de Sanidad',
            'unit':{
                'value': {
                    'Gasto sanitario público consolidado sobre PIB. Sector CC.AA Cantabria': {
                        'decimals': 0, 'label': '%'},
                    'Gasto sanitario público consolidado sobre PIB. Sector CC.AA España': {
                        'decimals': 0, 'label': '%'},
                },
                'trend': {
                    'Gasto sanitario público consolidado sobre PIB. Sector CC.AA Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Gasto sanitario público consolidado sobre PIB. Sector CC.AA España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
            'json': {
                'value': 'gasto-sanitario-consolidado-pib.json-stat',
                'trend': 'gasto-sanitario-consolidado-pib-tendencia.json-stat'
            }
        },
        'ingresos_tributarios_netos': {
            'sheet': 'Hoja7',
            'label': 'Ingresos tributarios netos anuales',
            'value_vars': [
                'Ingresos tributarios netos Delegación Cantabria',
                'Ingresos tributarios netos España'],
            'rate_vars': [
                'Ingresos tributarios netos Delegación Cantabria. Var interanual',
                'Ingresos tributarios netos España. Var interanual'],
            'trend_vars': [],
            'source': 'Fuente: ICANE a partir de Informes de Recaudación Tributaria de la AEAT',
            'unit':{
                'value': {
                    'Ingresos tributarios netos Delegación Cantabria': {
                        'decimals': 0, 'label': 'Miles de euros'},
                    'Ingresos tributarios netos España': {
                        'decimals': 0, 'label': 'Miles de euros'},
                },
                'trend': {
                    'Ingresos tributarios netos Delegación Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Ingresos tributarios netos España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
            'json': {
                'value': 'ingresos-tributarios-netos.json-stat',
                'trend': 'ingresos-tributarios-netos-tendencia.json-stat'
            }
        }
    },
    'globals': {
        'source': 'Fuente: ICANE a partir de Contabilidad Regional de España Base 2015 (INE), Estadística de Gasto Sanitario Público (Ministerio de Sanidad)',
        'note': [""],
        'json': 'globales-anual.json-stat',
        'csv': 'globales-anual-tabla.csv'
    }
}

annual_cfg = Baseconfig(params)
annual_cfg.add(common_cfg)