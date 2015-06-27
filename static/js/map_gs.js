ymaps.ready(function () {
    var myMap = new ymaps.Map('map', {
            center: [55.76, 37.64],
            zoom: 12
        }),
        objectManager = new ymaps.ObjectManager({
            // Чтобы метки начали кластеризоваться, выставляем опцию.
            clusterize: true,
            // ObjectManager принимает те же опции, что и кластеризатор.
            gridSize: 32
        });

    // Чтобы задать опции одиночным объектам и кластерам,
    // обратимся к дочерним коллекциям ObjectManager.
    objectManager.objects.options.set('preset', 'islands#redDotIcon');
    objectManager.clusters.options.set('preset', 'islands#redClusterIcons');
    myMap.geoObjects.add(objectManager);

    $.ajax({
        url: "/map-data"
    }).done(function(data) {
        objectManager.add(data);
    });

});