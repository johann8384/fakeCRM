import json
import string
import random
from faker import Factory
from random import randrange

from random import choice

f = Factory.create()

billing_roles = ['N/A', 'Add Services']

contactid = 10000
clientid = 1000
ticketid = 10000
deviceid = 10000

# https://github.com/joke2k/faker/blob/master/faker/providers/en_US/company.py
bsWords = [
        [
            'implement', 'utilize', 'integrate', 'streamline', 'optimize', 'evolve', 'transform', 'embrace', 'enable',
            'orchestrate', 'leverage', 'reinvent', 'aggregate', 'architect', 'enhance', 'incentivize', 'morph',
            'empower', 'envisioneer', 'monetize', 'harness', 'facilitate', 'seize', 'disintermediate', 'synergize',
            'strategize', 'deploy', 'brand', 'grow', 'target', 'syndicate', 'synthesize', 'deliver', 'mesh', 'incubate',
            'engage', 'maximize', 'benchmark', 'expedite', 'reintermediate', 'whiteboard', 'visualize', 'repurpose',
            'innovate', 'scale', 'unleash', 'drive', 'extend', 'engineer', 'revolutionize', 'generate', 'exploit',
            'transition', 'e-enable', 'iterate', 'cultivate', 'matrix', 'productize', 'redefine', 'recontextualize'
        ],
        [
            'clicks-and-mortar', 'value-added', 'vertical', 'proactive', 'robust', 'revolutionary', 'scalable',
            'leading-edge', 'innovative', 'intuitive', 'strategic', 'e-business', 'mission-critical', 'sticky',
            'one-to-one', '24/7', 'end-to-end', 'global', 'B2B', 'B2C', 'granular', 'frictionless', 'virtual', 'viral',
            'dynamic', '24/365', 'best-of-breed', 'killer', 'magnetic', 'bleeding-edge', 'web-enabled', 'interactive',
            'dot-com', 'sexy', 'back-end', 'real-time', 'efficient', 'front-end', 'distributed', 'seamless',
            'extensible', 'turn-key', 'world-class', 'open-source', 'cross-platform', 'cross-media', 'synergistic',
            'bricks-and-clicks', 'out-of-the-box', 'enterprise', 'integrated', 'impactful', 'wireless', 'transparent',
            'next-generation', 'cutting-edge', 'user-centric', 'visionary', 'customized', 'ubiquitous', 'plug-and-play',
            'collaborative', 'compelling', 'holistic', 'rich'
        ],
        [
            'synergies', 'web-readiness', 'paradigms', 'markets', 'partnerships', 'infrastructures', 'platforms',
            'initiatives', 'channels', 'eyeballs', 'communities', 'ROI', 'solutions', 'e-tailers', 'e-services',
            'action-items', 'portals', 'niches', 'technologies', 'content', 'vortals', 'supply-chains', 'convergence',
            'relationships', 'architectures', 'interfaces', 'e-markets', 'e-commerce', 'systems', 'bandwidth',
            'infomediaries', 'models', 'mindshare', 'deliverables', 'users', 'schemas', 'networks', 'applications',
            'metrics', 'e-business', 'functionalities', 'experiences', 'webservices', 'methodologies'
        ]
    ]


itemList = [
 'server',
 'network',
 'user',
 'chicken',
 'provider',
 'outsourced internet',
 'portal',
 'system',
 'bandwidth'
]
stateList = [
    'borked',
    'transferred',
    'initializing',
    'occupying time-space continuity blankets',
    'down'
]

serverSpecs = {"devtype_group_id":"1",
     "name":"Servers",
     "priority":"1",
     "names": ['implement', 'utilize', 'integrate', 'streamline', 'optimize', 'evolve', 'transform', 'embrace', 'enable',
                'orchestrate', 'leverage', 'reinvent', 'aggregate', 'architect', 'enhance', 'incentivize', 'morph',
                'empower', 'envisioneer', 'monetize', 'harness', 'facilitate', 'seize', 'disintermediate', 'synergize',
                'strategize', 'deploy', 'brand', 'grow', 'target', 'syndicate', 'synthesize', 'deliver', 'mesh', 'incubate',
                'engage', 'maximize', 'benchmark', 'expedite', 'reintermediate', 'whiteboard', 'visualize', 'repurpose',
                'innovate', 'scale', 'unleash', 'drive', 'extend', 'engineer', 'revolutionize', 'generate', 'exploit',
                'transition', 'iterate', 'cultivate', 'matrix', 'productize', 'redefine', 'recontextualize']}
lbSpecs =  {"devtype_group_id":"3",
     "name":"Load Balancers",
     "priority":"3",
     "names": ['lb', 'balancer']}

