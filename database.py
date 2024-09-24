import sqlite3

# Veri sözlüğü ve sinyal hesaplamalarını içerir
data_fields = {
    'fiyat': 'currentPrice',
    'dusuk52': 'fiftyTwoWeekLow',
    'yuksek52': 'fiftyTwoWeekHigh',
    'ort200': 'twoHundredDayAverage',
    'hacim3ay': 'averageVolume',
    'ort50': 'fiftyDayAverage',
    'hacim10gun': 'averageVolume10days',
    'hisse_adet': 'sharesOutstanding',
    'tahmini_hisse': 'impliedSharesOutstanding',
    'kurum_oran': 'heldPercentInstitutions',
    'iceriden_oran': 'heldPercentInsiders',
    'halka_acik': 'floatShares',
    'gelir': 'totalRevenue',
    'net_gelir': 'netIncomeToCommon',
    'nakit': 'totalCash',
    'borc': 'totalDebt',
    'nakit_hisse': 'totalCashPerShare',
    'gelir_hisse': 'revenuePerShare',
    'kar_marji': 'profitMargins',
    'favok': 'ebitda',
    'piyasa_deger': 'marketCap',
    'defter_deger': 'bookValue',
    'hisse_basina_kazanc': 'trailingEps'  # Hisse başına kazanç için yeni alan
}

signal_fields = {
    'fiyat_puan': 'Price Status',
    'pd_dd_puan': 'Book Value Rating',
    'pd_dd': 'Price to Book Ratio',
    'fk_orani': 'Price to Earnings Ratio'  # F/K oranı için yeni alan
}

def get_db_connection():
    return sqlite3.connect('bist_stocks.db')

def check_and_add_columns():
    conn = get_db_connection()
    c = conn.cursor()
    
    c.execute('PRAGMA table_info(stocks)')
    existing_columns = [info[1] for info in c.fetchall()]

    all_fields = {**data_fields, **signal_fields}
    for field in all_fields.keys():
        if field not in existing_columns:
            c.execute(f'ALTER TABLE stocks ADD COLUMN {field} REAL')

    conn.commit()
    conn.close()

def create_table():
    conn = get_db_connection()
    c = conn.cursor()
    
    all_fields = {**data_fields, **signal_fields}
    columns = ", ".join([f"{col} REAL" for col in all_fields.keys()])
    c.execute(f'''
        CREATE TABLE IF NOT EXISTS stocks (
            ticker TEXT PRIMARY KEY,
            {columns}
        )
    ''')
    conn.commit()
    conn.close()

def calculate_price_status(fiyat, dusuk52, yuksek52, ort50, ort200):
    if None in (fiyat, dusuk52, yuksek52, ort50, ort200):
        return None

    distance_to_low = (fiyat - dusuk52) / (yuksek52 - dusuk52)
    distance_to_avg_50 = (fiyat - ort50) / ort50
    distance_to_avg_200 = (fiyat - ort200) / ort200

    score = (distance_to_low + distance_to_avg_50 + distance_to_avg_200) / 3
    fiyat_puan = max(1, min(100, 100 - (score * 100)))
    return round(fiyat_puan)

def calculate_price_to_book_ratio(fiyat, defter_deger):
    if None in (fiyat, defter_deger) or defter_deger == 0:
        return None
    return fiyat / defter_deger

def calculate_book_value_rating(pd_dd):
    if pd_dd is None:
        return None
    pd_dd_puan = max(1, min(100, 100 - (pd_dd * 10)))  # 10 ile çarparak daha geniş bir aralık elde ediyoruz
    return round(pd_dd_puan)

def calculate_ebitda(data):  
    if data.get('favok') is not None:
        return data['favok']
    return None

def calculate_price_to_earnings_ratio(fiyat, hisse_basina_kazanc):
    if None in (fiyat, hisse_basina_kazanc) or hisse_basina_kazanc == 0:
        return None
    return fiyat / hisse_basina_kazanc

