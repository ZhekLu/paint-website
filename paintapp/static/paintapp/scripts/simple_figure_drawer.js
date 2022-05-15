class SimpleFigureDrawer extends Drawer{
    constructor(canvas, temp_canvas, def_filling = false, def_tool = 'line') {
        super(canvas, temp_canvas, def_tool, def_filling,
            {
                'line': Line,
                'rectangle': Rectangle,
                'circle': Ellipse
            });
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
}