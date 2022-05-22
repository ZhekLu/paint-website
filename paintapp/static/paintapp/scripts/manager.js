class Manager {
    constructor(canvas, temp_canvas, view_presenter, start_picture = [],
                def_tool = 'line', def_filling = false, def_line_width = 2) {
        this.current_picture = new FigureManager(view_presenter, start_picture);

        this.simple_drawer = new SimpleFigureDrawer(canvas, temp_canvas, this.current_picture);
        this.complex_drawer = new ComplexFigureDrawer(canvas, temp_canvas, this.current_picture);
        this.current_drawer = null;

        this.ctx = temp_canvas.getContext('2d');
        this.res_ctx = canvas.getContext('2d');
        this.canvas = canvas;
        this.temp_canvas = temp_canvas;

        this.set_tool(def_tool);
        this.set_filling(def_filling);
        this.set_width(def_line_width);
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
        this.ctx.lineWidth = value;
    }

    reset() {
        this.ctx.clearRect(0, 0, this.temp_canvas.width, this.temp_canvas.height);
        this.res_ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        this.current_picture.clear();
    }

    handleEvent(event) {
        this.current_drawer.handleEvent(event);
    }

    get_storage() {
        return this.current_picture.get_storage();
    }

    figure_state_changed(id) {
        this.current_picture.figure_state_changed(id);
        this.redraw_all_figures();
    }

    redraw_all_figures() {
        this.res_ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        let figures = this.current_picture.get_storage();
        for (let i = 0; i < figures.length; i++) {
            let curr = figures[i];
            if (!curr.deleted)
                curr.object.restore(this.res_ctx);
        }
    }

    get_picture() {
        let figures = this.current_picture.get_storage();
        let file_picture = [];
        for (let i = 0; i < figures.length; i++) {
            let curr = figures[i];
            if (!curr.deleted)
                file_picture.push(curr.object.get_json());
        }
        return file_picture;
    }

    load_picture(picture) {
        this.reset();
        for(let i = 0; i < picture.length; i++) {
            let figure_json = picture[i];
            let figure = eval(String('new ' + figure_json.type + '(this.canvas)'));
            figure.load_params_from_json(picture[i]);
            this.current_picture.add_figure(figure);
        }
        this.redraw_all_figures();
    }

    add_plugin(plugin, is_simple = true) {
        if(is_simple)
            this.simple_drawer.add_plugin(plugin);
        else
            this.complex_drawer.add_plugin(plugin);
    }

}