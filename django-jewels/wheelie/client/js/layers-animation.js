$(document).ready(function() {

    var plant = $('.splash-illustration-plant');
    var hill = $('.splash-illustration-hill');
    var bghill = $('.splash-illustration-background-hill');
    var goblin = $('.splash-illustration-goblin');
    var castle = $('.splash-illustration-castle');
    var fgclouds = $('.splash-illustration-foreground-clouds');
    var logo = $('.splash-illustration-logo');
    var bgclouds = $('.splash-illustration-background-clouds');


    $(window).scroll(function() {
        var scrolled = $(window).scrollTop();

        parallax(plant, scrolled, -0.2);
        parallax(goblin, scrolled, 0.162);
        parallax(fgclouds, scrolled, 0.262);
        parallax(castle, scrolled, 0.424);
        parallax(bgclouds, scrolled, 0.685);
        parallax(logo, scrolled, 0.424);
        parallax(bghill, scrolled, 0.1, -1);
    });

    function parallax(div, scrolled, ratio, scaleX) {
        //assign a default value of 1 to the scaleX property
        scaleX = scaleX || 1;

        div.css({
            'transform': 'scaleX('+scaleX +') translate3d(0,'+(scrolled*ratio)+'px, 0)'
        })
    }

});