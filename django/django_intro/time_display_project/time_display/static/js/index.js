$(()=>{
    $("div").slideUp(300);
    setTimeout(()=>{
        $("div").slideDown(400);

    },1000)
    setInterval(() => {
        $("div").fadeToggle(1000);
    }, 3000);
});