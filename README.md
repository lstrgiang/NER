## Introduction

- The current application consist of 3 independent servers:
   - CoreNLP Server: pre-trained server to handle NLP input and return NER/word
   segmenter for English language
   - VnCore server: pre-trained server to handle NLP input and return NER/word
   segmenter for Vietnamese language
   - Main website application: An simple web application that get result
   from both NLP server and summarize the probability of NER for given text data

## Prerequisite
- Python 3.7
- JDK 1.8
- Virtualenv (optional - installed with Python)

## Prepare python module
- Use virtualenv to create venv folder and activate the environment (optional) 
```
virtualenv --python=python3 venv
```
activate the environment (optional)
```
source venv/bin/activate
```

- Install packages: 
```
pip install -r requirements.txt
```

## Prepare packages 
- Go to `packages/corenlp/` directory and execute `setup.sh`
- Go to `packages/vncore/` directory and execute `setup.sh`

## Start CoreNLP Server 

- Go to `packages` directory
- Unzip `corenlp.zip` file
- Go the `corenlp` directory
- Start entrypoint.sh: `./entrypoint.sh`


## Start VNCore Server
- Go to `packages` directory
- Unzip `vncore.zip` file
- Go the `vncore` directory
- Start entrypoint.sh: `./entrypoint.sh`


## Start main website application
- At the root directory, use make file to start the application:
```
make server/run
```


## Test the application
- Access `localhost:8000` from the browser
- Input text data into the box and click submit
- View and check the result
