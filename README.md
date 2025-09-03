
## KomoDeFi Framework wrapper for Python

[**pykomodefi**](https://pypi.org/project/pykomodefi/) is a simple wrapper around [Komodo Platform's](https://komodoplatform.com/en/) [DeFi Framework](https://github.com/KomodoPlatform/komodo-defi-framework).


### Installation

`pip install pykomodefi`


### Usage

**Configuration:**

The configuration file can be passed as a parameter to the `KomoDeFi_API` class constructor:

```
   >>> import pykomodefi
   >>> dexapi = pykomodefi.KomoDeFi_API(config="/path/to/MM2.json")
```
If not set, the default configuration file path is `MM2.json` in the current folder, or `~/.kdf/MM2.json`.
It can be set to a different file later:

```
   >>> import pykomodefi
   >>> dexapi = pykomodefi.KomoDeFi_API()
   >>> dexapi.set_config = "/path/to/MM2.json"
```


**Simple RPC call:**
```
   >>> resp = dexapi.rpc("get_enabled_coins")
   >>> resp
   {
      'result': [
         {
            'ticker': 'KMD',
            'address': 'RMC1cWXngQf2117apEKoLh3x27NoG88yzd'
         },
         {
            'ticker': 'LTC',
            'address': 'LQyzwFtf8HU7VYQMhop5bv857uMao4jnKX'
         }
      ]
   }
```
   
**RPC call with parameters:**
```
   >>> params = {"coin": "KMD"}
   >>> resp = dexapi.rpc("my_balance", params)
   >>> resp
   {
      'coin': 'KMD',
      'balance': '20',
      'unspendable_balance': '0',
      'address': 'RMC1cWXngQf2117apEKoLh3x27NoG88yzd'
   }
```

**v2 RPC call:**
```
   >>> resp = dexapi.rpc("get_public_key", v2=True)
   >>> resp
   {
      'mmrpc': '2.0',
      'result': {
         'public_key': '0371792f7a6846a0da28f3422501927ae103355c02750bc4c4d8430375329a09ac'
      },
      'id': None
   }
```


The following methods are available as properties of the `KomoDeFi_API` class. These methods do not require any input parameters:
```
   >>> dexapi.version
   '1.0.7-beta_afe2e08'

   >>> dexapi.pubkey
   '0366d28a7926fb20287132692c4cef7bc7e00e76da064948676f8549c0ed7114d3'

   >>> dexapi.pubkey_hash
   '05aab5342166f8594baf17a7d9bef5d567443327'

   >>> dexapi.peer_id
   '12D3KooWS9MeuFZhJCfQTntwbTVnXMAJpz9Tvd1XYFuURrGqnJVR'

   >>> dexapi.peers_info
   {
      "12D3KooWM8BrDBXc1TVw2vswoqYcQVn7fFvpAvcCfaV2Uqg2L9jU":["/ip4/89.248.168.39/tcp/38890"],
      "12D3KooWJ3dEWK7ym1uwc5SmwbmfFSRmELrA9aPJYxFRrQCCNdwF":["/ip4/188.124.46.112/tcp/38890/p2p/12D3KooWJ3dEWK7ym1uwc5SmwbmfFSRmELrA9aPJYxFRrQCCNdwF"],
      "12D3KooWL6yrrNACb7t7RPyTEPxKmq8jtrcbkcNd6H5G2hK7bXaL":["/ip4/168.119.236.233/tcp/38890/p2p/12D3KooWL6yrrNACb7t7RPyTEPxKmq8jtrcbkcNd6H5G2hK7bXaL"],
      "12D3KooWPR2RoPi19vQtLugjCdvVmCcGLP2iXAzbDfP3tp81ZL4d":["/ip4/168.119.237.13/tcp/38890/p2p/12D3KooWPR2RoPi19vQtLugjCdvVmCcGLP2iXAzbDfP3tp81ZL4d"],
      "12D3KooWKxavLCJVrQ5Gk1kd9m6cohctGQBmiKPS9XQFoXEoyGmS":["/ip4/168.119.236.249/tcp/38890/p2p/12D3KooWKxavLCJVrQ5Gk1kd9m6cohctGQBmiKPS9XQFoXEoyGmS"],
      "12D3KooWDbBdifGp3viDR4dCECEFKepjhwhd2YwAqgNVdXpEeewu":["/ip4/80.82.76.214/tcp/38890"],
      "12D3KooWJDoV9vJdy6PnzwVETZ3fWGMhV41VhSbocR1h2geFqq9Y":["/ip4/89.248.173.231/tcp/38890"]
   }

   >>> dexapi.orders
   {
      "maker_orders": {
         ....
      },
      "taker_orders": {
         ....
      }
   }

   >>> dexapi.active_swaps
   {
      "uuids": [
         "015c13bc-da79-43e1-a6d4-4ac8b3099b34",
         "7592a07a-2805-4050-8ab8-984480e812f0",
         "82cbad96-ea9f-40fb-9225-07496323e35d",
         "177f7fa5-c9f3-4673-a2fa-28451a123e61"
      ]
   }

   >>> dexapi.enabled_coins
   [
      {
         "address": "1WxswvLF2HdaDr4k77e92VjaXuPQA8Uji",
         "ticker": "BTC"
      },
      {
         "address": "R9o9xTocqr6CeEDGDH6mEYpwLoMz6jNjMW",
         "ticker": "KMD"
      },
      {
         "address": "R9o9xTocqr6CeEDGDH6mEYpwLoMz6jNjMW",
         "ticker": "VRSC"
      },
      {
         "address": "0xbAB36286672fbdc7B250804bf6D14Be0dF69fa29",
         "ticker": "ETH"
      }
   ]
```

For documentation about available methods and parameters, refer to: <https://developers.komodoplatform.com/basic-docs/atomicdex/introduction-to-atomicdex.html>

Some configuration params from within `MM2.json` are also available as properties:
```
>>> dexapi.netid
8762
>>> dexapi.rpcip
127.0.0.1
>>> dexapi.rpcport
7783
>>> dexapi.db_dir
/path/to/DB
```

### Building locally

- Run `poetry build`
- Run `pipx install --spec $(pwd)/dist/pykomodefi-0.2.5.tar.gz pykomodefi --include-deps --force` (change version number accordingly)

### Running tests

**Prerequisites:**
- Install dependencies: `poetry install`
- Set up test configuration by either:
  - Creating `tests/.env` file with: `MM2_JSON_PATH=tests/MM2.json`
  - OR copying test config to project root: `cp tests/MM2.json .`

**Run tests:**
```bash
# Run all tests with coverage
poetry run pytest tests/ -v

# Run tests with verbose output
poetry run pytest tests/ -vv

# Run with coverage report
poetry run pytest tests/ --cov=pykomodefi --cov-report=html
```

**Note:** Tests will show connection errors if the KomoDeFi Framework (MM2) is not running. This is expected behavior - the package correctly handles and reports connection failures. To run tests against a live MM2 instance, ensure MM2 is running on `127.0.0.1:7783` before running the tests.
