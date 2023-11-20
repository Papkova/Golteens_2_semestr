window.onload = function () {
    let username = document.getElementById("zmina");
    let username_ = prompt("What is your name");
    let result= "Name: " + username_;
    username.innerHTML = result;
}