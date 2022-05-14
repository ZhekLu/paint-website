const canvas = document.getElementById('canvas');
const temp_canvas = document.getElementById('pre_canvas')
const width_setter = document.getElementById("selclr");

let manager = new Manager(canvas, temp_canvas);
temp_canvas.addEventListener('mousedown', manager);
temp_canvas.addEventListener('mouseup', manager);
temp_canvas.addEventListener('mousemove', manager);
temp_canvas.addEventListener('dblclick', manager);

document.getElementById("background_color").oninput = function () {
    manager.set_color(this.value, true);
}
document.getElementById("line_color").oninput = function () {
    manager.set_color(this.value, false);
}
document.getElementById("fill_checker").onchange = function () {
    manager.set_filling(this.checked);
}

function width() {
    manager.set_width(width_setter.value);
}

function set_tool(tool) {
    manager.set_tool(tool);
}

function color (color_value){
    manager.set_color(color_value, true);
}

function reset (){
    manager.reset();
}

