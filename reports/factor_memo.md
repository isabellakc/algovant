This memo summarizes a factor analysis of momentum and contrarian (price reversal) strategies applied to 10 large-cap US equities from May 2013 to December 2025. Key findings:

Momentum L-S: +9.2% annualized return, Sharpe 0.23, max drawdown -65%
Contrarian L-S: -14.5% annualized return, Sharpe -0.36, max drawdown -95%
Correlation: -0.89 (strong negative correlation indicates complementary diversification)
Momentum dominated in 2013-2019 and 2021-2023; contrarian briefly worked in 2018, 2020, and 2022

1. Methodology
1.1 Daily Price Data (Stooq)
10 large-cap US equities (AAPL, MSFT, GOOGL, AMZN, META, TSLA, NVDA, JPM, V, UNH)
Period: May 2013 to December 2025 (152 months with full coverage)
Rebalancing: Monthly

1.2 Factor Definitions
Momentum Factor (12-1 Month):  momentum_12_1 = (Price_t-1 / Price_t-12) - 1
Measures price performance from 12 months ago to 1 month ago (skip most recent month to avoid short-term reversal)

Contrarian Factor (Price Reversal): value_score = -(Price_t / Price_t-12 - 1)

1.3 Portfolio Construction
Each month:
Rank all stocks by factor score (cross-sectional)
Divide into 5 quintiles (Q1 = lowest, Q5 = highest)
Compute equal-weighted returns for each quintile over next month
Long-Short: Q5 - Q1 (buy high factor stocks, sell low factor stocks)

2. Results
2.1 Quintile Performance
Momentum Quintiles (Cumulative Returns):
Q5 (high momentum): $1 → $203
Q4: $1 → $16
Q3: $1 → $8
Q2: $1 → $17
Q1 (low momentum): $1 → $87

Monthly Return Statistics (Momentum):
Q1 mean 3.28%, Std Dev 8.71%, min -16.9%, max 32.2%
Q5 mean 4.04%, Std Dev 10.22%, min -22.6%, max 50.8%

2.2 Long-Short Portfolio Performance
Momentum L-S: return 9.16%, vol 39.6%, Sharpe 0.23, max DD −65%; $1 → $1.30
Contrarian L-S: return −14.48%, vol 40.2%, Sharpe −0.36, max DD −95%; $1 → $0.05

2.3 Year-by-Year Returns
Momentum L-S: Best year: 2020 (+160%), worst year: 2019 (-42%), positive in 8/13 years
Contrarian L-S: Best year: 2018 (+36%), worst year: 2020 (-85%), negative in 10/13 years
Correlation: -0.89 (very strong negative correlation)
Momentum = buy (P_t-1 / P_t-12) > 1 (stocks that went up)
Contrarian = buy -(P_t / P_t-12 - 1) > 0 (stocks that went down)

3. Analysis 
3.1 Why Momentum Works
Under-reaction: Market slowly incorporates positive news; prices drift upward, herding: Investors chase past winners, creating self-reinforcing trends; anchoring: Investors slow to update beliefs, allowing trends to persist
3.2 Why Contrarian Failed
Recent losers continued to underperform, especially in a momentum driven market
Tech stocks with high momentum dominated
Value stocks underperformed for over a decade
When Contrarian Worked:
2018: Market correction created overselling, 2020 (briefly): Post-COVID bounce, 2022: Growth stock selloff allowed losers to bounce
Portfolio Implication:
Running both strategies together provides diversification and smoothed returns

4. Factor Neutral vs Market Neutral
4.1 Market Neutrality (What We Have)
Both L-S portfolios are market neutral, remove broad market direction (beta ≈ 0)
4.2 Factor Neutrality (What We Don't Have)
Definition: Neutral to other risk factors (size, value, quality, etc.)
Our momentum L-S is market-neutral but not size-neutral (may favor large caps like NVDA), sector-neutral (may overweigh tech), nor value-neutral (may be long growth stocks).
4.3 How to Achieve Factor Neutrality
Sector neutrality, larger universe, residualized signals

5. Limitations and Caveats
10 stocks are current large caps; excludes failures
Contrarian strategy is a return-based proxy, not true value
Ignores transaction costs
Results are specific to 2013-2025 bull market: may not generalize to other periods


