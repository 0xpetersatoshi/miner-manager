import os
import yaml
import logging
import logging.config
from miner_manager.averages import calculate_ema
from miner_manager.client import APIClient
from miner_manager.response_handler import ResponseHandler
from miner_manager.miner import miner_is_on, toggle_miner_on_off
from miner_manager.models import Gas

with open('log.yaml') as fp:
    config = yaml.safe_load(fp.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

N_RECORDS = 4
GAS_PRICE_THRESHOLD = 40

def get_and_create_gas_record():
    api_key = os.getenv('ETH_GAS_STATION_API_KEY')
    client = APIClient(api_key)
    logger.info('making API request')
    handler = ResponseHandler(client.get())
    logger.info('creating gas record')
    gas_record = handler.create_record()
    logger.info('saving record to db')
    gas_record.save()


def evaluate_latest_gas_trend(n_records: int) -> float:
    """Calculate EMA of previous N_RECORDS of gas prices"""
    gas_prices = []
    for gas in Gas.select().order_by(Gas.created_at.desc()).limit(n_records):
        gas_prices.append(gas.gas_price_average)

    return calculate_ema(gas_prices)


def miner_handler(ema: float):
    """Check EMA and miner status and turn on/off depending on results"""
    miner_on = miner_is_on()
    logger.info(f'current gas price EMA: {ema} GWEI')
    logger.info(f'miner status: {"on" if miner_on else "off"}')
    if ema >= GAS_PRICE_THRESHOLD and not miner_on:
        logger.info(f'turning miner on...')
        toggle_miner_on_off()
    elif ema < GAS_PRICE_THRESHOLD and miner_on:
        logger.info(f'turning miner off...')
        toggle_miner_on_off()
    else:
        logger.info('no action necessary')


def main():
    logger.info(f'gas price (GWEI) threshold: {GAS_PRICE_THRESHOLD}')
    logger.info(f'number of gas prices to compare: {N_RECORDS}')
    get_and_create_gas_record()
    ema = evaluate_latest_gas_trend(N_RECORDS)
    miner_handler(ema)


if __name__ == '__main__':
    main()
