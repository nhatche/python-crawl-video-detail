

for i in range(20):
  print(f'process{i} = Process(target=f, args=(queue,))')
  
for i in range(20):
  print(f'process{i}.start()')