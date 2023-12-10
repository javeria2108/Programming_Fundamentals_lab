import hashlib
import json
def hash(block):
            string_object = json.dumps(block, sort_keys=True)
            print (string_object)
            block_string = string_object.encode()
            print (block_string)    
            raw_hash = hashlib.sha256(block_string)
            print (raw_hash)
            hex_hash = raw_hash.hexdigest()
            return hex_hash
block={
                'index': 1,
                'timestamp': 1233243.3534543,
                'transactions': [],
                'proof': 76473246,
                'previous_hash': "1233434"
            }            
new_hash=(hash( block))
print (new_hash)            