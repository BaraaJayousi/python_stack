$(()=>{
    $("#username, #email, #confirm-pw").keyup((e) =>{ 
        let data = $("#regForm").serialize()
        console.log(data)

        // Start AJAX code
        $.ajax({
            method: "POST",
            url: "/check-data",
            data: data,
            cache: false,
            success: (res)=>{
                $("#loading").hide();
                $("#username-msg").show();
                $("#username-msg").html(res);
            }
        })
        let loader = "<div class='spinner-grow m-3' role='status'><span class='visually-hidden'>Loading...</span></div>"
        $("#loading").html(loader)
        $("#loading").show();
        $("#username-msg").hide();

    });
})