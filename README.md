This is a personal project.

# Chronicle SecOps MCP Server
[![smithery badge](https://smithery.ai/badge/@emeryray2002/mcp-secops-v3)](https://smithery.ai/server/@emeryray2002/mcp-secops-v3)

This is an MCP (Model Context Protocol) server for interacting with Google's Chronicle Security Operations suite.
[MCP Info](https://modelcontextprotocol.io/introduction)
## Installing in Claude Desktop

To use this MCP server with Claude Desktop:

1. Install Claude Desktop 

2. Open Claude Desktop and select "Settings" from the Claude menu

3. Click on "Developer" in the lefthand bar, then click "Edit Config"

4. Update your `claude_desktop_config.json` with the following configuration (replace paths with your actual paths):

```json
{
  "mcpServers": {
    "secops-mcp": {
      "command": "/path/to/your/uv",
      "args": [
        "--directory",
        "/path/to/your/mcp-secops-v3",
        "run",
        "secops_mcp.py"
      ],
      "env": {
        "CHRONICLE_PROJECT_ID": "your-google-cloud-project-id",
        "CHRONICLE_CUSTOMER_ID": "your-chronicle-customer-id",
        "CHRONICLE_REGION": "us"
      }
    }
  }
}
```

5. Make sure to update:
   - The path to `uv` (use `which uv` to find it)
   - The directory path to where this repository is cloned
   - Your Chronicle credentials (project ID, customer ID, and region)

6. Save the file and restart Claude Desktop

7. You should now see the hammer icon in the Claude Desktop interface, indicating the MCP server is active

## Features

### Security Tools
- `search_security_events`: Search for security events in Chronicle with customizable queries
- `get_security_alerts`: Get security alerts from Chronicle
- `lookup_entity`: Look up information about an entity (IP, domain, hash)
- `list_security_rules`: List security detection rules from Chronicle
- `get_ioc_matches`: Get Indicators of Compromise (IoCs) matches from Chronicle

## Installation

### Installing via Smithery

To install mcp-secops-v3 for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@emeryray2002/mcp-secops-v3):

```bash
npx -y @smithery/cli install @emeryray2002/mcp-secops-v3 --client claude
```

### Manual Installation
1. Install the package:

```bash
pip install -e .
```

2. Set up your environment variables:

```bash
export CHRONICLE_PROJECT_ID="your-google-cloud-project-id"
export CHRONICLE_CUSTOMER_ID="your-chronicle-customer-id"
export CHRONICLE_REGION="us"  # or your region
```

## Requirements

- Python 3.11+
- A Google Cloud account with Chronicle Security Operations enabled
- Proper authentication configured

## Usage

### Running the MCP Server

```bash
python main.py
```

### API Capabilities

The MCP server provides the following capabilities:

1. **Search Security Events**: Search for security events in Chronicle
2. **Get Security Alerts**: Retrieve security alerts
3. **Lookup Entity**: Look up entity information (IP, domain, hash, etc.)
4. **List Security Rules**: List detection rules
5. **Get IoC Matches**: Get Indicators of Compromise matches

### Example

See `example.py` for a complete example of using the MCP server.

## Authentication

The server uses Google's authentication. Make sure you have either:

1. Set up Application Default Credentials (ADC)
2. Set a GOOGLE_APPLICATION_CREDENTIALS environment variable
3. Used `gcloud auth application-default login`

## License

Apache 2.0

## Development

The project is structured as follows:

- `secops_mcp.py`: Main MCP server implementation
- `example.py`: Example usage of the MCP server
