from django.shortcuts import render
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

def IndexesPage(request):
    indexes = cg.get_coins_markets(vs_currency='usd',category='defi-index')
    context ={
        'indexes':indexes,
    }
    return render(request,'front/indexes.html',context)