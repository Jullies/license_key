#!/usr/bin/env python3.5.2
# -*- coding: utf-8 -*-
"""
Project started on Mon September 24 10:09:41 2018
@author: Jullies Onyango
@whatItDoes: Generate license key based on users name
"""

import datetime
import hashlib as julliesencrypt

varch = "Jullies Onyango"
newvarchar = varch[::-1]
sfirstcharacter = newvarchar[::-2]
fencrypt=sfirstcharacter[::-1]
salt = "d7m27y1995"
cryp_x = 0
crypt_value = ""
for row in fencrypt:
    crypt_value = crypt_value + row + salt[cryp_x]
    cryp_x = cryp_x + 1
cyp = datetime.datetime.today()
cypt_date = cyp.strftime('%m%Y')
fin_crpt_value=""
cryp_y = 0
for row in crypt_value:
    try:
        pck_date = cypt_date[cryp_y]
    except:
        pck_date=""
    fin_crpt_value = fin_crpt_value + row + pck_date
    cryp_y = cryp_y + 1

nwcrypt_value = fin_crpt_value.encode('ascii')
coll_cyp_v = julliesencrypt.sha256()
coll_cyp_v.update(nwcrypt_value)
show_coll_cyp_v = coll_cyp_v.hexdigest()
cyp_user = show_coll_cyp_v[:16]
cyp_for_user = cyp_user[::-1]
cyp_auoth = ""
st_a = 1
dnt_length = len(cyp_for_user)
for row in cyp_for_user:
    if dnt_length > st_a:
        if st_a%4 ==0:
            cyp_auoth = cyp_auoth + row + "-"
        else:
            cyp_auoth = cyp_auoth + row         
    else:
        cyp_auoth = cyp_auoth + row  
    st_a = st_a + 1
permit_code = cyp_auoth.upper()
print(permit_code)