# 🎬 BoomTown Productions—Expense ETL Pipeline

A Python-based ETL (Extract, Transform, Load) pipeline built to track and manage department-wise expenses for a film production project based in **Dubai**. Raw data from 4 departments is cleaned, combined, and loaded into a MySQL database.

---

## 📌 What It Does

| Stage | Script | Description |
|-------|--------|-------------|
| Extract & Transform | `read.py` | Reads raw CSVs, validates columns, computes costs, saves cleaned files |
| Combine | `outcome.py` | Merges all department data into one unified expense record |
| Load | `load_to_mysql.py` | Inserts the combined data into a MySQL database |

---

## 🗂️ Project Structure

```
BoomTown/
│
├── RAW DATA/                        # Input files (you provide these)
│   ├── catering_log.csv
│   ├── camera_dept.csv
│   ├── transport_dubai.csv
│   └── talent_payouts.csv
│
├── PROCESSED_DATA/                  # Auto-created by read.py
│   ├── Cleaned_catering.csv
│   ├── Cleaned_camera_dept.csv
│   ├── Cleaned_Transport_Dubai.csv
│   └── Cleaned_Talent_Payout.csv
│
├── Combined_Record/                 # Create this folder manually
│   └── combined_expenses.csv        # Auto-created by outcome.py
│
├── read.py                          # Stage 1 — Clean raw data
├── outcome.py                       # Stage 2 — Combine departments
└── load_to_mysql.py                 # Stage 3 — Load to MySQL
```

---

## 🧪 Raw Data Format

Each CSV in `RAW DATA/` must have these columns:

**catering_log.csv**
`Date, Vendor, Meal_Type, Headcount, Price_Per_Head`

**camera_dept.csv**
`Date, Item_Name, Daily_Rate, Days, Total_Cost`

**transport_dubai.csv**
`Date, Vehicle_Type, Fuel_AED, Salik_Tolls, Driver_OT_Hours`

**talent_payouts.csv**
`Actor_Name, Role, Agency, Contract_Fee, Status`

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Toufiq1806/BoomTown-Productions-Expense-ETL-Pipeline.git
cd BoomTown-Productions-Expense-ETL-Pipeline
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up the MySQL database
```sql
CREATE DATABASE BoomTown;
USE BoomTown;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT,
    department VARCHAR(50),
    amount DECIMAL(10,2),
    expense_date DATE
);
```

### 4. Update your database credentials
Open `load_to_mysql.py` and update:
```python
con = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="YOUR_PASSWORD",  # your password
    database="BoomTown",
)
```

---

## ▶️ How to Run

Run the three scripts **in order**:

```bash
# Step 1 — Clean and validate raw data
python read.py

# Step 2 — Merge all departments into one file
python outcome.py

# Step 3 — Load into MySQL
python load_to_mysql.py
```

---

## 🔢 Business Logic

| Department | Cost Calculation |
|-----------|-----------------|
| Camera | `Total_Cost = Daily_Rate × Days` |
| Catering | `Total_Spend = Headcount × Price_Per_Head` |
| Transport | `Total = Fuel_AED + Salik_Tolls + (Driver_OT_Hours × 50 AED)` |
| Talent | `Contract_Fee` (excludes rows with Status = "pending") |

---

## 🛠️ Tech Stack

- **Python 3**
- **Pandas** — data cleaning and transformation
- **PyMySQL** — MySQL database connection
- **MySQL** — expense data storage

---

## 📋 Requirements

```
pandas
pymysql
```

> Make sure MySQL is running locally before executing `load_to_mysql.py`.

---

## 👤 Author

Made by **Mohamed Toufiq** — feel free to connect on [LinkedIn](https://linkedin.com/in/mohamed-toufiq-1a31a13a7/)
