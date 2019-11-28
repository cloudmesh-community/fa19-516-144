""" 
config_get.py
Demonstrate that the config.get() does not work in all cases
"""

from cloudmesh.common.console import Console
from cloudmesh.configuration.Config import Config
from cloudmesh.common.util import banner
config = Config()
#########################################################################
banner("Demonstration Using get_value()", color = "RED")

Console.ok("Test: Full Path: cloudmesh.version")
path = "cloudmesh.version"
foo = config.get_value(path)
Console.ok(f"res type: {type(foo)}")
Console.ok(f"result: {foo}\n")

Console.ok("Test: From Docs: default.group")
path = "default.group"
foo = config.get_value(path)
Console.ok(f"res type: {type(foo)}")
Console.ok(f"result: {foo}")
Console.error("Explanation: get_value() only full paths defined in config\n")

Console.ok("Test: Part Path: cloudmesh.profile")
path = "cloudmesh.profile"
foo = config.get_value(path)
Console.ok(f"res type: {type(foo)}")
Console.ok(f"result:{foo}\n")

#########################################################################
banner("Demonstration Using get_value()", color = "RED")
Console.ok("Test: Full Path: cloudmesh.version")
path = "cloudmesh.version"
foo = config.get(path)
Console.ok(f"res type: {type(foo)}")
Console.ok(f"result: {foo}")
Console.error("Explanation: unknown\n")

Console.ok("Test: From Docs: default.group")
path = "default.group"
foo = config.get(path)
Console.ok(f"res type: {type(foo)}")
Console.ok(f"result: {foo}")
Console.error("Explanation: unknown\n")

Console.ok("Test: Part Path: cloudmesh.profile")
path = "cloudmesh.profile"
foo = config.get(path)
Console.ok(f"res type: {type(foo)}")
Console.ok(f"result:{foo}")
Console.error("Explanation: unknown\n")

##########################################################################
banner("Explanations and Notes", color = "RED")
Console.error("get() returns none in all cases\n")
Console.ok("gett_value() returns string, dict, or None [only if full path doesn't exist")
