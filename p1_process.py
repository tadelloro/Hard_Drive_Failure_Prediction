
import numpy as np
import pandas as pd
import os
import argparse
import glob
import ast
import argparse
import dask
import dask.dataframe as dd


def dtypes_mkr(columns):
    dtypes = {}
    dtypes['date'] = 'object'
    dtypes['serial_number'] = 'string'
    dtypes['model'] = 'string'
    if 'capacity_bytes' in columns: dtypes['capacity_bytes'] = 'float' 
    dtypes['failure'] = 'int'
    dtypes.update({smart:'float' for smart in [c for c in columns if 'smart' in c]})
    return dtypes

def cols_dtypes(file):
    with open(file, 'r') as f:
        cols = ast.literal_eval(f.read())
        #cols = [c for c in cols if 'normalized' not in c]
    dtypes = dtypes_mkr(cols)
    return cols, dtypes
    
def p1_proc(model_number):
    """
    Process raw data, deduplicate, clean data, and write to disk.
    
    Returns: 
        writes to disk.
    """
    print(f'Running p1 process for hard drive model: {model_number}')
    if not os.path.isdir('data/p1_proc/'):
        os.system('mkdir data/p1_proc/')
        
    cols_r, dtypes_r = cols_dtypes('columns_raw.txt')
    cols_s, dtypes_s = cols_dtypes('columns_select.txt')   

    filedct = {qqyy:glob.glob(os.getcwd() + f'/data/p0_raw/{qqyy}/*.csv') for qqyy in next(os.walk(os.getcwd() + '/data/p0_raw'))[1]}
    qqyy_list = list(filedct.keys())
    qqyy_list.sort()
    
    @dask.delayed
    def proc_csv(filepath, columns, dtypes):
        df = pd.read_csv(filepath, dtype=dtypes)
        df = df.reindex(columns=columns, )
        df = df.dropna(how='any', )
        return df

    df_list = []
    for qqyy in qqyy_list:
        
        yr = int('20'+qqyy[-2:])
        qtr = int(qqyy[0])
        filelist = filedct[qqyy]
        
        ddf = dd.from_delayed([proc_csv(filepath=f, columns=cols_s, dtypes=dtypes_r) for f in filelist], meta=dtypes_s)
        ddf['date'] = dd.to_datetime(ddf['date'])
        ddf = ddf.loc[ddf['model'] == model_number]
        ddf = ddf.loc[ddf.date.dt.year == yr]
        ddf = ddf.loc[ddf.date.dt.quarter == qtr]
        ddf['smart_9_raw'] = ddf['smart_9_raw'] / 24 # convert hours to days
        ddf = ddf.drop_duplicates(subset=['model', 'serial_number', 'date'])
        df_list.append(ddf)
    
    ddf = dd.concat(df_list, axis=0)
    
    def failure_category(days):
        if days > 30: category = 3
        elif (days <= 30) and (days > 15): category = 2
        elif (days <= 15) and (days > 5): category = 1
        else: # implied (days <=5) and (days >= 0)
            category = 0
        return category
    
    ddf = dd.merge(ddf, 
                   ddf.loc[ddf['failure'] == 1][['serial_number', 'date']].rename(columns={'date':'failure_date'}),
                   on=['serial_number'],
                   how='left',
                  )

    ddf['time_to_failure'] = ddf['failure_date'] - ddf['date']
    ddf['time_to_failure'] = ddf['time_to_failure'].dt.days.replace(np.nan, 99999)
    ddf = ddf.loc[ddf['time_to_failure'] >= 0]
    ddf['category'] = ddf['time_to_failure'].apply(failure_category, meta=('time_to_failure', 'int64'))
    
    ddf.to_csv(os.getcwd() + f'/data/p1_proc/p1_*.csv', index=False)
    print(f'Completed p1 processing for {model_number}.')
    
    
def parse_arguments():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model_number', 
                        type=str, 
                        required=True, 
                        help='Hard drive model number to select for processing.',
                       )

    args = parser.parse_args()
    return args

def main():
    
    args = parse_arguments()
    p1_proc(
        model_number=args.model_number,
            )
    
    
if __name__ == '__main__':
    main()
    
    
    
    