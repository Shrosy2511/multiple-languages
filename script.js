var btn = document.createElement('button');
btn.style.margin = '10px';
btn.innerHTML = 'klik hier om de achtergrond aan te passen';
document.body.appendChild(btn);

// schijf hier tussen je code
btn.onclick = changecolor;
btnOnClick = 0
function changecolor(){
    if(btnOnClick == 0){
        document.body.style.backgroundColor = 'purple';
        btnOnClick += 1
        return false;
    }
    else if(btnOnClick == 1){
        document.body.style.backgroundColor = 'red';
        btnOnClick -= 1
        return false;        
    }
}

// schijf hier tussen je code