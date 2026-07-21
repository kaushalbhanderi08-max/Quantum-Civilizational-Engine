import os
import pandas as pd
import yfinance as yf

class DataIngestionEngine:
    def __init__(self):
        pass
        
    def fetch_live_market_data(self):
        """
        Yahoo Finance (yfinance) નો ઉપયોગ કરીને ફ્રીમાં રિયલ માર્કેટ ડેટા ફેચ કરો
        """
        try:
            # S&P 500 (^GSPC) અને Crude Oil / Gold જેવી કમોડિટીઝ માર્કેટ વોલેટિલિટી માટે
            ticker = yf.Ticker("^GSPC")
            history = ticker.history(period="5d")
            
            if not history.empty:
                recent_close = history['Close'].iloc[-1]
                prev_close = history['Close'].iloc[-2]
                volatility = abs(recent_close - prev_close) / prev_close
                # નોર્મલાઇઝ્ડ સ્કેલ
                market_volatility = min(float(volatility * 10), 1.0)
            else:
                market_volatility = 0.5
                
            # વૈશ્વિક સપ્લાય ચેઈન અથવા ટ્રેડ ઇન્ડેક્સ માટે શિપિંગ/લાજિસ્ટિક્સ ડેટા (જેમ કે BDI અથવા ETF)
            shipping_ticker = yf.Ticker("BDRY") # DryShips / Shipping ETF
            shipping_hist = shipping_ticker.history(period="5d")
            if not shipping_hist.empty:
                supply_index = float(shipping_hist['Close'].iloc[-1] / 100)
                supply_chain_index = max(0.0, min(supply_index, 1.0))
            else:
                supply_chain_index = 0.6
                
            market_signals = {
                'market_volatility': market_volatility,
                'supply_chain_index': supply_chain_index,
                'tech_adoption_rate': 0.98, # ટેક્નોલોજી ગ્રોથ ઇન્ડેક્સ
                'global_sentiment': 0.99
            }
            print("Live Market Signals Retrieved Successfully via yfinance!")
            return market_signals
            
        except Exception as e:
            print(f"Error fetching live data, falling back to default signals: {e}")
            return {
                'market_volatility': 0.5,
                'supply_chain_index': 0.5,
                'tech_adoption_rate': 0.9,
                'global_sentiment': 0.9
            }

if __name__ == "__main__":
    engine = DataIngestionEngine()
    signals = engine.fetch_live_market_data()
    print("Market Signals:", signals)
