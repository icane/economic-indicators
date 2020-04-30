from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_mensual.xlsx',
    'series': {
        'paro': {
            'sheet': 'Paro',
            'label': 'Paro registrado',
            'category': 'Mercado de Trabajo',
            'value_vars': ['Paro Cantabria', 'Paro España'],
            'rate_vars': [
                'Paro Cantabria. Var interanual',
                'Paro España. Var interanual'],
            'trend_vars': [
                'Paro Cantabria. Tendencia',
                'Paro España. Tendencia'],
            'source': 'ICANE a partir de Movimiento Laboral Registrado del SEPE',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Personas'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Personas'},
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
                'value': 'paro.json-stat',
                'trend': 'paro-tendencia.json-stat'
            }
        },
        'contratos': {
            'sheet': 'Contratos',
            'label': 'Contratos',
            'category': 'Mercado de Trabajo',
            'value_vars': [
                'Contratos Cantabria', 'Contratos España'],
            'rate_vars': [
                'Contratos Cantabria. Var interanual',
                'Contratos España. Var interanual'],
            'trend_vars': [
                'Contratos Cantabria. Tendencia',
                'Contratos España. Tendencia'],
            'source': 'ICANE a partir de Movimiento Laboral Registrado del SEPE',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Contratos'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Contratos'},
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
                'value': 'contratos.json-stat',
                'trend': 'contratos-tendencia.json-stat'
            }
        },
        'afiliados': {
            'sheet': 'Afiliados',
            'label': 'Afiliados',
            'category': 'Mercado de Trabajo',
            'value_vars': [
                'Afiliados Cantabria',
                'Afiliados España'],
            'rate_vars': [
                'Afiliados Cantabria. Var interanual',
                'Afiliados España. Var interanual'],
            'trend_vars': [
                'Afiliados Cantabria. Tendencia',
                'Afiliados España. Tendencia'],
            'source': 'ICANE a partir de Afiliaciones a la Seguridad Social de la Tesorería General de la Seguridad Social',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Afiliados (a último día de mes)'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Afiliados (a último día de mes)'},
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
            "note":["Datos a último día de mes"],
            'json': {
                'value': 'afiliados.json-stat',
                'trend': 'afiliados-tendencia.json-stat'
            }
        },
        'asalariados': {
            'sheet': 'Afiliados_Asalariados',
            'label': 'Afiliados asalariados',
            'category': 'Mercado de Trabajo',
            'value_vars': [
                'Afiliados asalariados Cantabria',
                'Afiliados asalariados España'],
            'rate_vars': [
                'Afiliados asalariados Cantabria. Var interanual',
                'Afiliados asalariados España. Var interanual'],
            'trend_vars': [
                'Afiliados asalariados Cantabria. Tendencia',
                'Afiliados asalariados España. Tendencia'],
            'source': 'ICANE a partir de Afiliaciones a la Seguridad Social de la Tesorería General de la Seguridad Social',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Afiliados (a último día de mes)'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Afiliados (a último día de mes)'},
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
            "note":["Datos a último día de mes"],
            'json': {
                'value': 'afiliados-asalariados.json-stat',
                'trend': 'afiliados-asalariados-tendencia.json-stat'
            }
        },
        'no_asalariados': {
            'sheet': 'Afiliados_No_asalariados',
            'label': 'Afiliados no asalariados',
            'category': 'Mercado de Trabajo',
            'value_vars': [
                'Afiliados no asalariados Cantabria',
                'Afiliados. No asalariados España'],
            'rate_vars': [
                'Afiliados no asalariados Cantabria. Var interanual',
                'Afiliados no asalariados España. Var interanual'],
            'trend_vars': [
                'Afiliados no asalariados Cantabria. Tendencia',
                'Afiliados no asalariados España. Tendencia'],
            'source': 'ICANE a partir de Afiliaciones a la Seguridad Social de la Tesorería General de la Seguridad Social',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Afiliados (a último día de mes)'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Afiliados (a último día de mes)'},
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
            "note":["Datos a último día de mes"],
            'json': {
                'value': 'afiliados-no-asalariados.json-stat',
                'trend': 'afiliados-no-asalariados-tendencia.json-stat'
            }
        },
        'ipc': {
            'sheet': 'Ipc',
            'label': 'Índice de precios al consumo',
            'category': 'Nivel, calidad y condiciones de vida',
            'value_vars': ['Ipc Cantabria', 'Ipc España'],
            'rate_vars': [
                'Ipc Cantabria. Var interanual',
                'Ipc España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Índice de Precios al Consumo del INE',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Índice'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Índice'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
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
            'category': 'Industria y energía',
            'value_vars': [
                'Matriculación de vehículos Cantabria',
                'Matriculación de vehículos España'],
            'rate_vars': [
                'Matriculación de vehículos Cantabria. Var interanual',
                'Matriculación de vehículos España. Var interanual'],
            'trend_vars': [
                'Matriculación de vehículos Cantabria. Tendencia',
                'Matriculación de vehículos España. Tendencia'],
            'source': 'ICANE a partir de Matriculación de Vehiculos de la Dirección General de Tráfico',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Vehículos'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Vehículos'},
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
                'value': 'matriculaciones.json-stat',
                'trend': 'matriculaciones-tendencia.json-stat'
            }
        },
        'clima': {
            'sheet': 'ECI',
            'label': 'Indicador de clima industrial',
            'category': 'Industria y energía',
            'value_vars': [
                'Indicador de clima industrial Cantabria',
                'Indicador de clima industrial España'],
            'rate_vars': [
                'Indicador de clima industrial Cantabria. Var interanual',
                'Indicador de clima industrial España. Var interanual'],
            'trend_vars': [
                'Indicador de clima industrial Cantabria. Tendencia',
                'Indicador de clima industrial España. Tendencia'],
            'source': 'ICANE a partir de Encuesta de Coyuntura Industrial del Ministerio de Industria, Comercio y Turismo',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 2, 'label': 'Saldo'},
                    'Valor España': {
                        'decimals': 2, 'label': 'Saldo'},
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
            "note":["Para una mejor interpretación la tasa de variación se da en términos absolutos al tratarse de un saldo de porcentaje"],
            'json': {
                'value': 'clima-industrial.json-stat',
                'trend': 'clima-industrial-tendencia.json-stat'
            }
        },
        'empresas': {
            'sheet': 'Emp',
            'label': 'Empresas inscritas en la Seguridad social',
            'category': 'Empresas',
            'value_vars': [
                'Empresas inscritas en la Seguridad Social Cantabria',
                'Empresas inscritas en la Seguridad Social España'],
            'rate_vars': [
                'Empresas inscritas en la Seguridad Social Cantabria. Var interanual',
                'Empresas inscritas en la Seguridad Social España. Var interanual'],
            'trend_vars': [
                'Empresas inscritas en la Seguridad Social Cantabria. Tendencia',
                'Empresas inscritas en la Seguridad Social España. Tendencia'],
            'source': 'ICANE a partir de Estadística de Empresas Inscritas en Seguridad Social del Ministerio de Trabajo, Migraciones y Seguridad Social',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Empresas'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Empresas'},
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
                'value': 'empresas.json-stat',
                'trend': 'empresas-tendencia.json-stat'
            }
        },
        'personas_fisicas': {
            'sheet': 'Emp_fi',
            'label': 'Personas físicas inscritas en la Seguridad social',
            'category': 'Empresas',
            'value_vars': [
                'Empresas personas físicas inscritas en la Seguridad Social Cantabria',
                'Personas físicas inscritas en la Seguridad Social España'],
            'rate_vars': [
                'Empresas personas físicas inscritas en la Seguridad Social Cantabria. Var interanual',
                'Empresas personas físicas inscritas en la Seguridad Social España. Var interanual'],
            'trend_vars': [
                'Empresas personas físicas inscritas en la Seguridad Social Cantabria. Tendencia',
                'Empresas personas físicass inscritas en la Seguridad Social España. Tendencia'],
            'source': 'ICANE a partir de Estadística de Empresas Inscritas en Seguridad Social del Ministerio de Trabajo, Migraciones y Seguridad Social',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Empresas'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Empresas'},
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
                'value': 'personas-fisicas.json-stat',
                'trend': 'personas-fisicas-tendencia.json-stat'
            }
        },
        'personas_juridicas': {
            'sheet': 'Emp_ju',
            'label': 'Personas jurídicas inscritas en la Seguridad social',
            'category': 'Empresas',
            'value_vars': [
                'Personas jurídicas inscritas en la Seguridad Social Cantabria',
                'Empresas personas jurídicas inscritas en la Seguridad Social España'],
            'rate_vars': [
                'Empresas personas jurídicas inscritas en la Seguridad Social Cantabria. Var interanual',
                'Empresas personas jurídicas inscritas en la Seguridad Social España. Var interanual'],
            'trend_vars': [
                'Empresas personas jurídicas inscritas en la Seguridad Social Cantabria. Tendencia',
                'Empresas personas jurídicas inscritas en la Seguridad Social España. Tendencia'],
            'source': 'ICANE a partir de Estadística de Empresas Inscritas en Seguridad Social del Ministerio de Trabajo, Migraciones y Seguridad Social',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Empresas'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Empresas'},
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
                'value': 'personas-juridicas.json-stat',
                'trend': 'personas-juridicas-tendencia.json-stat'
            }
        },
        'trafico_aereo': {
            'sheet': 'Taereo',
            'label': 'Tráfico aéreo de pasajeros',
            'category': 'Servicios',
            'value_vars': [
                'Tráfico aéreo de pasajeros Cantabria',
                'Tráfico aéreo de pasajeros España'],
            'rate_vars': [
                'Tráfico aéreo de pasajeros Cantabria. Var interanual',
                'Tráfico aéreo de pasajeros España. Var interanual'],
            'trend_vars': [
                'Tráfico aéreo de pasajeros Cantabria. Tendencia',
                'Tráfico aéreo de pasajeros España. Tendencia'],
            'source': 'ICANE a partir de Estadística de tráfico aéreo de AENA',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Pasajeros'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Pasajeros'},
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
            "note":["Los datos de 2018 son provisionales"],
            'json': {
                'value': 'trafico-aereo.json-stat',
                'trend': 'trafico-aereo-tendencia.json-stat'
            }
        },
        'pernoctaciones_hoteleras': {
            'sheet': 'CTH',
            'label': 'Pernoctaciones hoteleras',
            'category': 'Servicios',
            'value_vars': [
                'Pernoctaciones hoteleras Cantabria',
                'Pernoctaciones hoteleras España'],
            'rate_vars': [
                'Pernoctaciones hoteleras Cantabria. Var interanual',
                'Pernoctaciones hoteleras España. Var interanual'],
            'trend_vars': [
                'Pernoctaciones hoteleras Cantabria. Tendencia',
                'Pernoctaciones hoteleras España. Tendencia'],
            'source': 'ICANE a partir de Coyuntura Turística Hotelera del INE',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Pernoctaciones'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Pernoctaciones'},
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
                'value': 'pernoctaciones-hoteleras.json-stat',
                'trend': 'pernoctaciones-hoteleras-tendencia.json-stat'
            }
        },
        'icm': {
            'sheet': 'ICM',
            'label': 'Índice de comercio al por menor a precios constantes',
            'category': 'Servicios',
            'value_vars': [
                'Índice de comercio al por menor a precios constantes Cantabria',
                'Índice de comercio al por menor a precios constantes España'],
            'rate_vars': [
                'Índice de comercio al por menor a precios constantes Cantabria. Var interanual',
                'Índice de comercio al por menor a precios constantes España. Var interanual'],
            'trend_vars': [
                'Índice de comercio al por menor a precios constantes Cantabria. Tendencia',
                'Índice de comercio al por menor a precios constantes España. Tendencia'],
            'source': 'ICANE a partir de Índice de Comercio al por Menor del INE',
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
                'value': 'icm.json-stat',
                'trend': 'icm-tendencia.json-stat'
            }
        }
    },
    'globals': {
        'csv': 'vision-global-mensuales.csv'
    }
}

monthly_cfg = Baseconfig(params)
monthly_cfg.add(common_cfg)
