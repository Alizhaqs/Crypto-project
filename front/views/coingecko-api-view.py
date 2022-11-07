from pycoingecko import CoinGeckoAPI
import json
cg = CoinGeckoAPI()
from django.core.serializers.json import DjangoJSONEncoder

bitcoin_price = cg.get_price(ids='bitcoin',vs_currencies='usd')
coin_list = cg.get_coins_list()

coins = cg.get_coin_by_id(id='defipulse-index')

print(coins)