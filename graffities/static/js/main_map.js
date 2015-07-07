ymaps.ready(function () {
    var myMap = new ymaps.Map('map', {
            center: [55.76, 37.64],
            zoom: 12
        },{suppressMapOpenBlock: true}),
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
        url: "/api/graffities"
    }).done(function(data) {
        // полученные данные приведем к требуемой структуре
        // https://tech.yandex.ru/maps/doc/jsapi/2.1/ref/reference/ObjectManager-docpage/#add
        // проблема в том, что при больших данных надо будет использовать pagination
        var add_data = {
          "type": "FeatureCollection",
          "features": []
        }
        for (i = 0; i < data.length; i++) {
          add_data["features"].push(
            {
              "type": "Feature",
              "id": i,
              "geometry": {
                "type": "Point",
                "coordinates": [data[i]["lat"], data[i]["lon"]]
                },
              "properties": {
                "balloonContentHeader": data[i]["name"],
                "balloonContent": '<center><a href="/graffiti/'+ data[i]["id"] +'"><img class="img-responsive" src="'+ data[i]["photo"] +'" width="250px" height="250px"></a></center>',
                "balloonContentFooter": '<center><a href="/graffiti/'+ data[i]["id"] +'">Посмотреть и обсудить</a></center>',
                "clusterCaption": "Граффити №" + data[i]["id"],
                "hintContent": data[i]["name"]
              }
            }
          );
        }
        objectManager.add(add_data);
    });

});
