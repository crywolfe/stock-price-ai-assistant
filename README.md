# Stock Price AI Assistant

This project is a financial assistant that uses AI to fetch and analyze stock prices and sector information. It leverages the `pydantic_ai` library for AI agents and `yfinance` for financial data. The user interface is built using `gradio`.

## Table of Contents

- [Stock Price AI Assistant](#stock-price-ai-assistant)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Code Structure](#code-structure)
    - [`app.py`](#apppy)
    - [`requirements.txt`](#requirementstxt)
  - [Dependencies](#dependencies)
  - [License](#license)

## Overview

The Stock Price AI Assistant is designed to provide users with up-to-date financial information about stocks and their respective sectors. It uses two AI agents: one for fetching stock price information and another for analyzing sector information.

## Features

- **Stock Price Information**: Fetches current stock prices, low and high prices, volume, and sentiment.
- **Sector Analysis**: Provides detailed information about the sector, including growth rate, revenue, key statistics, and companies within the sector.
- **User Interface**: Built with `gradio`, allowing users to interact with the assistant through a web interface.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/crywolfe/stock-price-ai-assistant.git
   cd stock-price-ai-assistant
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set the environment variable**:
   ```bash
   export GROQ_API_KEY=your_groq_api_key
   ```

## Usage

1. **Run the application**:
   ```bash
   python app.py
   ```

2. **Interact with the assistant**:
   - Open the provided URL in your web browser.
   - Enter a stock symbol or name in the input box.
   - Click "Submit" to get the stock price and sector information.

## Code Structure

### `app.py`

- **Imports**: Necessary libraries and modules are imported at the beginning.
- **Data Models**: `StockPriceResult` and `SectorResult` classes define the structure of the data returned by the AI agents.
- **AI Agents**: `stock_info_agent` and `sector_agent` are initialized with specific system prompts.
- **Tools**: `get_stock_info_async` and `get_sector_info` functions are defined as tools for the AI agents.
- **Main Function**: `get_stock_info` function orchestrates the sequence of operations, first fetching stock information and then sector information.
- **Gradio Interface**: A `gradio` interface is created to allow user interaction.

### `requirements.txt`

- Lists all the dependencies required to run the application.

## Dependencies

- `pydantic_ai`: For AI agents.
- `pydantic`: For data validation.
- `yfinance`: For fetching financial data.
- `gradio`: For creating the user interface.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.