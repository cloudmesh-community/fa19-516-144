""" 
config_get.py
Demonstrate that the config.get() does not work in all cases
"""
from cloudmesh.common.console import Console
from cloudmesh.configuration.Config import Config
from cloudmesh.common.util import banner
from pprint import pprint

config = Config()

p = config["cloudmesh.profile"]
q = config.get("cloudmesh.profile")

pprint(p)
pprint(q)

    
#########################################################################
banner("Demonstration Using get()", color = "BLUE")

    
    
for path in ["cloudmesh.version", "cloudmesh.profile"]: # default.group was not in my yaml
    Console.ok(f"Test Path: {path}")
    for value in [config.get(path), config[path]]:
        Console.ok(f"res type: {type(value)}")
        Console.ok(f"result: {value}\n")


