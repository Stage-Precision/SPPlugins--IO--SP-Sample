import sp
import os


#Sample SP IO Structure

class SampleModule(sp.BaseModule):

	#plugin info used 
	pluginInfo = {
        "name" : "Sample Plugin",
		"category" : "Plugins",
        "description" : "show how to create SP Plugin IO \r ",
        "author" : "SP",
        "version" : (1, 0),
        "spVersion" : (1, 0, 142),
		"helpPath" : os.path.join(os.path.dirname(os.path.abspath(__file__)),"help.md")
    }

	def __init__(self):
		sp.BaseModule.__init__(self)
		
	def afterInit(self):

		#create Settings with Parameter inside the IO

		#inside module Container
		self.stringPara = self.moduleContainer.addStringParameter("Example String", "string")
		self.intPara = self.moduleContainer.addIntParameter("Exampel Int", 587, 1, 65535)
		self.floatPara = self.moduleContainer.addFloatParameter("Example Float", 0, 0, 100)

		#create own stackable containers 
		subContainer = self.addContainer("Setting")
		self.stringpara = subContainer.addStringParameter("Eample", "sring")

		#create actions with definable parameters
		# (nicename, folder, function)
		action = self.addAction("Run Example Action", "", self.onRunExampleAction)
		action.addStringParameter("Message", "mes")

		#create event to react inside SP events
		self.registerEvent("Example Event", "exampleEvent")

		#create a timer callback to run in cycle - in this example every 30s 
		self.addTimer("checker", 30, self.checkfunction)
		
	# function to react on user change of parameters - it will call by change by user or remoted
	def onParameterFeedback(self, parameter):
		if parameter == self.stringPara:
			print("string parameter changed"+ self.stringPara.value)

	def onRunExampleAction(self, sMessage):
		print(sMessage+ self.stringPara.value)
		self.emitEvent("exampleEvent")

	def checkfunction(self):
		print("timer called")


if __name__ == "__main__":
    sp.registerPlugin(SampleModule)
