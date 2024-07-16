document.getElementById("myForm").addEventListener("submit", function (event) {
    event.preventDefault(); 
    document.getElementById("loading-screen").style2.display = "flex";
setTimeout(function () {
        document.getElementById("loading-screen").style2.display = "none";
    }, 10000);
});
