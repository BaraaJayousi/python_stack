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
    

    $("#search").keyup((e) => { 

        var searchLoader = "<div class='d-flex justify-content-start'><div class='spinner-border' role='status'><span class='visually-hidden'>Loading...</span></div></div>"

        $.ajax({
            url: $("#search-form").attr("action"),
            method: "GET",
            data: $("#search-form").serialize()
        }).done((res)=>{
            $("#search-loading").hide();
            $("#search-results").html(res);
            $("#search-results").show();
        })

        $("#search-results").hide();
        $("#search-loading").show();
        $("#search-loading").html(searchLoader);
        return false
    });  
    
    $("#search-results").on("click",".list-group-item",(e)=>{
        e.preventDefault()
        elements = $(".list-group-item").toArray()
        elements.forEach(element => {
            $(element).removeClass("active");
        });
        
        $(e.target).addClass("active");
    })
    
})