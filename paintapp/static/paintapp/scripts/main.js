const canvas = document.getElementById('canvas');
const temp_canvas = document.getElementById('pre_canvas')


let manager = new Manager(canvas, temp_canvas);
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

