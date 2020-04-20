"""Quarterly indicators."""

from etl.common import to_json_stat, write_to_file

from etl.config_quarterly import quarterly_cfg as cfg

from etlstat.extractor.extractor import xlsx

import json


def transform(df, periods):
    """Slice dataframe. Generate time period column.
    
        df (dataframe): dataset
        periods (int): number of time periods
    """
    df = df.tail(periods)
    df.reset_index(inplace=True)

    for i in range(0, len(df)):
        period1 = str(df.loc[i, 'Año'])
        period2 = str(df.loc[i, 'Trimestre'])
        df.loc[i, 'period'] =  period1 + ' - ' + period2

    df.drop(columns={'Año', 'Trimestre'}, axis=1, inplace=True)
    df.rename(columns={'period': 'Trimestre'}, inplace=True)
    return df


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
    json_file = json.dumps(json_obj)
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
    json_file = json.dumps(json_obj)
    write_to_file(json_file, cfg.path.output + cfg.series[key].json.trend)

print('\nEnd of process. Files generated successfully.')
