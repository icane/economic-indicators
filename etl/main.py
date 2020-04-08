"""Generation of JSON-Stat datasets."""

"""Import configuration."""
from config import etl_cfg

from etlstat.extractor.extractor import xlsx

from numpy import arange

from pyjstat import pyjstat


def transform(df, time_columns, labels):
    """Slice dataframe. Generate time period column.
    
        df (dataframe): dataset
        time_columns (list): [year_column, month|quarter_column]
        labels (dict): time period labels
    """
    df = df.tail(etl_cfg.periods)
    df.reset_index(inplace=True)

    for i in range(0, len(df)):
        period1 = str(df.loc[i, time_columns[0]])
        period2 = str(df.loc[i, time_columns[1]])
        df.loc[i, 'period'] =  period1 + ' - ' + \
            labels[str(df.loc[i, time_columns[1]])]

    df.drop(columns={time_columns[0], time_columns[1]}, axis=1, inplace=True)
    df.rename(columns={'period': time_columns[1]}, inplace=True)
    return df

def to_json(df, id_vars, value_vars,
            source='Instituto Cántabro de Estadística'):
    """Export dataframe to JSON-Stat dataset.
    
        df (dataframe): dataset
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

"""Comienzo del proceso."""
data = xlsx(etl_cfg.input.path)

"""Series trimestrales."""

# Confianza empresarial
confianza = data[etl_cfg.input.trimestral.file]\
    [etl_cfg.input.trimestral.series.confianza][[
    'Año', 'Trimestre', 'Dato Cantabria', 'Dato España']].copy()
confianza = transform(confianza, ['Año', 'Trimestre'], etl_cfg.quarter)
json_file = to_json(
    confianza,
    ['Trimestre'],
    ['Dato Cantabria', 'Dato España'],
    etl_cfg.input.trimestral.sources.confianza)
write_to_file(json_file, etl_cfg.output.path + etl_cfg.output.trimestral.files.confianza)

print('Fin del proceso. Ficheros generados con éxito')