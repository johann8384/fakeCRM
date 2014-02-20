fakeCRM
=======

## About: 

Creates Contact, Device, Ticket and Customer information for testing ticketing, helpdesk, support, crm type applicaitons. 

Creates Customers as the head item, contacts have a clientID they are associated with, then creates devices and tickets associated with those customers and contacts. 

The number of contacts per customer varies, the number of devices per customer varies, and the number of tickets as well as whether or not there will be a ticket varies. 

Within a ticket the status is open or acknowledged with no response or one of the later statuses with a response.

## Usage:

git clone https://github.com/johann8384/fakeCRM
cd fakeCRM
python ./fakeUsers.py | more

## Example Data:

### Ticket:
```
    {
        "status": {
            "status": "Waiting on Customer",
            "id": 3
        },
        "body": "Thank you for being so reliable. Please incentivize transparent content on my server disk-array controller subsystem because I can't use the user-centric client-server pricingstructure while the user is moving",
        "cc": [
            {
                "username": "aerdman",
                "contactID": 10012,
                "name": "Annie Erdman",
                "email": "aerdman@cummings.com"
            },
            {
                "username": "hstreich",
                "contactID": 10011,
                "name": "Hailey Streich",
                "email": "hstreich@cummings.com"
            }
        ],
        "clientID": 1002,
        "device": {
            "domain": "cummings.com",
            "ipAddr": "10.50.28.149",
            "deviceID": 10010,
            "name": "cmmngs-remote 1"
        },
        "ticketID": 10001,
        "subject": "incentivize transparent content",
        "author": {
            "username": "ho'keefe",
            "contactID": 10010,
            "name": "Humberto O'Keefe",
            "email": "ho'keefe@cummings.com"
        },
        "posts": [
            {
                "body": "I believe the problem is power surges on the underground.. Please stop trying the monitored executive processimprovement on my monitor",
                "adminID": 4,
                "name": "Will Rogahn",
                "subject": "grow end-to-end synergies"
            }
        ],
        "priority": 3,
        "client": "Cummings Group"
    }
```
### Device:
```
    {
        "domain": "cummings.com",
        "deviceID": 10010,
        "typeGroupID": "5",
        "shortname": "cmmngs",
        "ipAddr": "10.50.28.149",
        "typeGroupName": "VPN Appliance",
        "clientID": 1002,
        "name": "cmmngs-remote 1"
    }
```
### Customer:
```
    {
        "domain": "cummings.com",
        "address1": "7981 Kassulke Lodge Apt. 096",
        "address2": "Suite 733",
        "clientID": 1002,
        "phone": "05188658797",
        "keywords": "integrate real-time eyeballs",
        "city": "West Gustave",
        "zip": "14690",
        "state": "Nevada",
        "shortname": "cmmngs",
        "catch_phrase": "Diverse discrete synergy",
        "company": "Cummings Group"
    }
```
Contact:
```
    {
        "username": "ho'keefe",
        "name": "Humberto O'Keefe",
        "clientID": 1002,
        "phone": "425.337.4280",
        "contactID": 10010,
        "password": "vmkLYnY9",
        "email": "ho'keefe@cummings.com"
    }
```    
