
from cnf2sat import satisfiable

def NOT(var):
	return var*-1;

#find the 2 switches a light is connected to.
#the light is a number between 0 and num_lights -1
def get_switches(switch_matrix, num_switches, light):

	switches = [-1, -1];
	#search every element in the switch matrix
	for j in range(num_switches):
		for k in range(len(switch_matrix[j])):
			#if you find that a switch is connected to the lightbulb i
			if (switch_matrix[j][k] != None and switch_matrix[j][k] == light+1):
				#set it as either switch 1 (if it is the first switch you found)
				if(switches[0] == -1):
					switches[0] = j+1;
				#or switch 2 (if it is the second switch oyu found)
				else:
					switches[1] = j+1;
					print("Light # " + str(light+1) + " is connected to switch #" + str(switches[0]) + " and switch #" + str(switches[1]));
					return switches;
	return None;


#this function takes in the conditions of the lights, and which switches are connected to which lights
#and creates an expression that can be solved by 2SAT in poly time
def get_expression(num_lights, num_switches, switch_matrix, lights):
	#walk through the lights. 
	expression = [];
	for i in range(num_lights):
		#expr_len = 0;
		clause1 = [];
		clause2 = [];

		switches = get_switches(switch_matrix, num_switches, i);
		#if (switches == None):
			#print("could not find switches for light_bulb #" + str(i+1));
			#return None;

		#If it is on you want it to be off (odd number of toggles). 
		#if the light is on you want to toggle 1 of the lights
		#(-s1 and s2) or (s1 and -s2)
		#put into 2SAT form: (-s1 or -s2) and (s1 or s2)
		if (lights[i] == 1): #it is on
			clause1 = [NOT(switches[0]), NOT(switches[1])];
			clause2 = [switches[0], switches[1]];

		#If the light is off you want to keep it off (even number of toggles).
		#if the light is off you want to toggle 0 of the lights or both
		#(-s1 and -s2) or (s1 and s2) 
		#put into 2SAT form: (-s1 or s2) and (s1 or -s2)
		if (lights[i] == 0): #it is off
			clause1 = [NOT(switches[0]), switches[1]];
			clause2 = [switches[0], NOT(switches[1])];

		expression.append(clause1);
		expression.append(clause2); 

	#print(expression);
	return expression;


		#look at (find) the 2 switches it is connected to.
		# s1 = -1;
		# s2 = -1;
		# #search every element in the switch matrix
		# for j in range(num_switches):
		# 	for k in range(len(switch_matrix[j])):
		# 		#if you find that a switch is connected to the lightbulb i
		# 		if (switch_matrix[j][k] != None and switch_matrix[j][k] == i+1):
		# 			#set it as either switch 1 (if it is the first switch you found)
		# 			if(s1 == -1):
		# 				s1 = j;
		# 			#or switch 2 (if it is the second switch oyu found)
		# 			else:
		# 				s2 = j;

#this function will get all of the data from the file and give it to a function to get the
#expression readble by 2SAT

def build_data():

	num_lights = 0;
	num_switches = 0;
	lights = []; #on/off of lights
	switch_matrix = []; #= [[None for i in range(num_lights)] for j in range(num_switches)]; #which lights the switches are connected to
	#expected = False;

	#this is the input file
	input_info = open("input.txt", "r");

	#the first line will have the number of switches 
	#followed by the number of lights
	text = input_info.readline();
	array = text.split(',');
	num_switches = int(array[0]);
	num_lights = int(array[1]);

	#the second line will have whether each light is on or off
	text = input_info.readline();
	lights = text.split(',');
	for i in range(num_lights):
		lights[i] = int(lights[i]);
	#print(lights);

	#the next information is which lightbulbs each switch is connected to
	for i in range(num_switches):
		text = input_info.readline();
		switch_matrix.append(text.split(','));
		for j in range(len(switch_matrix[i])):
			switch_matrix[i][j] = int(switch_matrix[i][j]);
		#print(switch_matrix[i]);

	input_info.close();

	lights_expression = get_expression(num_lights, num_switches, switch_matrix, lights);
	#print(lights_expression);

	return satisfiable(lights_expression);

def main():

	satisfiable = build_data();

	output_info = open("output.txt", "w");
	if(satisfiable):
		print("All lights can be turned off");
		output_info.write("yes");
	else:
		print("Not all lights can be turned off");
		output_info.write("no");

	output_info.close();
	



main();