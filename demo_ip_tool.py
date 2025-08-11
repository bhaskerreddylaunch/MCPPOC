#!/usr/bin/env python3
"""
Demonstration script for the get_ip_info MCP tool.
Shows how to use the tool and provides examples of expected output.
"""

import json
import subprocess
import sys
import time
from typing import Dict, Any

def create_mcp_request(tool_name: str, arguments: Dict[str, Any] = None) -> Dict[str, Any]:
    """Create a properly formatted MCP request."""
    return {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments or {}
        }
    }

def demonstrate_tool_usage():
    """Demonstrate how to use the get_ip_info tool via MCP."""
    print("🚀 MCP Server get_ip_info Tool Demonstration")
    print("=" * 60)
    
    print("\n1. 📋 Tool Information:")
    print("   Name: get_ip_info")
    print("   Description: Get current public IP address and location information")
    print("   Parameters: None")
    
    print("\n2. 📦 MCP Request Format:")
    request = create_mcp_request("get_ip_info")
    print("   " + json.dumps(request, indent=2).replace('\n', '\n   '))
    
    print("\n3. 🌐 What the tool does:")
    print("   • Queries multiple IP APIs (ipify.org, httpbin.org, jsonip.com)")
    print("   • Gets location data from ip-api.com") 
    print("   • Returns formatted information including:")
    print("     - Public IP address")
    print("     - City")
    print("     - Region/State") 
    print("     - Country")
    print("     - ISP information")
    
    print("\n4. ✅ Expected Output Format:")
    print("   IP: 203.0.113.42")
    print("   City: New York")
    print("   Region: New York")
    print("   Country: United States")
    print("   ISP: Example Internet Provider")
    
    print("\n5. 🛡️ Error Handling:")
    print("   • Graceful fallback between multiple API endpoints")
    print("   • Timeout handling (10 seconds per request)")
    print("   • Returns basic IP if location data unavailable")
    print("   • Clear error messages if all APIs fail")

def simulate_tool_response():
    """Simulate what a successful tool response would look like."""
    print("\n6. 🎭 Simulated Successful Response:")
    print("   " + "─" * 40)
    
    # Simulate typical responses
    examples = [
        {
            "scenario": "Full response with location",
            "response": "IP: 198.51.100.123\nCity: San Francisco\nRegion: California\nCountry: United States\nISP: Example Broadband LLC"
        },
        {
            "scenario": "Basic IP only (location unavailable)",
            "response": "IP: 203.0.113.89"
        },
        {
            "scenario": "Network error",
            "response": "Error: Unable to fetch IP information from any API"
        }
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n   Example {i}: {example['scenario']}")
        print("   Response:")
        for line in example['response'].split('\n'):
            print(f"     {line}")

def show_integration_examples():
    """Show examples of how to integrate with the MCP server."""
    print("\n7. 🔌 Integration Examples:")
    print("   " + "─" * 40)
    
    print("\n   A. Using with MCP Client:")
    print("   ```python")
    print("   import asyncio")
    print("   from mcp import ClientSession")
    print("   ")
    print("   async def get_ip():")
    print("       async with ClientSession('stdio', ['python', 'mcp_server.py']) as session:")
    print("           result = await session.call_tool('get_ip_info')")
    print("           print(result.content[0].text)")
    print("   ```")
    
    print("\n   B. Using with VS Code Copilot MCP:")
    print("   - Configure in .vscode/mcp.json")
    print("   - Ask Copilot: 'What is my current IP address?'")
    print("   - Copilot will use the get_ip_info tool automatically")

def main():
    """Main demonstration function."""
    demonstrate_tool_usage()
    simulate_tool_response()
    show_integration_examples()
    
    print("\n" + "=" * 60)
    print("🎯 Summary:")
    print("The get_ip_info tool is ready to use and provides comprehensive")
    print("IP address and location information through the MCP protocol.")
    print("It can be called by any MCP-compatible client or AI assistant.")
    print("=" * 60)

if __name__ == "__main__":
    main()