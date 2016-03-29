$(document).ready(function() {

    var gems = $('.gems');

    var desktop = $(window).width() > 1350;

    if(desktop) {
        $(window).scroll(function() {
            var scrolled = $(window).scrollTop();
            gems.css({
                'background-position-x': (scrolled*0.05)+'%'
            });
        });
    }

});