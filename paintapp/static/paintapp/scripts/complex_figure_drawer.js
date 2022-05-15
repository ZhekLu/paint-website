class ComplexFigureDrawer extends Drawer{
    constructor(canvas, temp_canvas, def_filling = false, def_tool = 'polygon') {
        super(canvas, temp_canvas, def_tool, def_filling,
            {
                'polygon':Polygon,
                'polygonal_chain':PolygonalChain
            });
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
}