#!/usr/bin/env python3
import os
import json
import requests


class KomoDeFi_API():
    def __init__(self, config: str, protocol: str = "http"):
        if not os.path.isfile(config):
            raise FileNotFoundError(f"Komodefi SDK config not found at {config}!")
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
            return r
        except ConnectionRefusedError:
            raise ConnectionRefusedError(f"Komodefi SDK is not reponding at {self.mm2_ip}! Download it from https://github.com/KomodoPlatform/atomicDEX-API/releases")
        except Exception as e:
            body["userpass"] = "*********"
            print(f"Rpc request failed: {body}")
            print(f"Unhandled exception in KomoDeFi_API.rpc: {e}")
            return {"error": str(e)}

    @property
    def version(self):
        return self.rpc("version").json()["result"]

    @property
    def pubkey(self):
        return self.rpc("get_public_key", v2=True).json()["result"]

    @property
    def help(self):
        print("Please refer to https://github.com/smk762/pykomodo for docs and examples using pykomodefi.")
