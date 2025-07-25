from flask import Blueprint, render_template, request,flash,redirect,session,url_for
from .ipwhois import lookup_ip_whois

ipwhois_bp = Blueprint('ipwhois', __name__, url_prefix='/ipwhois')

@ipwhois_bp.route('/ipwhois_form')
def ipwhois_form():
    if 'user_id' not in session:
        flash('User not logged in.','error')
        return redirect(url_for('main.welcome'))
    return render_template('ipwhois/ipwhois_form.html')

@ipwhois_bp.route('/ip_lookup', methods=['POST','GET'])
def ip_lookup():
    if 'user_id' not in session:
        flash('User not logged in.','error')
        return redirect(url_for('main.welcome'))
    ip = request.form.get('ip')
    if not ip:
        return render_template('ipwhois/ipwhois_form.html', error="Please enter an IP address.")
    
    result = lookup_ip_whois(ip)
    return render_template('ipwhois/ipwhois_result.html', ip=ip, result=result)
