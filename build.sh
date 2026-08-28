#!/usr/bin/env bash
echo "🚀 Starting build process for RENTAL-SYSTEM..."

# 1. Remove everything - database and all migrations
echo "🧹 Cleaning up..."
rm -f db.sqlite3
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# 2. Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# 3. Create and apply migrations
echo "📝 Creating migrations..."
python manage.py makemigrations user --noinput
python manage.py makemigrations --noinput

echo "🗄️  Applying migrations..."
python manage.py migrate --noinput

# 4. Load initial data
echo "📊 Loading initial data..."
python load_data.py

# 5. Collect static files
echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

# 6. Force create superuser
echo "👤 Creating superuser..."
python manage.py shell << EOF
from user.models import User

# Delete existing admin if exists
User.objects.filter(email='admin@admin.com').delete()

# Create fresh superuser
User.objects.create_superuser(
    email='admin@admin.com',
    name='System Administrator',
    number=1234567890,
    password='admin123'
)
print('✅ Superuser created: admin@admin.com / admin123')

# Create test user
User.objects.create_user(
    email='test@example.com',
    name='Test User',
    location='Test Location',
    city='Test City',
    state='Test State',
    number=9876543210,
    password='test123'
)
print('✅ Test user created: test@example.com / test123')
EOF

echo "✅ Build completed successfully!"
echo "========================================"
echo "🔑 Superuser: admin@admin.com"
echo "🔑 Password: admin123"
echo "========================================"