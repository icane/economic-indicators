"""Quarterly indicators."""

import json

from etl.common import global_with_format, to_json_stat, write_to_file
from etl.config_quarterly import quarterly_cfg as cfg

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
        period1 = str(df.loc[i, 'Año'])
        period2 = str(df.loc[i, 'Trimestre'])
        df.loc[i, 'period'] = prefix + period1 + '-' + period2

    df.drop(columns={'Año', 'Trimestre'}, axis=1, inplace=True)
    df.rename(columns={'period': 'Trimestre'}, inplace=True)
    # df = df.tail(periods)
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

# Value and trend files for each indicator
for key in cfg.series:
    print(key)
    # Drop NA rows, if any
    data[cfg.file][cfg.series[key].sheet].dropna(
        axis=0, how='all', inplace=True)

    # Rename variables
    data[cfg.file][cfg.series[key].sheet].rename(
        columns={
            cfg.series[key].value_vars[0]: 'Valor Cantabria',
            cfg.series[key].value_vars[1]: 'Valor España'},
        inplace=True)
    if cfg.series[key].rate_vars != []:
        data[cfg.file][cfg.series[key].sheet].rename(
            columns={
                cfg.series[key].rate_vars[0]: 'Var. interanual Cantabria',
                cfg.series[key].rate_vars[1]: 'Var. interanual España'},
            inplace=True)
    if cfg.series[key].trend_vars != []:
        data[cfg.file][cfg.series[key].sheet].rename(
            columns={
                cfg.series[key].trend_vars[0]: 'Tendencia Cantabria',
                cfg.series[key].trend_vars[1]: 'Tendencia España'},
            inplace=True)

    # Remove .0 from Año and Trimestre
    data[cfg.file][cfg.series[key].sheet]['Año'] = \
        data[cfg.file][cfg.series[key].sheet]['Año'].astype(str).replace(
            r'\.0', '', regex=True)
    data[cfg.file][cfg.series[key].sheet]['Trimestre'] = \
        data[cfg.file][cfg.series[key].sheet]['Trimestre'].astype(str).replace(
            r'\.0', '', regex=True)

    # Value variables
    variables = ['Año', 'Trimestre', 'Valor Cantabria', 'Valor España']
    df = data[cfg.file][
        cfg.series[key].sheet][variables].copy()
    df = transform(df, cfg.periods.quarterly)
    json_file = to_json_stat(
        df,
        ['Trimestre'],
        ['Valor Cantabria', 'Valor España'],
        cfg.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        cfg.series[key].unit.value
    json_obj['note'] = cfg.series[key].note
    json_file = json.dumps(json_obj)
    json_file = replace_quarter(json_file)
    write_to_file(json_file, cfg.path.output + cfg.series[key].json.value)

    # Rate and trend vars
    if cfg.series[key].rate_vars != []:
        if cfg.series[key].trend_vars == []:
            variables = [
                'Año', 'Trimestre', 'Var. interanual Cantabria',
                'Var. interanual España']
        else:
            variables = [
                'Año', 'Trimestre', 'Var. interanual Cantabria',
                'Var. interanual España', 'Tendencia Cantabria',
                'Tendencia España']
        df_trend = data[cfg.file][
            cfg.series[key].sheet][variables].copy()
        df_trend = transform(
            df_trend, cfg.periods.quarterly)
        variables.remove('Año')
        variables.remove('Trimestre')
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
df_global = pd.DataFrame()
indicators = []
for key in cfg.series:
    if cfg.series[key].rate_vars != []:
        # Crea dos nuevas variables para mostrar el valor del indicador
        if key in ['deuda_publica_ccaa_pib', 'balanza_comercial']:
            coltoshow = 'Valor Cantabria'
            coltoshowes = 'Valor España'
        else:
            coltoshow = 'Var. interanual Cantabria'
            coltoshowes = 'Var. interanual España'
        # Cantabria
        df_cant = data[cfg.file][cfg.series[key].sheet][[
            'Año', 'Trimestre', coltoshow]].copy()
        df_cant = transform(
            df_cant, cfg.periods.global_quarterly, 'Cantabria - ')
        df_cant.set_index('Trimestre', inplace=True)
        df_cant = df_cant.transpose()
        df_cant.insert(0, 'Categoria', cfg.series[key].category)
        df_cant[' - Indicadores'] = cfg.series[key].label
        # España
        df_esp = data[cfg.file][cfg.series[key].sheet][[
            'Año', 'Trimestre', coltoshowes]].copy()
        df_esp = transform(df_esp, cfg.periods.global_quarterly, 'España - ')
        df_esp.set_index('Trimestre', inplace=True)
        df_esp = df_esp.transpose()
        df_esp[' - Indicadores'] = cfg.series[key].label
        # merge dataframes
        df_cant = df_cant.merge(df_esp, on=' - Indicadores')
        # append to global
        indicators.append(df_cant)

print('\nEnd of process. Files generated successfully.')
