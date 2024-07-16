const pass = document.getElementById("pass"),
      icon = document.querySelector(".bx");

icon.addEventListener("click", e =>{
    if(pass.type === "password"){
        icon.classList.remove("bx-show-alt")
        icon.classList.add("bx-hide")
        pass.type = "text"
    }
    else{
        icon.classList.remove("bx-hide")
        icon.classList.add("bx-show-alt")
        pass.type = "password"
    }
}
)