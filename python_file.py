def Dict(sample_dict):
  result=''
  for i in range(len(sample_dict['name'])):
    name=sample_dict['name'][i]
    numbers=sample_dict['lucky_numbers'][i]
    for number in numbers:
      result+=name+' '+str(number)+','
  res1=result[:-1]
  print(res1)
Dict({'name':['Ganesh','Manas','Prachi'],'lucky_numbers':[[1,2,3],[2,7],[2,8,9,11]]})
