from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
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
                'value': {
                    'Paro Cantabria': {
                        'decimals': 0, 'label': 'Personas'},
                    'Paro España': {
                        'decimals': 0, 'label': 'Personas'},
                },
                'trend': {
                    'Paro Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Paro España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Paro Cantabria. Tendencia': {
                        'decimals': 2, 'label': '%'},
                    'Paro España. Tendencia': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
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
                'value': {
                    'Contratos Cantabria': {
                        'decimals': 0, 'label': 'Contratos'},
                    'Contratos España': {
                        'decimals': 0, 'label': 'Contratos'},
                },
                'trend': {
                    'Contratos Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Contratos España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Contratos Cantabria. Tendencia': {
                        'decimals': 2, 'label': '%'},
                    'Contratos España. Tendencia': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
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
                'value': {
                    'Afiliados a último día de mes Cantabria': {
                        'decimals': 0, 'label': 'Afiliados (a último día de mes)'},
                    'Afiliados a último día de mes España': {
                        'decimals': 0, 'label': 'Afiliados (a último día de mes)'},
                },
                'trend': {
                    'Afiliados a último día de mes Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Afiliados a último día de mes España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Afiliados a último día de mes Cantabria. Tendencia': {
                        'decimals': 2, 'label': '%'},
                    'Afiliados a último día de mes España. Tendencia': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
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
                'value': {
                    'Afiliados. Asalariados Cantabria': {
                        'decimals': 0, 'label': 'Afiliados (a último día de mes)'},
                    'Afiliados. Asalariados España': {
                        'decimals': 0, 'label': 'Afiliados (a último día de mes)'},
                },
                'trend': {
                    'Afiliados. Asalariados Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Afiliados. Asalariados España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Afiliados. Asalariados Cantabria. Tendencia': {
                        'decimals': 2, 'label': '%'},
                    'Afiliados. Asalariados España. Tendencia': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
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
                'value': {
                    'Afiliados. No asalariados Cantabria': {
                        'decimals': 0, 'label': 'Afiliados (a último día de mes)'},
                    'Afiliados. No asalariados España': {
                        'decimals': 0, 'label': 'Afiliados (a último día de mes)'},
                },
                'trend': {
                    'Afiliados. No asalariados Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Afiliados. No asalariados España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Afiliados. No asalariados Cantabria. Tendencia': {
                        'decimals': 2, 'label': '%'},
                    'Afiliados. No asalariados España. Tendencia': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
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
                'value': {
                    'Ipc Cantabria': {
                        'decimals': 2, 'label': 'Índice'},
                    'Ipc España': {
                        'decimals': 2, 'label': 'Índice'},
                },
                'trend': {
                    'Ipc Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Ipc España. Var interanual': {
                        'decimals': 2, 'label': '%'}
                }
            },
            "note":[""],
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
                'value': {
                    'Matriculación de vehículos Cantabria': {
                        'decimals': 0, 'label': 'Vehículos'},
                    'Matriculación de vehículos España': {
                        'decimals': 0, 'label': 'Vehículos'},
                },
                'trend': {
                    'Matriculación de vehículos Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Matriculación de vehículos España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Matriculación de vehículos Cantabria. Tendencia': {
                        'decimals': 2, 'label': '%'},
                    'Matriculación de vehículos España. Tendencia': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
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
                'value': {
                    'Indicador de clima industrial Cantabria': {
                        'decimals': 0, 'label': 'Saldo'},
                    'Indicador de clima industrial España': {
                        'decimals': 0, 'label': 'Saldo'},
                },
                'trend': {
                    'Indicador de clima industrial Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Indicador de clima industrial España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Indicador de clima industrial Cantabria. Tendencia': {
                        'decimals': 2, 'label': '%'},
                    'Indicador de clima industrial España. Tendencia': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":["Para una mejor interpretación la tasa de variación se da en términos absolutos al tratarse de un saldo de porcentaje"],
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
                'value': {
                    'Empresas inscritas en la Seguridad Social Cantabria': {
                        'decimals': 0, 'label': 'Empresas'},
                    'Empresas inscritas en la Seguridad Social España': {
                        'decimals': 0, 'label': 'Empresas'},
                },
                'trend': {
                    'Empresas inscritas en la Seguridad Social Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Empresas inscritas en la Seguridad Social España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Empresas inscritas en la Seguridad Social Cantabria. Tendencia': {
                        'decimals': 2, 'label': '%'},
                    'Empresas inscritas en la Seguridad Social España. Tendencia': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
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
                'value': {
                    'Personas físicas inscritas en la Seguridad Social Cantabria': {
                        'decimals': 0, 'label': 'Empresas'},
                    'Personas físicas inscritas en la Seguridad Social España': {
                        'decimals': 0, 'label': 'Empresas'},
                },
                'trend': {
                    'Personas físicas inscritas en la Seguridad Social Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Personas físicas inscritas en la Seguridad Social España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Personas físicas inscritas en la Seguridad Social Cantabria. Tendencia': {
                        'decimals': 2, 'label': '%'},
                    'Personas físicas inscritas en la Seguridad Social España. Tendencia': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
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
                'value': {
                    'Personas jurídicas inscritas en la Seguridad Social Cantabria': {
                        'decimals': 0, 'label': 'Empresas'},
                    'Personas jurídicas inscritas en la Seguridad Social España': {
                        'decimals': 0, 'label': 'Empresas'},
                },
                'trend': {
                    'Personas jurídicas inscritas en la Seguridad Social Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Personas jurídicas inscritas en la Seguridad Social España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Personas jurídicas inscritas en la Seguridad Social Cantabria. Tendencia': {
                        'decimals': 2, 'label': '%'},
                    'Personas jurídicas inscritas en la Seguridad Social España. Tendencia': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
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
                'value': {
                    'Tráfico aéreo de pasajeros Cantabria': {
                        'decimals': 0, 'label': 'Pasajeros'},
                    'Tráfico aéreo de pasajeros España': {
                        'decimals': 0, 'label': 'Pasajeros'},
                },
                'trend': {
                    'Tráfico aéreo de pasajeros Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Tráfico aéreo de pasajeros España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Tráfico aéreo de pasajeros Cantabria. Tendencia': {
                        'decimals': 2, 'label': '%'},
                    'Tráfico aéreo de pasajeros España. Tendencia': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
            'json': {
                'value': 'trafico-aereo.json-stat',
                'trend': 'trafico-aereo-tendencia.json-stat'
            }
        },
        'pernoctaciones_hoteleras': {
            'sheet': 'CTH',
            'label': 'Pernoctaciones hoteleras',
            'value_vars': [
                'Pernoctaciones hoteleras Cantabria',
                'Pernoctaciones hoteleras España'],
            'rate_vars': [
                'Pernoctaciones hoteleras Cantabria. Var interanual',
                'Pernoctaciones hoteleras España. Var interanual'],
            'trend_vars': [
                'Pernoctaciones hoteleras Cantabria. Tendencia',
                'Pernoctaciones hoteleras España. Tendencia'],
            'source': 'Fuente: ICANE a partir de Coyuntura Turística Hotelera del INE',
            'unit':{
                'value': {
                    'Pernoctaciones hoteleras Cantabria': {
                        'decimals': 0, 'label': 'Pernoctaciones'},
                    'Pernoctaciones hoteleras España': {
                        'decimals': 0, 'label': 'Pernoctaciones'},
                },
                'trend': {
                    'Pernoctaciones hoteleras Cantabria. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Pernoctaciones hoteleras España. Var interanual': {
                        'decimals': 2, 'label': '%'},
                    'Pernoctaciones hoteleras Cantabria. Tendencia': {
                        'decimals': 2, 'label': '%'},
                    'Pernoctaciones hoteleras España. Tendencia': {
                        'decimals': 2, 'label': '%'},
                }
            },
            "note":[""],
            'json': {
                'value': 'pernoctaciones-hoteleras.json-stat',
                'trend': 'pernoctaciones-hoteleras-tendencia.json-stat'
            }
        }
    },
    'globals': {
        'source': 'Fuente: ICANE a partir de Movimiento Laboral Registrado [SEPE], Afiliaciones a la Seguridad Social [TGSS], Índice de Precios al Consumo [INE], Matriculación de Vehiculos [DGT], Encuesta de Coyuntura Industrial [MICT], Empresas Inscritas en Seguridad Social [MTMSS], Estadística de tráfico aéreo [AENA]',
        'json': 'globales-mensual.json-stat',
        'csv': 'globales-mensual-tabla.csv'
    }
}

monthly_cfg = Baseconfig(params)
monthly_cfg.add(common_cfg)
