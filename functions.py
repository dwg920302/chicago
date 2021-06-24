import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from icecream import ic
import folium
import googlemaps
import numpy as np
from tqdm import tqdm


def make_data():
    url_pre = 'https://www.chicagomag.com/Chicago-Magazine/November-2012'
    url_suf1 = '/Best-Sandwiches-Chicago/'
    url_suf2 = '/Best-Sandwiches-in-Chicago-'
    header = {'User-Agent': 'Mozilla/5.0'}
    framed_data = []

    cols = ['Rank', 'Menu', 'Rst', 'Price', 'Addr']

    url = url_pre + url_suf1
    soup = BeautifulSoup(urlopen(Request(url, headers=header)), 'lxml')
    unpacked_data = soup.find_all('div', 'sammy')

    for i in unpacked_data:
        url = url_pre + url_suf2 + str(i.find('a')['href']).split('Best-Sandwiches-in-Chicago-')[1]
        soup = BeautifulSoup(urlopen(Request(url, headers=header)), 'lxml')
        raw = soup.find('em').text
        framed_data.append([i.find('div', 'sammyRank').text,
                            i.find('div', 'sammyListing').text.split('\n')[0],
                            i.find('div', 'sammyListing').text.split('\n')[1],
                            raw.split()[0],
                            ' '.join(raw.split()[1:-2])])
    ic(framed_data)

    df = pd.DataFrame(framed_data, columns=cols)
    ic(df)

    gmaps = googlemaps.Client('AIzaSyCaM2VXqJxXpB0b5_teQBl-dUFDkRYHhWo')

    lat = []
    lng = []

    for n in tqdm(df.index):
        if df['Addr'][n] != 'Multiple':
            target_name = df['Addr'][n] + ', ' + 'Chicago'
            gmaps_output = gmaps.geocode(target_name)
            location_output = gmaps_output[0].get('geometry')
            lat.append(location_output['location']['lat'])
            lng.append(location_output['location']['lng'])
        else:
            lat.append(np.nan)
            lng.append(np.nan)

    df['lat'] = lat
    df['lng'] = lng

    return df


def show_map(df):
    mapping = folium.Map(location=[df['lat'].mean(), df['lng'].mean()],
                         zoom_start=11)
    folium.Marker([df['lat'].mean(), df['lng'].mean()],
                  popup='center').add_to(mapping)
    for n in df.index:
        if df['Addr'][n] != 'Multiple':
            folium.Marker([df['lat'][n], df['lng'][n]],
                          popup=df['Rst'][n]).add_to(mapping)
    folium.LayerControl().add_to(mapping)

    mapping.save("data_saved/chicago_sandwich_mat_zip.html")
