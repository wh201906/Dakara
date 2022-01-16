# Local mode

create secret.py in this folder, then add these lines.

```
from os import environ

environ['MY_SECRET_USERNAME'] = '<y_i-b a-n username>'
environ['MY_SECRET_PASSWORD'] = '<y_i-b a-n password>'
environ['MY_SECRET_TOKEN'] = '<token from w=e_c h-a_t>'
environ['MY_SECRET_LOCATION'] = '{"province" : "<province name>", "city" : "<city name>", "district" : "<district name>", "lng" : <longitude>, "lat" : <latitude>}'
```
school location:

```
{"province" : 7, "city" : 9, "district" : 4, "lng" : 120.3432, "lat" : 30.3151}
```
("province", "city" and "district" are useless now)
# Github Action mode

add repository secrets in "Settings"->"Secrets" according to the key-value pairs above.  
Example:  
create a new secret named "MY_SECRET_USERNAME", then set the "Value" to the username (don't type the single quotation marks).