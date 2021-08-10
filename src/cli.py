import argparse
from enum import Enum
from collections import ChainMap
from importlib import import_module
import json
import os
from typing import Dict
import sys

import requests


class League(Enum):
    NBA = "NBA"
    MLB = "MLB"
    NFL = "NFL"
    NCAAFB = "NCAAFB"
    NCAABB = "NCAABB"


class Action(Enum):
    Update = "update"
    Remove = "remove"
    Replace = "replace"
    Build = "build"


def build_headers(token: str, user: str, league: League, action: Action):
    return {
        "token": token,
        "username": user,
        "league": league.value,
        "action": action.value,
    }


def post_data(
    headers: Dict[str, str], data: Dict, url: str = "https://s3.sportsdatabase.com/api"
):
    req = requests.post(url, headers, json=data)
    return req


def main():
    parser = argparse.ArgumentParser(description="Process SDQL input data")
    parser.add_argument("--token", dest="token", required=True)
    parser.add_argument("--user", dest="user", required=True)
    parser.add_argument(
        "--action", dest="action", required=True, choices=[x.name for x in list(Action)]
    )
    parser.add_argument(
        "--league", dest="league", required=True, choices=[x.name for x in list(League)]
    )
    parser.add_argument("--data-file", dest="data_file", required=True)
    parser.add_argument("--url", dest="url", help="Override default API URL")
    parser.add_argument("-v", "--verbose", default=0, action="count", help="Show debug output")
    args = parser.parse_args()
    headers = build_headers(
        token=args.token,
        user=args.user,
        league=League[args.league],
        action=Action[args.action],
    )
    if args.data_file.endswith("py"):
        data_file_name = args.data_file.split("/")[-1]
        data_file_path = "/".join(args.data_file.split("/")[:-1])
        sys.path.append(os.path.expanduser(data_file_path))
        data_file = import_module(data_file_name.replace(".py", ""))
        data_attributes = [x for x in dir(data_file) if not x.startswith("_")]
        data_list = []
        [
            data_list.append(data_file.__dict__[x])
            for x in data_attributes
            if isinstance(data_file.__dict__[x], dict)
        ]
        data = dict(ChainMap(*data_list))
    else:
        with open(args.data_file, "r") as data_file:
            data = json.load(data_file)
    if args.verbose > 0:
        print(f"Headers: {headers}")
    if args.verbose > 1:
        print(f"Data: {data}")
    if args.verbose > 2:
        print(f"Data: {data}")
    if args.url:
        req = post_data(headers, data, url=args.url)
    else:
        req = post_data(headers, data)
    if req.status_code == 200:
        # Looks like the API is returning a 200 even in case of errors :(
        # print("Update Successful")
        try:
            print(req.json())
        except:
            print(req.text)
    else:
        print(f"Error: {req.status_code}. {req.text}")


if __name__ == "__main__":
    main()
