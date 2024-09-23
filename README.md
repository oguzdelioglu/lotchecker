# BIST Hisse Senedi Verileri Uygulaması

Bu proje, Borsa İstanbul (BIST) hisse senetleri hakkında güncel veriler sunan ve bu verileri filtrelemeye olanak tanıyan bir web uygulamasıdır.

## Özellikler

- BIST hisse senetleri için güncel veri görüntüleme
- Hisse adedi, fiyat puanı ve PD/DD puanına göre filtreleme
- Verileri ve sinyalleri güncelleme özelliği

## Teknolojiler

- Backend: Python, Flask
- Frontend: HTML, JavaScript
- Veritabanı: SQLite
- Veri Kaynağı: Yahoo Finance API (yfinance)

## Kurulum

1. Repoyu klonlayın:
   ```
   git clone https://github.com/oguzdelioglu/lotchecker.git
   ```

2. Gerekli Python paketlerini yükleyin:
   ```
   pip install -r requirements.txt
   ```

3. Uygulamayı çalıştırın:
   ```
   python app.py
   ```

4. Tarayıcınızda `http://localhost:3535` adresine gidin.

## Kullanım

- Ana sayfada tüm hisse senetleri ve ilgili veriler görüntülenir.
- Filtreleme seçeneklerini kullanarak verileri daraltabilirsiniz.
- "Verileri Güncelle" butonuyla en son verileri çekebilirsiniz.
- "Sinyalleri Güncelle" butonuyla hesaplanan değerleri yenileyebilirsiniz.

## Katkıda Bulunma

Pull request'ler kabul edilmektedir. Büyük değişiklikler için, lütfen önce neyi değiştirmek istediğinizi tartışmak üzere bir konu açınız.

## Lisans

[MIT](https://choosealicense.com/licenses/mit/)

---

# BIST Stock Data Application

This project is a web application that provides up-to-date data on Borsa Istanbul (BIST) stocks and allows filtering of this data.

## Features

- Display current data for BIST stocks
- Filter by number of shares, price score, and P/B score
- Option to update data and signals

## Technologies

- Backend: Python, Flask
- Frontend: HTML, JavaScript
- Database: SQLite
- Data Source: Yahoo Finance API (yfinance)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/oguzdelioglu/lotchecker.git
   ```

2. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Go to `http://localhost:3535` in your browser.

## Usage

- The main page displays all stocks and related data.
- Use the filtering options to narrow down the data.
- Click "Update Data" to fetch the latest data.
- Click "Update Signals" to recalculate the computed values.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
