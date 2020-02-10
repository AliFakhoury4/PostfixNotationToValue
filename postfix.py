import array_stack as AS 

def postfixOperation(value1, value2, operand):
	newValue = 0

	if(operand=='+'):
		print("Stack adds "+str(value1)+" and "+str(value2))
		newValue = float(value1)+float(value2)
	elif(operand=='-'):
		newValue = float(value2)-float(value1)
		print("Stack subtracts "+str(value2)+" and "+str(value1))
	elif(operand=='/'):
		newValue = float(value2)/float(value1)
		print("Stack divides "+str(value2)+" and "+str(value1))
	elif(operand=='*'):
		newValue = float(value2)*float(value1)
		print("Stack multiplies "+str(value1)+" and "+str(value2))

	return newValue


stack = AS.ArrayStack()
outputStack = AS.ArrayStack()

postfixString = "52+83-*4/"

for x in postfixString:
	stack.push(x)

	print("Stack reads "+x)

	if (x=='+' or x=='-' or x=='/' or x=='*'):
		stack.pop()
		if(stack.is_empty()):
			val1 = outputStack.pop()
			val2 = outputStack.pop()

			newValue = postfixOperation(val1, val2, x)
			outputStack.push(newValue)
		else:
			val1 = stack.pop()

			if(stack.is_empty()):
				val2 = outputStack.pop()
				newValue = postfixOperation(val1, val2, x)
				outputStack.push(newValue)
			else:
				val2 = stack.pop()
				newValue = postfixOperation(val1, val2, x)	
				outputStack.push(newValue)

print("Final answer of the postfix notation is: "+str(outputStack.pop()))