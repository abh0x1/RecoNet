from flask import flash, url_for,session,redirect , Blueprint , render_template

main_bp = Blueprint('main',__name__)

@main_bp.route('/')
def welcome():
    if 'user_id' in session:
        return redirect(url_for('auth.logout'))
    return render_template('welcome.html')
        
        