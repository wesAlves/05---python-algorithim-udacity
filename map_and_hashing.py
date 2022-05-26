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
    if key != 'Africa':
        for country in locations[key]:
            for city in sorted(locations[key][country]):
                print(city)
