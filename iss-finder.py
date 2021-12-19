import pandas
import plotly.express as px
import sys

#dont need to include requests library since direct api access now possible

url = 'http://api.open-notify.org/iss-now.json'

data_frame = pandas.read_json(url)

#json from url has headers iss_position which contains lat and long respectively

if(data_frame.loc['latitude', 'message'] == "failure" or data_frame.loc['longitude', 'message'] == "failure"):
    print("There was an error retrieving ISS location.")
    sys.exit()
else:
    data_frame['latitude'] = data_frame.loc['latitude', 'iss_position']
    data_frame['longitude'] = data_frame.loc['longitude', 'iss_position']

    data_frame.reset_index(inplace=True)

    data_frame = data_frame.drop(['index', 'message'], axis = 1) #dont need index header

    fig1 = px.scatter_geo(data_frame, lat = 'latitude', lon = 'longitude') # geographical scatter plot
    
    fig1.update_geos(resolution=50, showcountries=True) #shows country borders
    fig1.update_geos(projection_type="natural earth", locationmode='country names')
    fig1.update_traces(marker=dict(
                size=10, color='Crimson')
    )

    fig1.show() #will open in browser
    
