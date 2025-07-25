from flask import url_for,flash,session,render_template,redirect,Blueprint,request
from app.models import db, User
from werkzeug.security import generate_password_hash

admin_bp = Blueprint('admin',__name__,url_prefix='/admin')

@admin_bp.route('/admin_home')
def admin_home():
    if 'email' not in session:
        flash('Unauthorized Access!','error')
        return redirect(url_for('main.welcome'))
    flash("Login Sucessfully!","success")
    return render_template('admin/dash.html')

@admin_bp.route('/manage_users')
def manage_users():
    if 'email' not in session:
        flash('Unauthorized Access!','error')
        return redirect(url_for('main.welcome'))
    users = User.query.all()
    return render_template('admin/users.html',users=users)

@admin_bp.route('/add_user_form')
def add_user_form():
    if 'email' not in session:
        flash('Unauthorized Access!','error')
        return redirect(url_for('main.welcome'))
    return render_template('admin/add_user.html')  # You'll need this template

@admin_bp.route('/users/create', methods=['POST'])
def create_user():
    if 'email' not in session:
        flash('Unauthorized Access!','error')
        return redirect(url_for('main.welcome'))
    
    username = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upasswd')

    if not username or not email or not password:
        flash("All fields are required!", "error")
        return redirect(url_for('admin.add_user_form'))

    check_user = User.query.filter_by(email=email).first()
    if check_user:
        flash("User already exists!", "warning")
    else:
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("User created successfully!", "success")

    return redirect(url_for('admin.manage_users'))

@admin_bp.route('/update_user_form')
def update_user_form():
    if 'email' not in session:
        flash('Unauthorized Access!','error')
        return redirect(url_for('main.welcome'))
    return render_template('admin/update_user.html')

@admin_bp.route('/update_user', methods=['POST'])
def update_user():
    if 'email' not in session:
        flash('Unauthorized Access!','error')
        return redirect(url_for('main.welcome'))
    
    
    email = request.form.get('email')
    new_name = request.form.get('name')
    new_email = request.form.get('new_email')
    new_password = request.form.get('password')
    user = User.query.filter_by(email=email).first()

    if user:
        user.username = new_name
        user.email = new_email
        if new_password:
            user.password = generate_password_hash(new_password)
        db.session.commit()
        
        flash(f"User updated successfully!", "success")
    else:
        flash("User not found!", "danger")
    return redirect(url_for('admin.update_user_form'))


@admin_bp.route('/delete_user_form')
def delete_user_form():
    if 'email' not in session:
        flash('Unauthorized Access!','error')
        return redirect(url_for('main.welcome'))
    return render_template('admin/delete_user.html')


@admin_bp.route('/delete_user', methods=['POST'])
def delete_user():
    if 'email' not in session:
        flash('Unauthorized Access!','error')
        return redirect(url_for('main.welcome'))
    email = request.form.get('email')
    user = User.query.filter_by(email=email).first()

    if user:
        db.session.delete(user)
        db.session.commit()
        flash(f"User with email {email} deleted!", "info")
    else:
        flash("User not found!", "danger")
    return redirect(url_for('admin.delete_user_form'))