# Setup & Installation Guide

## Prerequisites
- Python 3.7 or higher
- Git (for cloning the repository)

## Step 1: Clone the Repository
```bash
git clone <repository-url>
cd MoMo-SMS-Financial-Insights-Platform
```

## Step 2: Install Dependencies
This project uses only Python standard library modules - **no external packages required**.

```bash
# Optional: Create a virtual environment (recommended)
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

## Step 3: Prepare Data
Ensure `raw/momo.xml` exists in the repository with SMS transaction data.

## Step 4: Run the ETL Pipeline
Process the XML SMS data into JSON format:

```bash
# On macOS/Linux:
bash scripts/run_etl.sh

# On Windows:
python3 etl/run.py
```

**Output:** `data/transactions.json` (contains parsed transactions)

## Step 5: Start the API Server
Serve the dashboard and provide API access:

```bash
# On macOS/Linux:
bash scripts/serve_frontend.sh

# On Windows:
python3 api/app.py
```

**Access Dashboard:** http://localhost:8000
**Credentials:** 
- Username: `admin`
- Password: `admin123`

## Troubleshooting

### Issue: `ModuleNotFoundError` or missing modules
**Solution:** All required modules are part of Python's standard library. Make sure you're using Python 3.7+
```bash
python3 --version
```

### Issue: `raw/momo.xml` not found
**Solution:** The XML file must be present in the `raw/` directory. Make sure:
1. The file exists in your cloned repository
2. The path is correct: `raw/momo.xml` (relative to repo root)

### Issue: Permission denied when running `.sh` scripts
**Solution:** Make scripts executable:
```bash
chmod +x scripts/*.sh
bash scripts/run_etl.sh
```

### Issue: Address already in use (Port 8000)
**Solution:** The API server is already running. Stop the current process and try again:
```bash
# Find the process using port 8000 and kill it
# Then run the server again
python3 api/app.py
```

## Project Structure
```
MoMo-SMS-Financial-Insights-Platform/
├── raw/                    # Raw XML SMS data
├── data/                   # Processed JSON transactions
├── etl/                    # ETL pipeline (XML → JSON)
├── api/                    # REST API server
├── web/                    # Frontend assets
├── dsa/                    # Data structure algorithms
├── tests/                  # Unit tests
├── scripts/                # Utility scripts
└── README.md              # Project documentation
```

## Next Steps
1. Run the ETL pipeline to generate transaction data
2. Start the API server
3. Open http://localhost:8000 in your browser
4. Log in with admin credentials
5. View financial insights dashboard

## For Developers
- Run tests: `python3 -m pytest tests/`
- View API docs: See `docs/api_docs.md`
- Check DSA analysis: See `docs/DSA_ANALYSIS.md`

---
**Note:** Paths are calculated relative to the repository root, so this works on any machine after cloning.
