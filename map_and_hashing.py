locations = {
    'North America': {
        'USA': [
            'Mountain View',
            'Atlanta'
        ]
    },
    'Africa': {
        'Egypt': [
            'Cairo'
        ]
    },
    'Asia': {
        'India': [
            'Bangalore'
        ],
        "China": [
            'Shanghai'
        ]
    }
}


for key in locations.keys():
    for country in locations[key]:
        print(sorted(locations[key][country]))
