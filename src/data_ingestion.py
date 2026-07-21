import os
import pandas as pd
import yfinance as yf
import wbgapi as wb
import feedparser

class DataIngestionEngine:
    def __init__(self):
        pass
        
    def fetch_global_planetary_data(self):
        """
        1. World Bank Demographics (Population, Birth/Death rates)
        2. Environment & Wildlife / Biodiversity Proxy
        3. WTO / World Bank Economic Classes & Human Consumption
        4. WEF Strategic Intelligence & Tech News via RSS
        """
        try:
            # 1. World Bank Population & Vital Statistics (SP.POP.TOTL, SP.DYN.CBRT.IN, SP.DYN.CDRT.IN)
            pop_data = wb.data.get('SP.POP.TOTL', 'WLD', mrv=1)
            population = float(next(iter(pop_data), {}).get('value', 8000000000))
            
            # 2. Environment / Tree / Biodiversity Proxy (Forest area % or CO2 emissions index from World Bank)
            forest_data = wb.data.get('AG.LND.FRST.ZS', 'WLD', mrv=1)
            forest_index = float(next(iter(forest_data), {}).get('value', 31.0)) / 100.0 # Normalized
            
            # 3. Economic Classes / Consumption Proxy (World Bank Poverty Headcount or GNI per capita)
            gni_data = wb.data.get('NY.GNP.PCAP.CD', 'WLD', mrv=1)
            gni_value = float(next(iter(gni_data), {}).get('value', 12000.0))
            middle_class_index = min(gni_value / 50000.0, 1.0)
            
            # 4 & 5. WEF / Tech News Feeds via Free RSS (Yahoo Finance Tech / TechCrunch / Reuters)
            rss_url = "https://finance.yahoo.com/news/rssindex"
            feed = feedparser.parse(rss_url)
            tech_sentiment = 0.95
            if feed.entries:
                # જો ન્યૂઝ ફીડ્સ ચાલુ હોય તો ટેક સેન્ટિમેન્ટ કેલ્ક્યુલેટ કરો
                tech_sentiment = min(0.99, 0.90 + (len(feed.entries) / 1000.0))

            # Existing Market Volatility via yfinance
            ticker = yf.Ticker("^GSPC")
            history = ticker.history(period="5d")
            market_volatility = 0.05
            if not history.empty:
                recent_close = history['Close'].iloc[-1]
                prev_close = history['Close'].iloc[-2]
                market_volatility = min(float(abs(recent_close - prev_close) / prev_close * 10), 1.0)

            global_signals = {
                'market_volatility': market_volatility,
                'supply_chain_index': forest_index, # Using environmental health index as a proxy
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
