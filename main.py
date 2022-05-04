module_list = []

if __name__ == '__main__':
    print('main - run')
    
    try:
        from submodule import submodule
        module = submodule.version_check()
        module_name = module['name']
        module_version = module['version']
        print(f'submodule - {module_name}:{module_version}')
        module_list.append(module)
    except ImportError:
        print('main - import error')