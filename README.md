# Miner Manager
This program is intended to help manage Ethereum miners and help turn them off when ETH Gas prices are too low. When run, the package will make an API call to [ETH Gas Station's](https://ethgasstation.info) API to get the current gas prices in GWEI. The program will record the result in a SQLite DB stored in the `db` directory locally and will calculate the [Exponential Moving Average](https://www.investopedia.com/ask/answers/122314/what-exponential-moving-average-ema-formula-and-how-ema-calculated.asp#:~:text=The%20exponential%20moving%20average%20(EMA)%20is%20a%20technical%20chart%20indicator,importance%20to%20recent%20price%20data.)(EMA) over the last `n` calls and compare that to a threshold parameter to determine if the miner should be turned on/off. The EMA is used to avoid turning the miner on/off if there are sudden spikes in the price. It should only turn on/off based on the average price over a pre-determined timeframe. A `GAS_PRICE_THRESHOLD` parameter can be modified in [main.py](main.py) as well as a `N_RECORDS` parameter which controls how many previous API calls to compare against. This program is intended to be scheduled so that it runs every few minutes.

Lastly, the miner executable file and the corresponding `.bat` file should be placed in this directory _or_ otherwise you can edit the `PROCESS_NAME` and `BAT_FILEPATH` variables in the [miner.py](miner.py) file to point to the right path where those are installed.

## Requirements

A free API key for [ETH Gas Station](https://docs.ethgasstation.info/#how-to-obtain-an-api-key) is needed to run this program and should be exported as an environment varialbe named `ETH_GAS_STATION_API_KEY`.

## Installation and Usage

Install:
```bash
pip install setup.py
```

Run manually:
```bash
python main.py
```

**Note**: This is intented to run on a scheduled basis


