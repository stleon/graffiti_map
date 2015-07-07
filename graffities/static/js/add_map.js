ymaps.ready(init);
var myMap;

function init () {
  var lat = $('#id_lat').val();
  var lon = $('#id_lon').val();
  var zoom = 11

  if (lat && lon) {
    var do_balloon = true;
    zoom = 17
  }
  else{
    lat = 55.753559;
    lon = 37.609218;
  }

    myMap = new ymaps.Map("map", {
        center: [lat, lon],
        zoom: zoom
    }, {
        balloonMaxWidth: 200,
        searchControlProvider: 'yandex#search',
        suppressMapOpenBlock: true
    });

    // Если координаты есть, добавим балун
    if (do_balloon) {
      var myPlacemark = new ymaps.Placemark(myMap.getCenter(), {}, {
          preset: 'islands#redDotIcon'
        });

        myMap.geoObjects.add(myPlacemark);
    }


    // Обработка события, возникающего при щелчке
    // левой кнопкой мыши в любой точке карты.
    // При возникновении такого события откроем балун.
    myMap.events.add('click', function (e) {
        if (!myMap.balloon.isOpen()) {
            var coords = e.get('coords');
            $('#id_lat').val(coords[0].toPrecision(8));
            $('#id_lon').val(coords[1].toPrecision(8));
            myMap.balloon.open(coords, {
                contentHeader:'Ура!',
                contentBody:'<p>Вы отметили граффити на карте.</p>' +
                    '<p>Координаты граффити: ' + [
                    coords[0].toPrecision(8),
                    coords[1].toPrecision(8)
                    ].join(', ') + '</p>',
                contentFooter:'<sup>Мы обязательно проверим :)</sup>'
            });
        }
        else {
            myMap.balloon.close();
        }
    });

    // Обработка события, возникающего при щелчке
    // правой кнопки мыши в любой точке карты.
    // При возникновении такого события покажем всплывающую подсказку
    // в точке щелчка.
    myMap.events.add('contextmenu', function (e) {
        myMap.hint.open(e.get('coords'), 'Щелкните левой кнопкой');
    });

    // Скрываем хинт при открытии балуна.
    myMap.events.add('balloonopen', function (e) {
        myMap.hint.close();
    });
}
