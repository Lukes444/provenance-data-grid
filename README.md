# pdg-mcp — Provenance Data Grid MCP Server

Compliance and entity intelligence tools for AI agents via the Model Context Protocol. OFAC sanctions screening, 9.89M healthcare provider lookup, SEC filings, business entity search, plus market data, weather, and more. Works with Claude Desktop, Cursor, Windsurf, and any MCP-compatible client.

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

### Entity & Compliance

| Tool | Description |
|------|-------------|
| `sanctions_screen` | OFAC SDN screening (19,596 entries, fuzzy matching) |
| `provider_search` | 9.89M US healthcare providers by name, NPI, specialty |
| `company_detail` | SEC company details + filings |
| `company_financials` | SEC XBRL financials (revenue, assets, EPS) |
| `entity_search` | Business entity search (SEC + 5 state SOS + NPPES) |
| `entity_federal` | SAM.gov federal contractor lookup |
| `address_enrich` | Multi-source address enrichment |

### Market Data, Weather & Web

| Tool | Description |
|------|-------------|
| `crypto_price` | Crypto price, 24h change, volume, market cap |
| `stock_price` | US stock quotes |
| `weather` | Global weather + 48h forecast |
| `weather_us` | NWS weather + alerts (US only) |
| `news_search` | News headlines by keyword |
| `web_extract` | URL to clean markdown |
| `web_search` | Brave Search results |
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
