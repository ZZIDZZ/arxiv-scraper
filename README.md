
# Arxiv Paper Scraper

Scrape and download academic papers from arXiv.org effortlessly! This tool is designed for researchers, students, and anyone interested in quickly obtaining batch of papers from arXiv.org based on specific search criteria.

## Installation

Ensure you have Python installed on your system and then follow these steps:

```bash
git clone https://github.com/ZZIDZZ/arxiv-scraper.git
pip install -r requirements.txt
```

## Configuration

Before running the scraper, you need to set up your search criteria in the `config.py` file:

```python
# Configuration for your search query and download preferences
search_term = 'intrusion detection system'
start_year = 2022
end_year = 2024
size_per_page = 200
order = '-announced_date_first'  # Sort by announcement date (newest first)
max_results = 1000
get_abstract = False  # Set to True if you want to download abstracts
download_pdf = False  # Set to True if you want to download PDFs
```

## Usage

To start scraping, simply run:

```bash
python scrap.py
```

The script will start fetching the papers based on your specified criteria in `config.py`.

## Contributing

Your contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open source and available under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Acknowledgements

Special thanks to [arXiv](https://arxiv.org/) for maintaining an incredible resource for the academic community.

---

Please feel free to open an issue or submit a pull request.


