
gulahmedproducts = [
    {
     'SkuCode': 110,
     'Name': "3PC Yarn Dyed Unstitched digital Printed Suit CLP-32046",
     'isAvailable': "true",
     'category': "unstiched",
     'price': 4043,
     'color': ["black", "red", "white"],
     'totalStock': 2,
     'isonSale': "false",
     'reviews': [
         {
             'udId': 1,
             'uName': "abc",
             'ratings': 4.5,
             'comments': "nice product",
             'isApproved': "false"

         },

         {
             'udId': 2,
             'uName': "abc",
             'ratings': 2.0,
             'comments': "faulty product",
             'isApproved': "false"
         },

         {
             'udId': 3,
             'uName': "abc",
             'ratings': 2.0,
             'comments': "great product",
             'isApproved': "false"
         }
     ]
     },

    {
        'SkuCode': 111,
        'Name': "3PC Yarn Dyed Unstitched digital Printed Suit CLP-32046",
        'isAvailable': "true",
        'category': "stiched",
        'price': 4043,
        'color': ["black", "red", "white"],
        'totalStock': 2,
        'isonSale': "true",
    },

    {
        'SkuCode': 112,
        'Name': "3PC Yarn Dyed Unstitched digital Printed Suit CLP-32046",
        'isAvailable': 'true',
        'category': "two-pice",
        'price': 4043,
        'color': ["black", "red", "white"],
        'totalStock': 2,
        'isonSale': "true"
    },

    {
        'SkuCode': 113,
        'Name': "3PC Yarn Dyed Unstitched digital Printed Suit CLP-32046",
        'isAvailable': "true",
        'category': "unstiched",
        'price': 4043,
        'color': ["black", "red", "white"],
        'totalStock': 2,
        'isonSale': "false",
     }
]

for i in gulahmedproducts:
    if i['category'] == 'unstiched':
        i['isonSale'] = "true"
        #print(i['isonSale'])
        print(str(i['SkuCode']) + " : it's on sale now")


for i in gulahmedproducts:
    if 'reviews' in i:
        for x in i['reviews']:
            if x['comments'] == 'nice product' or x['comments'] == 'great product':
                x['isApproved'] = 'True'
                print(str(i['SkuCode']) + " : " + str(x['udId']) + " : comment is approved")
            #print(x)