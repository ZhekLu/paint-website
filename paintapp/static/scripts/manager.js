class Manager {
    constructor(canvas, temp_canvas, def_tool = 'line', def_filling = false) {
        this.tool = def_tool;
        this.current_figure = null;
        this.temp_canvas = temp_canvas;
        this.main_canvas = canvas;
        this.figure_fill = def_filling;
    }

    set_tool(tool) {
        this.tool = tool;
    }

    set_color(color, is_fill=false) {
        if (is_fill)
            ctx.fillStyle = color;
        else
            ctx.strokeStyle = color;
    }

    set_filling(is_filled){
        this.figure_fill = is_filled;
    }

    handleEvent(event) {
        switch (event.type) {
            case 'mousedown':
                this.create(event.clientX, event.clientY);
                break;

            case 'mouseup':
                this.save();
                break;

            case 'mousemove':
                this.draw(event.clientX, event.clientY);
                break;

            case 'dblclick':
                alert('double');
                break;
        }

    }

    create(mouseX, mouseY) {
        switch (this.tool) {
            case 'line':
                this.current_figure = new Line(this.temp_canvas,
                    (mouseX - this.temp_canvas.offsetLeft),
                    (mouseY - this.temp_canvas.offsetTop)
                );
                break;
            case 'rectangle':
                this.current_figure = new Rectangle(this.temp_canvas,
                    (mouseX - this.temp_canvas.offsetLeft),
                    (mouseY - this.temp_canvas.offsetTop),
                    true
                );
                break;
            case 'circle':
                this.current_figure = new Ellipse(this.temp_canvas,
                    (mouseX - this.temp_canvas.offsetLeft),
                    (mouseY - this.temp_canvas.offsetTop),
                    true
                );
                break;
            case 'polygonal_chain':
                break;
            case 'polygon':
                break;
        }
    }

    save() {
        this.current_figure = null;
    }

    draw(mouseX, mouseY) {
        if (!this.current_figure)
            return;
        let x = mouseX - this.temp_canvas.offsetLeft;
        let y = mouseY - this.temp_canvas.offsetTop;
        this.current_figure.redraw(x, y);
    }
}