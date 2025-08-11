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
- `get_ip_info`: Get current public IP address and location information
- `get_weather`: Get current weather information for a city
- `divide_numbers`: Divide two numbers and return the result
- `get_server_info`: Get server system information including hostname and platform
- `multiply_numbers`: Multiply two numbers and return the result
- `get_system_status`: Get current system resource usage (CPU, memory, disk)

## Tool Details

### get_ip_info
**Description**: Get current public IP address and detailed location information

**Parameters**: None

**Returns**: Formatted string containing:
- Public IP address
- City
- Region/State
- Country
- ISP information

**Example Output**:
```
IP: 198.51.100.123
City: San Francisco
Region: California
Country: United States
ISP: Example Broadband LLC
```

**Features**:
- Queries multiple IP APIs for reliability (ipify.org, httpbin.org, jsonip.com)
- Gets location data from ip-api.com
- Graceful fallback between API endpoints
- 10-second timeout per request
- Returns basic IP if location data unavailable
- Clear error messages if all APIs fail

**Usage Examples**:
- In Copilot Chat: "What is my current IP address?"
- Direct MCP call: `{"method": "tools/call", "params": {"name": "get_ip_info"}}`

## VS Code Integration
The server is configured in your VS Code settings.json under `mcp.servers` section and should be discoverable by MCP-compatible extensions like Copilot MCP.
