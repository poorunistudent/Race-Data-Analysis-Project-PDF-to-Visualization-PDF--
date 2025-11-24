import pdfplumber
import re
import pandas as pd

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text

race_text = extract_text_from_pdf("Race 2.pdf")
print(race_text)

lines = race_text.strip().split('\n')

header_line =lines[0]
data_lines = lines[1:]
print(header_line)

columns = ['Pos', 'No.', 'Name', 'Class', 'Laps', 'Total_Time', 'Diff', 'Gap']

# 4. Use a Regular Expression to parse each line
data = []
# ...
pattern = re.compile(r'(\d+)\s+(\d+)\s+([A-Za-z\s]+)\s+([A-Z0-9]+)\s+(\d+)\s+([\d:]+\.?\d*)\s*(.*)')

for line in data_lines:
    match = pattern.match(line.strip())
    if match:
        row = list(match.groups())
        
        # Split the remaining data (Diff, Gap, or Laps Behind text)
        remaining = row.pop()
        
        # Handle the two main patterns:
        if 'Laps' in remaining:
            # For drivers who didn't finish (e.g., '8 Laps')
            row.extend([remaining.strip(), None])
        elif remaining:
            # For finished drivers (Diff and Gap values)
            diff_gap_values = [v.strip() for v in remaining.split()]
            if len(diff_gap_values) >= 2:
                row.extend(diff_gap_values[:2])
            # ... (omitted edge cases for brevity)
        else:
            # For the 1st place driver, Diff and Gap are empty
            row.extend([None, None])
            
        data.append(row)

        # 5. Create the DataFrame
df = pd.DataFrame(data, columns=columns)

# ... printing and checking ...

# 6. Save the DataFrame to a CSV file
output_file = 'race_results.csv'
df.to_csv(output_file, index=False)
