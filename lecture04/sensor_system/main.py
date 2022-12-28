import html_creater as hc
import xml_generat as xg
import data_provider as dp

# hc.new_create(dp.data_collection())
hc.new_create(xg.new_create(dp.data_collection()))



# print(hc.create())
# print(xg.create())
