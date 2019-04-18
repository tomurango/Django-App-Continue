function count_n() {
    var t_num = document.getElementById('num');
    t_num.textContent++;
    var num = t_num.textContent;
    var hid = document.getElementById("hid");
    hid.value = num;
}

function log_t() {
    var text = document.getElementById('run')
    var title = document.getElementById('d_title')
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


const time_dialog = new mdc.dialog.MDCDialog(document.querySelector('#time_dialog'));

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