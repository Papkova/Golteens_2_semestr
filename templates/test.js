window.onload = function () {
    let password = document.getElementById("zmina");
    let password_ = prompt("Enter your password");
    let result= "Password: " + password_;
    password.innerHTML = result;
}

// window.onload =function () {
//     onload_window_zmina = document.getElementById("zmina")
//     console.log(onload_window_zmina)
//     onload_window_zmina.innerHTML = "<h1>Hello world!!!<h1/>"
// }
//
// // window.onload = function (){
// //     let username= document.getElementById("zmina");
// //     let age= prompt("Скільки тобі років");
// //     let years= age * 2;
// //     let result= "Число" + years;
// //     username.innerHTML = result;
// // }
//
// window.onload = function (){
//     let password= document.getElementById("zmina_1");
//     let age= prompt("Enter your password");
//     let years= age * 2;
//     let result= "Число" + years;
//     password.innerHTML = result;
// }