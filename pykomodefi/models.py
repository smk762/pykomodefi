#!/usr/bin/env python3
import os
import json
import requests


class KomoDeFi_API:
    def __init__(self, config: str = "", protocol: str = "http"):
        self.protocol = protocol
        self.set_config(config)

    def rpc(self, method: str, params: dict = dict(), v2: bool = False):
        try:
            if v2:
                body = {"mmrpc": "2.0", "params": params}
            elif params:
                body = params
            else:
                body = dict()

            body.update({"userpass": self.userpass, "method": method})
            r = requests.post(self.mm2_ip, json.dumps(body)).json()
            return r
        except ConnectionRefusedError:
            raise ConnectionRefusedError(f"Komodefi SDK is not reponding at {self.mm2_ip}!")
        except Exception as e:
            body["userpass"] = "*********"
            return {
                "error": f"Unhandled exception in KomoDeFi_API.rpc: {e}",
                "request": body,
            }

    def set_config(self, config: str):
        if config == "":
            config = f"{os.getcwd()}/MM2.json"
        if not os.path.exists(config):
            raise FileNotFoundError(f"Komodefi SDK config not found at {config}!")
        else:
            self.config = config
            with open(self.config, "r") as f:
                self.mm2_json = json.load(f)

    @property
    def db_dir(self):
        return (
            self.mm2_json["dbdir"]
            if "dbdir" in self.mm2_json
            else f"{os.path.dirname(self.config)}/DB"
        )

    @property
    def netid(self):
        return self.mm2_json["netid"] if "netid" in self.mm2_json else 8762

    @property
    def account_id(self):
        return (
            self.mm2_json["hd_account_id"] if "hd_account_id" in self.mm2_json else None
        )

    @property
    def userpass(self):
        return (
            self.mm2_json["rpc_password"] if "rpc_password" in self.mm2_json else None
        )

    @property
    def rpcip(self):
        return self.mm2_json["rpcip"] if "rpcip" in self.mm2_json else "127.0.0.1"

    @property
    def rpcport(self):
        return self.mm2_json["rpcport"] if "rpcport" in self.mm2_json else 7783

    @property
    def version(self):
        r = self.rpc("version")
        if "result" in r:
            return r["result"]
        return r

    @property
    def pubkey(self):
        r = self.rpc("get_public_key", v2=True)
        if "result" in r:
            if "public_key" in r["result"]:
                return r["result"]["public_key"]
        return r

    @property
    def pubkey_hash(self):
        r = self.rpc("get_public_key_hash", v2=True)
        if "result" in r:
            if "public_key_hash" in r["result"]:
                return r["result"]["public_key_hash"]
        return r

    @property
    def mm2_ip(self):
        return f"{self.protocol}://{self.rpcip}:{self.rpcport}"

    @property
    def peers_info(self):
        r = self.rpc("get_peers_info")
        if "result" in r:
            return r["result"]
        return r

    @property
    def peer_id(self):
        r = self.rpc("get_my_peer_id")
        if "result" in r:
            return r["result"]
        return r

    @property
    def orders(self):
        r = self.rpc("my_orders")
        if "result" in r:
            return r["result"]
        return r

    @property
    def active_swaps(self):
        r = self.rpc("active_swaps")
        if "result" in r:
            return r["result"]
        return r

    @property
    def enabled_coins(self):
        r = self.rpc("get_enabled_coins")
        if "result" in r:
            return r["result"]
        return r

    @property
    def help(self):
        print(
            "Please refer to https://github.com/smk762/pykomodefi for documentation."
        )
