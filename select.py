######################################################################################
#
#	Author: Ayush Choudhury, Anand, Munisha
#
#	Title: Group Assignment 1
#
#	Description: This program reads in one file giving values
#		for m, n, and k. Then the program reads in m text
#		files each with n binary numbers, then outputs the kth
#		smallest value among all the numbers in all the files
#		in m^2log^2(n) time.
#
#######################################################################################

#############################################################################################################
#
#	Name: binary_search_max()
#
#	Description: This function calculates how many numbers are 
#		smaller than or equal to an inputed number (value) in an already sorted 
#		array
#
#	Preconditions: Each row of the 2d array is sorted
#
#	parameters: m, is the soecific row you are looking at
#				first is where in the array you start
#				last is where in the array you stop
#				halfway is the midpoint of the section of the array you are looking for
#				Data is the 2d array
#				value is the inputed number you are counting how many numbers are smaller than it 
#
###############################################################################################################

def binary_search_max (n, m, first, last, halfway, Data, value):

	halfway = int((last + first)/2);
	#print(str(halfway) + ", " + str(Data[m][halfway]));

	if (Data[m][halfway] == value):

		while (halfway <= n and Data[m][halfway] == value):
			
			halfway = halfway + 1;
		
		return halfway;
	
	if (not(first > last)):

		if (Data[m][halfway] > value):		#value is in first half

			last = halfway - 1;
			#halfway = (first + last)/2;
			return binary_search_max(n, m, first, last, halfway, Data, value);

		if (Data[m][halfway] < value):		#value is in last half

			first = halfway + 1;
			#halfway = (first + last)/2;
			return binary_search_max(n, m, first, last, halfway, Data, value);
			
	if (Data[m][halfway] < value):
		
		return halfway+1; 
	
	else:

		return halfway;

def binary_search_min (n, m, first, last, halfway, Data, value):

	halfway = int((last + first)/2);
	#print(str(halfway) + ", " + str(Data[m][halfway]));

	if (Data[m][halfway] == value):
		#print("value found");
		while (halfway > 0 and Data[m][halfway - 1] == value):
			
			halfway = halfway - 1;
		
		return halfway;
	
	if (not(first > last)):

		if (Data[m][halfway] > value):		#value is in first half

			last = halfway - 1;
			#halfway = (first + last)/2;
			return binary_search_min(n, m, first, last, halfway, Data, value);

		if (Data[m][halfway] < value):		#value is in last half

			first = halfway + 1;
			#halfway = (first + last)/2;
			return binary_search_min(n, m, first, last, halfway, Data, value);
	
	#print("value not found");	
	if (Data[m][halfway] < value):
		
		return halfway+1; 
	
	else:

		return halfway;


# def binary_search_min(m, first, last, halfway, Data, value):

# 	halfway = (last + first)/2;

# 	if (Data[m][halfway] == value):

# 		while (Data[m][halfway] == value and halfway > 0):
			
# 			halfway = halfway - 1;
		
# 		return halfway;
	
# 	if (halfway != last):

# 		if (Data[m][halfway] > value):		#value is in first half

# 			last = halfway-1;
# 			#halfway = (first + last)/2;
# 			return binary_search_min(m, first, last, halfway, Data, value);

# 		if (Data[m][halfway] < value):		#value is in last half

# 			first = halfway + 1;
# 			#halfway = (first + last)/2;
# 			return binary_search_min(m, first, last, halfway, Data, value);
			
# 	if (Data[m][halfway] < value):
		
# 		return halfway+1; 
	
# 	else:

# 		return halfway;


def get_kval(m, n, k, Data, value):

	k_min = 0;
	k_max = 0;
	
	#print("value: " + str(value));
	for i in range(m):
		k_min = k_min + binary_search_min (n, i, 0, n, n/2, Data, value);
		k_max = k_max + binary_search_max (n, i, 0, n, n/2, Data, value);
		#print("k_min: " + str(k_min));
		#print("k_max: " + str(k_max));

	#print("value: " + str(value) + ", k_min: " + str(k_min) + ", k_max: " + str(k_max));

	if(k_min > k):
		return k_min+1;
	elif(k_max < k):
		return k_max;
	else:
		return k;


def kth_in_arr(m, m_value, n, k, Data, first, last, halfway):

	halfway = int((first+last)/2);

	#print("m: " + str(m) + " halfway: " + str(halfway));
	

	k_value = get_kval(m, n, k, Data, Data[m_value][halfway]);
	

	#if(halfway >= 0 and halfway <= n):
	#print(str(Data[m_value][halfway]) + ", k_value: " + str(k_value));
	

	if (k_value == k):

		return Data[m_value][halfway]; #write kval to file


	#print("first: " + str(first) + ", last: " + str(last));
	if (not(first > last)):

		if(k_value < k):

			first = halfway + 1;
			return kth_in_arr(m, m_value, n, k, Data, first, last, halfway);

		elif (k_value > k):

			last = halfway - 1;
			return kth_in_arr(m, m_value, n, k, Data, first, last, halfway);

	else:
		return -1;	#index of kth smallest element is not in array


def find_kth(m, n, k, Data):

	for i in range(m):	#walk through each row

		kth_smallest = kth_in_arr(m, i, n, k, Data, 0, n, n/2);
		if(kth_smallest >= 0): #if the row contains the kth smallest element
			return kth_smallest;	#you are done

def build_Data():
	input_info = open("input.txt", "r");
	text = input_info.readline();
	array = text.split(',');
	m = int(array[0]);
	n = int(array[1]);
	k = int(array[2]);
	input_info.close();
	print(array);

	Data = [[ ' ' for i in range(n) ] for j in range(m)];

	for i in range(1, m+1):
		input_data = open(str(i) + ".dat", "rb");
		
		for j in range(n):
			bin_value = input_data.read(4);
			dec_value = int.from_bytes(bin_value, byteorder='big');
			#print(dec_value);
			Data[i-1][j] = dec_value;
		input_data.close();
	print(Data);
	kth_smallest_num = find_kth(m, n-1, k, Data);
	print(kth_smallest_num);

	output_kth = open("output.txt", "w");
	#output_kth.write("Hello There!");
	output_kth.write(str(kth_smallest_num));
	output_kth.close();


	#value = int(new_text);
	#Data = new_text.read(1);
	#print(Data);


def main ():
	
	build_Data();
	# m = 3;
	# n = 10;
	# k = 29;

	# Data = [[1, 1, 2, 2, 2, 3, 3, 3, 4, 4], 
	# 		[1, 1, 1, 1, 1, 2, 2, 4, 4, 5], 
	# 		[1, 3, 3, 3, 3, 3, 3, 3, 3, 6]];
	
	#Data = [[' ' for i in range(m) ] for j in range(n)];
	#kth_snallest_num = find_kth(m, n-1, k, Data);
	#print(kth_snallest_num);

main();