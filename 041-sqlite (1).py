#!/usr/bin/env python
# coding: utf-8

# <font size="+3"><strong>4.1. Wrangling Data with SQL</strong></font>

# In[21]:


import sqlite3

import pandas as pd
from IPython.display import VimeoVideo


# In[2]:


VimeoVideo("665414044", h="ff34728e6a", width=600)


# # Prepare Data

# ## Connect

# In[3]:


VimeoVideo("665414180", h="573444d2f6", width=600)


# **Task 4.1.1:** Run the cell below to connect to the `nepal.sqlite` database. 
# 
# - [What's <span id='term'>ipython-sql</span>?](../%40textbook/10-databases-sql.ipynb#SQL-Databases)
# - [What's a <span id='term'>Magics function</span>?](../%40textbook/10-databases-sql.ipynb#Magic-Commands)

# In[22]:


get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', 'sqlite:////home/jovyan/nepal.sqlite')


# ## Explore

# In[4]:


VimeoVideo("665414201", h="4f30b7a95f", width=600)


# **Task 4.1.2:** Select all rows and columns from the `sqlite_schema` table, and examine the output. 
# 
# - [What's a <span id='term'>SQL database</span>?](../%40textbook/10-databases-sql.ipynb#SQL-Databases)
# - [What's a <span id='term'>SQL table</span>?](../%40textbook/10-databases-sql.ipynb#SQL-Databases)
# - [<span id='technique'>Write a basic query in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Building-Blocks-of-the-Basic-Query)
# 
# How many tables are in the `nepal.sqlite` database? What information do they hold? 

# In[23]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM sqlite_schema')


# In[5]:


VimeoVideo("665414239", h="d7319aa0a8", width=600)


# **Task 4.1.3:** Select the `name` column from the `sqlite_schema` table, showing only rows where the **`type`** is `"table"`.
# 
# - [<span id='technique'>Select a column from a table in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Building-Blocks-of-the-Basic-Query)
# - [<span id='technique'>Subset a table using a `WHERE` clause in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Building-Blocks-of-the-Basic-Query)

# In[26]:


get_ipython().run_cell_magic('sql', '', 'SELECT name\nFROM sqlite_schema\nWHERE type="table"')


# In[6]:


VimeoVideo("665414263", h="5b7d1e875f", width=600)


# **Task 4.1.4:** Select all columns from the `id_map` table, limiting your results to the first five rows. 
# 
# - [<span id='technique'>Inspect a table using a `LIMIT` clause in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Building-Blocks-of-the-Basic-Query)
# 
# How is the data organized? What type of observation does each row represent? How do you think the **`household_id`**, **`building_id`**, **`vdcmun_id`**, and **`district_id`** columns are related to each other?

# In[27]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM id_map\nLIMIT 5')


# In[7]:


VimeoVideo("665414293", h="72fbe6b7d8", width=600)


# **Task 4.1.5:** How many observations are in the `id_map` table? Use the `count` command to find out.
# 
# - [<span id='technique'>Calculate the number of rows in a table using a `count` function in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Aggregating-Data) 

# In[28]:


get_ipython().run_cell_magic('sql', '', 'SELECT count(*)\nFROM id_map')


# In[8]:


VimeoVideo("665414303", h="6ba10ddf88", width=600)


# **Task 4.1.6:** What districts are represented in the `id_map` table? Use the `distinct` command to determine the unique values in the **`district_id`** column.
# 
# - [<span id='technique'>Determine the unique values in a column using a `distinct` function in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Aggregating-Data) 

# In[29]:


get_ipython().run_cell_magic('sql', '', 'SELECT distinct(district_id)\nFROM id_map')


# In[9]:


VimeoVideo("665414313", h="adbab3e418", width=600)


# **Task 4.1.7:** How many buildings are there in `id_map` table? Combine the `count` and `distinct` commands to calculate the number of unique values in **`building_id`**.
# 
# - [<span id='technique'>Calculate the number of rows in a table using a `count` function in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Aggregating-Data) 
# - [<span id='technique'>Determine the unique values in a column using a `distinct` function in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Aggregating-Data) 

# In[30]:


get_ipython().run_cell_magic('sql', '', 'SELECT count(distinct(building_id))\nFROM id_map')


# In[10]:


VimeoVideo("665414336", h="5b595107c6", width=600)


