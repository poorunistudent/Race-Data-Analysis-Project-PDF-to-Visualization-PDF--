import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('race_results.csv')
df['Diff_seconds'] = pd.to_numeric(df['Diff'], errors='coerce')

df_finishers = df.dropna(subset=['Diff_seconds'])

plt.figure(figsize=(10, 6))
plt.bar(df_finishers['Name'], df_finishers['Diff_seconds'], color='teal')
plt.xlabel('Driver Name')
plt.ylabel('Time Difference to leader (seconds)')
plt.title('Race Time Differences to Leader')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('race_diff_bar_chart.png')



