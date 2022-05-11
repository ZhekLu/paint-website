class Manager {
    constructor(canvas, temp_canvas, def_tool = 'line') {
        this.tool = def_tool;
        this.rect = new RectangleTool(canvas, temp_canvas);
    }

    set_tool(tool) {
        this.tool = tool;
    }

    handleEvent(event) {
        switch (this.tool) {
            case 'rectangle':
                this.rect.handleEvent(event);
                break;
            case 'circle':
                break;
        }

    }
}