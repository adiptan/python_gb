import os
dirs_list = {'my_project_task_7_1': ['settings', 'mainapp', 'adminapp', 'authapp']}

root = os.path.abspath('.')
for dir, subdirs in dirs_list.items():
    root_dir = os.path.join(root, dir)
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
        print(f'Directory created: {root_dir}')
    for el in subdirs:
        root_dir = os.path.join(root, dir, el)
        if not os.path.exists(root_dir):
            os.mkdir(root_dir)
            print(f'Directory created: {root_dir}')
