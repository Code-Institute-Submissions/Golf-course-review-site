from .time import Time
import time
from bson.objectid import ObjectId

class Record:
    
    @staticmethod   
    def find_value(obj,key):
    #Finds the value of certain key/value pair passed in
        value = []
        for fields in obj:
            value.append(fields[key]) 
        return value

    @staticmethod   
    def find_single_value(obj,key):
    #Finds the value of certain key/value pair passed in
        value = obj.get(key)
        return value
    
    @staticmethod
    def update_kv(obj,key,value):
        #Updates a key value pair with new value
        obj[key] = value
        return obj
    
    @staticmethod
    def return_list(obj):
    #Returns list of items in collection
        records = []
        for record in obj:
            records += [record]
        return records
    
    @staticmethod
    def create_course_record(obj):
    #Creates a dictionary from the form fields
        data = {
        'course_name':obj.get('course_name'),
        'address_line_1':obj.get('address_line_1'),
        'address_line_2': obj.get('address_line_2'),
        'address_line_3': obj.get('address_line_3'),
        'region': obj.get('region'),
        'postcode': obj.get('postcode'),
        'course_img': obj.get('course_img'),
        'affiliate_link': obj.get('affiliate_link'),
        'avg_rating': 0,
        'par': int(obj.get('par')),
        'description': obj.get('description')
        }
        return data

    @staticmethod
    def create_review_record(obj,user,course):
    #Creates a dictionary from the form fields
        data = {
        'user_id': ObjectId(user),
        'date': time.time(),
        'star_rating': int(obj.get('star_rating')),
        'review_title': obj.get('review_title'),
        'review_article': obj.get('review_article'),
        'course_id': ObjectId(course)
        }
        return data
    
    @staticmethod
    #Removes duplicates from list due to conversion to dict and then back
    def find_course_ids(obj):
        data = Record.find_value(obj, 'course_id')
        data = list(dict.fromkeys(data))

        return data
    

    @staticmethod
    def convert_time(obj):
        
        records = []
        for record in obj:
            unix_time = Record.find_single_value(record, "date")
            print(unix_time)
            date_val = Time.return_time(unix_time)
            updated = Record.update_kv(record,"date",date_val)
            records.append(updated)
        
        return records
    
    @staticmethod
    #find the sum of ratings and return avg rating (rounded)
    def average_rating(obj):
        data = Record.find_value(obj,"star_rating")
        total = 0
        for val in data:
            total += val
        
        average = round(total / len(data))

        return average




        
