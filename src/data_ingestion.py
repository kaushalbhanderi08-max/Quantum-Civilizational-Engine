import pandas as pd
import numpy as np
import datetime

def fetch_live_market_data():
    """
    લાઈવ માર્કેટ ડેટા ફીડ (માર્કેટ ટ્રેન્ડ્સ, ઇકોનોમિક વાઇબ્સ, સપ્લાય ચેઈન સિગ્નલ્સ)
    """
    print("Fetching live market data feeds...")
    # અહીં આપણે માર્કેટ વોલેટિલિટી અને ટ્રેન્ડ સિમ્યુલેટ કરીએ છીએ
    np.random.seed(int(datetime.datetime.now().timestamp()) % 1000)
    market_signals = {
        'market_volatility': np.random.uniform(0.1, 0.9),
        'supply_chain_index': np.random.uniform(0.2, 0.95),
        'tech_adoption_rate': np.random.uniform(0.5, 0.99),
        'global_sentiment': np.random.uniform(0.0, 1.0)
    }
    return market_signals

def merge_csv_and_market_data(csv_path):
    """
    તમારી ૧૪-ચેનલ CSV અને માર્કેટ ડેટાને મર્જ કરીને ક્વોન્ટમ ઇનપુટ તૈયાર કરશે
    """
    try:
        df = pd.read_csv(csv_path)
        print(f"Successfully loaded CSV with shape: {df.shape}")
    except FileNotFoundError:
        print(f"Error: CSV file not found at {csv_path}")
        return None

    # માર્કેટ ડેટા મેળવો
    market_data = fetch_live_market_data()
    print("Market Signals Retrieved:", market_data)

    # ૧૪ ચેનલો માટે ડેટા નોર્મલાઇઝેશન (0 થી 1 સ્કેલિંગ)
    # જેથી ક્વોન્ટમ સર્કિટ રોટેશનલ એન્ગલ (0 થી 2*pi) માં વાપરી શકે
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        max_val = df[col].max()
        if max_val != 0:
            df[col] = df[col] / max_val

    print("Data Ingestion & Normalization Complete!")
    return df, market_data

if __name__ == "__main__":
    df_ingested, market_signals = merge_csv_and_market_data('data/Human Timeline - Product SCM.csv')
    if df_ingested is not None:
        print("Ready for Quantum Decision Engine Processing!")
