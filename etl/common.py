"""Common methods."""

from pyjstat import pyjstat


def to_json_stat(df, id_vars, value_vars, source):
    """Export dataframe to JSON-Stat dataset.
    
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
    file.write(str_data)
    file.close()