def resolve_settings(base_config=None, override=None, built_in_defaults=None):
    # TODO: handle the mutable default argument problem for all three dict parameters.
    # Then resolve each of the four known settings by checking override first,
    # then base_config, then built_in_defaults — using "key exists" checks,
    # NOT truthiness checks, since 0/False/"" are valid explicit values.
    
    resolve = {}

    if override == None:
        override = {}

    if base_config == None:
        base_config = {}
        
    if built_in_defaults == None:
        built_in_defaults = {'timeout': 30, 'retries': 3, 'verbose': False, 'cache': True}

    for setting in built_in_defaults:
        if setting in override:
            resolve[setting] = override[setting]
        elif setting in base_config:
            resolve[setting] = base_config[setting]
        else:
            resolve[setting] = built_in_defaults[setting]
    
    return resolve

print(resolve_settings())
print(resolve_settings(base_config={'timeout': 60}))
print(resolve_settings(base_config={'retries': 5}, override={'retries': 0}))
