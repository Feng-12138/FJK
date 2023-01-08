from faker import Faker
import json
import uuid
import random
import math
import pymongo
import os
import certifi
from werkzeug.security import generate_password_hash


path = os.environ['MONGODB_URI']
mongoClient = pymongo.MongoClient(path, tlsCAFile=certifi.where(), uuidRepresentation="standard",)

Faker.seed(0)
fake = Faker(['en_US'])

cloth_info_list = []

cloth_id_list = []

brand_id_list = []

picture_urls_4 = ['/_next/static/media/4001672806245_.pic.79677ebf.jpg', '/_next/static/media/3991672806245_.pic.e5f91ebd.jpg', '/_next/static/media/4001672806245_.pic.79677ebf.jpg', '/_next/static/media/3991672806245_.pic.e5f91ebd.jpg']

picture_urls_3 = ['/_next/static/media/4011672806264_.pic.eb68dc53.jpg', '/_next/static/media/4001672806245_.pic.79677ebf.jpg', '/_next/static/media/3991672806245_.pic.e5f91ebd.jpg']

color_list = ["grey", "wood", "red", "black", "brown", "smoke", "navy blue"]

material_list = ["nylon", "cottom", "wool", "silver", "bronze"]

main_categories = ['Accessories', 'Clothing', 'Shoes']

sub_categories = ["Jackets & Coats", "Pants", "Shirts", "Shorts", "Sweaters", "Sneakers", "Boots", 'jewelry']

available_list = [True, False]

name_list = ['Black Attachment Turtle Neck Warmer', 'Black Stripe Ponte T-Shirt', 'Plain-woven cotton shorts', 'Black Nylon Shorts', 'Black OOFOS Edition "Way Of Life" Flip Flops', 'Silver Bone Ring']

size_list = ['XS', "S", "M", "L", "XL"]

order_status_list = ['error', 'order received', 'shipping', 'delivered', 'expired', 'returned']

amount_list = [1, 2, 3]

shopping_cart_id_list = []
wish_list_id_list = []
user_id_list = []
order_id_list = []
address_id_list = []

clothing_info_list = []
brand_info_list = []
user_info_list = []
order_info_list = []
shopping_info_list = []
wish_list_info_list = []
address_info_list = []
shopping_cart_info_list = []

def produce_clothing_info_list():
    clothing_id_list = []
    cloth_info_list = []
    for _ in range(3):
        clothing_id_list.append(random.choice(cloth_id_list))
    clothing_id_list = list(dict.fromkeys(clothing_id_list))
    for id in clothing_id_list:
        info_dict = {}
        amount = random.choices(amount_list, weights=[5, 1, 1], k=1)[0]
        size = random.choice(size_list)
        info_dict["clothing_id"] = id
        info_dict['amount'] = amount
        info_dict['size'] = size
        cloth_info_list.append(info_dict)
        
    return cloth_info_list




for _ in range(20):
    brand_id = uuid.uuid4()
    brand_id_list.append(brand_id)

for idx in range(500):
    cloth_id = uuid.uuid4()
    cloth_id_list.append(cloth_id)
    brand_idx = math.floor(idx / 25)
    brand_id = brand_id_list[brand_idx]
    if (idx % 2):
        picture_urls = picture_urls_3
    else:
        picture_urls = picture_urls_4
    
    clothing_name = random.choice(name_list)
    price_normal = random.randint(20, 600)
    price_sale = math.ceil(random.uniform(0.4, 0.9) * price_normal)
    color = random.choices(color_list, k=3)
    color = list(dict.fromkeys(color))
    material = random.choice(material_list)
    category = random.choice(sub_categories)
    description = fake.paragraph(nb_sentences=5)
    time = fake.date_time_ad()
    # available = random.choices(available_list, weights=[5, 1], k=1)[0]
    xs_amount = random.randint(0, 20)
    s_amount = random.randint(0, 20)
    m_amount = random.randint(0, 20)
    l_amount = random.randint(0, 20)
    xl_amount = random.randint(0, 20)
    clothing_info = {
        
    }
    clothing_info['_id'] = cloth_id
    clothing_info['clothing_id'] = cloth_id
    clothing_info['brand_id'] = brand_id
    clothing_info['clothing_name'] = clothing_name
    clothing_info['price_normal'] = price_normal
    clothing_info['price_sale'] = price_sale
    clothing_info['color'] = color
    clothing_info['material'] = material
    clothing_info['category'] = category
    clothing_info['description'] = description
    clothing_info['time_uploaded'] = time
    clothing_info['xs_amount'] = xs_amount
    clothing_info['s_amount'] = s_amount
    clothing_info['m_amount'] = m_amount
    clothing_info['l_amount'] = l_amount
    clothing_info['xl_amount'] = xl_amount
    # clothing_info['available'] = available
    clothing_info_list.append(clothing_info)
    
    