# **Task 4.1.8:** For our model, we'll focus on Gorkha (district `4`). Select all columns that from `id_map`, showing only rows where the **`district_id`** is `4` and limiting your results to the first five rows.
# 
# - [<span id='technique'>Inspect a table using a `LIMIT` clause in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Building-Blocks-of-the-Basic-Query)
# - [<span id='technique'>Subset a table using a `WHERE` clause in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Building-Blocks-of-the-Basic-Query)

# In[31]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM id_map\nWHERE district_id=4\nLIMIT 5')


# In[11]:


VimeoVideo("665414344", h="bdcb4a50a3", width=600)


# **Task 4.1.9:** How many observations in the `id_map` table come from Gorkha? Use the `count` and `WHERE` commands together to calculate the answer.
# 
# - [<span id='technique'>Calculate the number of rows in a table using a `count` function in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Aggregating-Data) 
# - [<span id='technique'>Subset a table using a `WHERE` clause in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Building-Blocks-of-the-Basic-Query)

# In[33]:


get_ipython().run_cell_magic('sql', '', 'SELECT count(*)\nFROM id_map\nWHERE district_id=4')


# In[12]:


VimeoVideo("665414356", h="5d2bdb3813", width=600)


# **Task 4.1.10:** How many buildings in the `id_map` table are in Gorkha? Combine the `count` and `distinct` commands to calculate the number of unique values in **`building_id`**, considering only rows where the **`district_id`** is `4`.
# 
# - [<span id='technique'>Calculate the number of rows in a table using a `count` function in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Aggregating-Data) 
# - [<span id='technique'>Determine the unique values in a column using a `distinct` function in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Aggregating-Data) 
# - [<span id='technique'>Subset a table using a `WHERE` clause in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Building-Blocks-of-the-Basic-Query)

# In[35]:


get_ipython().run_cell_magic('sql', '', 'SELECT count(distinct(building_id)) AS unique_buildings_gorkha\nFROM id_map\nWHERE district_id=4')


# In[13]:


VimeoVideo("665414390", h="308ea86e4b", width=600)


# **Task 4.1.11:** Select all the columns from the `building_structure` table, and limit your results to the first five rows. 
# 
# - [<span id='technique'>Inspect a table using a `LIMIT` clause in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Querying-a-Database)
# 
# What information is in this table? What does each row represent? How does it relate to the information in the `id_map` table?

# In[37]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM building_structure\nLIMIT 5')


# In[14]:


VimeoVideo("665414402", h="64875c7779", width=600)


# **Task 4.1.12:** How many building are there in the `building_structure` table? Use the `count` command to find out.
# 
# - [<span id='technique'>Calculate the number of rows in a table using a `count` function in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Aggregating-Data) 

# In[38]:


get_ipython().run_cell_magic('sql', '', 'SELECT count(*)\nFROM building_structure')


# In[15]:


VimeoVideo("665414414", h="202f83f3cb", width=600)


# **Task 4.1.13:** There are over 200,000 buildings in the `building_structure` table, but how can we retrieve only buildings that are in Gorkha? Use the `JOIN` command to join the `id_map` and `building_structure` tables, showing only buildings where **`district_id`** is `4` and limiting your results to the first five rows of the new table.
# 
# - [<span id='technique'>Create an alias for a column or table using the `AS` command in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#SELECT-and-FROM) 
# - [<span id='technique'>Merge two tables using a `JOIN` clause in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Joining-Tables)
# - [<span id='technique'>Inspect a table using a `LIMIT` clause in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Building-Blocks-of-the-Basic-Query)
# - [<span id='technique'>Subset a table using a `WHERE` clause in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Building-Blocks-of-the-Basic-Query)

# In[44]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM id_map AS i\nJOIN building_structure AS s ON i.building_id = s.building_id\nWHERE district_id=4\nLIMIT 5')


# In the table we just made, each row represents a unique household in Gorkha. How can we create a table where each row represents a unique building?

# In[16]:


VimeoVideo("665414450", h="0fcb4dc3fa", width=600)


# **Task 4.1.14:** Use the `distinct` command to create a column with all unique building IDs in the `id_map` table. `JOIN` this column with all the columns from the `building_structure` table, showing only buildings where **`district_id`** is `4` and limiting your results to the first five rows of the new table.
# 
# - [<span id='technique'>Create an alias for a column or table using the `AS` command in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#SELECT-and-FROM) 
# - [<span id='technique'>Determine the unique values in a column using a `distinct` function in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Aggregating-Data) 
# - [<span id='technique'>Merge two tables using a `JOIN` clause in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Joining-Tables)
# - [<span id='technique'>Inspect a table using a `LIMIT` clause in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Building-Blocks-of-the-Basic-Query)
# - [<span id='technique'>Subset a table using a `WHERE` clause in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Building-Blocks-of-the-Basic-Query)

