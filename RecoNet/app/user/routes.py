from flask import Blueprint,render_template,session,redirect, url_for,flash

user_bp = Blueprint('user',__name__,url_prefix='/user')

@user_bp.route('/user_home')
def user_home():
    if 'user_id' not in session:
        flash("User not logged in , Please login!","error")
        return redirect(url_for('main.welcome'))
    flash("Sucessfully! Login","success")
    return render_template('user/dash.html')