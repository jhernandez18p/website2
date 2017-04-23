$(document).ready(function(){
    $(function(){
        var menu = $("#myMenu");
        $(window).scroll(function(){
            var scroll = $(window).scrollTop();
            if (scroll >= 80){
                if(!menu.hasClass("fixedMenu")){
                    menu.addClass('fixedMenu').fadeIn(1000);
                }
            } else {
                if(menu.hasClass("fixedMenu")){
                    menu.removeClass("fixedMenu").fadeIn(1000);
                }
            }
        });
    });

    var music = $("#music");
    var playButton = $("#play");
    var pauseButton = $("#pause");
    var playhead = $("#elapsed");
    var timeline = $("#slider");
    var timer = $("#timer");
    var duration;
    $("#pause").css("display","none");
    $("#pause").click( "click", function pause() {
        console.log( "stop audio" );
        document.getElementById('music').pause();
        $("#play").css("display","initial");
        $("#pause").css("display","none");
    });
    $("#play").click( "click", function play() {
        console.log( "play audio" );
        document.getElementById('music').play();
        $("#play").css("display","none");
        $("#pause").css("display","initial");
    });
    
    var swiper;
    swipper = new Swiper(
        '.social-carousel .swiper-container', {
            pagination: '.social-carousel .swiper-pagination',
            nextButton: '.social-carousel .swiper-button-next',
            prevButton: '.social-carousel .swiper-button-prev',
            paginationClickable: true
        }
    );
    
    swiper = new Swiper(
        '.groups-carousel .swiper-container', {
            pagination: '.groups-carousel .swiper-pagination',
            nextButton: '.groups-carousel .swiper-button-next',
            prevButton: '.groups-carousel .swiper-button-prev',
            paginationClickable: true,
            spaceBetween: 30,
        }
    );
    
    swiper = new Swiper(
        '.blog .swiper-container', {
            pagination: '.blog .swiper-pagination',
            slidesPerView: 'auto',
            paginationClickable: true,
            spaceBetween: 30,
            freeMode: true
        }
    );
    
    swiper = new Swiper(
        '.blog-lg .swiper-container', {
            pagination: '.blog-lg .swiper-pagination',
            slidesPerView: 'auto',
            paginationClickable: true,
            spaceBetween: 30,
            freeMode: true
        }
    );

    swiper = new Swiper(
        '.tv .swiper-container', {
            pagination: '.tv .swiper-pagination',
            slidesPerView: '1',
            paginationClickable: true,
            nextButton: '.tv .swiper-button-next',
            prevButton: '.tv .swiper-button-prev',
            // Disable preloading of all images
            preloadImages: false,
            // Enable lazy loading
            lazyLoading: true
        }
    );
});
