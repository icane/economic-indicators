"""Common methods."""

from pyjstat import pyjstat
import re


def to_json_stat(df, id_vars, value_vars, source):
    """
    Export dataframe to JSON-Stat dataset.

    df (dataframe): dataset
    id_vars (list): index columns
    value_vars (list): numeric variables (metrics)
    source (str): metadata
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


def write_to_file(str_data, file_name):
    """Write a string variable to disk file."""
    file = open(file_name, 'w')
    str_data = re.sub("updated.*source\"", "updated\": null, \"source\"", str_data)
    file.write(str_data)
    file.close()


def global_with_format(full_df):
    """
    Format global view df.

    Omit unwanted columns (old periods), retain 5 latest periods and reorder.

        full_df (dataframe): global dataframe to reformat
    """
    col_list = list(full_df.columns)
    pivot_idx = col_list.index('Categoria')

    # rearrange column names in the desired order
    ordcol = (
        col_list[pivot_idx:pivot_idx+1] + col_list[pivot_idx-5:pivot_idx]
        + col_list[0:1] + col_list[-5:]
    )

    full_df = full_df[ordcol]

    return full_df
