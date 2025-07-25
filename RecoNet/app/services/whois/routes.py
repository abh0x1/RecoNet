from flask import Blueprint,render_template,request,redirect,url_for,flash,session
from app.services.whois.whois import whois_lookup

whois_bp = Blueprint('whois',__name__,url_prefix='/whois')


@whois_bp.route('/whois_form')
def whois_form():
    if 'user_id' not in session:
        flash('User not logged in.','error')
        return redirect(url_for('main.welcome'))

    return render_template('whois/form.html')

@whois_bp.route('/whois_result', methods=['GET','POST'])
def whois_result():
    if 'user_id' not in session:
        flash('User not logged in.','error')
        return redirect(url_for('main.welcome'))
    if request.method == "POST":
        domain = request.form.get('domain')
        if domain:
            data = whois_lookup(domain)
            return render_template('whois/result.html',data=data)
        else:
            return "No domain names"
        
    return render_template('whois/form.html')
