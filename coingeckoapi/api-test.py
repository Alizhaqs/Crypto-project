from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

bit_price = cg.get_price(ids='bitcoin',vs_currencies='usd')
breakpoint()