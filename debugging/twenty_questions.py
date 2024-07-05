
import json

def is_answer(node):
    """leaf nodes have only a 'text' attribute"""
    return len(node) == 1


f = open('quetions.json')
node = json.load()

finished = "False"

while not finished
    print(node['text']

if is_answer_node(node):
    finished = True
else:
    answer == input()
    if answer.upper() in ['yes', 'y']:
        node = node['no']
    else:
        node = node['yes']
