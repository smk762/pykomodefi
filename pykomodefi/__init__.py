#  _   __                     ______    ______ _ 
# | | / /                     |  _  \   |  ___(_)
# | |/ /  ___  _ __ ___   ___ | | | |___| |_   _ 
# |    \ / _ \| '_ ` _ \ / _ \| | | / _ \  _| | |
# | |\  \ (_) | | | | | | (_) | |/ /  __/ |   | |
# \_| \_/\___/|_| |_| |_|\___/|___/ \___\_|   |_|
#

"""
KomoDeFi Framework wrapper for Python
~~~~~~~~~~~~~~~~~~~~~

pykomodifi is a simple wrapper around Komodo Platform's DeFi API.


Basic usage:

   >>> import komodefi
   >>> dexapi = komodefi.KomoDeFi_API(config="path/to/MM2.json")
   >>> dexapi.version
   '1.0.7-beta_afe2e08'


Simple RPC call:

   >>> r = dexapi.rpc("get_enabled_coins")
   >>> r
   <Response [200]>
   >>> r.status_code
   200
   >>> r.json()
   {'result': [{'ticker': 'KMD', 'address': 'RMC1cWXngQf2117apEKoLh3x27NoG88yzd'}, {'ticker': 'LTC', 'address': 'LQyzwFtf8HU7VYQMhop5bv857uMao4jnKX'}]}

   
RPC call with parameters:

   >>> params = {"coin": "KMD"}
   >>> r = dexapi.rpc("my_balance", params)
   >>> r.json()
   {'coin': 'KMD', 'balance': '20', 'unspendable_balance': '0', 'address': 'RMC1cWXngQf2117apEKoLh3x27NoG88yzd'}


v2 RPC call:

   >>> r = dexapi.rpc("get_public_key", v2=True)
   >>> r.json()
   {'mmrpc': '2.0', 'result': {'public_key': '0371792f7a6846a0da28f3422501927ae103355c02750bc4c4d8430375329a09ac'}, 'id': None}


For documentation about available methods and parameters, refer to:
<https://developers.komodoplatform.com/basic-docs/atomicdex/introduction-to-atomicdex.html>

"""

from .models import KomoDeFi_API