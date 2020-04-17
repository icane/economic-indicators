"""Generation of JSON-Stat datasets for indicators."""

from config import etl_cfg

from etlstat.extractor.extractor import xlsx

import json

from numpy import arange

from pyjstat import pyjstat


def transform(df, time_columns, labels, periods):
    """Slice dataframe. Generate time period column.
    
        df (dataframe): dataset
        time_columns (list): [year_column, month|quarter_column]
        labels (dict): time period labels
        periods (int): number of time periods
    """
    df = df.tail(periods)
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
data = xlsx(etl_cfg.path.input)

"""Quarterly series."""
for key in etl_cfg.quarterly.series:
    # Value variables
    value_vars = etl_cfg.quarterly.series[key].value_vars
    variables = ['Año', 'Trimestre']
    variables.extend(value_vars)
    df = data[etl_cfg.quarterly.file]\
        [etl_cfg.quarterly.series[key].sheet][variables].copy()
    df = transform(
        df, ['Año', 'Trimestre'],
        etl_cfg.value_labels.quarter, etl_cfg.periods.quarterly)
    json_file = to_json(
        df,
        ['Trimestre'],
        value_vars,
        etl_cfg.quarterly.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        etl_cfg.quarterly.series[key].unit.value
    json_file = json.dumps(json_obj)
    write_to_file(json_file, etl_cfg.path.output + etl_cfg.quarterly.series[key].json.value)

    # Rate and trend vars
    rate_vars = etl_cfg.quarterly.series[key].rate_vars
    trend_vars = etl_cfg.quarterly.series[key].trend_vars
    variables = ['Año', 'Trimestre']
    variables.extend(rate_vars)
    variables.extend(trend_vars)
    df_trend = data[etl_cfg.quarterly.file]\
        [etl_cfg.quarterly.series[key].sheet][variables].copy()
    df_trend = transform(
        df_trend, ['Año', 'Trimestre'],
        etl_cfg.value_labels.quarter, etl_cfg.periods.quarterly)
    variables = rate_vars
    variables.extend(trend_vars)
    json_file = to_json(
        df_trend,
        ['Trimestre'],
        variables,
        etl_cfg.quarterly.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        etl_cfg.quarterly.series[key].unit.trend
    json_file = json.dumps(json_obj)
    write_to_file(json_file, etl_cfg.path.output + etl_cfg.quarterly.series[key].json.trend)

"""Monthly series."""
for key in etl_cfg.monthly.series:
    # Value variables
    value_vars = etl_cfg.monthly.series[key].value_vars
    variables = ['Año', 'Mes']
    variables.extend(value_vars)
    df = data[etl_cfg.monthly.file]\
        [etl_cfg.monthly.series[key].sheet][variables].copy()
    df = transform(
        df, ['Año', 'Mes'],
        etl_cfg.value_labels.month, etl_cfg.periods.monthly)
    json_file = to_json(
        df,
        ['Mes'],
        value_vars,
        etl_cfg.monthly.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        etl_cfg.monthly.series[key].unit.value
    json_file = json.dumps(json_obj)
    write_to_file(json_file, etl_cfg.path.output + etl_cfg.monthly.series[key].json.value)

    # Rate and trend vars
    rate_vars = etl_cfg.monthly.series[key].rate_vars
    trend_vars = etl_cfg.monthly.series[key].trend_vars
    variables = ['Año', 'Mes']
    variables.extend(rate_vars)
    variables.extend(trend_vars)
    df_trend = data[etl_cfg.monthly.file]\
        [etl_cfg.monthly.series[key].sheet][variables].copy()
    df_trend = transform(
        df_trend, ['Año', 'Mes'],
        etl_cfg.value_labels.month, etl_cfg.periods.monthly)
    variables = rate_vars
    variables.extend(trend_vars)
    json_file = to_json(
        df_trend,
        ['Mes'],
        variables,
        etl_cfg.monthly.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        etl_cfg.monthly.series[key].unit.trend
    json_file = json.dumps(json_obj)
    write_to_file(json_file, etl_cfg.path.output + etl_cfg.monthly.series[key].json.trend)

print('\nEnd of process. Files generated successfully.')