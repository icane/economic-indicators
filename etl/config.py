from beautifuldict.baseconfig import Baseconfig

from decouple import config

from pkg_resources import resource_filename


params = {
    'input': {
        'path': resource_filename(__name__, 'data/input/'),
        'mensual': {
            'file': 'Datos_carga_mensual.xlsx',
            'series': {
                'paro': 'Paro',
                'contratos': 'Contratos',
                'afiliados': 'Afiliados',
                'asalariados': 'Afiliados_Asalariados',
                'no-asalariados': 'Afiliados_No_asalariados',
                'ipc': 'Ipc',
                'matriculaciones': 'Matriculacion_turismos'
            },
            'sources': {
                'paro': 'ICANE a partir de Movimiento Laboral Registrado del SEPE',
                'contratos': 'ICANE a partir de Movimiento Laboral Registrado del SEPE',
                'afiliados': 'ICANE a partir de microdatos de la TGSS',
                'asalariados': 'ICANE a partir de microdatos de la TGSS',
                'no-asalariados': 'ICANE a partir de microdatos de la TGSS',
                'ipc': 'ICANE a partir del Índice de Precios al Consumo del INE',
                'matriculaciones': 'ICANE a partir de datos de la DGT'
            }
        },
        'trimestral': {
            'file': 'Datos_carga_trimestral.xlsx',
            'series': {
                'confianza': 'Indice confianza empresarial'
            },
            'sources': {
                'confianza': 'ICANE a partir del Índice de Confianza Empresarial del INE'
            }
        }
    },
    'output': {
        'path': resource_filename(__name__, 'data/output/'),
        'mensual': {
            'files': {
                'paro': 'paro.json-stat',
                'paro-tendencia': 'paro-tendencia.json-stat',
                'contratos': 'contratos.json-stat',
                'contratos-tendencia': 'contratos-tendencia.json-stat',
                'afiliados': 'afiliados.json-stat',
                'afiliados-tendencia': 'afiliados-tendencia.json-stat',
                'asalariados': 'afiliados-asalariados.json-stat',
                'asalariados-tendencia': 'afiliados-asalariados-tendencia.json-stat',
                'no_asalariados': 'afiliados-no-asalariados.json-stat',
                'no_asalariados-tendencia': 'afiliados-no-asalariados-tendencia.json-stat',
                'ipc': 'ipc.json-stat',
                'ipc-tendencia': 'ipc-tendencia.json-stat',
                'matriculaciones': 'matriculaciones.json-stat',
                'matriculaciones-tendencia': 'matriculaciones-tendencia.json-stat'
            }
        },
        'trimestral': {
            'files': {
                'confianza': 'confianza.json-stat',
                'confianza-tendencia': 'confianza-tendencia.json-stat'
            }
        }
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
    },
    'quarter': {
        '1': '1T',
        '2': '2T',
        '3': '3T',
        '4': '4T'
    },
    'periods': 61
}

etl_cfg = Baseconfig(params)
