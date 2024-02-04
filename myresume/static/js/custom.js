
  (function ($) {
  
  "use strict";

    // PRE LOADER
    $(window).load(function(){
      $('.preloader').fadeOut(1000); // set duration in brackets
      var value = document.getElementsByClassName("my-custom")[0].innerText.replace(/(\d{1})(\d{3})(\d{3})(\d{3})/, "+84 ($2)-$3-$4");
      var arr = document.getElementsByClassName("my-custom");
      for (let i = 0; i < arr.length; i ++){
          arr[i].innerText = value;
      }
    });

    // CUSTOM LINK
    $('.custom-link').click(function(){
    var el = $(this).attr('href');
    var elWrapped = $(el);
    var header_height = $('.navbar').height() + 10;

    scrollToDiv(elWrapped,header_height);
    return false;

    function scrollToDiv(element,navheight){
      var offset = element.offset();
      var offsetTop = offset.top;
      var totalScroll = offsetTop-navheight;

      $('body,html').animate({
      scrollTop: totalScroll
      }, 300);
  }
});
    
  })(window.jQuery);


