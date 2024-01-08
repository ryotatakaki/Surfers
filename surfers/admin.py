from flask import Blueprint
from . import db
from .models import Category, Product, Order


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():
    category1 = Category(name='surfboards', image='board1 2.jpeg''' )
    category2 = Category(name='accesories', image='accesory 3.jpg''' )
    category3 = Category(name='swimsuites', image='wetsuit 2.jpeg''' )
      
    try:
        db.session.add(category1)
        db.session.add(category2)
        db.session.add(category3)
        db.session.commit()
    except:
        return 'There was an issue adding the cities in dbseed function'

    p1 = Product(category_id=category1.id, image='surfboard1.jpeg', price=980.50,\
        name='SHADOW XL',\
        description= 'The Shadow is one of the high-performance shortboards from the Ghost family. With the Phantom additional flow and glide are retained in the Shadow, a more streamlined, high-performance shortboard is here.') 
    p2 = Product(category_id=category1.id, image='kanoa 2.jpg', price=999.00,\
        name='LOST PUDDLE JUMPER PRO',\
        description= 'The Futures Fins John John Florence Techflex Thruster fin is a balanced fin with additional hardness that is ideal for powerful surfers and powerful waves. It comes in small, medium, and large sizes.')
    p3 = Product(category_id=category1.id, image='lostboard 2.jpg', price=999.00,\
        name='LOST RETRO TRIPPER',\
        description= 'The RETRO TRIPPER is inspired by the desire for a short and wide, with plenty of glide, fish alternative, for surfing punchy and powerful waves with confidence and control.')
    p4 = Product(category_id=category2.id, image='leash 2.jpg', price=74.95,\
        name='FCS FREEDOM HELIX LEASH - COMP 6 FT',\
        description= 'The Freedom Helix creates the perfect blend of weightlessness, strength and sustainability in a leash that is one of a kind. Featuring a 6 ft cord made from natural bio-resin, the Helix ups the performance levels by being lighter and faster than anything you’ve experienced.')                
    p5 = Product(category_id=category2.id, image='fin1.jpeg', price=148.20,\
        name='JOHN JOHN TECHFLEX TRI FINS',\
        description= 'John John Florence Techflex Thruster fin is a balanced fin with additional stiffness that is ideal for powerful surfers and powerful waves. It comes in small, medium, and large sizes. Ride all your boards using the same template as John John.')
    p6 = Product(category_id=category2.id, image='pad 2.jpg', price=65.15,\
        name='CREATURES OF LEISURE MICK FANNING : BLACK FADE CYAN',\
        description= 'A signature traction pad developed by Mick Fanning in response to his need for high-performance gear has won dozens of competitions and three World Championships. As a result, kicks and arches are more resistant and operate more expertly.')
    p7 = Product(category_id=category3.id, image='billabongboardshorts 2.jpg', price=99.99,\
        name='Billabong D Bah Airlite Boardshorts 19"',\
        description= 'In order to provide you with stability, flexibility, and comfort where you need it most, the Billabong D Bah Airlite Boardshorts 19" feature three distinct performance fabrics that have been seamlessly engineered into one. This includes Airlite Recycler Stretch, a sustainable material made from recycled plastic bottles. These surf basics have a fixed waist, an adjustable drawcord, and a rear patch pocket for all your needs.')
    p8 = Product(category_id=category3.id, image='spring 2.jpg', price=389.99,\
        name='Billabong 2/2 Revolution Chest Zip Steamer Wetsuit',\
        description= 'Billabong’s 2/2 Revolution Chest Zip Short Sleeve Full Wetsuit is made with stretchy and environmentally friendly neoprene, strategically placed seams, high-end materials and advanced construction for a perfect fit. The product is available in a variety of colors and sizes. This men’s short sleeve full suit has adhesive and is blind stitched for heat protection, and machine applied Super Flex Neotape adds extra stretch. A zipper at the chest provides an easy fit.')
    p9 = Product(category_id=category3.id, image='wetsuit.JPG', price=250.00,\
        name='2022 QUIKSILVER Mens Prologue 3/2mm Back Zip Wetsuit',\
        description= 'For an affordable price, the 3/2 Prologue Back Zip Wetsuit offers excellent stretch, warmth, and comfort. This revolutionary FreeMax and StretchFlight neoprene is used exclusively in the creation of this cold water complete suit to provide outstanding stretch, comfort, and warmth. With bonded and blind stitched seams and cutting-edge technology that traps your body heat, there is a tonne of water blockage here as well.')
   
    try:
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.add(p5)
        db.session.add(p6)
        db.session.add(p7)
        db.session.add(p8)
        db.session.add(p9)
        db.session.commit()
    except:
        return 'There was an issue adding a product in dbseed function'

    return 'DATA LOADED'
