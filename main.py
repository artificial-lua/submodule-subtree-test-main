# module_list = []

# if __name__ == '__main__':
#     print('main - run')
    
#     try:
#         submodule = __import__('modules.submodule', fromlist=['submodule'])
#         module = submodule.version_check()
#         module_name = module['name']
#         module_version = module['version']
#         print(f'submodule - {module_name}:{module_version}')
#         module_list.append(module)
#     except Exception as e:
#         print(f'main:error - {e}')
import os

MODULES = []


def import_modules(path:str):
    modules = []
    for package in os.listdir(path):
        try:
            module = __import__(path + '.' + package, fromlist=[package])
            module_name = module.version_check()['name']
            module_version = module.version_check()['version']
            print(f'main:import - {module_name}:{module_version}')
            modules.append(module)
        except Exception as e:
            print(f'main:error - {e}')
    return modules



if __name__ == '__main__':
    print('main - run')
    MODULES = import_modules('modules')

    for module in MODULES:
        print(module.version_check())