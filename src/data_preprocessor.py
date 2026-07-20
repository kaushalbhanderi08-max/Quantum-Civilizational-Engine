import pandas as pd
import numpy as np

def preprocess_civilizational_data(file_path):
    # 1. ડેટા લોડ કરો
    try:
        df = pd.read_csv(file_path)
        print(f"File loaded successfully from: {file_path}")
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found. Check your folder structure!")
        return None, None
    
    # 2. ખાલી સેલ્સ (NaN) ને '0' થી ભરી દો
    df = df.fillna(0)
    
    # 3. કેટેગરીઝ ને ન્યુમેરિકલ ફોર્મેટમાં કન્વર્ટ કરો (Label Encoding)
    # આથી ક્વોન્ટમ સર્કિટ લોજિક ગેટ્સ તેને સમજી શકશે
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col] = df[col].astype('category').cat.codes
    
    # 4. ૧૪-ચેનલ લોજિક મુજબ સ્ટ્રક્ચર તૈયાર કરો (Mapping)
    channel_mapping = {
        'q_alg1': ['Location', 'Winter', 'Summer', 'Monsoon', 'Earth'],
        'q_alg2': ['Age', 'Name', 'Routine'],
        'q_alg3': ['Industry', 'Product', 'Raw Material (BOM) Company', 'Storage Company'],
        'q_alg4': ['Tech Updation', 'Digital- Ecommerce / Screen ', 'Ai', 'IOT', 'Reserch - Personalize Customization'],
        'q_alg5': ['Finance & Investment Company', 'Sell - Physical/Virtual', 'Profit - Physical/Virtual'],
        'q_alg6': ['Infrastructure Construction Company'],
        'q_alg7': ['Production Machinery (Making or Manufacturing) Company', 'Packaging Company'],
        'q_alg8': ['Testing (Certification) Company'],
        'q_alg9': ['Sensing', 'Class', 'Gender'],
        'q_alg10': ['Occupation', 'Timeline'],
        'q_alg11': ['Distribution Transport Company ', 'Marketing Company'],
        'q_alg12': ['Recycle Comapany', 'Carbon Credit'],
        'q_alg13': ['History', 'Future', 'Present', 'Digital Twin'],
        'q_alg14': ['World Population Live', 'Space', 'Orbit', 'Multi Planet']
    }
    
    print("Data Preprocessing Completed successfully!")
    return df, channel_mapping

# મુખ્ય એક્ઝેક્યુશન લાઈન
# અહીં આપણે 'data/' ફોલ્ડરનો પાથ આપ્યો છે
df_clean, mapping = preprocess_civilizational_data('data/Human Timeline - Product SCM.csv')

if df_clean is not None:
    print(f"Cleaned DataFrame Shape: {df_clean.shape}")
