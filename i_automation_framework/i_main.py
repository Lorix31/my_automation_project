# from fuzzywuzzy import fuzz
#
# from i_automation_framework.i_utile import validation, get_input_data, test_driven
#
#
# def test_case(input_data, expected_data):
#     similarity = fuzz.partial_ratio(input_data, expected_data)    #install and import package fuzz de la beculetul rosu
#     validation(similarity) #import validation de la beculetul rosu  =>from i_automation_framework.i_utile import validation
#     return similarity
# # main + enter sau tab =>shortcut completeaza automat if __name__ == '__main__':
# if __name__ == '__main__':
#     data = get_input_data("C:/Users/Loredana/Documents/GitHub/my_automation_project/i_automation_framework/i_input_data.json") #am dat import pt get_input_data
#     print(data)
#     output = test_driven(data, test_case) #import test driven
#     print(output)



#cod gabi
from fuzzywuzzy import fuzz

from i_automation_framework.i_utile import validation, get_input_data, test_driven


def test_case(input_data, expected_data):
    similarity = fuzz.partial_ratio(input_data, expected_data)
    validation(similarity)
    return similarity


if __name__ == '__main__':
    data = get_input_data("C:/Users/Loredana/Documents/GitHub/my_automation_project/i_automation_framework/i_input_data.json")
    print(data)
    output = test_driven(data, test_case)  # nu apelam functia, ci doar ii returnam numele pentru a putea fi folosita mai departe
    print(output)