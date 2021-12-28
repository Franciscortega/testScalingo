import os
import pkg_resources

def calc_container(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size



dists = [d for d in pkg_resources.working_set]

all_total = 0
element_list = []
for dist in dists:
    try:
        path = os.path.join(dist.location, dist.project_name)
        size = calc_container(path)
        all_total += size
        if size/1000 > 1.0:
            element_list.append([size, dist])
    except OSError:
        '{} no longer exists'.format(dist.project_name)

element_list.sort(key=lambda x:x[0],reverse=True)
for element in element_list:
    print (f"{element[1]}: {element[0]/1000} KB")
    print("-" * 40)

print (f"TOTAL{dist}: {all_total/1000} KB")