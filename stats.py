# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def get_n_words(str_f):
	return len(str_f.split())

def get_n_chars(str_f):
	dict_res = {}
	set_char = set(str_f.lower())
	for char in set_char:
		dict_res[char] = 0
	#print(set_char)
	for char in str_f.lower():
		dict_res[char] +=1
	return dict_res

def lists_dicts(dict_char):
	res_list = []
	for char in dict_char:
		#print(char)
		#print(dict_char[char])
		#print("\n")
		res_list.append({"char":char, "num":dict_char[char]})
	res_list.sort(reverse=True, key = sort_on)
	return res_list
