# Srape and download Papers from arxiv.org

Installation: 
```bash
pip install -r requirements.txt
```

Edit the config.py file to set the search query and the number of papers to download   
```python
search_term='intrusion detection system'
start_year=2022
end_year=2024
size_per_page=200
order='-announced_date_first' # announcement date (newest first)
max_results=1000
get_abstract = False
download_pdf = False
```


Running: 
```python
python scrap.py
```
