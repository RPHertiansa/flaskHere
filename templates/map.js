let platform = new H.service.Platform({
    'apikey': 'eTkvMZBgvLBhS0UZvwtl_1seMMqr80'
})

const lat = -10;
const long = 104;

let maptypes = platform.createDefault.Layers()

let map = new H.map(
    document.getElementById('mapContainer'),
    maptypes.vector.normal.map,
    {
        zoom: 10,
        center: { lat: lat, lng: long}
    }
);

let marker = new H.map.Marker({lat: lat, lng: long})

map.addObject(marker)