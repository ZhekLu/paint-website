class Drawer {
    constructor(canvas, temp_canvas, def_tool, def_filling) {
        this.tool = def_tool;
        this.current_figure = null;
        this.temp_canvas = temp_canvas;
        this.main_canvas = canvas;
        this.figure_fill = def_filling;
    }

    set_filling(is_filled){
        this.figure_fill = is_filled;
    }

    set_tool(tool) {
        this.tool = tool;
    }

    handleEvent(event) {
        throw "Abstract method should be implemented";
    }

    save() {
        this.current_figure = null;
        // TODO!
    }

    draw(mouseX, mouseY) {
        if (!this.current_figure)
            return;
        let x = mouseX - this.temp_canvas.offsetLeft;
        let y = mouseY - this.temp_canvas.offsetTop;
        this.current_figure.redraw(x, y);
    }
}