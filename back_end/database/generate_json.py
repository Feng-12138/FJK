from faker import Faker
import json
import uuid
import random
import math

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

shopping_cart_id_list = []
wish_list_id_list = []
user_id_list = []
order_id_list = []

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
    available = random.choices(available_list, weights=[5, 1], k=1)[0]
    clothing_info = {
        
    }
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
    clothing_info['available'] = available
    
for idx in range(20):
    brand_info = {
        
    }
    
    clothing_id_list = []
    len_clothing = math.floor(len(cloth_id_list) / len(brand_id_list))
    for idx_1 in range(len_clothing):
        clothing_id_list.append(cloth_id_list[idx * len_clothing + idx_1])
    
    brand_info['brand_id'] = brand_id
    brand_info['clothing_id_list'] = clothing_id_list
    
for _ in range(400):
    order_id = uuid.uuid4()
    order_id_list.append(order_id)
    

for _ in range(100):
    user_id = uuid.uuid4()
    user_id_list.append(user_id)
    
    
    
    # print(available)
    
    
    
    
    
    
    
    

for _ in range(5):
    fake.paragraph(nb_sentences=5)
    

