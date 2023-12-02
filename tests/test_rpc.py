#!/usr/bin/env python3
import os
import pykomodefi as pkd
from dotenv import load_dotenv

load_dotenv()

SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))
MM2_PATH = os.path.dirname(SCRIPT_PATH)
MM2_JSON_PATH = os.getenv("MM2_JSON_PATH", f"{MM2_PATH}/MM2.json")

print(f"Using {MM2_JSON_PATH}...")
dexapi = pkd.KomoDeFi_API(config=MM2_JSON_PATH)


def test_rpcs():
    print(f"dexapi.mm2_ip:        {dexapi.mm2_ip}")
    print(f"dexapi.version:       {dexapi.version}")
    print(f"dexapi.pubkey:        {dexapi.pubkey}")
    print(f"dexapi.orders:        {dexapi.orders}")
    print(f"dexapi.active_swaps:  {dexapi.active_swaps}")
    print(f"dexapi.enabled_coins: {dexapi.enabled_coins}")
    print(f"dexapi.pubkey_hash:   {dexapi.pubkey_hash}")
    print(f"dexapi.peers_info:    {dexapi.peers_info}")
    print(f"dexapi.peer_id:       {dexapi.peer_id}")
    assert dexapi.rpc("get_enabled_coins")["result"] == dexapi.enabled_coins
    params = {"base": "DGB", "rel": "KMD"}
    assert "asks" in dexapi.rpc("orderbook", params)
    dexapi.help
