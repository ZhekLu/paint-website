class Manager {
    constructor(canvas, temp_canvas, def_tool = 'line', def_filling = false) {
        this.tool = def_tool;
        this.current_figure = null;
        this.temp_canvas = temp_canvas;
        this.main_canvas = canvas;
        this.figure_fill = def_filling;

        this.simple_drawer = new SimpleFigureDrawer(canvas, temp_canvas);
        this.complex_drawer = new ComplexFigureDrawer(canvas, temp_canvas);
        this.current_drawer = null;
        this.set_tool(def_tool);
    }

    set_tool(tool) {
        this.tool = tool;
        this.current_drawer = this.is_simple()
            ? this.simple_drawer
            : this.complex_drawer;
        this.current_drawer.set_tool(tool);
    }

    set_color(color, is_fill=false) {
        if (is_fill)
            ctx.fillStyle = color;
        else
            ctx.strokeStyle = color;
    }

    set_filling(is_filled){
        this.figure_fill = is_filled;
        this.simple_drawer.set_filling(is_filled);
        this.complex_drawer.set_filling(is_filled);
    }

    handleEvent(event) {
        this.current_drawer.handleEvent(event);
    }

    is_simple() {
        return this.simple_drawer.is_supported(this.tool)
    }

}