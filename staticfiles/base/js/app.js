$(document).ready(function(){
    // *Initializer
    $('#prayModal').modal('show');

    // *Modal resizer
    function setModalMaxHeight(element){
        this.$element = $(element);
        this.$content = this.$element.find('.modal-content');
        var borderWidth = this.$content.outerHeight() - this.$content.innerHeight();
        var dialogMargin = $(window).width() < 768 ? 20 : 60;
        var contentHeight = $(window).height() - (dialogMargin + borderWidth);
        var headerHeight  = this.$element.find('.modal-header').outerHeight() || 0;
        var footerHeight = this.$element.find('.modal-footer').outerHeight() || 0;
        var maxHeight = contentHeight - (headerHeight + footerHeight);

        this.$content.css({
            'overflow': 'hidden'
        });

        this.$element.find('.modal-body').css({
            'max-height': maxHeight,
            'overflow-y': 'auto'
        });
    }

    $('.modal').on('show.bs.modal', function(){
        $(this).show();
        setModalMaxHeight(this);
    });

    $(window).resize(function(){
        if ($('.modal.in').length != 0){
            setModalMaxHeight($('.modal.in'));
        }
    });

    // *Scroll function
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


});
