"""Generation of JSON-Stat datasets."""

"""Import configuration."""
from config import etl_cfg

from etlstat.extractor.extractor import xlsx

from numpy import arange

from pyjstat import pyjstat


def anno_mes(df):
    """Replace the value of Mes with yyyy - month."""
    df.reset_index(inplace=True)
    for i in range(1, len(df)):
        anno = str(df.loc[i, 'Año'])
        mes = str(df.loc[i, 'Mes'])
        df.loc[i, 'anno_mes'] =  anno + ' - ' + etl_cfg.month[mes]
    df.drop('Año', axis=1, inplace=True)
    df.drop('Mes', axis=1, inplace=True)
    df.rename(columns={'anno_mes': 'Mes'}, inplace=True)
    return df

def to_json(df, id_vars, value_vars,
            source='Instituto Cántabro de Estadística'):
    """Export dataframe to JSON-Stat dataset.
    
        id_vars (list): index columns
        value_vars (list): numeric variables (metrics)
    """
    df = df.melt(
        id_vars=id_vars,
        value_vars=value_vars,
        var_name='Variables')
    id_vars.append('Variables')
    df = df.sort_values(by=id_vars)
    dataset = pyjstat.Dataset.read(df, source=source)
    metric = {'metric': ['Variables']}
    dataset.setdefault('role', metric)
    return dataset.write(output='jsonstat')

def write_to_file(json_data, file_name):
    file = open(file_name, 'w')
    file.write(json_data)
    file.close()

data = xlsx(etl_cfg.input.path)

# Indicadores de paro registrado mensual
paro = data[etl_cfg.input.file.mensual]['Hoja1'][[
    'Año',
    'Mes',
    'Paro Cantabria',
    'Paro España'
]].copy()
paro = paro.tail(61)
paro = anno_mes(paro)
json_file = to_json(
    paro,
    ['Mes'],
    ['Paro Cantabria', 'Paro España'],
    'ICANE a partir de Movimiento Laboral Registrado del SEPE')
write_to_file(json_file, etl_cfg.output.path + 'paro_registrado.json-stat')

paro_tendencia = data[etl_cfg.input.file.mensual]['Hoja1'][[
    'Año',
    'Mes',
    'Paro Cantabria. Var interanual',
    'Paro Cantabria. Tendencia',
    'Paro España. Var interanual',
    'Paro España. Tendencia'
]].copy()
paro_tendencia = paro_tendencia.tail(61)
paro_tendencia = anno_mes(paro_tendencia)
json_file = to_json(
    paro_tendencia,
    ['Mes'],
    ['Paro Cantabria. Var interanual', 'Paro Cantabria. Tendencia',
     'Paro España. Var interanual', 'Paro España. Tendencia'],
    'ICANE a partir de Movimiento Laboral Registrado del SEPE')
write_to_file(json_file, etl_cfg.output.path + 'paro_registrado_tendencia.json-stat')

# Indicadores de contratos registrados mensuales
contratos = data[etl_cfg.input.file.mensual]['Hoja1'][[
    'Año',
    'Mes',
    'Contratos Cantabria',
    'Contratos España'
]].copy()
contratos = contratos.tail(61)
contratos = anno_mes(contratos)
json_file = to_json(
    contratos,
    ['Mes'],
    ['Contratos Cantabria', 'Contratos España'],
    'ICANE a partir de Movimiento Laboral Registrado del SEPE')
write_to_file(json_file, etl_cfg.output.path + 'contratos_registrados.json-stat')

contratos_tendencia = data[etl_cfg.input.file.mensual]['Hoja1'][[
    'Año',
    'Mes',
    'Contratos Cantabria. Var interanual',
    'Contratos Cantabria. Tendencia',
    'Contratos España. Var interanual',
    'Contratos España. Tendencia'
]].copy()
contratos_tendencia = contratos_tendencia.tail(61)
contratos_tendencia = anno_mes(contratos_tendencia)
json_file = to_json(
    contratos_tendencia,
    ['Mes'],
    ['Contratos Cantabria. Var interanual', 'Contratos Cantabria. Tendencia',
     'Contratos España. Var interanual', 'Contratos España. Tendencia'],
    'ICANE a partir de Movimiento Laboral Registrado del SEPE')
write_to_file(json_file, etl_cfg.output.path + 'contratos_registrados_tendencia.json-stat')

print('Fin del proceso. Ficheros generados con éxito')