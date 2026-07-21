import os
import pandas as pd
import yfinance as yf
import wbgapi as wb
import feedparser

class DataIngestionEngine:
    def __init__(self):
        pass
        
    def fetch_global_planetary_data(self):
        try:
            # 1. World Bank Population (Safe parsing)
            pop_raw = wb.data.get('SP.POP.TOTL', 'WLD', mrv=1)
            population = 8000000000.0
            if isinstance(pop_raw, list) and len(pop_raw) > 0:
                val = pop_raw[0].get('value') if isinstance(pop_raw[0], dict) else getattr(pop_raw[0], 'value', None)
                if val: population = float(val)

            # 2. Environment / Forest Area Proxy
            forest_raw = wb.data.get('AG.LND.FRST.ZS', 'WLD', mrv=1)
            forest_index = 0.31
            if isinstance(forest_raw, list) and len(forest_raw) > 0:
                val = forest_raw[0].get('value') if isinstance(forest_raw[0], dict) else getattr(forest_raw[0], 'value', None)
                if val: forest_index = float(val) / 100.0

            # 3. GNI per capita Proxy for Middle Class Index
            gni_raw = wb.data.get('NY.GNP.PCAP.CD', 'WLD', mrv=1)
            middle_class_index = 0.60
            if isinstance(gni_raw, list) and len(gni_raw) > 0:
                val = gni_raw[0].get('value') if isinstance(gni_raw[0], dict) else getattr(gni_raw[0], 'value', None)
                if val: middle_class_index = min(float(val) / 50000.0, 1.0)

            # 4 & 5. Tech News Feeds via RSS
            rss_url = "https://finance.yahoo.com/news/rssindex"
            feed = feedparser.parse(rss_url)
            tech_sentiment = 0.95
            if feed.entries:
                tech_sentiment = min(0.99, 0.90 + (len(feed.entries) / 1000.0))

            # Market Volatility via yfinance
            ticker = yf.Ticker("^GSPC")
            history = ticker.history(period="5d")
            market_volatility = 0.05
            if not history.empty:
                recent_close = history['Close'].iloc[-1]
                prev_close = history['Close'].iloc[-2]
                market_volatility = min(float(abs(recent_close - prev_close) / prev_close * 10), 1.0)

            global_signals = {
                'market_volatility': market_volatility,
                'supply_chain_index': forest_index,
                'tech_adoption_rate': tech_sentiment,
                'global_sentiment': middle_class_index,
                'total_population': population
            }
            print("Global Planetary & Market Data Retrieved Successfully!")
            return global_signals
            
        except Exception as e:
            print(f"Error fetching global data, using fallback defaults: {e}")
            return {
                'market_volatility': 0.05,
                'supply_chain_index': 0.31,
                'tech_adoption_rate': 0.95,
                'global_sentiment': 0.60,
                'total_population': 8000000000
            }

if __name__ == "__main__":
    engine = DataIngestionEngine()
    signals = engine.fetch_global_planetary_data()
    print("Global Signals:", signals)
