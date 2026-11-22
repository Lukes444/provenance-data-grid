"""Provenance Data Grid MCP Server — 20 data tools for AI agents.

Runs as:
1. Remote: mounted at /mcp on the FastAPI app (Streamable HTTP transport)
2. Standalone: `python -m mcp_server` (stdio transport)

5 free calls/day per tool. For more, set PDG_API_KEY env var.
Buy credits at https://pdg.neprovenance.com/billing/plans
"""

import os
import json

import httpx
from mcp.server import Server
from mcp import types

PDG_BASE_URL = os.environ.get("PDG_BASE_URL", "https://pdg.neprovenance.com")
PDG_API_KEY = os.environ.get("PDG_API_KEY", "")

server = Server("provenance-data-grid")


async def _call(path: str, params: dict = None) -> dict:
    headers = {}
    if PDG_API_KEY:
        headers["X-API-Key"] = PDG_API_KEY
    async with httpx.AsyncClient(timeout=15.0, base_url=PDG_BASE_URL) as client:
        resp = await client.get(path, params=params or {}, headers=headers)
        return resp.json()


# --- Tool definitions ---

TOOLS = [
    types.Tool(name="crypto_price", description="Get cryptocurrency price, 24h change, volume, and market cap. Supports BTC, ETH, SOL, and 100+ coins.",
               inputSchema={"type": "object", "properties": {"symbol": {"type": "string", "description": "Crypto symbol (btc, eth, sol)"}}, "required": ["symbol"]}),
    types.Tool(name="crypto_top", description="Top cryptocurrencies ranked by market cap with prices and 24h changes.",
               inputSchema={"type": "object", "properties": {"limit": {"type": "integer", "description": "Number of coins (default 20, max 100)", "default": 20}}}),
    types.Tool(name="stock_price", description="Current stock quote: price, day high/low, volume. All US-listed stocks.",
               inputSchema={"type": "object", "properties": {"ticker": {"type": "string", "description": "Stock ticker (AAPL, MSFT, TSLA)"}}, "required": ["ticker"]}),
    types.Tool(name="weather", description="Current weather and 48-hour forecast for any location worldwide.",
               inputSchema={"type": "object", "properties": {"lat": {"type": "number", "description": "Latitude"}, "lon": {"type": "number", "description": "Longitude"}}, "required": ["lat", "lon"]}),
    types.Tool(name="weather_us", description="US weather from NWS: current conditions, 7-day forecast, and active alerts.",
               inputSchema={"type": "object", "properties": {"lat": {"type": "number", "description": "Latitude (US only)"}, "lon": {"type": "number", "description": "Longitude (US only)"}}, "required": ["lat", "lon"]}),
    types.Tool(name="web_extract", description="Extract main content from any URL as clean markdown. Strips ads and navigation.",
               inputSchema={"type": "object", "properties": {"url": {"type": "string", "description": "URL to extract"}}, "required": ["url"]}),
    types.Tool(name="web_search", description="Web search via Brave Search. Structured results with titles, URLs, snippets.",
               inputSchema={"type": "object", "properties": {"query": {"type": "string", "description": "Search query"}}, "required": ["query"]}),
    types.Tool(name="news_search", description="Search news headlines by keyword. Returns titles, sources, URLs, dates.",
               inputSchema={"type": "object", "properties": {"query": {"type": "string", "description": "Search query"}}, "required": ["query"]}),
    types.Tool(name="entity_search", description="Search US business entities across 5 state SOS databases, SEC EDGAR, and 9.89M NPPES healthcare providers.",
               inputSchema={"type": "object", "properties": {"name": {"type": "string", "description": "Business or entity name"}, "state": {"type": "string", "description": "Two-letter state code (optional)"}}, "required": ["name"]}),
    types.Tool(name="entity_federal", description="SAM.gov federal contractor lookup: status, certifications (HUBZone, 8(a), WOSB), NAICS codes.",
               inputSchema={"type": "object", "properties": {"name": {"type": "string", "description": "Business name"}}, "required": ["name"]}),
    types.Tool(name="sanctions_screen", description="OFAC SDN sanctions screening. 19,596 entries with exact and fuzzy matching. Essential for compliance.",
               inputSchema={"type": "object", "properties": {"name": {"type": "string", "description": "Name to screen"}}, "required": ["name"]}),
    types.Tool(name="provider_search", description="Search 9.89M US healthcare providers by name, NPI, location, or specialty. All 50 states.",
               inputSchema={"type": "object", "properties": {"name": {"type": "string", "description": "Provider name"}, "npi": {"type": "string", "description": "NPI number"}, "state": {"type": "string", "description": "State code"}, "city": {"type": "string", "description": "City"}}}),
    types.Tool(name="company_detail", description="SEC company details: tickers, SIC code, addresses, recent filings. Use CIK number.",
               inputSchema={"type": "object", "properties": {"cik": {"type": "string", "description": "SEC CIK number (e.g., 320193 for Apple)"}}, "required": ["cik"]}),
    types.Tool(name="company_financials", description="Public company financials from SEC XBRL: revenue, net income, assets, equity, EPS.",
               inputSchema={"type": "object", "properties": {"cik": {"type": "string", "description": "SEC CIK number"}}, "required": ["cik"]}),
    types.Tool(name="compliance_screen", description="Compound compliance screening: OFAC SDN (19,596) + OIG LEIE (84,224) + SAM.gov debarment in one call. Returns CLEAR/FLAGGED/INCOMPLETE.",
               inputSchema={"type": "object", "properties": {"name": {"type": "string", "description": "Person or entity name to screen"}}, "required": ["name"]}),
    types.Tool(name="address_enrich", description="Multi-source address enrichment: property data (New England), healthcare providers, and business entities at address.",
               inputSchema={"type": "object", "properties": {"address": {"type": "string", "description": "Street address"}, "city": {"type": "string", "description": "City"}, "state": {"type": "string", "description": "State code"}}, "required": ["address", "city", "state"]}),
    types.Tool(name="market_search", description="Search prediction markets on Polymarket and Kalshi. Prices, volume, liquidity.",
               inputSchema={"type": "object", "properties": {"query": {"type": "string", "description": "Search query"}}, "required": ["query"]}),
    types.Tool(name="market_quote", description="Prediction market quote: bid/ask, volume, outcome prices.",
               inputSchema={"type": "object", "properties": {"market_id": {"type": "string", "description": "Market ID from market_search"}}, "required": ["market_id"]}),
    types.Tool(name="chain_balance", description="ETH and token balances for a wallet on Base, Ethereum, or Arbitrum.",
               inputSchema={"type": "object", "properties": {"address": {"type": "string", "description": "Wallet address (0x...)"}, "chain": {"type": "string", "description": "base, ethereum, or arbitrum", "default": "base"}}, "required": ["address"]}),
    types.Tool(name="chain_gas", description="Current gas price and base fee on Base, Ethereum, or Arbitrum.",
               inputSchema={"type": "object", "properties": {"chain": {"type": "string", "description": "base, ethereum, or arbitrum", "default": "base"}}}),
    types.Tool(name="chain_tx", description="Transaction details: sender, recipient, value, gas, status.",
               inputSchema={"type": "object", "properties": {"tx_hash": {"type": "string", "description": "Transaction hash"}, "chain": {"type": "string", "description": "base, ethereum, or arbitrum", "default": "base"}}, "required": ["tx_hash"]}),
]

