# Create admin file

from app import create_app , db
from app.models import Admin
from werkzeug.security import generate_password_hash

app = create_app()
app.app_context().push()

admin_name = "abhi"
admin_email = "admin@gmail.com"
admin_pass = "#admin1234"

dup_admin = Admin.query.filter_by(email=admin_email).first()

if dup_admin:
    print(f"Admin with email {admin_email} already exists.")
else:
    hash_pass = generate_password_hash(admin_pass)
    admin_user = Admin(
        username = admin_name,
        email=admin_email,
        password = hash_pass
    )
    
db.session.add(admin_user)
db.session.commit()
print(f"Admin user {admin_email} created successfully!")