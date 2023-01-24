"""Annual indicators."""

import json

from etl.common import global_with_format, to_json_stat, write_to_file
from etl.config_annual import annual_cfg as cfg

from etlstat.extractor.extractor import xlsx

import pandas as pd


def transform(df, periods, prefix=''):
    """
    Slice dataframe. Generate time period column.

        df (dataframe): dataset
        periods (int): number of time periods
        prefix (str): prefix for time periods
    """
    for i in range(0, len(df)):
        period = str(df.loc[i, 'Año'])
        df.loc[i, 'period'] = prefix + period

    df.drop(columns={'Año'}, axis=1, inplace=True)
    df.rename(columns={'period': 'Año'}, inplace=True)
    df = df.tail(periods)
    df = df.round(2)
    return df


# Read  input files
data = xlsx(cfg.path.input)

# Value and trend files for each indicator
for key in cfg.series:
    print(key)
    # Drop NA rows, if any
    data[cfg.file][cfg.series[key].sheet].dropna(
        axis=0, how='all', inplace=True)

    # Rename variables
    if cfg.series[key].rate_vars == []:
        data[cfg.file][cfg.series[key].sheet].rename(
            columns={
                cfg.series[key].value_vars[0]: 'Valor Cantabria',
                cfg.series[key].value_vars[1]: 'Valor España'},
            inplace=True)
    else:
        data[cfg.file][cfg.series[key].sheet].rename(
            columns={
                cfg.series[key].value_vars[0]: 'Valor Cantabria',
                cfg.series[key].value_vars[1]: 'Valor España',
                cfg.series[key].rate_vars[0]: 'Var. interanual Cantabria',
                cfg.series[key].rate_vars[1]: 'Var. interanual España'},
            inplace=True)

    # Remove .0 from Año
    data[cfg.file][cfg.series[key].sheet]['Año'] = \
        data[cfg.file][cfg.series[key].sheet]['Año'].astype(str).replace(
            r'\.0', '', regex=True)

    # Value variables
    value_vars = cfg.series[key].value_vars
    variables = ['Año', 'Valor Cantabria', 'Valor España']
    df = data[cfg.file][
            cfg.series[key].sheet][variables].copy()
    df = transform(df, cfg.periods.annual)
    json_file = to_json_stat(
        df,
        ['Año'],
        ['Valor Cantabria', 'Valor España'],
        cfg.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        cfg.series[key].unit.value
    json_obj['note'] = cfg.series[key].note
    json_file = json.dumps(json_obj)
    write_to_file(json_file, cfg.path.output + cfg.series[key].json.value)

    # Rate and trend vars
    if cfg.series[key].rate_vars != []:
        variables = [
            'Año', 'Var. interanual Cantabria', 'Var. interanual España'
        ]
        df_trend = data[cfg.file][
            cfg.series[key].sheet
        ][variables].copy()
        df_trend = transform(
            df_trend, cfg.periods.annual)

        # Exclude series for which all values for Var. interanual Cantabria
        # are NA
        if df_trend['Var. interanual Cantabria'].isna().all():
            df_trend = df_trend[df_trend['Var. interanual Cantabria'].notna()]

        json_file = to_json_stat(
            df_trend,
            ['Año'],
            ['Var. interanual Cantabria', 'Var. interanual España'],
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
    if cfg.series[key].rate_vars != []:
        # Crea una variable para mostrar el valor del indicador
        if key in [
                'deuda_publica_pib', 'deficit_publico_pib',
                'gasto_sanitario_consolidado_pib'
        ]:
            coltoshow = 'Valor Cantabria'
            coltoshowes = 'Valor España'
        else:
            coltoshow = 'Var. interanual Cantabria'
            coltoshowes = 'Var. interanual España'
        df_cant = data[cfg.file][cfg.series[key].sheet][[
                'Año', coltoshow]].copy()
        df_cant = transform(df_cant, cfg.periods.global_annual, 'Cantabria - ')
        df_cant.set_index('Año', inplace=True)
        df_cant = df_cant.transpose()
        df_cant.insert(0, 'Categoria', cfg.series[key].category)
        df_cant[' - Indicadores'] = cfg.series[key].label
        # España
        df_esp = data[cfg.file][cfg.series[key].sheet][[
            'Año', coltoshowes]].copy()
        df_esp = transform(df_esp, cfg.periods.global_annual, 'España - ')
        df_esp.set_index('Año', inplace=True)
        df_esp = df_esp.transpose()
        df_esp[' - Indicadores'] = cfg.series[key].label
        # merge dataframes
        df_cant = df_cant.merge(df_esp, on=' - Indicadores')
        # append to global
        indicators.append(df_cant)

df_global = pd.concat(indicators, axis=0, verify_integrity=False, sort=True)
# reorder df_global before save to csv
df_global = global_with_format(df_global)
df_global.to_csv(cfg.path.output + cfg.globals.csv, index=False)

print('\nEnd of process. Files generated successfully.')
