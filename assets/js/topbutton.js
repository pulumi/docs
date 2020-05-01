// Scroll to top button
(function ($) {
    $(document).ready(function () {
        $(window).scroll(function () {
          if ($(this).scrollTop() > 2500) {
            $(".top-button").fadeIn();
          } else {
            $(".top-button").fadeOut();
          }
        });
      
        $(".top-button").click(function () {
          $("html, body").animate({
            scrollTop: 0
          }, 100);
            return false;
        });
      
      });
})(jQuery)
