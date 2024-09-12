import re

file_path = 'post_traces/pylint_post.txt'

def extract_score(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        
        match = re.search(r'Your code has been rated at (\d+\.\d+)/10', content)
        if match:
            score = match.group(1)
            return float(score)
        else:
            raise ValueError('Score not found in the file')

try:
    score = extract_score(file_path)
    print(f'Pylint Score: {score}')
except Exception as e:
    print(e)