$(document).ready(function () {
    $(document).on("click", "#myid", function () {
        // console.log("ㅇㅇㅇ")
        // $("#boothinfe").hide();
        // alert("a")
        // console.log("ㅇㅇㅇ")
        console.log("#"+ $(this).val())
        const offset = $("#"+ $(this).val()).offset();
        const offset2 = $("#target").offset();

        console.log(offset2)
        if (offset2.top =! 381.9375){
            $('#scroll').animate({scrollTop: 0});
            $('#scroll').animate({scrollTop: offset.top -400}, 1000);
        } else {
            $('#scroll').animate({scrollTop: offset.top -400}, 1000);
        }
    });
});
