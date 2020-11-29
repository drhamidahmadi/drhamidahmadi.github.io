import glob, os

for name in glob.glob('C:/Users/Test/Downloads/mihanblog/post/*.htm'):
  path = name[:-4]
  os.mkdir(path)
  try:
    os.rename(name, path + '/index.htm')
  except FileExistsError:
    print('exists')

#manual = [26, 74, 114, 115, 124, 127, 130, 137, 168, 177, 180, 183, 208, 211, 259, 291, 299, 304, 306, 307, 309, 318, 336, 345, 375, 391, 392, 397, 400, 452, 457, 463, 474, 493, 500, 505, 526, 531, 533, 537, 569, 598, 616, 644, 656, 657, 670, 688, 706, 715, 768, 795, 797, 804, 806, 814, 817, 818, 820, 821, 822, 830, 835, 846, 866, 869, 880, 887, 890, 894, 896, 897, 898, 903, 904, 906, 913, 919, 925, 942, 947, 955, 957, 958, 960, 963, 964, 966, 968, 974, 976, 978, 981, 984, 989, 993, 994, 1011, 1029, 1030, 1038, 1047, 1064]

#for i in manual:
#  os.rename("C:/Users/Test/Downloads/dr_ahmadi_manually/post/" + str(i) + ".htm", "C:/Users/Test/Downloads/dr_ahmadi.mihanblog.com/post/" + str(i) + ".manual.htm")

#for i in range(25, 47):
#  os.rename("C:/Users/Test/Downloads/dr_ahmadi.mihanblog.com/page/" + str(i) + ".htm", "C:/Users/Test/Downloads/dr_ahmadi.mihanblog.com/page/" + str(i) + ".manual.htm")