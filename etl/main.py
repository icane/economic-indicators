"""Generation of JSON-Stat datasets."""

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

"""Read all input files."""
data = xlsx(etl_cfg.input.path)

"""Quarterly series."""

for key in etl_cfg.input.quarterly.series:
    df = data[etl_cfg.input.quarterly.file]\
        [etl_cfg.input.quarterly.series[key]][[
        'Año', 'Trimestre', 'Dato Cantabria', 'Dato España']].copy()
    df = transform(df, ['Año', 'Trimestre'], etl_cfg.quarter)
    json_file = to_json(
        df,
        ['Trimestre'],
        ['Dato Cantabria', 'Dato España'],
        etl_cfg.input.quarterly.sources[key])
    write_to_file(json_file, etl_cfg.output.path + etl_cfg.output.quarterly.files[key])

    df_tendencia = data[etl_cfg.input.quarterly.file]\
        [etl_cfg.input.quarterly.series[key]][[
            'Año',
            'Trimestre',
            'Var interanual Cantabria',
            'Tendencia Cantabria',
            'Var interanual España',
            'Tendencia España']].copy()
    df_tendencia = transform(df_tendencia, ['Año', 'Trimestre'], etl_cfg.quarter)
    json_file = to_json(
        df_tendencia,
        ['Trimestre'],
        ['Var interanual Cantabria','Tendencia Cantabria',
        'Var interanual España', 'Tendencia España'],
        etl_cfg.input.quarterly.sources[key])
    write_to_file(json_file, etl_cfg.output.path + etl_cfg.output.quarterly.files[str(key) + '_tendencia'])

"""Monthly series."""

for key in etl_cfg.input.monthly.series:
    df = data[etl_cfg.input.monthly.file]\
        [etl_cfg.input.monthly.series[key]][[
        'Año', 'Mes', 'Dato Cantabria', 'Dato España']].copy()
    df = transform(df, ['Año', 'Mes'], etl_cfg.month)
    json_file = to_json(
        df,
        ['Mes'],
        ['Dato Cantabria', 'Dato España'],
        etl_cfg.input.monthly.sources[key])
    write_to_file(json_file, etl_cfg.output.path + etl_cfg.output.monthly.files[key])

    df_tendencia = data[etl_cfg.input.monthly.file]\
        [etl_cfg.input.monthly.series[key]][[
            'Año',
            'Mes',
            'Var interanual Cantabria',
            'Tendencia Cantabria',
            'Var interanual España',
            'Tendencia España']].copy()
    df_tendencia = transform(df_tendencia, ['Año', 'Mes'], etl_cfg.month)
    json_file = to_json(
        df_tendencia,
        ['Mes'],
        ['Var interanual Cantabria','Tendencia Cantabria',
        'Var interanual España', 'Tendencia España'],
        etl_cfg.input.monthly.sources[key])
    write_to_file(json_file, etl_cfg.output.path + etl_cfg.output.monthly.files[str(key) + '_tendencia'])


print('Fin del proceso. Ficheros generados con éxito')