DISPATCH = {
    "crypto_price": lambda a: _call(f"/price/crypto/{a['symbol']}"),
    "crypto_top": lambda a: _call("/price/crypto", {"limit": a.get("limit", 20)}),
    "stock_price": lambda a: _call(f"/price/stock/{a['ticker']}"),
    "weather": lambda a: _call(f"/weather/{a['lat']},{a['lon']}"),
    "weather_us": lambda a: _call(f"/weather-us/{a['lat']},{a['lon']}"),
    "web_extract": lambda a: _call("/web/extract", {"url": a["url"]}),
    "web_search": lambda a: _call("/web/search", {"q": a["query"]}),
    "news_search": lambda a: _call("/news/search", {"q": a["query"]}),
    "entity_search": lambda a: _call("/entity/search", {"name": a["name"], **({"state": a["state"]} if a.get("state") else {})}),
    "entity_federal": lambda a: _call("/entity/federal", {"name": a["name"]}),
    "sanctions_screen": lambda a: _call("/sanctions/screen", {"name": a["name"]}),
    "compliance_screen": lambda a: _call("/compliance/screen", {"name": a["name"]}),
    "provider_search": lambda a: _call("/provider/search", {k: v for k, v in a.items() if v}),
    "company_detail": lambda a: _call(f"/company/{a['cik']}"),
    "company_financials": lambda a: _call(f"/company/{a['cik']}/financials"),
    "address_enrich": lambda a: _call("/address/enrich", {"address": a["address"], "city": a["city"], "state": a["state"]}),
    "market_search": lambda a: _call("/market/search", {"q": a["query"]}),
    "market_quote": lambda a: _call(f"/market/quote/{a['market_id']}"),
    "chain_balance": lambda a: _call(f"/chain/balance/{a['address']}", {"chain": a.get("chain", "base")}),
    "chain_gas": lambda a: _call("/chain/gas", {"chain": a.get("chain", "base")}),
    "chain_tx": lambda a: _call(f"/chain/tx/{a['tx_hash']}", {"chain": a.get("chain", "base")}),
}


# --- MCP protocol handlers ---

async def handle_list_tools(request, *args):
    return types.ListToolsResult(tools=TOOLS)


async def handle_call_tool(request, *args):
    name = request.params.name
    args = request.params.arguments or {}

    handler = DISPATCH.get(name)
    if not handler:
        return types.CallToolResult(
            content=[types.TextContent(type="text", text=f"Unknown tool: {name}")],
            isError=True,
        )
    try:
        result = await handler(args)
        return types.CallToolResult(
            content=[types.TextContent(type="text", text=json.dumps(result, indent=2))],
        )
    except Exception as e:
        return types.CallToolResult(
            content=[types.TextContent(type="text", text=f"Error: {e}")],
            isError=True,
        )


server.add_request_handler("tools/list", types.ListToolsRequest, handle_list_tools)
server.add_request_handler("tools/call", types.CallToolRequest, handle_call_tool)


def get_streamable_app():
    """Get a Starlette app for mounting in FastAPI (remote HTTP transport)."""
    return server.streamable_http_app()
