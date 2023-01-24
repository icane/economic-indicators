from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_mensual.xlsx',
    'series': {
        'deficit_publico_ccaa': {
            'sheet': 'PCN',
            'label': 'Déficit público CC.AA',
            'category': 'Economía',
            'value_vars': [
                'Deficit público CC.AA  Cantabria',
                'Deficit público CC.AA España'],
            'rate_vars': [
                'Deficit público CC.AA Cantabria. Var interanual',
                'Deficit público CC.AA España. Var interanual'],
            'trend_vars': [
                'Deficit público CC.AA Cantabria. Tendencia',
                'Deficit público CC.AA España. Tendencia'],
            'source': 'ICANE a partir de Presupuestos de la Comunidad Autónoma en términos de Contabilidad Nacional de la IGAE',
            'unit': {
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
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': ['Datos acumulados a final de periodo. Los datos de 2020 son avance.'],
            'json': {
                'value': 'deficit-publico-ccaa.json-stat',
                'trend': 'deficit-publico-ccaa-tendencia.json-stat'
            }
        },
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
            'unit': {
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
            'note': [''],
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
            'unit': {
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
            'note': [''],
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
            'unit': {
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
            'note': ['Datos a último día de mes'],
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
            'unit': {
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
            'note': ['Datos a último día de mes'],
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
            'unit': {
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
            'note': ['Datos a último día de mes'],
            'json': {
                'value': 'afiliados-no-asalariados.json-stat',
                'trend': 'afiliados-no-asalariados-tendencia.json-stat'
            }
        },
        'prd_b': {
            'sheet': 'PRD_B',
            'label': 'Beneficiarios prestaciones por desempleo',
            'category': 'Nivel, calidad y condiciones de vida',
            'value_vars': [
                'Beneficiarios prestaciones por desempleo Cantabria',
                'Beneficiarios prestaciones por desempleos España'],
            'rate_vars': [
                'Beneficiarios prestaciones por desempleo Cantabria. Var interanual',
                'Beneficiarios prestaciones por desempleos España. Var interanual'],
            'trend_vars': [
                'Beneficiarios prestaciones por desempleo Cantabria. Tendencia',
                'Beneficiarios prestaciones por desempleos España. Tendencia'],
            'source': 'ICANE a partir de Prestaciones por Desempleo del Ministerio de Trabajo, Migraciones y Seguridad Social',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Beneficiarios'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Beneficiarios'},
                },
                'trend': {
                    'Var. interanual Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Var. interanual España': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'}
                }
            },
            'note': ['A último día del mes'],
            'json': {
                'value': 'prestacion-desempleo-beneficiarios.json-stat',
                'trend': 'prestacion-desempleo-beneficiarios-tendencia.json-stat'
            }
        },
        'prd_g': {
            'sheet': 'PRD_G',
            'label': 'Gasto prestaciones por desempleo',
            'category': 'Nivel, calidad y condiciones de vida',
            'value_vars': [
                'Gasto prestaciones por desempleo Cantabria',
                'Gasto prestaciones por desempleos España'],
            'rate_vars': [
                'Gasto prestaciones por desempleo Cantabria. Var interanual',
                'Gasto prestaciones por desempleos España. Var interanual'],
            'trend_vars': [
                'Gasto prestaciones por desempleo Cantabria. Tendencia',
                'Gasto prestaciones por desempleos España. Tendencia'],
            'source': 'ICANE a partir de Prestaciones por Desempleo del Ministerio de Trabajo, Migraciones y Seguridad Social',
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
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'}
                }
            },
            'note': ['Gasto contablilizado en el mes siguiente pero devengado en el mes'],
            'json': {
                'value': 'gasto-prestaciones-desempleo.json-stat',
                'trend': 'gasto-prestaciones-desempleo-tendencia.json-stat'
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
            'trend_vars': [
                'Ipc Cantabria. Tendencia',
                'Ipc España. Tendencia'],
            'source': 'ICANE a partir de Índice de Precios al Consumo del INE',
            'unit': {
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
                        'decimals': 2, 'label': '%'},
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': [''],
            'json': {
                'value': 'ipc.json-stat',
                'trend': 'ipc-tendencia.json-stat'
            }
        },
        'pensiones_contributivas': {
            'sheet': 'P_CONTR',
            'label': 'Pensiones Contributivas',
            'category': 'Nivel, calidad y condiciones de vida',
            'value_vars': [
                'Pensiones Contributivas Cantabria',
                'Pensiones Contributivas España'],
            'rate_vars': [
                'Pensiones Contributivas Cantabria. Var interanual',
                'Pensiones Contributivas España. Var interanual'],
            'trend_vars': [
                'Pensiones Conbtributivas Cantabria. Tendencia',
                'Pensiones Contributivas España. Tendencia'],
            'source': 'ICANE a partir de pensiones contributivas del Ministerio de Trabajo, Migraciones y Seguridad Social',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Número de pensiones'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Número de pensiones'},
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
            'note': [''],
            'json': {
                'value': 'pensiones-contributivas.json-stat',
                'trend': 'pensiones-contributivas-tendencia.json-stat'
            }
        },
        'pensiones_no_contributivas': {
            'sheet': 'P_NO_CONTR',
            'label': 'Pensiones No Contributivas',
            'category': 'Nivel, calidad y condiciones de vida',
            'value_vars': [
                'Pensiones no Contributivas Cantabria',
                'Pensiones no Contributivas España'],
            'rate_vars': [
                'Pensiones no Contributivas Cantabria. Var interanual',
                'Pensiones no Contributivas España. Var interanual'],
            'trend_vars': [
                'Pensiones no Conbtributivas Cantabria. Tendencia',
                'Pensiones no Contributivas España. Tendencia'],
            'source': 'ICANE a partir de prestaciones no contributivas del Ministerio de Trabajo, Migraciones y Seguridad Social',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Número de pensiones'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Número de pensiones'},
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
            'note': [''],
            'json': {
                'value': 'pensiones-no-contributivas.json-stat',
                'trend': 'pensiones-no-contributivas-tendencia.json-stat'
            }
        },
        'indice_cifra_negocios_industria': {
            'sheet': 'ICN',
            'label': 'Índice de cifra de negocios en la industria',
            'category': 'Industria y energía',
            'value_vars': [
                'Índice de cifra de negocios en la industria Cantabria',
                'Índice de cifra de negocios en la industria España'],
            'rate_vars': [
                'Índice de cifra de negocios en la industria Cantabria. Var interanual',
                'Índice de cifra de negocios en la industria España. Var interanual'],
            'trend_vars': [
                'Índice de cifra de negocios en la industria Cantabria. Tendencia',
                'Índice de cifra de negocios en la industria España. Tendencia'],
            'source': 'ICANE a partir de Ìndice de Cifra de Negocios en la Industria del INE',
            'unit': {
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
                        'decimals': 2, 'label': '%'},
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': [''],
            'json': {
                'value': 'indice-cifra-negocios-industria.json-stat',
                'trend': 'indice-cifra-negocios-industria-tendencia.json-stat'
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
            'unit': {
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
            'note': [''],
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
            'unit': {
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
            'note': ['Para una mejor interpretación la tasa de variación se da en términos absolutos al tratarse de un saldo de porcentaje'],
            'json': {
                'value': 'clima-industrial.json-stat',
                'trend': 'clima-industrial-tendencia.json-stat'
            }
        },
        'ipi': {
            'sheet': 'IPI',
            'label': 'Índice de Producción Industrial',
            'category': 'Industria y energía',
            'value_vars': [
                'Índice de Producción Industrial  Cantabria',
                'Índice de Producción Industrial  España'],
            'rate_vars': [
                'Índice de Producción Industrial  Cantabria. Var interanual',
                'Índice de Producción Industrial s España. Var interanual'],
            'trend_vars': [
                'Índice de Producción Industrial  Cantabria. Tendencia',
                'Índice de Producción Industrial s España. Tendencia'],
            'source': 'ICANE  a partir de Índice de Producción Industrial del INE',
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
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': [''],
            'json': {
                'value': 'ipi.json-stat',
                'trend': 'ipi-tendencia.json-stat'
            }
        },
        'consumo_productos_petroliferos': {
            'sheet': 'CP',
            'label': 'Consumo de productos petrolíferos',
            'category': 'Industria y energía',
            'value_vars': [
                'Consumo de productos petrolíferos Cantabria',
                'Consumo de productos petrolíferos España'],
            'rate_vars': [
                'Consumo de productos petrolíferos Cantabria. Var interanual',
                'Consumo de productos petrolíferos España. Var interanual'],
            'trend_vars': [
                'Consumo de productos petrolíferos Cantabria. Tendencia',
                'Consumo de productos petrolíferos España. Tendencia'],
            'source': 'ICANE a partir de Consumo de Productos Pretrolíferos del CORES',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 2, 'label': 'Toneladas'},
                    'Valor España': {
                        'decimals': 2, 'label': 'Toneladas'},
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
            'note': ['Los datos del año en curso y del año precedente pueden sufrir variaciones debidas a rectificaciones enviadas por las compañías informantes.'],
            'json': {
                'value': 'consumo-productos-petroliferos.json-stat',
                'trend': 'consumo-productos-petroliferos-tendencia.json-stat'
            }
        },
        'consumo_gas_natural': {
            'sheet': 'CGN',
            'label': 'Consumo de gas natural',
            'category': 'Industria y energía',
            'value_vars': [
                'Consumo de gas natural Cantabria',
                'Consumo de gas natural España'],
            'rate_vars': [
                'Consumo de gas natural Cantabria. Var interanual',
                'Consumo de gas natural España. Var interanual'],
            'trend_vars': [
                'Consumo de gas natural Cantabria. Tendencia',
                'Consumo de gas natural España. Tendencia'],
            'source': 'ICANE a partir de consumo de Gas Natural de CORES',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Gigavatios hora'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Gigavatios hora'},
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
            'note': ['Debido a desajustes en la información remitida pueden encontrarse pequeñas diferencias entre los datos de consumos desglosados por grupos de presión y los desglosados por Comunidades Autónomas. Datos provisionales.'],
            'json': {
                'value': 'consumo-gas-natural.json-stat',
                'trend': 'consumo-gas-natural-tendencia.json-stat'
            }
        },
        'consumo_cemento': {
            'sheet': 'CEMENTO',
            'label': 'Consumo de cemento',
            'category': 'Construcción',
            'value_vars': [
                'Consumo de cemento Zona Oeste',
                'Consumo de cemento España'],
            'rate_vars': [
                'Consumo de cemento Zona Oeste. Var interanual',
                'Consumo de cemento España. Var interanual'],
            'trend_vars': [
                'Consumo de cemento Zona Oeste. Tendencia',
                'Consumo de cemento España. Tendencia'],
            'source': 'ICANE a partir de datos de Estadística de Cemento de Oficemen',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Toneladas'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Toneladas'},
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
            'note': ['Son provisionales los datos del último año.'],
            'json': {
                'value': 'consumo-cemento.json-stat',
                'trend': 'consumo-cemento-tendencia.json-stat'
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
            'unit': {
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
            'note': [''],
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
            'unit': {
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
            'note': [''],
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
            'unit': {
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
            'note': [''],
            'json': {
                'value': 'personas-juridicas.json-stat',
                'trend': 'personas-juridicas-tendencia.json-stat'
            }
        },
        'sociedades_mercantiles_constituidas': {
            'sheet': 'SM_C',
            'label': 'Sociedades mercantiles constituidas',
            'category': 'Empresas',
            'value_vars': [
                'Sociedades mercantiles constituidas Cantabria',
                'Sociedades mercantiles constituidas España'],
            'rate_vars': [
                'Sociedades mercantiles constituidas Cantabria. Var interanual',
                'Sociedades mercantiles constituidas España. Var interanual'],
            'trend_vars': [
                'Sociedades mercantiles constituidas Cantabria. Tendencia',
                'Sociedades mercantiles constituidas España. Tendencia'],
            'source': 'ICANE a partir de Sociedades Mercantiles del INE',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Sociedades'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Sociedades'},
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
            'note': ['Los datos son provisionales desde Enero de 2020'],
            'json': {
                'value': 'sociedades-mercantiles-constituidas.json-stat',
                'trend': 'sociedades-mercantiles-constituidas-tendencia.json-stat'
            }
        },
        'sociedades_mercantiles_disueltas': {
            'sheet': 'SM_D',
            'label': 'Sociedades mercantiles disueltas',
            'category': 'Empresas',
            'value_vars': [
                'Sociedades mercantiles disueltas Cantabria',
                'Sociedades mercantiles disueltas España'],
            'rate_vars': [
                'Sociedades mercantiles disueltas Cantabria. Var interanual',
                'Sociedades mercantiles disueltas España. Var interanual'],
            'trend_vars': [
                'Sociedades mercantiles disueltas Cantabria. Tendencia',
                'Sociedades mercantiles disueltas España. Tendencia'],
            'source': 'ICANE a partir de Sociedades Mercantiles del INE',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 0, 'label': 'Sociedades'},
                    'Valor España': {
                        'decimals': 0, 'label': 'Sociedades'},
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
            'note': ['Los datos son provisionales desde Enero de 2020'],
            'json': {
                'value': 'sociedades-mercantiles-disueltas.json-stat',
                'trend': 'sociedades-mercantiles-disueltas-tendencia.json-stat'
            }
        },
        'indice_cifra_negocios_servicios': {
            'sheet': 'IASS',
            'label': 'Índice de cifra de negocios del sector servicios',
            'category': 'Servicios',
            'value_vars': [
                'Índice de cifra de negocios del sector servicios Cantabria',
                'Índice de cifra de negocios del sector servicios España'],
            'rate_vars': [
                'Índice de cifra de negocios del sector servicios Cantabria. Var interanual',
                'Índice de cifra de negocios del sector servicios España. Var interanual'],
            'trend_vars': [
                'Índice de cifra de negocios del sector servicios Cantabria. Tendencia',
                'Índice de cifra de negocios del sector servicios España. Tendencia'],
            'source': 'ICANE a partir de Indicador de Actividad del Sector Servicios del INE',
            'unit': {
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
                        'decimals': 2, 'label': '%'},
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': [''],
            'json': {
                'value': 'indice-cifra-negocios-servicios.json-stat',
                'trend': 'indice-cifra-negocios-servicios-tendencia.json-stat'
            }
        },
        'indice_ocupacion_servicios': {
            'sheet': 'IASS_2',
            'label': 'Índice de ocupación del sector servicios',
            'category': 'Servicios',
            'value_vars': [
                'Índice de ocupación del sector servicios Cantabria',
                'Índice de ocupación del sector servicios España'],
            'rate_vars': [
                'Índice de ocupación del sector servicios Cantabria. Var interanual',
                'Índice de ocupación del sector servicios España. Var interanual'],
            'trend_vars': [
                'Índice de ocupación del sector servicios Cantabria. Tendencia',
                'Índice de ocupación del sector servicios España. Tendencia'],
            'source': 'ICANE a partir de Indicador de Actividad del Sector Servicios del INE',
            'unit': {
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
                        'decimals': 2, 'label': '%'},
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': [''],
            'json': {
                'value': 'indice-ocupacion-servicios.json-stat',
                'trend': 'indice-ocupacion-servicios-tendencia.json-stat'
            }
        },
        'icm': {
            'sheet': 'ICM',
            'label': 'Índice de cifra de negocios del comercio al por menor a precios constantes',
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
            'unit': {
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
            'note': [''],
            'json': {
                'value': 'icm.json-stat',
                'trend': 'icm-tendencia.json-stat'
            }
        },
        'indice_ocupacion_comercio_menor': {
            'sheet': 'ICM (2)',
            'label': 'Índice de ocupación del comercio al por menor',
            'category': 'Servicios',
            'value_vars': [
                'Índice de ocupacion del comercio al por menor Cantabria',
                'Índice de ocupacion del comercio al por menor España'],
            'rate_vars': [
                'Índice de ocupacion del comercio al por menor Cantabria. Var interanual',
                'Índice de ocupacion del comercio al por menors España. Var interanual'],
            'trend_vars': [
                'Índice de ocupacion del comercio al por menor Cantabria. Tendencia',
                'Índice de ocupacion del comercio al por menor España. Tendencia'],
            'source': 'ICANE a partir de Índice de Comercio al por Menor del INE',
            'unit': {
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
                        'decimals': 2, 'label': '%'},
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': [''],
            'json': {
                'value': 'indice-ocupacion-comercio-menor.json-stat',
                'trend': 'indice-ocupacion-comercio-menor-tendencia.json-stat'
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
            'unit': {
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
            'note': [''],
            'json': {
                'value': 'trafico-aereo.json-stat',
                'trend': 'trafico-aereo-tendencia.json-stat'
            }
        },
        'trafico_portuario': {
            'sheet': 'TPS_M',
            'label': 'Tráfico portuario',
            'category': 'Servicios',
            'value_vars': [
                'Tráfico portuario Cantabria',
                'Tráfico portuario España'],
            'rate_vars': [
                'Tráfico portuario Cantabria. Var interanual',
                'Tráfico portuario España. Var interanual'],
            'trend_vars': [
                'Tráfico portuario Cantabria. Tendencia',
                'Tráfico portuario España. Tendencia'],
            'source': 'ICANE a partir de Estadística del Puerto de la Autoridad Portuaria de Santander y Ministerio de Fomento',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 1, 'label': 'Toneladas'},
                    'Valor España': {
                        'decimals': 1, 'label': 'Toneladas'},
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
            'note': [''],
            'json': {
                'value': 'trafico-portuario.json-stat',
                'trend': 'trafico-portuario-tendencia.json-stat'
            }
        },
        'trafico_portuario_pasajeros': {
            'sheet': 'TPS_P',
            'label': 'Tráfico portuario de pasajeros',
            'category': 'Servicios',
            'value_vars': [
                'Tráfico portuario de pasajeros Cantabria',
                'Tráfico portuario de pasajeros España'],
            'rate_vars': [
                'Tráfico portuario de pasajeros Cantabria. Var interanual',
                'Tráfico portuario de pasajeros España. Var interanual'],
            'trend_vars': [
                'Tráfico portuario de pasajeros Cantabria. Tendencia',
                'Tráfico portuario de pasajeros España. Tendencia'],
            'source': 'ICANE a partir de Estadística del Puerto de la Autoridad Portuaria de Santander y Ministerio de Fomento',
            'unit': {
                'value': {
                    'Valor Cantabria': {
                        'decimals': 1, 'label': 'Pasajeros'},
                    'Valor España': {
                        'decimals': 1, 'label': 'Pasajeros'},
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
            'note': [''],
            'json': {
                'value': 'trafico-portuario-pasajeros.json-stat',
                'trend': 'trafico-portuario-pasajeros-tendencia.json-stat'
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
            'unit': {
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
            'note': [''],
            'json': {
                'value': 'pernoctaciones-hoteleras.json-stat',
                'trend': 'pernoctaciones-hoteleras-tendencia.json-stat'
            }
        },
        'pernoctaciones_extrahoteleras': {
            'sheet': 'EOAT',
            'label': 'Pernoctaciones extrahoteleras',
            'category': 'Servicios',
            'value_vars': [
                'Pernoctaciones extrahoteleras Cantabria',
                'Pernoctaciones extrahoteleras España'],
            'rate_vars': [
                'Pernoctaciones extrahoteleras Cantabria. Var interanual',
                'Pernoctaciones extrahoteleras España. Var interanual'],
            'trend_vars': [
                'Pernoctaciones extrahoteleras Cantabria. Tendencia',
                'Pernoctaciones extrahoteleras España. Tendencia'],
            'source': 'ICANE a partir de Encuesta de Ocupación de Alojamientos Turísticos Extrahoteleros del INE',
            'unit': {
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
            'note': ['Los datos de enero, febrero, marzo y mayo de 2020 para Cantabria no tienen la información de camping por secreto estadístico.'],
            'json': {
                'value': 'pernoctaciones-extrahoteleras.json-stat',
                'trend': 'pernoctaciones-extrahoteleras-tendencia.json-stat'
            }
        },
        'importaciones': {
            'sheet': 'M',
            'label': 'Importaciones',
            'category': 'Sector exterior',
            'value_vars': ['Importaciones Cantabria', 'Importaciones España'],
            'rate_vars': [
                'Importaciones Cantabria. Var interanual',
                'Importaciones España. Var interanual'],
            'trend_vars': [
                'Importaciones Cantabria. Tendencia',
                'Importaciones España. Tendencia'],
            'source': 'ICANE a partir de Estadistica de Comercio Exterior de la AEAT',
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
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': ['Los datos son provisionales desde enero 2020. Las tasas de variación de 2020 se han calculado con los datos provisionales del año 2019 según las recomendaciones de la AEAT.'],
            'json': {
                'value': 'importaciones.json-stat',
                'trend': 'importaciones-tendencia.json-stat'
            }
        },
        'exportaciones': {
            'sheet': 'X',
            'label': 'Exportaciones',
            'category': 'Sector exterior',
            'value_vars': [
                'Exportaciones Cantabria', 'Exportaciones España'],
            'rate_vars': [
                'Exportaciones Cantabria. Var interanual',
                'Exportaciones España. Var interanual'],
            'trend_vars': [
                'Exportaciones Cantabria. Tendencia',
                'Exportaciones España. Tendencia'],
            'source': 'ICANE a partir de Estadistica de Comercio Exterior de la AEAT',
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
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': ['Los datos son provisionales desde enero 2020. Las tasas de variación de 2020 se han calculado con los datos provisionales del año 2019 según las recomendaciones de la AEAT.'],
            'json': {
                'value': 'exportaciones.json-stat',
                'trend': 'exportaciones-tendencia.json-stat'
            }
        },
        'saldo_comercial': {
            'sheet': 'SALDO',
            'label': 'Saldo comercial',
            'category': 'Sector exterior',
            'value_vars': ['Saldo comercial Cantabria', 'Saldo comercial España'],
            'rate_vars': [
                'Saldo comercial Cantabria. Var interanual',
                'Saldo comercial España. Var interanual'],
            'trend_vars': [
                'Saldo comercial Cantabria. Tendencia',
                'Saldo comercial España. Tendencia'],
            'source': 'ICANE a partir de Estadistica de Comercio Exterior de la AEAT',
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
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': ['Los datos son provisionales desde enero 2019. Las tasas de variación de 2019 se han calculado con los datos provisionales del año 2018 según las recomendaciones de la AEAT'],
            'json': {
                'value': 'saldo-comercial.json-stat',
                'trend': 'saldo-comercial-tendencia.json-stat'
            }
        },
        'tasa_cobertura': {
            'sheet': 'TCOBER',
            'label': 'Tasa de cobertura',
            'category': 'Sector exterior',
            'value_vars': ['Tasa cobertura Cantabria', 'Tasa cobertura España'],
            'rate_vars': [
                'Tasa cobertura Cantabria. Var interanual',
                'Tasa cobertura España. Var interanual'],
            'trend_vars': [
                'Tasa cobertura Cantabria. Tendencia',
                'Tasa cobertura España. Tendencia'],
            'source': 'ICANE a partir de Estadistica de Comercio Exterior de la AEAT',
            'unit': {
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
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': ['Los datos son provisionales desde enero 2020. Las tasas de variación de 2020 se han calculado con los datos provisionales del año 2019 según las recomendaciones de la AEAT. Para una mejor interpretación la tasa de variación se da en términos absolutos al tratarse de una tasa.'],
            'json': {
                'value': 'tasa-cobertura.json-stat',
                'trend': 'tasa-cobertura-tendencia.json-stat'
            }
        },
        'gasto_farmaceutico_sanitario': {
            'sheet': 'GS',
            'label': 'Gasto en productos farmacéuticos y sanitarios',
            'category': 'Sanidad',
            'value_vars': [
                'Gasto en productos farmacéuticos y sanitarios Cantabria',
                'Gasto en productos farmacéuticos y sanitarios España'],
            'rate_vars': [
                'Gasto en productos farmacéuticos y sanitarios Cantabria. Var interanual',
                'Gasto en productos farmacéuticos y sanitarios España. Var interanual'],
            'trend_vars': [
                'Gasto en productos farmacéuticos y sanitarios Cantabria. Tendencia',
                'Gasto en productos farmacéuticos y sanitarios España. Tendencia'],
            'source': 'ICANE a partir de Gasto en productos farmacéuticos y sanitarios del Ministerio de Hacienda',
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
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note': ['Gasto devengado neto acumulado anual.'],
            'json': {
                'value': 'gasto-farmaceutico-sanitario.json-stat',
                'trend': 'gasto-farmaceutico-sanitario-tendencia.json-stat'
            }
        }
    },
    'globals': {
        'csv': 'vision-global-mensuales.csv'
    }
}

monthly_cfg = Baseconfig(params)
monthly_cfg.add(common_cfg)
