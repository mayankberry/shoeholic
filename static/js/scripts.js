$(window).scroll(function(){
    var scroll = $(window).scrollTop();
    $('.zoom').css({
        width : (80 + scroll/5) + "%",
        opacity : (1- scroll/550)
    })
    $('.parallax-text').css({
        opacity : (1- scroll/550)
    })



    if (document.documentElement.scrollTop > 500) {
        document.getElementById('shoe2').className = 'zoom3';
        $('.zoom3').css({
            width : (80 + scroll/20) + "%"
        }) 
    }
    // $('.zoom2').css({
    //     width : (80 + scroll > 300) - "%"
    // })
})

