from beautifuldict.baseconfig import Baseconfig

from decouple import config

from pkg_resources import resource_filename


params = {
    'path': {
        'input': resource_filename(__name__, 'data/input/'),
        'output': resource_filename(__name__, 'data/output/')
    },
    'annual': {
        'file': 'Datos_carga_anual.xlsx',
        'series': {
            'pib_indice_volumen': {
                'sheet': 'Hoja1',
                'label': 'PIB. Índices de volumen',
                'value_vars': [
                    'PIB. Índice de volumen Cantabria',
                    'PIB. Índice de volumen España'],
                'rate_vars': [
                    'PIB. Índice de volumen Cantabria. Var interanual',
                    'PIB. Índice de volumen España. Var interanual'],
                'trend_vars': [
                    'PIB. Índice de volumen Cantabria. Tendencia',
                    'PIB. Índice de volumen España. Tendencia'],
                'source': 'Fuente: ICANE a partir de Contabilidad Regional de España Base 2015 del INE',
                'unit':{
                    'value': 'Índice',
                    'trend': '%'
                },
                'json': {
                    'value': 'pib-indice-volumen.json-stat',
                    'trend': 'pib-iv-tendencia.json-stat'
                }
            },
            'pib_precios_corrientes': {
                'sheet': 'Hoja2',
                'label': 'PIB. Precios corrientes',
                'value_vars': [
                    'PIB. Precios corrientes Cantabria',
                    'PIB. Precios corrientes España'],
                'rate_vars': [
                    'PIB. Precios corrientes Cantabria. Var interanual',
                    'PIB. Precios corrientes España. Var interanual'],
                'trend_vars': [
                    'PIB. Precios corrientes Cantabria. Tendencia',
                    'PIB. Precios corrientes España. Tendencia'],
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
            'pib_per_capita': {
                'sheet': 'Hoja3',
                'label': 'PIB per cápita',
                'value_vars': [
                    'PIB per cápita Cantabria','PIB per cápita España'],
                'rate_vars': [
                    'PIB per cápita Cantabria. Var interanual',
                    'PIB per cápita España. Var interanual'],
                'trend_vars': [
                    'PIB per cápita Cantabria. Tendencia',
                    'PIB per cápita España. Tendencia'],
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
                'trend_vars': [
                    'Gasto sanitario público consolidado. Sector CC.AA Cantabria. Tendencia',
                    'Gasto sanitario público consolidado. Sector CC.AA España. Tendencia'],
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
                'trend_vars': [
                    'Gasto sanitario público consolidado per cápita. Sector CC.AA Cantabria. Tendencia',
                    'Gasto sanitario público consolidado per cápita. Sector CC.AA España. Tendencia'],
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
        }
    },
    'monthly': {
        'file': 'Datos_carga_mensual.xlsx',
        'series': {
            'paro': {
                'sheet': 'Paro',
                'label': 'Paro registrado',
                'value_vars': ['Paro Cantabria', 'Paro España'],
                'rate_vars': [
                    'Paro Cantabria. Var interanual',
                    'Paro España. Var interanual'],
                'trend_vars': [
                    'Paro Cantabria. Tendencia',
                    'Paro España. Tendencia'],
                'source': 'Fuente: ICANE a partir de Movimiento Laboral Registrado del SEPE',
                'unit':{
                    'value': 'Personas',
                    'trend': '%'
                },
                'json': {
                    'value': 'paro.json-stat',
                    'trend': 'paro-tendencia.json-stat'
                }
            },
            'contratos': {
                'sheet': 'Contratos',
                'label': 'Contratos',
                'value_vars': [
                    'Contratos Cantabria', 'Contratos España'],
                'rate_vars': [
                    'Contratos Cantabria. Var interanual',
                    'Contratos España. Var interanual'],
                'trend_vars': [
                    'Contratos Cantabria. Tendencia',
                    'Contratos España. Tendencia'],
                'source': 'Fuente: ICANE a partir de Movimiento Laboral Registrado del SEPE',
                'unit':{
                    'value': 'Contratos',
                    'trend': '%'
                },
                'json': {
                    'value': 'contratos.json-stat',
                    'trend': 'contratos-tendencia.json-stat'
                }
            },
            'afiliados': {
                'sheet': 'Afiliados',
                'label': 'Afiliados',
                'value_vars': [
                    'Afiliados a último día de mes Cantabria',
                    'Afiliados a último día de mes España'],
                'rate_vars': [
                    'Afiliados a último día de mes Cantabria. Var interanual',
                    'Afiliados a último día de mes España. Var interanual'],
                'trend_vars': [
                    'Afiliados a último día de mes Cantabria. Tendencia',
                    'Afiliados a último día de mes España. Tendencia'],
                'source': 'Fuente: ICANE a partir de Afiliaciones a la Seguridad Social de la Tesorería General de la Seguridad Social',
                'unit':{
                    'value': 'Afiliados (a último día de mes)',
                    'trend': '%'
                },
                'json': {
                    'value': 'afiliados.json-stat',
                    'trend': 'afiliados-tendencia.json-stat'
                }
            },
            'asalariados': {
                'sheet': 'Afiliados_Asalariados',
                'label': 'Afiliados asalariados',
                'value_vars': [
                    'Afiliados. Asalariados Cantabria',
                    'Afiliados. Asalariados España'],
                'rate_vars': [
                    'Afiliados. Asalariados Cantabria. Var interanual',
                    'Afiliados. Asalariados España. Var interanual'],
                'trend_vars': [
                    'Afiliados. Asalariados Cantabria. Tendencia',
                    'Afiliados. Asalariados España. Tendencia'],
                'source': 'Fuente: ICANE a partir de Afiliaciones a la Seguridad Social de la Tesorería General de la Seguridad Social',
                'unit':{
                    'value': 'Afiliados (a último día de mes)',
                    'trend': '%'
                },
                'json': {
                    'value': 'afiliados-asalariados.json-stat',
                    'trend': 'afiliados-asalariados-tendencia.json-stat'
                }
            },
            'no_asalariados': {
                'sheet': 'Afiliados_No_asalariados',
                'label': 'Afiliados no asalariados',
                'value_vars': [
                    'Afiliados. No asalariados Cantabria',
                    'Afiliados. No asalariados España'],
                'rate_vars': [
                    'Afiliados. No asalariados Cantabria. Var interanual',
                    'Afiliados. No asalariados España. Var interanual'],
                'trend_vars': [
                    'Afiliados. No asalariados Cantabria. Tendencia',
                    'Afiliados. No asalariados España. Tendencia'],
                'source': 'Fuente: ICANE a partir de Afiliaciones a la Seguridad Social de la Tesorería General de la Seguridad Social',
                'unit':{
                    'value': 'Afiliados (a último día de mes)',
                    'trend': '%'
                },
                'json': {
                    'value': 'afiliados-no-asalariados.json-stat',
                    'trend': 'afiliados-no-asalariados-tendencia.json-stat'
                }
            },
            'ipc': {
                'sheet': 'Ipc',
                'label': 'IPC',
                'value_vars': ['Ipc Cantabria', 'Ipc España'],
                'rate_vars': [
                    'Ipc Cantabria. Var interanual',
                    'Ipc España. Var interanual'],
                'trend_vars': [],
                'source': 'Fuente: ICANE a partir de Índice de Precios al Consumo del INE',
                'unit':{
                    'value': 'Índice',
                    'trend': '%'
                },
                'json': {
                    'value': 'ipc.json-stat',
                    'trend': 'ipc-tendencia.json-stat'
                }
            },
            'matriculaciones': {
                'sheet': 'Matriculacion_turismos',
                'label': 'Matriculación de vehículos',
                'value_vars': [
                    'Matriculación de vehículos Cantabria',
                    'Matriculación de vehículos España'],
                'rate_vars': [
                    'Matriculación de vehículos Cantabria. Var interanual',
                    'Matriculación de vehículos España. Var interanual'],
                'trend_vars': [
                    'Matriculación de vehículos Cantabria. Tendencia',
                    'Matriculación de vehículos España. Tendencia'],
                'source': 'Fuente: ICANE a partir de Matriculación de Vehiculos de la Dirección General de Tráfico',
                'unit':{
                    'value': 'Vehículos',
                    'trend': '%'
                },
                'json': {
                    'value': 'matriculaciones.json-stat',
                    'trend': 'matriculaciones-tendencia.json-stat'
                }
            },
            'clima': {
                'sheet': 'ECI',
                'label': 'Indicador de clima industrial',
                'value_vars': [
                    'Indicador de clima industrial Cantabria',
                    'Indicador de clima industrial España'],
                'rate_vars': [
                    'Indicador de clima industrial Cantabria. Var interanual',
                    'Indicador de clima industrial España. Var interanual'],
                'trend_vars': [
                    'Indicador de clima industrial Cantabria. Tendencia',
                    'Indicador de clima industrial España. Tendencia'],
                'source': 'Fuente: ICANE a partir de Encuesta de Coyuntura Industrial del Ministerio de Industria, Comercio y Turismo',
                'unit':{
                    'value': 'Saldo',
                    'trend': '%'
                },
                'json': {
                    'value': 'clima-industrial.json-stat',
                    'trend': 'clima-industrial-tendencia.json-stat'
                }
            },
            'empresas': {
                'sheet': 'Emp',
                'label': 'Empresas inscritas en la Seguridad social',
                'value_vars': [
                    'Empresas inscritas en la Seguridad Social Cantabria',
                    'Empresas inscritas en la Seguridad Social España'],
                'rate_vars': [
                    'Empresas inscritas en la Seguridad Social Cantabria. Var interanual',
                    'Empresas inscritas en la Seguridad Social España. Var interanual'],
                'trend_vars': [
                    'Empresas inscritas en la Seguridad Social Cantabria. Tendencia',
                    'Empresas inscritas en la Seguridad Social España. Tendencia'],
                'source': 'Fuente: ICANE a partir de Estadística de Empresas Inscritas en Seguridad Social del Ministerio de Trabajo, Migraciones y Seguridad Social',
                'unit':{
                    'value': 'Empresas',
                    'trend': '%'
                },
                'json': {
                    'value': 'empresas.json-stat',
                    'trend': 'empresas-tendencia.json-stat'
                }
            },
            'personas_fisicas': {
                'sheet': 'Emp_fi',
                'label': 'Personas físicas inscritas en la Seguridad social',
                'value_vars': [
                    'Personas físicas inscritas en la Seguridad Social Cantabria',
                    'Personas físicas inscritas en la Seguridad Social España'],
                'rate_vars': [
                    'Personas físicas inscritas en la Seguridad Social Cantabria. Var interanual',
                    'Personas físicas inscritas en la Seguridad Social España. Var interanual'],
                'trend_vars': [
                    'Personas físicas inscritas en la Seguridad Social Cantabria. Tendencia',
                    'Personas físicas inscritas en la Seguridad Social España. Tendencia'],
                'source': 'Fuente: ICANE a partir de Estadística de Empresas Inscritas en Seguridad Social del Ministerio de Trabajo, Migraciones y Seguridad Social',
                'unit':{
                    'value': 'Empresas',
                    'trend': '%'
                },
                'json': {
                    'value': 'personas-fisicas.json-stat',
                    'trend': 'personas-fisicas-tendencia.json-stat'
                }
            },
            'personas_juridicas': {
                'sheet': 'Emp_ju',
                'label': 'Personas jurídicas inscritas en la Seguridad social',
                'value_vars': [
                    'Personas jurídicas inscritas en la Seguridad Social Cantabria',
                    'Personas jurídicas inscritas en la Seguridad Social España'],
                'rate_vars': [
                    'Personas jurídicas inscritas en la Seguridad Social Cantabria. Var interanual',
                    'Personas jurídicas inscritas en la Seguridad Social España. Var interanual'],
                'trend_vars': [
                    'Personas jurídicas inscritas en la Seguridad Social Cantabria. Tendencia',
                    'Personas jurídicas inscritas en la Seguridad Social España. Tendencia'],
                'source': 'Fuente: ICANE a partir de Estadística de Empresas Inscritas en Seguridad Social del Ministerio de Trabajo, Migraciones y Seguridad Social',
                'unit':{
                    'value': 'Empresas',
                    'trend': '%'
                },
                'json': {
                    'value': 'personas-juridicas.json-stat',
                    'trend': 'personas-juridicas-tendencia.json-stat'
                }
            },
            'trafico_aereo': {
                'sheet': 'Taereo',
                'label': 'Tráfico aéreo de pasajeros',
                'value_vars': [
                    'Tráfico aéreo de pasajeros Cantabria',
                    'Tráfico aéreo de pasajeros España'],
                'rate_vars': [
                    'Tráfico aéreo de pasajeros Cantabria. Var interanual',
                    'Tráfico aéreo de pasajeros España. Var interanual'],
                'trend_vars': [
                    'Tráfico aéreo de pasajeros Cantabria. Tendencia',
                    'Tráfico aéreo de pasajeros España. Tendencia'],
                'source': 'Fuente: ICANE a partir de Estadística de tráfico aéreo de AENA',
                'unit':{
                    'value': 'Pasajeros',
                    'trend': '%'
                },
                'json': {
                    'value': 'trafico-aereo.json-stat',
                    'trend': 'trafico-aereo-tendencia.json-stat'
                }
            }
        }
    },
    'quarterly': {
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
                    'value': 'confianza.json-stat',
                    'trend': 'confianza-tendencia.json-stat'
                }
            }
        }
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
        'globals': 5,
        'monthly': 61,
        'quarterly': 15
    }
}

etl_cfg = Baseconfig(params)
