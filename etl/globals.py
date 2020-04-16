"""Generation of global datasets (JSON-Stat and CSV)."""

from config import etl_cfg

from etlstat.extractor.extractor import xlsx

from numpy import arange

import pandas as pd

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
qdata = pd.DataFrame()
qframes = []
for key in etl_cfg.quarterly.series:
    # Remove unused variables
    data[etl_cfg.quarterly.file]\
        [etl_cfg.quarterly.series[key].sheet].drop(
            columns=etl_cfg.quarterly.series[key].value_vars,
            axis=1,
            inplace=True
        )
    data[etl_cfg.quarterly.file]\
        [etl_cfg.quarterly.series[key].sheet].drop(
            columns=etl_cfg.quarterly.series[key].trend_vars,
            axis=1,
            inplace=True
        )
    
    # Last periods
    data[etl_cfg.quarterly.file][etl_cfg.quarterly.series[key].sheet] = \
        data[etl_cfg.quarterly.file][etl_cfg.quarterly.series[key].sheet].tail(
            etl_cfg.periods.globals)

    qframes.append(data[etl_cfg.quarterly.file][etl_cfg.quarterly.series[key].sheet])

qdata = pd.concat(qframes, axis=1)

print(qdata)


"""Monthly series."""
mdata = pd.DataFrame()
mframes = []
for key in etl_cfg.monthly.series:
    # Remove unused variables
    data[etl_cfg.monthly.file]\
        [etl_cfg.monthly.series[key].sheet].drop(
            columns=etl_cfg.monthly.series[key].value_vars,
            axis=1,
            inplace=True
        )
    data[etl_cfg.monthly.file]\
        [etl_cfg.monthly.series[key].sheet].drop(
            columns=etl_cfg.monthly.series[key].trend_vars,
            axis=1,
            inplace=True
        )

    # Last periods
    data[etl_cfg.monthly.file][etl_cfg.monthly.series[key].sheet] = \
        data[etl_cfg.monthly.file][etl_cfg.monthly.series[key].sheet].tail(
            etl_cfg.periods.globals)

    mframes.append(data[etl_cfg.monthly.file][etl_cfg.monthly.series[key].sheet])

mdata = pd.concat(mframes, axis=1)

print(mdata)

print('\nEnd of process. Files generated successfully.')