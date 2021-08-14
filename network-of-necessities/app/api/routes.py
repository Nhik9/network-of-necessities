from flask import render_template
from app import current_app
import folium
from folium.plugins import MarkerCluster
import pandas as pd
import io
import os

# Sample Data including geographical location
data = """Name,Address,Lat,Lon
EU,"Rue de la Loi/Wetstraat 175, Brussel, Belgium",50.842313,4.382300
Apple,"1 Apple Park Way, Cupertino, CA",37.329428,-122.010258
Google,"1600 Amphitheatre Parkway Mountain View, CA 94043",37.422058,-122.084090
UN,"760 United Nations Plaza; Manhattan, New York City",40.748898,-73.968209
"""
current_dir = os.path.abspath ('..')
print(current_dir)
template_dir = current_dir +  '/network-of-necessities/app/templates/'
@current_app.route('/')
def mapview():
    # creating a map in the view
    df = pd.read_csv ( io.StringIO ( data ) )
    map = folium.Map( location=df[['Lat' , 'Lon']].mean ().to_list () , tiles='Stamen Terrain', zoom_start=2 )
    marker_cluster = MarkerCluster ().add_to ( map )
    for i , r in df.iterrows () :
        location = (r['Lat'] , r['Lon'])
        folium.Marker ( location=location ,
                        popup=r['Name'] ,
                        tooltip=r['Name'] ) \
            .add_to ( marker_cluster )
    map.save(template_dir + 'map.html')
    return render_template('index.html')


if __name__ == "__main__":
    current_app.run(debug=True)