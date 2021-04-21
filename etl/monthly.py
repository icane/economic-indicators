"""Monthly indicators."""

import json

from etl.common import to_json_stat, write_to_file
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
        # España
        df_esp = data[cfg.file][cfg.series[key].sheet][[
            'Año', 'Mes', coltoshowes]].copy()
        df_esp = transform(
            df_esp, cfg.periods.global_monthly, 'España - '
        )
        df_esp.set_index('Mes', inplace=True)
        df_esp = df_esp.transpose()
        df_esp[' - Indicadores'] = cfg.series[key].label
        # merge dataframes
        df_cant = df_cant.merge(df_esp, on=' - Indicadores')
        # append to global
        indicators.append(df_cant)

df_global = pd.concat(indicators, axis=0, verify_integrity=False, sort=True)
df_global.to_csv(cfg.path.output + cfg.globals.csv, index=False)

print('\nEnd of process. Files generated successfully.')
print('\nCheck the following:')
print('\n\tFormat of the global file.')
print('\n\tReplace "Cantabria" by "Zona Oeste" in "consumo-cemento" files.')
