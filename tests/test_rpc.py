#!/usr/bin/env python3
import time
import pykomodefi as pkd

dexapi = pkd.KomoDeFi_API(config="MM2.json")

print(dexapi.mm2_ip)
print(dexapi.version)
print(dexapi.pubkey)
print(dexapi.orders)
print(dexapi.active_swaps)
print(dexapi.enabled_coins)
print(dexapi.rpc("get_enabled_coins").json()["result"])
assert dexapi.rpc("get_enabled_coins").json()["result"] == dexapi.enabled_coins
print(dexapi.pubkey_hash)
print(dexapi.peers_info)
print(dexapi.peer_id)
print(dexapi.rpc("get_enabled_coins").json()["result"])
params = {
  "coin":"ETH",
  "from":"0xfb6916095ca1df60bb79ce92ce3ea74c37c5d359",
  "to_address_format":{
    "format":"mixedcase"
  }
}
print(dexapi.rpc("convertaddress", params).json()["result"])
assert dexapi.rpc("convertaddress", params).json()["result"]["address"] == "0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359"

dexapi.help
