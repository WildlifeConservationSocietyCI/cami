barrier_types = ['unknown', 'not a barrier', 'partial barrier', 'complete barrier']

conflict_matrix = {
    'Procapra_gutturosa': {
        'road': {
            'not a barrier': [
                ('type_', 'paved'),
                ('type_', 'unpaved'),
                ('type1', 'local road'),
                ('traffic', 'low [<=1 car/hour]'),
            ],
            'partial barrier': [
                ('type1', 'major road'),
                ('type1', 'highway'),
                ('traffic', 'medium [2-60 cars/hour]'),
            ],
            'complete barrier': [
                ('traffic', 'high [>= 1 car/minute]'),
            ],
        },
        'railroad': {
            'not a barrier': [
                ('speed', 'low'),
                ('track', 'single track'),
            ],
            'partial barrier': [
                ('speed', 'regular train'),
                ('speed', 'high speed train'),
            ],
            'unknown': [
                ('track', 'double track'),
            ],
        },
        'fence': {
            'partial barrier': [
                ('type_', 'tight barbed wire'),
                ('type_', 'woven barbed wire'),
                ('height', 'low [<1m]'),
                ('height', 'medium'),
                ('bottom_gap', 'high [>30cm]'),
            ],
            'complete barrier': [
                ('type_', 'metal panel'),
                ('type_', 'not barbed - horizontal'),
                ('type_', 'not barbed - vertical'),
                ('type_', 'chain link'),
                ('bottom_gap', 'low [<30cm]'),
                ('height', 'high [>2m]'),
            ],
            'unknown': [
                ('covered', 'yes'),
                ('covered', 'no'),
            ],
        },
        'pipeline': {
            'unknown': [
                ('buried', 'yes'),
                ('buried', 'yes, with a berm'),
                ('buried', 'no'),
                ('trenches', 'trenches'),
                ('trenches', 'no trenches'),
            ],
        },
    },
    'Equus_hemionus': {
        'road': {
            'not a barrier': [
                ('type_', 'paved'),
                ('type_', 'unpaved'),
                ('type1', 'local road'),
                ('traffic', 'low [<=1 car/hour]'),
            ],
            'partial barrier': [
                ('type1', 'major road'),
                ('type1', 'highway'),
                ('traffic', 'medium [2-60 cars/hour]'),
            ],
            'complete barrier': [
                ('traffic', 'high [>= 1 car/minute]'),
            ],
        },
        'railroad': {
            'not a barrier': [
                ('track', 'single track'),
            ],
            'unknown': [
                ('track', 'double track'),
                ('speed', 'slow train'),
                ('speed', 'regular train'),
                ('speed', 'high speed train'),
            ],
        },
        'fence': {
            'partial barrier': [
                ('type_', 'ditch / trench'),
                ('height', 'low [<1m]'),
            ],
            'complete barrier': [
                ('type_', 'metal panel'),
                ('type_', 'tight barbed wire'),
                ('type_', 'woven barbed wire'),
                ('type_', 'not barbed - horizontal'),
                ('type_', 'not barbed - vertical'),
                ('type_', 'chain link'),
                ('height', 'medium'),
                ('height', 'high [>2m]'),
                ('bottom_gap', 'low [<30cm]'),
                ('bottom_gap', 'high [>30cm]'),
            ],
            'unknown': [
                ('covered', 'yes'),
                ('covered', 'no'),
            ],
        },
        'pipeline': {
            'not a barrier': [
                ('buried', 'yes'),
                ('buried', 'yes, with a berm'),
                ('trenches', 'no trenches'),
            ],
            'partial barrier': [
                ('trenches', 'trenches'),
            ],
            'complete barrier': [
                ('buried', 'no'),
            ],
        },
    },
    'Camelus_bactrianus': {
        'road': {
            'not a barrier': [
                ('type1', 'local road'),
            ],
            'partial barrier': [
                ('type_', 'unpaved'),
                ('type1', 'major road'),
                ('traffic', 'low [<=1 car/hour]'),
            ],
            'complete barrier': [
                ('type_', 'paved'),
                ('type1', 'highway'),
                ('traffic', 'medium [2-60 cars/hour]'),
                ('traffic', 'high [>= 1 car/minute]'),
            ],
        },
        'railroad': {
            'partial barrier': [
                ('speed', 'low'),
                ('speed', 'regular train'),
            ],
            'complete barrier': [
                ('track', 'single track'),
                ('track', 'double track'),
                ('speed', 'high speed train'),
            ],
        },
        'fence': {
            'not a barrier': [
                ('height', 'low [<1m]'),
            ],
            'partial barrier': [
                ('height', 'medium'),
            ],
            'complete barrier': [
                ('type_', 'metal panel'),
                ('type_', 'tight barbed wire'),
                ('type_', 'woven barbed wire'),
                ('type_', 'not barbed - horizontal'),
                ('type_', 'not barbed - vertical'),
                ('type_', 'chain link'),
                ('height', 'high [>2m]'),
                ('bottom_gap', 'low [<30cm]'),
                ('bottom_gap', 'high [>30cm]'),
                ('covered', 'yes'),
                ('covered', 'no'),
            ],
            'unknown': [
                ('type_', 'ditch / trench'),
            ],
        },
        'pipeline': {
            'unknown': [
                ('buried', 'yes'),
                ('buried', 'yes, with a berm'),
                ('buried', 'no'),
                ('trenches', 'trenches'),
                ('trenches', 'no trenches'),
            ],
        },
    },
    'Saiga_spp': {
        'road': {
            'not a barrier': [
                ('type_', 'paved'),
                ('type_', 'unpaved'),
                ('type1', 'local road'),
                ('traffic', 'low [<=1 car/hour]'),
            ],
            'partial barrier': [
                ('type1', 'major road'),
                ('traffic', 'medium [2-60 cars/hour]'),
            ],
            'complete barrier': [
                ('type1', 'highway'),
                ('traffic', 'high [>= 1 car/minute]'),
            ],
        },
        'railroad': {
            'partial barrier': [
                ('track', 'single track'),
                ('speed', 'low'),
                ('speed', 'regular train'),
            ],
            'complete barrier': [
                ('track', 'double track'),
                ('speed', 'high speed train'),
            ],
        },
        'fence': {
            'partial barrier': [
                ('type_', 'woven barbed wire'),
                ('type_', 'not barbed - horizontal'),
                ('type_', 'not barbed - vertical'),
                ('type_', 'ditch / trench'),
                ('type_', 'chain link'),
                ('height', 'low [<1m]'),
                ('height', 'medium'),
                ('height', 'high [>2m]'),
                ('bottom_gap', 'high [>30cm]'),
            ],
            'complete barrier': [
                ('type_', 'metal panel'),
                ('type_', 'tight barbed wire'),
                ('bottom_gap', 'low [<30cm]'),
                ('covered', 'yes'),
                ('covered', 'no'),
            ],
        },
        'pipeline': {
            'not a barrier': [
                ('buried', 'yes'),
                ('buried', 'yes, with a berm'),
                ('trenches', 'no trenches'),
            ],
            'partial barrier': [
                ('trenches', 'trenches'),
            ],
            'complete barrier': [
                ('buried', 'no'),
            ],
        },
    },
    'Acinonyx_jubatus_venaticus': {
        'road': {
            'not a barrier': [
                ('type_', 'paved'),
                ('type_', 'unpaved'),
                ('type1', 'local road'),
                ('type1', 'major road'),
                ('type1', 'highway'),
                ('traffic', 'low [<=1 car/hour]'),
            ],
            'partial barrier': [
                ('traffic', 'medium [2-60 cars/hour]'),
                ('traffic', 'high [>= 1 car/minute]'),
            ],
        },
        'railroad': {
            'unknown': [
                ('track', 'single track'),
                ('track', 'double track'),
                ('speed', 'low'),
                ('speed', 'regular train'),
                ('speed', 'high speed train'),
            ],
        },
        'fence': {
            'not a barrier': [
                ('bottom_gap', 'low [<30cm]'),
                ('bottom_gap', 'high [>30cm]'),
                ('covered', 'no'),
            ],
            'partial barrier': [
                ('type_', 'not barbed - horizontal'),
                ('type_', 'not barbed - vertical'),
                ('height', 'low [<1m]'),
            ],
            'complete barrier': [
                ('type_', 'metal panel'),
                ('type_', 'tight barbed wire'),
                ('type_', 'woven barbed wire'),
                ('type_', 'chain link'),
                ('height', 'medium'),
                ('height', 'high [>2m]'),
                ('covered', 'yes'),
            ],
            'unknown': [
                ('type_', 'ditch / trench'),
            ],
        },
        'pipeline': {
            'not a barrier': [
                ('buried', 'yes'),
                ('buried', 'yes, with a berm'),
            ],
            'unknown': [
                ('buried', 'no'),
                ('trenches', 'trenches'),
                ('trenches', 'no trenches'),
            ],
        },
    },
    'Cervus_hanglu_bactrianus': {
        'road': {
            'not a barrier': [
                ('type_', 'paved'),
                ('type_', 'unpaved'),
                ('type1', 'local road'),
                ('traffic', 'low [<=1 car/hour]'),
                ('traffic', 'medium [2-60 cars/hour]'),
            ],
            'partial barrier': [
                ('type1', 'major road'),
                ('traffic', 'high [>= 1 car/minute]'),
            ],
            'complete barrier': [
                ('type1', 'highway'),
            ],
        },
        'railroad': {
            'not a barrier': [
                ('track', 'single track'),
                ('speed', 'low'),
                ('speed', 'regular train'),
            ],
            'partial barrier': [
                ('track', 'double track'),
                ('speed', 'high speed train'),
            ],
        },
        'fence': {
            'not a barrier': [
                ('type_', 'ditch / trench'),
                ('height', 'low [<1m]'),
                ('bottom_gap', 'high [>30cm]'),
            ],
            'partial barrier': [
                ('type_', 'metal panel'),
                ('type_', 'not barbed - horizontal'),
                ('type_', 'not barbed - vertical'),
                ('height', 'medium'),
                ('bottom_gap', 'low [<30cm]'),
            ],
            'complete barrier': [
                ('type_', 'tight barbed wire'),
                ('type_', 'woven barbed wire'),
                ('type_', 'chain link'),
                ('height', 'high [>2m]'),
                ('covered', 'yes'),
            ],
            'unknown': [
                ('covered', 'no'),
            ],
        },
        'pipeline': {
            'not a barrier': [
                ('buried', 'yes'),
                ('buried', 'yes, with a berm'),
                ('trenches', 'trenches'),
                ('trenches', 'no trenches'),
            ],
            'partial barrier': [
                ('buried', 'no'),
            ],
        },
    },
    'Gazella_bennettii': {
        'road': {
            'not a barrier': [
                ('type_', 'paved'),
                ('type_', 'unpaved'),
                ('type1', 'local road'),
                ('type1', 'major road'),
                ('traffic', 'low [<=1 car/hour]'),
            ],
            'partial barrier': [
                ('type1', 'highway'),
                ('traffic', 'medium [2-60 cars/hour]'),
                ('traffic', 'high [>= 1 car/minute]'),
            ],
        },
        'railroad': {
            'unknown': [
                ('track', 'single track'),
                ('track', 'double track'),
                ('speed', 'low'),
                ('speed', 'regular train'),
                ('speed', 'high speed train'),
            ],
        },
        'fence': {
            'not a barrier': [
                ('height', 'low [<1m]'),
                ('bottom_gap', 'low [<30cm]'),
                ('bottom_gap', 'high [>30cm]'),
            ],
            'partial barrier': [
                ('type_', 'tight barbed wire'),
                ('type_', 'woven barbed wire'),
                ('type_', 'not barbed - horizontal'),
                ('type_', 'not barbed - vertical'),
                ('height', 'medium'),
            ],
            'complete barrier': [
                ('type_', 'metal panel'),
                ('type_', 'chain link'),
                ('height', 'high [>2m]'),
                ('covered', 'yes'),
            ],
            'unknown': [
                ('type_', 'ditch / trench'),
                ('covered', 'no'),
            ],
        },
        'pipeline': {
            'not a barrier': [
                ('buried', 'yes'),
                ('buried', 'yes, with a berm'),
            ],
            'unknown': [
                ('buried', 'no'),
                ('trenches', 'trenches'),
                ('trenches', 'no trenches'),
            ],
        },
    },
    'Gazella_subgutturosa': {
        'road': {
            'not a barrier': [
                ('type_', 'paved'),
                ('type_', 'unpaved'),
                ('type1', 'local road'),
                ('type1', 'major road'),
                ('traffic', 'low [<=1 car/hour]'),
            ],
            'partial barrier': [
                ('traffic', 'medium [2-60 cars/hour]'),
            ],
            'complete barrier': [
                ('type1', 'highway'),
                ('traffic', 'high [>= 1 car/minute]'),
            ],
        },
        'railroad': {
            'not a barrier': [
                ('speed', 'low'),
                ('speed', 'regular train'),
            ],
            'partial barrier': [
                ('speed', 'high speed train'),
            ],
            'unknown': [
                ('track', 'single track'),
                ('track', 'double track'),
            ],
        },
        'fence': {
            'not a barrier': [
                ('height', 'low [<1m]'),
                ('covered', 'no'),
            ],
            'partial barrier': [
                ('type_', 'ditch / trench'),
                ('height', 'medium'),
                ('bottom_gap', 'high [>30cm]'),
            ],
            'complete barrier': [
                ('type_', 'metal panel'),
                ('type_', 'tight barbed wire'),
                ('type_', 'woven barbed wire'),
                ('type_', 'not barbed - horizontal'),
                ('type_', 'not barbed - vertical'),
                ('type_', 'chain link'),
                ('height', 'high [>2m]'),
                ('bottom_gap', 'low [<30cm]'),
                ('covered', 'yes'),
            ],
        },
        'pipeline': {
            'not a barrier': [
                ('buried', 'yes'),
                ('buried', 'yes, with a berm'),
                ('buried', 'no'),
            ],
            'unknown': [
                ('trenches', 'trenches'),
                ('trenches', 'no trenches'),
            ],
        },
    },
    'Ovis_ammon': {
        'road': {
            'not a barrier': [
                ('type_', 'unpaved'),
                ('type1', 'local road'),
                ('traffic', 'low [<=1 car/hour]'),
            ],
            'partial barrier': [
                ('type_', 'paved'),
                ('type1', 'major road'),
                ('type1', 'highway'),
                ('traffic', 'medium [2-60 cars/hour]'),
            ],
            'complete barrier': [
                ('traffic', 'high [>= 1 car/minute]'),
            ],
        },
        'railroad': {
            'not a barrier': [
                ('speed', 'low'),
            ],
            'partial barrier': [
                ('track', 'single track'),
                ('track', 'double track'),
                ('speed', 'regular train'),
                ('speed', 'high speed train'),
            ],
        },
        'fence': {
            'partial barrier': [
                ('type_', 'ditch / trench'),
                ('height', 'low [<1m]'),
                ('height', 'medium'),
                ('covered', 'no'),
            ],
            'complete barrier': [
                ('type_', 'metal panel'),
                ('type_', 'tight barbed wire'),
                ('type_', 'woven barbed wire'),
                ('type_', 'not barbed - horizontal'),
                ('type_', 'not barbed - vertical'),
                ('type_', 'chain link'),
                ('height', 'high [>2m]'),
                ('bottom_gap', 'low [<30cm]'),
                ('bottom_gap', 'high [>30cm]'),
                ('covered', 'yes'),
            ],
        },
        'pipeline': {
            'not a barrier': [
                ('buried', 'yes'),
                ('buried', 'yes, with a berm'),
                ('trenches', 'trenches'),
                ('trenches', 'no trenches'),
            ],
            'complete barrier': [
                ('buried', 'no'),
            ],
        },
    },
    'Panthera_uncia': {
        'road': {
            'not a barrier': [
                ('type_', 'unpaved'),
                ('type1', 'local road'),
                ('traffic', 'low [<=1 car/hour]'),
                ('traffic', 'medium [2-60 cars/hour]'),
            ],
            'partial barrier': [
                ('type_', 'paved'),
                ('type1', 'major road'),
                ('type1', 'highway'),
                ('traffic', 'high [>= 1 car/minute]'),
            ],
        },
        'railroad': {
            'not a barrier': [
                ('speed', 'low'),
            ],
            'partial barrier': [
                ('track', 'single track'),
                ('track', 'double track'),
                ('speed', 'regular train'),
                ('speed', 'high speed train'),
            ],
        },
        'fence': {
            'not a barrier': [
                ('type_', 'ditch / trench'),
                ('height', 'low [<1m]'),
                ('bottom_gap', 'high [>30cm]'),
            ],
            'partial barrier': [
                ('type_', 'woven barbed wire'),
                ('type_', 'not barbed - horizontal'),
                ('type_', 'not barbed - vertical'),
                ('height', 'medium'),
                ('height', 'high [>2m]'),
                ('bottom_gap', 'low [<30cm]'),
                ('covered', 'no'),
            ],
            'complete barrier': [
                ('type_', 'metal panel'),
                ('type_', 'tight barbed wire'),
                ('type_', 'chain link'),
                ('covered', 'yes'),
            ],
        },
        'pipeline': {
            'not a barrier': [
                ('buried', 'yes'),
                ('buried', 'yes, with a berm'),
                ('buried', 'no'),
                ('trenches', 'trenches'),
                ('trenches', 'no trenches'),
            ],
        },
    },
}
