Inspired by 6C2W1azD1rBs1oWLtRT41A76WY2WYGvT4r58uNcdmu5cYHHfvJ2RCJs

# Local mode

create secret.py in this folder, then add these lines.

```
from os import environ

environ['MY_SECRET_USERNAME'] = '<hdu username>'
environ['MY_SECRET_PASSWORD'] = '<hdu password>'
```
# Github Action mode

add repository secrets in "Settings"->"Secrets" according to the key-value pairs above.  
Example:  
create a new secret named "MY_SECRET_USERNAME", then set the "Value" to the username (don't type the single quotation marks).