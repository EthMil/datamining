import copy
import sys

def parse_file(f):
	training_set = open(f)
	input_file = training_set.readlines()
	output = []
	for i in input_file:
		temp = i.split(",")
		output.extend([temp])
	return output

def condition_table(training_set):
        # create a table that contains all of the values associated with the car's condition
        # as well as a count to keep track of how many of each object has been found.
        table = {
                "vgood":{"count":0, "buying":{"vhigh":0,"high":0,"med":0,"low":0}, "maint":{"vhigh":0,"high":0,"med":0,"low":0}, "doors":{"2":0,"3":0,"4":0,"5more":0}, "persons":{"2":0,"4":0,"more":0}, "lug_boot":{"small":0,"med":0,"big":0}, "safety":{"low":0,"med":0,"high":0}},

                "good":{"count":0, "buying":{"vhigh":0,"high":0,"med":0,"low":0}, "maint":{"vhigh":0,"high":0,"med":0,"low":0},
                        "doors":{"2":0,"3":0,"4":0,"5more":0},"persons":{"2":0,"4":0,"more":0},"lug_boot":{"small":0,"med":0,"big":0},
                        "safety":{"low":0,"med":0,"high":0}},

                "acc":{"count":0,"buying":{"vhigh":0,"high":0,"med":0,"low":0},"maint":{"vhigh":0,"high":0,"med":0,"low":0},"doors":{"2":0,"3":0,"4":0,"5more":0},"persons":{"2":0,"4":0,"more":0},"lug_boot":{"small":0,"med":0,"big":0},"safety":{"low":0,"med":0,"high":0}
                },

                "unacc":{"count":0,"buying":{"vhigh":0,"high":0,"med":0,"low":0},"maint":{"vhigh":0,"high":0,"med":0,"low":0},"doors":{"2":0,"3":0,"4":0,"5more":0},"persons":{"2":0,"4":0,"more":0},"lug_boot":{"small":0,"med":0,"big":0},"safety":{"low":0,"med":0,"high":0}}
        }
        for i in training_set:	# increment attribute values for all entries
                category = i[-1].rstrip()
                table[category]['count'] += 1
                for k, j in enumerate(i):
                        if k == 0:
                                table[category]["buying"][j] += 1
                        elif k == 1:
                                table[category]["maint"][j] += 1
                        elif k == 2:
                                table[category]["doors"][j] += 1
                        elif k == 3:
                                table[category]["persons"][j] += 1
                        elif k == 4:
                                table[category]["lug_boot"][j] += 1
                        elif k == 5:
                                table[category]["safety"][j] += 1

        return table


def frequency(table):
	number_of_entries = 0
	for i in table:
		number_of_entries += table[i]['count']
	
	for category in table:
		for attribute in table[category]:
			if attribute != 'count':
				for value in table[category][attribute]:
					table[category][attribute][value] /= float(table[category]['count'])
	for category in table:
		table[category]['count'] /= float(number_of_entries)
	return table



def get_accuracy(frequency_table, input_set):
	match_probability = 0.0
	no_match_probability = 0.0
	testing_set = copy.deepcopy(input_set)
	for input in testing_set:
		test_category = input[-1].rstrip()
		categories = ["unacc","acc","good","vgood"]
		category_odds = {"unacc":0,"acc":0,"good":0,"vgood":0}
		for c in categories:
			input[-1] = c
                        category = input[-1]
                        a = ["buying","maint","doors","persons","lug_boot","safety"]
                        odds = 1
                        for i in range(0,len(input)-1):
                                temp = frequency_table[category][a[i]][input[i]]
                                odds = odds * temp
                        category_odds[c] = odds
                        prediction = max(category_odds, key=lambda i: category_odds[i])
                if prediction == test_category:
                        match_probability += 1
		else:
			no_match_probability += 1
                accuracy = match_probability/(match_probability+no_match_probability)
        return accuracy
        
def classify(training, testing):
	if type(training) == str:
		training_set = parse_file(training)
	else: 
		training_set = training
	if type(testing) == str:
			testing_set = parse_file(testing)
	else: 
		testing_set = testing
	table = condition_table(training_set)
	frequency_table = frequency(table)

	if __name__ == "__main__":
                for category in table:
                        print "Class = ",category 
                        for attribute in table[category]:
                                print "\t",attribute,"=", table[category][attribute]

	accuracy = get_accuracy(frequency_table, testing_set)
	return accuracy


if(len(sys.argv)==3):
	training_file = sys.argv[1]
	testing_file = sys.argv[2]
else:
	training_file = "carTraining.data"
	testing_file = "carTesting.data"
accuracy = classify(training_file,testing_file)
print "Accuracy:", accuracy
