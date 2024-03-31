#!/usr/bin/env python3

import os
from htmldom import htmldom
import requests
import pandas as pd
from config import *


def get_arxiv_papers(search_term='intrusion detection', start_year=2022, end_year=2024, size_per_page=200, order='-announced_date_first', max_results=1000, get_abstract=False):
    result_papers = []
    for i in range(0, max_results, 200):
        url = f'https://arxiv.org/search/advanced?advanced=1&terms-0-term={search_term}&terms-0-operator=AND&terms-0-field=all&classification-computer_science=y&classification-physics_archives=all&classification-include_cross_list=include&date-filter_by=date_range&date-year=&date-from_date={start_year}&date-to_date={end_year}&date-date_type=submitted_date&abstracts=show&size={size_per_page}&order={order}&start={i}'
        response = requests.get(url)
        print(f'Getting papers from {url}')
        dom = htmldom.HtmlDom().createDom(response.text)
        papers = dom.find('li.arxiv-result')
        for paper in papers:
            title = paper.find('p.title').text().strip()
            authors = paper.find('p.authors > a')
            abstract = paper.find('p.abstract > abstract-full').text().strip()
            result_authors = ', '.join([authors.text() for authors in authors]).strip()
            try:
                pdf_link = paper.find('div.is-marginless > p.list-title > span > a')[0].attr('href').strip()
            except:
                pdf_link = 'No PDF'
            paper_data = {
                'title': title,
                'authors': result_authors,
                'pdf_link': pdf_link
            }
            if get_abstract:
                paper_data['abstract'] = abstract
            result_papers.append(paper_data)
        
    df = pd.DataFrame(result_papers)
    df.to_excel('papers.xlsx', index=False)
    print('done')
    return result_papers

def download_papers(papers):
    # check if papers folder exists
    if not os.path.exists('papers'):
        os.makedirs('papers')
    for paper in papers:
        pdf_link = paper['pdf_link']
        title = paper['title'].replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').strip()

        # change title to os compatible file name
        title = title.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_')
        authors = paper['authors']
        print(pdf_link)

        # check if pdf link is not available
        if pdf_link == 'No PDF':
            print(f'{title} has no pdf')
            continue

        # check if content-length is less 0 (no pdf)
        head = requests.head(pdf_link)
        if 'Content-Length' in head.headers and int(head.headers['Content-Length']) < 100:
            print(f'{title} has no pdf')
            continue

        # download pdf
        response = requests.get(pdf_link)
        with open(f'papers/{title}.pdf', 'wb') as f:
            f.write(response.content)
        print(f'{title} downloaded')

if __name__ == '__main__':
    # import variables from config.py
    papers = get_arxiv_papers(search_term=search_term, start_year=start_year, end_year=end_year, size_per_page=size_per_page, order=order, max_results=max_results, get_abstract=get_abstract)
    if download_pdf:
        download_papers(papers)