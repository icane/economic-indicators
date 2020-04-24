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
    for i in range(0, len(df)):
        period1 = str(df.loc[i, 'Año'])
        period2 = '{:0>2}'.format(df.loc[i, 'Mes'])
        df.loc[i, 'period'] =  period1 + '-' + period2

    df.drop(columns={'Año', 'Mes'}, axis=1, inplace=True)
    df.rename(columns={'period': 'Mes'}, inplace=True)
    df = df.tail(periods)
    df = df.round(2)
    return df

def replace_month(json_str):
    """Replace month number by its name."""
    json_str = json_str.replace('-01"', '-Ene"')
    json_str = json_str.replace('-02"', '-Feb"')
    json_str = json_str.replace('-03"', '-Mar"')
    json_str = json_str.replace('-04"', '-Abr"')
    json_str = json_str.replace('-05"', '-May"')
    json_str = json_str.replace('-06"', '-Jun"')
    json_str = json_str.replace('-07"', '-Jul"')
    json_str = json_str.replace('-08"', '-Ago"')
    json_str = json_str.replace('-09"', '-Sep"')
    json_str = json_str.replace('-10"', '-Oct"')
    json_str = json_str.replace('-11"', '-Nov"')
    json_str = json_str.replace('-12"', '-Dic"')
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
    json_obj['note'] = cfg.series[key].note
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
    json_obj['note'] = cfg.series[key].note
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
json_file = json.dumps(json_obj)
json_file = replace_month(json_file)
write_to_file(json_file, cfg.path.output + cfg.globals.json)

# CSV dataset
indicators = []
for key in cfg.series:
    cant = gdata[['Mes', cfg.series[key].rate_vars[0]]].copy()
    cant.set_index('Mes', inplace=True)
    cant.rename(
        columns={cfg.series[key].rate_vars[0]:
                cfg.series[key].label},
                inplace=True)
    cant = cant.transpose()
    esp = gdata[['Mes', cfg.series[key].rate_vars[1]]].copy()
    esp.set_index('Mes', inplace=True)
    esp.rename(
        columns={cfg.series[key].rate_vars[1]:
                cfg.series[key].label},
                inplace=True)
    esp = esp.transpose()
    indicator = pd.concat([cant, esp], axis=1)
    indicators.append(indicator)

global_table = pd.concat(indicators, axis=0, verify_integrity=False)

global_table.to_csv(cfg.path.output + cfg.globals.csv)

print('\nEnd of process. Files generated successfully.')
