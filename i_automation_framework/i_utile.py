import json

def get_input_data(test_file):
    json_file = open(test_file) # functia open ne permite sa deschidem fisiere
    return json.load(json_file)

def validation(similarity):
    if similarity > 90:
        print(f'test case passed - {similarity}')
    elif 80 < similarity < 90:
        print(f'Warning - {similarity}')
    else:
        print('Test case failed')

def test_driven(data, test_case):
    output = []
    for k,v in data.items():
        status = test_case(data[k]["input"], data[k]["expected"])
        output.append(dict(input = data[k]["input"], expected = data[k]["expected"], actual = status))
    return output