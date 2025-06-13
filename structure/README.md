# GPT-CLI

GPT-CLI is a simple command-line interface tool designed to provide quick access to AI-powered responses directly from your terminal. It utilizes any supported AI API key specified in the `config.yaml` file to act as a GPT-like assistant.

## Features

- **Terminal-based interaction**: Get AI responses without leaving your terminal.
- **Configurable API key**: Use any supported AI API by specifying the key in `config.yaml`.
- **Lightweight and fast**: Ideal for developers and power users who need quick access to AI assistance.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/playfairs/gpt-cli.git
    cd gpt-cli
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure your API key:
    - Open `config.yaml`.
    - Add your API key and default API

## Usage

Run the CLI tool:
```bash
python gpt-cli.py
```

Start typing your queries, and the tool will provide AI-generated responses.

## Configuration

The `config.yaml` file should include:
```yaml
api:
  api_key: "your-pi-key-here"
  model: "your-model-preference"
  endpoint: "https://api.your-api-choice.com/v1/chat/completions"
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Disclaimer

Ensure your API key is kept secure and do not share it publicly.