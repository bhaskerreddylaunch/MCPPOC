# MCP Local Server Example

This is a proper Model Context Protocol (MCP) server implementation using Python and the official MCP SDK. It provides tools that can be integrated into MCP-compatible clients like GitHub Copilot Chat.

## Requirements
- Python 3.8+
- mcp

## Setup
1. Install dependencies:
   ```powershell
   pip install mcp
   ```
2. Run the server directly:
   ```powershell
   python mcp_server.py
   ```

## Available Tools
- `ping`: Check if the MCP server is alive
- `echo`: Echo back a message
- `add_numbers`: Add two numbers and return the result

## VS Code Integration
The server is configured in your VS Code settings.json under `mcp.servers` section and should be discoverable by MCP-compatible extensions like Copilot MCP.
