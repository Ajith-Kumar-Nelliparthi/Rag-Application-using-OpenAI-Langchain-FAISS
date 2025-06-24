# RAG Project

A modular, production-ready Retrieval-Augmented Generation (RAG) framework for building, experimenting, and deploying advanced LLM-powered applications. This project is designed for research and practical use, supporting custom data ingestion, embeddings, vector stores, and LLM pipelines.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
- [Development](#development)
- [Testing](#testing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Features

- **Modular Architecture**: Easily extend or swap components (embeddings, vector stores, LLMs, pipelines).
- **Configurable**: Centralized settings for environment and model configuration.
- **Data Ingestion**: Flexible ingestion pipelines for various data sources.
- **Embeddings**: Pluggable embedding models for document representation.
- **Vector Store**: Efficient similarity search and retrieval.
- **LLM Integration**: Seamless integration with large language models.
- **Jupyter Notebooks**: For research, prototyping, and experimentation.
- **Production-Ready**: Structured for deployment and scaling.

---

## Project Structure

```
.
├── .env                      # Environment variables
├── .gitignore
├── .python-version
├── LICENSE
├── pyproject.toml            # Project metadata and dependencies
├── README.md
├── uv.lock                   # Dependency lock file
├── create_project_structure.py
├── notebook/
│   └── research.ipynb        # Jupyter notebook for experiments
└── rag_project/
    ├── app/
    │   ├── __init__.py
    │   └── main.py           # Main application entry point
    ├── config/
    │   ├── __init__.py
    │   └── settings.py       # Configuration management
    ├── data/                 # Data storage (raw, processed, etc.)
    └── src/
        ├── __init__.py
        ├── embeddings/       # Embedding models and utilities
        ├── ingestion/        # Data ingestion pipelines
        ├── llm/              # LLM integration and utilities
        ├── pipeline/         # RAG pipeline orchestration
        └── vectorstore/      # Vector database and retrieval logic
```

---

## Getting Started

### Prerequisites

- Python 3.11+
- [pip](https://pip.pypa.io/en/stable/)
- (Recommended) [virtualenv](https://virtualenv.pypa.io/en/latest/) or [venv](https://docs.python.org/3/library/venv.html)

### Installation

1. **Clone the repository:**
   ```sh
   git clone "https://github.com/Ajith-Kumar-Nelliparthi/Rag-Application-using-OpenAI-Langchain-FAISS.git"
   cd project
   ```

2. **Set up a virtual environment:**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   # or, if using pyproject.toml:
   pip install .
   ```

4. **Configure environment variables:**
   - Copy `.env.example` to `.env` and update as needed.

---

## Configuration

All configuration is managed in [`rag_project/config/settings.py`](rag_project/config/settings.py).  
You can set environment variables in the `.env` file for secrets, API keys, and runtime options.

---

## Usage

### Running the Application

```sh
python -m rag_project.app.main
```

### Running Notebooks

Open [notebook/research.ipynb](notebook/research.ipynb) in Jupyter Lab or Notebook for experimentation.

---

## Development

- Source code is organized under [`rag_project/src/`](rag_project/src/).
- Add new modules or extend existing ones for custom embeddings, ingestion, or LLMs.
- Use the provided project structure script (`create_project_structure.py`) to scaffold new components.

---

## Testing

- Add your tests in a `tests/` directory (not included by default).
- Use `pytest` or your preferred test runner.
- Example:
  ```sh
  pytest
  ```

---

## License

This project is licensed under the GNU General Public License v3.0.  
See [LICENSE](LICENSE) for details.

---

## Acknowledgements

- Built with inspiration from open-source RAG frameworks and the broader LLM community.
- See [LICENSE](LICENSE) for third-party notices.
