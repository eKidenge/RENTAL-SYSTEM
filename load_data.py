import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Guest.settings')
django.setup()

from user.models import User, Room, House

def load_sample_data():
    print("📊 Loading sample property data...")
    
    # Get or create a test user
    user, created = User.objects.get_or_create(
        email='test@example.com',
        defaults={
            'name': 'Test User',
            'location': 'Test Location',
            'city': 'Test City',
            'state': 'Test State',
            'number': 9876543210
        }
    )
    
    # Sample rooms
    rooms_data = [
        {
            'user_email': user,
            'dimention': '12 x 10',
            'location': 'Westlands',
            'city': 'Nairobi',
            'state': 'KE',
            'cost': 42500,
            'bedrooms': 2,
            'kitchen': 'Yes',
            'hall': 'Yes',
            'balcany': 'Yes',
            'desc': 'MODERN APARTMENT WITH SECURITY AND LIFT',
            'AC': 'No',
            'img': 'room_id/default.jpg'
        },
        {
            'user_email': user,
            'dimention': '10 x 8',
            'location': 'Kilimani',
            'city': 'Nairobi',
            'state': 'KE',
            'cost': 31000,
            'bedrooms': 1,
            'kitchen': 'Yes',
            'hall': 'No',
            'balcany': 'No',
            'desc': 'SEMI-FURNISHED QUIET APARTMENT',
            'AC': 'No',
            'img': 'room_id/default.jpg'
        }
    ]
    
    for data in rooms_data:
        Room.objects.get_or_create(
            room_id=None,  # AutoField will generate
            defaults=data
        )
    
    # Sample houses
    houses_data = [
        {
            'user_email': user,
            'area': 1200,
            'floor': 2,
            'location': 'Karen',
            'city': 'Nairobi',
            'state': 'KE',
            'cost': 120000,
            'bedrooms': 4,
            'kitchen': 2,
            'hall': 'Yes',
            'balcany': 'Yes',
            'desc': 'BUNGALOW WITH LARGE PLOT',
            'AC': 'Yes',
            'img': 'house_id/default.jpg'
        },
        {
            'user_email': user,
            'area': 800,
            'floor': 1,
            'location': 'Runda',
            'city': 'Nairobi',
            'state': 'KE',
            'cost': 87500,
            'bedrooms': 3,
            'kitchen': 1,
            'hall': 'Yes',
            'balcany': 'Yes',
            'desc': 'GATED COMMUNITY HOUSE',
            'AC': 'Yes',
            'img': 'house_id/default.jpg'
        }
    ]
    
    for data in houses_data:
        House.objects.get_or_create(
            house_id=None,  # AutoField will generate
            defaults=data
        )
    
    print("✅ Sample data loaded successfully!")

if __name__ == '__main__':
    load_sample_data()