# In[47]:


get_ipython().run_cell_magic('sql', '', 'SELECT distinct(i.building_id),\n        s.*\nFROM id_map AS i\nJOIN building_structure AS s ON i.building_id = s.building_id\nWHERE district_id=4\nLIMIT 5')


# We've combined the `id_map` and `building_structure` tables to create a table with all the buildings in Gorkha, but the final piece of data needed for our model, the damage that each building sustained in the earthquake, is in the `building_damage` table.

# In[17]:


VimeoVideo("665414466", h="37dde03c93", width=600)


# **Task 4.1.15:** How can combine all three tables? Using the query you created in the last task as a foundation, include the **`damage_grade`** column to your table by adding a second `JOIN` for the `building_damage` table. Be sure to limit your results to the first five rows of the new table.
# 
# - [<span id='technique'>Create an alias for a column or table using the `AS` command in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#SELECT-and-FROM) 
# - [<span id='technique'>Determine the unique values in a column using a `distinct` function in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Aggregating-Data) 
# - [<span id='technique'>Merge two tables using a `JOIN` clause in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Joining-Tables)
# - [<span id='technique'>Inspect a table using a `LIMIT` clause in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Building-Blocks-of-the-Basic-Query)
# - [<span id='technique'>Subset a table using a `WHERE` clause in <span id='tool'>SQL</span></span>.](../%40textbook/10-databases-sql.ipynb#Building-Blocks-of-the-Basic-Query)

# In[49]:


get_ipython().run_cell_magic('sql', '', 'SELECT distinct(i.building_id) AS b_id,\n        s.*,\n        d.damage_grade\nFROM id_map AS i\nJOIN building_structure AS s ON i.building_id = s.building_id\nJOIN building_damage AS d ON i.building_id = d.building_id\nWHERE district_id=4\nLIMIT 5')


# ## Import

# In[18]:


VimeoVideo("665414492", h="9392e1a66e", width=600)


# **Task 4.1.16:** Use the [`connect`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect) method from the sqlite3 library to connect to the database. Remember that the database is located at `"/home/jovyan/nepal.sqlite"`.
# 
# - [<span id='technique'>Open a connection to a SQL database using <span id='tool'>sqlite3</span></span>.](../%40textbook/10-databases-sql.ipynb#Using-pandas-with-SQL-Databases)

# In[50]:


conn = sqlite3.connect("/home/jovyan/nepal.sqlite")


# In[19]:


VimeoVideo("665414501", h="812d482c73", width=600)


# **Task 4.1.17:** Put your last SQL query into a string and assign it to the variable `query`.

# In[51]:



query = """
SELECT distinct(i.building_id) AS b_id,
        s.*,
        d.damage_grade
FROM id_map AS i
JOIN building_structure AS s ON i.building_id = s.building_id
JOIN building_damage AS d ON i.building_id = d.building_id
WHERE district_id=4
"""
print(query)


# In[20]:


VimeoVideo("665414513", h="c6a81b49ad", width=600)


# **Task 4.1.18:** Use the [`read_sql`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html#pandas-read-sql) from the pandas library to create a DataFrame from your `query`. Be sure that the **`building_id`** is set as your index column.
# 
# - [<span id='technique'>Read SQL query into a DataFrame using <span id='tool'>pandas</span></span>.](../%40textbook/10-databases-sql.ipynb#Using-pandas-with-SQL-Databases)
# 
# <div class="alert alert-block alert-info">
# <b>Tip:</b> Your table might have two <b><code>building_id</code></b> columns, and that will make it hard to set it as the index column for your DataFrame. If you face this problem, add an alias for one of the <b><code>building_id</code></b> columns in your query using <code>AS</code>.
# </div>

# In[52]:


df = pd.read_sql(query, conn, index_col="b_id")

df.head()


# In[53]:


# Check your work
assert df.shape[0] == 70836, f"`df` should have 70,836 rows, not {df.shape[0]}."
assert (
    df.shape[1] > 14
), "`df` seems to be missing columns. Does your query combine the `id_map`, `building_structure`, and `building_damage` tables?"
assert (
    "damage_grade" in df.columns
), "`df` is missing the target column, `'damage_grade'`."


# ---
# Copyright © 2022 WorldQuant University. This
# content is licensed solely for personal use. Redistribution or
# publication of this material is strictly prohibited.
# 
