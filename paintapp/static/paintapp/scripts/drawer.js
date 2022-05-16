class Drawer {
    constructor(canvas, temp_canvas, storage, def_tool, def_filling, supported_figures={}) {
        this.tool = def_tool;
        this.current_figure = null;
        this.temp_canvas = temp_canvas;
        this.main_canvas = canvas;
        this.figure_fill = def_filling;
        this.supported_figures = supported_figures;
        this.storage = storage;

        this.temp_ctx = temp_canvas.getContext('2d');
        this.real_ctx = canvas.getContext('2d');
    }

    set_filling(is_filled){
        this.figure_fill = is_filled;
    }

    set_tool(tool) {
        this.tool = tool;
    }

    is_supported(figure) {
        return figure in this.supported_figures;
    }

    handleEvent(event) {
        throw "Abstract method should be implemented";
    }

    save() {
        this.current_figure.set_colors(this.temp_ctx.stroke_color, this.temp_ctx.fill_color);

        // let figure_json = this.current_figure.get_json();
        // this.storage.add_figure(figure_json);
        this.storage.add_figure(this.current_figure);

        this.current_figure = null;

        this.real_ctx.drawImage(this.temp_canvas, 0, 0);
        this.temp_ctx.clearRect(0, 0, this.temp_canvas.width, this.temp_canvas.height);
    }

     create(mouseX, mouseY) {
        this.current_figure = new this.supported_figures[this.tool](
            this.temp_canvas,
            (mouseX - this.temp_canvas.offsetLeft),
            (mouseY - this.temp_canvas.offsetTop)
        );
        this.current_figure.set_fill(this.figure_fill);
    }

    draw(mouseX, mouseY) {
        if (!this.current_figure)
            return;
        let x = mouseX - this.temp_canvas.offsetLeft;
        let y = mouseY - this.temp_canvas.offsetTop;
        this.current_figure.redraw(x, y);
    }
}