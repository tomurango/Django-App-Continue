function count_n(){
    var t_num = document.getElementById('num');
    t_num.textContent++;
    var num = t_num.textContent;
    var hid = document.getElementById("hid");
    hid.value = num ;
}

function log_t(){
    var text=document.getElementById('run')
    var title=document.getElementById('d_title')
    if (text.textContent == 'START'){
        text.textContent = 'STOP';
        title.textContent = 'Stop Timer';
        timer=setInterval(count_n,1000);
    }else{
        text.textContent = 'START';
        title.textContent = 'Start Timer';
        clearInterval(timer)
        d()
    }
}

function rest_t(){
    var num = document.getElementById('num');
    num.textContent = 0;
}
