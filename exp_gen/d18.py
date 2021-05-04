#!/usr/bin/env python
# coding: utf-8

# ## D18 - 1

# In[1]:


NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


# In[14]:


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    return list({name.title() for name in names})


# In[15]:


dedup_and_title_case_names(NAMES)


# In[8]:


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return [name for name in sorted(names, key=lambda n:n.split()[1], reverse=True)]


# In[9]:


sort_by_surname_desc(NAMES)


# In[20]:


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    return sorted([name.split()[0] for name in names], key=len)[0]


# In[21]:


shortest_first_name(NAMES)


# # D18 - 2

# In[22]:


bites = {6: 'PyBites Die Hard',
         7: 'Parsing dates from logs',
         9: 'Palindromes',
         10: 'Practice exceptions',
         11: 'Enrich a class with dunder methods',
         12: 'Write a user validation function',
         13: 'Convert dict in namedtuple/json',
         14: 'Generate a table of n sequences',
         15: 'Enumerate 2 sequences',
         16: 'Special PyBites date generator',
         17: 'Form teams from a group of friends',
         18: 'Find the most common word',
         19: 'Write a simple property',
         20: 'Write a context manager',
         21: 'Query a nested data structure'}
exclude_bites = {6, 10, 16, 18, 21}


# In[33]:


def filter_bites(bites=bites, bites_done=exclude_bites):
    """return the bites dict with the exclude_bites filtered out"""
    return { x:y for x,y in bites.items() if x not in bites_done}


# In[34]:


filter_bites()

