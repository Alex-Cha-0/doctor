const btnGeo = document.querySelector('.btn-geo')



btnGeo.addEventListener('click', (e) => {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition((position) => {
            const {coords} = position;
            alert(`широта - ${coords.latitude}, долгота - ${coords.longitude}`);
            // writeGeoToScreen(`https://www.openstreetmap.org/#map=15/${coords.latitude}/${coords.longitude}`);
            document.getElementById('id_latitude').value = `${coords.latitude}`
            document.getElementById('id_longitude').value = `${coords.longitude}`
        });
    }
})
