import re
from models import Gas

class InvalidRecord(Exception):
    pass

class ResponseHandler:
    
    def __init__(self, response) -> None:
        self.response = response
        self.excluded = ['gasPriceRange']
        self.transform_fields = ['fast', 'fastest', 'safeLow', 'average']

    def _ensure_valid_data(self):
        keys = [key for key in self.response.keys() if key not in self.excluded]
        for key in keys:
            is_valid = self._is_valid_record(self.response[key])
            if not is_valid:
                raise InvalidRecord

    def transform_data(self):
        for key, value in self.response.items():
            if key in self.transform_fields:
                self.response[key] = self._transform(value)

    @staticmethod
    def _transform(data):
        try:
            return data / 10
        except ZeroDivisionError:
            raise ZeroDivisionError

    @staticmethod
    def _is_valid_record(record):
        try:
            if record >= 0:
                return True
            return False
        except TypeError:
            raise InvalidRecord

    @staticmethod
    def _camel_to_snake(name):
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

    @staticmethod
    def remap():
        return {
            'fast': 'gas_price_fast',
            'fastest': 'gas_price_fastest',
            'safe_low': 'gas_price_safe_low',
            'average': 'gas_price_average',
            'avg_wait': 'average_wait',
        }

    def to_snake_case(self):
        self._ensure_valid_data()
        self.transform_data()
        return {self._camel_to_snake(key): value for key, value 
                in self.response.items() if key not in self.excluded}
        
    def create_record(self):
        remapped = {self.remap().get(key, key): value for key, value
                    in self.to_snake_case().items()}
        return Gas(**remapped)


if __name__ == '__main__':
    import json
    with open('example.json') as fh:
        response = json.load(fh)

    handler = ResponseHandler(response)
    gas = handler.create_record()
    print('record created successfully')
    print(f"average gas price: {gas.gas_price_average}")
    print(f"gas price fastest: {gas.gas_price_fastest}")
    print(f"block number: {gas.block_num}")
    print(f"average wait: {gas.average_wait}")
   