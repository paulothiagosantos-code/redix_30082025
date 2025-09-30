import redis
r = redis.Redis(host='10.1.68.172', port=6379, db=0)
r.ping()
# True

# ### Inserindo Dados ###

r.set('paulo_mykey', '55555')

# True

# ### Obtendo Dados ###

name = r.get('paulo_mykey')
print(name.decode())
# myvalue

# ### Removendo Dados ###

r.delete('paulo_mykey')
# 1
name = r.get('paulo_mykey')
print(name.decode())
# Traceback (most recent call last):
# File "", line 1, in print(name.decode())
# ^^^^^^^^^^^
# AttributeError: 'NoneType' object has no attribute 'decode'
