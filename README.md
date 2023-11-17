# Ollama Note-Taker App
## Overview
The Ollama Note-Taker App is a simple yet powerful application that leverages the Ollama API hosted locally to prompt queries to a Large Language Model (LLM). This application aims to assist users in making notes based on their queries, utilizing the capabilities of advanced language models to generate informative, relevant content.

## Features
Integration with Ollama API: The app seamlessly integrates with the Ollama API hosted locally, allowing users to leverage the power of the language model for generating content.

Query-based Note-Taking: Users can input queries into the app, and the underlying Large Language Model will generate informative notes based on those queries and they will be saved in /notes directory.

Local Hosting: The Ollama API is hosted locally, ensuring that the application is secure, and responsive.

## Use cases and pros
### Batch Query Processing Scenario:
As a user, I often find myself with multiple queries or ideas that I want to transform into notes without the risk of forgetting any important points.

The user opens the Ollama Note-Taker App.
Instead of entering a single query, the user can input a list of queries or ideas at once in a batch.
### Batch Processing:

The app processes each query in the batch sequentially.
For each query, the app generates a note based on the input, utilizing the Ollama API.

After the batch processing is complete, the user can review all the generated notes.
The user has the option to save the entire batch of notes or individual notes.

Users can efficiently capture a stream of thoughts or questions without the fear of forgetting any important information.

## Cons

Longer list of queries longer the time of executing the program.

# How to use

## Install Ollama
```bash
curl https://ollama.ai/install.sh | sh
```
## Pull mistral model from Ollama
```bash
ollama pull mistral
```
## Start Ollama
```bash
./ollama serve
```
## Fill the queries you want to prompt in queries.txt file (example)
```
Write an essay about Roman Empire
Create notes about Roman Empire
Create notes about Julius Caesar
```
## Install Python (Ubuntu)
```
sudo apt install python3
```
## Install requirements
```
pip install -r requirements.txt
```
## Run main.py
```
python3 main.py
```