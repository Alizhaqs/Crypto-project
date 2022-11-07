from django.shortcuts import redirect,render
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


def MainPage(request):
    btc_price = cg.get_price(ids='bitcoin', vs_currencies='usd')
    coins = cg.get_coins_markets(vs_currency='usd')

    context ={
        'coins':coins,
    }
    return render(request,'front/index.html',context)

def UserProfile(request):
    context = {

    }
    return render(request,'front/user-profile.html',context)
