# pdg-mcp — Provenance Data Grid MCP Server

20 data tools for AI agents via the Model Context Protocol. Works with Claude Desktop, Cursor, Windsurf, and any MCP-compatible client.

## Install

```bash
pip install pdg-mcp
```

## Configure

**Claude Desktop** (`~/.claude/settings.json`):
```json
{
  "mcpServers": {
    "pdg": {
      "command": "pdg-mcp"
    }
  }
}
```

**With API key** (for more than 5 free calls/day):
```json
{
  "mcpServers": {
    "pdg": {
      "command": "pdg-mcp",
      "env": {
        "PDG_API_KEY": "pdg_your_key_here"
      }
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `crypto_price` | Crypto price, 24h change, volume, market cap |
| `stock_price` | US stock quotes |
| `weather` | Global weather + 48h forecast |
| `weather_us` | NWS weather + alerts (US only) |
| `web_extract` | URL to clean markdown |
| `web_search` | Brave Search results |
| `news_search` | News headlines by keyword |
| `entity_search` | Business entity search (SEC + 5 state SOS + NPPES) |
| `entity_federal` | SAM.gov federal contractor lookup |
| `sanctions_screen` | OFAC SDN screening (19,596 entries) |
| `provider_search` | 9.89M US healthcare providers |
| `company_detail` | SEC company details + filings |
| `company_financials` | SEC XBRL financials (revenue, assets, EPS) |
| `address_enrich` | Multi-source address enrichment |
| `market_search` | Prediction markets (Polymarket + Kalshi) |
| `market_quote` | Prediction market quotes |
| `chain_balance` | Wallet balances (Base/ETH/Arbitrum) |
| `chain_gas` | Gas prices |
| `chain_tx` | Transaction details |

## Pricing

- **Free:** 5 calls/day per tool, no API key needed
- **API Key:** Credit packs from $5 at https://pdg.neprovenance.com/billing/plans
- **x402:** Pay per call in USDC on Base

## Links

- API Docs: https://pdg.neprovenance.com/docs
- Buy Credits: https://pdg.neprovenance.com/billing/plans
