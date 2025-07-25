from flask import Blueprint,render_template,request,session,redirect,url_for,flash
from geopy.geocoders import Nominatim
from app.services.geopy.geotool import GeoTool

geopy_bp = Blueprint('geopy',__name__,url_prefix='/geopy')

geo = GeoTool()

@geopy_bp.route('/geopy_form',methods=['GET','POST'])
def geopy_form():
    if 'user_id' not in session:
        flash('User not logged in.','error')
        return redirect(url_for('main.welcome'))

    return render_template('geopy/geopy_form.html')

@geopy_bp.route('/geopy_lookup',methods=['GET','POST'])
def geopy_lookup():
    if 'user_id' not in session:
        flash('User not logged in.','error')
        return redirect(url_for('main.welcome'))

    if request.method == "POST":
        city1 = request.form.get('city1')
        city2 = request.form.get('city2')
        coord1 = request.form.get('coord1')
        coord2 = request.form.get('coord2')
        city2_coord1 = request.form.get('city2_coord1')
        city2_coord2 = request.form.get('city2_coord2')
        
        try:
            coord1 = float(coord1) if coord1 else None
            coord2 = float(coord2) if coord2 else None
            city2_coord1 = float(city2_coord1) if city2_coord1 else None
            city2_coord2 = float(city2_coord2) if city2_coord2 else None
        except:
            return "Invalid Coordinates!"
        
        
        if city1:
            cord_by_city = geo.get_coordinates(city1)
        else:
            cord_by_city = None
        
        if coord1 and coord2:
            reverse_cord = geo.reverse_lookup(coord1, coord2)
        else:
            reverse_cord = None

        if city1 and city2:
            dist_cities = geo.get_distance_by_name(city1, city2)
            if dist_cities:
                dist_cities = round(dist_cities,2)
        else:
            dist_cities = None

        if coord1 and coord2:
            cord_to_city = geo.get_city_from_coords(coord1, coord2)
        else:
            cord_to_city = None

        if coord1 and coord2 and city2_coord1 and city2_coord2:
            dist_by_cord = geo.get_distance_by_coords(coord1, coord2, city2_coord1, city2_coord2)
            if dist_by_cord:
                dist_by_cord = round(dist_by_cord,2)
        else:
            dist_by_cord = None

        return render_template('geopy/geopy_result.html',
                                cord_by_city=cord_by_city,
                               reverse_cord=reverse_cord,
                               dist_cities=dist_cities,
                               cord_to_city=cord_to_city,
                               dist_by_cord=dist_by_cord,
                               cord1=coord1,
                               cord2 = coord2,
                               city1=city1,
                               city2=city2,
                               city2_coord1=city2_coord1,
                               city2_coord2=city2_coord2
                               )
            
    return render_template('geopy/geopy_form.html')

