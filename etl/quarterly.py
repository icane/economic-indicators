"""Quarterly indicators."""

from etl.common import to_json_stat, write_to_file

from etl.config_quarterly import quarterly_cfg as cfg

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
        period2 = str(df.loc[i, 'Trimestre'])
        df.loc[i, 'period'] =  period1 + '-' + period2

    df.drop(columns={'Año', 'Trimestre'}, axis=1, inplace=True)
    df.rename(columns={'period': 'Trimestre'}, inplace=True)
    df = df.tail(periods)
    df = df.round(2)
    return df

def replace_quarter(json_str):
    """Replace quarter number by its label."""
    json_str = json_str.replace('-1"', '-1T"')
    json_str = json_str.replace('-2"', '-2T"')
    json_str = json_str.replace('-3"', '-3T"')
    json_str = json_str.replace('-4"', '-4T"')
    return json_str

# Read  input files
data = xlsx(cfg.path.input)

for key in cfg.series:
    # Value variables
    value_vars = cfg.series[key].value_vars
    variables = ['Año', 'Trimestre']
    variables.extend(value_vars)
    df = data[cfg.file]\
        [cfg.series[key].sheet][variables].copy()
    df = transform(df, cfg.periods.quarterly)
    json_file = to_json_stat(
        df,
        ['Trimestre'],
        value_vars,
        cfg.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        cfg.series[key].unit.value
    json_obj['note'] = cfg.series[key].note
    json_file = json.dumps(json_obj)
    json_file = replace_quarter(json_file)
    write_to_file(json_file, cfg.path.output + cfg.series[key].json.value)

    # Rate and trend vars
    rate_vars = cfg.series[key].rate_vars
    trend_vars = cfg.series[key].trend_vars
    variables = ['Año', 'Trimestre']
    variables.extend(rate_vars)
    variables.extend(trend_vars)
    df_trend = data[cfg.file]\
        [cfg.series[key].sheet][variables].copy()
    df_trend = transform(
        df_trend, cfg.periods.quarterly)
    variables = rate_vars
    variables.extend(trend_vars)
    json_file = to_json_stat(
        df_trend,
        ['Trimestre'],
        variables,
        cfg.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        cfg.series[key].unit.trend
    json_obj['note'] = cfg.series[key].note
    json_file = json.dumps(json_obj)
    json_file = replace_quarter(json_file)
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

# JSON-Stat dataset
variables = list(gdata.columns.values).remove('Trimestre')
json_file = to_json_stat(
        gdata,
        ['Trimestre'],
        variables,
        cfg.globals.source)
json_obj = json.loads(json_file)
json_file = json.dumps(json_obj)
json_file = replace_quarter(json_file)
write_to_file(json_file, cfg.path.output + cfg.globals.json)

# CSV dataset
indicators = []
for key in cfg.series:
    cant = gdata[['Trimestre', cfg.series[key].rate_vars[0]]].copy()
    cant.set_index('Trimestre', inplace=True)
    cant.rename(
        columns={cfg.series[key].rate_vars[0]:
                cfg.series[key].label},
                inplace=True)
    cant = cant.transpose()
    esp = gdata[['Trimestre', cfg.series[key].rate_vars[1]]].copy()
    esp.set_index('Trimestre', inplace=True)
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
