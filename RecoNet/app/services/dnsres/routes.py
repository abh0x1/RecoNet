

from flask import Blueprint, render_template, request,flash,session,redirect,url_for
from .dnsres import resolve_dns

dns_bp = Blueprint('dns', __name__, url_prefix='/dns')

@dns_bp.route('/dns_form')
def dns_form():
    if 'user_id' not in session:
        flash('User not logged in.','error')
        return redirect(url_for('main.welcome'))
    return render_template('dnsres/dnsres_form.html')

@dns_bp.route('/dns_lookup', methods=['POST'])
def dns_lookup():
    if 'user_id' not in session:
        flash('User not logged in.','error')
        return redirect(url_for('main.welcome'))
    domain = request.form.get('domain')
    if not domain:
        return render_template('dnsres/dnsres_form.html', error="Please enter a domain.")
    
    records = resolve_dns(domain)
    return render_template('dnsres/dnsres_result.html', domain=domain, records=records)
