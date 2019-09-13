"""
common.py 
Pupose: Domonstrate Knowledge of Common Cloudmesh Functionality
"""

from cloudmesh.common.util import banner, HEADING
from cloudmesh.common.variables import Variables
from cloudmesh.common.FlatDict import FlatDict
from cloudmesh.common.dotdict import dotdict
from cloudmesh.common.console import Console
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.Shell import Shell
from cloudmesh.common.StopWatch import StopWatch
import time

# E.Cloudmesh.Common.5
StopWatch.start("test")

# Sets variables within  ~/.cloudmesh/var-data 
varz = Variables()
varz['debug'] = True
varz['trace'] = True
varz['verbose'] = 10

# E.Cloudmesh.Common.1
banner("Exercise Cloudmesh Common", color="GREEN")

class Common:
	def __init__(self):
		self.data = {"user": "andrew", "test": {"res": "success",  "time": "30s"}}
		self.flat = FlatDict( self.data )
		self.dotd = dotdict( self.data )
	
	def run_all(self):
		self.exercise1()
		self.exercise2()
		self.exercise3()
		self.exercise4()
		self.exercise5()

	# E.Cloudmesh.Common.1
	def exercise1(self):
		HEADING()
		VERBOSE(self.data)
	
	# E.Cloudmesh.Common.2
	def exercise2(self):
		HEADING()
		Console.msg("User = " + self.dotd.user)			
		Console.msg("User = " + self.dotd['user'])

	# E.Cloudmesh.Common.3
	def exercise3(self):
		HEADING()
		Console.msg("User = " + self.flat['user'])
		Console.msg("Res = " + self.flat['test__res'])
	
	# E.Cloudmesh.Common.4
	def exercise4(self):
		HEADING()
		res = Shell.pwd()
		print (res)
		res = Shell.get_python()
		print (res)

	# E.Cloudmesh.Common.5
	def exercise5(self):
		HEADING()
		time.sleep(1)
		StopWatch.stop("test")
		print (StopWatch.get("test"))
	
common = Common()
common.run_all()
