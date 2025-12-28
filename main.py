import pandas as pd
from utils import addDatesCol, checkNanValues, cleanData, logReturns, logVolume, volZScore, cumsum

next_power = "NXT"
nextera = "NEE"
centrus = "LEU"
energy_fuels = "UUUU"
enphase_energy = "ENPH"
sp500 = "SPX"

df_next_power = pd.read_csv("./datasets/nxt_us_d.csv")
df_nextera = pd.read_csv("./datasets/nee_us_d.csv")
df_centrus = pd.read_csv("./datasets/leu_us_d.csv")
df_energy_fuels = pd.read_csv("./datasets/uuuu_us_d.csv")
df_enphase = pd.read_csv("./datasets/enph_us_d.csv")
df_spx = pd.read_csv("./datasets/^spx_d.csv")

dataframes = [df_next_power, df_nextera, df_centrus, df_energy_fuels, df_enphase, df_spx]
symbols = [next_power, nextera, centrus, energy_fuels, enphase_energy, sp500]

for i in range(len(dataframes)):
    dataframe = dataframes[i]
    symbol = symbols[i]
    # print("-----------------------------------")
    # print("symbol:",symbol,"\n",dataframe)
    addDatesCol(dataframe)
    years = sorted(dataframe['Year'].dropna().unique())
    # print(years)
    # print(checkNanValues(dataframe))

for i in range(len(dataframes)):
    dataframe = dataframes[i]
    symbol = symbols[i]
    dataframe = cleanData(dataframe)
    print(symbol)
    #print(dataframe)
    dataframe = logReturns(dataframe)
    dataframe = logVolume(dataframe)
    print(dataframe)
    print(dataframe["log_returns"].describe())
    dataframe = volZScore(dataframe)
    print("z score volume", dataframe["vol_zscore_20"])
    cumsum(dataframe, symbol)





