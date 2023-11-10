#!/usr/bin/env bash
from datadog import initialize, api

options = {
    'api_key': '7c87085524cbf73af6ef78094cf84e2a',
    'app_key': '4dcebc9fb6dde1ed535330874c4ac9549a35a1fa'
}

initialize(**options)

api.Hosts.search()

