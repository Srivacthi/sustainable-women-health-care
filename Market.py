from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Eco-friendly Cotton Pads (20ct)', 'barcode': 9375628461, 'price': 10}, 
        {'id': 2, 'name': 'No-plastic Lipstick (.12oz)', 'barcode': 4729472593, 'price': 15}, #choose color
        {'id': 3, 'name': 'PureSilk Reusable Facial Rounds (12ct)', 'barcode': 2749274927, 'price': 12},
        {'id': 4, 'name': 'Refillable Mascara (.10oz)', 'barcode': 3856284618, 'price': 14},
        {'id': 5, 'name': 'Vegan Lip Balm (.15oz)', 'barcode': 7438255364, 'price': 10}, #choose flavors
        {'id': 6, 'name': '100% Wooden-Metal Recyclable Razors (3-pack)', 'barcode': 6553873647, 'price': 15},
        {'id': 7, 'name': 'EcoLush Menstrual Cups (2-pack)', 'barcode': 9276443589, 'price': 16},
        {'id': 8, 'name': 'PureEarth Charcoal Mud Face Mask (12oz)', 'barcode': 4264742145, 'price': 28},
        {'id': 9, 'name': 'PureEarth Amazonian White Clay Mask (5oz)', 'barcode': 9376624347, 'price': 22},
        {'id': 10, 'name': 'Biodegradable Aloe Vera + Hyaluronic Acid Under-Eye Masks (15 pairs)', 'barcode': 8465387563, 'price': 16},
        {'id': 11, 'name': 'Ahimsa Silk SleepWear Set (Top + Bottom)', 'barcode': 1385729494, 'price': 222},
        {'id': 12, 'name': 'Natural Deodorant Plastic-Free Aluminum-Free (4.5oz)', 'barcode': 5747421578, 'price': 14} #Various scents (e.g., lavender, citrus, unscented
    ]
    return render_template('market.html', items=items)

@app.route('/impact')
def impact_page():
    return render_template('impact.html', item_name = "Phone")

