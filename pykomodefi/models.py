#!/usr/bin/env python3
import os
import json
import requests
from .logger import logger


class KomoDeFi_API():
    def __init__(self, config: str, protocol: str = "http"):
        if not os.path.isfile(config):
            logger.error(f"Komodefi SDK config not found at {config}!")
        else:            
            with open(config, "r") as f:
                conf = json.load(f)
            self.userpass = conf["rpc_password"]

            ip = '127.0.0.1'
            if "rpc_ip" in conf:
                ip = conf["rpc_ip"]

            port = 7783
            if "rpcport" in conf:
                port = conf["rpcport"]

            netid = 7777
            if "netid" in conf:
                self.netid = conf["netid"]

            self.mm2_ip = f"{protocol}://{ip}:{port}"


    def rpc(self, method: str, params: dict = dict(), v2: bool = False):
        try:
            if v2:
                body = {
                    "mmrpc": "2.0",
                    "params": params
                }
            elif params:
                body = params
            else:
                body = dict()

            body.update({
                "userpass": self.userpass,
                "method": method
            })
            r = requests.post(self.mm2_ip, json.dumps(body))
            if 'error' in r.json():
                logger.error(f"Error in KomoDeFi_API.rpc: {r.json()['error']}")
            return r
        except ConnectionRefusedError:
            logger.error(f"Komodefi SDK is not reponding at {self.mm2_ip}! Download it from https://github.com/KomodoPlatform/atomicDEX-API/releases")
        except Exception as e:
            logger.error(f"Exception in KomoDeFi_API.rpc: {e}")
            return None

    @property
    def version(self):
        try:
            return self.rpc("version").json()["result"]
        except ConnectionRefusedError:
            return "Error"

    @property
    def pubkey(self):
        try:
            return self.rpc("get_public_key", v2=True).json()["result"]
        except ConnectionRefusedError:
            return "Error"

    @property
    def help(self):
        print("Please refer to https://github.com/smk762/pykomodo for docs and examples using pykomodefi.")
