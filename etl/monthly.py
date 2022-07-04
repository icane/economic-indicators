"""Monthly indicators."""

import json
import re

from etl.common import global_with_format, to_json_stat, write_to_file
from etl.config_monthly import monthly_cfg as cfg

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
        period2 = '{:0>2}'.format(df.loc[i, 'Mes'])
        df.loc[i, 'period'] = prefix + period1 + '-' + period2

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


def zona_oeste_rplc(file):
    """Replace 'Cantabria' by 'Zona Oeste' in text file."""
    f = open(file, 'r+')
    text = f.read()
    # Replace
    text = re.sub(r'Cantabria"', r'Zona Oeste"', text)
    # Go to top of file and clear content
    f.seek(0)
    f.truncate()
    # re-write file and close
    f.write(text)
    f.close()


def round_avoiding_errors(value, decimals):
    try:
        _ = round(value, decimals)
        return _
    except:
        return value


# Read  input files
data = xlsx(cfg.path.input)

# Value and trend files for each indicator
for key in cfg.series:

    # Drop NA rows, if any
    data[cfg.file][cfg.series[key].sheet].dropna(
        axis=0, how='all', inplace=True)

    # Rename variables

    if key not in ['empresas_afectadas_erte',
                   'afiliados_afectados_erte']:
        if cfg.series[key].trend_vars == []:
            data[cfg.file][cfg.series[key].sheet].rename(
                columns={
                    cfg.series[key].value_vars[0]: 'Valor Cantabria',
                    cfg.series[key].value_vars[1]: 'Valor España',
                    cfg.series[key].rate_vars[0]: 'Var. interanual Cantabria',
                    cfg.series[key].rate_vars[1]: 'Var. interanual España'},
                inplace=True)
        else:
            data[cfg.file][cfg.series[key].sheet].rename(
                columns={
                    cfg.series[key].value_vars[0]: 'Valor Cantabria',
                    cfg.series[key].value_vars[1]: 'Valor España',
                    cfg.series[key].rate_vars[0]: 'Var. interanual Cantabria',
                    cfg.series[key].rate_vars[1]: 'Var. interanual España',
                    cfg.series[key].trend_vars[0]: 'Tendencia Cantabria',
                    cfg.series[key].trend_vars[1]: 'Tendencia España'},
                inplace=True)
    else:
        data[cfg.file][cfg.series[key].sheet].rename(
                columns={
                    cfg.series[key].value_vars[0]: 'Valor Cantabria',
                    cfg.series[key].value_vars[1]: 'Valor España',
                    cfg.series[key].rate_vars[0]: 'Cantabria',
                    cfg.series[key].rate_vars[1]: 'España'},
                inplace=True)
    # Remove .0 from Año and Mes
    data[cfg.file][cfg.series[key].sheet]['Año'] = data[
        cfg.file][cfg.series[key].sheet]['Año'].astype(str).replace(
            r'\.0', '', regex=True
        )
    data[cfg.file][cfg.series[key].sheet]['Mes'] = data[
        cfg.file][cfg.series[key].sheet]['Mes'].astype(str).replace(
            r'\.0', '', regex=True
        )

    # Value variables
    variables = ['Año', 'Mes', 'Valor Cantabria', 'Valor España']
    df = data[cfg.file][
        cfg.series[key].sheet][variables].copy()
    df = transform(df, cfg.periods.monthly)
    json_file = to_json_stat(
        df,
        ['Mes'],
        ['Valor Cantabria', 'Valor España'],
        cfg.series[key].source)
    json_obj = json.loads(json_file)
    json_obj['dimension']['Variables']['category']['unit'] = \
        cfg.series[key].unit.value
    json_obj['note'] = cfg.series[key].note
    json_file = json.dumps(json_obj)
    json_file = replace_month(json_file)
    write_to_file(json_file, cfg.path.output + cfg.series[key].json.value)

    # Rate and trend vars
    if key not in ['empresas_afectadas_erte',
                   'afiliados_afectados_erte']:
        if cfg.series[key].trend_vars == []:
            variables = [
                'Año', 'Mes', 'Var. interanual Cantabria',
                'Var. interanual España'
            ]
        else:
            variables = [
                'Año', 'Mes', 'Var. interanual Cantabria',
                'Var. interanual España', 'Tendencia Cantabria',
                'Tendencia España']
    else:
        variables = [
                'Año', 'Mes', 'Cantabria', 'España']
    df_trend = data[cfg.file][
        cfg.series[key].sheet][variables].copy()
    df_trend = transform(
        df_trend, cfg.periods.monthly)
    variables.remove('Año')
    variables.remove('Mes')

    # Apply decimals from config file depeding on the column
    if 'Cantabria' in df_trend:
        decimals = cfg.series[key].unit.trend.Cantabria.decimals
        df_trend['Cantabria'] = df_trend['Cantabria'].apply(
            lambda x: round_avoiding_errors(x, decimals))

    if 'España' in df_trend:
        decimals = cfg.series[key].unit.trend.España.decimals
        df_trend['España'] = df_trend['España'].apply(
            lambda x: round_avoiding_errors(x, decimals))
    
    if 'Var. interanual Cantabria' in df_trend:
        decimals = cfg.series[key].unit.trend['Var. interanual Cantabria'].decimals
        df_trend['Var. interanual Cantabria'] = df_trend[
            'Var. interanual Cantabria'].apply(
            lambda x: round_avoiding_errors(x, decimals))

    if 'Var. interanual España' in df_trend:
        decimals = cfg.series[key].unit.trend['Var. interanual España'].decimals
        df_trend['Var. interanual España'] = df_trend[
            'Var. interanual España'].apply(
            lambda x: round_avoiding_errors(x, decimals))

    if 'Tendencia Cantabria' in df_trend:
        decimals = cfg.series[key].unit.trend['Tendencia Cantabria'].decimals
        df_trend['Tendencia Cantabria'] = df_trend['Tendencia Cantabria'].apply(
            lambda x: round_avoiding_errors(x, decimals))

    if 'Tendencia España' in df_trend:
        decimals = cfg.series[key].unit.trend['Tendencia España'].decimals
        df_trend['Tendencia España'] = df_trend['Tendencia España'].apply(
            lambda x: round_avoiding_errors(x, decimals))

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
df_global = pd.DataFrame()
indicators = []
for key in cfg.series:
    if cfg.series[key].rate_vars != []:  # if there is a variation to show
        if key in ['empresas_afectadas_erte', 'afiliados_afectados_erte']:
            coltoshow = 'Cantabria'
            coltoshowes = 'España'
        else:
            coltoshow = 'Var. interanual Cantabria'
            coltoshowes = 'Var. interanual España'
        # Cantabria
        df_cant = data[cfg.file][cfg.series[key].sheet][[
            'Año', 'Mes', coltoshow]].copy()
        df_cant = transform(
            df_cant, cfg.periods.global_monthly, 'Cantabria - '
        )
        df_cant.set_index('Mes', inplace=True)
        df_cant = df_cant.transpose()
        df_cant.insert(0, 'Categoria', cfg.series[key].category)
        df_cant[' - Indicadores'] = cfg.series[key].label

        # (Cantabria) Round to 2 decimals for all columns less first and last
        for column in df_cant.columns[1:-1]:
            df_cant[column] = df_cant[column].apply(
                lambda x: round_avoiding_errors(x,2))

        # España
        df_esp = data[cfg.file][cfg.series[key].sheet][[
            'Año', 'Mes', coltoshowes]].copy()
        df_esp = transform(
            df_esp, cfg.periods.global_monthly, 'España - '
        )
        df_esp.set_index('Mes', inplace=True)
        df_esp = df_esp.transpose()
        df_esp[' - Indicadores'] = cfg.series[key].label

        # (España) Round to 2 decimals for all columns 
        for column in df_esp.columns:
            df_esp[column] = df_esp[column].apply(
                lambda x: round_avoiding_errors(x,2))

        # merge dataframes
        df_cant = df_cant.merge(df_esp, on=' - Indicadores')
        # append to global
        indicators.append(df_cant)

df_global = pd.concat(indicators, axis=0, verify_integrity=False, sort=True)
# reorder df_global before save to csv
df_global = global_with_format(df_global)
df_global.to_csv(cfg.path.output + cfg.globals.csv, index=False)

# Replace 'Cantabria' by 'Zona Oeste' in json-stat.
zona_oeste_rplc(cfg.path.output + "consumo-cemento.json-stat")
zona_oeste_rplc(cfg.path.output + "consumo-cemento-tendencia.json-stat")


print('\nEnd of process. Files generated successfully.')
