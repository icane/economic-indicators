from beautifuldict.baseconfig import Baseconfig

from etl.config_common import common_cfg

from decouple import config


params = {
    'file': 'Datos_carga_trimestral.xlsx',
    'series': {
        'pib_indices_volumen': {
            'sheet': 'PIB',
            'label': 'PIB índices de volumen',
            'category': 'Economía',
            'value_vars': [
                'PIB. Índice de volumen Cantabria',
                'PIB. Índice de volumen España'],
            'rate_vars': [
                'PIB. Índice de volumen Cantabria. Var interanual',
                'PIB. Índice de volumen España. Var interanual'],
            'trend_vars': [],
            'source': 'ICANE a partir de Contabilidad Trimestral de España del INE y Contabilidad Trimestral de Cantabria Base 2015 del ICANE',
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
                'value': 'pib-indices-volumen.json-stat',
                'trend': 'pib-indices-volumen-tendencia.json-stat'
            }
        },
        'deuda_publica_ccaa': {
            'sheet': 'DEUDA',
            'label': 'Deuda pública CC.AA',
            'category': 'Economía',
            'value_vars': [
                'Deuda pública CC.AA Cantabria',
                'Deuda pública CC.AA España'],
            'rate_vars': [
                'Deuda pública CC.AA Cantabria. Var interanual',
                'Deuda pública CC.AA España. Var interanual'],
            'trend_vars': [
                'Deuda pública CC.AA Cantabria. Tendencia',
                'Deuda pública CC.AA. Tendencia'],
            'source': 'ICANE a partir de Deuda según PDE del Banco de España',
            'unit':{
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
            'note':[''],
            'json': {
                'value': 'deuda-publica-ccaa.json-stat',
                'trend': 'deuda-publica-ccaa-tendencia.json-stat'
            }
        },
        'deuda_publica_ccaa_pib': {
            'sheet': 'DEUDA_PIB',
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
                        'decimals': 2, 'label': '%'}
                }
            },
            'note':['Para una mejor interpretación es el dato del indicador y no su tasa de variación anual'],
            'json': {
                'value': 'deuda-publica-ccaa-pib.json-stat',
                'trend': 'deuda-publica-ccaa-pib-tendencia.json-stat'
            }
        },
        'confianza': {
            'sheet': 'Indice confianza empresarial',
            'label': 'Índice de confianza empresarial',
            'category': 'Empresas y establecimientos',
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
            'category': 'Empresas y establecimientos',
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
            'note':['Los datos del T3 del año 2019 y posteriores son provisionales.'],
            'json': {
                'value': 'deudores-concursados.json-stat',
                'trend': 'deudores-concursados-tendencia.json-stat'
            }
        },
        'empresas_concursadas': {
            'sheet': 'EPC_E',
            'label': 'Empresas concursadas',
            'category': 'Empresas y establecimientos',
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
            'note':['Los datos del T3 del año 2019 y posteriores son provisionales.'],
            'json': {
                'value': 'empresas-concursadas.json-stat',
                'trend': 'empresas-concursadas-tendencia.json-stat'
            }
        },
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
        'transporte_mercancias_carretera': {
            'sheet': 'TMC',
            'label': 'Transporte de mercancías por carretera',
            'category': 'Servicios',
            'value_vars': [
                'Transporte de mercancias por carreteraCantabria',
                'Transporte de mercancias por carreteraEspaña'],
            'rate_vars': [
                'Transporte de mercancias por carreteraCantabria. Var interanual',
                'Transporte de mercancias por carreteraEspaña. Var interanual'],
            'trend_vars': [
                'Transporte de mercancias por carreteraCantabria. Tendencia',
                'Transporte de mercancias por carreteraEspaña. Tendencia'],
            'source': 'ICANE a partir de Transporte de Mercancías por Carretera del Ministerio de Transporte, Movilidad y Agenda Urbana',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 1, 'label': 'Miles de de toneladas'},
                    'Valor España': {
                        'decimals': 1, 'label': 'Miles de de toneladas'},
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
                'value': 'transporte-mercancias-carretera.json-stat',
                'trend': 'transporte-mercancias-carretera-tendencia.json-stat'
            }
        },
        'pernoctaciones_residentes_espana': {
            'sheet': 'ETR_1',
            'label': 'Pernoctaciones de los residentes en España',
            'category': 'Servicios',
            'value_vars': [
                'Pernoctaciones de los residentes en España. Cantabria',
                'Pernoctaciones de los residentes en España. España'],
            'rate_vars': [
                'Pernoctaciones de los residentes en España. Cantabria. Var. Interanual',
                'Pernoctaciones de los residentes en España. España. Var. Interanual'],
            'trend_vars': [
                'Pernoctaciones de los residentes en España. Cantabria. Tendencia',
                'Pernoctaciones de los residentes en España. España. Tendencia'],
            'source': 'ICANE a partir de Encuesta de Turismo de Residentes del INE',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 1, 'label': 'Pernoctaciones'},
                    'Valor España': {
                        'decimals': 1, 'label': 'Pernoctaciones'},
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
            'note':['Los datos del primer trimestre del año 2019 y posteriores son provisionales.'],
            'json': {
                'value': 'pernoctaciones-residentes-espana.json-stat',
                'trend': 'pernoctaciones-residentes-espana-tendencia.json-stat'
            }
        },
        'gasto_turistico_residentes_espana': {
            'sheet': 'ETR_2',
            'label': 'Gasto turístico de los residentes en España',
            'category': 'Servicios',
            'value_vars': [
                'Gasto turístico de los residentes en España. Cantabria',
                'Gasto turístico de los residentes en España. España'],
            'rate_vars': [
                'Gasto turístico de los residentes en España. Cantabria. Var. Interanual',
                'Gasto turístico de los residentes en España. España. Var. Interanual'],
            'trend_vars': [
                'Gasto turístico de los residentes en España. Cantabria. Tendencia',
                'Gasto turístico de los residentes en España. España. Tendencia'],
            'source': 'ICANE a partir de Encuesta de Turismo de Residentes del INE',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 1, 'label': 'Miles de euros '},
                    'Valor España': {
                        'decimals': 1, 'label': 'Miles de euros '},
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
            'note':['Los datos del primer trimestre del año 2019 y posteriores son provisionales.'],
            'json': {
                'value': 'gasto-turistico-residentes-espana.json-stat',
                'trend': 'gasto-turistico-residentes-espana-tendencia.json-stat'
            }
        },
        'turistas_internacionales': {
            'sheet': 'FRONTUR',
            'label': 'Turistas internacionales',
            'category': 'Servicios',
            'value_vars': [
                'Turistas internacionalesCantabria',
                'Turistas internacionales España'],
            'rate_vars': [
                'Turistas internacionalesCantabria. Var interanual',
                'Turistas internacionales España. Var interanual'],
            'trend_vars': [
                'Turistas internacionalesCantabria. Tendencia',
                'Turistas internacionales España. Tendencia'],
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
            'note':['Los datos del primer trimestre del año 2020 y posteriores son provisionales. Segundo trimestre del año 2020 para Cantabria no disponible por falta de respaldo muestral.'],
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
            'note':['Los datos del primer trimestre del año 2020 y posteriores son provisionales. Segundo trimestre del año 2020 para Cantabria no disponible por falta de respaldo muestral.'],
            'json': {
                'value': 'gasto-turistas-internacionales.json-stat',
                'trend': 'gasto-turistas-internacionales-tendencia.json-stat'
            }
        },
        'indice_precios_vivienda': {
            'sheet': 'IPV',
            'label': 'Índice de precios de vivienda',
            'category': 'Construcción',
            'value_vars': [
                'Índice de Pecios de Vivienda Cantabria',
                'Índice de Pecios de Vivienda España'],
            'rate_vars': [
                'Índice de Pecios de Vivienda Cantabria. Var interanual',
                'Índice de Pecios de Vivienda España. Var interanual'],
            'trend_vars': [
                'Índice de Pecios de Vivienda Cantabria. Tendencia',
                'Índice de Pecios de Vivienda España. Tendencia'],
            'source': 'ICANE a partir de  Índice de precios de vivienda del INE',
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
                'value': 'indice-precios-vivienda.json-stat',
                'trend': 'indice-precios-vivienda-tendencia.json-stat'
            }
        },
        'tasa_apertura': {
            'sheet': 'TA',
            'label': 'Tasa de apertura',
            'category': 'Sector exterior',
            'value_vars': [
                'Tasa de apertura Cantabria',
                'Tasa de apertura España'],
            'rate_vars': [],
            'trend_vars': [],
            'source': 'ICANE a partir de Estadística de Comercio Exterior de la AEAT, Contabilidad Nacional Trimestral de España del INE y Contabilidad Trimestral de Cantabria Base 2015 del ICANE',
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
                    'Tendencia Cantabria': {
                        'decimals': 2, 'label': '%'},
                    'Tendencia España': {
                        'decimals': 2, 'label': '%'},
                }
            },
            'note':['Tasa de apertura= (saldo comercial/PIB)*100.  Para una mejor interpretación es el dato del indicador y no su tasa de variación anual'],
            'json': {
                'value': 'tasa-apertura.json-stat',
                'trend': 'tasa-apertura-tendencia.json-stat'
            }
        },
        'transacciones_inmobiliarias': {
            'sheet': 'TI',
            'label': 'Transacciones inmobiliarias',
            'category': 'Construcción',
            'value_vars': [
                'Transacciones inmobiliarias Cantabria',
                'Transacciones inmobiliarias España'],
            'rate_vars': [
                'Transacciones inmobiliarias Cantabria. Var interanual',
                'Transacciones inmobiliarias España. Var interanual'],
            'trend_vars': [
                'Transacciones inmobiliarias Cantabria. Tendencia',
                'Transacciones inmobiliarias. Tendencia'],
            'source': 'ICANE a partir de Transacciones inmobiliarias del Ministerio de Transportes Movilidad y Agenda Urbana',
            'unit':{
                'value': {
                    'Valor Cantabria': {
                        'decimals': 1, 'label': 'Transacciones'},
                    'Valor España': {
                        'decimals': 1, 'label': 'Transacciones'},
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
            'note':['Los datos del último trimestre son provisionales'],
            'json': {
                'value': 'transacciones-inmobiliarias.json-stat',
                'trend': 'transacciones-inmobiliarias-tendencia.json-stat'
            }
        }
    },
    'globals': {
        'csv': 'vision-global-trimestrales.csv'
    }
}

quarterly_cfg = Baseconfig(params)
quarterly_cfg.add(common_cfg)