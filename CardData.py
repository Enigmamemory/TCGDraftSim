import requests
import json

def Get_Card_Info(card_id):
    response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php?id={}".format(card_id))
    card_info = response.json()
    del response

    if 'error' in card_info:
        raise Exception("\t" + card_id + ": " + card_info["error"])

    # There's only one item in this list
    return card_info['data'][0]

def Parse_Type(type):
    #type = card_data['type']
    ptype = type.split(' ')
    return ptype

def Is_Pend(ptype):
    return ('Pendulum' in ptype)

def Is_Link(ptype):
    return ('Link' in ptype)

def Is_Mon(ptype):
    return ('Monster' in ptype)

#test = Get_Card_Info(5043010)
#print(test['linkmarkers'])

'''
ptest = Parse_Type(test)
print(ptest)
print(Is_Pend(ptest))
print(Is_Link(ptest))
print(Is_Mon(ptest))
'''
