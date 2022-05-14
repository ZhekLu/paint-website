class Manager {
    constructor(canvas, temp_canvas, def_tool = 'line', def_filling = false) {
        this.simple_drawer = new SimpleFigureDrawer(canvas, temp_canvas);
        this.complex_drawer = new ComplexFigureDrawer(canvas, temp_canvas);
        this.current_drawer = null;

        this.ctx = temp_canvas.getContext('2d');
        this.res_ctx = canvas.getContext('2d');
        this.canvas = canvas;
        this.temp_canvas = temp_canvas;

        this.set_tool(def_tool);
        this.set_filling(def_filling);
    }

    set_tool(tool) {
        this.current_drawer = this.simple_drawer.is_supported(tool)
            ? this.simple_drawer
            : this.complex_drawer;
        this.current_drawer.set_tool(tool);
    }

    set_color(color, is_fill_color=false) {
        if (is_fill_color)
            this.ctx.fillStyle = color;
        else
            this.ctx.strokeStyle = color;
    }

    set_filling(is_filled) {
        this.simple_drawer.set_filling(is_filled);
        this.complex_drawer.set_filling(is_filled);
    }

    set_width(value) {
        // TODO!
    }

    reset() {
        this.ctx.clearRect(0, 0, this.temp_canvas.width, this.temp_canvas.height);
        this.res_ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }

    handleEvent(event) {
        this.current_drawer.handleEvent(event);
    }

}