switchSpecs = {"devtype_group_id":"4",
     "name":"Switches",
     "priority":"4",
     "names": ['sw']}

vpnSpecs = {"devtype_group_id":"5",
     "name":"VPN Appliance",
     "priority":"5",
     "names": ['vpn','remote', 'access']}

storageSpecs = {"devtype_group_id":"6",
     "name":"Storage Appliance",
     "priority":"6",
     "names": ['storage', 'san', 'nas']}

routerSpecs = {"devtype_group_id":"9",
     "name":"Router",
     "priority":"9",
     "names": ['router', 'rtr', 'gw', 'uplink']}

deviceTypeAGroups = [serverSpecs]
deviceTypeBGroups = [switchSpecs, vpnSpecs, storageSpecs, routerSpecs]

def randompassword():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = random.randint(8, 12)
  return ''.join(random.choice(chars) for x in range(size))

def ipv4():
  """
  Convert 32-bit integer to dotted IPv4 address.
  """
  return ".".join(map(lambda n: str(random.randint(171048960, 171065342) >> n & 0xFF), [24, 16, 8, 0]))

contacts = []
clients = []
devices = []
tickets = []

for i in range(560):
  company = f.company();
  domain = company.split(' ')[0].strip(',').lower() + '.' + f.domain_name().split('.')[1]
  shortname = company.split(' ')[0].strip(',').lower()
  companyContacts = []

  for eachLetter in shortname:
        if eachLetter in ['a','e','i','o','u', '-']:
                shortname = shortname.replace(eachLetter, '')

  clientid = clientid+1

  for t in range(randrange(1,9)):
    password = randompassword();
    first = f.first_name();
    last = f.last_name();
    username = first[0].lower() + last.lower();
    contactid = contactid+1;
    contact = {'contactID': contactid, 'clientID': clientid, 'name': first + ' ' + last, 'username': username, 'email': username + '@' + domain, 'phone': f.phone_number(), 'password': password }
    contacts.append(contact)
    companyContacts.append({'contactID': contactid, 'name': first + ' ' + last, 'username': username, 'email': username + '@' + domain})

  for t in range(randrange(1,4)):
    typeGroup = random.choice(deviceTypeBGroups);
    name = random.choice(typeGroup['names']);
    deviceid = deviceid + 1;
    device = {'deviceID': deviceid, 'clientID': clientid, 'shortname': shortname, 'domain': domain, 'typeGroupID': typeGroup['devtype_group_id'],  'typeGroupName': typeGroup['name'], 'ipAddr': ipv4(), 'name': shortname + '-' + name + "{0:03d}".format(t+1)}
    devices.append(device)

  for t in range(randrange(3,12)):
    typeGroup = random.choice(deviceTypeAGroups);
    name = random.choice(typeGroup['names']);
    deviceid = deviceid + 1;
    device = {'deviceID': deviceid, 'clientID': clientid, 'shortname': shortname, 'domain': domain, 'typeGroupID': typeGroup['devtype_group_id'],  'typeGroupName': typeGroup['name'], 'ipAddr': ipv4(), 'name': shortname + '-' + name + "{0:03d}".format(t+1)}
    devices.append(device)

  if random.choice([True, False]) == True:
    for t in range(randrange(0,2)):
      ticketid = ticketid + 1;
      ticketText = "Please " + f.bs() + " on my " + f.catch_phrase() + " because I can't " + f.catch_phrase() + " while the " + random.choice(itemList) + " is " + random.choice(stateList);
      ticketContact = random.choice(companyContacts);
      ticket = {'ticketID': ticketid, 'contact': ticketContact, 'clientID': clientid, 'client': company, 'subject': f.bs(), 'body': ticketText, 'priority': random.choice([0,1,2,3])};
      tickets.append(ticket);

  client = {'clientID': clientid, 'company': company, 'shortname': shortname, 'catch_phrase': f.catch_phrase(), 'keywords': f.bs(), 'domain': domain, 'phone': f.phone_number(), 'address1': f.street_address(), 'address2': f.secondary_address(), 'city': f.city(), 'state': f.state(), 'zip': f.postcode(), 'phone': f.phone_number()}
  clients.append(client)

print 'var tickets = ' + json.dumps(tickets, sort_keys=False, indent=4, separators=(',', ': '))
print 'var devices = ' + json.dumps(devices, sort_keys=False, indent=4, separators=(',', ': '))
print 'var clients = ' + json.dumps(clients, sort_keys=False, indent=4, separators=(',', ': '))
print 'var contacts = ' + json.dumps(contacts, sort_keys=False, indent=4, separators=(',', ': '))
