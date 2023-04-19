# Mobileiron-Api
![MobileIron](https://user-images.githubusercontent.com/27059441/233013869-aa00a61e-92f1-4c86-9a91-396c9b7f0104.jpg)

A python API for Mobile Iron Cloud

## Install



    pip install moblieiron-api # supported python version >= 3.8


## Usage


    
    from mobileiron_api.client import *    

    client = MobileIronCloudAPI(username="<YOUR_USERNAME>", password="<YOUR_PASSWORD>",
                                fqdn="<YOUR_FQDN>", dmPartitionId=<YOUR_MI_SPACE_ID>)
    resp = client.user_management_api.get_user_profiles_bulk(rows=1)

    print(resp)


