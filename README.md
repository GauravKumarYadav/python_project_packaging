# FastAPI Project

**Description:** This FastAPI project is designed to facilitate the insertion of data into a Hive table efficiently.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)

## Overview

FastAPI Project is a robust solution for inserting data into a Hive table. Leveraging FastAPI, a modern and high-performance web framework for building APIs, this project provides a seamless and efficient way to interact with Hive.

## Prerequisites

Before you get started, ensure you have the following prerequisites:

- **Python 3.8 or later**: If not installed, download and install Python from [python.org](https://www.python.org/downloads/) or through your package manager.

- **Poetry**: This project uses Poetry for managing dependencies. If you don't have Poetry installed, you can install it following the instructions [here](https://python-poetry.org/docs/).

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/fastapiproject.git
   ```

2. Change to the project directory:

   ```bash
   cd fastapiproject
   ```

3. Install project dependencies using Poetry:

   ```bash
   poetry install
   ```

## Usage

To run the FastAPI application, execute the following command:

```bash
poetry run uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload
```

You can access the API at http://localhost:8000. Make sure to modify the host and port as needed.

## API Endpoints

The FastAPI project provides the following API endpoints:

- **POST /insert_into**: Insert data into the Hive table. You can send a JSON payload with the data to be inserted.

Example request:

```bash
{
    "data": "your_data_here"
}
```

- **GET /status**: Check the status of the FastAPI server.

## Testing

To run the tests, execute the following command:

```bash
poetry run pytest --cov=src tests/
```

## Contributing

Contributions are welcome!
