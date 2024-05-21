# Policy_Search Python Script

The `TalkDocument` Python script is designed to process and interact with documents, embeddings, and question-answering chains. It provides functionalities for loading documents, splitting them into chunks, obtaining embeddings, creating vector storage, performing similarity searches, and answering questions using a question-answering chain.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Examples](#examples)
- [License](#license)

## Features

- Load documents from various sources (TXT, PDF, WEB).
- Split documents into chunks based on characters or tokens.
- Obtain embeddings using Hugging Face or OpenAI models.
- Create vector storage using FAISS, Chroma, or SVM.
- Perform similarity searches for relevant documents.
- Answer questions using a question-answering chain.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the `TalkDocument` script, instantiate the `TalkDocument` class and utilize its methods. See the examples section below for sample usage scenarios.

## Configuration

The script includes several constants and configuration options. Update the relevant parameters within the script to customize its behavior:

- `DS_TYPE_LIST`: List of supported data source types (e.g., ["WEB", "PDF", "TXT"]).
- `SPLIT_TYPE_LIST`: List of supported document splitting types (e.g., ["CHARACTER", "TOKEN"]).
- `EMBEDDING_TYPE_LIST`: List of supported embedding types (e.g., ["HF", "OPENAI"]).
- `VECTORSTORE_TYPE_LIST`: List of supported vector storage types (e.g., ["FAISS", "CHROMA", "SVM"]).
- `REPO_ID_DEFAULT`: Default repository ID for Hugging Face models.
- `CHAIN_TYPE_LIST`: List of supported question-answering chain types (e.g., ["stuff", "map_reduce", "map_rerank", "refine"]).

## Documentation

For detailed information on each method and its parameters, refer to the docstrings within the script. Additional documentation can be found [here](link_to_documentation).

## Examples

Here are some usage examples:

```python
# Instantiate TalkDocument
obj = TalkDocument(HF_API_TOKEN="your_hugging_face_api_token", data_source_path=["/path/to/document.txt"])

# Load document, split, and create vector storage
obj.create_db_document()

# Ask questions and obtain answers
question = "What is the main concept of this document?"
response = obj.do_question(question=question, language="ENGLISH")
print(response)

## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

