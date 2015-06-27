% include('header.tpl', title='Page Title', meta_d='123', meta_k='345',)
% include('first_block.tpl',)


<h1>{{ g.name }} </h1>

<img class="center-block img-responsive" src="/dynamic/{{ g.image }}" alt="">

<p class="lead">
{{g.text}}
</p>

<script type="text/javascript" src="//yastatic.net/share/share.js" charset="utf-8"></script><div class="yashare-auto-init" data-yashareL10n="ru" data-yashareType="small" data-yashareQuickServices="vkontakte,facebook,twitter,odnoklassniki,moimir,gplus,surfingbird" data-yashareTheme="counter"></div>

<div id="disqus_thread"></div>
<script type="text/javascript">
    /* * * CONFIGURATION VARIABLES * * */
    var disqus_shortname = 'graffity19';
    
    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function() {
        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
        dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>


% include('map_block.tpl',)
% include('footer.tpl', map_g=True)