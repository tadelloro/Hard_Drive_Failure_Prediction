
import pandas as pd
import os
# import time
import requests
import argparse


def pull_data(start_date, end_date):
    """
    Pull data from source and write to disk.
    
    Parameters:
        start_date: Start date in yyyy-mm-dd format.
        end_date: End date in yyyy-mm-dd format.
    Returns: 
        writes to disk.
    """
    urls = {
    f'{Q}Q{str(Y)[-2:]}':f'https://f001.backblazeb2.com/file/Backblaze-Hard-Drive-Data/data_Q{Q}_{Y}.zip'
    for Q, Y in [(d.quarter, d.year) for d in pd.date_range(start_date, end_date, freq='Q')]
    }

    if not os.path.isdir('data/p0_raw/'):
        os.system('mkdir data/p0_raw/')
    
    for k in urls.keys():
        if not os.path.exists('data/p0_raw/' + k):
            os.system('mkdir data/p0_raw/' + k)

        print('Requesting response from: ' + urls[k])
        resp = requests.get(urls[k])

        if resp.ok:
            print('Writing response to: /data/p0_raw/' + k + '/' + k + '.zip')
            with open('data/p0_raw/' + k + '/' + k + '.zip', 'wb') as f:
                f.write(resp.content)
            
            print('Unzipping data... \n')
            os.system('unzip ' + 'data/p0_raw/' + k + '/' + k + '.zip -d data/p0_raw/' + k + '/')
            
            os.system('rm ' + 'data/p0_raw/' + k + '/' + k + '.zip')
            os.system('rm -rf ' + 'data/p0_raw/' + k + '/' + '__MACOSX')
            
            if os.path.isdir('data/p0_raw/' + k + f'/data_Q{k[0]}_20{k[-2:]}'):
                os.system('mv data/p0_raw/' + k + f'/data_Q{k[0]}_20{k[-2:]}/* data/p0_raw/{k}/')
                os.system('rm -rf ' + 'data/p0_raw/' + k + f'/data_Q{k[0]}_20{k[-2:]}')
                
            if os.path.isdir('data/p0_raw/' + k + f'/data_q{k[0]}_20{k[-2:]}'):
                os.system('mv data/p0_raw/' + k + f'/data_q{k[0]}_20{k[-2:]}/* data/p0_raw/{k}/')
                os.system('rm -rf ' + 'data/p0_raw/' + k + f'/data_q{k[0]}_20{k[-2:]}')
                
            if os.path.isdir('data/p0_raw/' + k + f'/drive_stats_20{k[-2:]}_Q{k[0]}'):
                os.system('mv data/p0_raw/' + k + f'/drive_stats_20{k[-2:]}_Q{k[0]}/* data/p0_raw/{k}/')
                os.system('rm -rf ' + 'data/p0_raw/' + k + f'/drive_stats_20{k[-2:]}_Q{k[0]}')
                
            print('\n', k + ' complete. \n')
            print('------------------------------------------------------------------------------- \n')

        else:
            print(f'Response for {k} failed with {resp}')
            print(resp.content.decode('ascii'))
    
    
def parse_arguments():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-sd', '--start_date', 
                        type=str, 
                        required=True, 
                        help='Start date in yyyy-mm-dd format.',
                       )
    parser.add_argument('-ed', '--end_date', 
                        type=str, 
                        required=True, 
                        help='End date in yyyy-mm-dd format.',
                       )
    args = parser.parse_args()
    
    return args
    
    
def main():
    
    args = parse_arguments()
    print(args)

    
    pull_data(start_date=args.start_date, 
              end_date=args.end_date, 
             )
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    