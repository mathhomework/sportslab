$(document).ready(function(){
    $("#submit_form").on("submit", function(){
        var link = $("#link").val();
        $('#link').attr("value", "");
        var link_json = JSON.stringify({'link':link});
        console.log(link);
        console.log(link_json);
        $.ajax({
            url:"/do_scrape/",
            data: link_json,
            type:"POST",
            dataType: "json",
            success:function(data){
                console.log("success");
            },
            error:function(data){
                console.log("failure");
            }
        });

    })
}());