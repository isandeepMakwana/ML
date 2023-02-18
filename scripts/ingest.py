import dask.dataframe as dd
import os
import sqlite3


def IngestData(directory):
    # list to store Dask dataframes for each file
    dfs = []

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)

            # create Dask dataframe from text file
            df = dd.read_csv(filepath, sep="\t", header=None,
                            names=["Date", "Maxtemp", "Mintemp", "Precipitation"])

            # add filename as new column
            df["Station_ID"] = filename[:11]
            dfs.append(df)

    # concatenate Dask dataframes into one
    df = dd.concat(dfs)

    # compute the final dataframe and convert to Pandas dataframe
    df = df.compute()
    df = df.reset_index(drop=True)

    #Drop the -9999 indicating the empty values
    stats = df[(df['Maxtemp'] != -9999) |
            (df['Mintemp'] != -9999) | (df['Precipitation'] != -9999)]

    #creating the stats data
    stats = stats.groupby(['Station_ID', df['Date'].map(str).str[:4]]).agg({
        'Maxtemp': 'mean',
        'Mintemp': 'mean',
        'Precipitation': 'sum'
    }).reset_index()

    stats.rename(columns={'Maxtemp': 'AvgMaxtemp',
                        'Mintemp': 'AvgMintemp',
                        'Precipitation': 'TotalAccPrecipitation'}, inplace=True)

    conn = sqlite3.connect('data/db.sqlite3')


    # write data to database
    df.to_sql("app_weather", conn, if_exists="replace",
            index=True, index_label='id')
    stats.to_sql("app_stats", conn, if_exists="replace",
                index=True, index_label='id')
    # close database connection
    conn.close()
    return

IngestData('data')