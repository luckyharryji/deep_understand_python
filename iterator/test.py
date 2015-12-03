from iterator import Fab, fab_yield, read_file

print Fab(5)
# for i in Fab(5):
#     pass
    # print i

for i in fab_yield(5):
    print i

inst = fab_yield(5)
inst.next()
inst.next()

file_test = read_file('frontface_list.csv')
for i in file_test:
    print i
# print file_test
# print file_test.next()
# print file_test.next()
