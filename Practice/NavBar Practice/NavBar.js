
var headerHeight = document.querySelector("header").offsetHeight;
function sticky() {
    // var headerHeight = document.querySelector("header").offsetHeight;
    if(window.pageYOffset > 100) {
        document.querySelector("nav").classList.add("fixed")
    }
    if(window.pageYOffset < 100) {
        document.querySelector("nav").classList.remove("fixed")
    }

    if(window.pageYOffset > headerHeight) {
        document.querySelector("nav").classList.add("bg-white")
    }
    if(window.pageYOffset < headerHeight) {
        document.querySelector("nav").classList.remove("bg-white")
    }
}
