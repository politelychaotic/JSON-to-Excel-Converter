import json, csv

#########################################################################################
# This program takes a JSON file and converts it into a Python dictionary,              #
# this dictionary is then iterated through with tests for each value's datatype         #
# such as Dict, List, or NOT List and NOT Dict. These tests tell the code how to        #
# iterate through the JSON data at each step. This is still a work in progress and      #
# currently is not using a Object Class which is the ultimate goal once it is out of    #
# the testing phase.                                                                    # 
#                                                                                       #
# Program by PolitelyChaotic                                                            #
#########################################################################################


'''
This is a test dictionary to demonstrate 
how the program takes a JSON object 
(which Python converts into a dict type),
and prints it out as delimited text.
'''
dictionary = {
    '5': '',
    "name": ['sathiyajith', 'hello'],
    "rollno": [{'name' : 'heading', 'link' : 'heading', 'something':['bob', 'dylan']}],
    "cgpa": {'b':'23', 'c': '24'},
    "phonenumber": "9976770500"
}

# Variable to hold the name of the JSON file
file_name = 'report'

# This adds the '.json' extension to the 
# filename and then opens it to read
json_file = open(file_name+'.json', 'r')

#convert JSON data from file to Python Dict
jsondata = json.load(json_file)

# Open a text file to save the data to
text_name = 'report_out'
textfile = open(text_name+'.txt', 'a+')

def iterate_json(data):
    '''
    This function takes a Dict Object and passes it 
    through a series of checks so that each Dict or List
    within the Original Dict Object is iterated through 
    and printed out in a delimited form that is much 
    more readable than pure JSON.
    
    :param data: Dict(JSON DATA)
    '''
    print('\n')
    for key,value in data.items():
        #print(type(key), type(value))
        if type(value) == dict:
            print(key + ':', end='')
            textfile.write(key + ':')
            for k,v in value.items():
                #print(type(v))
                if type(v) == list:
                    #print(type(v))
                    for el in range(len(v)):
                        print('\n\t{}'.format(value[el]) + '; ', end='')
                        textfile.write('\n\t{}'.format(value[el]) + '; ')
                else:
                    print('\n\t{} : {}'.format(k,v) + '; ', end='')
                    textfile.write('\n\t{} : {}'.format(k,v) + '; ')
            print('\n')
            textfile.write('\n')
        elif type(value) == list:
            print('\n' + key+': ', end='')
            textfile.write('\n' + key+': ')
            for element in range(len(value)):
                if type(value[element]) == dict:
                    for k,v in value[element].items():
                        if type(v) == list:
                            print('\n' + k+': ', end='')
                            textfile.write('\n' + k+': ')
                            for element in range(len(v)):
                                print('\n\t{}'.format(v[element]) + '; ', end='')
                                textfile.write('\n\t{}'.format(v[element]) + '; ')
                        else:
                            print('{} : {}'.format(k,v) + ';')
                            textfile.write('{} : {}'.format(k,v) + ';')
                    print('')
                    textfile.write(
                else:
                    print('\n\t{}'.format(value[element]) + '; ', end='')
                    textfile.write('\n\t{}'.format(value[element]) + '; ')
            print('')
            textfile.write('')
        else:
            print(key + ':' + str(value) + ';', end='')
            textfile.write(key + ':' + str(value) + ';')
    print('\n')
    textfile.write('\n')


#iterate_json(jsondata) #This takes the data from the json file and parses through it
iterate_json(dictionary) #Same as above, except this uses the test case of the dictionary which is how Python interprets JSON data
