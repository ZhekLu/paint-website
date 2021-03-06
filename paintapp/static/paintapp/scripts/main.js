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

function save_picture() {
    let picture = manager.get_picture();
    download_json(picture, 'picture_paint_web');
}

function download_json(obj, name) {
    let data_str = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(obj));
    let download_node = document.createElement('a');
    download_node.setAttribute("href", data_str);
    download_node.setAttribute("download", name + ".json");
    document.body.appendChild(download_node);
    download_node.click();
    download_node.remove();
}

let loader = document.getElementById("file_selector");
function load_picture() {
    let file = loader.files[0];
    if(!file)
        return;
    let reader = new FileReader();
    reader.readAsText(file);
    reader.onload = function() {
        console.log(reader.result)
        let picture = JSON.parse(reader.result);
        try {
            manager.load_picture(picture);
        } catch (e) {
            alert('Error while loading picture :' + e.message);
        }
    };

    reader.onerror = function() {
        console.log(reader.error);
    };
}


// plugin loading
function load_plugin(src, plugin_name, but_name = 'PL') {
    let plug = document.createElement('script');
    plug.src = src;
    document.body.appendChild(plug);

    plug.addEventListener("load", () => {
        console.log("Plugin" + plugin_name + " loaded");
        manager.add_plugin(plugin_name);
        add_plugin_butt(plugin_name, but_name);
    });

    plug.addEventListener("error", (ev) => {
        console.log("Error on loading plugin ", plugin_name, ev);
    });

    function add_plugin_butt(plugin_name, but_name) {
        let div = document.getElementById('toolbox');
        let butt = document.createElement('button');
        butt.textContent = but_name;
        butt.className = 'button';
        butt.onclick = () => manager.set_tool(plugin_name);
        div.append(butt);
    }
}

// load_plugin('static/paintapp/plugins/plugin_trapezoid.js', 'TrapezoidPlugin', 'TR');
