// import signal from 'signal-js'

const canvas = document.getElementById('canvas');
const temp_canvas = document.getElementById('pre_canvas')
let figures = document.getElementById('figure_list');


let manager = new Manager(canvas, temp_canvas, figures);
temp_canvas.addEventListener('mousedown', manager);
temp_canvas.addEventListener('mouseup', manager);
temp_canvas.addEventListener('mousemove', manager);
temp_canvas.addEventListener('dblclick', manager);

// let ctx = canvas.getContext('2d');
// for(let i = 0; i < temp_canvas.width; i += 10) {
//     ctx.fillRect(i, 200, 1, 50)
// }

document.getElementById("background_color").oninput = function () {
    manager.set_color(this.value, true);
}

document.getElementById("line_color").oninput = function () {
    manager.set_color(this.value, false);
}

document.getElementById("fill_checker").onchange = function () {
    manager.set_filling(this.checked);
}

document.getElementById("width_chooser").onchange = function () {
    if (this.validity.valid) {
        manager.set_width(this.value);
    }
}

let coords_shower = document.getElementById('coords');
document.onmousemove = function(e) { // shows mouse coordinates
    coords_shower.innerHTML = e.clientX + ':' + e.clientY;
};

function set_tool(tool) {
    manager.set_tool(tool);
}

function color (color_value){
    manager.set_color(color_value, true);
}

function reset (){
    manager.reset();
}

function figure_state_changed(id) {
    manager.figure_state_changed(id);
}

// function  update_figures() {
//     let list = manager.get_storage();
//     figures.innerHTML = "";
//     for (let i = 0; i < list.length; i++) {
//         let item = document.createElement('button');
//         item.textContent = 'OFOF';
//         figures.append(item);
//     }
// }


// document.addEventListener('mouseup', update_figures);
// document.addEventListener('mousedown', update_figures);
// signal.on('figure_list_changed', update_figures);


// plugin loading
// plug = document.createElement('script');
// plug.src = "{% static 'paintapp/scripts/plugin_trapezoid.js' %}"
// document.body.append(plug);
// let blob = new Blob(["It's ok."], {type: 'text/plain;charset=utf-8'});
// saveAs()
