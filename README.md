This is a command line app. What it does convert a CSV file into a regular data file to make it easier to read. I included random CSV data files to test it with.

# CSV Column Formatter (Native Python)

A lightweight Python utility designed to clean and restructure CSV data using the standard library. This tool automates the process of extracting specific substrings from data rows and reorganizing the column order for better data management.

## 🚀 Overview
I developed this script to handle data cleaning tasks without the need for heavy external dependencies. It demonstrates how to use Python's built-in `csv` module to perform complex data transformations, making it highly portable and efficient.

## ✨ Key Features
* **Zero Dependencies:** Runs on standard Python 3.x—no `pip install` required.
* **String Parsing:** Efficiently slices strings to isolate key identifiers (e.g., extracting ID prefixes).
* **Structural Reorganization:** Dynamically reorders columns, moving processed data to the primary index.
* **Streamlined Output:** Automatically generates a formatted `changed_file.csv` ready for use.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Module:** `csv` (Standard Library)

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/jradcode/change_csv_file.git](https://github.com/jradcode/change_csv_file.git)
   cd change_csv_file
