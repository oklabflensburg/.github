import click
import geopandas as gp
import pandas as pd
import os

from requests import Request
from owslib.wfs import WebFeatureService
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)


try:
    database = os.getenv('DB_NAME')
    password = os.getenv('DB_PASS')
    user = os.getenv('DB_USER')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')

    connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'
    engine = create_engine(connection_string)
except Exception as e:
    print(e)



def fetch_features(url, service, version, from_crs, to_crs, layer, limit, ix) -> gp.GeoDataFrame:
    params = dict(service=service, version=version, request='GetFeature',
        typeNames=layer, count=limit, startIndex=ix*limit,
        outputFormat='application/gml+xml; version=3.2', crsname=from_crs)

    wfs_request_url = Request('GET', url, params=params).prepare().url
    print(wfs_request_url)

    try:
        df_new = gp.read_file(wfs_request_url)
        df_new = df_new.set_crs(crs=from_crs)
        df_new = df_new.to_crs(crs=to_crs)
    except ValueError as e:
        print(e)
        return

    return df_new


def loop_layer(url, service, version, from_crs, to_crs, layer, max_loops=100, item_limit=1000) -> gp.GeoDataFrame:
    df = None
    cnt = 0

    for ix in range(1000):
        df_new = fetch_features(url, service, version, from_crs, to_crs, layer, item_limit, ix)

        if df_new is None:
            break

        new_cnt = len(df_new)

        if new_cnt == 0:
            break

        cnt += new_cnt

        if df is None:
            df = df_new
        else:
            df = pd.concat([df, df_new])

        if new_cnt < item_limit:
            break

    return df


@click.command()
@click.option('--url', '-u', required=True, type=str, help='xxx')
@click.option('--to_crs', '-tc', required=True, type=str, help='xxx')
@click.option('--from_crs', '-fc', required=True, type=str, help='xxx')
@click.option('--version', '-v', required=True, type=str, help='xxx')
@click.option('--service', '-s', required=True, type=str, help='xxx')
@click.option('--output', '-o', type=str, help='xxx')
@click.option('--table', '-t', type=str, help='xxx')
def main(url, from_crs, to_crs, service, version, output, table):
    # url = 'https://gdi.berlin.de/services/wfs/postleitzahlen'

    wfs = WebFeatureService(url=url, version=version)
    layers = list(wfs.contents)
    print(layers)

    for layer in layers:
        df = loop_layer(url, service, version, from_crs, to_crs, layer)
        df.to_postgis(table, if_exists='replace', con=engine)
        # df.to_file(output)


if __name__ == '__main__':
    main()
