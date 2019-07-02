(function($) {

    // The home-page carousel. Items cycle every four seconds. Clicking a label stops the
    // cycling and shows the selected item.

    var carouselIndex = 1;

    var carouselInterval = window.setInterval(function() {
        showCarouselItem(carouselIndex);
        carouselIndex++;

        if (carouselIndex > 2) {
            carouselIndex = 0;
        }
    }, 4000);

    $(".carousel-item-label").click(function() {
        clearInterval(carouselInterval);

        var i = $(".carousel-item-label").index(this);
        showCarouselItem(i);
    });

    function showCarouselItem(i) {
        $(".carousel-item")
            .css("opacity", 0)
            .eq(i)
            .css("opacity", 1);

        $(".carousel-item-label")
            .removeClass("border-b-2")
            .eq(i)
            .addClass("border-b-2");
    }
})(jQuery);
