

if __name__ == '__main__':
    print('main - run')
    
    try:
        from submodule import submodule
        print(f'submodule - {submodule.version_check()}')
    except ImportError:
        print('main - import error')