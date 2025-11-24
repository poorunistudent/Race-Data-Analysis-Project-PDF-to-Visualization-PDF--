# Race-Data-Analysis-Project-PDF-to-Visualization-PDF--
This project demonstrates a complete data pipeline written in Python, covering extraction, cleaning, transformation, and visualization of raw race results from a PDF file.

for English scrol down

რბოლის მონაცემთა ანალიზი: PDF-დან ვიზუალიზაციამდე
ეს პროექტი წარმოადგენს Python-ზე დაწერილ სრულ მონაცემთა მილსადენს (data pipeline), რომელიც მოიცავს ნედლი სარბოლო შედეგების ამოღებას, გაწმენდას, ტრანსფორმაციას და ვიზუალიზაციას PDF ფაილიდან.


პროექტის ფაილები
ფაილის სახელი	აღწერა
Race_2.pdf	წყარო მონაცემები, რომელიც შეიცავს დაუზუსტებელ რბოლის შედეგებს.
Race_Differences.py / main.py	მთავარი Python სკრიპტი, რომელიც გამოიყენება დამუშავების ყველა ეტაპისთვის.
race_results.csv	გაწმენდილი, სტრუქტურირებული მონაცემები. ეს ფაილი ინახავს რბოლის შედეგებს ცხრილის ფორმატში, რომელიც გამოსადეგია ანალიზისთვის.
race_diff_bar_chart.png	საბოლოო მონაცემთა ვიზუალიზაცია, რომელიც აჩვენებს დროის სხვაობებს მძღოლებს შორის.

პროცესის მიმოხილვა (3 ძირითადი ეტაპი)
1. მონაცემთა ამოღება და წინასწარი დამუშავება
მიზანი: PDF ფაილიდან არასტრუქტურირებული ტექსტის წაკითხვა.
ინსტრუმენტები: pdfplumber ბიბლიოთეკა გამოყენებული იქნა Race_2.pdf ფაილის გასახსნელად და მთელი ტექსტის ამოსაღებად.
გამოწვევა: ამოღებული ტექსტი იყო არეული, აკლდა მკაფიო გამყოფები და ჰქონდა არათანმიმდევრული ფორმატირება (განსაკუთრებით ფინიშზე გასული და პენსიაზე გასული მძღოლებისთვის).

2. მონაცემთა გაწმენდა და ტრანსფორმაცია
მიზანი: არეული ტექსტის სტრუქტურირებულ, რიცხვით ცხრილად გადაქცევა.
ინსტრუმენტები: re და pandas ბიბლიოთეკები იყო აუცილებელი.
პროცესი:
რეგულარული გამოსახულების ნიმუში (Regex pattern) განისაზღვრა, რათა ზუსტად ამომეღო მონაცემების თითოეული ნაწილი (პოზიცია, მანქანის ნომერი, სახელი, საერთო დრო და ა.შ.) ყოველი ხაზიდან.
შედეგები ჩაიტვირთა pandas DataFrame-ში.
Diff (განსხვავება) სვეტი კონვერტირდა რიცხვით ტიპად, არასარაცხობი ჩანაწერებით ("8 Laps"-ის მსგავსად) გადაკეთდა NaN-ად, რათა მონაცემები მომზადებულიყო გრაფიკისთვის.

3. ვიზუალიზაცია
მიზანი: რბოლის შედეგების მკაფიო ვიზუალური წარმოდგენის შექმნა.
ინსტრუმენტები: matplotlib ბიბლიოთეკა გამოყენებული იქნა გრაფიკების შესაქმნელად.
შედეგი: შეიქმნა სვეტოვანი დიაგრამა (bar chart), რომელიც ასახავს დროის სხვაობას ლიდერთან (Diff სვეტი) ყველა ფინიშზე გასული მძღოლისთვის. ეს ვიზუალიზაცია სწრაფად წარმოაჩენს შესრულების ხარვეზებს სარბოლო მოედანზე.


Race Data Analysis Project: PDF to Visualization
This project demonstrates a complete data pipeline written in Python, covering extraction, cleaning, transformation, and visualization of raw race results from a PDF file.

Project Files
File Name	Description
Race_2.pdf	The source data file containing the raw, unstructured race results.
Race_Differences.py / main.py	The main Python script used for all processing steps.
race_results.csv	The cleaned, structured data. This file stores the race results in a tabular format suitable for analysis.
race_diff_bar_chart.png	The final data visualization, showing the time differences between drivers.
Process Overview (The 3 Key Steps)
1. Data Extraction and Pre-processing
Goal: Read the unstructured text from the PDF file.
Tools: The pdfplumber library was used to open the Race_2.pdf file and extract all text content.
Challenge: The extracted text was messy, lacking clear separators, and had inconsistent formatting (especially for drivers who finished vs. those who retired).

2. Data Cleaning and Transformation
Goal: Convert the messy text into a structured, numerical table.
Tools: The re (Regular Expressions) library and pandas were essential here.
Process:
A Regular Expression pattern was defined to accurately capture each piece of data (Position, Car Number, Name, Total Time, etc.) from every line.
The results were loaded into a pandas DataFrame.
The Diff (difference) column was explicitly converted to a numerical type, with non-numerical entries (like "8 Laps") converted to NaN to prepare the data for plotting.

3. Visualization
Goal: Create a clear visual representation of the race results.
Tools: The matplotlib library was used for plotting.
Result: A bar chart was generated to visualize the Time Difference to the Leader (Diff column) for all finishing drivers. This visualization quickly highlights the gaps in performance across the field.


