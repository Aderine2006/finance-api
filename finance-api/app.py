from flask import Flask, request, jsonify
import yfinance as yf

app = Flask(__name__)

# ----------------------------------------------------
# 1. Company Information Endpoint
# ----------------------------------------------------
@app.route("/company-info", methods=["GET"])
def company_info():
    symbol = request.args.get("symbol")

    if not symbol:
        return jsonify({"error": "Symbol is required"}), 400

    stock = yf.Ticker(symbol)
    info = stock.info

    return jsonify({
        "symbol": symbol,
        "name": info.get("longName"),
        "industry": info.get("industry"),
        "sector": info.get("sector"),
        "summary": info.get("longBusinessSummary"),
        "website": info.get("website")
    })


# ----------------------------------------------------
# 2. Real-Time Stock Market Data Endpoint
# ----------------------------------------------------
@app.route("/stock-data", methods=["GET"])
def stock_data():
    symbol = request.args.get("symbol")

    if not symbol:
        return jsonify({"error": "Symbol is required"}), 400

    stock = yf.Ticker(symbol)
    info = stock.info

    return jsonify({
        "symbol": symbol,
        "currentPrice": info.get("regularMarketPrice"),
        "previousClose": info.get("regularMarketPreviousClose"),
        "change": info.get("regularMarketChange"),
        "percentChange": info.get("regularMarketChangePercent"),
        "dayHigh": info.get("dayHigh"),
        "dayLow": info.get("dayLow"),
        "volume": info.get("volume")
    })


# ----------------------------------------------------
# 3. Historical Market Data Endpoint
# ----------------------------------------------------
@app.route("/historical-data", methods=["POST"])
def historical_data():
    data = request.json
    symbol = data.get("symbol")
    start = data.get("start")
    end = data.get("end")

    if not symbol or not start or not end:
        return jsonify({"error": "symbol, start, end are required"}), 400

    stock = yf.Ticker(symbol)
    hist = stock.history(start=start, end=end)

    return jsonify(hist.reset_index().to_dict(orient="records"))


# ----------------------------------------------------
# 4. Analytical Insights Endpoint (Very Simple Version)
# ----------------------------------------------------
@app.route("/analysis", methods=["POST"])
def analysis():
    data = request.json
    symbol = data.get("symbol")
    start = data.get("start")
    end = data.get("end")

    if not symbol or not start or not end:
        return jsonify({"error": "symbol, start, end are required"}), 400

    stock = yf.Ticker(symbol)
    hist = stock.history(start=start, end=end)

    if hist.empty:
        return jsonify({"error": "No historical data found"}), 404

    # Simple insights
    first_price = hist["Close"].iloc[0]
    last_price = hist["Close"].iloc[-1]
    percent_change = ((last_price - first_price) / first_price) * 100

    insight = "Uptrend" if percent_change > 0 else "Downtrend"

    return jsonify({
        "symbol": symbol,
        "startPrice": float(first_price),
        "endPrice": float(last_price),
        "percentChange": float(percent_change),
        "insight": insight
    })


# ----------------------------------------------------
# Root
# ----------------------------------------------------
@app.route("/")
def home():
    return jsonify({"message": "Simple Finance API is running!"})


if __name__ == "__main__":
    app.run(debug=True)
