#!/usr/bin/env python3
"""Launch the SecOps MCP server."""

from secops_mcp import mcp

if __name__ == "__main__":
    mcp.run(transport="stdio") 