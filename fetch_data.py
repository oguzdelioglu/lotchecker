import yfinance as yf
from database import insert_data, create_database

# Hisse sembollerini tanımla
tickers = ['AKBNK.IS', 'GARAN.IS', 'ISCTR.IS']  # BIST hisselerini buraya ekle

# Veritabanını oluştur
create_database()

# Hisse verilerini çekme ve veritabanına ekleme
for ticker in tickers:
    stock = yf.Ticker(ticker)
    info = stock.info
    insert_data(ticker, info)