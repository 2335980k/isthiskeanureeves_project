$('#likes').click(function(){
    var pageid;
    pageid = $(this).attr("data-catid");
    $.get('/isthiskeanureeves/rating/', {category_id: pageid}, function(data){
        $('#like_count').html(data);
            $('#likes').hide();
    });
});