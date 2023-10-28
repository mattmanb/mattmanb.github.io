function loadArticle(name) {
    $("#article_frame").attr("src", name);
    console.log("article loaded");
}
function setHeight() {
     $("main").height((innerHeight)-100);
}
//set the height to match the window, refresh every second
setInterval(setHeight, 500);
