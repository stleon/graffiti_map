<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="google-site-verification" content="" />
  <meta name='yandex-verification' content='' />

  <title>Graffiry Net - {{ title }}</title>
  <meta name="description" content="{{ meta_d }}">
  <meta name="keywords" content="{{ meta_k }}">
  <link rel="icon" href="/static/favicon-black.ico">
  <link rel="stylesheet" href="/static/css/bootstrap.min.css">
  <link rel="stylesheet" href="/static/css/bootstrap-theme.min.css">
  <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  <link href="/static/css/main.css" rel="stylesheet">
</head>
<body>
  <nav class="navbar navbar-inverse navbar-default navbar-fixed-top">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
        <span class="sr-only">Переключить навигацию</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="/">Graffity Net</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li
        % if defined('main'):
            class="active"
        % end
        ><a href="/">Главная</a></li>


      </ul>


    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