for idx in range(20):
    brand_info = {
        
    }
    
    clothing_id_list = []
    len_clothing = math.floor(len(cloth_id_list) / len(brand_id_list))
    for idx_1 in range(len_clothing):
        clothing_id_list.append(cloth_id_list[idx * len_clothing + idx_1])
    
    brand_info['_id'] = brand_id_list[idx]
    brand_info['brand_id'] = brand_id_list[idx]
    brand_info['clothing_id_list'] = clothing_id_list
    brand_info['brand_name'] = fake.company()
    brand_info['brand_description'] = fake.paragraph(nb_sentences=5)
    brand_info_list.append(brand_info)
    
        
    
for _ in range(100):
    user_id = uuid.uuid4()
    user_id_list.append(user_id)
    
for idx in range(400):
    order_info = {}
    order_id = uuid.uuid4()
    order_id_list.append(order_id)
    user_idx = math.floor(idx / 4)
    user_id = user_id_list[user_idx]
    cloth_info_list = produce_clothing_info_list()
    order_info['_id'] = order_id
    order_info['order_id'] = order_id
    order_info['user_id'] = user_id
    order_info['cloth_info_list'] = cloth_info_list
    order_info['order_time'] = fake.date_time_ad()
    order_info['order_status'] = random.choice(order_status_list)
    if (order_info['order_status'] == 'delivered' or order_info['order_status'] == 'expired' or order_info['order_status'] == 'returned'):
        order_info['delivered_time'] = fake.date_time_ad()
    else:
        order_info['delivered_time'] = None
    order_info_list.append(order_info)
    
for idx in range(300):
    address_info = {}
    address_id = uuid.uuid4()
    address_id_list.append(address_id)
    receiver_name = fake.name()
    street_address = '40 Rue du Syrah'
    city = "Kirkland"
    province = "Québec"
    country = "Canada"
    post_code = "H9H 0B1"
    phone_number = fake.phone_number()
    address_info['_id'] = address_id
    address_info['address_id'] = address_id
    address_info['user_id'] = random.choice(user_id_list)
    address_info['receiver_name'] = receiver_name
    address_info['street_address'] = street_address
    address_info['city'] = city
    address_info['province'] = province
    address_info['country'] = country
    address_info['post_code'] = post_code
    address_info['phone_number'] = phone_number
    address_info_list.append(address_info)
    
    
for idx in range(100):
    user_info = {}
    user_id = user_id_list[idx]
    email = "y598sun@uwaterloo.ca"
    password = generate_password_hash("2005yyds")
    order_list = []
    for idx_2 in range(4):
        order_id = order_id_list[idx * 4 + idx_2]
        order_list.append(order_id)
    for idx_3 in range(3):
        address_id = address_id_list[idx * 3 + idx_3]
        address_id_list.append(address_id)
    
    deliver_address_id = random.choice(address_id_list)
    billing_address_id = random.choice(address_id_list)
    user_info['_id'] = user_id
    user_info['user_id'] = user_id
    user_info['email'] = email
    user_info['password'] = password
    user_info['order_ids'] = order_list
    user_info['address_id_list'] =  address_id_list
    user_info['deliver_address_id'] = deliver_address_id
    user_info['billing_address_id'] = billing_address_id
    user_info_list.append(user_info)
    
    
    
for idx in range(100):
    wish_list_info = {}
    user_id = user_id_list[idx]
    cloth_info_list = produce_clothing_info_list()
    wish_list_info['_id'] = user_id
    wish_list_info['user_id'] = user_id
    wish_list_info['cloth_info_list'] = cloth_info_list
    wish_list_info_list.append(wish_list_info)
    
for idx in range(100):
    shopping_cart_info = {
    }
    user_id = user_id_list[idx]
    cloth_info_list = produce_clothing_info_list()
    shopping_cart_info['_id'] = user_id
    shopping_cart_info['user_id'] = user_id
    shopping_cart_info['cloth_info_list'] = cloth_id_list
    shopping_cart_info_list.append(shopping_cart_info)
    



with mongoClient.start_session() as session:
    database = session.client.get_database('customer_facing')
    try:
        database.address.insert_many(address_info_list)
        database.brands.insert_many(brand_info_list)
        database.clothing.insert_many(clothing_info_list)
        database.order.insert_many(order_info_list)
        database.shopping_cart.insert_many(shopping_cart_info_list)
        database.user.insert_many(user_info_list)
        database.wishlist.insert_many(wish_list_info_list)
        
    except Exception as e:
        print(e)
    
    
    
