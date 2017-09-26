$('.rbac-menu-header').click(function () {
    $(this).next().toggleClass('rbac-hide');
    //$(this).next().removeClass('rbac-hide').parent().siblings().find('.rbac-menu-body').addClass('rbac-hide');
});