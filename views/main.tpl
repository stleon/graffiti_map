% include('header.tpl', title='Page Title', meta_d='123', meta_k='345', main=True)
% include('first_block.tpl',)


<h1>Граффити на карте Москвы</h1>


<table class="table table-hover table-responsive">
	%for g in gs:
	
		<tr>
			<td>
			<a href="graffities/{{ g.id }}">
			<img class="img-rounded" src="/dynamic/{{ g.image }}" style="width: 400px; height: 275px;">
			</a>
			</td>
			<td>
			<p class="lead">{{g.name}}</p>
			<p class="lead"><span class="glyphicon glyphicon-time" aria-hidden="true"></span> {{ g.date_created.strftime("%H:%M:%S") }}</p>
			<p class="lead"><span class="glyphicon glyphicon-calendar" aria-hidden="true"></span> {{ g.date_created.strftime("%d-%m-%Y") }}</p>
			<p class="lead"><span class="glyphicon glyphicon-hand-right" aria-hidden="true"></span> <a href="graffities/{{ g.id }}">Подробнее</a></p>
			</td>
		</tr>

	%end
</table>


% include('map_block.tpl',)
% include('footer.tpl', map_g=True)