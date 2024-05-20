import pandas as pd
import jieba
import re
import numpy

def clean_text(text):
    # Tokenize the text using Jieba
    tokens = jieba.cut(text, cut_all=False)
    
    # Remove hashtags and mentions
    cleaned_tokens = [token for token in tokens if not re.match(r'(^#\w+$)|(^@\w+$)', token)]
    
    # Join the cleaned tokens back into a string
    cleaned_text = ' '.join(cleaned_tokens)
    
    return cleaned_text

# Load the Excel file
input_file = 'D:/python/lda/data/data.xlsx'
output_file = 'D:/python/lda/data/data_cleaned1.xlsx'


try:
    df = pd.read_excel(input_file_path, header=None, names=['Weibo Post'])
except Exception as e:
    print(f"Error: {e}")
    exit()

# Apply the clean_text function to the 'Weibo Post' column
df['Cleaned Weibo Post'] = df['content'].apply(clean_text)

# Save the cleaned data to a new Excel file
df[['Cleaned Weibo Post']].to_excel(output_file_path, index=False)

print(f'Cleaned data saved to {output_file_path}')
