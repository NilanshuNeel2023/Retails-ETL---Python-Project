## 🛒 Retail ETL Project

## 📌 Project Overview

The **Retail ETL Project** is a Python-based data engineering project designed to implement an ETL (Extract, Transform, Load) pipeline for retail data.

The project extracts data related to features, sales, and stores, transforms it into structured dimension and fact tables, and loads the processed data into a MySQL database.

The objective is to organize retail data into a structured format that can support data analysis, reporting, and business intelligence.

## 🎯 Project Objectives

* Automate the ETL process using Python.
* Extract retail data from multiple data sources.
* Transform raw data into structured dimension and fact tables.
* Load processed data into a MySQL database.
* Organize retail data for further analysis and reporting.
* Build a modular and maintainable ETL pipeline.

## 🛠️ Technologies Used

* **Python** – ETL pipeline development
* **Pandas** – Data manipulation and transformation
* **MySQL** – Database storage
* **SQL** – Querying and managing structured data
* **Git & GitHub** – Version control and project management

## 🔄 ETL Pipeline Architecture

The project follows three main stages:

### 1. Extract

The extraction module retrieves the following datasets:

* Features Data
* Sales Data
* Store Data

### 2. Transform

The transformation module processes the extracted datasets and prepares four tables:

* `dim_date` – Date dimension table
* `dim_feature` – Feature dimension table
* `dim_store` – Store dimension table
* `fact_sales` – Sales fact table

This structure organizes the data into dimension and fact tables for analytical use.

### 3. Load

The loading module loads the transformed tables into MySQL for storage and further analysis.

**Pipeline workflow:**

`Extract Data → Transform Data → Load Data into MySQL`

## 📂 Project Structure

```text
Retail-ETL-Project/
│
├── main.py
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

*Note: Adjust the folder structure above to match your actual GitHub repository.*

## ⚙️ Installation and Setup

### Prerequisites

Make sure you have installed:

* Python 3.9 or later
* MySQL Server
* Git

### Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate to the project directory:

```bash
cd Retail-ETL-Project
```

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### Step 3: Install Dependencies

If your project contains a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

Ensure that the required Python packages and MySQL database connector are installed.

### Step 4: Configure MySQL

1. Start your MySQL server.
2. Create the target database.
3. Configure the database connection settings in your ETL loading module.
4. Ensure that the required tables and permissions are configured according to your implementation.

**Security note:** Keep database passwords and other credentials private. Use environment variables or a `.env` file, and never commit sensitive credentials to GitHub.

## ▶️ How to Run the Project

After completing the setup and database configuration, execute:

```bash
python main.py
```

The main script runs the ETL pipeline in the following sequence:

1. Starts the pipeline.
2. Extracts feature, sales, and store datasets.
3. Transforms the datasets into dimension and fact tables.
4. Loads the transformed tables into MySQL.
5. Displays a completion message when the loading function returns successfully.

Expected console output:

```text
Pipeline Started
Pipeline completed, Data loaded to MySQL Succesfully
```

The completion message reflects the current script's behavior; successful database loading depends on the extraction, transformation, and loading modules completing without errors.

## 📊 Database Design

The project organizes the transformed data into the following tables:

| Table         | Purpose                               |
| ------------- | ------------------------------------- |
| `dim_date`    | Stores date-related dimension data    |
| `dim_feature` | Stores feature-related dimension data |
| `dim_store`   | Stores store-related dimension data   |
| `fact_sales`  | Stores sales-related fact data        |

This dimensional structure can serve as a foundation for analytical queries, reporting, and business intelligence dashboards.

## 💡 Key Learning Outcomes

Through this project, I developed practical experience with:

* Designing a modular ETL pipeline in Python.
* Separating extraction, transformation, and loading logic.
* Working with multiple datasets in a single workflow.
* Organizing data into dimension and fact tables.
* Integrating Python-based data processing with MySQL.
* Structuring a data engineering project for version control and collaboration.

## 🚀 Future Improvements

* Add logging and detailed error handling.
* Implement data quality checks and validation.
* Automate scheduled pipeline execution.
* Optimize database loading performance.
* Add incremental data loading.
* Connect the MySQL database to Power BI for interactive retail dashboards.

## 👨‍💻 Author

**Nilanshu Vishwakarma**

GitHub: [Your GitHub Profile](https://github.com/)

Feel free to explore the project, share feedback, or suggest improvements.

---

⭐ If you find this project useful, consider giving the repository a star!
