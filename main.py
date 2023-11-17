import requests
import json

queries = open('queries.txt', 'r').read().split('\n')

headers = {
    'Content-Type': 'application/json',
}

for query in queries:
    data = {
            "model": "mistral",
            "stream": False,
            "prompt": query,
            }

    response = requests.post('http://localhost:11434/api/generate', headers=headers, data=json.dumps(data))

    if response.status_code == 200:
            response_text = response.text
            data = json.loads(response_text)
            actual_response = data["response"]
            file = open(f"notes/{query}.txt", "w")
            file.write(actual_response)
            print("Processed query, ", query)
    else:
        print("Error:", response.status_code, response.text)