def update_signals_for_all_stocks():
    conn = get_db_connection()
    c = conn.cursor()

    c.execute(f"SELECT ticker, {', '.join(data_fields.keys())} FROM stocks")
    stocks = c.fetchall()

    for stock in stocks:
        ticker = stock[0]
        stock_data = dict(zip(data_fields.keys(), stock[1:]))

        fiyat_puan = calculate_price_status(
            stock_data.get('fiyat'),
            stock_data.get('dusuk52'),
            stock_data.get('yuksek52'),
            stock_data.get('ort50'),
            stock_data.get('ort200')
        )

        pd_dd = calculate_price_to_book_ratio(
            stock_data.get('fiyat'),
            stock_data.get('defter_deger')
        )

        pd_dd_puan = calculate_book_value_rating(pd_dd)

        favok = calculate_ebitda(stock_data)

        fk_orani = calculate_price_to_earnings_ratio(
            stock_data.get('fiyat'),
            stock_data.get('hisse_basina_kazanc')
        )

        c.execute('''
            UPDATE stocks
            SET fiyat_puan = ?, pd_dd = ?, pd_dd_puan = ?, favok = ?, fk_orani = ?
            WHERE ticker = ?
        ''', (fiyat_puan, pd_dd, pd_dd_puan, favok, fk_orani, ticker))

    conn.commit()
    conn.close()

def insert_or_update_stock_data(ticker, data):
    conn = get_db_connection()
    c = conn.cursor()

    fiyat_puan = calculate_price_status(
        data.get('fiyat'),
        data.get('dusuk52'),
        data.get('yuksek52'),
        data.get('ort50'),
        data.get('ort200')
    )

    pd_dd = calculate_price_to_book_ratio(
        data.get('fiyat'),
        data.get('defter_deger')
    )

    pd_dd_puan = calculate_book_value_rating(pd_dd)

    favok = calculate_ebitda(data)

    fk_orani = calculate_price_to_earnings_ratio(
        data.get('fiyat'),
        data.get('hisse_basina_kazanc')
    )

    data['fiyat_puan'] = fiyat_puan
    data['pd_dd'] = pd_dd
    data['pd_dd_puan'] = pd_dd_puan
    data['fk_orani'] = fk_orani
    if favok is not None:
        data['favok'] = favok

    columns = ', '.join(data.keys())
    placeholders = ', '.join(['?'] * len(data))
    
    c.execute(f'''
        INSERT OR REPLACE INTO stocks ({columns})
        VALUES ({placeholders})
    ''', list(data.values()))

    conn.commit()
    conn.close()

def get_all_stocks():
    conn = get_db_connection()
    c = conn.cursor()
    
    c.execute("SELECT * FROM stocks")
    column_names = [description[0] for description in c.description]
    data = c.fetchall()
    
    conn.close()
    return column_names, data

def filter_stocks(filters):
    conn = get_db_connection()
    c = conn.cursor()
    
    query = "SELECT * FROM stocks WHERE 1=1"
    params = []
    
    if 'hisse_adet' in filters and filters['hisse_adet'] != 'all':
        min_shares, max_shares = map(lambda x: int(x) if x else None, filters['hisse_adet'].split(','))
        if min_shares is not None and max_shares is not None:
            query += " AND hisse_adet >= ? AND hisse_adet <= ?"
            params.extend([min_shares, max_shares])
        elif min_shares is not None:
            query += " AND hisse_adet > ?"
            params.append(min_shares)
    
    if 'fiyat_puan' in filters and filters['fiyat_puan'] != 'all':
        min_price_status, max_price_status = map(int, filters['fiyat_puan'].split(','))
        query += " AND fiyat_puan >= ? AND fiyat_puan <= ?"
        params.extend([min_price_status, max_price_status])
    
    if 'pd_dd_puan' in filters and filters['pd_dd_puan'] != 'all':
        min_book_value_rating, max_book_value_rating = map(int, filters['pd_dd_puan'].split(','))
        query += " AND pd_dd_puan >= ? AND pd_dd_puan <= ?"
        params.extend([min_book_value_rating, max_book_value_rating])
    
    if 'fk_orani' in filters and filters['fk_orani'] != 'all':
        min_fk_orani, max_fk_orani = map(float, filters['fk_orani'].split(','))
        query += " AND fk_orani >= ? AND fk_orani <= ?"
        params.extend([min_fk_orani, max_fk_orani])
    
    c.execute(query, params)
    data = c.fetchall()
    conn.close()
    return data

def init_db():
    create_table()
    check_and_add_columns()
    update_signals_for_all_stocks()

if __name__ == "__main__":
    init_db()