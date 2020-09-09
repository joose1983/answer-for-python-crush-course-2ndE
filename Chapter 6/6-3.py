glossary={'list':'a group of data with numerical indexes','boolean':'true or false'}
print('list:',glossary['list'])
print('boolean:',glossary.get('boolean','no items found in this dictionary'))
print('int:', glossary.get('int','no items found in this dictionary'))
