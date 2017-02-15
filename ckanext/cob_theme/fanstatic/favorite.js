// Based on http://www.bootply.com/62742

$('#vizcarousel').carousel({
    interval: 0 // remove interval for manual sliding
});

// when the carousel slides, load the ajax content
$('#vizcarousel').on('slid', function (e) {
    // get index of currently active item
    var idx = $('#vizcarousel .item.active').index();
    var url = $('.item.active').data('url');
    $('.item').removeClass('in');
    // ajax load from data-url
        $('.item.active').load(url,function(result){
            $(this).addClass('in');
        });
});

$('.carousel-inner').hover(
    function (){
        $('#vizcarousel .vizcarousel-desc').addClass('active');
    },
    function () {
        $('#vizcarousel .vizcarousel-desc').removeClass('active');
    }
);

$('[data-slide-number=0]').load($('[data-slide-number=0]').data('url'),function(result){
    $('#vizcarousel').carousel(0);
});

function initNewDropdown (){
    // assign initial value
    var formerSelectedValue =  $("#field-order-by").find("[selected='selected']").html();
    if (!formerSelectedValue){
        formerSelectedValue = $("#field-order-by").find("option").html();
    }
    $("#field-order-by-stylable").find("dt").find(".value").append(formerSelectedValue);
    // mimic select element: make the options toggle
    $("#field-order-by-stylable dt a").click(function() {
        $("#field-order-by-stylable dd ul").toggle();
    });
    // mimic select element: show the selected value to the select box if clicked
    $("#field-order-by-stylable ul li a").click(function() {
        var text = $(this).html();
        $("#field-order-by-stylable dt a span").html(text);
        $("#field-order-by-stylable dd ul").hide();
    });
}

initNewDropdown();

// make the submit happen
$("#field-order-by-stylable dd ul li a").click(function() {
    // bind the original select element 
    var text = $(this).find('.value').html();
    
    var formerSelected = $("#field-order-by").find("[selected='selected']");
    formerSelected.removeAttr("selected")

    var nowSelected = $("#field-order-by").find("[value='"+text+"']");
    nowSelected.attr("selected","selected");

    // trigger submit
    $(".control-order-by").find('[type="submit"]').click();

})
