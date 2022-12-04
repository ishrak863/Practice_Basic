import pandas as pd
a= input()
a= a.lower()
result = [x.strip() for x in a.split(',')]
s = pd.Series(result)
d= s.value_counts()
print (d)
d.to_excel(r'H:\Python Programs\test_data.xlsx')
