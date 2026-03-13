# Algovant

A quantitative research project analyzing price momentum strategies across 10 large-cap US stocks (1999–2025). Investigates factor returns, portfolio construction, earnings event studies, and robustness to transaction costs and market regimes.

**Key finding:** A 12-1 month momentum long-short strategy generates +9.2% annualized gross returns (Sharpe 0.23), driven largely by Tech sector stocks. Net return at 10 bps transaction costs is 8.1%. Strategy works in trending markets and fails during crises.

---

## Project Structure

```
algovant/
├── utils.py                                # Data loading utilities
├── requirements.txt                        # Python dependencies
├── data/
│   └── daily/us/                           # Raw daily price data (Stooq)
├── notebooks/
│   ├── data_quality_checks.ipynb           # Data validation and cleaning
│   ├── factor_value_momentum.ipynb         # Momentum and contrarian factors
│   ├── risk_portfolio_construction.ipynb   # Portfolio construction and risk metrics
│   ├── event_study.ipynb                   # Earnings announcement analysis
│   └── transaction_costs_robustness.ipynb  # Cost sensitivity and robustness tests
└── reports/
    ├── data_cleaning_report.md
    ├── factor_memo.md
    └── final_report.md
```

---

## How to Run

**Requirements:** Python 3.9+

```bash
pip install -r requirements.txt
```

Then run the notebooks in order — each builds on the data and variables from the previous one. Data loads automatically from `data/daily/us/` via `utils.py` (source: [Stooq](https://stooq.com)).
