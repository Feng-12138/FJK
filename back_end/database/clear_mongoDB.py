import pymongo
import os
import certifi
path = os.environ['MONGODB_URI']
mongoClient = pymongo.MongoClient(path, tlsCAFile=certifi.where(), uuidRepresentation="standard",)

with mongoClient.start_session() as session:
    address = session.client.get_database(
      'customer_facing').address
    brands = session.client.get_database(
      'customer_facing').brands
    clothing = session.client.get_database(
      'customer_facing').clothing
    order = session.client.get_database('customer_facing'
    ).order
    shopping_cart = session.client.get_database('customer_facing'
    ).shopping_cart
    user = session.client.get_database(
      'customer_facing').user
    wishlist = session.client.get_database('customer_facing'
    ).wishlist
    try:
        address.delete_many({})
        brands.delete_many({})
        clothing.delete_many({})
        order.delete_many({})
        shopping_cart.delete_many({})
        user.delete_many({})
        wishlist.delete_many({})
    except Exception as e:
        print(e)
        
        
    
    
    