# finance-api

📘 Finance Data API — Flask Application

A simple and lightweight Flask-based REST API that provides:

✅ Company Information

✅ Real-Time Stock Market Data

✅ Historical Price Data

✅ Basic Analytical Insights

This project uses yfinance to fetch financial data and returns clean JSON responses that any frontend can consume.

🚀 Features
1. Company Information Endpoint

Retrieve company details such as:

Full company name

Industry

Sector

Business summary

Website

2. Real-Time Stock Data Endpoint

Fetch live market data:

Current price

Previous close

Price change

Percentage change

Day high & low

Volume

3. Historical Data Endpoint

Get OHLC (Open, High, Low, Close) values for any time period.

4. Simple Analytical Insights Endpoint

Performs a basic trend analysis:

Start vs end price

Percentage change

Uptrend or downtrend indicator

📁 Project Structure
finance-api/
│
├── app.py
├── README.md
└── requirements.txt

🛠 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/finance-api.git
cd finance-api

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Flask server
python app.py

4️⃣ Server Running On:
http://127.0.0.1:5000/

📦 API Endpoints & Usage
1️⃣ Company Information
GET /company-info?symbol=AAPL
Example Request:
http://127.0.0.1:5000/company-info?symbol=AAPL

Example Response:
{
  "symbol": "AAPL",
  "name": "Apple Inc.",
  "industry": "Consumer Electronics",
  "sector": "Technology",
  "summary": "Apple Inc. designs...",
  "website": "https://www.apple.com"
}

2️⃣ Real-Time Stock Data
GET /stock-data?symbol=TSLA
Example Request:
http://127.0.0.1:5000/stock-data?symbol=TSLA

Example Response:
{
  "symbol": "TSLA",
  "currentPrice": 189.23,
  "previousClose": 187.56,
  "change": 1.67,
  "percentChange": 0.89,
  "dayHigh": 192.30,
  "dayLow": 186.00,
  "volume": 123456789
}

3️⃣ Historical Price Data
POST /historical-data
Example JSON Body:
{
  "symbol": "AAPL",
  "start": "2023-01-01",
  "end": "2023-02-01"
}

Example Output:
[
  {
    "Date": "2023-01-03T00:00:00",
    "Open": 130.47,
    "High": 131.26,
    "Low": 124.17,
    "Close": 125.07,
    "Volume": 112117500
  }
]

4️⃣ Analytics Endpoint
POST /analysis
Example Body:
{
  "symbol": "AAPL",
  "start": "2023-01-01",
  "end": "2023-06-01"
}

Example Response:
{
  "symbol": "AAPL",
  "startPrice": 125.02,
  "endPrice": 178.30,
  "percentChange": 42.52,
  "insight": "Uptrend"
}

🧪 Testing via cURL
Company Info
curl "http://127.0.0.1:5000/company-info?symbol=GOOGL"

Real-Time Data
curl "http://127.0.0.1:5000/stock-data?symbol=MSFT"

Historical Data
curl -X POST "http://127.0.0.1:5000/historical-data" \
-H "Content-Type: application/json" \
-d '{"symbol":"AAPL","start":"2023-01-01","end":"2023-02-01"}'

Analysis
curl -X POST "http://127.0.0.1:5000/analysis" \
-H "Content-Type: application/json" \
-d '{"symbol":"TSLA","start":"2023-01-01","end":"2023-06-01"}'

🧾 Requirements

requirements.txt

Flask
yfinance
pandas


Install with:

pip install -r requirements.txt

🚀 Future Enhancements (Optional)

If you want to upgrade the API later:

Add RSI, MACD, EMA, SMA indicators

Add MongoDB / Postgres database

Add API key authentication

Convert to FastAPI with auto Swagger Docs

Deploy to Render / Railway / AWS

Just tell me and I’ll build the next version with you, Boss 😎🔥
