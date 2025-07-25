from flask import Flask,flash,redirect,render_template,url_for,render_template,session,Blueprint,request
from app.models import User,db,Admin
from werkzeug.security import generate_password_hash,check_password_hash
from email_validator import validate_email, EmailNotValidError

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/user_signup_form')
def user_signup_form():
    return render_template('auth/signup.html')

@auth_bp.route('/user_signup', methods=['GET','POST'])
def user_signup():
    if request.method == 'POST':
        username = request.form['uname']
        email = request.form['uemail']
        password = request.form['upasswd']
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered.', 'errorde')
            return redirect(url_for('auth.user_signup'))
        
        hashed_password = generate_password_hash(password)
        
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Signup successful. Please log in.', 'success')
        return redirect(url_for('auth.user_login'))
    
    return render_template('auth/signup.html')


@auth_bp.route('/user_login_form')
def user_login_form():
    return render_template('auth/login.html')

@auth_bp.route('/user_login', methods=['POST','GET'])
def user_login():
    if request.method == 'POST':
        email = request.form['uemail']
        password = request.form['upasswd']
        
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['user_type'] = 'user'
            return redirect(url_for('user.user_home'))
        else:
            flash('Invalid credentials', 'danger')
    
    return render_template('auth/login.html')
        
@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully.","info")
    return redirect(url_for('main.welcome'))


@auth_bp.route('/admin_form',methods=['GET'])
def admin_form():
    return render_template('admin/login.html')

@auth_bp.route('/admin_login',methods=['GET','POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form.get('uemail')
        passwd = request.form.get('upasswd')
        
        
        if not email or not passwd:
            flash('Email and Password are required', 'danger')
            return redirect(url_for('auth.admin_form'))


        admin = Admin.query.filter_by(email=email).first()
        if admin and check_password_hash(admin.password,passwd):
            session['id'] = admin.id
            session['user_type'] = 'admin'
            session['email'] = admin.email
            return redirect(url_for('admin.admin_home'))
        else:
            flash('Invalid admin credentials','danger')
    return redirect(url_for('auth.admin_form'))