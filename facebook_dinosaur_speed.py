file1='./facebook_dinosaur_speed_file1.txt'
file2='./facebook_dinosaur_speed_file2.txt'

def sort_animal(file1,file2):
  d_leg, d_weight, d_stride,  d_speed = {}, {}, {}, {}
  with open(file1, 'r') as f1:
    for line in f1:
      if 'animal' in line:
        list1 = line.split(',')
        name = list1[0].strip()
        d_leg[name] = list1[1]
        d_weight[name] = list1[2]
  with open(file2, 'r') as f2:
    for line in f2:
      if 'animal' in line:
        list2 = line.split(',')
        name = list2[3].strip()
        if name in d_leg.keys():
          d_stride[name] = list2[2]
  for k in d_leg.keys():
    d_speed[k] = int(d_leg[k]) * int(d_stride[k]) / int(d_weight[k])
  name_speed = sorted(d_speed.items(), key = lambda x:x[1], reverse=True)
  res = [x[0] for x in name_speed ]
  return res

print sort_animal(file1,file2)


