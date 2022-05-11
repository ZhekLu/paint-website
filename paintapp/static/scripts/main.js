const canvas = document.getElementById('canvas');
const temp_canvas = document.getElementById('pre_canvas')

const ctx = temp_canvas.getContext('2d');
ctx.lineWidth = 2;

let manager = new Manager(temp_canvas);
temp_canvas.addEventListener('mousedown', manager);
temp_canvas.addEventListener('mouseup', manager);
temp_canvas.addEventListener('mousemove', manager);


function set_tool(tool) {
    manager.set_tool(tool);
}

function color (color_value){
    ctx.strokeStyle = color_value;
    ctx.fillStyle = color_value;
}

function reset (){
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

