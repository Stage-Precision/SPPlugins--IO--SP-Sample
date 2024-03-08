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
		self.intPara = self.moduleContainer.addIntParameter("Example Int", 587, 1, 65535)
		self.floatPara = self.moduleContainer.addFloatParameter("Example Float", 0, 0, 100)


		#create own stackable containers 
		subContainer = self.addContainer("Setting")
		self.stringpara = subContainer.addStringParameter("Example", "string")
		self.ippara = subContainer.addIPParameter("Example IP", False)
		self.datatargetpara = subContainer.addDataTargetParameter("Example Data Target", "", "")

		#create a dropdown parameter
		self.enumpara = subContainer.addEnumParameter("Dropdown", 0, "Option 1;Option 2;Option 3;Option 4")
		self.enumpara.addOption("dynamic Option 5", 4)
		
		#create actions with definable parameters
		# (nickname, folder, function)
		action = self.addAction("Run Example Action", "", self.onRunExampleAction)
		action.addStringParameter("Message", "msg")
		action.addFloatParameter("Float", 0, 0, 100)
		action.addIntParameter("Int", 0, 0, 100)
		action.addBoolParameter("Bool", False)
		action.addEnumParameter("Enum", 0, "A 1;B 2;C 3")
		action.addPointParameter("Point", 0, 0, -100, 100, -100, 100)
		action.addVectorParameter("Vector", 0, 0, 0, -100, 100, -100, 100, -100, 100)
		#action.addIPParameter("IP", False)
		#action.addColorParameter("Color", 0, 0, 0, 255)
		#action.addDataParameter("Data")
		#action.addDataTargetParameter("Data Target", "", "")
		
		#action withe return values - with names for Action Tokens
		actionR = self.addAction("Get Var from Action", "", self.onRunExampleReturnAction)
		actionR.addScriptTokens(["temperature", "humidity"])

		#create event to react inside SP events
		self.registerEvent("Example Event", "exampleEvent")

		#create a timer callback to run in cycle - in this example every 30s 
		self.addTimer("checker", 30, self.checkfunction)
		
	# function to react on user change of parameters - it will call by change by user or remoted
	def onParameterFeedback(self, parameter):
		if parameter == self.stringPara:
			print("string parameter changed"+ self.stringPara.value)

	def onRunExampleAction(self, msg, float, int, bool, enum, point, vector):
		print(f"String Message: {msg}")
		print(f"Float: {float}")
		print(f"Int: {int}")
		print(f"Bool: {bool}")
		print(f"Enum: {enum}")
		print(f"Point: {point}")
		print(f"Vector: {vector}")
		#print(f"Data Target: {dataTarget[0]}")
		self.emitEvent("exampleEvent")
		
	def onRunExampleReturnAction(self):
		return {"temperature": 29.5, "humidity": 50.5}

	def checkfunction(self):
		print("timer called")


if __name__ == "__main__":
	sp.registerPlugin(SampleModule)
