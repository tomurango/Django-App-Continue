function count_n() {
    var t_num = document.getElementById('num');
    t_num.textContent++;
    var num = t_num.textContent;
    var hid = document.getElementById("hid");
    hid.value = num;
}


function log_t() {
    var text = document.getElementById('run');
    var title = document.getElementById('d_title');
    if (text.textContent == 'START') {
        text.textContent = 'STOP';
        title.textContent = 'Stop Timer';
        timer = setInterval(count_n, 1000);
    } else {
        text.textContent = 'START';
        title.textContent = 'Start Timer';
        clearInterval(timer)
        d()
    }
}

function rest_t() {
    var num = document.getElementById('num');
    num.textContent = 0;
}

const menu = new mdc.menu.MDCMenu(document.querySelector('.mdc-menu'));
function a() {
    menu.open = true;
}

const fabRipple = new mdc.ripple.MDCRipple(document.querySelector('.mdc-fab'));

const dialog = new mdc.dialog.MDCDialog(document.querySelector('#input_dialog'));
function b() {
    dialog.open()
}
dialog.listen('MDCDialog:closing', function () {
    document.forms.i_form.i_text.value="";
});

const alert_dialog = new mdc.dialog.MDCDialog(document.querySelector('#alert_dialog'));
alert_dialog.listen('MDCDialog:closing', function(){
});

const time_dialog = new mdc.dialog.MDCDialog(document.querySelector('#time_dialog'));
time_dialog.listen('MDCDialog:closing', function() {
    var number = document.getElementById('hid').value;
    if(number > 0){
        var text = document.getElementById('run');
        var title = document.getElementById('d_title');
        text.textContent = 'START';
        title.textContent = 'Start Timer';
        clearInterval(timer);
        alert_dialog.open();
    }else{
        try{
            var text = document.getElementById('run');
            var title = document.getElementById('d_title');
            text.textContent = 'START';
            title.textContent = 'Start Timer';
            clearInterval(timer);
        }catch{
            console.log('インターバル設定してないエラーだよ！');
        }
    }
});

function dont_delete() {
    alert_dialog.close();
    time_dialog.open();
}

function delete_data() {
    var number = document.getElementById('num');
    number.textContent = 0;
    var hid = document.getElementById("hid");
    hid.value = 0;
    alert_dialog.close();
    dialog.close();
}

var defau = document.getElementById("hide_what").value;

function c() {
    var text = document.forms.i_form.i_text.value;
    if (text.length >= 1) {
        document.getElementById("hide_what").value = text;
    } else {
        document.getElementById("hide_what").value = defau;
    }
    time_dialog.open()
}

const send_dialog = new mdc.dialog.MDCDialog(document.querySelector('#send_dialog'));

function d() {
    send_dialog.open()
}

const bar = new mdc.topAppBar.MDCTopAppBar(document.querySelector('.mdc-top-app-bar'));


mdc.autoInit()