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
                'value': 'Miles de euros',
                'trend': '%'
            },
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
                'value': 'Índice',
                'trend': '%'
            },
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
                'value': 'Euros',
                'trend': '%'
            },
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
                'value': 'Miles de euros',
                'trend': '%'
            },
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
                'value': 'Euros',
                'trend': '%'
            },
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
                'value': '%',
                'trend': '%'
            },
            'json': {
                'value': 'gasto-sanitario-consolidado-pib.json-stat',
                'trend': 'gasto-sanitario-consolidado-pib-tendencia.json-stat'
            }
        }
    },
    'globals': {
        'source': 'Fuente: ICANE a partir de Contabilidad Regional de España Base 2015 (INE), Estadística de Gasto Sanitario Público (Ministerio de Sanidad)',
        'json': 'globales-anual.json-stat',
        'csv': 'globales-anual-tabla.csv'
    }
}

annual_cfg = Baseconfig(params)
annual_cfg.add(common_cfg)