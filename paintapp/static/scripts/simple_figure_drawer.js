class SimpleFigureDrawer extends Drawer{
    constructor(canvas, temp_canvas, def_tool = 'line', def_filling = false) {
        super(canvas, temp_canvas, def_tool, def_filling);
        this.supported_figures = ['line', 'rectangle', 'circle'];
    }

    is_supported(figure) {
        return this.supported_figures.includes(figure);
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
        }
    }

}