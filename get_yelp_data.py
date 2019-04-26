from yelpapi import YelpAPI
import json
from fuzzywuzzy import fuzz

def getYelpData():
    count=0
    # File containing restaurant names: RestaurantNames.txt
    input_file=open("RestaurantNames.txt","r")
    out_file=open("yelp_data_final.txt","w")
    data=input_file.read()
    json_data=json.loads(data)
    yelp_api = YelpAPI('t3EnvPrJD5QFX9byrhYDronkMOjI17LzpSvePzEIRd-NS1FzIK_ayRigJn_iH8qLFI40RRmOXw56V38qcB-JBYdKImFYCg4F8eSmiAQEaOTLfkcNOAz3zxTuWQjBXHYx')
    restaurant_data_yelp=[]
    for each_data in json_data:
        each_data=json_data[each_data]
        res_data = each_data
        search_results = yelp_api.search_query(term = each_data["name"], location='Los Angeles, CA')
        #search_results=json.loads(input_file2.read())
        #json.dump(search_results,out_file)
        search_results['businesses'][1]
        for each_result in search_results['businesses']:
            score1=fuzz.partial_ratio(each_result['location']['display_address'],each_data["street_address"])
            score2=fuzz.partial_ratio(each_result['name'],each_data["name"])
            if score1>90 and score2>90:
                if 'id' in each_result:
                    res_data['yelp_id']=each_result['id']
                if 'rating' in each_result:
                    res_data['rating']=each_result['rating']
                if 'review_count' in each_result:
                    res_data['review_count']=each_result['review_count']
                if 'url' in each_result:
                    res_data['url']=each_result['url']
                if 'categories' in each_result:
                    res_data['category']=each_result['categories']
                if 'display_phone' in each_result:
                    res_data['phone_number']=each_result['display_phone']
                res_data['lat']=each_result['coordinates']['latitude']
                res_data['lon']=each_result['coordinates']['longitude']
                restaurant_data_yelp.append(res_data)
                print ("processed:",count)
                count=count+1
    json.dump(restaurant_data_yelp,out_file,sort_keys=True,indent=4,separators=(',', ': '))
getYelpData()
