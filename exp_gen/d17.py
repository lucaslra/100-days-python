#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random


# In[4]:


NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


# #### Can you write a simple list comprehension to convert these names to title case (brad pitt -> Brad Pitt).

# In[5]:


[name.title() for name in NAMES]


# #### Or reverse the first and last name?

# In[6]:


[' '.join(reversed(name.split())) for name in NAMES]


# #### Then use this same list and make a little generator, for example to randomly return a pair of names, try to make this work:
# 
# ```python
# pairs = gen_pairs()
# for _ in range(10):
#     next(pairs)
# ```

# In[20]:


gen_NAMES = NAMES[:]
random.shuffle(gen_NAMES)

def get_name(idx):
    return gen_NAMES[idx].split()[0].title()

def gen_pairs():
    idx = 1
    while idx <= len(gen_NAMES) - 1:
        r = f'{get_name(idx-1)} teams up with {get_name(idx)}'
        idx+=2
        yield r


# #### Should print (values might change as random):
# 
# ```python
# Arnold teams up with Brad
# Alec teams up with Julian
# ```

# In[21]:


pairs = gen_pairs()
for p in pairs:
    print(p)

