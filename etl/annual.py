"""Annual indicators."""

from etl.common import to_json_stat, write_to_file

from etl.config_annual import annual_cfg as cfg

from etlstat.extractor.extractor import xlsx

import json

import pandas as pd


def transform(df, periods, prefix=''):
    """Slice dataframe. Generate time period column.
    
        df (dataframe): dataset
        periods (int): number of time periods
        prefix (str): prefix for time periods
    """
    for i in range(0, len(df)):
        period = str(df.loc[i, 'Año'])
        df.loc[i, 'period'] =  prefix + period

    df.drop(columns={'Año'}, axis=1, inplace=True)
    df.rename(columns={'period': 'Año'}, inplace=True)
    df = df.tail(periods)
    df = df.round(2)
    return df


# Read  input files
data = xlsx(cfg.path.input)

# Value and trend files for each indicator
for key in cfg.series:
    # Drop NA rows, if any
    data[cfg.file][cfg.series[key].sheet].dropna(
        axis=0, how='all', inplace=True)

    # Value variables
    value_vars = cfg.series[key].value_vars
    variables = ['Año']
    variables.extend(value_vars)
    df = data[cfg.file]\
        [cfg.series[key].sheet][variables].copy()
    df = transform(df, cfg.periods.annual)
    json_file = to_json_stat(
        df,
        ['Año'],
        value_vars,
        cfg.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        cfg.series[key].unit.value
    json_obj['note'] = cfg.series[key].note
    json_file = json.dumps(json_obj)
    write_to_file(json_file, cfg.path.output + cfg.series[key].json.value)

    # Rate and trend vars
    rate_vars = cfg.series[key].rate_vars
    trend_vars = cfg.series[key].trend_vars
    variables = ['Año']
    variables.extend(rate_vars)
    variables.extend(trend_vars)
    df_trend = data[cfg.file]\
        [cfg.series[key].sheet][variables].copy()
    df_trend = transform(
        df_trend, cfg.periods.annual)
    variables = rate_vars
    variables.extend(trend_vars)
    json_file = to_json_stat(
        df_trend,
        ['Año'],
        variables,
        cfg.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        cfg.series[key].unit.trend
    json_obj['note'] = cfg.series[key].note
    json_file = json.dumps(json_obj)
    write_to_file(json_file, cfg.path.output + cfg.series[key].json.trend)

# Global dataset
df_global = pd.DataFrame()
indicators = []
for key in cfg.series:
    # Cantabria
    df_cant = data[cfg.file][cfg.series[key].sheet][[
        'Año', cfg.series[key].rate_vars[0]]].copy()
    df_cant = transform(df_cant, cfg.periods.global_annual, 'Cantabria - ')
    df_cant.set_index('Año', inplace=True)
    df_cant = df_cant.transpose()
    df_cant.insert(0, 'Categoria', cfg.series[key].category)
    df_cant[' - Indicadores'] = cfg.series[key].label
    # España
    df_esp = data[cfg.file][cfg.series[key].sheet][[
        'Año', cfg.series[key].rate_vars[1]]].copy()
    df_esp = transform(df_esp, cfg.periods.global_annual, 'España - ')
    df_esp.set_index('Año', inplace=True)
    df_esp = df_esp.transpose()
    df_esp[' - Indicadores'] = cfg.series[key].label
    # merge dataframes
    df_cant = df_cant.merge(df_esp, on=' - Indicadores')
    # append to global
    indicators.append(df_cant)

df_global = pd.concat(indicators, axis=0, verify_integrity=False)
df_global.to_csv(cfg.path.output + cfg.globals.csv, index=False)

print('\nEnd of process. Files generated successfully.')