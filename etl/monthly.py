"""Monthly indicators."""

from etl.common import to_json_stat, write_to_file

from etl.config_monthly import monthly_cfg as cfg

from etlstat.extractor.extractor import xlsx

import json

import pandas as pd


def transform(df, periods):
    """Slice dataframe. Generate time period column.
    
        df (dataframe): dataset
        periods (int): number of time periods
    """
    df = df.tail(periods)
    df.reset_index(inplace=True)

    for i in range(0, len(df)):
        period1 = str(df.loc[i, 'Año'])
        period2 = str(df.loc[i, 'Mes'])
        df.loc[i, 'period'] =  period1 + ' - ' + period2

    df.drop(columns={'Año', 'Mes'}, axis=1, inplace=True)
    df.rename(columns={'period': 'Mes'}, inplace=True)
    return df

def replace_month(json_str):
    """Replace month number by its name."""
    json_str = json_str.replace(' - 1"', ' - Enero"')
    json_str = json_str.replace(' - 2"', ' - Febrero"')
    json_str = json_str.replace(' - 3"', ' - Marzo"')
    json_str = json_str.replace(' - 4"', ' - Abril"')
    json_str = json_str.replace(' - 5"', ' - Mayo"')
    json_str = json_str.replace(' - 6"', ' - Junio"')
    json_str = json_str.replace(' - 7"', ' - Julio"')
    json_str = json_str.replace(' - 8"', ' - Agosto"')
    json_str = json_str.replace(' - 9"', ' - Septiembre"')
    json_str = json_str.replace(' - 10"', ' - Octubre"')
    json_str = json_str.replace(' - 11"', ' - Noviembre"')
    json_str = json_str.replace(' - 12"', ' - Diciembre"')
    return json_str

# Read  input files
data = xlsx(cfg.path.input)

for key in cfg.series:
    # Value variables
    value_vars = cfg.series[key].value_vars
    variables = ['Año', 'Mes']
    variables.extend(value_vars)
    df = data[cfg.file]\
        [cfg.series[key].sheet][variables].copy()
    df = transform(df, cfg.periods.monthly)
    json_file = to_json_stat(
        df,
        ['Mes'],
        value_vars,
        cfg.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        cfg.series[key].unit.value
    json_file = json.dumps(json_obj)
    json_file = replace_month(json_file)
    write_to_file(json_file, cfg.path.output + cfg.series[key].json.value)

    # Rate and trend vars
    rate_vars = cfg.series[key].rate_vars
    trend_vars = cfg.series[key].trend_vars
    variables = ['Año', 'Mes']
    variables.extend(rate_vars)
    variables.extend(trend_vars)
    df_trend = data[cfg.file]\
        [cfg.series[key].sheet][variables].copy()
    df_trend = transform(
        df_trend, cfg.periods.monthly)
    variables = rate_vars
    variables.extend(trend_vars)
    json_file = to_json_stat(
        df_trend,
        ['Mes'],
        variables,
        cfg.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        cfg.series[key].unit.trend
    json_file = json.dumps(json_obj)
    json_file = replace_month(json_file)
    write_to_file(json_file, cfg.path.output + cfg.series[key].json.trend)

# Global dataset
gdata = pd.DataFrame()
qframes = []
for key in cfg.series:
    # Remove unused variables
    data[cfg.file][cfg.series[key].sheet].drop(
            columns=cfg.series[key].value_vars,
            axis=1,
            inplace=True)
    data[cfg.file][cfg.series[key].sheet].drop(
            columns=cfg.series[key].trend_vars,
            axis=1,
            inplace=True)
    
    qframes.append(data[cfg.file][cfg.series[key].sheet])

# Join dataframes and remove duplicate columns
gdata = pd.concat(qframes, axis=1, verify_integrity=False)
gdata = gdata.loc[:,~gdata.columns.duplicated()]

# Change time dimension
gdata = transform(gdata, cfg.periods.globals)

# Export JSON-Stat dataset
variables = list(gdata.columns.values).remove('Mes')
json_file = to_json_stat(
        gdata,
        ['Mes'],
        variables,
        cfg.globals.source)
json_obj = json.loads(json_file)
json_obj['dimension']['Variables']['category']['unit'] = \
    cfg.series[key].unit.value
json_file = json.dumps(json_obj)
json_file = replace_month(json_file)
write_to_file(json_file, cfg.path.output + cfg.globals.json)

print('\nEnd of process. Files generated successfully.')
