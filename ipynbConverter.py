import json
from ipynbConverterContent import data

dirname = 'ex3/'
filename = 'Jean-Loup.ipynb'

# Writing the JSON content to an .ipynb file
with open(dirname+filename, 'w') as file:
    json.dump(data, file)

print(f"Notebook saved successfully as {filename}")