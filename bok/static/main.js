function count_num(){
    var t_num = document.getElementById('timer');
    t_num.textContent++;
    var num = t_num.textContent;
    var hid = document.getElementById("hide");
    hid.value = num ;
}

function logt(){
    var text=document.getElementById('start')
    if (text.textContent == 'start'){
        text.textContent = 'stop';
        timer=setInterval(count_num,1000);
    }else{
        text.textContent = 'start';
        clearInterval(timer)
    }
}

function rest(){
    var num = document.getElementById('timer');
    num.textContent = 0;
}