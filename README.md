# mobileiron-api
A python API for Mobile Iron Cloud

## Install



    pip install moblieiron-api # supported python version > 3.9


## Usage


    
    from mobileiron_api.client import *    

    client = MobileIronCloudAPI(username="<YOUR_USERNAME>", password="<YOUR_PASSWORD>",
                                fqdn="<YOUR_FQDN>", dmPartitionId=<YOUR_MI_SPACE_ID>)
    resp = client.user_management_api.get_user_profiles_bulk(rows=1)

    print(resp)


