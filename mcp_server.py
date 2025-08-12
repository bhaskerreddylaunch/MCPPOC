#!/usr/bin/env python3
import requests
import json
from fastmcp import FastMCP

# Create a FastMCP server
mcp = FastMCP("local-mcp-server")


@mcp.tool()
def ping() -> str:
    """Check if the MCP server is alive. Returns 'pong'."""
    return "pong"


@mcp.tool()
def echo(message: str) -> str:
    """Echo back a message sent by the user."""
    return f"Echo: {message}"


@mcp.tool()
def add_numbers(a: float, b: float) -> str:
    """Add two numbers and return the result."""
    result = a + b
    return f"Result: {result}"


@mcp.tool()
def get_ip_info() -> str:
    """Get current public IP address and location information."""
    try:
        # Try multiple free IP APIs
        apis = [
            "https://api.ipify.org?format=json",
            "https://httpbin.org/ip", 
            "https://jsonip.com"
        ]

        for api in apis:
            try:
                response = requests.get(api, timeout=10, verify=False)
                if response.status_code == 200:
                    data = response.json()
                    ip = data.get('ip') or data.get('origin')
                    if ip:
                        # Get location info for the IP
                        try:
                            loc_response = requests.get(
                                f"http://ip-api.com/json/{ip}", timeout=10)
                            if loc_response.status_code == 200:
                                loc_data = loc_response.json()
                                info = f"IP: {ip}\n"
                                info += f"City: {loc_data.get('city', 'Unknown')}\n"
                                info += f"Region: {loc_data.get('regionName', 'Unknown')}\n"
                                info += f"Country: {loc_data.get('country', 'Unknown')}\n"
                                info += f"ISP: {loc_data.get('isp', 'Unknown')}"
                                return info
                        except:
                            pass
                        return f"IP: {ip}"
            except:
                continue

        return "Error: Unable to fetch IP information from any API"
    except Exception as e:
        return f"Error fetching IP info: {str(e)}"


@mcp.tool()
def get_local_ip_config() -> str:
    """Get local network configuration including hostname, interfaces, and IP addresses."""
    try:
        import subprocess
        import socket
        import platform
        
        result = "🌐 Local IP Configuration\n"
        result += "=" * 40 + "\n"
        
        # Get hostname
        hostname = socket.gethostname()
        result += f"Hostname: {hostname}\n"
        
        # Get local IP address
        try:
            # Connect to a dummy address to get local IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            result += f"Local IP: {local_ip}\n"
        except:
            result += "Local IP: Unable to determine\n"
        
        # Get platform info
        result += f"Platform: {platform.platform()}\n"
        result += f"System: {platform.system()}\n\n"
        
        # Try to get network interface info using ip command (Linux)
        try:
            ip_output = subprocess.check_output(['ip', 'addr', 'show'], text=True, timeout=10)
            result += "--- Network Interfaces ---\n"
            result += ip_output
        except:
            # Fallback to ifconfig if available
            try:
                ifconfig_output = subprocess.check_output(['ifconfig'], text=True, timeout=10)
                result += "--- Network Interfaces (ifconfig) ---\n"
                result += ifconfig_output
            except:
                result += "--- Network Interfaces ---\n"
                result += "Unable to retrieve network interface information\n"
        
        return result
        
    except Exception as e:
        return f"Error getting local IP configuration: {str(e)}"


@mcp.tool()
def get_weather(city: str) -> str:
    """Get current weather information for a city using OpenWeatherMap free API."""
    try:
        # Using OpenWeatherMap free API (no key required for basic data)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=demo"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            weather = f"Weather in {data.get('name', city)}:\n"
            weather += f"Temperature: {data['main']['temp']}°C\n"
            weather += f"Feels like: {data['main']['feels_like']}°C\n"
            weather += f"Humidity: {data['main']['humidity']}%\n"
            weather += f"Description: {data['weather'][0]['description'].title()}\n"
            weather += f"Wind Speed: {data['wind']['speed']} m/s"
            return weather
        else:
            # Fallback to a different free weather API
            url2 = f"https://wttr.in/{city}?format=j1"
            response2 = requests.get(url2, timeout=10)
            if response2.status_code == 200:
                data2 = response2.json()
                current = data2['current_condition'][0]
                weather = f"Weather in {city}:\n"
                weather += f"Temperature: {current['temp_C']}°C\n"
                weather += f"Feels like: {current['FeelsLikeC']}°C\n"
                weather += f"Humidity: {current['humidity']}%\n"
                weather += f"Description: {current['weatherDesc'][0]['value']}\n"
                weather += f"Wind Speed: {current['windspeedKmph']} km/h"
                return weather
            else:
                return f"Error: Unable to fetch weather for {city}"
    except Exception as e:
        return f"Error fetching weather: {str(e)}"


@mcp.tool()
def divide_numbers(a: float, b: float) -> str:
    """Divide two numbers and return the result."""
    if b == 0:
        return "Error: Division by zero"
    result = a / b
    return f"Result: {a} ÷ {b} = {result}"


@mcp.tool()
def get_server_info() -> str:
    """Get server system information including hostname, platform, and resource usage."""
    try:
        import platform
        import psutil
        from datetime import datetime
        
        info = {
            "hostname": platform.node(),
            "platform": platform.platform(),
            "python_version": platform.python_version(),
            "cpu_count": psutil.cpu_count(),
            "memory_gb": round(psutil.virtual_memory().total / (1024**3), 2),
            "server_time": datetime.now().isoformat()
        }
        
        result = "🖥️ Server Information:\n"
        result += f"Hostname: {info['hostname']}\n"
        result += f"Platform: {info['platform']}\n"
        result += f"Python Version: {info['python_version']}\n"
        result += f"CPU Cores: {info['cpu_count']}\n"
        result += f"Total Memory: {info['memory_gb']} GB\n"
        result += f"Server Time: {info['server_time']}"
        
        return result
    except Exception as e:
        return f"Error getting server info: {str(e)}"


@mcp.tool()
def multiply_numbers(a: float, b: float) -> str:
    """Multiply two numbers and return the result."""
    result = a * b
    return f"Result: {a} × {b} = {result}"


@mcp.tool()
def get_system_status() -> str:
    """Get current system resource usage (CPU, memory, disk)."""
    try:
        import psutil
        
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        result = "📊 System Status:\n"
        result += f"CPU Usage: {cpu_percent}%\n"
        result += f"Memory Usage: {memory.percent}% ({memory.used / (1024**3):.1f} GB used of {memory.total / (1024**3):.1f} GB)\n"
        result += f"Disk Usage: {disk.percent}% ({disk.used / (1024**3):.1f} GB used of {disk.total / (1024**3):.1f} GB)"
        
        return result
    except Exception as e:
        return f"Error getting system status: {str(e)}"


if __name__ == "__main__":
    mcp.run()
