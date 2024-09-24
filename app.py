from flask import Flask, redirect, render_template, jsonify, request, url_for
import yfinance as yf
from database import filter_stocks, get_all_stocks, init_db, data_fields, insert_or_update_stock_data, update_signals_for_all_stocks
from config import bist_tickers

app = Flask(__name__)

def fetch_stock_data():
    for ticker in bist_tickers:
        ticker = ticker + ".IS"
        stock = yf.Ticker(ticker)
        info = stock.info
        
        print(f"Fetching data for {ticker}...")
        data = {field: info.get(yfinance_key) for field, yfinance_key in data_fields.items()}
        data['ticker'] = ticker

        insert_or_update_stock_data(ticker, data)

# Veritabanını başlat
init_db()

@app.route('/')
def index():
    column_names, data = get_all_stocks()
    return render_template('index.html', column_names=column_names, data=data)

@app.route('/filter', methods=['POST'])
def filter_stocks_route():
    filters = request.json
    data = filter_stocks(filters)
    column_names, _ = get_all_stocks()  # Sütun isimlerini al
    return jsonify({'columns': column_names, 'stocks': data})

@app.route('/fetch_data')
def fetch_data_route():
    fetch_stock_data()  # Yeni veriyi çek
    column_names, data = get_all_stocks()  # Güncellenmiş veriyi al
    return jsonify({'columns': column_names, 'stocks': data})

@app.route('/update_signals', methods=['POST'])
def update_signals():
    try:
        update_signals_for_all_stocks()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
    
if __name__ == '__main__':
    app.run(debug=True, port=3535)