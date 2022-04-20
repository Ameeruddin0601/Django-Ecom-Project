$(document).ready(function(){
    $('.dot1').click(function(){
        $('.img1').css('display','block');
        $('.img2').css('display','none');
        $('.img3').css('display','none');
    });
    $('.dot2').click(function(){
        $('.img1').css('display','none');
        $('.img2').css('display','block');
        $('.img3').css('display','none');
    });
    $('.dot3').click(function(){
        $('.img1').css('display','none');
        $('.img2').css('display','none');
        $('.img3').css('display','block');
    });

    $(window).on('scroll load', function(){
        if($(window).scrollTop() > 10){
            $('#header').addClass('header-active');
        }else{
            $('#header').removeClass('header-active');
        }
    });
});