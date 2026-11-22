# Provenance Data Grid MCP Server

[![PyPI](https://img.shields.io/pypi/v/pdg-mcp)](https://pypi.org/project/pdg-mcp/)
[![Python](https://img.shields.io/pypi/pyversions/pdg-mcp)](https://pypi.org/project/pdg-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

20 data tools for AI agents via the [Model Context Protocol](https://modelcontextprotocol.io). Access OFAC sanctions screening, SEC filings, healthcare provider data, business entity search, market data, and more — directly from Claude Desktop, Cursor, Windsurf, or any MCP-compatible client.

**5 free calls per day per tool. No API key or account needed to start.**

<img width="700" alt="Provenance Data Grid" src="https://pdg.neprovenance.com/static/og-image.png">

## Quick Start

### Install

```bash
pip install pdg-mcp
```

### Configure Claude Desktop

Add to your Claude Desktop config (`~/.claude/settings.json`):

```json
{
  "mcpServers": {
    "pdg": {
      "command": "pdg-mcp"
    }
  }
}
```

Restart Claude Desktop. You'll see 20 new tools available.

### Configure Cursor

Add to Cursor's MCP settings (`.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "pdg": {
      "command": "pdg-mcp"
    }
  }
}
```

### Configure VS Code

```json
{
  "mcp": {
    "servers": {
      "pdg": {
        "command": "pdg-mcp"
      }
    }
  }
}
```

## Tools

### Entity & Compliance
| Tool | Description |
|------|-------------|
| `sanctions_screen` | Screen names against OFAC SDN list (19,596 entries, fuzzy matching) |
| `entity_search` | Search businesses across SEC, NPPES, and 5 state SOS databases |
| `entity_federal` | SAM.gov federal contractor lookup with certifications |
| `provider_search` | Search 9.89M US healthcare providers by name, NPI, specialty |
| `company_detail` | SEC company details: tickers, SIC code, filings |
| `company_financials` | SEC XBRL financials: revenue, net income, assets, EPS |
| `address_enrich` | Multi-source address enrichment (property + providers + entities) |

### Market Data
| Tool | Description |
|------|-------------|
| `crypto_price` | Crypto price, 24h change, volume, market cap (100+ coins) |
| `crypto_top` | Top cryptocurrencies ranked by market cap |
| `stock_price` | US stock quotes: price, volume, day range |
| `market_search` | Search prediction markets (Polymarket + Kalshi) |
| `market_quote` | Prediction market bid/ask and volume |

### Web & Weather
| Tool | Description |
|------|-------------|
| `web_extract` | Extract clean markdown from any URL |
| `web_search` | Web search via Brave Search |
| `news_search` | News headlines by keyword |
| `weather` | Global weather + 48h forecast |
| `weather_us` | NWS weather + alerts (US only) |

### Blockchain
| Tool | Description |
|------|-------------|
| `chain_balance` | Wallet balances on Base/Ethereum/Arbitrum |
| `chain_gas` | Current gas prices |
| `chain_tx` | Transaction details by hash |

## Example Usage

Once configured, ask your AI assistant:

- *"Screen Acme Corp against OFAC sanctions"*
- *"Look up Apple's SEC financials"*
- *"Find healthcare providers named Smith in Boston"*
- *"What's the current price of ETH?"*
- *"Extract the main content from this article: https://..."*
- *"Search prediction markets about the Fed rate decision"*

## Authentication

The free tier gives you **5 calls per day per tool** with no configuration needed.

For higher volume, purchase API credits and set your key:

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

| Plan | Credits | Price | Per Call |
|------|---------|-------|---------|
| Starter | 1,000 | $5 | $0.005 |
| Growth | 10,000 | $40 | $0.004 |
| Scale | 100,000 | $300 | $0.003 |

**[Buy API Credits →](https://pdg.neprovenance.com/billing/plans)**

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PDG_API_KEY` | *(none)* | API key for authenticated access |
| `PDG_BASE_URL` | `https://pdg.neprovenance.com` | API base URL |

## Data Sources

All data sourced from authoritative public sources:

- **OFAC SDN** — US Treasury sanctions list (19,596 entries)
- **CMS NPPES** — National Provider Identifier registry (9.89M providers)
- **SEC EDGAR** — Company filings and XBRL financials (7,993 companies)
- **State SOS** — Secretary of State business registrations (NY, PA, CT, CO, OR)
- **SAM.gov** — Federal contractor registrations
- **CoinGecko** — Cryptocurrency market data
- **Brave Search** — Web search results
- **Open-Meteo / NWS** — Weather data
- **Polymarket / Kalshi** — Prediction market data

## Also Available

- **[LangChain Tools](https://pypi.org/project/pdg-langchain/)** — `pip install pdg-langchain`
- **[REST API](https://pdg.neprovenance.com/docs)** — Full OpenAPI spec
- **[x402 Protocol](https://pdg.neprovenance.com/.well-known/x402)** — Pay per call in USDC on Base

## License

MIT — see [LICENSE](LICENSE).

Built by [New England Provenance LLC](https://neprovenance.com) · [API Docs](https://pdg.neprovenance.com/docs) · [Buy Credits](https://pdg.neprovenance.com/billing/plans) · [Service Health](https://pdg.neprovenance.com/health)
