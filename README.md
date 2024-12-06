<h1 align="center" style="font-weight: bold;"> FINANCIAL TRANSACTIONS PROCESSING APP 💳</h1>

<div align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff" alt="Python Badge" width="100">
    <img src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=fff" alt="Pandas Badge" width="100">
    <img src="https://img.shields.io/badge/SQL-F29111?logo=postgresql&logoColor=fff" alt="SQL Badge" width="100">
  </a>
</div>

<br>
<p align="center">
   <strong>
This project processes financial transaction data, user information, and card details from CSV files and generates SQL scripts for inserting the data into a relational database. It provides a practical example of ETL (Extract, Transform, Load) in Python using Pandas and basic SQL scripting.
   </strong>
</p>

---

## **Features**
- 📊 **Data Transformation**: Handles null values and special characters to ensure data consistency.
- 📝 **SQL Generation**: Produces SQL INSERT statements for seamless database integration.
- 📂 **Custom CSV Input**: Allows processing of any compatible financial data in CSV format.

---

## **Technologies Used 💻**
- **Python**: For scripting and data manipulation.
- **Pandas**: To process and clean data from CSV files.
- **SQL**: For generating database-compatible scripts.

---

## **Getting Started**

### **Install Dependencies**
Run the following command to install Pandas in your environment:
```bash
pip install pandas
```

# Usage
### 1. Clone this repository to your local machine:
```bash
git clone https://github.com/ThiagoRosa21/FinancialTransactionsApp
```
### 2. Navigate to the project folder:
```
cd FinancialTransactionsApp
```
### 3. Place your CSV files in the folder. Ensure they follow the required format:
Users Data: Contains client information.
Cards Data: Includes credit card details.
Transaction Data: Records financial transactions.

### 4. Modify the script to point to your CSV files and run the Python scripts:
```bash
python process_users_data.py
python process_cards_data.py
python process_transactions.py
```
### 5. The generated SQL scripts will be saved in the project folder.
``` bash
FinancialTransactionsApp/
│
├── process_users_data.py    # Script to process user data
├── process_cards_data.py    # Script to process card data
├── process_transactions.py  # Script to process transactions
├── users_data.csv           # Example CSV for users
├── cards_data.csv           # Example CSV for cards
├── transactions_data.csv    # Example CSV for transactions
├── inserts/                 # Folder for SQL scripts output
│   ├── Users_Inserts.sql
│   ├── Cards_Inserts.sql
│   └── Transactions_Inserts.sql
```
## Contributing
Feel free to open issues or contribute to this project by submitting pull requests. For major changes, please open a discussion first to ensure the changes align with the project goals.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
