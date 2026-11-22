"""Run the PDG MCP server over stdio for local use with Claude Desktop, Cursor, etc."""

import asyncio
from mcp.server.stdio import stdio_server
from mcp_server.server import server


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


def main_sync():
    asyncio.run(main())


if __name__ == "__main__":
    main_sync()
