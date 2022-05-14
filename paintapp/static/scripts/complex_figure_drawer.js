class ComplexFigureDrawer extends Drawer{
    constructor(canvas, temp_canvas, def_tool = 'polygon', def_filling = false) {
        super(canvas, temp_canvas, def_tool, def_filling);
    }

    handleEvent(event) {
        switch (event.type) {
            case 'mousedown':
                if (!this.current_figure) {
                    this.create(event.clientX, event.clientY);
                    break;
                }
            case 'mouseup':
                if (this.current_figure)
                    this.current_figure.fix();
                break;

            case 'mousemove':
                this.draw(event.clientX, event.clientY);
                break;

            case 'dblclick':
                this.save();
                break;
        }

    }

    create(mouseX, mouseY) {
        switch (this.tool) {
            case 'polygonal_chain':
                this.current_figure = new PolygonalChain(this.temp_canvas,
                    (mouseX - this.temp_canvas.offsetLeft),
                    (mouseY - this.temp_canvas.offsetTop)
                );
                break;
            case 'polygon':
                this.current_figure = new Polygon(this.temp_canvas,
                    (mouseX - this.temp_canvas.offsetLeft),
                    (mouseY - this.temp_canvas.offsetTop)
                );
                break;
        }
    }


}