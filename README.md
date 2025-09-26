### Software and Platforms Used

* **Primary Software:**
  Python, executed within Jupyter and Google Colab notebooks.

* **Required Packages:**
  The following Python libraries were imported and used for analysis and visualization:

  ```python
  import requests
  import xml.etree.ElementTree as ET
  from bs4 import BeautifulSoup
  import json
  import pandas as pd
  import re
  import matplotlib.pyplot as plt
  import seaborn as sns
  ```

* **Platforms:**
  The project was conducted on both **Windows** and **Mac** operating systems.


  Project_Folder/
│
├── Data/
│   ├── raw_data.csv
│   ├── cleaned_data.csv
│   └── metadata.json
│
├── Scripts/
│   ├── data_cleaning.py
│   ├── web_scraper.py
│   └── utils.py
│
├── Results/
│   ├── figures/
│   │   ├── correlation_plot.png
│   │   └── heatmap.png
│   └── tables/
│       ├── summary_statistics.xlsx
│       └── regression_results.csv
│
├── Documentation/
│   ├── project_report.docx
│   ├── references.bib
│   └── software_and_platforms.txt
│
└── README.md
